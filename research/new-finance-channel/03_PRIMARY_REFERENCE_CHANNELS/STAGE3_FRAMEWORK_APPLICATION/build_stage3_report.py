import sys,json,csv,sqlite3,statistics as st,datetime as dt,pathlib,markdown
sys.path.insert(0,'../STAGE2_SIX_REPORTS'); import build_data as B
D=pathlib.Path('.')
R=json.load(open('stage3_results.json')); T=json.load(open('stage3_topics.json'))
def g(feat,s='excl_pb'): return next(r for r in R['res'][s] if r['feat']==feat)
def row(feat,s='excl_pb'):
    r=g(feat,s)
    if 'p' not in r or r.get('p') is None: return 'too few'
    return f"{r['n_with']}/{r['n_without']}; PI {r['med_with']:.2f} vs {r['med_without']:.2f}; p={r['p']:.2f}; channels agree {r['chan_agree']}/{r['chan_tot']}"
def rowo(feat): return row(feat,'older60')
ref=sqlite3.connect('file:../../../../data/knowledge/reference_knowledge.db?mode=ro',uri=True)
ids=['FR-TITLE-01','FR-SEO-01','FR-VC-05','FR-VC-06','FR-HOOK-01','FR-VC-04','FR-VC-01','FR-16C-16','FR-SCR-05','FR-BT-01','FR-SCR-03','FR-INTRO-02','FR-TITLE-03','FR-16C-06','FR-16C-13','FR-SCR-01']
prov=[]
for i in ids:
    x=ref.execute('select rule_id,framework_version,member_id,locator,rule_class from ref_rule where rule_id=?',(i,)).fetchone()
    mem=ref.execute('select filename from ref_source_member where member_id=?',(x[2],)).fetchone() if x and x[2] else None
    prov.append((x[0],x[1],x[2],(mem[0] if mem else ''),x[3],x[4]))
# launch cadence
T0=dt.date(2026,11,19); launch=[]
for slug,name in B.CH.items():
    nm,cid,Rw=B.load(slug); ds=sorted(r['d'] for r in Rw if r['d'] and not r['member'])
    f=ds[0]; launch.append((nm,str(f),sum(d<=f+dt.timedelta(days=13) for d in ds),sum(d<=f+dt.timedelta(days=29) for d in ds),len(ds)))
# per-video applications
F=list(csv.DictReader(open('stage3_features.csv')))
ex=[]
for ch in ['MonkeyExplains','Casual Finance','Monkey Economics','Crayon Capital','Paper Billions','Capital Case']:
    V=sorted([r for r in F if r['channel']==ch],key=lambda r:-int(float(r['views'])))[:2]
    ex+=V
