# Relationships

_[← Front door](./README.md)_

The relationships between peers that no catalogue column carries, declared once. The other relationships are the catalogues' own columns: `Needed by`, `Served by`, `Answers`, `Realizes`, `For`, `Serves` and `Recorded first in`.

## Layer 1 — Strategy and Motivation

### [Motivation](./1_strategy/1_motivation.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `STK1` | `DRV1` | concerned with |  |
| `STK1` | `DRV6` | concerned with |  |
| `STK2` | `DRV1` | concerned with |  |
| `STK2` | `DRV4` | concerned with |  |
| `STK2` | `DRV8` | concerned with |  |
| `STK3` | `DRV2` | concerned with |  |
| `STK3` | `DRV4` | concerned with |  |
| `STK4` | `DRV3` | concerned with |  |
| `STK4` | `DRV6` | concerned with |  |
| `STK5` | `DRV5` | concerned with |  |
| `STK5` | `DRV6` | concerned with |  |
| `STK6` | `DRV7` | concerned with |  |
| `STK7` | `DRV9` | concerned with |  |
| `DRV1` | `G1` | influences |  |
| `DRV2` | `G1` | influences |  |
| `DRV3` | `G1` | influences |  |
| `DRV8` | `G1` | influences |  |
| `DRV1` | `G2` | influences |  |
| `DRV6` | `G2` | influences |  |
| `DRV7` | `G2` | influences |  |
| `DRV4` | `G3` | influences |  |
| `DRV5` | `G3` | influences |  |
| `DRV9` | `G4` | influences |  |
| `G1` | `OUT1` | realized by |  |
| `G2` | `OUT2` | realized by |  |
| `G3` | `OUT3` | realized by |  |
| `G4` | `OUT4` | realized by |  |
| `P1` | `G2` | constrains |  |
| `P2` | `G1` | constrains |  |
| `P2` | `G2` | constrains |  |
| `P3` | `G4` | constrains |  |
| `P4` | `G1` | constrains |  |

## Layer 2 — Business

### [Actors and services](./2_business/1_actors-and-services.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `BSVC11` | `BSVC1` | serves |  |
| `BSVC11` | `BSVC2` | serves |  |
| `BSVC11` | `BSVC3` | serves |  |
| `BSVC11` | `BSVC4` | serves |  |
| `BSVC11` | `BSVC5` | serves |  |
| `BSVC11` | `BSVC6` | serves |  |
| `BSVC11` | `BSVC7` | serves |  |
| `BSVC11` | `BSVC8` | serves |  |
| `BSVC11` | `BSVC9` | serves |  |
| `BSVC10` | `BSVC11` | serves |  |
