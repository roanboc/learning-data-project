# AGENTS.md

The enterprise architecture of the fictional university behind the Learning
Data films, written with [ArChreator](https://github.com/roanboc/archreator):
plain Markdown, six layers, ArchiMate's elements drawn in Mermaid.

At a real university this is the enterprise architecture team's, and it
usually lives in an architecture tool, or a repository of its own. It sits
here, beside data governance and the data project, so that people and agents
can read all three in one place.

## Modeling depth

**Declared depth: 2 — Organization.** One university, modelled for the
questions its data answers. Every level-1 capability area and every data
domain is named, so the map is whole; below level 1, only what a question in
[`architecture/1_strategy/1_motivation.md`](./architecture/1_strategy/1_motivation.md)
needs. A new question comes from Analytics' records
([`../00-initiatives/`](../00-initiatives/README.md)): it adds a driver of the same number first, then only the capabilities,
services, objects and systems it needs. Domains (`architecture/domains/`) stay
unused.

## Who decides

| Role | Who | Does |
| ---- | --- | ---- |
| **Requester** | Noor, the data architect, for the university (in the films) | Says what should change and confirms what the model claims |
| **Agent** | An AI agent, or a person | Works the change through the layers and opens a pull request |
| **Reviewer** | The data architect | Reviews and merges (`.github/CODEOWNERS`) |

## This tree

- **Federation ID:** `UNI`.
- **Links point one way.** This model names data governance's map and the
  data project's folders as where things are realized; neither of them is
  needed to read it, and nothing here is copied from them. Each driver's question is copied from Analytics' records in
  `../00-initiatives/`, and `scripts/check_questions.py` fails if the two differ.
- Relationships between peers are in
  [`architecture/relationships.md`](./architecture/relationships.md); the
  others are the catalogues' columns.
- The validators, from this folder, before every push:

```bash
python3 scripts/check_links.py
python3 scripts/check_model.py
python3 scripts/check_prose.py
python3 scripts/check_questions.py
```

The first three came with ArChreator's scaffold, unchanged (MIT licence); `check_questions.py` is this project's.

## Delivery

**Delivery framework:** the data project, `../30-data-project/`, with its own
`AGENTS.md`. The model says *that* a service exists and what realizes it; how
it is built is the data project's.
