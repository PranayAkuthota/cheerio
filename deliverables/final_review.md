# Skeptical hiring-manager review — Cheerio Resolve, Assignment A

**Verdict: local development and arithmetic pass; the package is not submission-ready.** The product judgment is plausible and the prototype is useful, but public prototype/Sheet/chat evidence links remain missing and Pranay's independent testing/review has not happened. A fully AI-generated submission would violate the brief. Nothing has been submitted, pushed or published by this review.

Sources inspected first: all four pages of the official assignment PDF, the HR email screenshot, the existing PDF/Markdown report, all six workbook sheets and caches, prototype source and production preview, existing tests, all five screenshot files, AI usage log, product strategy, README and previous final review. The email's explicit deadline is **15 October 2026, 11:59 PM IST**; use this over the PDF's generic two-day timing. Assignment B is excluded.

PASS means the stated local content/check is satisfied; it does not establish customer validation or public availability. FAIL means a requirement or submission gate is still unmet. Optional items are labeled OPTIONAL.

## Requirement-by-requirement pass/fail checklist

| Source / requirement | Result | Evidence and skeptical finding |
|---|---|---|
| Choose one assignment | PASS | Assignment A only; no B deliverables. |
| A1.1: user and five initial issues, with reasons | PASS | Hypothetical small D2C owner. Connection blocks all sending; templates block campaign execution; consent is safety-critical; flows/integrations follow. These are plausible hypotheses, not observed ticket frequencies. |
| A1.2: alternatives, prioritization, chosen solution | PASS | Eight options; all 13 issue/solution weighted scores recalculated correctly. Connection-first is an explicit dependency override. Human-only is gated out for scaling. No comparative experiment supports the scores. |
| A1.3: clear solution, inclusions/exclusions | PASS | Guided questions, evidence labels, approved steps, confirmation and handoff. Proposed first-three pilot; only template/campaign journey implemented fully, as allowed by the one-scenario requirement. |
| A1.4: when humans intervene | PASS | Sensitive/unsupported/inconclusive cases, unknown phone status, direct user request and two failed fixes. Human access remains available during repeated clarification. |
| A1.5: three success metrics | PASS | Resolution time paired with abandonment; seven-day repeat contact; acknowledged, complete handoff / all requested or mandatory handoffs. |
| A1.6: precise North Star | PASS, corrected | Frozen intake eligibility; distinct business/campaign/problem episodes; user-confirmed test within seven days of intake; no human and no reopen for seven further days; monthly cohort final at month-end +14 days. Abandoned, late/unconfirmed and reopened episodes stay unresolved. |
| A1.6: baseline, three-month target and improvement plan | PASS as hypothesis | 60% eligible success target. An illustrative 45% baseline implies +15 points, +33.3% relative. Actual baseline must be observed and target rebased if different. Month-one instrumentation, branch fixes and vetted recipient guidance are specific actions, not proven causal effects. |
| Overall ambition: resolve most support queries | FAIL at base-case forecast | 75% eligibility ×60% success =45% of all queries. Majority requires >66.7% eligible success at 75% eligibility. This shortfall is now explicit; no inflated assumption was inserted to hide it. The high scenario reaches 56% overall, but remains hypothetical. |
| A2.1: clickable prototype | PASS locally / public link supplied | Existing production build works. Supplied Netlify URL is public and recorded in the checklist. |
| A2.2: one realistic scenario end to end and edge cases | PASS | Successful opted-in campaign test; unsuccessful fixes → handoff; pending/rejected templates; unknown/conflicting information; unavailable check; unsupported/security cases; cancellation, reopening and return home. Deterministic simulation, not a live customer account. |
| A2.3: share link plus 3–4 screenshots | PASS screenshots / public link supplied | Four actual app images, embedded and supplied full size; optional phone image. Supplied Netlify URL is public and recorded. |
| A3.1: AI tools and actual roles | PASS | Codex drafted, coded, analyzed and tested. Python/Chromium/React are implementation tools. Prototype calls no AI API. |
| A3.2: three successful prompts and one failed prompt, changes | FAIL under strict four-distinct-execution reading | Three real useful inputs are selected: master task, priority reply, current skeptical review. A genuine failed portion of the master task produced spreadsheet boundary errors. The same master prompt is reused as a useful and failed entry; overlap is disclosed, not invented away. Real screenshot evidence still needs packaging. |
| A3.3: wrong/weak AI answer and how caught | PASS | Saved-file audit exposed division-by-zero and impossible break-even bugs missed by narrow earlier checks. Exact initial failure JSON retained; seven boundary formulas corrected and retested. |
| A3.4: what applicant did without AI | PASS attribution / FAIL completed independent review | User supplied Assignment A choice, connection-first ordering, first-three scope and escalation judgment. The report now labels alternative scoring AI-assisted. No interviews, ticket review or firsthand platform use claimed. User journey/financial/alternative review is still pending. |
| A4.1: 5,000-business query/resolution guesstimate | PASS | Only business count is brief-supplied. Other operating inputs are assumptions. Eligible/ineligible/success/unresolved categories reconcile, with no duplicate query count. |
| A4.2: running cost, tokens, price source | PASS illustrative estimate | $0.40/$1.60 per million input/output tokens clearly illustrative. Official price URL and 14 October 2026 access attempt are recorded; previous proxy 403 is disclosed. No claim of verified current provider prices. |
| A4.3: billing price and margin | PASS scoped estimate | Included at $0 incremental charge; standalone margin is undefined at zero revenue. 54.98% is conditional internal-allocation margin, not actual Cheerio margin. Add-on/usage feature and full-support scopes are separate. |
| A4.4: monthly usage/billing audit and alerts | PASS design | Episode deduplication, token/invoice reconciliation, handoff delivery, repeated/failed conversations, cost/resolution, usage spikes, pricing changes and margin deterioration; thresholds and actions listed. No actual production ledger or invoice reconciliation has been performed. |
| A4.5: savings vs human support for same volume | PASS calculation | Ten minutes and $6/hour retained for residual human work; no handoff time-saving credit. Savings are possible avoided cost/capacity, not guaranteed cash reduction. |
| Formula-preserving Google Sheet | PASS XLSX / public Sheet supplied | Six sheets and 218 current formulas/caches audited. The supplied Google Sheet URL is public; import/recalculation verification remains a user check. |
| Document maximum four pages | PASS | Corrected PDF exactly four pages; all pages rendered and visually inspected. Body 9.5pt, tables 8.3pt. Screenshots are overview thumbnails; full-size originals are needed for UI text detail. |
| Mandatory actual AI chat links/screenshots | PASS supplied links / access unverified | User supplied a Codex chat URL and Drive evidence URL; signed-out access and authenticity still require verification. |
| Email: every link Anyone with the link → Viewer | PARTIAL | Prototype and Google Sheet URLs are public and recorded; document sharing and signed-out access still need final verification. |
| Email: form submission | FAIL, outstanding | Form URL recorded: https://forms.gle/Doq6ouBNbjRFz5ur5 . It has not been inspected or submitted here. |
| Optional 3–5 minute Loom | OPTIONAL, unrun | No recording or URL fabricated. |

