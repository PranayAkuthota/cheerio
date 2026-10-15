"""Create the four-page report and matching Markdown from shared content."""
from pathlib import Path
from xml.sax.saxutils import escape
import json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
pdfmetrics.registerFont(TTFont('CheerioSans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('CheerioBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'deliverables'
n=json.loads((OUT/'financial_results.json').read_text())
# Fail rather than publish stale prose if the model's declared base inputs change.
for sheet,cell,expected in [
 ('Volume','B5',20000),('Volume','B8',9000),('Volume','B10',11000),
 ('AI Costs','B8',.00372),('AI Costs','B11',55.8),('AI Costs','B14',255.8),
 ('AI Costs','B15',.01279),('AI Costs','B17',255.8/9000),
 ('Human Comparison','B6',20000),('Human Comparison','B11',11255.8),
 ('Human Comparison','B12',8744.2),('Human Comparison','B13',.43721),
 ('Human Comparison','B18',448),('Human Comparison','B19',112),
 ('Billing','B6',25000),('Billing','B10',13744.2),('Billing','B11',.549768),
 ('Billing','B17',2000),('Billing','B20',1788.84),('Billing','B21',.89442),
 ('Billing','B22',-411.16),('Billing','B24',101),('Billing','B27',900),
 ('Billing','B29',644.2),('Billing','B30',644.2/900),('Billing','B31',-10355.8),
 ('Audit and Sensitivity','B27',2477.68),('Audit and Sensitivity','B41',8744.2),
 ('Audit and Sensitivity','B55',22080.96)]:
 assert abs(n[sheet][cell]-expected)<1e-7,f'Update report prose for changed model: {sheet} {cell}'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom',fontName='CheerioBold',fontSize=24,leading=28,textColor=colors.HexColor('#206e55'),spaceAfter=10))
styles.add(ParagraphStyle(name='SubCustom',fontName='CheerioSans',fontSize=9.5,leading=13.5,textColor=colors.HexColor('#6c8172'),spaceAfter=12))
styles.add(ParagraphStyle(name='HCustom',fontName='CheerioBold',fontSize=12,leading=16,textColor=colors.HexColor('#286046'),spaceBefore=10,spaceAfter=6))
styles.add(ParagraphStyle(name='BodyCustom',fontName='CheerioSans',fontSize=9.5,leading=13.5,textColor=colors.HexColor('#31483a'),spaceAfter=7))
styles.add(ParagraphStyle(name='CellCustom',fontName='CheerioSans',fontSize=8.3,leading=11.5,textColor=colors.HexColor('#31483a')))
styles.add(ParagraphStyle(name='CaptionCustom',fontName='CheerioSans',fontSize=6.5,leading=8,textColor=colors.HexColor('#6c8172'),spaceAfter=5))
flow=[];md=['# Cheerio Resolve — Assignment A','Pranay Kumar Akuthota · 14 October 2026 · AI-assisted draft for personal review','']
def para(text,style='BodyCustom'):
 flow.append(Paragraph(escape(text),styles[style]));md.append(text+'\n')
def h(text):para(text,'HCustom');md[-1]='## '+text+'\n'
def table(headers,rows,widths):
 data=[[Paragraph(escape(str(x)),styles['CellCustom']) for x in row] for row in [headers]+rows]
 t=Table(data,colWidths=widths,hAlign='LEFT',repeatRows=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3ec')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#c3d6c6')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#e6ede6'))]))
 flow.append(t);flow.append(Spacer(1,6));md.append('| '+' | '.join(headers)+' |');md.append('| '+' | '.join(['---']*len(headers))+' |');md.extend('| '+' | '.join(str(x) for x in r)+' |' for r in rows);md.append('')
def page(title,sub,first=False):
 if not first:flow.append(PageBreak());md.append('\n<div style="page-break-after: always;"></div>\n')
 para(title,'TitleCustom');para(sub,'SubCustom')
W=A4[0]-84
page('Cheerio Resolve','1 / 4 · Problem, priorities and product judgment',True)
para('A proposed guided AI support experience for non-technical business owners. The brief describes growing support demand; it does not establish ticket volumes or resolution benchmarks. This proposal treats those numbers as hypotheses.')
h('The user and the job')
para('A small D2C store owner runs WhatsApp promotions herself. She wants to get an opted-in campaign working without debugging APIs, duplicating sends, or waiting through repeated explanations. Clear next steps and access to a person matter more than a long answer.')
h('Five issues to tackle first')
table(['Priority','Issue','Why / safe boundary'],[
 ['1','Phone connection','Blocks sending. Identify status; escalate ownership, restrictions and complex verification.'],
 ['2','Template approval / rejection','Campaign blocker. Explain status and reason; guide correction, never promise Meta approval.'],
 ['3','Recipient consent / eligibility','Compliance-critical. Check evidence; never bypass consent to get a campaign out.'],
 ['4','Chatbot flow not triggering','Check published state, triggers and conditions with a controlled test.'],
 ['5','Integration setup','Step-by-step guidance; specialist for credentials and complex permission issues.']], [45,153,W-198])
para('Prioritization: 30% expected frequency + 30% impact + 25% safe feasibility + 15% business value (1–5 scores; all assumed). Templates score 4.75, connection 4.20, consent 4.00, flows 3.70, integrations 3.20. I put connection first because it is a prerequisite for sending; that dependency overrides the raw score.')
h('Alternatives and the choice')
para('AI-assisted comparison: documentation (3.45), searchable help (3.65), rule-based guidance (4.00), generic AI chat (3.50), account-aware AI (3.90), human-only support (4.55), proactive onboarding/alerts (3.35), and guided rules + constrained AI + handoff (4.45). Scores weight usefulness 35%, coverage 25%, safety 25%, delivery ease 15%; all are hypotheses.')
para('Human-only ranks well for service but fails the scaling objective. Documentation and search stay as foundations. I choose bounded guidance with optional AI interpretation of redacted text: safer than unconstrained answers and faster to pilot than account-wide integration. Start with the first three issues; validate ordering on real tickets before expanding.')
page('A fix you can follow','2 / 4 · Solution, human boundary and measurement')
h('One end-to-end journey')
para('Support home → describe/select campaign issue → report template status → report phone connection → read a possible cause and one small set of safe steps → test with one opted-in recipient → confirm or try one alternative → hand off if still stuck. The prototype implements this campaign/template journey; other topics disclose specialist boundaries.')
h('What it will and will not do')
para('Initial production scope: vetted connection, template and recipient playbooks; understandable guidance; source labels; explicit confirmation; context-rich handoff. AI classifies and explains approved guidance, while deterministic rules gate risk and actions. Later, permissioned read-only account context can reduce questions. The current prototype is deterministic, not a live AI service.')
para('No autonomous template approval, campaign sending, production edits, credential handling or billing changes. No invented account checks or real tickets. Sample context, user reports and unavailable checks are visibly distinct. Production needs versioned help content, least-privilege access and monitoring before launch.')
h('A person is part of the journey')
para('Escalate security/payment/ownership cases, unsupported problems, unresolved conflicting evidence, disconnected accounts requiring specialist work, or two failed attempts. A person can be requested at any point. An unavailable check offers manual status input or handoff. Transfer issue wording, reported statuses with sources/timestamps, attempted steps, outcomes and reason; let the user review/redact first. The demo downloads a summary and says no ticket was created.')
h('North Star and a three-month hypothesis')
para('Confirmed self-service resolution rate = eligible issue episodes resolved without a human / all eligible episodes opened that month. Freeze eligibility at intake; deduplicate same-business/campaign/problem contacts over seven days. Require a user-confirmed successful test within seven days of intake and no same-issue reopen for seven further days. Finalize cohorts 14 days after month-end. Count abandoned, unconfirmed, late and reopened episodes as unresolved. Audit a redacted success sample.')
para('Month-three hypothesis: 60% eligible success. An illustrative 45% baseline means +15 percentage points (+33% relative); measure the actual baseline and rebase if it differs. Month 1: instrument and audit the first 100 episodes. Month 2: fix the two worst branches. Month 3: add vetted recipient guidance and reduce repeated clarification. Keep eligibility and human access stable; stop unsafe playbooks.')
h('Three supporting metrics')
para('1. Median and p90 time to confirmed resolution, with abandonment as a guardrail. 2. Seven-day repeat-contact rate across eligible episodes. 3. Acknowledged, complete-context handoffs / all requested or mandatory handoffs; failed delivery stays in the denominator. Segment by issue, language and tenure. Track privacy incidents and CSAT without optimizing away human access.')
page('Prototype and AI evidence','3 / 4 · Working interactions, real screenshots and honest attribution')
para('Prototype: https://cosmic-torte-9064aa.netlify.app/ | Local validation: 8 state-machine tests, 23 browser checks, responsive layouts and production build. No credentials or backend required. Screens below are from the running application.', 'CaptionCustom')
images=[]
for name,caption in [('01-support-home.png','1. Support home'),('02-guided-troubleshooting.png','2. Targeted questions'),('03-diagnosis.png','3. Possible cause and safe steps'),('04-human-escalation.png','4. Handoff with history')]:
 path=OUT/'screenshots'/name
 with PILImage.open(path) as source: iw,ih=source.size
 scale=min(((W-14)/2)/iw,160/ih)
 im=Image(str(path),width=iw*scale,height=ih*scale)
 images.append([im,Paragraph(caption,styles['CaptionCustom'])])
 grid=images
for i in [0,2]:
 t=Table([[images[i],images[i+1]]],colWidths=[W/2,W/2],hAlign='LEFT');t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),5)]));flow.append(t)
