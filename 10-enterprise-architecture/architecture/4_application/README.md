# Application Layer

_[← Front door](../README.md)_

Which software records the data and serves each business service.

**ArchiMate viewpoint:** Application usage: Application Component.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [1_realization-register.md](./1_realization-register.md) | Application components: the systems, the data team's tools, the agents | Which software serves each answer, and where is it specified? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  svc(["⬭ «Business Service» what it serves [BSVC#]"]):::business
  app["⊞ «Application Component» the software [ACMP#]"]:::application
  ai["⊞ «Application Component» an agent [ACMP#]"]:::ai

  app -->|serves| svc
  ai -->|drafts in| app

  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef ai fill:#7fd6f2,stroke:#0277bd,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

The darker cyan marks an agent; the yellow service visits from the Business layer.

## Layer view

```mermaid
flowchart LR
  a1["⊞ Student system [ACMP1]"]:::application
  p["⊞ Data platform [ACMP12]"]:::application
  d["⊞ dbt project [ACMP13]"]:::application
  s1(["⬭ Learners near an award [BSVC1]"]):::business

  a1 -->|flows to| p
  d -->|runs on| p
  d -->|serves| s1

  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

The student system's data lands on the platform, where the dbt project builds Planning's answer.
