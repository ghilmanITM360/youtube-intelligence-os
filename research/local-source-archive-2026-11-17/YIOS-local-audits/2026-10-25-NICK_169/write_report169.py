from pathlib import Path
import json,hashlib
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=json.loads((B/'audit-batches/NICK_169_READ_RECEIPTS.json').read_text());pr=json.loads((O/'provenance.json').read_text());q=rec['queue_distinction'];integ=json.loads((O/'final-integrity.json').read_text());pub=json.loads((O/'publication.json').read_text()) if (O/'publication.json').exists() else {'state':'VALIDATED_AWAITING_PUBLICATION'};usage=json.loads((O/'final-usage.json').read_text()) if (O/'final-usage.json').exists() else {'five_hour_used_percent':15,'weekly_used_percent':2,'reading':'prepublication'}
text=f'''# Machine A — NICK_169 deep audit result

Date: 2026-10-25, Asia/Karachi. Video: `Tg_n8zGC7qw`, Nick Invests, “At What Age Most People Hit $100K, $500K & $1M (Not What You Think)”. Publication status: **{pub['state']}**.

## Executive finding
The compounding lesson is conditionally useful, but the title's national wealth-age schedule is not supported by a representative first-attainment study. The narration starts with a selection warning and ends by calling a mixed set of figures the average American's timeline. Community respondents, sampled millionaires, adults, families and households are different denominators. Do not replace those ages with interpolated SCF age-band medians.

Verified numerical issues include 25/130 = 19.23077%, not12%, with the additional invalid person/household division. The generational comparison changes a wealth percentile into top-income earners. The stored caption174 differs from the identified rent table1174; audio was not checked, so spoken error is unverified. The original cohort paper itself uses an inconsistent median percentage, which is disclosed rather than silently repaired.

All six existing dimensions are COMPLETE_LIMITED_EVIDENCE. This certifies the documented transcript, current authentic image, frozen public benchmarking and bounded claim research. It does not certify actual audio, editing, upload-era artwork or private analytics.

## Authentication, ownership and provenance
Owner explicitly confirmed the new ChatGPT account after local nonsecret identity matched the live usage account ID. No tokens, credentials or authentication payloads were exported to research. Fresh starting usage was1%five-hour/0%weekly; the former account's81%/34% was not reused. No reset credits or paid acquisitions used. Latest reading: {json.dumps(usage)}.

Accepted parent: `2bbc0a74c1f149c21168657c6e2209bd9e681101`; local/origin/live Finance/PR36 matched before work. PR OPEN/DRAFT. Published ownership document has MACHINE_A_SOLE_WRITER_ACCEPTED and MachineB released. The additional Claude process in this checkout was verified as the separate Visual Forensics video003 continuation; other Claude processes were in offline-map. No session interrupted or messaged. Disk initially13GiB free. Numeric context capacity unavailable; no visible pressure warning. This continues the complete checksummed handoff, whose five listed evidence-file checksums passed unchanged.

Registered original DS-000022/channelUCXzNNA2ngRpRiWvyA7eGd6w. Archive header establishes upload `2025-11-28T10:22:00.000Z`, duration1235seconds/20:35. Frozen2026-09-11:115774views,2000likes,363comments; metric-day timezone unknown. Target was genuinely untouched, not merely referenced as a peer. Validator's first unresolved master record remains legacy `TFtBWn9CWOU`; opening95/ending65-only IN_PROGRESS evidence is preserved. Owner-approved genuinely-untouched policy selected this target without modifying the legacy record.

## Full transcript and authentic image
SQLite opened read-only, transcripts row2089. All19509characters read in contiguous [0,8000),[8000,16000),[16000,19509) ranges with exact boundary witnesses in canonical receipts. Canonical SHA `{pr['computed_sha256']}`. Archive `{pr['archive']}` SHA `{pr['archive_sha256']}`. Member `{pr['member']}`, {pr['member_bytes']}bytes, SHA `{pr['member_sha256']}`. Archive word count3110 and coverage-registry token count{rec['receipts'][0]['coverage_token_count']} are recorded separately; counting conventions are not silently merged. Auto-generated English, untimed, not human/audio verified. Stored disfluencies include h100000, wealth-b buildinging and an abrupt repeated first. Complete stored ending read; completeness against narration remains unknown.

Authentic registered [thumbnail](https://i.ytimg.com/vi/Tg_n8zGC7qw/maxresdefault.jpg) fetched2026-10-25:1280×720, SHA `{sha(O/'registered-thumbnail.jpg')}`. Native and aspect-preserved320×180 inspected. White background;large black100K→1M,cartoon man/cash jar,stopwatch,arrow and stacked bills. Numbers and main visual hierarchy remain legible on mobile;fine jar detail becomes small. Title asks age,image promises progression. Cash iconography risks implying liquid assets when the narration discusses total wealth. Historical artwork,CTR and A/B effects unknown.

## Frozen performance
Exact stored age286.5681days. Target115774/286.5681 =404.0017015153views/day. Same channel,format,snapshot,age≥7,age ratio0.5–2;nearest absolute age distance thenVideo_ID;four-decimal stored ages. Ten median111.9088907551 gives3.6100947725 STRONG. First-five median128.4536124647 gives3.1451174768 STRONG. Tier stable;STRONG≥2,WEAK<0.5. No refreshed counts or causal packaging inference.

|Peer|Age days|Views|Lifetime views/day|
|---|---:|---:|---:|
'''
for p in rec['calculation_receipts'][0]['results']['peers']:text+=f"|`{p['Video_ID']}`|{p['age']:.4f}|{p['views']}|{p['vpd']:.10f}|\n"
text+='''
## Wealth definitions and source vintage
Net worth is assets minus liabilities; invested portfolio, liquid savings, retirement-account balances and home equity are separate concepts. A wealthy homeowner may have limited liquid investments. A portfolio's total return can include unrealized price changes and is not necessarily cash income. An8% accumulation illustration is not an8% safe withdrawal policy. No4%rule appears in this transcript.

Four distinct quantities must remain separate: median wealth within a reference-person age band;share above a threshold in that band;retrospective individual/family first-crossing age;prospective expected attainment age conditional on a person's inputs. Cross-sectional age-band statistics do not establish the last two. A mean is not “most”;a percentile among reported successes is not an eventual-attainment probability for everyone. Household formation,cohorts,survivorship,selection,transfers and asset composition matter.

The historical2023 SCF report is preserved in original2022 dollars. Current rebased2025-dollar tables and the independently verified October9,2026 SCF release are retrospective only. Sources dated after upload were not used to claim the creator should have known them. Original NLSY cohort research does contain longitudinal work/family histories,but that does not make it a national first-million age study.

## Source ledger
The following dates,definitions and access limitations are the source-of-truth receipts. Downloaded primary PDFs and web extraction receipts are checksummed externally. A source being original does not make every extrapolation from it valid.

'''
for s in rec['primary_source_receipts']:
 text+=f"### {s['source_id']}\n[{s['url']}]({s['url']})\n\nDate: {s['source_date']}. Observation: {s['observation_period']}. Vintage: `{s['publication_applicability']}`. Access: {s['access_scope']}.\n\n{s['finding']}\n\nLimit: {s['methodology']}\n\n"
