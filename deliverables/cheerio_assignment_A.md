# Cheerio Resolve — Assignment A
Pranay Kumar Akuthota · 14 October 2026 · AI-assisted draft for personal review

Cheerio Resolve

1 / 4 · Problem, priorities and product judgment

A proposed guided AI support experience for non-technical business owners. The brief describes growing support demand; it does not establish ticket volumes or resolution benchmarks. This proposal treats those numbers as hypotheses.

## The user and the job

A small D2C store owner runs WhatsApp promotions herself. She wants to get an opted-in campaign working without debugging APIs, duplicating sends, or waiting through repeated explanations. Clear next steps and access to a person matter more than a long answer.

## Five issues to tackle first

| Priority | Issue | Why / safe boundary |
| --- | --- | --- |
| 1 | Phone connection | Blocks sending. Identify status; escalate ownership, restrictions and complex verification. |
| 2 | Template approval / rejection | Campaign blocker. Explain status and reason; guide correction, never promise Meta approval. |
| 3 | Recipient consent / eligibility | Compliance-critical. Check evidence; never bypass consent to get a campaign out. |
| 4 | Chatbot flow not triggering | Check published state, triggers and conditions with a controlled test. |
| 5 | Integration setup | Step-by-step guidance; specialist for credentials and complex permission issues. |

Prioritization: 30% expected frequency + 30% impact + 25% safe feasibility + 15% business value (1–5 scores; all assumed). Templates score 4.75, connection 4.20, consent 4.00, flows 3.70, integrations 3.20. I put connection first because it is a prerequisite for sending; that dependency overrides the raw score.

## Alternatives and the choice

AI-assisted comparison: documentation (3.45), searchable help (3.65), rule-based guidance (4.00), generic AI chat (3.50), account-aware AI (3.90), human-only support (4.55), proactive onboarding/alerts (3.35), and guided rules + constrained AI + handoff (4.45). Scores weight usefulness 35%, coverage 25%, safety 25%, delivery ease 15%; all are hypotheses.

Human-only ranks well for service but fails the scaling objective. Documentation and search stay as foundations. I choose bounded guidance with optional AI interpretation of redacted text: safer than unconstrained answers and faster to pilot than account-wide integration. Start with the first three issues; validate ordering on real tickets before expanding.


<div style="page-break-after: always;"></div>

A fix you can follow

2 / 4 · Solution, human boundary and measurement

## One end-to-end journey

Support home → describe/select campaign issue → report template status → report phone connection → read a possible cause and one small set of safe steps → test with one opted-in recipient → confirm or try one alternative → hand off if still stuck. The prototype implements this campaign/template journey; other topics disclose specialist boundaries.

## What it will and will not do

Initial production scope: vetted connection, template and recipient playbooks; understandable guidance; source labels; explicit confirmation; context-rich handoff. AI classifies and explains approved guidance, while deterministic rules gate risk and actions. Later, permissioned read-only account context can reduce questions. The current prototype is deterministic, not a live AI service.

No autonomous template approval, campaign sending, production edits, credential handling or billing changes. No invented account checks or real tickets. Sample context, user reports and unavailable checks are visibly distinct. Production needs versioned help content, least-privilege access and monitoring before launch.

## A person is part of the journey

Escalate security/payment/ownership cases, unsupported problems, unresolved conflicting evidence, disconnected accounts requiring specialist work, or two failed attempts. A person can be requested at any point. An unavailable check offers manual status input or handoff. Transfer issue wording, reported statuses with sources/timestamps, attempted steps, outcomes and reason; let the user review/redact first. The demo downloads a summary and says no ticket was created.

## North Star and a three-month hypothesis

Confirmed self-service resolution rate = eligible issue episodes resolved without a human / all eligible episodes opened that month. Freeze eligibility at intake; deduplicate same-business/campaign/problem contacts over seven days. Require a user-confirmed successful test within seven days of intake and no same-issue reopen for seven further days. Finalize cohorts 14 days after month-end. Count abandoned, unconfirmed, late and reopened episodes as unresolved. Audit a redacted success sample.

Month-three hypothesis: 60% eligible success. An illustrative 45% baseline means +15 percentage points (+33% relative); measure the actual baseline and rebase if it differs. Month 1: instrument and audit the first 100 episodes. Month 2: fix the two worst branches. Month 3: add vetted recipient guidance and reduce repeated clarification. Keep eligibility and human access stable; stop unsafe playbooks.

## Three supporting metrics

1. Median and p90 time to confirmed resolution, with abandonment as a guardrail. 2. Seven-day repeat-contact rate across eligible episodes. 3. Acknowledged, complete-context handoffs / all requested or mandatory handoffs; failed delivery stays in the denominator. Segment by issue, language and tenure. Track privacy incidents and CSAT without optimizing away human access.


<div style="page-break-after: always;"></div>

Prototype and AI evidence

3 / 4 · Working interactions, real screenshots and honest attribution

Prototype: https://cosmic-torte-9064aa.netlify.app/ | Local validation: 8 state-machine tests, 23 browser checks, responsive layouts and production build. No credentials or backend required. Screens below are from the running application.