md.extend(['![Support home](screenshots/01-support-home.png)','![Guided troubleshooting](screenshots/02-guided-troubleshooting.png)','![Diagnosis](screenshots/03-diagnosis.png)','![Human handoff](screenshots/04-human-escalation.png)',''])
h('How I used Codex')
para('Codex drafted strategy, built React/Vite, generated the workbook/report and ran checks. Three actual useful inputs: (1) the end-to-end master task; (2) my reply “I would prioritize issues based on how much they block…”, which put connection first; (3) “Perform a final, skeptical hiring-manager review…”, which audited the saved workbook without regenerating it and tested existing journeys. Verbatim inputs and outcomes are in ai_usage_log.md and ai-prompts/.')
para('Failed part of the master task (“Add sanity checks and reconciliation checks”): the generated workbook passed base checks but divided by zero in sensitivity ratios and mapped impossible break-even to zero businesses. The skeptical review caught this by testing the saved file across all six sheets, without regenerating it first. Seven boundary formulas were corrected and base inputs linked; the repeat audit passed. The master prompt had both useful and failed outputs; no separate failed interaction is invented.')
para('My decisions so far: Assignment A, connection-first priority, three-issue scope and human-escalation rules supplied in this chat. No interviews, ticket review or firsthand platform use has occurred. Independent journey testing and financial review are pending; record actual decisions changed after doing them. AI evidence: https://chatgpt.com/s/cx_6ad08b445a508191bd5b7f4198b1534e | Drive: https://drive.google.com/file/d/1OgBfmudySJ_BoaFR-ZvifwrtKhS3HQnU/view?usp=sharing. This session is not a public chat link.')
page('Costs, billing and controls','4 / 4 · Hypothetical monthly economics · all currency USD, pre-tax')
para('Google Sheet: https://docs.google.com/spreadsheets/d/1BclVbPPVFTLHb1R1XT82PBmMfqERoWuT3W7dXH_aJjQ/edit?usp=drive_link | Prototype: https://cosmic-torte-9064aa.netlify.app/\nWorkbook: cheerio_financial_model.xlsx, six sheets with editable assumptions and visible formula text. Only 5,000 active businesses comes from the brief; other figures below are assumptions.', 'CaptionCustom')
table(['Item','Base case / workbook reference'],[
 ['Volume and outcomes','5,000 × 4 queries = 20,000/month; 75% eligible = 15,000; 60% eligible success = 9,000. Humans handle 5,000 ineligible + 6,000 unresolved = 11,000. This pilot resolves 45% of all queries, not yet most; at 75% eligibility a majority needs >66.7% eligible success. Volume B5:B10.'],
 ['AI tokens','1,500 input + 400 output tokens/interaction; 3 interactions/eligible query. Illustrative $0.40/$1.60 per million input/output tokens → $0.00372/eligible query; $55.80/month. AI Costs B5:B11.'],
 ['Feature costs','$200 infrastructure + $55.80 AI = $255.80/month; $0.01279/all queries; $0.02842/confirmed resolution. AI Costs B14, B15, B17.'],
 ['Human comparison','10 minutes/query at $6/hour = $20,000 baseline. Same handling time after handoff: $11,000 residual + $255.80 feature = $11,255.80. Savings $8,744.20 (43.72%). Human Comparison B6:B13.'],
 ['Break-even','448 total queries/month or 112 businesses at 4 queries each; 1.71% eligible success at base volume covers feature costs. Human Comparison B16:B19.']], [105,W-105])
