# Metrics

Each measure the university agrees, defined once, in Apache Ossie 0.1.1, the open, tool-neutral format
for semantic models (called Open Semantic Interchange, OSI, until July 2026). Its schema is in
`../7-standards/`.

| File | Measures | Owners |
|---|---|---|
| `learners_near_an_award.ossie.yaml` | learners near a graduate certificate; credit points towards an award | Clara Jensen, Planning |
| `casual_staff_costs.ossie.yaml` | casual teaching cost; casual pay paid | Rohan Desai, Finance; Ingrid Holm, HR |

A measure is defined here by its owner, in the glossary's words, before any tool builds it. Each tool
then builds its own version from this one: the dbt project's MetricFlow metrics (the `DBT` extension
says which measure, aggregation and filter) and Unity Catalog's metric views (the `DATABRICKS` dialect
is the view's expression). No converter does that build yet for these two tools, so the data project's
`scripts/check/from_governance.py` holds them together, and fails on a metric it builds that isn't
defined here, or is built differently.

`../scripts/check.py` validates every file against the schema, and fails on a measure defined twice or
one with no owner.
