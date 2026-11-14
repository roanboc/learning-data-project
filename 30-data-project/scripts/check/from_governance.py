"""Checks the project against what data governance defines, in ../20-data-governance/.

- Every metric the project builds is defined there once, in Apache Ossie (11-metrics/*.ossie.yaml): each
  MetricFlow metric in models/**/_*__semantic.yml names the same measure, aggregation and filter as its
  definition's DBT extension, and each measure of a Unity Catalog metric view (a model materialized as
  metric_view) has the same expression as its definition's DATABRICKS dialect. A metric here with no
  definition there fails: a measure is defined once, by its owner, and built from that definition.
- The example export of the platform's glossary (skills/sync-the-glossary/example_glossary.json) holds the
  same terms, definitions and owners as the business glossary, 1-glossary/business-glossary.yml.

The project reads governance's files; governance never reads the project's.

    python scripts/check/from_governance.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE = ROOT.parent / "20-data-governance"
EXPORT = ROOT / "skills" / "sync-the-glossary" / "example_glossary.json"


def flat(text):
    return " ".join(str(text).split())


def definitions():
    """Every metric governance defines, by name: its document, its dialects and its extensions."""
    found = {}
    for doc in sorted((GOVERNANCE / "11-metrics").glob("*.ossie.yaml")):
        for model in (yaml.safe_load(doc.read_text()) or {}).get("semantic_model") or []:
            for metric in model.get("metrics") or []:
                dialects = {d["dialect"]: flat(d["expression"]) for d in metric["expression"]["dialects"]}
                extensions = {e["vendor_name"]: json.loads(e["data"]) for e in metric.get("custom_extensions") or []}
                found[metric["name"]] = dict(doc=doc.name, dialects=dialects, extensions=extensions)
    return found


def check_metricflow(defined, problems):
    for path in sorted((ROOT / "models").rglob("_*__semantic.yml")):
        body = yaml.safe_load(path.read_text()) or {}
        measures = {m["name"]: m for sm in body.get("semantic_models") or [] for m in sm.get("measures") or []}
        for metric in body.get("metrics") or []:
            where = f"{path.relative_to(ROOT)}: {metric['name']}"
            definition = defined.get(metric["name"])
            if definition is None:
                problems.append(f"{where} isn't defined in ../20-data-governance/11-metrics/: its owner defines it there first")
                continue
            dbt = definition["extensions"].get("DBT")
            if dbt is None:
                problems.append(f"{where}: its definition, {definition['doc']}, has no DBT extension to build it from")
                continue
            measure = (metric.get("type_params") or {}).get("measure")
            if measure != dbt.get("measure"):
                problems.append(f"{where} counts {measure!r}; its definition counts {dbt.get('measure')!r}")
            if measures.get(measure, {}).get("agg") != dbt.get("agg"):
                problems.append(f"{where} aggregates by {measures.get(measure, {}).get('agg')!r}; its definition by {dbt.get('agg')!r}")
            text = flat(metric.get("filter", ""))
            for condition in dbt.get("filter") or []:
                column, _, value = condition.partition(" = ")
                if f"__{column}')" not in text or (value and value not in text):
                    problems.append(f"{where}'s filter doesn't hold {condition!r}, as its definition does")


def check_metric_views(defined, problems):
    for path in sorted((ROOT / "models").rglob("*.sql")):
        text = path.read_text()
        if "materialized='metric_view'" not in text:
            continue
        body = yaml.safe_load(re.sub(r"\{\{.*?\}\}|\{#-?.*?-?#\}", "", text, flags=re.S).replace('""', '"x"')) or {}
        for measure in body.get("measures") or []:
            where = f"{path.relative_to(ROOT)}: {measure['name']}"
            definition = defined.get(measure["name"])
            if definition is None:
                problems.append(f"{where} isn't defined in ../20-data-governance/11-metrics/: its owner defines it there first")
            elif flat(measure["expr"]) != definition["dialects"].get("DATABRICKS"):
                problems.append(f"{where}: {flat(measure['expr'])!r} differs from its definition in {definition['doc']}, "
                                f"{definition['dialects'].get('DATABRICKS')!r}")


def check_glossary(problems):
    glossary = {t["term"]: t for t in yaml.safe_load((GOVERNANCE / "1-glossary" / "business-glossary.yml").read_text())["terms"]}
    export = {t["term"]: t for t in json.loads(EXPORT.read_text())["terms"]}
    for term in sorted(set(glossary) | set(export)):
        mine, theirs = glossary.get(term), export.get(term)
        if mine is None or theirs is None:
            problems.append(f"glossary: {term!r} is in {'the export' if mine is None else 'the business glossary'} only")
        elif (flat(mine["definition"]), mine["owner"]) != (flat(theirs["definition"]), theirs["owner"]):
            problems.append(f"glossary: {term!r} differs between the business glossary and the export")


def main():
    problems = []
    defined = definitions()
    check_metricflow(defined, problems)
    check_metric_views(defined, problems)
    check_glossary(problems)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print(f"every metric the project builds is defined once in governance's {len(defined)}, "
          "and the glossary export matches the business glossary")


if __name__ == "__main__":
    main()
