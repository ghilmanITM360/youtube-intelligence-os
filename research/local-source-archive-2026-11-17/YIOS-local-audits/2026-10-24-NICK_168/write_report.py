from pathlib import Path
import json,hashlib,collections,datetime
R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';O=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_168');r=json.loads((B/'audit-batches/NICK_168_READ_RECEIPTS.json').read_text());a=json.loads((B/'audit-batches/NICK_168.json').read_text())['reviews'][0];i=json.loads((O/'final-integrity.json').read_text());receipt=r['receipts'][0];pf=r['calculation_receipts'][0]['results'];pub=json.loads((O/'publication.json').read_text()) if (O/'publication.json').exists() else {'status':'VALIDATED_LOCAL_PENDING_PUBLICATION'}
text=f'''# Machine A — NICK_168 individual deep-audit result

Dated 2026-10-24. Repository: `{R}`. Branch: `research/finance-economics-intelligence`. Accepted parent: `7e7c14016141977cd77fda48bcc6650aa6c3f517`. PR #36 remains open/draft; Machine A is the published sole Finance writer and Machine B remains released.

## Executive finding

`TdNH3QP3qao` — **Who Can Actually Afford a $50K Truck in 2026?**, Nick Invests, uploaded **2026-05-24T22:16:00Z**, registered duration **1,295 seconds /21:35**. DS-000022 original population, channel `UCXzNNA2ngRpRiWvyA7eGd6w`. The full stored text, actual thumbnail, financial claims and all six existing dimensions were researched under `COMPLETE_LIMITED_EVIDENCE`; this does not certify the original audio or private analytics.

The central approval-versus-affordability lesson is useful. Several supporting definitions and calculations need qualification. A $50K, zero-down,7%,84-month loan gives **$754.63/month**, **$13,389.26 interest**, and **$44,262.64 balance after12 payments**. At the assumed $40K resale, negative equity is **$4,262.64**, not $5,700. The stated total-transportation version of20/4/10 implies about **$192K gross annual income**, not $150K, using its own operating assumptions. $150K is not the top15% household threshold: the available2024 Census distribution puts26.1% of households at or above it. The20.3% payment statistic describes financed new purchases, not all purchases.

$700 invested each month for30years at8%/12 reproduces **$1,043,251.61 nominal**. It requires a continuous30-year contribution stream; a single seven-year loan saving does not establish that stream. This neither guarantees retirement at65 nor supplies a retirement withdrawal plan. The transcript does not invoke the4% rule. Cash-flow affordability and economic ownership costs must be separate to avoid counting principal and depreciation twice.

## Provenance and preservation

Initial local/origin/live Finance/PR36 heads matched the accepted parent. Tracked tree was clean; the existing stash and the three unrelated untracked roots were preserved. No branch switch, fetch, clone, worktree, delegation, reset, rebase, paid acquisition, reset-credit use or unrelated canonical correction occurred. The existing Visual Forensics video003 external checkpoint was not modified. Claude10878 had repository cwd but its completed external visual-session log retained mtime1792858357; other identified Claude sessions used offline-map. No competing Finance writer was observed. Remote refs cannot prove absence of unpushed work on another machine; published ownership and explicit owner authorization govern this run.

Initial resource order: five-hour60%, weekly31%, then context(no visible warning; exact percentage unavailable), disk14GiB free/97%used. Interim checkpoints63/31,67/32,70/32,73/33 consumed. No reset credits or paid balance used. Final live resource evidence appears below.

Canonical SQLite was opened read-only/immutable, transcript row1921. Registered metadata matches video identity, title, duration, counts and timestamp; archive header also supplies explicit UTC. Frozen snapshot2026-09-11 is source-declared scrape day with unknown timezone:59,539views/1,400likes/524comments. No live counts replaced it.

## Entire transcript and image receipts

Canonical text: **{receipt['character_count']} characters /{receipt['canonical_utf8_bytes']} UTF-8 bytes**; SHA-256 `{receipt['Text_SHA256']}`. Database/source word count3427 differs from regex coverage counter3491 and whitespace count{receipt['canonical_whitespace_word_count']}; these are tokenizer conventions, not invented missing speech.

Archive: `{receipt['archive']}`; SHA-256 `{receipt['archive_sha256']}`.
Member: `{receipt['archive_member']}`; **{receipt['archive_member_bytes']}bytes/{receipt['archive_member_lines']}lines**, SHA-256 `{receipt['archive_member_sha256']}`. Original member and canonical text are preserved externally as distinct artifacts; no normalization overwrote either.

Three fully read, contiguous, end-exclusive canonical ranges:
'''
for b in receipt['range_boundary_witnesses']:text+=f"\n- [{b['start']},{b['end']}): first80 `{b['first80']!r}`; last80 `{b['last80']!r}`.\n"
text+=f'''\nOpening witness: “{receipt['first_text_witness']}”

Closing witness: “{receipt['last_text_witness']}”

Auto-generated untimed captions are not verified narration. Preserve disfluencies such as “I I,” “20 25,” “Facebook Marketplace” as a verb and captioned prices without currency signs. No script gap was established in stored text, but audio completeness remains unverified. No intonation, music, edits, motion, graphics or timed retention is inferred.

Authentic registered URL: [{a['thumbnail']['image_source']}]({a['thumbnail']['image_source']}); fetched2026-10-24. Image **1280×720 JPEG/{receipt['image_bytes']}bytes**, SHA-256 `{receipt['image_sha256']}`. Native and aspect-preserved320×180 inspected. Original bytes retained at `audit-batches/NICK_TdNH3QP3qao.jpg`, identical to external acquisition. White background, cartoon man, grey pickup in red chains, beige$50,000 tag, bold$50K...WHO? and curved black arrow reinforce cost and captivity. Exact historical artwork, model configuration and performance effect are unavailable.

## Frozen performance reconstruction

Method unchanged: same channel/format/snapshot, ages>=7days, peer age0.5–2target age, nearest absolute age difference thenVideo_ID; unweighted median views/storedfour-decimalage. Ten peers, first-five sensitivity. STRONG>=2;WEAK<0.5;otherwiseTYPICAL. This is lifetime-rate normalization, not current velocity or causal attribution.

Target59,539/109.0722 = **{pf['target_vpd']:.11f}views/day**. Ten-peer median **{pf['10']['median']:.11f}**, ratio **{pf['10']['ratio']:.11f} STRONG**. Five-peer median **{pf['5']['median']:.11f}**, ratio **{pf['5']['ratio']:.11f} STRONG**. Frozen stored ratio7.42186 reproduces. Both classifications agree.

|Order|Peer Video ID|Stored age days|Frozen views|Views/day|
|---|---|---:|---:|---:|
'''
for j,p in enumerate(pf['peers'],1):text+=f"|{j}|`{p['Video_ID']}`|{p['age']:.4f}|{p['views']}|{p['vpd']:.11f}|\n"
text+='\nNo CTR, impressions, watch time, retention, traffic sources, revenue, subscriber conversion or title/thumbnail causal effect is available. The creator’s assertion that most viewers left during the math is unverified.\n\n## All material claim groups\n\nExact quotes use zero-based canonical character offsets, end exclusive. Original whitespace is preserved in JSON receipts; the display below flattens line breaks only. Institutional evidence and mathematical correctness are separate. Unsupported means unverified, not automatically false.\n'
for c in r['financial_claim_locations']:
 text+=f"\n### {c['claim_id']} — {c['classification']}\n\nLocation[{c['start_char']},{c['end_char']}); type`{c['claim_type']}`.\n\n> {' '.join(c['original_quote'].split())}\n\n{c['assessment']}\n\nSources: {', '.join(c['source_ids']) or 'No matching original source established; rhetorical or unverified claim.'}\n"
