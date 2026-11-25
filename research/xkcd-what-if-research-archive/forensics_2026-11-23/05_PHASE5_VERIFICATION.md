# 05 Phase 5 verification of the script synthesis and playbook (continuation, 2026-11-23)

Scope: check `05_CROSS_VIDEO_SYNTHESIS.md` and `05_MASTER_SCRIPT_PLAYBOOK.md` against the 83 audits without re-running the audits. Method: `scripts/phase5_verify.py` (read-only). Outputs: `05_RULE_EVIDENCE_LINKS.csv`, `05_HOLDOUT_TEMPORAL_SPLIT.csv`. Status: **machine recomputation plus same-model self-review; no independent reviewer.**

## 1. Rule -> video IDs -> locators
Every operational rule now has a row with the supporting video IDs, example locators (`V### paraN`, using the repo's `locate.py` convention: ¶N = Nth paragraph under "## Script"), exceptions and the recompute path.

| Rule | Result | Exceptions | Notes |
|---|---|---|---|
| R01 attributed opening question | 41 of 43 long | V019 (promo, "comes from me"), V024 (meta hook) | Audit hook labels give 40; **V015** is attributed in ¶1 ("This question comes from AJ, who wrote") but was labelled a story hook. The playbook's 41 is right; the label-only count is 40. A loose regex gives 42 because it also fires on V019 |
| R02 no CTA | **41 of 43** (38 plain None + 3 qualified None) | V019 book promo at the opening, V020 playful real-world action | **Corrected:** playbook v0.1 said 38 of 43. Regex for subscribe/sponsor/patreon/next video finds 0 hits in all 83 scripts |
| R03 Shorts are excerpts | 38 of 40 Shorts have a long parent (8-gram containment >= 0.30, median 0.895); exceptions V065, V080 | | Containment is measured; "contiguous" is not |
| R04 length and rate | median 680 words and 3.59 w/s recomputed equal | | but see the holdout |
| R05-R08 spine keywords | ladder 13, cascade 5, tournament 1, audit 1 of 43 | | keyword tagging of the audit's structure label, not a coded taxonomy; the playbook's "about 13 / 5 / 2 / 4" is approximate and the tournament and feasibility counts do not reproduce by keyword (1 and 1) |

## 2. Videos versus content families
The 83 videos are 45 content families (43 long roots, 2 independent Shorts, 38 derived Shorts inside 28 families). **Every long-video rule above has families_with == videos_with** (each long video is its own family root; no long overlaps another long at containment 0.30), so the long-video counts are already family-level counts. Shorts are not independent observations: 38 of 40 re-cut long material, so any Short statistic (4 of 40 keep an attributed line; 46% numeral-on-screen) is a statement about a re-cut, not about 40 separate scripts.

## 3. Holdout: temporal split of the 43 long videos (older 21: 2023-11-29 to 2025-02-11; newer 22: 2025-03-04 to 2026-08-25)
Descriptive plus a seeded permutation test on medians (5,000 shuffles). Not a pre-registered holdout: the playbook numbers were computed on all 43, so this is a **stability check, not an out-of-sample test**.

| Metric | Older | Newer | Result |
|---|---|---|---|
| Words (median) | 825 | 632 | differs (p 0.009) |
| Paragraphs (median) | 28 | 10.5 | differs (p 0.032; partly caption formatting) |
| Words per second | 3.57 | 3.63 | stable (p 0.18) |
| Question marks | 2 | 2 | stable |
| Numerals per 100 words | 2.2 | 3.25 | not distinguishable at n=21/22 (p 0.30) |
| Second person per 100 words | 0.7 | 1.3 | not distinguishable (p 0.38) |
| Attributed opening | 19 of 21 (audit labels) | 21 of 22 | stable |
| No CTA label | 21 of 21 (regex) | 22 of 22 | stable |

Reading: the opening and ending rules and the speech rate are stable across the two eras. The **length statement is not**: use the era split. Failures and exceptions are recorded above (V015 label, V019, V020, V024, the two non-derived Shorts V065 and V080, the keyword-count mismatches).

## 4. What was not checked
Prose judgements inside the 83 audits (humour, curiosity, emotion); sentence-level locators beyond `locate.py check` ok; audits were written against auto-captions for 16 videos (no punctuation), so sentence counts there are unreliable; no independent second coder.
