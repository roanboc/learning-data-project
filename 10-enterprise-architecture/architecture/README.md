# Architecture — the university, for the questions its data answers

_The front door of this model. This folder's rules: [`AGENTS.md`](../AGENTS.md)._

What the university knows about itself, for the questions its data has to
answer: who asks them, what it must be able to do, who takes part, which
information it holds, and which software records and serves it.

**Federation ID:** `UNI`. Data governance's map cites this model's elements as
`UNI.<ID>`. Every relationship between peers is declared once, in
[`relationships.md`](./relationships.md).

## What is modeled, and what is not

```mermaid
flowchart TB
  subgraph here["Modeled in this tree"]
    l1["1 · Strategy — the questions, the goals, every area and the capabilities they need"]:::strategy
    l2["2 · Business — who takes part, and one service per answer"]:::business
    l3["3 · Information — every data domain, and the objects the questions need"]:::info
    l4["4 · Application — the systems, the data team's tools, the agents"]:::app
    l5["5 · Technology — where an answer depends on where it runs"]:::tech
  end

  gov["Data governance's map — its services, roles and steps in detail"]:::ext
  gap["— · Transition — a stated gap, not a silence"]:::gap

  l1 -->|is realized by| l2
  l2 -->|acts on| l3
  l2 -->|its services run on| l4
  l4 -->|runs on| l5
  l2 -.->|governance's part, in detail| gov
  l1 -.->|no roadmap confirmed yet| gap

  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef app fill:#9adcf0,stroke:#0288d1,color:#333
  classDef tech fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
  classDef gap fill:#ffd6d6,stroke:#c62828,color:#333,stroke-dasharray: 4 3
```

Wide at the top, narrow below. Every area and every data domain of the
university is named; below them, only what one of the questions in
[Motivation](./1_strategy/1_motivation.md) needs. The dashed boxes are where
the model stops: data governance details its own part, and no roadmap has
been confirmed.

| # | Layer | The question it answers | Status |
| - | ----- | ----------------------- | ------ |
| 0 | Business design | Who are the customers, and how does each offering pay? | `Out of scope` — the questions are about the university's data, not its business model |
| 1 | [Strategy](./1_strategy/README.md) | Why does this exist, and what must it be able to do? | `Local` — the questions as drivers; every area at level 1 |
| 2 | [Business](./2_business/README.md) | Who does what, and which services are offered? | `Local` — actors and one service per answer; governance's roles and steps are `External` — owned by `20-data-governance/3-architecture-map/` |
| 3 | [Information](./3_information/README.md) | What information exists, and where does it live? | `Local` — every data domain, and the objects the questions need; their governance is `External` — owned by `20-data-governance/9-information-assets/` |
| 4 | [Application](./4_application/README.md) | Which software realizes each business service? | `Local` — the register |
| 5 | [Technology](./5_technology/README.md) | What runs it all? | `Local` — two nodes |
| — | Transition | Where is this going, and in what order? | `Gap` — current state only |

Domains stay unused at Depth 2; see [`AGENTS.md`](../AGENTS.md).

## How far each document has been validated

| Mark | Meaning |
| ---- | ------- |
| `○` | Not started — the document exists so the gap is visible |
| `◐` | Draft catalogue — identified and written down; nobody has confirmed it |
| `●` | Validated — the Requester has read it and stands behind it, since a date |

Every document is `◐` today: the university and its people are fictional, so
nobody can confirm it but the author of the films.
