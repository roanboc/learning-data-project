# Technology Layer

_[← Front door](../README.md)_

Where the data runs, only where an answer depends on it.

**ArchiMate viewpoint:** Technology: Node.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [1_platforms.md](./1_platforms.md) | Nodes | Where does it run, and why does the business care? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  node["⬒ «Node» where it runs [NODE#]"]:::technology
  app["⊞ «Application Component» what runs there [ACMP#]"]:::application

  app -->|runs on| node

  classDef technology fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
```

Green is Technology; the cyan component visits from the Application layer.

## Layer view

```mermaid
flowchart LR
  n1["⬒ Databricks workspace, with Unity Catalog [NODE1]"]:::technology
  n2["⬒ DuckDB, on a laptop or in CI [NODE2]"]:::technology

  classDef technology fill:#c9e7b7,stroke:#558b2f,color:#333
```

Two places, one codebase.
