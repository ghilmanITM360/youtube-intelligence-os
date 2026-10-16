# Continue Finance & Economics intelligence

Status: **FINANCE_INTELLIGENCE_IN_PROGRESS**. Existing branch `research/finance-economics-intelligence`; draft [PR #36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36). Do not create another branch/worktree/PR or merge. Starting checkpoint was `03a6cd0e98c9fb10b7d6a954bc1ef1f1c3ec8566`; final pushed head and CI belong in the PR body, avoiding a self-referential commit hash here.

Read FINANCE_ECONOMICS_MASTER_REPORT.md, QA_AND_LIMITATIONS.md, METHODS.md and VALIDATION.json. The baseline commit is `ef02fad`; later commits correct CSV line endings and add research. Pre-existing untracked folders `finance-short-02-visual-calibration/`, `productions/`, `research/casually-finance-script-intelligence/` were preserved. Do not stage them.

## Completed/remaining matrix

| Unit | Completed | Remaining next action |
|---|---|---|
| Baseline | 13 canonical channels; 966 videos/titles; 955 distinct text hashes; baseline coverage | Preserve source scope; do not redo discovery |
| Performance | 723 reproducible labels; 598 agree under five-peer sensitivity | 243 insufficient; seek original collection-time evidence for DS-000001 and source format for 159 historical records, without guessing |
| Scripts/topics | All available canonical texts have lexical features; 30 contextual reviews; 15 full reads | 936 semantic labels; 15 full reads now span five channels; broaden the remaining channel sample; no blanket human verification |
| Packaging | 966 lexical title feature rows; 27 mobile image reviews /30 attempts | Three Shaami 404s; expand images across selected important channels; 939 without fresh review; 30 explicit semantic title records now complete; 936 remain unreviewed |
| Reuse | Frozen 206 Casually Finance +11 Economics metric rows and relevant reports/Trends | Keep methods separate; source claims/financial facts not fully independently reverified |
| Expansion | Six partial Tier B first-page captures, 180 IDs | Emerging-channel cohort and representative weak/average channels; full history where decision-relevant |
| Trends | 22 inherited window rows reviewed; normalization preserved; event chronology checked | Broader canonical publication-event matching; query-specific demand validation; no extra fetch merely to duplicate existing series |
| Strategy | Cross-channel hypotheses; 12 scored ideas; four-episode pilot | Validate remaining evidence before promoting editorial hypotheses; no production requested |
| Source gaps | 26 original-path dispositions | Drive: 128 candidates, five prior content reviews plus five new triages; 118 remaining. Finance export duplicates 206 reused rows; see DRIVE_FOLLOWUP.md |
| QA | Local research validator, unit tests, source hashes, secrets/whitespace | Recheck exact-head CI after final push; see PR body for latest run |

## Commands

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git ls-remote origin refs/heads/research/finance-economics-intelligence
gh pr view 36 --json headRefOid,statusCheckRollup,url,isDraft
python3 -m unittest discover -s research/finance-economics-intelligence -p 'test_*.py'
python3 research/finance-economics-intelligence/build_comparisons.py
python3 research/finance-economics-intelligence/validate_research.py
python3 knowledge/youtube/validate_knowledge.py
python3 scripts/scan_tracked_secrets.py
git diff --check
```

`build_baseline.py` reproducibly regenerates baseline tables and overlays existing semantic/image annotations; it does not reacquire anything. `collect_landscape.py` reuses saved `*-videos-v2.json` captures and does not refetch them. Do not delete saved evidence to force a refresh; new snapshots require new filenames. Fetch provenance is in SOURCE_REGISTER and thumbnail registers. Existing report content can be read with `git show <Version>` using REUSED_SOURCE_REGISTER, without switching branches. No graph build/query is authorized.

Next atomic unit: deep-read matched strong/typical/weak videos from a newly rankable DS-000022 channel (Carl/Nick/Bob/Lucas), or expand mobile thumbnail coverage. DS-000022 dates are repaired; do not repeat that investigation. DS-000001 format and date provenance remain unresolved. Preserve unknowns if original evidence cannot resolve them. Check usage **five-hour → weekly → context** before starting: stop beginning expensive units around 90% five-hour or 95% weekly, finish current unit, validate/commit/push/handoff. Context indicators unavailable must remain UNKNOWN. Do not claim FINANCE_INTELLIGENCE_COMPLETE until the scope gaps are resolved or the user explicitly narrows the scope.

Legacy follow-up: [LEGACY_METADATA_PROBE.json](LEGACY_METADATA_PROBE.json) records the existing inventory catalog's candidate DS-000001 observation day, 2026-08-24, for all 159 records. The original date provenance still needs verification and all formats remain null; no tiers were promoted. Do not repeat this catalog lookup.

Prior checkpoint stopped at 93% five-hour /41% weekly. On explicit continuation, live usage was checked again in order: 5% five-hour /16% weekly /context UNKNOWN. Work resumed in bounded batches; the prior resource reading is historical, not the current limit.

Continuation validation must include `build_baseline.py` then `build_comparisons.py` when metadata changes. `METRIC_DATE_EVIDENCE.csv` records immutable source-cell evidence; `verify_workbook_dates.py` reproduces the 595-row source reconciliation using Python with openpyxl. Drive follow-up is finished for the five selected candidates; remaining 118 are not all relevant and should not be fetched indiscriminately.
