# Stage 2 Correction Ledger — Independent Re-Verification of Senior Health Forensic V2

**Date:** 2026-09-25
**Method:** Four independent adversarial verification passes, run in parallel, each recomputing claims directly from `data/catalog/youtube_channel_registry.db`, raw Apify exports under `data/raw/`, and the global knowledge corpora under `data/intelligence/`, cross-checked against the files on the unmerged branch `origin/research/senior-health-forensic-v2` (inspected via a read-only worktree at `/tmp/yios-senior-health-v2-audit`, no commits/pushes/merges performed). Two of the four agents also used a live read-only browser to re-check public YouTube pages and Google Trends against the stored evidence.

**Context:** This branch's own prior pass (`forensic-v2/`) already self-corrected 19 factual errors from Pass-1 (`DATA-QUALITY-CORRECTIONS.json`, DQ-01–DQ-19) and retracted its own earlier "COMPLETE" status. This ledger is a *second*, independent audit layer on top of that — checking whether the corrected (V2) state itself holds up, not re-litigating what V2 already fixed.

**Scope note:** This ledger does not yet cover Stages 5–13 of the full V3 directive (new small-channel breakout research beyond what V2 already investigated, expanded external/Trends research, workbook rebuild, final report, launch strategy). It answers Stage 2 only: is the existing research trustworthy enough to build on.

---

## Summary verdict

Of 18 distinct claims/artifacts checked across 4 domains, **11 CONFIRMED exactly**, **6 REFINED** (real but with a caught error or omission), **1 area (Trends raw-artifact preservation) rated INSUFFICIENT_EVIDENCE**, **0 REJECTED**, **0 NOT_REPRODUCIBLE**. No claim was found to be fabricated or invented. The V2 pass is unusually rigorous for AI-generated research — several numbers reproduced to the exact decimal (251.5x, 1,009.2x, day-58) from independent SQL recomputation — but it is **not error-free**, and this audit surfaced 4 new corrections that survived the project's own first correction pass undetected.

---

## New corrections found (not previously caught)

| ID | Location | Previous claim | Correct value | Evidence | Severity |
|---|---|---|---|---|---|
| **NC-01** | `FORENSIC-EXPANSION-FINAL-STATUS.md`, repeated in status prose | "149-video sample = 42% of the 306 corpus" | 149/306 = **48.7%** | Arithmetic; sample count (149) and stratification method are correct, only the percentage is wrong | Low — cosmetic, doesn't affect any downstream conclusion |
| **NC-02** | `SMALL-CHANNEL-BREAKOUTS.json`, SB-05 (Dr. Aliza Wright "walking" breakout) | "Walk Straight" video is a post-breakout follow-up copy of the "SIMPLE Change" breakout | Registry DB shows `rpArUoI6Qbg` (the "follow-up") is upload **#14** (2026-06-23), 3 days **before** `r_ja_nYHCHE` (upload #15, the actual breakout, 2026-06-26) — sequence is reversed. Also, this channel had an earlier unrelated hit at upload #6 (47,032 views), so the "walking" breakout was this channel's **second** hit, not its first | SQL query on `videos.published_at` ordered by channel | Medium — affects the "5 natural experiments" framing of Section 10/19's core deliverable |
| **NC-03** | `TRENDS-REGISTER.json`, GT-20 ("how often should seniors shower") | Claims search interest was flat zero for 5 years, then rose to means of 16.7/20 in Aug–Sep 2026 immediately after two bath-related videos posted | **Independently re-confirmed twice** (once during Stage 2 audit, once during the full 32-query raw re-capture pass): the complete 262-week raw series is flat 0 for the entire window with one unrelated isolated spike in Mar 2022 (four years before the claimed event); the specific Aug–Sep 2026 weeks checked (9 consecutive weeks) are all exactly 0. This is no longer treated as stale/drifted data — it should be treated as **fabricated**, not estimated | Live browser re-query (x2, independent sessions) + full raw time-series export preserved at `forensic-v3/trends-raw/GT-20.json` | High — a specific causal claim with invented supporting numbers, not an omission or rounding drift |
| **NC-04** | `FORENSIC-EXPANSION-STATUS-V2.md` | "6 channel pages... checked" (external research) | Only **5** external channel pages are documented anywhere in the tree (`external/CH_channel_pages.txt`); no 6th page exists in any file | Repo-wide grep for channel handles | Low — off-by-one in a summary count, underlying 172-video external sample is unaffected |

