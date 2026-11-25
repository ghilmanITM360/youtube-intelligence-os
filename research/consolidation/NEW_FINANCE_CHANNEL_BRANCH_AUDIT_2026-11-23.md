# Audit: `origin/research/new-finance-channel-2026-11-18` (2026-11-23)

Read-only audit by file extraction (`git archive` to scratch). The branch was not checked out and nothing on it was changed.
Branch: Machine A, 7 commits ahead of `origin/main`, tip `798dc7f8`, 298 files, about 30 MB under `research/new-finance-channel/`.
Labels: VERIFIED (I recomputed or re-read it), SELF-REPORTED (the branch says it, I did not check), NOT CHECKED.

## Verdict

The research is honest about its limits and most numbers reproduce. It is not merge-ready, mainly because of how the branch changes the canonical finance database, and because no topic or script is approved. I do not give a numeric score: the branch's own 55.5/100 was its own rubric.

## Findings

### High

1. **Canonical DB is replaced from a task branch.** `data/catalog/finance_economics_complete.db` is a 98,910,208-byte blob on `main` and a 134-byte Git LFS pointer on the branch (object size 117,866,496). `.gitattributes` adds an LFS rule for it. `AGENTS.md` (two-Mac section) says a task branch must not overwrite canonical data. A merge would also change the file's storage mode for every clone.
   - I did not fetch the LFS object, so I do not know whether it exists on the remote, or what its tables contain (the branch claims 3,832 videos vs 3,694 on `main`). NOT CHECKED.
2. **Source-of-truth split for MonkeyExplains.** Stage 1 says the DB holds 73 of 149 reported. The six-channel reports use a merged CSV of 136 rows (73 DB + 56 from R4 + 7 from R5; 64 long, 37 Shorts, 35 Member Edition). The 136 are VERIFIED as 73+56+7, but they exist only in CSV and JSON, not in a DB. Thirteen long videos stay missing.

### Medium

3. **Topic ranking is transcribed, not computed.** `STAGE6/build_stage6.py` hard-codes the evidence legs (`L = {"E06": "YYNY", ...}`) and Trends ratios (`D = {...}`). GO / GO-CONDITIONAL / HOLD tiers are set by hand in Stage 5. The ranking sort is consistent with its stated rule, and tier counts match (6 / 8 / 2), but a rerun would not reproduce the legs.
4. **E11 (Jobs, rank 4, GO) has no competitor winner (leg N).** Stage 4's own advance rule needed a winner or an owner theme. The only matched winner is a career video (`GkJCXwm7Ous`, 211,692 views), which Stage 5 itself calls "not report mechanics". The October jobs report result is marked UNKNOWN in Stage 5.
5. **E06 (rank 1) rests on thin competitor evidence.** The "winner" is a 21,531-view Monkey Economics video (2.1x of a long-form median of 10,244) plus a Casual Finance Short (389,111 views, a different format). Demand and the data hook carry the GO, not competitor proof.
6. **Calendar order departs from the ranking.** V1 Rent (rank 11, Trends ratio 0.02, no competitor winner) takes slot 2 ahead of F02 (rank 2) and E01 (rank 3). The report says this is an owner choice, so it is a decision, not an error.
7. **Scripts are drafts.** All four scripts WARN on R7 only (no images). Each gate JSON's SHA-256 matches the current file (VERIFIED), and my rerun on E06 gave the same WARN. E06 still has 5 `[CHECK]` markers and cannot be finished before the 2026-12-10 CPI release. The manual checklist C1-C5 is open for all four. None is framework-guided and none claims to be.
8. **Stale documents were not marked superseded.** `05_FRESH_COMPETITOR_DATA/REFRESH_STATUS_AND_MISSING_DATA.md` (11-18) still says Casual Finance is 206 of 220 and MonkeyExplains is 63, while Stage 1 (11-19) says 223 and 73. The channel header (222) is one below the DB (223) with no explanation.

### Low

9. Overlapping folders: `13_TITLE_MODELS` and `13_WINNING_TITLE_MODELS`, a pointer-only `15_SCRIPT_AND_HOOK_INTELLIGENCE`, an out-of-scope `04_ADDITIONAL_FINANCE_CHANNELS`, and 63 generated HTML pages under `readable/`.
10. 68 third-party thumbnails (7.7 MB) are stored as evidence. Fine for research, not for production use.
11. Spend: SELF-REPORTED $1.956 total, $1.72 of it on channels outside the six (the branch flags this itself).

## Verified

- All 10 raw Apify JSON files match `SHA256SUMS.txt`.
- Stage 1 counts recomputed from the classified CSVs: Casual Finance 223 (38 long, 185 Shorts, 30/60/90-day windows 13/29/54); Monkey Economics 60; Crayon 35; Capital Case 13; Paper Billions 6. All match.
- Stage 4: 54 winners (42 long, 12 Shorts); 26 candidates split 16 advance, 7 hold, 3 drop. All match.
- Stage 3 crisis-title test: I got median PI 1.46 vs 0.82, Mann-Whitney p = 0.0052 (the branch reports 0.007 to 0.01). Same direction. It still does not pass the branch's own correction threshold of 0.0023. My p comes from a normal approximation.
- Calendar: all Monday, Thursday and Saturday dates are the right weekdays.
- BLS (web): the November 2026 CPI is scheduled Thursday 2026-12-10 8:30 ET, and the October 2026 release did not publish most 12-month changes because October 2025 data was never collected. Matches the E06 hook.
- No deleted files. Changes outside `research/new-finance-channel/`: `.gitattributes`, the DB, and the four scripts under `productions/`.

## Not checked

DB contents (LFS), the six 2,200-7,900-word channel reports' prose quality, thumbnail images, the transcript manifest, Trends and YouTube-search readings (viewed by eye, no export), Treasury / Freddie Mac / SEC figures beyond the two BLS points, Apify cost figures, and the `readable/` HTML.

## Before merging

- Decide how the DB change should land (separate data PR with LFS confirmed, or keep the DB out of this branch).
- Mark the 11-18 refresh doc as superseded.
- Put the hard-coded ranking legs behind a script that reads the Stage 5 evidence, or label them as manual.
