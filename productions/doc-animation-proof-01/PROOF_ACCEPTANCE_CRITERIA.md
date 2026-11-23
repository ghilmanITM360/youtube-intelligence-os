# Acceptance criteria for the document-animation proof (frozen BEFORE the first render, 2026-11-22)

Subject: ~60 s original explainer, "does interest earn interest?", using an authentic CFPB page capture plus an original, labelled hypothetical mechanism diagram. Silent render with a prepared timing track; audible review is NOT part of this pass and stays PENDING.

Each gate is PASS/FAIL, judged by a read-only reviewer on the actual MP4 frames and files, not on this author's claims.

| # | Gate | Pass condition |
|---|---|---|
| 1 | Claims entail visuals | Every figure/definition shown on screen is in the cited excerpt (real page text) or is a labelled hypothetical whose arithmetic the reviewer recomputes. |
| 2 | Claim gate blocks bad scenes | `tests/test_claim_gate.py` passes (19 cases incl. banking definition, unsupported number, misleading comparison, hypothetical-as-actual, fabricated quote, missing qualification); the proof's own register authorizes; mutating one proof claim to UNVERIFIED makes the build refuse to render. |
| 3 | Provenance complete | Capture file SHA-256 matches the manifest; URL, publisher, title, last-reviewed date, retrieval timestamp, rights basis recorded; derived frames do not modify the original. |
| 4 | No misleading crop | Each highlighted figure is shown with its row label/unit/qualifier visible in the same frame (`required_context`), and no crop hides a word that changes the meaning. |
| 5 | Registration through transforms | Marks stay on their passage in frames before, during and after each zoom/pan (reviewer samples frames; unit test proves image and marks share one transform). |
| 6 | Timing matches clause | Mark onset frames fall on or just before the spoken clause named in the timing track (planned track, not audio): tolerance and mode (instant vs progressive) as declared; marks are not visible before the passage is legible. |
| 7 | Diagram arithmetic | Hypothetical numbers are exactly: year interest $50.00, $52.50, $55.13; balance $1,157.63; simple-interest total $150.00; compound interest total $157.63; difference $7.63. Label "Hypothetical illustration, not a forecast" visible whenever they appear; bars start at $0. |
| 8 | Readable at playback size | At 1920x1080 the source identity and the marked figure are legible; at a 25% (480x270) proxy the marked figure, row label and attribution remain distinguishable; hand-lettered labels at least 5% of frame height. |
| 9 | Phone scale | Same at 640x360 downscale: marked value and key diagram numerals readable. |
| 10 | Visual coherence | Existing provisional host family and white-canvas grammar; no new master character; no overlap/clipping of text; hard cuts. |
| 11 | Technical decode | ffprobe 1920x1080, 30 fps, duration 60.0 s +/-0.1; full decode with zero errors; frame count = 1800; no black/duplicate-frame anomalies beyond the intended 24-fps stepping. |
| 12 | No regression | Existing renderer tests: importing `v1r4_render` and `v1r9b` machinery unchanged (git diff shows no edits to existing renderer files); doc_scene tests pass. |
| A | Audio (separate) | PENDING: no narration was recorded; mechanical, forced-alignment and human-listening gates are not claimed. |
