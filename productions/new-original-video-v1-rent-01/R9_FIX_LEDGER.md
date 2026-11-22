# V1 Rent R9 fix ledger (2026-11-21)
Candidate: `out_full/V1_RENT_FULL_R9_assembled.mp4`. Baselines preserved untouched: R7 segment files in `out_r7/`, R8 segments in `out_r8/`, R8 assembly `out_full/V1_RENT_FULL_R8_assembled.mp4` (sha f7f11071...3688b), edited master v1 `audio/take2_edited/...cut124-254.8.wav`, original Take 2 WAV.
Times below are R9 timeline (S090 trim shifts everything after 251 s by -3.32 s; R8 times in brackets).

| Ledger | Defect (R8 QA) | R9 action | Where | Status |
|---|---|---|---|---|
| P1-1 | S090 spoken "matches the market measure today within a fraction of a point" | Owner-approved trim: candidate `CANDIDATE_S090_trim_cut250.95-254.25.wav` becomes master v2 (copy, sha 0521dd42...63e75). Sentence now: "The official rent number moves in six-month steps, and it cannot tell you the dollar price of renting." On-screen "close to the market measure" chip removed. | audio v2; summary beat 243.5-253.7 [243.5-257.0] | fixed (audio listening PENDING owner) |
| P1-2 | Untagged numbers | Tags added: +2.8% at 189.2-193.9 and 193.9-199.5 (BLS CPI release Oct 14, 2026, Table 1); Zillow +2.9% beat 232.9-243.5 now carries BLS Nov 10 + Zillow ZORI tag. Code scan of all six segments: no other beat with a financial figure lacks a tag. | v1r9_tail.py | fixed |
| P1-3 | BLS evidence empty | `evidence/bls/BLS_EVIDENCE_RECORD.md` (3 pages: URL, title, date, passages); Zillow CSV re-downloaded and byte-identical | evidence/ | fixed (text evidence; no image screenshots saved) |
| P2-1 | BLS-tagged quote | No quote marks. "a claim we searched for:" + both lines struck + "no such sentence in the BLS factsheet"; tag "Searched: BLS factsheet" | 210.4-216.9 | fixed |
| P2-2 | "not this" underline | Both lines struck through in red | 144.0-147.6 | fixed |
| P2-3 | Oct wording | "no October 2025 survey data (funding lapse), so BLS cannot print an October-to-October change"; Zillow +2.9% tagged | 232.9-243.5 | fixed |
| P2-4 | Clipped descenders | Renderer pads text images (no position change). Applies to every scene | v1r4_render.txt | fixed |
| P2-5 | "9" reads as "q" | Numerals ("num" kind) now Caveat Brush (OFL) everywhere (clear 9). Hand font "g" still reads like "q" in Patrick Hand; word context disambiguates; documented P3, font not changed | all num text | 9 fixed; g = P3 accepted |
| P2-6 | Chart scale | Direct label "different scale from the last chart: 1 month, not 12" on the October one-month chart | 225.9-232.9 | fixed |
| P2-7 | BLS colour flip | BLS = olive and Zillow = blue throughout the tail (seg 3 houses, group homes, 12-month bar, one-month bar, +0.2%). Zillow +2.9% chip now blue | tail | fixed |
| P2-8 | No authentic imagery | Not added. Evidence now preserved; any insert would be a separate V2 design. | - | deferred (owner call) |
| P2-9 | Title | New working title in package: "Why Is Rent So High? How the Official Rent Number Is Measured". Script headers untouched (source script rule) | package doc | fixed in package |
| QA-new | Reviewer found missing arrow glyph (tofu box) between $1,859 and $1,913 after the font change | arrow drawn with arrow(); two separate numbers | 161.5-164.3 | fixed, frame checked |
| P3 | edge ink at 181.5-183.5 s | "how fast" arrow/label moved left 80 px | 180.6-183.9 | fixed |
| Font | Helvetica source tags not clearly redistributable | Source tags now Atkinson Hyperlegible (OFL 1.1). All fonts in the render path are OFL | v1r4_render.PLAINFONT | fixed |

Not changed: character art, Visual DNA, scene designs outside the list, verified figures, source references, narration timing before 251 s, R7/R8 renders.
