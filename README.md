# The university's data, end to end

The example behind the [Learning Data](https://data.learn-all.org/) films: one fictional university, from
why its data matters to the code that answers its questions. Three folders, in the order to read them:

| Folder | Whose it is, usually | What it holds |
|---|---|---|
| [`10-enterprise-architecture/`](10-enterprise-architecture/README.md) | The enterprise architecture team, in an architecture tool | Who asks which question, what the university must be able to do, who takes part, which information it holds, which systems record it. Written with [ArChreator](https://github.com/roanboc/archreator) |
| [`20-data-governance/`](20-data-governance/README.md) | Data governance, in a catalogue, a glossary tool or a suite of them | The business glossary, owners, the governance part of the map, information assets, data products and contracts in open standards, matrices, agent mandates, metrics in Apache Ossie |
| [`30-data-project/`](30-data-project/README.md) | The data team, in its own repository | The dbt project that builds and tests every answer; it runs on a laptop with DuckDB and on Databricks |

## Why three folders in one repository

At a real organisation these are usually separate repositories, owned by different teams, or whole
applications and suites: an architecture tool, a governance catalogue, a code repository. They are here
side by side for two reasons.

- **The least that has to exist.** A small organisation may have no enterprise architecture tool or team,
  and no data governance tool or team. These folders show the minimum to write down when nothing else
  exists, and each one is enough on its own.
- **Agents can read it all.** Plain files in one repository are easy for an AI agent to walk: from a
  question in the architecture's motivation, to the information asset and its owner in governance, to the
  model and its test in the data project, with no tool to sign in to.

Each folder stands alone: its own README, `AGENTS.md`, checks and owners (`.github/CODEOWNERS`), so a team
could lift it into a repository of its own unchanged.

## Wide at the top, only what is needed below

The architecture names every area of the university and every data domain, so the map is whole. Below
that it holds only what one of the questions in its motivation needs: Planning's count of learners near
a graduate certificate, the learner's wallet, tuition saved by recognised credit, the graduation list,
pay on Thursday, casual teaching cost, who teaches this term, short-course follow-ups and what an agent
may do alone. A new question adds a driver first, then only what it needs, in each folder in turn.

## Links point one way

A check or a build only ever reads in one direction: the data project reads governance's files, and
governance cites the architecture's elements. The architecture names where each thing is realized, as an
address, but reads nothing from the other two, so each team can change its own folder without breaking
another's checks.

## Check it

```bash
(cd 10-enterprise-architecture && python3 scripts/check_links.py && python3 scripts/check_model.py && python3 scripts/check_prose.py)
(cd 20-data-governance && pip install pyyaml jsonschema && python scripts/check.py --check)
(cd 30-data-project && pip install -r requirements.txt && dbt build --profiles-dir .)
```

CI runs all three on every pull request (`.github/workflows/`).

The university, its people and its data are fictional. Code: MIT licence ([LICENSE](LICENSE)). Text:
CC BY 4.0 ([LICENSE-CONTENT.md](LICENSE-CONTENT.md)).