para('Price source reference: openai.com/api/pricing/; access attempted 14 October 2026, blocked by proxy 403. Rates are explicitly illustrative, not verified live prices. Refresh before a real budget decision. No cache discounts. Human costs include overhead by assumption; engineering, one-time rollout and tax/FX are excluded. All amounts are pre-tax USD, with no incremental invoice-processing fee assumed.')
h('Billing: include core support in the platform')
para('Recommend $0 incremental price: no retry charge or human paywall. Incremental revenue is $0 and feature expense $255.80, so standalone gross margin is undefined. Funding is modeled cost avoidance, not new sales. A hypothetical $5/business allocation gives $25,000 revenue, $13,744.20 allocated gross profit and 54.98% margin on $11,255.80 full support cost. Actual platform margin needs real plan revenue (Billing B5:B13).')
para('Alternatives: $2/month add-on at 20% adoption earns $2,000; feature-only profit $1,788.84, margin 89.44%, break-even 101 subscribers. Including their residual human costs turns profit to −$411.16 (−20.56%). $0.10/confirmed resolution earns $900; feature-only profit $644.20, margin 71.58%; full-support profit −$10,355.80. These margins use different clearly labeled cost scopes. An add-on creates adoption friction; success billing risks premature confirmation, so neither is preferred.')
h('Monthly audit and uncertainty')
para('Reconcile distinct issue episodes and token invoices (alert any count mismatch, >2% token variance); review handoff delivery and seven-day reopen rates (>15%); investigate usage >30% above forecast, cost/resolution >$0.05, model-price changes, invoice mismatch >1%, any unresolved-case bill and allocated margin <40%. Fix the playbook or forecast; preserve human access. Privacy/safety incidents stop the affected flow.')
para('Low/base/high scenarios (2/4/8 queries per business; 60/75/80% eligible; 45/60/70% success) save $2,477.68 / $8,744.20 / $22,080.96 monthly. Main risks: unvalidated frequency/eligibility, weak guidance, repeat contacts, and savings as capacity rather than cash. Validate on tickets and with non-technical owners.')
# Shared Markdown artifact.
(OUT/'cheerio_assignment_A.md').write_text('\n'.join(md))
def footer(c,doc):
 c.setStrokeColor(colors.HexColor('#dce7df'));c.line(42,39,A4[0]-42,39)
 c.setFillColor(colors.HexColor('#7a8f80'));c.setFont('CheerioSans',7);c.drawString(42,26,'Pranay Kumar Akuthota | Cheerio Resolve | AI-assisted review draft')
 c.drawRightString(A4[0]-42,26,str(doc.page))
doc=SimpleDocTemplate(str(OUT/'cheerio_assignment_A.pdf'),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=48,title='Cheerio Resolve — Assignment A',author='Pranay Kumar Akuthota with Codex assistance')
doc.build(flow,onFirstPage=footer,onLaterPages=footer)
pages=len(PdfReader(OUT/'cheerio_assignment_A.pdf').pages)
print('Report pages:',pages)
assert pages==4,f'Report is {pages} pages; adjust layout before submission.'
