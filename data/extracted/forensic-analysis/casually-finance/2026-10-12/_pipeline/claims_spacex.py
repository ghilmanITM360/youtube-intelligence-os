import csv,json
from pathlib import Path
p=Path('02_VIDEO_FORENSICS/-X6YzlY_8tM');s={r['sentence_id']:r for r in csv.DictReader(open(p/'SENTENCES.csv'))}
data='''0|2|Proposed $1.75T IPO exceeds defense contractors, five consumer companies and ten LSE companies|S001.1;S002;S003;S004|PARTLY_CHECKED|Target valuation versus dated listed market caps; largest IPO company valuation differs from proceeds raised; charts omit valuation-date methodology.
3|3|SpaceX loses nearly $5B in2025|S005.3-S005.4|SOURCE_EXCERPT_CONSISTENT|Reuters citing The Information; reported consolidated scope, not audited by reviewer.
5|6|Retirement accounts will become large buyers within weeks because rule specifically designed for SpaceX|S006.4-S006.9|UNVERIFIED|Future eligibility/index exposure conditional; purpose inferred, not proven by chronology; all retirement accounts generalization unsupported.
12|15|SpaceX has three businesses; xAI creates least value|S007.10-S008.5|SOURCE_INTERPRETATION_UNVERIFIED|Three-box simplification and value judgement; not segment audit.
18|19|xAI founded2023 and acquired at $250B in $1.25T all-stock merger|S010.11-S010.20|PARTLY_CHECKED|CNBC excerpt supports stated allocations; valuation is transaction basis, not cash paid; merger and IPO target are different dates.
25|26|Eleven cofounders came from DeepMind OpenAI Google Toronto|S011.0-S012.3|UNVERIFIED|Nine photographed plus two caption; identities and employment not independently established.
27|27|xAI burns more than $1B monthly in2025|S013.0-S013.8|PARTLY_CHECKED|Bloomberg headline says $1B a month, not strictly greater; cash burn differs from accounting loss.
28|28|All eleven cofounders departed by March2026|S015.0|UNVERIFIED|Faded photograph illustrates claim; no independent departure roster.
29|30|Musk says xAI must rebuild and acquisition grossly overvalued|S016.0;S017;S018.0-S018.2|PARTLY_CHECKED|Displayed Mar12 2026 post supports rebuild wording; overvaluation judgement and paid$250B phrasing interpretation of all-stock valuation.
31|32|AI valuation/revenue comparison: OpenAI850/24, Anthropic400/30, xAI250/1 billions|S018.5-S018.8|UNVERIFIED|No recoverable underlying source/date for all figures; annual revenue versus annualized run rate not established; simple ratios35x13x250x approximate.
35|35|xAI burns whatever cash other units generate|S019|SOURCE_INTERPRETATION_UNVERIFIED|Absolute statement requires cash-flow reconciliation; meme is not evidence.
42|44|Rockets roughly$4B lastyear, about quarter of SpaceX revenue|S024.3;S025.1|PARTLY_CHECKED|Reuters says perhaps$4B;4/18.5 is21.6%, only approximately quarter; dates and consolidated revenue denominator matter.
51|52|Starlink beta2020 fastest scaling telecom ever, >10000satellites|S027.13-S027.15|PARTLY_CHECKED|Not a Tesla App headline supports count, headline67% versus body66%; fastest-ever superlative unverified.
53|55|Starlink satellites communicate and roof dish self-points|S028.0-S028.2|UNVERIFIED|Simplified network diagram; generation/hardware exceptions not assessed.
58|67|Podcast guest praises Starlink while allowing overvaluation|S029-S031|ATTRIBUTED_OPINION|Diary of CEO footage; ASR Scott Galaway/Plains errors possible; speaker opinion not measured product performance.
68|68|More than10M active subscribers in about150countries|S032.1-S032.2|UNVERIFIED|Caption and coverage map do not independently establish active-subscriber count or country denominator.
69|69|Starlink2025 revenue$11.4B and61%of total|S033.0-S033.4|SOURCE_EXCERPT_CONSISTENT|HarianBasis and later Yahoo cite reporting; same upstream report is not independent corroboration;61% roughly reconciles to18.5B.
72|74|Margins rise41%to63%in two years and are accelerating|S035-S036.2|ACCOUNTING_LABEL_CONFLICT|Screenshot and dates explicitly adjusted EBITDA margins2023/2025; narration says profit margins and thisyear; two endpoints cannot prove acceleration.
76|77|Maritime aviation and Starshield government customers|S036.7-S036.10|UNVERIFIED|Illustrative drawings/seal and ASR Starsheald; exact contracts not recoverable here.
78|78|Rocket and Starlink earn$8B but combined SpaceX/xAI loses$5B on18.5B revenue|S041.3;S043|ACCOUNTING_SCOPE_UNVERIFIED|2025 combination versus February2026 merger needs pro-forma explanation; adjusted EBITDA versus net profit unresolved; long33s ASR sentence retained.
83|84|May1 Fast Entry rule follows February announcement before June IPO target|S043.20-S043.25|UNVERIFIED|Calendar is creator reconstruction; June explicitly target not completed listing; source rule document absent.
88|88|Each video requires20+research hours|S051|ATTRIBUTED_SELF_REPORT|Sponsor self-description, not measured production-time dataset.
92|93|Sponsor dictation four times faster, any app/device|S057.1-S058.5|SPONSORED_CLAIM_UNVERIFIED|Demo45versus220wpm is selected comparison, not independent controlled benchmark; universal support claim untested.
95|99|Saudi/OPEC relationship,40year dollar peg,89%FX dollar side|S059.3-S063.0|SPONSOR_EXAMPLE_PARTLY_CHECKED|Demonstration corrections are preserved; BIS89.2%2025 versus88.4%2022; two currency sides sum200%; causality and precise peg date not certified.
110|111|200+products and$600B track Nasdaq100 and automatically buy entrants|S068|PARTLY_CHECKED|Yahoo excerpt supports dated assets; AUM is not promised net inflow to new component; replication/derivatives differences omitted.
112|116|Seasoning changes from3months to15tradingdays|S071.1-S073.8|UNVERIFIED_RULE_DETAILS|On-screen rule summary lacks primary methodology, eligibility restrictions and evaluation dates;15tradingdays roughly3weeks not calendar15days.
118|121|Prior floatminimum10%, SpaceX4-5%, minimum gone and qualifies|S074.3-S075.3|UNVERIFIED_RULE_DETAILS|Cartoon illustrates claim but no primary methodology; removing one condition does not guarantee all eligibility criteria satisfied.
125|126|Float under20%treated3xlarger;4→12%,5→15%|S078.3-S079.3|UNVERIFIED_RULE_DETAILS|Arithmetic correct if premise applies; weighting adjustment versus eligibility/float capitalization rule unverified and may be oversimplified.
129|131|ETFs legally required to triple float and buy SpaceX after15days|S082-S084.1|UNVERIFIED_LEGAL_AND_CAUSAL_CLAIM|Index-provider methodology is not automatically statutory mandate; weighting formula, timing and actual fund trades not evidenced.
133|135|OpenAI/Anthropic likely list thisyear under rules tailored to their class|S085.3-S085.12|FORECAST_AND_INTENT_UNVERIFIED|Reported aspirations and inferred rule intent are not completed IPOs or guaranteed configuration.
138|138|Usual IPO retail5-10%, SpaceX target30%|S089.0-S089.3|UNVERIFIED|Comparison denominator should be offering allocation, not total outstanding float; target not final allocation.
139|140|CFO makes on-record loyalty-based retail allocation statement|S089.4-S089.6|SOURCE_MODALITY_CONFLICT|Article says private virtual meeting reported by anonymous sources; not on-record. Screen Bret Johnsen versus ASR Brett Johnson. Motive interpretation exceeds excerpt.
142|146|Early forced buyers, later insider sellers, retirement absorbs peak valuation|S091.8-S093.3|PLAUSIBLE_HYPOTHESIS|No lockup schedule, trades or realized peak valuation shown; George Noble criticism is attributed opinion, not proof.
147|149|Any US index retirement account inevitably owns SpaceX within weeks|S094.0-S094.14|OVERGENERALIZATION_UNVERIFIED|Fund benchmark/eligibility/replication differ; proposed listing and index entry conditional, not universally guaranteed.
150|154|Financial media omits mechanism because it is not clickable|S098-S101.0|SOURCE_INTERPRETATION_UNVERIFIED|No media coverage census or click analytics; creator headline comparison.
157|165|Passive lowfees/diversification automate purchases of included components|S102-S106|ILLUSTRATIVE_SIMPLIFICATION|General mechanism illustrated; fees/results vary by fund; final someone entered statement not proof of actual SpaceX inclusion.'''
rows=[]
for i,l in enumerate(data.splitlines(),1):
 a,b,c,v,status,n=l.split('|');a,b=int(a),int(b);rows.append(dict(claim_id=f'C{i:02}',start_sec=s[f'T{a:04}']['start_sec'],end_sec=s[f'T{b:04}']['end_sec'],sentence_ids=f'T{a:04}-T{b:04}',claim_summary=c,claim_class='SOURCE_CLAIM',on_screen_support=v,verification_status=status,fact_check_priority='HIGH',notes=n+' ASR figures and names uncertified; no direct listening; supplied-source review, no live fact-check.'))
with (p/'FINANCE_CLAIMS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
q=json.load(open(p/'QA.json'));q['counts']['financial_claims']=len(rows);q['audiovisual_status']='AUDIOVISUAL_QA_PARTIAL';(p/'QA.json').write_text(json.dumps(q,indent=1));print(len(rows),'claims')
