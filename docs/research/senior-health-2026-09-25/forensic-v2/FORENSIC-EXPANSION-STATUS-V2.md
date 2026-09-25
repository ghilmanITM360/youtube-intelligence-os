# Senior Health Forensic Expansion: Status V2

**Date:** 2026-09-25
**Scope:** continuation of the forensic expansion from the existing files. Nothing from Pass-1 or the first forensic pass was deleted.
**Working status on entry:** FORENSIC EXPANSION: IN PROGRESS. The earlier "COMPLETE" claim was retracted; see the header note added to `../FORENSIC-EXPANSION-FINAL-STATUS.md`.

## Completion gates

| Gate | Result | Evidence |
|---|---|---|
| Actual transcript-level analyses | **DONE** | All 305 stored transcripts parsed from `registry.db`. The 149-video deep population has full per-video fields: first 15/30/60 s, hook, promise flags, authority, credibility, open loop, fear, hope, curiosity, payoff, CTA, bridge, ending, word count, density and claim counts (`TRANSCRIPT-FORENSICS.json`, workbook sheet 16). The 58 matched-pair videos and 11 case-study scripts were read in full. Times are APPROXIMATED_FROM_WORD_POSITION. 1 transcript is absent (fj4TaPrLl8U, no caption track). |
| 29 matched pairs: actual script comparison | **DONE** | `MATCHED-PAIRS-SCRIPT-FORENSICS.json`. Each pair has actual first-30-s text, promise, authority, specificity, progression, payoff timing, CTA and thumbnail, plus a unique finding. 14 pairs are CLEAN, 14 TIME_CONFOUNDED, 1 INVALID_CONTROL. |
| Live thumbnail matrix | **DONE** | 149/149 thumbnails LIVE_WEB_VISUAL, 30 fields each (`THUMBNAIL-MATRIX.json`). Winner-vs-loser comparison is in the pair file. 4 external breakout thumbnails also inspected. |
| Google Trends: live queries only, no estimates | **DONE** | 32 live investigations (`TRENDS-REGISTER.json`). Every earlier estimate is withdrawn and listed. Coverage: US and UK queries, plus worldwide country comparisons that give US/UK/CA/AU values; 5-year, 12-month and a custom daily window; ±90-day upload windows; web and YouTube search. |
| Related/rising queries | **DONE** | Top, rising and breakout queries and topics captured per investigation. They feed sheet 17 (audience language) and the new concepts N01–N17. |
| Historical context: major cases | **DONE** | 10 events researched, including 2 checked and rejected or low relevance (`HISTORICAL-CONTEXT.json`). |
| External YouTube mapping: all major clusters | **DONE** | 13 strategic clusters, 172 live search results, roles assigned (large / medium / recent / evergreen winner, mill duplicate, failed copy). 6 channel pages and 4 watch pages checked (`external/`, `EXTERNAL-BENCHMARKS.json`). |
| Small-channel breakouts | **DONE** | 5 natural experiments (`SMALL-CHANNEL-BREAKOUTS.json`). The script opening is UNKNOWN for the 3 external ones: the transcript panel does not load without sign-in. |
| Content-mill / duplicate network | **DONE** | `DUPLICATE-NETWORK.json` (66 candidate pairs) and `DUPLICATE-NETWORK-SUMMARY.json`. Covers title, transcript 5-gram, thumbnail text and persona clones, internal and external. |
| DS-000011 traceably applied | **DONE** | 13-row matrix: knowledge unit, framework, videos, evidence, counterexample, result, contribution (sheet 34). |
| DS-000018 traceably applied | **DONE** | 19 claims with original source, status, official support, internal/external evidence, counterexample and implication (sheet 35). |
| DS-000031 traceably applied | **DONE** | All 11 requested frameworks, each with internal support, internal counterexample, external support, limitation and implication (sheet 36). |
| Medical fact-check: high-risk items | **DONE** | 24 claims with SOURCE / SOURCE TYPE / verdict / SAFE REFRAMING. Results: 10 UNSUPPORTED, 2 CONTRADICTED, 9 PARTIAL, 3 SUPPORTED (sheet 28). |
| Excel fully built | **DONE (with one verification caveat)** | `SENIOR-HEALTH-FORENSIC-WORKBOOK-V2.xlsx`: 38 sheets (all 31 required plus 7 supporting). Formulas were cross-checked in Python: 306 videos, 76 ≥3x, 85 <0.5x, 650 evidence rows, no range mismatches. **Caveat:** LibreOffice is not installed, so the skill's `recalc.py` could not run. The file is set to recalculate fully when opened in Excel. |
| Charts actually built | **DONE** | 20 native Excel charts, each with plain-English commentary (sheet 37). |
| Evidence register granular | **DONE** | 650 records (`EVIDENCE-REGISTER-V2.json`, sheet 29), covering: deep transcripts 149, thumbnails 149, external videos 172, Trends 32, pairs 29, medical checks 24, corpus tests 43, data corrections 19, conclusions 18, historical events 10, small-channel breakouts 5. |
| Case studies: actual evidence | **DONE** | 11 case studies from actual transcripts, thumbnails, Trends and external data (`SENIOR-HEALTH-CASE-STUDIES-V2.md`). No "expected script" reconstructions. |
| First 50 re-evaluated | **DONE** | 26 KEEP / 18 MODIFY / 6 DROP, each with an evidence reason, plus 17 new concepts (`FIRST-50-REEVALUATED.json`). |
| First 10 finalized after research | **DONE** | `FIRST-10-FINAL.json`, sheet 26. All 17 required fields per video. |
| Data-quality contradictions fixed first | **DONE** | 19 corrections (`DATA-QUALITY-CORRECTIONS.json`, sheet 31). |

```text
FINAL STATUS:
COMPLETE — all acceptance gates pass.
Open caveats (disclosed, not hidden):
 1. Workbook formulas are not machine-recalculated (LibreOffice absent); Excel recalculates on open.
 2. No first-party analytics (CTR / retention / traffic source) exist, so every causal statement stays a hypothesis.
 3. Openings of 3 external breakout videos UNKNOWN (transcript panel blocked without sign-in).
 4. Topic tags are regex-based (pass-1); lexical script features are heuristics on actual text.
```

## Scope limits kept

- The repository's canonical DBs and raw evidence were only read, never changed.
- No YouTube API use and no paid acquisition.
- Web research was read-only: no sign-in, no forms, no downloads.
- The browser preview server (`.claude/launch.json` → `python -m http.server` on the scratchpad contact sheets) was used only to display thumbnails.