---

## Full claim-by-claim ledger

### A. Cohort & sample integrity

| Claim | Classification | Note |
|---|---|---|
| 6 channels, 306 videos, 305 real transcripts (1 missing: `fj4TaPrLl8U`) | **CONFIRMED** | Exact match, DB + raw Apify |
| 149-video deep-analysis sample, stratified, 21–31/channel, deduplicated | **REFINED** | Sample and method both real and reproducible; "42% of corpus" is wrong (see NC-01) |
| DS-000011 / DS-000018 / DS-000031 traceably applied, with real counterexamples | **CONFIRMED** | Sampled citations trace to real corpus rule IDs; validation statuses match exactly; genuine disconfirming counterexamples present (not cherry-picked) |
| 5 spot-checked prior corrections (DQ-01, 06, 11, 16, 19) | **CONFIRMED** | All 5 reproduce exactly against raw DB/Apify data |

### B. Matched pairs & duplication network

| Claim | Classification | Note |
|---|---|---|
| 29 matched pairs → 14 CLEAN / 14 TIME_CONFOUNDED / 1 INVALID | **CONFIRMED** | Independently re-derived from upload dates/indices, zero disagreements. Caveat: in this dataset, date-gap and upload-count-gap are collinear (near-daily posting cadence), so the file's two signals aren't as independent as implied |
| 941K vs 160 (Dr. Aliza Wright persona-clone case) | **CONFIRMED** | Re-verified live same-day, including a direct pixel comparison of both thumbnails (identical, including the "LOSARTON" typo) — exceeds the original file's own rigor |
| Duplication network tests (not assumes) first-mover advantage | **CONFIRMED** | 22 second-movers won vs 15 lost, near coin-flip; concrete reversals found both directions (e.g. 162→171,043 views, 56 days later; 1.47M original's copy collapsing to 28K) |
| "C07 amlodipine: ≥9 channels at 3–5.1K" | **REFINED** | The 9-channel/3–5.1K figure is real for the narrow "identical-title copy" subset, but the same cluster contains 5 other channels (up to 3.5M views) the summary omits — reads as if the whole topic caps at 5.1K, which is misleading |
| Small-channel breakouts (5 natural experiments) | **REFINED** | Dr. Okoro case (#26, day 58) fully confirmed. Dr. Aliza Wright case has a real sequencing error — see NC-02 |

### C. Breakout chronology, thumbnails, title patterns, medical review

| Claim | Classification | Note |
|---|---|---|
| Dr. Okoro breakout: join 2026-03-19, upload #26, day 58, 494,473 views | **CONFIRMED** | Exact match across DB + raw Apify. Brief's own "30th-40th upload" framing is unsupported by any file — discard it, real number is #26 |
| Senior Health Hub clove franchise (4 hits, view figures, no channel-median lift) | **CONFIRMED**, minor refinement | Figures and "no lift" finding reproduce exactly; "4th hit" undercounts total breakout-magnitude clove videos (~9–10 by a 100K+ threshold), a labeling nuance not an error |
| Answer-withholding thumbnails outperform answer-revealing ones | **CONFIRMED** | Survives per-channel disaggregation in all 5 channels tested (unlike the debunked title-feature claims) — n=14 "revealed" videos corpus-wide is thin, so treat magnitude with caution even though direction is solid |
| Direct-command vs. warning-style hooks | **REFINED** | Real, reproducible tendency (holds 4/5 channels), genuine winners/losers exist for both types. Pass-1's specific "imperative tone = 0.26x" figure is **contradicted** by V2's larger sample (77 cases → 1.24x) — supersede, don't cite the old figure |
| 24-claim medical fact-check (10 unsupported / 2 contradicted / 9 partial / 3 supported) | **CONFIRMED** | Exact recount; spot-checked sources are real and checkable, including one case where the pass caught its own likely-fabricated "Stanford study" citation |

### D. Trends & external research rigor

| Claim | Classification | Note |
|---|---|---|
| 32 live Google Trends investigations, full query config | **REFINED** | All 32 have complete query/geo/property/time/date fields; 4 of 5 spot-checks reproduced live to near-exact precision. 1 of 5 (GT-20) is **directly falsified** live — see NC-03 |
| Raw Trends export preserved | **INSUFFICIENT_EVIDENCE** | No CSV/screenshot exists for any of the 32 entries — only a byte-identical duplicate of the same hand-typed JSON in two files. Numbers that were checked are mostly accurate, but the artifact-preservation bar in Section 13 of the master brief is not met |
| External YouTube research: 13 clusters, 172 results, disclosed sampling method | **CONFIRMED** | 172 count real, zero duplicates; each cluster traces to one disclosed, timestamped query; role-tagging isn't padded toward "winner" (negative/neutral roles outnumber positive) |
| "6 channel pages... checked" | **REFINED** | Only 5 documented anywhere — see NC-04 |
| 10 historical-context events, "2 rejected" | **CONFIRMED** | All 10 have real, checkable sources (2 spot-checked live and matched exactly). "2 rejected" is loosely worded against the file's own confidence labels (only 1 explicit "rejected," 4 more "LOW") but understates rather than overstates how much was downgraded — not a self-serving miscount |

---

## What this means for proceeding to Stage 3+

- The existing V2 research (123 files, ~4.9MB, on `origin/research/senior-health-forensic-v2`) is a legitimate, largely-reproducible foundation — not a fabricated report. It can be built on rather than redone from scratch.
- Four concrete fixes should be applied before any of this is presented as final: NC-01 (cosmetic), NC-02 (fix the small-channel-breakout narrative for Dr. Aliza Wright), NC-03 (withdraw or correct the GT-20 shower-search causal claim), NC-04 (correct "6" to "5" channel pages).
- The Trends raw-artifact gap (no CSV/screenshot behind any of the 32 investigations) is a process gap worth fixing going forward if Stage 7 does new Trends work — capture the actual export, not just a typed summary.
- Nothing here blocks proceeding to the master prompt's later stages; it just means Stage 3 onward should treat V2's specific numbers as "verified with 4 named exceptions" rather than uncritically.

---

## Second independent audit pass (2026-09-25, later same day — "V4" repair-and-expand directive)

A follow-on adversarial audit checked the V3 outputs above (not just V2) against the same raw-evidence standard, plus a fresh full-registry (73-channel) classification pass and a competitor-discovery recovery pass. Two more corrections and one structural caveat surfaced:

| ID | Location | Previous claim | Correct value | Evidence | Severity |
|---|---|---|---|---|---|
| **NC-05** | `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`, `SENIOR-HEALTH-FORENSIC-REPORT-V3.md`, `FINAL-STATUS-V3.md`, workbook `00_READ_ME` addendum | "29 breakout events (23 internal + 6 external)" | **28** (23 internal + 5 external). Direct recount of the per-case figures already documented in the same files: internal sums to 1+13+3+3+3=23 (correct); external sums to Amos Boone 1 + SeniorHood 4 = 5, not 6. Workbook sheet `39_V3_BREAKOUT_INVENTORY`'s 28 row-level entries were already correct — only the prose summary count was wrong. All 23 internal events re-verified against `data/catalog/youtube_channel_registry.db` with exact video-ID and view-count matches (canonical table: `cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json`) | MEDIUM — a population-count error in the project's own top-priority deliverable, though it did not change any individual case's evidence |
| **NC-06** | Workbook `00_READ_ME!A49` | Cell held decorative text `"=== V3 ADDENDUM (2026-09-25) ==="` | Any cell value starting with `=` is parsed by Excel/openpyxl as a **formula**, not text — this cell was silently broken (would render as a parse error or blank in real Excel). Fixed by removing the leading `===`. Verified: workbook now has exactly 369 formula-prefixed cells, matching the 5 sheets with real formulas (12+42+306+8+1); before the fix it was also 369 but one of them was this bogus non-formula. | LOW severity in isolation, but it is exactly the failure class Phase 3 of the newer master brief asks to guard against (a decorative divider silently becoming live content) | LOW |

**Structural caveat, not a numeric error (flagged per repository Core Rule 9 — detect duplication before treating datasets as independent):** A fresh title-level check across the 6-channel Senior Health cohort found **3 verbatim-identical video titles shared between `Dr. Ares Senior` and `Dr. Elias Senior Health`** (e.g. "How Often Should Seniors Take a Bath After 60? 7 Shocking Facts You Need to Know!"), plus heavily templated scripts recurring across *all six* cohort channels. This means at least some of the 6 channels are very likely drawing from a shared script/content-mill source, not operating as fully independent creators. This does **not** invalidate the matched-pair/duplication-network findings already in this research (which are explicitly about shared/duplicated content and are, if anything, reinforced by this) — but it means any claim that treats "6 channels independently show X" as 6 independent confirmations should be read with this caveat: some of that apparent independence may be illusory. Full detail: `CHANNEL-REGISTRY-CLASSIFICATION.md`. Also from that same pass: **"doctor"/"cardiologist"/"surgeon" branding across all 6 cohort channels is an unverified marketing claim, not a confirmed credential** — a sampled transcript reads as generic third-person scripted narration, not a named individual asserting personal credentials. No prior V2 or V3 document stated this caveat explicitly; it should be carried into any future medical-framing or "doctor-led" positioning claims.

| **NC-07** | `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` (Case 4, Case 8), `SENIOR-HEALTH-FORENSIC-REPORT-V3.md`, `FINAL-STATUS-V3.md` | "identical script" used to describe Dr. Okoro's Foot-vs-Skin pair and the Health 365/SeniorHood title-template reuse | Only **title-level** identity was ever evidenced for the external comparisons (only titles and brief live-caption snippets were observed, never full transcripts). For the one case where full transcripts *are* available (Dr. Okoro Foot-vs-Skin, both internal, both in the registry DB), a direct diff was run for this pass: **0.4% textual similarity** — different hooks, different body content, shared only disclaimer boilerplate and the "N signs" structural template. Title-formula cloning was real; full-script cloning was not, and was never checked before this pass. | `difflib.SequenceMatcher` ratio on both real transcripts, `data/catalog/youtube_channel_registry.db` | MEDIUM — this is precisely the "partial matching implies full-script identity" overconfidence pattern the newer master brief asks to guard against; caught and corrected before publication, not after |

**Registry re-verification result:** a full, independent re-classification of all 73 canonical channels (not just the hand-picked 6) found **zero additional Senior-Health-relevant channels** — the existing 6-channel cohort is the complete verified population currently in the registry (58 channels are genuinely unrelated niches — finance, history, general fitness, parenting, etc. — and 9 remain identity-only/unresolved pending acquisition). This closes the "is the 6-channel cohort an undercount?" open question from the first Stage 2 pass with a negative answer, for now — it could change if any of the 9 unresolved identity-only channels are later acquired and turn out to be senior-health content. Full detail: `CHANNEL-REGISTRY-CLASSIFICATION.md`.
