# Business Layer

_[← Front door](../README.md)_

Who takes part in answering the university's questions, and the services that hand each answer over.

**ArchiMate viewpoint:** Business: Business Actor, Business Service.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [1_actors-and-services.md](./1_actors-and-services.md) | Actors, people and AI agents; business services | Who answers for what, and which service hands over each answer? |
| 2 | Process map | — | Not started: the steps of governance's services are on its own map, `20-data-governance/3-architecture-map/3-business/process-steps/` |

## Metamodel

```mermaid
flowchart LR
  %% legend
  act["⚇ «Business Actor» a person or a team (Human) [ACT#]"]:::business
  ai["⚇ «Business Actor» an AI agent (AI) [ACT#]"]:::ai
  svc(["⬭ «Business Service» an answer handed over [BSVC#]"]):::business
  cap["✦ «Capability» what it realizes [CAP#.#]"]:::strategy

  act -->|is served by| svc
  svc -->|realizes| cap

  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef ai fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
```

Yellow is Business, cyan an AI actor, and tan the capability a service realizes, visiting from Strategy.

## Layer view

```mermaid
flowchart LR
  a1["⚇ Planning (Human) [ACT1]"]:::business
  a10["⚇ Data team (Human) [ACT10]"]:::business
  a12["⚇ Planning agent (AI) [ACT12]"]:::ai
  s1(["⬭ Learners near an award [BSVC1]"]):::business
  s11(["⬭ Data products, built and released [BSVC11]"]):::business

  a1 -->|is served by| s1
  s11 -->|serves| s1
  a10 -->|assigned to| s11
  a12 -->|drafts for| a10

  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef ai fill:#c2f0ff,stroke:#0288d1,color:#333
```

Planning's answer reaches it as a service; the data team builds it, and the planning agent drafts changes a person approves.
