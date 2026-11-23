# AGENTS.md

Where a question starts, then three folders, each a team's, each with its own `AGENTS.md`. Read the root README first, then the
`AGENTS.md` of the folder you change: its rules win inside it.

| Folder | Its rules |
|---|---|
| `00-initiatives/` | [AGENTS.md](00-initiatives/AGENTS.md): Analytics' questions, the initiatives' tickets and each goal's tree of questions; a question starts here |
| `10-enterprise-architecture/` | [AGENTS.md](10-enterprise-architecture/AGENTS.md): ArChreator's method; a change is aligned through the layers |
| `20-data-governance/` | [README.md](20-data-governance/README.md): who writes each folder, and the check |
| `30-data-project/` | [AGENTS.md](30-data-project/AGENTS.md): how the data team works, what agents may do |

## Rules for the whole repository

- **Wide at the top, only what is needed below.** Every capability area and data domain is named; below
  them, only what a question in `00-initiatives/analytics-questions.md` needs. A new question starts there,
  and the architecture records it as a driver of the same number.
- **Links point one way.** The data project reads governance; governance cites the architecture; the
  architecture copies Analytics' questions, with a check. No check in 00 reads anything, none in 10 reads 20 or
  30, and none in 20 reads 30.
- **One home for every artifact.** A definition lives in one folder; another keeps a copy only with a check
  that fails on drift. A measure is defined once, in `20-data-governance/11-metrics/`, in Apache Ossie.
- **Open standards.** Data products in the Open Data Product Standard, enterprise contracts in the Open Data
  Contract Standard, metrics in Apache Ossie; their schemas in `20-data-governance/7-standards/`.
- **Contracts change additively first**; a breaking change is a new version.
- **Tool-neutral where the films are.** Master data rules name no product.
- **Agents never change production**, and read it with personal and sensitive data masked.
- **Keep cited lines in place.** The films cite files here by path and line: append or replace in place.
- **A fictional world.** Organisations, people and numbers are invented.

## Checks

Before every push, the checks in the root README's *Check it*; CI runs the same.

## Hooks

`.claude/settings.json` runs `.github/hooks/guard.py` before and after Claude Code's tools, and GitHub's *Guards* check runs
the same rules on every change: no force-push or push to main, no Claude trailers, squash merges, dbt writes only on the
duckdb target, samples of at most 20 rows, nothing that changes Databricks, no secrets, no hand edits of generated files, and
a weakened test fed back. A refusal says what to do instead ([.github/hooks/README.md](.github/hooks/README.md)).