## Product judgment

The solution is meaningfully different in design from generic chat: bounded questions and vetted steps; explicit provenance; a successful-test question; retry ceiling; reopen handling; and a reviewable, transferable history. This reduces the opportunity for arbitrary advice and prevents silent fake account verification. It does **not** demonstrate improved real customer resolution: there is no user study, account integration or live language-model behavior.

The five priorities are defensible because they separate total channel blockage, campaign blockage, consent risk, and more complex workflow/permission issues. Their expected frequency and impact scores are not evidence. A fixed five-point ranking creates false precision if treated as a discovery result; validate against redacted ticket volume, handling time and business impact. The consent priority is a safety judgment even if its real frequency is lower.

The 60% target is plausible as a bounded pilot hypothesis, but unproven. The first 100 episodes are useful for finding branches; they provide a noisy baseline and do not prove the target. Keep eligibility fixed and report overall coverage as well as eligible resolution so success cannot be improved by removing hard cases. The prototype models provisional confirmation only; seven-day cohort analytics are proposed production behavior, not implemented telemetry.

## Recalculated base case and traces

All currency USD, pre-tax. Calculations were read directly from the saved XLSX using a separate Python evaluator for its actual formula subset; neither Excel nor Google Sheets has recalculated it in this environment.

| Item | Independent calculation | Result / workbook reference |
|---|---|---|
| Monthly queries | 5,000 ×4 | 20,000; Volume B5 |
| Eligible | 20,000 ×75% | 15,000; Volume B6 |
| Automated resolution | 15,000 ×60% | 9,000; Volume B8 |
| Residual people demand | 5,000 ineligible +6,000 unresolved | 11,000; Volume B10 |
| Input / output tokens | 15,000 ×3 ×1,500 /400 | 67.5M input; 18M output; AI Costs B9:B10 |
| AI unit cost | 3 ×(1,500 ×$0.40 +400 ×$1.60)/1M | $0.00372 per eligible query; AI Costs B8 |
| Monthly AI cost | 67.5 ×$0.40 +18 ×$1.60 | $55.80; AI Costs B11 |
| Feature cost | AI $55.80 +infrastructure $200 | $255.80; AI Costs B14 |
| Feature cost per all queries / resolution | $255.80 /20,000 or /9,000 | $0.01279 /$0.02842; AI Costs B15/B17 |
| Fully human baseline | 20,000 ×10/60 ×$6 | $20,000; Human Comparison B6 |
| Residual human cost | 11,000 ×10/60 ×$6 | $11,000; Human Comparison B9 |
| Total after automation | $11,000 +$255.80 | $11,255.80; Human Comparison B11 |
| Net savings / reduction | $20,000 −$11,255.80 | $8,744.20 /43.72%; Human Comparison B12:B13 |
| Included revenue/profit/margin | hypothetical 5,000 ×$5, less full support cost | $25,000 /$13,744.20 /54.98%; Billing B6/B10/B11 |
| Add-on feature revenue/profit/margin | 1,000 ×$2, less $11.16 AI and $200 fixed | $2,000 /$1,788.84 /89.44%; Billing B17/B20/B21 |
| Add-on full-support profit/margin | feature profit less $2,200 residual people allocation | −$411.16 /−20.56%; Billing B22:B23 |
| Usage feature revenue/profit/margin | 9,000 ×$0.10, less $255.80 feature | $900 /$644.20 /71.58%; Billing B27/B29/B30 |
| Usage full-support profit | $900 −$11,255.80 | −$10,355.80; Billing B31 |
| Savings break-even | fixed $200 /$0.44721 net contribution/query, round up | 448 queries /112 businesses; Human Comparison B18:B19 |
| Eligible success break-even at base volume | $255.80 /15,000 | 1.7053%; Human Comparison B16 |