text+='\n## Dated source and definition ledger\n\nAvailability is assessed against2026-05-24, not the research date. Current manufacturer pages are explicitly not historical price captures. September2026AAA results are not used; current index material is retrospective only.\n'
for s in r['primary_source_receipts']:
 text+=f"\n### {s['source_id']}\n\n[{s['source_id']}]({s['url']}). Publication/review date: {s['source_date']}. Observation period: {s['observation_period']}. **{s['publication_applicability']}**.\n\n{s['finding']}\n\n{s['methodology']}\n"
 if s.get('saved_source_sha256'):text+=f"\nSaved original `{s['saved_source_path']}`: {s['saved_source_bytes']}bytes; SHA-256`{s['saved_source_sha256']}`.\n"
text+='\n## Independent numerical receipts\n\n'
for j,c in enumerate(r['calculation_receipts'],1):
 text+=f"### R{j}: {c['method']}\n\nFormula: `{c['formula']}`\n\nAssumptions: {c['assumptions']}\n\n"
 results=c['results']
 if j==1: text+='Exact peer table and both results are above; full source metadata and peer IDs are in the JSON receipt.\n\n'
 else:text+='```json\n'+json.dumps(results,indent=2)+'\n```\n\n'
text+='Independent iteration of all84 loan payments and360 monthly investment contributions agrees with the closed forms. The separate five-year purchase/resale/loan-balance identity reconciles capital cost without double counting. All assumptions are nominal unless explicitly labeled analyst inflation sensitivity. No guaranteed return, resale, retirement date, perpetual income or universal affordability threshold is inferred.\n\n## Six research dimensions\n\n'
for key in ['title','thumbnail','script','topic','virality']:text+=f"### {key.upper()} — COMPLETE_LIMITED_EVIDENCE\n\n{a[key]['analysis']}\n\n"
text+='### PERFORMANCE — COMPLETE_LIMITED_EVIDENCE\n\nBoth frozen peer reconstructions above pass; source public counts and existing benchmarks remain unchanged.\n\n'
text+='## Integrity, tests and publication\n\n```json\n'+json.dumps(i,indent=2)+'\n```\n\n'
text+='Fresh audit and bounded research validators pass.34 focused Finance tests pass;2 workbook-formatting tests pass. Full regression: **460passed,1failed,5warnings,38.11seconds**. The sole failure is `LedgerChecksumTests.test_all_csv_ledger_datasets_are_clean`, DS-000028-F020 `.gitattributes` expected627bytes/SHA1970079d0da551fe6400b93d55c5f8cf9be2beeb628089457be11a6d0a79f43d; actual895bytes/SHA93d4461c54929f06d8977a3741b20dbf788bcfffbb4d2f2234027e914a230222. Actual bytes independently equal the accepted NICK_167 parent. No unrelated ledger repair, ignored assertion or new failing test. Full suite is not green.\n\nAll966detail rows×8 research sections/statuses match JSONL;966 originals,646 expansion metadata-only records and1612unique IDs preserved. Only target cells change in All Finance Videos and Detailed Research; Channel Directory values are identical. All cell styles, table names and freeze panes compare equal to the accepted parent. Dashboard dependent counts/provenance change. Formula/object-placeholder scan0; maximum cell text28190characters. Four sheets and target row437 reviewed visually; prior and next rows remain intact. Native Microsoft Excel desktop recalculation was not tested.\n\nFresh tracked secret scan0; exact diff and whitespace verified before commit. The focused suite and full regression ran after export completed. No prior NICK_165/166/167 finding was changed.\n\nPublication checkpoint:\n\n```json\n'+json.dumps(pub,indent=2)+'\n```\n\n'
text+='## Queue and next safe task\n\nValidator master-order next remains legacy partial `TFtBWn9CWOU`, scope`OPENING_95_ENDING_65_WORDS_ONLY`,IN_PROGRESS; it was not overwritten or silently reordered. Owner-approved genuinely untouched policy selected this target. Next genuinely untouched original is **`Tg_n8zGC7qw` — At What Age Most People Hit $100K, $500K & $1M (Not What You Think)**, expectedNICK_169 only on a new authorization and fresh resource/ownership check. No next video was started.\n\n## Unresolved evidence and bounded recommendations\n\nRetain limited-evidence status. The historical MSRP/trim configuration, model-specific depreciation, installed tires, Camry cost ledger and Strategic Vision questionnaire/tables remain unresolved; no paid data is necessary to mark those limits honestly. Do not import the NICK_165 configuration findings as facts here. Correct only this video’s loan balance, total-cost rule arithmetic, buyer/statistic denominators and investment horizon interpretation. Preserve the useful approval distinction, fictional budget arithmetic and work-use exception. A reusable original treatment should itemize one real out-the-door quote, distinguish gross/net budgets and cash/economic costs, and model alternative vehicle-replacement horizons.\n\nDurable evidence folder contains the original transcript/member/image,3 original source PDFs,read receipts,source/claim/calculation ledgers,frozen peer reconstruction,validator/test logs,workbook images,parent-failure proof and complete publication verification. `EVIDENCE_SHA256SUMS` covers durable files except itself and dependency symlink contents. Historical authoring scripts are construction aids; canonical published packet and receipts are the final authority. Do not rerun scripts blindly over a completed target.\n'
(O/'MACHINE_A_NICK_168_DEEP_AUDIT_RESULT.md').write_text(text)
print('Report written',len(text))