yn=lambda v:'yes' if v=='True' else 'no'
exrows='\n'.join(f"| {r['channel']} | [{r['title'].replace('|','/')}]({r['url']}) | {int(float(r['views'])):,} | {float(r['pi']):.1f}x | {yn(r['title_le55'])} | {yn(r['fam_warning/crisis'])} | {yn(r['title_digit'])} | {yn(r['open_digits'])} | {yn(r['open_dated'])} | {yn(r['kw_in_open'])} | {yn(r['echo'])} | {yn(r['cta_early'])} | {yn(r['dur_ge8'])} |" for r in ex)
def pct(a,b): return f"{100*a/b:.0f}%"
orr=R['orr']; rep=R['rep']
orrrows='\n'.join(f"| {c} | {v['n']} | {v['ge1']} | {v['ge2']} | {v['ge5']} | {v['mx']:.1f}x | {v['med']:.2f}x |" for c,v in orr.items())
launchrows='\n'.join(f"| {a} | {b} | {c} | {d} | {e} |" for a,b,c,d,e in launch)
trows='\n'.join(f"| {t['topic']} | {t['channels']} | {t['long']} | {t['shorts']} | {t['views']:,} | {t['med_pi']} | {t['winners']} | {t['first'][0]} {t['first'][1]} |" for t in sorted(T,key=lambda t:-t['views']))
provrows='\n'.join(f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a,b,c,d,e,f in prov)
md=f"""# Stage 3: frameworks applied to the six channels' actual videos (2026-11-19)

Scope: the six fixed channels only. Sample: **{R['n']} long-form videos** with public views and a transcript (MonkeyExplains 62 of its 64 public long videos; Paper Billions 6). Shorts and Member Edition items are excluded from text tests. Read-only on the DB; no paid run; nothing committed. Code: `stage3_apply.py`, `stage3_topics.py`, `build_stage3_report.py`; per-video features: `stage3_features.csv`; raw results: `stage3_results.json`, `stage3_topics.json`.

## 1. What "applied" means here (honest scope)

| Source | What it is (authority) | What was applied | How it was encoded |
|---|---|---|---|
| **DS-000011** (17 files) | Creator-education and creative library; creative heuristics, not YouTube facts | 9 of its 17 encoded rules (TR-011-002, -003, -004, -007, -010, -011, -012, -015, -016) that can be tested on text | `data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json` and the framework DB rows that point to DS-000011 documents |
| **DS-000018** (63-tab Google Doc) | Third-party creator commentary on the "2026 algorithm"; context, not platform fact (earlier audit: 10 of 33 claims supported, 12 partial, 1 contradicted, 8 lacking primary support, 2 not verifiable; REUSED, not re-run) | Only the claims and recommendations that competitor public data can test: CLM-003, CLM-009, CLM-015, CLM-018, REC-005, REC-006, REC-007, REC-009 | the same JSON (TR-018-*) |
| **YouTube Automation Master Playbook** (556 pp) | Course lessons plus prompts; Part D only is official-source | Principles P01, P04, P06, P07, P08, P09 and the "8+ minute sweet spot" | `00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md` principle table (REUSED); title families re-implemented by us as 9 regex proxies (INFERRED, not the PDF's own list of 10) |
| **Framework DB** `data/knowledge/reference_knowledge.db`, framework version **v1** | 33 rules (27 creative heuristics, 1 empirical hypothesis, 2 duplicates, 3 not applicable) | 16 rule rows listed with their source rows in section 6: 10 tested on text, 3 only partly (title-word echo), 3 not tested or not evaluable | `ref_rule` rows; member and locator recorded below |

Limits that apply to everything below: the DS and Playbook source files were NOT re-read page by page in this stage (reading coverage is stated in `01_PROJECT_OVERVIEW/01_KNOWLEDGE_BASE_FORENSIC_ANALYSIS.md`); I applied the rules as already encoded. No CTR, retention or impressions exist, so every test compares public views, expressed as **PI = views / that channel's own long-form median**, which removes channel size. Views depend on age; a second sample limited to videos older than 60 days is reported. About 20 features were tested on 3 samples, so one or two p-values below 0.05 are expected by chance. Paper Billions (11 days old) is excluded from the primary sample. Nothing here shows causation.

## 2. Rule-by-rule results (each row: which framework, which rule, what was measured)

Format of the result column: videos with / without the feature; median PI with vs without; Mann-Whitney p; number of channels where the "with" group has the higher median. Primary sample = 5 channels, 166 videos.

| # | Source and rule | Operationalisation on real videos | Result (primary sample) | Older-than-60-days check | Verdict |
|---|---|---|---|---|---|
| 1 | Playbook P07 "title psychology families"; DS-000011 TR-011-013 | Title matches crisis/collapse/bubble/recession words | {row('fam_warning/crisis')} | {rowo('fam_warning/crisis')} | Nominal signal only: 4 of 4 channels agree, but p=0.007 does NOT survive correction for 22 tests (threshold 0.0023) and the family overlaps the AI-bubble and crash topics (review, section 11). HYPOTHESIS |
| 2 | Playbook P07 (other 7 families) | curiosity/threat, explainer, story/person, contrarian, urgency, question, superlative | all p >= 0.19 (e.g. question {row('fam_question')}) | no p < 0.05 | NOT SUPPORTED |
| 3 | Playbook P08, DS-000011 TR-011-011, FR-VC-05 (specificity and numbers) | digit in title; digits or money/percent words in first 60 opening words | title {row('title_digit')}; opening {row('open_digits')} | title {rowo('title_digit')}; opening {rowo('open_digits')} | NOT SUPPORTED (titles with digits are slightly lower) |
| 4 | Playbook P09 title mistakes (ALL CAPS) | an ALL-CAPS word of 3+ letters | {row('title_caps')} | {rowo('title_caps')} | DIRECTIONAL (caps lower in 2 of 5 channels, not significant) |
| 5 | FR-TITLE-01 and TR-011-004 (key info in first ~55 chars; short title) | title <= 55 characters | {row('title_le55')} | {rowo('title_le55')} | rule is met by 93% of titles, so it cannot discriminate (only 12 exceptions) |
| 6 | Playbook "8+ min sweet spot" (an ad-eligibility rule officially, not a view rule) | duration >= 8 min | {row('dur_ge8')} | {rowo('dur_ge8')} | DIRECTIONAL, 3 of 3 channels, only 17 videos under 8 min. Spearman of transcript words vs PI = {R['cont']['words'][0]:.2f} (p={R['cont']['words'][1]:.3f}), duration {R['cont']['dur'][0]:.2f} (p={R['cont']['dur'][1]:.3f}): longer videos sit slightly higher within a channel. Confounded by topic |
| 7 | DS-000011 TR-011-002 / FR-HOOK-01 / TR-011-012 (3-step hook, contrarian snapback) | a "but / however / the problem / actually / nobody / never..." marker in the first 120 words | {row('open_contrarian')} | {rowo('open_contrarian')} | **PROXY INVALID**: 87% of openings contain such a word, and the few without score higher. A word search cannot detect a snapback; the qualitative reading of the top 8 openings per channel (Stage 2 section 9) is the only real evidence, and it shows fact-then-contradiction at Casual Finance and problem-first at MonkeyExplains/Paper Billions |
| 8 | DS-000011 TR-011-010 / FR-VC-01 (audience pain point; speak to the viewer) | "you/your" in first 75 words | {row('open_you')} | {rowo('open_you')} | NOT SUPPORTED |
| 9 | FR-VC-06 (timeliness) and DS-000018 REC-007 (early specific names/dates) | dated reference (year, month, "last week", "days ago", "just") in first 75 words | {row('open_dated')} | {rowo('open_dated')} | DIRECTIONAL (4 of 5 channels); effect fades in the older sample and top videos do not show it (section 7), so it may be recency |
| 10 | DS-000018 REC-007 (names, places early) | 3+ named entities in the first 60 words | {row('open_entity')} | n/a | 95% comply, cannot discriminate |
| 11 | FR-SEO-01 (title keyword spoken in first ~30 s) | at least half of the title's content words appear in the first 75 words | {row('kw_in_open')} | {rowo('kw_in_open')} | NOT SUPPORTED. Only 17% of videos say their title words in the first 30 s; a missing keyword does not lower views here |
| 12 | FR-16C-16 (echo: ending returns to the title/theme) | a title content word appears in the last 150 words | {row('echo')} | {rowo('echo')} | WEAK, borderline (older sample p<0.05, primary p=0.08, 4 of 5 channels). Needs replication |
| 13 | FR-SCR-05 (CTA and monetisation placement) | subscribe/like/sponsor wording anywhere; in the first 15% | any {row('cta_any')}; early {row('cta_early')} | n/a | descriptive only; no relation |
| 14 | FR-BT-01, FR-16C-03, TR-011-015 (BUT/THEREFORE, avoid "and then") | per-1000-word rates of but/however/yet vs therefore/because/that's why vs "and then", Spearman with PI | but {R['cont']['but_rate'][0]:.2f} (p={R['cont']['but_rate'][1]:.2f}); therefore {R['cont']['therefore_rate'][0]:.2f} (p={R['cont']['therefore_rate'][1]:.2f}); and-then {R['cont']['andthen_rate'][0]:.2f} (p={R['cont']['andthen_rate'][1]:.2f}) | n/a | NOT SUPPORTED (no positive relation; a word count is a weak proxy for causal structure) |
| 15 | Playbook P04, DS-000018 CLM-009 (templated repetition vs reusable format) | 8-gram Jaccard overlap of the first 400 words, all pairs within each channel | max pair overlap {max(v['max'] for v in rep.values() if v['max'] is not None):.3f}; 0 pairs >= 0.25 in any channel | n/a | PASS: no near-duplicate scripts. But 21 of MonkeyExplains' 62 openings start with the literal formula "This is Uncle Don / This is Sam..." (15 + 6), so the format repeats while the content differs, which is the case CLM-009 calls acceptable (a creator claim) |
| 16 | DS-000018 CLM-003 (evergreen: views arrive late) | Spearman of video age vs views per channel (single snapshot) | Casual Finance {R['ev']['Casual Finance'][0]:.2f} (p<0.001: newer videos have MORE views); Crayon {R['ev']['Crayon Capital'][0]:.2f}, MonkeyExplains {R['ev']['MonkeyExplains'][0]:.2f}, Capital Case {R['ev']['Capital Case'][0]:.2f}, Monkey Economics {R['ev']['Monkey Economics'][0]:.2f} (all n.s.) | n/a | NOT SUPPORTED in this snapshot; view velocity over time would be needed, and we hold one snapshot |
| 17 | FR-TITLE-03, FR-SCR-03, FR-INTRO-02, FR-16C-04 (title promise delivered, no overpromise) | only the title-word echo (row 12) was computed | see row 12 | n/a | PAYOFF READING NOT DONE at scale (would need reading every script). Not claimed |
| 18 | FR-16C-06 (reset every 20-30 s), FR-INTRO timings, TR-011-005 (first 10 s as packaging) | needs timed transcript, visuals or retention | none | n/a | NOT EVALUABLE (framework DB marks it so); FR-NA-01..03 NOT APPLICABLE |

## 3. Outlier method (Playbook P01) on actual numbers

Playbook rule: outlier ratio = views / subscribers; 5x strong, 10x+ clear outlier, studied best on 1K to 100K-subscriber channels. Applied to current subscribers (261K MonkeyExplains, 440K Casual Finance, 224K Monkey Economics, 319K Crayon, 23.6K Paper Billions, 12K Capital Case):

| Channel | Long videos tested | >= 1x subs | >= 2x | >= 5x | Max | Median ratio |
|---|---:|---:|---:|---:|---:|---:|
{orrrows}

Reading: the ratio only produces "outliers" for the two smallest channels (Paper Billions 4 of 6 at >= 5x, Capital Case 6 of 13), where the denominator is tiny. For the large channels it is nearly silent (Casual Finance max 5.5x even for 2.4M views). Monkey Economics has none (long-form median 0.05x of its subscribers), which confirms its audience was gathered by Shorts. So the playbook ratio is **informative only against small channels**, which is what the Playbook itself says; our within-channel PI is the better lens for large channels. Topics where several channels produced winners are the "cross-validated outliers" of Playbook Method 1 (section 5).

## 4. Launch cadence (DS-000018 REC-005 "launch with several linked videos")

| Channel | First public upload | Uploads in first 14 days | in first 30 days | Total held |
|---|---|---:|---:|---:|
{launchrows}

Paper Billions (6 in 12 days), Monkey Economics (11 in 14 days) and MonkeyExplains (4 in 14 days) started with several uploads. Casual Finance, Crayon Capital and Capital Case show 1 to 2 uploads in the first 14 days; Monkey Economics (Shorts burst, 11) and MonkeyExplains (4 in 14 days, 13 in 30) also started dense. Caveat: the first date is the first video held in the DB, which may not be the channel's true first upload (Casual Finance reports 222 videos but its DB window starts 2025-07-28). Those three have very different outcomes (Paper Billions 710K median, MonkeyExplains 275K, Monkey Economics long 10K), so launch density alone does not predict results here; the data cannot show cause.

DS-000018 REC-006 (repeatable "show" formats): MonkeyExplains uses "Explained Using Bananas" (19 titles, median 274K) and "... Worse Than You Think" (11, median 431K); Crayon uses "Explained Like You're 5" (21, median 301K, equal to its overall median). Template titles are not worse than the rest, in this set. CLM-018 (Shorts and long-form should be separate channels): Monkey Economics shows Shorts reach did not become long-form reach (913K vs 10K medians); Casual Finance kept both in one channel and its long median is 559K. One counter-example each way; not conclusive.

## 5. Topics: framework findings applied across channels (Playbook P01 cross-validation, P06, DS-000018 REC-004/009)

Keyword clusters over all six channels' titles (INFERRED labels; Stage 4 will curate). PI median is relative to each video's own channel.

| Topic cluster | Channels | Long videos | Shorts | Long views | Median PI | Winners (>=2x) | First covered by |
|---|---:|---:|---:|---:|---:|---:|---|
{trows}

Findings (clusters are first-match, so no video is counted twice; rebuilt during the review, section 11): (1) Crisis history (Depression, 2008, 1973, dot-com) has 5 channels, 13 long videos, 6 winners and median PI 1.65x. (2) The AI bubble / OpenAI / Nvidia cluster has the most views (19.4M, 28 long, 7 winners, median 1.56x) and 5 channels compete in it, so Playbook P06 (cover proven topics originally) and REC-009 (net-new information) both flag it as saturated. (3) Fed/rates/inflation has the highest median among multi-video clusters (1.88x) with only 5 long videos. (4) China and other countries (Singapore, Korea, Indonesia, France) has median 1.48x with 3 winners over 11 videos; stock-market structure and current crashes 1.24x with 3 winners. (5) Scams/fraud/crypto (14 long, median 0.58x, 1 winner), Iran/war/oil (0.62x), gold/dollar (0.64x, 0 winners), billionaire/company origin stories (0.78x, 3 winners but 12 videos) and national debt (median 0.21x, one 1.92M hit) are weak clusters. (6) Housing: 2 channels, 3 long videos, 1 winner (Casual Finance 2.42M). Airfares, rent data and jobs-report topics from our earlier shortlist do not appear in any channel's titles; see Stage 4.

## 6. Provenance: framework DB rows used (framework version v1, `data/knowledge/reference_knowledge.db`)

| Rule | Version | Member | Source file | Locator | Class |
|---|---|---|---|---|---|
{provrows}

Retrieval method: rows read directly from `ref_rule` and `ref_source_member` (read-only). Each rule's class is a creative heuristic unless shown; none is a platform fact. These validators are structural: only a reader can mark a rule semantically reviewed, and this stage did not do that.

## 7. Applied to actual videos (top two long videos of each channel)

yes/no per feature computed from the video's title and transcript. Columns: title <= 55 chars; crisis-family title; digit in title; numbers in the opening; dated opening; title keyword spoken early; closing echo; CTA in the first 15%; duration >= 8 min.

| Channel | Video | Views | PI | <=55 | crisis | digit | open nums | dated | kw early | echo | early CTA | >=8m |
|---|---|---:|---:|---|---|---|---|---|---|---|---|---|
{exrows}

Reading (counts from the table, 12 videos, against the base rate in all {R['n']} videos): crisis-family title 5 of 12 (42%, base 23%); closing echo 10 of 12 (83%, base 69%); title keyword spoken early 4 of 12 (33%, base 17%); dated opening only 2 of 12 (17%, base 33%); digit in title 4 of 12 (33%, base 31%); duration >= 8 min 10 of 12 (base 90%). So the top videos over-represent the crisis title and the closing echo, and do NOT over-represent dated openings, which weakens row 9. 12 videos are too few for any rule to be called a cause.

## 8. Findings and which framework produced each

| ID | Finding | Produced by | Label |
|---|---|---|---|
| F1 | Crisis/collapse/bubble titles have higher PI in 4 of 4 testable channels (1.45x vs 0.82x) | Playbook P07 family test on real titles | HYPOTHESIS: p=0.007 fails multiple-test correction; topic-confounded |
| F2 | Numbers in titles do not help; digit titles are slightly lower | Playbook P08, TR-011-011, FR-VC-05 | INFERRED |
| F3 | A "contrarian snapback" word search cannot detect hooks; the proxy fires on 87% of videos | TR-011-002, FR-HOOK-01 | proxy invalid; use reading |
| F4 | Dated openings trend higher (4 of 5 channels) but the effect vanishes in older videos and the top 12 videos under-represent them (2 of 12) | FR-VC-06, REC-007 | HYPOTHESIS, weak |
| F5 | Only 17% of videos speak the title keyword in the first ~30 s; no penalty | FR-SEO-01 | INFERRED |
| F6 | Ending that returns to the title's words trends higher | FR-16C-16 | HYPOTHESIS, borderline |
| F7 | No near-duplicate scripts anywhere; MonkeyExplains reuses a literal opener in 21 of 62 videos | Playbook P04, CLM-009 | VERIFIED text overlap |
| F8 | The outlier ratio flags only the two smallest channels; within-channel PI is the better lens for large ones | Playbook P01 | INFERRED |
| F9 | Cross-channel topic table (first-match clusters): crisis history and AI bubble strongest, AI bubble most saturated, rates/inflation and China/other-countries high median with few videos | Playbook P01/P06, REC-009 | INFERRED |
| F10 | Three channels launched with several uploads in 14 days (Paper Billions 6, Monkey Economics 11, MonkeyExplains 4) with very different outcomes; late-view (evergreen) growth is not visible in a single snapshot | REC-005, CLM-003 | UNKNOWN causal |

## 11. Review of this report (done 2026-11-19, after first publication)

| # | Issue found | Check | Result and fix |
|---|---|---|---|
| R1 | Crisis-title signal was labelled "only repeatable signal" | Benjamini-Hochberg and Bonferroni over the 22 primary tests | Smallest p=0.0071 vs threshold 0.0023: **not significant after correction**. Label downgraded to HYPOTHESIS (rows 1, F1) |
| R2 | Could the signal be a topic effect? | 39 crisis-family titles in the 5 channels: 19 sit in the Crashes category, 13 in AI bubble. Within AI: 1.56x vs 0.87x (13/13). Within Crashes only 2 titles lack the words, so it cannot be tested. Excluding both categories: 3.24x vs 0.82x, n=7, p=0.03 unadjusted | Unresolved: topic and wording are entangled, and the category regex itself contains "bubble"/"crash" (circular). Not usable as a rule |
| R3 | Topic clusters double-counted videos (an AI crash video counted in "AI" and "crises"; "debt" included an AI debt video; "war" included WW2) | Printed cluster membership | Clusters rebuilt with first-match priority (`stage3_topics.py`); section 5 and F9 text replaced. Changes: crisis history 1.71x to 1.65x, AI views 21.1M to 19.4M, national-debt median 0.60x to 0.21x |
| R4 | Launch cadence text said only Paper Billions launched with a batch | Table in section 4 | Already corrected: Monkey Economics and MonkeyExplains also started dense |
| R5 | Counts and provenance | Rule counts re-derived (27 creative, 1 empirical, 2 duplicate, 3 not applicable); framework rows re-read from `ref_rule` | Corrected from 29 to 27 |
| R6 | Proxies are crude (regex title families are ours, not the PDF's ten; hook "snapback" cannot be found by word search) | Reviewed | Already labelled INFERRED/PROXY INVALID. No rule was adopted |
| R7 | Sample scope | MonkeyExplains tested 62 of 64 public long (2 lack transcripts); Paper Billions only in the 'all' sample | Stated; does not change conclusions |

Net result of the review: the Stage 3 conclusion "no framework rule reliably separates winners" stands; the one positive signal is downgraded from "repeatable" to "nominal".

## 9. Implications for our channel (HYPOTHESIS, to be tested on our own Studio data)

1. Do not adopt any rule as a gate. In this sample, no framework heuristic reliably separates high from low views, which matches the earlier finding (Phase E) that title features did not separate winners.
2. Cheap, compatible choices: crisis/risk framing only when the data supports it; a dated, specific opening; a closing that returns to the title's question. All three are consistent with the evidence above and with the framework DB; none is proved.
3. Avoid the hook trope shared by MonkeyExplains and Paper Billions ("This is X, and he has a huge problem") and the AI-bubble cluster unless a data angle is original.
4. Keep the Part D measurement plan: test titles and thumbnails with YouTube's A/B tool, long-form only, from video 1.

## 10. Not done in Stage 3
- No page-by-page re-read of DS-000011, DS-000018 or the Playbook; no semantic review of rules.
- No payoff/overpromise reading across all scripts; no visual or retention tests (no data).
- DS-000018's platform-mechanism claims (CLM-001, -002, -004, -006 to -008, -010 to -014, -016, -017) cannot be tested on competitor public data; their status stays as in the 2026-09-04 primary validation.
"""
pathlib.Path('STAGE3_FRAMEWORK_APPLICATION_2026-11-19.md').write_text(md)
css=open('../STAGE2_SIX_REPORTS/build_reports.py').read().split('css="')[1].split('"\n')[0]
pathlib.Path('STAGE3_FRAMEWORK_APPLICATION_2026-11-19.html').write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Stage 3 framework application</title><style>{css}</style><p><a href='../../START_HERE.html'>&larr; START HERE</a></p>"+markdown.markdown(md,extensions=['tables']))
print('ok',len(md))
