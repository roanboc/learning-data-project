# The open standards' schemas

Copies of the JSON schemas the checks validate against, so they run with no network: the data project's
`scripts/generate/products.py` for the descriptors and contracts, and `../scripts/check.py` for the metrics:

| File | Standard | From | Read on |
|---|---|---|---|
| `open-data-contract-standard-3.1.0.schema.json` | Open Data Contract Standard v3.1.0 | [bitol-io/open-data-contract-standard](https://github.com/bitol-io/open-data-contract-standard), `schema/` | 20 October 2026 |
| `open-data-product-standard-1.0.0.schema.json` | Open Data Product Standard v1.0.0 | [bitol-io/open-data-product-standard](https://github.com/bitol-io/open-data-product-standard), `schema/` | 20 October 2026 |
| `ossie-0.1.1.schema.json` | Apache Ossie 0.1.1, the open format for semantic models (called Open Semantic Interchange, OSI, until July 2026) | [apache/ossie](https://github.com/apache/ossie), `core-spec/osi-schema.json` at tag `osi-0.1.1-rc1` | 14 November 2026 |

The first two are Bitol projects at the Linux Foundation, under the Apache License 2.0; the files are
unchanged; only their names are ours. The contract standard's 3.2.0 and the product standard's 1.1.0
are newer. Contract standard 3.1.0 is the version Ontos reads and writes (checked on 16 October 2026),
and product standard 1.0.0 is the release of the same time. To move to a newer version, copy its
schema here and change the versions in the script.

Apache Ossie is incubating at the Apache Software Foundation, under the Apache License 2.0; its schema
is unchanged; only its name is ours. Version 0.1.1 is its one release; 0.3.0 is being drafted and its
schema still changes, so the metrics stay on 0.1.1 until it is released.