All eligible episodes incur AI cost, including unsuccessful ones; ineligible intake is assumed rule-based with no AI charge. Budgeting every unresolved eligible query as residual human demand is conservative, not proof that all abandoned users actually receive support. Spreadsheet floating-point reconciliation is within 1e−8, not literally bitwise zero.

### Low/base/high scenarios

| Scenario | Queries | Eligible | Resolved | Residual human | AI +infra | Total post-automation | Savings | Feature cost/resolution |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Low: 2 queries, 60% eligible, 45% success | 10,000 | 6,000 | 2,700 | 7,300 | $222.32 | $7,522.32 | $2,477.68 | $0.08234 |
| Base: 4 queries, 75% eligible, 60% success | 20,000 | 15,000 | 9,000 | 11,000 | $255.80 | $11,255.80 | $8,744.20 | $0.02842 |
| High: 8 queries, 80% eligible, 70% success | 40,000 | 32,000 | 22,400 | 17,600 | $319.04 | $17,919.04 | $22,080.96 | $0.01424 |

All three were independently recalculated. The low scenario exceeds the proposed $0.05 cost-per-resolution threshold despite positive total savings. High volume retains $200 fixed infrastructure; do not assume this remains feasible without capacity evidence. The base scenario now follows main editable inputs; low/high remain separate assumptions.

Commercial conclusion: included support is credible because support is core platform value and the incremental feature cost is modest relative to the modeled avoided people cost. Actual profitability cannot be established without real plan revenue, labor rates and volume. Negative alternative full-support margins are not proof an add-on cannot be incrementally profitable: existing platform revenue is excluded from those alternative scopes. Engineering/ongoing playbook maintenance, rollout, tax/FX and extra processing fees are excluded or zero-assumed, not known to be free. Assumptions B27 is a pre-tax disclosure; changing it does not apply tax throughout the model.

## Material defects corrected locally

1. Six sensitivity ratios divided by zero for allowed boundary inputs. They now return N/A rather than fake zero cost or a broken formula: Audit and Sensitivity B28/B29, B42/B43, B56/B57.
2. Human Comparison B19 could turn the impossible-volume sentinel −1 into zero businesses. It now preserves −1.
3. Base sensitivity inputs B31:B33 were hardcoded copies that did not follow changes to main assumptions. They now reference Assumptions B6:B8, with visible FORMULATEXT cells. Input B6=5 now yields 25,000 queries and $10,980.25 savings in both main and base views.
4. The North Star lacked a deadline for initial confirmation. Report/strategy now specify the seven-day intake deadline and monthly finalization window; baseline is explicitly unobserved and must be rebased.
5. Report now states 45% overall resolution does not yet meet majority coverage and that zero-revenue standalone margin is undefined. Alternative scoring is labeled AI-assisted, not falsely attributed to completed independent comparison.
6. Strategy no longer claims a one-clarification limit that the demo does not enforce; visible human access is the tested behavior.
7. AI log records this actual review and the real spreadsheet failure/correction. No fabricated failure, interview or standalone fourth failed prompt was added.
8. Report amendments initially spilled to six pages. Screenshot/table spacing was adjusted, retaining readable body/table fonts; final output is four pages, all four pages inspected.

