# Analytics' questions

_[← Initiatives](README.md)_

Every question brought to Analytics that the example project answers, as Analytics recorded it when it
was asked. Most came with no known answer, so each says who checks the result, and how, before its
ticket closes. The architecture takes each question from here, as a driver of the same number.

| ID | The question | Asked by | Known when asked | Checked by | Initiative | Ticket |
| -- | ------------ | -------- | ---------------- | ---------- | ---------- | ------ |
| `AQ1` | **How many learners are within 15 credit points of a graduate certificate, by faculty, as at census date?** | Clara Jensen, Planning | The census team's count, by hand, two weeks after census day | Clara Jensen, in test, against the census team's count | [Census planning 2026](census-planning-2026.md) | `DATA-142` |
| `AQ2` | **Which credentials does a learner hold today, and how close are they to their award?** | The wallet app team, for learners | No | The wallet app team, in test, on learners they know | Learner wallet | `DATA-118` |
| `AQ3` | **How much tuition does recognised credit save learners, by award and faculty?** | Finance | Finance's own spreadsheet | Finance, in test, against its spreadsheet | Recognised credit | `DATA-131` |
| `AQ4` | **Who graduates at each ceremony, with which award, and under which printed name?** | The registrar's and graduations offices | No | Mei Tanaka, in test, before anything is printed | Graduations 2026 | `DATA-126` |
| `AQ5` | **Which approved claims are paid on the coming pay day, and for how much?** | HR, for payroll | No | Ingrid Holm, in test, against a pay run done by hand | Casual pay | `DATA-109` |
| `AQ6` | **What does the casual teaching in a teaching period cost?** | Finance, HR, Planning | No: the three meant three different sums | Rohan Desai, with HR and Planning, in test | Casual teaching cost | `DATA-137` |
| `AQ7` | **How many people teach in each school this term, and how many are casual?** | The Faculty of Health | No | Anil Kurian, in test, on one school he knows | Teaching workload | `DATA-140` |
| `AQ8` | **Which learner is a short-course enrolment that came with no email?** | The learning team, HR | No | The learning team, in test | Short-course follow-ups | `DATA-145` |

Only the first initiative is written out here. The others are named, as the architecture names every
area and details only what a question needs.
