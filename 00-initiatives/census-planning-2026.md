# Census planning 2026

_[← Initiatives](README.md)_

| Sponsor | Ticket | Status |
| ------- | ------ | ------ |
| Clara Jensen, Planning | `DATA-142` | Checked in test by Clara Jensen, released, and the ticket closed |

## Why

Each census, Planning decides where to put advising and teaching for the learners close to an award.
The census team counted them by hand, about two weeks after census day, and nobody could repeat the
count or split it another way.

## Business requirements

Each requirement is a line of the ticket, in Planning's words. The question behind them is `AQ1` in
[Analytics' records](analytics-questions.md).

| ID | Business requirement | Question | Ticket | Accepted when |
| -- | -------------------- | -------- | ------ | ------------- |
| `BR1` | **Count the learners within 15 credit points of a graduate certificate, by faculty, as at census date** | `AQ1` | `DATA-142` | Clara Jensen has checked the numbers in test, against the census team's count |
| `BR2` | **Have the count ready by 7 a.m. on census day, every year, with no count by hand** | `AQ1` | `DATA-142` | It's ready on time on the first census day |
| `BR3` | **Show Planning no names or emails: it counts learners, it doesn't need to know who they are** | `AQ1` | `DATA-142` | What Planning reads holds counts and keys only |

## Not in scope

- Learners near a master or a diploma: a later question, if Planning asks it.
- Who each learner is: advisers look them up in the student system, which they're allowed to read.

## Then

The architecture finds the question's domains, data objects and systems of record. Data governance maps
each data object to its glossary entity and owner, and to the core entity and contract it maps to. The
data team builds up to that core entity, or checks first what's already built. Clara Jensen checks the
result in test, and the ticket closes.
