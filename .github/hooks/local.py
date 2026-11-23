"""learning-data-project's own rules for .github/hooks/guard.py (the guard itself is the same file in roanboc/learning-data).

They hold 30-data-project/AGENTS.md: an agent runs dbt on the development target only, never writes to production, works with
samples of at most 20 rows, never weakens a test, and never writes a credential. A problem that starts with "!" fails GitHub's
check; the others warn there. In Claude Code every problem is fed back after the edit.
"""
import re

_WRITES = r"dbt\s+(?:run|build|seed|snapshot|run-operation|retry|clone)\b"

BASH_RULES = [
    (_WRITES + r"[^;&|\n]*(?:--target|-t)[ =](?!duckdb\b)\S+",
     "dbt writes only to the development target here: run it on duckdb (dbt build --profiles-dir .). Agents never change "
     "production; on Databricks a build runs as the agent's own service principal, in its own development schema, from its "
     "workflow (30-data-project/AGENTS.md). `dbt parse --target databricks` is fine: it connects to nothing."),
    (r"dbt\s+show\b[^;&|\n]*--limit[ =](?:-1\b|0*(?:2[1-9]|[3-9]\d|\d{3,}))",
     "Samples are at most 20 rows (dbt show --limit 20); work with counts and aggregates, never bulk personal data."),
    (r"databricks\s+(?:bundle\s+(?:deploy|run|destroy)|jobs\s+(?:run-now|submit|create|reset|delete)|"
     r"pipelines\s+(?:start-update|create|update|delete)|api\s+(?:post|put|patch|delete)|fs\s+(?:rm|cp|mv)|"
     r"tables\s+delete|schemas\s+(?:create|delete|update)|grants\s+update)\b",
     "Nothing here changes Databricks: a change reaches the platform only as a pull request a person reviews, and the release "
     "makes it. Read with limited, masked access."),
]

LONG_RUNS = []

TRIM = [r"\bdbt\s+(?:build|test|run|parse|compile|docs)\b", r"scripts/check/", r"scripts/generate/\S+\s+--check",
        r"scripts/check\.py", r"python3?\s+-m\s+unittest", r"\bpytest\b"]

PROTECTED = [
    (["30-data-project/target/*", "*/dbt_packages/*", "*/logs/*", "*.duckdb"], "deny",
     "dbt's output: dbt writes it; change the models and build again."),
]

BUILT = ["30-data-project/target/*", "*/dbt_packages/*", "*/logs/*", "*.duckdb"]

MERGE_NEEDS_LATEST_MAIN = False

SUMMARY = """
Hooks in .github/hooks/ enforce (README there): no force-push or push to main; no Claude trailers in commits or squash
messages; squash merges only; dbt writes only on the duckdb target (never production; dbt parse --target databricks is
fine); samples of at most 20 rows; no Databricks changes from here; no secrets (profiles.yml reads env_var); generated files
only by their generator (CODEOWNERS, product descriptors...); no whole reads of target/ or files over 300 KB. After an edit:
a weakened test (severity warn, enabled false, a new where, warn_if, error_if) or a new model without its YAML is fed back.
"""

WEAKEN = re.compile(r"severity:\s*['\"]?warn|enabled:\s*false|\bwarn_if:|\berror_if:|^\s*where:|store_failures:\s*false", re.I | re.M)
LITERAL_SECRET = re.compile(r"^\s*(token|password|client_secret|secret|private_key|api_key)\s*:\s*(?!['\"]?\{\{)(?!\s*$)\S+", re.I | re.M)


def check_file(rel, before, after):
    problems = []
    name = rel.rsplit("/", 1)[-1]
    if name in ("profiles.yml", "databricks.yml") or rel.endswith((".yml", ".yaml")) and "/agents/" in rel:
        for m in LITERAL_SECRET.finditer(after):
            problems.append(f"!{m.group(1)} has a literal value: read it with {{{{ env_var('...') }}}}, never write a credential")
    if rel.startswith("30-data-project/") and rel.endswith((".yml", ".yaml")) and ("/models/" in rel or "/tests/" in rel or "/sources/" in rel):
        added = len(WEAKEN.findall(after)) - len(WEAKEN.findall(before))
        entries = lambda t: len(re.findall(r"^\s*-\s+(?:\w+\.)?\w+", t, re.M))
        # a new test may carry its own where or severity; a weakener with no new entry beside it narrows a test that was there
        if before and added > max(0, entries(after) - entries(before)):
            problems.append("tests weakened: a new severity warn, enabled false, where, warn_if or error_if. Don't weaken a test to make "
                            "it pass: report the failing rows and propose a fix to the data or the code (30-data-project/AGENTS.md)")
        tests_then, tests_now = entries(before), entries(after)
        if before and tests_now < tests_then - 2:
            problems.append(f"{tests_then - tests_now} list entries (tests or columns) fewer than before: if a test was removed, say why in the pull request")
    if re.match(r"30-data-project/models/.+\.sql$", rel) and not before:
        import pathlib
        root = pathlib.Path(__file__).resolve().parents[2]
        model = name[:-4]
        folder = (root / rel).parent
        if not any(model in y.read_text(encoding="utf-8", errors="replace") for y in list(folder.glob("*.yml")) + list(folder.glob("*.yaml"))):
            problems.append(f"new model {model} has no YAML beside it: describe it, its owner, its columns and their tests in the folder's _<folder>__models.yml")
    return problems


def stop_checks(files):
    notes = []
    if any(f.startswith("30-data-project/models/") for f in files):
        notes.append("Models changed: before the pull request, run dbt build --profiles-dir . and the --check scripts "
                     "(30-data-project/AGENTS.md, Before you open a pull request), and put impact.py --base origin/main's output in it.")
    return notes
