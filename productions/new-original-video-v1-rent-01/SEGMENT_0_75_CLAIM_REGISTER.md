# V1 Rent segment 0-75 s: on-screen figures and citations (not a script; no new narration)

Narration: Take 2 (`audio/take2/v1_rent_take2.wav`, sha256 3ef02978...c14b6e). Timing: `audio/take2/t2_words_merged.json` (ASR, about +/-0.1 s). Build: `tools/v1_build_render.py`.
Segment length 75.0 s (S001-S015 end at 74.32 s; S016 starts 75.14 s).

| On screen | Time (s) | Value | Source / dossier ID | Status |
|---|---|---|---|---|
| BLS bar + counter | 3.9-5.3 | 2.8% (rent of primary residence, 12 months to Sep 2026) | BLS CPI release 2026-10-14, Table 1 (C-01) | V (read this session) |
| Zillow bar + counter | 8.2-9.4 | 2.7% (typical asking rent, 12-month change) | Zillow Group press release, Oct 6, 2026: typical U.S. rent +2.7% y/y to $1,932 (C-02) | V: Zillow Group IR press release, Oct 6, 2026 (RESEARCH_DOSSIER section 8). The research-site page still returned 403; no screenshot. |
| "almost the same answer" | 14.3-16.4 | 0.1 point apart, not printed | derived from C-01, C-02 | D |
| Rent 7.7% | 44.4-75 | 7.728 (Aug 2026 weights) | BLS 2026-10-14 Table 1 (C-03) | V |
| Owners' equivalent rent 25.9% | 49.4-75 | 25.902 | same (C-04) | V |
| Shelter 35.3% | 59.5-75 | 35.323 | same (C-05) | V |
| Light sliver (about 1.7%, shown in the note) | 56.5-75 | 35.323 - 7.728 - 25.902 = 1.693 | derived, labelled "derived" on screen | D |
| "About one third of the index" | 66.6-70.3 | 35.3% is about 1/3 | derived | D |

Notes
- Weights are the **August 2026** weights (C-06: Sept 2026 weights differ). The chart title and source line say so.
- No number is shown for anything the narration says after 122.7 s (C-24..C-29), so none of them appears here.
- "Seasonally adjusted" (C-23) is not claimed anywhere in this segment.
- No screenshot of BLS or Zillow is used (not captured; BLS and Zillow block automated access and nothing was bypassed). The charts are original redraws labelled with their source.
- Sprites are the five independently reviewed Codex artworks (SHA-256 in `codex_art/qa/INDEPENDENT_REVIEW_V1_RENT.md`); registered in `v1_assets/` through pipeline.py. Single closed-mouth pose: no lip sync.
