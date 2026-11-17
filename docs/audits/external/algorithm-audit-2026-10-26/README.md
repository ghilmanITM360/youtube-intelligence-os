# YIOS Master Algorithm Intelligence & Data Audit — 2026-10-26

This package was produced read-only against `youtube-intelligence-os` HEAD `d987510b` (clean before and after; QA-verified). It has **not committed to git**. A separate review is required before any repository integration.

## Reports
1. `YOUTUBE_ALGORITHM_DEEP_RESEARCH.md`: official vs historical vs unknown, surface by surface
2. `YIOS_COMPLETE_DATA_AUDIT.md`: full census, authority map, population integrity, coverage matrix
3. `YIOS_ALGORITHM_VS_EVIDENCE_MATRIX.csv`: 24 algorithm questions × YIOS evidence
4. `YIOS_VIRALITY_HYPOTHESIS_TESTS.md`: 14 primary + 14 exploratory tests, replication, prediction
5. `CHANNEL_DNA_AND_GROWTH_INSIGHTS.md`: channel profiles with IDs and denominators
6. `YIOS_GROWTH_EXPERIMENT_ROADMAP.md`: E0–E8 experiments, measurement plan, data priorities
7. `RESEARCH_LIMITATIONS_AND_MISSING_DATA.md`: missing metrics, inaccessible sources, resource checkpoint
8. `EXECUTIVE_SUMMARY_ROMAN_URDU.md`

## Reproduce (stdlib Python only; no new dependencies)
```
python3 -I scripts/census.py  <repo> receipts      # SQLite mode=ro; other branches via git show
python3 -I scripts/analyze.py <repo> derived       # seed 20261026
python3 -I scripts/channel_dna.py .
python3 -I scripts/charts.py .
python3 -I scripts/matrix.py .
python3 -I scripts/qa.py . <repo>                  # recomputes quoted numbers + checks repo untouched
```
`receipts/OUTPUT_SHA256SUMS` lists SHA-256 for every file in this package.

## Continuation
- **Done:** Stages 0–6.
- **Not done (needs separate approval or data):**
  - blind packaging coding (Roadmap E8)
  - transcripts for the 646 expansion videos
  - repeat competitor snapshots
  - Visual 003 (Machine A only)
  - owned-channel Studio exports
- The Finance audit's next item `UmKdQCMCc98` was not touched.
