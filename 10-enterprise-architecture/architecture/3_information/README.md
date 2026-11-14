# Information Layer

_[← Front door](../README.md)_

The university's data domains and the objects inside them that the questions need.

**ArchiMate viewpoint:** Information: Data Object, a domain at level 1 and an object at level 2.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [1_data-domains-and-objects.md](./1_data-domains-and-objects.md) | Data domains, every one; data objects, only where a question needs them | What information exists, who owns it, and where is it first recorded? |
| 2 | Classification and retention | — | Not started here: each object's class and level are data governance's, in `20-data-governance/9-information-assets/` |

## Metamodel

```mermaid
flowchart LR
  %% legend
  domain["▦ «Data Object» a domain, every one [DOBJ#]"]:::application1
  obj["▦ «Data Object» only what a question needs [DOBJ#.#]"]:::application
  sys["⊞ «Application Component» where it is first recorded [ACMP#]"]:::app

  domain -->|aggregates| obj
  sys -->|accesses| obj

  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef application1 fill:#9adcf0,stroke:#0288d1,color:#333
  classDef app fill:#e8f7fd,stroke:#0288d1,color:#333
```

The darker cyan marks a data domain; the pale box is a system visiting from the Application layer.

## Layer view

```mermaid
flowchart LR
  d2["▦ Student [DOBJ2]"]:::application1
  o21["▦ Learner [DOBJ2.1]"]:::application
  o23["▦ Credit towards an award [DOBJ2.3]"]:::application
  d3["▦ Course [DOBJ3]"]:::application1
  o31["▦ Award [DOBJ3.1]"]:::application

  d2 -->|aggregates| o21
  d2 -->|aggregates| o23
  d3 -->|aggregates| o31
  o23 -->|towards| o31

  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef application1 fill:#9adcf0,stroke:#0288d1,color:#333
```

Planning's question in data: a learner's credit, counted towards an award.