text+='## Exact located claim ledger\n\nCoordinates are canonical zero-based characters,endexclusive. Full original wording is preserved below;assessment is separate from arithmetic. Repeated material claims receive separate locations.\n\n'
for c in rec['financial_claim_locations']:
 text+=f"### {c['claim_id']} — [{c['start_char']},{c['end_char']}) — {c['classification']}\n\n> "+c['original_quote'].replace('\n','\n> ')+f"\n\n{c['assessment']} Sources: {', '.join(c['source_ids'])}.\n\n"
text+='## Independent calculation receipts\n\nAll contribution sensitivities are analyst examples,not inputs claimed by the creator. These do not estimate national milestone ages. Formula results independently checked using monthly/yearly recurrences,not merely restated from one closed form.\n\n'
for c in rec['calculation_receipts'][1:]:text+='### '+c['method']+'\n\n```json\n'+json.dumps(c,indent=2)+'\n```\n\n'
text+='''## Six dimensions and editorial implications
TITLE: numerical milestones and age comparison create a concrete promise;MostPeople overstates the source populations. THUMBNAIL: cash,time and progression complement the question but risk cash/net-worth conflation. SCRIPT: social-comparison hook,ladder,metaphors,repetition and generational turn create clear textual structure;selection caveat disappears at the close. TOPIC: useful compounding and benchmarking require clear wealth/age definitions. PERFORMANCE: above frozen same-channel peer medians in both windows. VIRALITY: plausible attention devices remain hypotheses;exposure,CTR,retention and recommendation causes are unavailable.

An original follow-up could show distributions rather than deadlines,with separate panels for age-band stocks,threshold shares,selected first-crossing histories and contribution-dependent scenarios. Add housing equity versus liquid funds and a variable-return drawdown. This is an editorial experiment,not a promised performance outcome.

## Validation and preservation
'''+json.dumps(integ,indent=2)+'''

Fresh structural audit and bounded research validators PASS;34focusedFinance tests PASS;2workbook-formatting tests PASS. Full regression:460passed,1failed,5warnings,49.74seconds. The sole failure is LedgerChecksumTests.test_all_csv_ledger_datasets_are_clean,DS-000028-F020 .gitattributes. Expected627bytes/SHA1970079d0da551fe6400b93d55c5f8cf9be2beeb628089457be11a6d0a79f43d;actual895bytes/SHA93d4461c54929f06d8977a3741b20dbf788bcfffbb4d2f2234027e914a230222. Actual bytes equal accepted parent. No new failing tests;fullsuite is not green. No unrelated repair.

Workbook recalculated in ArtifactTool,built with the existing builder in a disposable external runtime copy;nativeMicrosoftExcel recalculation NOT_TESTED. Four sheet renders and targetrow438 inspected;all cell styles,tables,freeze panes and unrelated values match accepted workbook. One target row changed in JSONL and each of seven projections. All prior444completed records,legacy partial,966originals,646expansion identities/metadata and26fingerprints preserved. No rawsource,VisualForensics,stash,untrackedroot or priorNICKrecord edited. NICK165corrections remain separate. Finalcounts445complete/1167remaining=521original+646expansionpending;42registeredchannels.

## Publication, next safe task and unresolved gaps
'''+json.dumps(pub,indent=2)+f'''

Next genuinely untouched original: `{q['next_genuinely_untouched_original']}` — {q['next_title']}. Its audit was not started. Legacy master-order partial remains separately unresolved. Source gaps,original forum rawresponses,unverified housing-series reconstruction,cohort-source percentage inconsistency,audio/current-image history and private analytics are explicitly preserved limitations. Billing-blockedActions were not rerun. See publication.json for current exact-head hosted evidence rather than treating historical CI as current.
'''
(O/'MACHINE_A_NICK_169_DEEP_AUDIT_RESULT.md').write_text(text)
print('Wrote detailed report',len(text),'characters')
