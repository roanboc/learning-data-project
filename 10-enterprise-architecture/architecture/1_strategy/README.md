# Strategy & Motivation Layer

_[← Front door](../README.md)_

Who has a stake in the university's data, the questions they ask, and what the
university must be able to do to answer them.

**ArchiMate viewpoint:** Motivation and Strategy: Stakeholder, Driver, Goal,
Outcome, Principle, Capability.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [1_motivation.md](./1_motivation.md) | Stakeholders, Drivers, Goals, Outcomes, Principles | Who asks which question, and what must be true for the answers to hold? |
| 2 | [2_capabilities.md](./2_capabilities.md) | Capabilities, every area at level 1 and level 2 only where a question needs it | What must the university be able to do to answer them? |
| 3 | Value stream | — | Not started: no question here needs one yet |

## Metamodel

```mermaid
flowchart LR
  %% legend
  stk(["◍ «Stakeholder» who asks [STK#]"]):::stakeholder
  drv{{"✳ «Driver» the question they ask [DRV#]"}}:::driver
  g("◎ «Goal» what must become true [G#]"):::goal
  out[["◉ «Outcome» how we know, checked [OUT#]"]]:::outcome
  p[/"⚑ «Principle» what constrains how [P#]"/]:::principle
  cap1["✦ «Capability» level 1, an area [CAP#]"]:::strategy1
  cap2["✦ «Capability» level 2, only where needed [CAP#.#]"]:::strategy

  stk -->|concerned with| drv
  drv -->|influences| g
  g -->|realized by| out
  p -->|constrains| g
  cap1 -->|composed of| cap2
  drv -->|needs| cap2

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef goal fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef outcome fill:#c9b1ea,stroke:#6a46b0,color:#333
  classDef principle fill:#efe6fa,stroke:#9575cd,color:#333
  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef strategy1 fill:#eed4a0,stroke:#c8a24a,color:#333
```

Purple is Motivation and tan is Strategy; the darker tan marks a level-1
capability.

## Layer view

```mermaid
flowchart LR
  d1{{"✳ Who is near a graduate certificate [DRV1]"}}:::driver
  d6{{"✳ What does casual teaching cost [DRV6]"}}:::driver
  g1("◎ One learner, one record [G1]"):::goal
  g2("◎ Every measure defined once [G2]"):::goal
  c13["✦ Learner records and credentials [CAP1.3]"]:::strategy
  c41["✦ Planning and census reporting [CAP4.1]"]:::strategy
  c61["✦ Cost reporting [CAP6.1]"]:::strategy
  c71["✦ Data governance [CAP7.1]"]:::strategy

  d1 -->|influences| g1
  d6 -->|influences| g2
  d1 -->|needs| c41
  d1 -->|needs| c13
  d6 -->|needs| c61
  d6 -->|needs| c71

  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef goal fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
```

The two questions that started the project: Planning's count, which needs one
learner across every system, and the cost three teams called by one name,
which needs a measure defined once.