![Support home](screenshots/01-support-home.png)
![Guided troubleshooting](screenshots/02-guided-troubleshooting.png)
![Diagnosis](screenshots/03-diagnosis.png)
![Human handoff](screenshots/04-human-escalation.png)

## How I used Codex

Codex drafted strategy, built React/Vite, generated the workbook/report and ran checks. Three actual useful inputs: (1) the end-to-end master task; (2) my reply “I would prioritize issues based on how much they block…”, which put connection first; (3) “Perform a final, skeptical hiring-manager review…”, which audited the saved workbook without regenerating it and tested existing journeys. Verbatim inputs and outcomes are in ai_usage_log.md and ai-prompts/.

Failed part of the master task (“Add sanity checks and reconciliation checks”): the generated workbook passed base checks but divided by zero in sensitivity ratios and mapped impossible break-even to zero businesses. The skeptical review caught this by testing the saved file across all six sheets, without regenerating it first. Seven boundary formulas were corrected and base inputs linked; the repeat audit passed. The master prompt had both useful and failed outputs; no separate failed interaction is invented.

My decisions so far: Assignment A, connection-first priority, three-issue scope and human-escalation rules supplied in this chat. No interviews, ticket review or firsthand platform use has occurred. Independent journey testing and financial review are pending; record actual decisions changed after doing them. AI evidence links supplied by the applicant; full URLs are recorded in submission_checklist.md. This session is not a public chat link.


<div style="page-break-after: always;"></div>

Costs, billing and controls

4 / 4 · Hypothetical monthly economics · all currency USD, pre-tax

Workbook: cheerio_financial_model.xlsx, six sheets with editable assumptions and visible formula text. Google Sheet URL: [ADD ACTUAL SHARED SHEET URL]. Only 5,000 active businesses comes from the brief; other figures below are assumptions, not actual Cheerio operations.

| Item | Base case / workbook reference |
| --- | --- |
| Volume and outcomes | 5,000 × 4 queries = 20,000/month; 75% eligible = 15,000; 60% eligible success = 9,000. Humans handle 5,000 ineligible + 6,000 unresolved = 11,000. This pilot resolves 45% of all queries, not yet most; at 75% eligibility a majority needs >66.7% eligible success. Volume B5:B10. |
| AI tokens | 1,500 input + 400 output tokens/interaction; 3 interactions/eligible query. Illustrative $0.40/$1.60 per million input/output tokens → $0.00372/eligible query; $55.80/month. AI Costs B5:B11. |
| Feature costs | $200 infrastructure + $55.80 AI = $255.80/month; $0.01279/all queries; $0.02842/confirmed resolution. AI Costs B14, B15, B17. |
| Human comparison | 10 minutes/query at $6/hour = $20,000 baseline. Same handling time after handoff: $11,000 residual + $255.80 feature = $11,255.80. Savings $8,744.20 (43.72%). Human Comparison B6:B13. |
| Break-even | 448 total queries/month or 112 businesses at 4 queries each; 1.71% eligible success at base volume covers feature costs. Human Comparison B16:B19. |

Price source reference: openai.com/api/pricing/; access attempted 14 October 2026, blocked by proxy 403. Rates are explicitly illustrative, not verified live prices. Refresh before a real budget decision. No cache discounts. Human costs include overhead by assumption; engineering, one-time rollout and tax/FX are excluded. All amounts are pre-tax USD, with no incremental invoice-processing fee assumed.

## Billing: include core support in the platform

Recommend $0 incremental price: no retry charge or human paywall. Incremental revenue is $0 and feature expense $255.80, so standalone gross margin is undefined. Funding is modeled cost avoidance, not new sales. A hypothetical $5/business allocation gives $25,000 revenue, $13,744.20 allocated gross profit and 54.98% margin on $11,255.80 full support cost. Actual platform margin needs real plan revenue (Billing B5:B13).

Alternatives: $2/month add-on at 20% adoption earns $2,000; feature-only profit $1,788.84, margin 89.44%, break-even 101 subscribers. Including their residual human costs turns profit to −$411.16 (−20.56%). $0.10/confirmed resolution earns $900; feature-only profit $644.20, margin 71.58%; full-support profit −$10,355.80. These margins use different clearly labeled cost scopes. An add-on creates adoption friction; success billing risks premature confirmation, so neither is preferred.

## Monthly audit and uncertainty

Reconcile distinct issue episodes and token invoices (alert any count mismatch, >2% token variance); review handoff delivery and seven-day reopen rates (>15%); investigate usage >30% above forecast, cost/resolution >$0.05, model-price changes, invoice mismatch >1%, any unresolved-case bill and allocated margin <40%. Fix the playbook or forecast; preserve human access. Privacy/safety incidents stop the affected flow.

Low/base/high scenarios (2/4/8 queries per business; 60/75/80% eligible; 45/60/70% success) save $2,477.68 / $8,744.20 / $22,080.96 monthly. Main risks: unvalidated frequency/eligibility, weak guidance, repeat contacts, and savings as capacity rather than cash. Validate on tickets and with non-technical owners.