The frontend source, dependencies, lockfile, production assets and original screenshot files were unchanged. No frontend build or dependency installation was rerun. Workbook changes were surgical XML edits with caches/styles retained; all original main assumptions and numeric base outputs were verified unchanged. Generator and formula inventory were synchronized for future use. Initial copies are preserved outside the submission at /tmp/cheerio-skeptical-review-original.

## Actual checks rerun

- `npm test`: **8 passed, 0 failed, 0 skipped**.
- Existing browser regression suite against the existing production preview: **23 passed**. Repeated after the initial audit diagnosis; no frontend rebuild. Fresh test outputs were redirected to scratch, preserving submitted screenshots.
- Seven supplemental browser checks: **7 passed**, covering unavailable-check handoff, unknown phone, first-failure handoff, resolution→home, repeated clarification, actual event JSON download and 320px diagnosis/escalation. Together: **30 browser checks passed**. No full accessibility certification or real owner usability study claimed.
- Saved-workbook audit: initially **FAIL** on boundary errors, preserved in skeptical_audit_initial_results.json; finally **PASS** across all six sheets, **218 formula cells/caches**, direct arithmetic, three scenarios, billing/break-even, seven boundary settings and base-input propagation.
- `python scripts/audit_existing_package.py --skip-browser`: final financial/PDF checks passed; explicitly retained the preceding passing browser result, rather than claiming it reran the browser.
- 13 prioritization scores: all recomputed and matched.
- `python scripts/build_report.py`: final **4 pages**, 4 actual embedded screenshots; all headline numbers checked against workbook traces and all pages rendered/visually inspected. Screenshots remain thumbnails; full-size files supplement them.
- Source generator/audit Python compile checks passed. The destructive generator-import financial test was **not** rerun, because it regenerates artifacts before inspection.
- ZIP integrity and archive/current-file consistency checked after repackaging. No live pricing check, Sheets import, deployment, public-link permission test or submission was executed.

Exact changed and added paths, separated from preserved files, are recorded in [review_changes.md](review_changes.md). This review is assistant work, not Pranay's independent validation.

## Five highest-priority remaining actions, in order

1. **Complete and record your own review.** Run the existing app. Personally test approved→success, two failures→handoff and missing-status paths on a phone. Change Assumptions B6 from 4 to 5, explain 25,000 queries and $10,980.25 savings, then restore it to 4. Write the alternative you reject and why, and whether you accept the 45% pilot shortfall. Fill only completed actions into the AI log and report; do not claim interviews or borrow assistant tests as your own.
2. **Verify the supplied AI evidence.** Open the Codex chat and Drive URLs signed out, confirm they show genuine prompts/outputs, and ensure Drive access is Anyone with the link → Viewer. Add screenshots only if the links do not satisfy the form.
3. **Create and verify the Google Sheet.** Upload the corrected XLSX, convert to Google Sheets, verify six sheets and formulas in B/D. Change B6 to 5: main and base should show 25,000 queries, 11,250 resolutions, $269.75 feature cost and $10,980.25 savings; restore 4. Inspect the new N/A boundary behavior and −1 impossible-break-even sentinel. Keep token rates explicitly illustrative unless you actually verify the official price source and record the date. Share Anyone with the link → Viewer.
4. **Verify the supplied prototype.** Open https://cosmic-torte-9064aa.netlify.app/ in incognito and on your phone. Test success and escalation, then keep the recorded URL if it is publicly accessible.
5. **Finalize links, permissions and form submission.** Insert actual prototype/Sheet/evidence URLs and completed independent-review statements into the report generator/source, regenerate the PDF, verify ≤4 pages and numbers, and upload the final document/screenshots with Viewer access. Open every link signed out. Submit through https://forms.gle/Doq6ouBNbjRFz5ur5 before 15 October 2026, 11:59 PM IST and save the actual acknowledgement. Optional Loom follows only if time permits. None of these external actions has been completed here.
