# Information assets

The university's information assets that the questions need, in one file, `information-assets.yml`.
For each: its owner, who looks after it day to day, its level (`public`, `internal`, `confidential` or
`restricted`), the strictest personal data it holds, the system it is first recorded in and those that
keep a copy, its shared table, its enterprise contract and the data products that serve it.

Each asset refines a data object on the enterprise architecture's map (`data_object: UNI.DOBJ2.1`, in
`../../10-enterprise-architecture/architecture/3_information/`). The map says what exists and where;
this says who answers for it and how it is protected. Only the assets a question needs are here, as only
those objects are on the map; a new question adds its object to the map first, then its asset here.

`../scripts/check.py` checks every row, and writes the matrices in `../10-matrices/` from it.
