# Casually Finance success and production playbook

Research date: 2026-10-13 (Asia/Karachi). Status: RESEARCH_IN_PROGRESS.

This research answers the owner's supplied brief using the existing dated corpus. It does not modify YIOS engines or source evidence. The isolated branch is `research/casually-finance-success-playbook`; its base is `codex/casually-finance-forensic-research` at `7e2f6d3a3d5e4294d5f8bc4737dd0c784610c1f1`. Dependency: [PR #21](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/21). Scope: [issue #27](https://github.com/ghilmanITM360/youtube-intelligence-os/issues/27). Do not merge this stacked PR into main before resolving its base dependency.

## Read in this order

1. EXECUTIVE_FINDINGS.md: decisions and counterexamples.
2. VIDEO_PERFORMANCE.csv: all 206 uploads and per-record evidence, dates, peers, tiers and uncertainty.
3. TITLE_THUMBNAIL_PLAYBOOK.md and TOPIC_TREND_ANALYSIS.md: choose an original promise.
4. SCRIPT_STORYTELLING_ANALYSIS.md and VISUAL_MOTION_PRODUCTION_DNA.md: turn the promise into explanatory beats.
5. ASSET_FACTORY_AND_CODEX_FEASIBILITY.md and ORIGINAL_CHANNEL_PRODUCTION_SOP.md: make the original production.
6. IMPROVEMENT_OPPORTUNITIES.md and EVIDENCE_AND_LIMITATIONS.md: tests and evidence boundaries.
7. DEMO/: optional original editable keyframe proof.

## Reproduce analytics

From the repository root, with Python 3.12+ and no external packages:

```sh
python3 research/casually-finance-success-playbook/test_analytics.py
python3 research/casually-finance-success-playbook/build_analytics.py
```

`ANALYTICS_SUMMARY.json` is computed supporting data. `SOURCE_HASHES.json` records the read-only inputs. No network access, API, source media decoding or model calls occur. Reruns require the same source branch and dated evidence. Rerun outputs should have no diff.

## Performance method, version 1

All 206 identities come from the existing October 11, 2026 public snapshot; no live view refresh. Deduplicate exact Video_ID records and reject conflicting duplicates. Age uses exact publication and per-record collection timestamps, including timezone offsets. Lifetime average views/day equals views divided by age; it is not current daily traffic.

Shorts and long-form always have separate peer pools. Exclude videos younger than seven days from scoring and peer baselines. For each eligible upload, find same-format peers with age between 0.5 and 2 times its age, exclude itself, then select up to twelve nearest peers by absolute log-age distance. Require at least five peers. If fewer exist, use the nearest eight aged same-format peers and mark WIDE_AGE_FALLBACK. Record peer IDs and age range. This fallback makes recent long-form comparisons explicitly uncertain.

Score = (video lifetime views/day + 1) / (peer median lifetime views/day + 1). The one-view/day regularizer is negligible for ordinary records and prevents a zero denominator. Analyst-defined tiers: BREAKOUT >=4; TOP_PERFORMER >=2; ABOVE_BASELINE >=1.25; TYPICAL >=0.8; BELOW_BASELINE >=0.5; UNDERPERFORMER <0.5. Younger than seven days or insufficient format coverage: INSUFFICIENT_DATA. Labels describe this snapshot and method, not intrinsic video quality or YouTube categories.

A fixed Video_ID seed draws 1,000 bootstrap peer samples with replacement. The 5th/95th percentiles give a 90% baseline sensitivity interval; ratio bounds invert those baselines. Bootstrap_Tier_Agreement records label stability. MODERATE_DESCRIPTIVE requires AGE_CALIPER and agreement >=0.8; otherwise LOW_BASELINE_SENSITIVE. These are descriptive sensitivity bands, not calibrated causal confidence intervals: peers are correlated, channel growth and topic mix are uncontrolled, and views are cumulative rather than exposure-normalized. Raw-view and views/day format percentiles provide contrasting rankings.

Topic labels are single-label analyst assignments for 33 long-forms and disclosed title-keyword heuristics for Shorts. Title features overlap; absence means the rule did not match, not that a device is impossible. All titles are processed. Group medians are exploratory, not significance tests. Source classification is retained alongside derived labels. Content_Format is unverified for metadata-only uploads. No private editorial method or traffic-source attribution is inferred.

## Execution checklist

- [x] Inspect duplicates, Git history, usage and actual available corpus.
- [x] Create issue and isolated stacked branch.
- [x] Validate and persist all-upload analytics.
- [ ] Compare packaging and topics; verify bounded news timing.
- [ ] Synthesize existing script/visual/motion evidence.
- [ ] Write asset factory, production gates and improvement tests.
- [ ] Build optional original demo using existing tools only.
- [ ] Verify source integrity, outputs, remote HEAD, PR HEAD and CI; update same draft PR.

No subagents, background watchers, paid acquisition, full forensic reruns, copying of competitor artwork or changes to other worktrees.
