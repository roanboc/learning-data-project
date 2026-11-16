# 00 · Initiatives

Where a question starts. A question is born in analytics: someone needs a number to decide something,
and most of the time nobody knows the answer yet, so it's explored and checked while the work is built.
Analytics keeps a record of every question it's asked, and each initiative's documentation carries its
questions into tickets, as business requirements.

At the university, the record is Analytics' own and the tickets are in Jira. This folder is both as
text, so people and agents can read them beside the rest of the project.

| File | What it is | Written by |
| ---- | ---------- | ---------- |
| [`analytics-questions.md`](analytics-questions.md) | Every question Analytics has been asked that the project answers: who asks, what's known of the answer, who checks the result, its initiative and its ticket | Analytics |
| [`census-planning-2026.md`](census-planning-2026.md) | One initiative written out: why, its business requirements as its ticket holds them, and when each is accepted | Its sponsor, Clara Jensen, with Analytics |

## From a question to the code

1. **A question, in Analytics' records.** Who asks, what for, what's known of the answer, and who will
   check the result.
2. **An initiative, and its ticket.** The question becomes a business requirement in the initiative's
   documentation, and goes into a ticket. The people who asked approve the ticket and close it, once
   they've checked the result.
3. **The architecture** finds the question's domains, the data objects it needs and the systems of
   record that feed them, and records it as a driver
   ([`10-enterprise-architecture/`](../10-enterprise-architecture/README.md)).
4. **Data governance** maps each data object to a glossary entity, with its owner, and each entity to
   a core entity under an enterprise contract ([`20-data-governance/`](../20-data-governance/README.md)).
5. **The data team** builds sources, staging and intermediate models up to that core entity. Where
   models already exist, it checks them first, then adds the core entity on top
   ([`30-data-project/`](../30-data-project/README.md)).

Links point one way: the architecture takes each question from here, and nothing here reads the other
folders.
