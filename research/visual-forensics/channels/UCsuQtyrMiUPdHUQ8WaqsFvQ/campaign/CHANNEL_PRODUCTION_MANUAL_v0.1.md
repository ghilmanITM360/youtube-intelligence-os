# Primitive Education — channel production manual v0.1 (INTERIM)
Evidence: 6 dev videos built (long qB_EKkMyuUE, 3AsDdMQr_nQ, KyBWJPaF1KI; Shorts IUur04eOd4A, f1vIzsTFrp4, uIG2U_1xynQ), all VISUAL_ANALYSIS_PARTIAL. n=3 per format: ranges below are provisional and may not hold for the channel. Not yet evaluated on held-out videos. Metrics: campaign/aggregate_dev_interim3.csv; reuse: campaign/reuse_dev.json. No audio listening; narration relations ASR_UNCERTIFIED. Public views are snapshots; no retention/CTR claims.

## A. Observed source features
| Feature | Long (n=3): median, range | Short (n=3): median, range | Label |
|---|---|---|---|
| Events/min | 44.7, 39.4–45.4 | 45.6, 45.5–47.9 | reviewer classes + MEASURED timing |
| Scene cuts/min | 29.8, 23.6–32.4 | 21.0, 18.9–23.5 | reviewer classes |
| Median hold s | 1.24, 1.18–1.36 | 1.01, 0.89–1.14 | MEASURED |
| Activity frame share | 0.022, 0.021–0.055 | 0.059, 0.054–0.076 | MEASURED |
| Holds with yellow | 0.41, 0.36–0.58 | 0.50, 0.43–0.75 | MEASURED |
Format: all 44 local videos are 50 fps CFR; 16:9 at 1920x1080, 9:16 at 1080x1920, no letterbox detected (MEASURED, census). Canvas #FDFDFD in 5/6 frame-0 samples; KyBWJPaF1KI opens on a dark night scene (MEASURED).
- Motion: state changes are overwhelmingly single-frame swaps (360/390 activity events are 1 frame, MEASURED). Rare multi-frame moves exist: fall/slide (qB G0132), tumble and shrink (KyB G0140), pan with slide-on (IUur G0060), drift (3As G0008). Zooms are stepped re-scales of one drawing, not smooth (OBSERVED; KyB G0074-G0078).
- Grammar: one idea, one drawing, about 1 s, then replace. Blank white and full-black frames are used as beats (uIG G0039, G0044; qB G0100).
- Character: bearded caveman, heavy brow bar, oversized nose, yellow tunic with black ovals and zigzag hem, forearm ticks, thick blunt black outline, flat fills, no cast shadow (OBSERVED native, 5 videos). Variants by colour or prop: green tunic plus headdress = other tribe (IUur), curly hair + beads (uIG), blue glow = soul (qB).
- Literalisation of narrated words: "forget bad face" → face erased (f1v G0004); "built like log" → log-body (f1v G0006); "magic orb that change color" → full hue rotation f3254–f3422 (3As, MEASURED). Relation labels ASR_UNCERTIFIED.
- Mixed media exception: real photo cutouts beside drawn reinterpretation (3As G0052/G0054), style breaks: grey painted face, charcoal figure, crayon figures (qB G0078, G0040, G0054).
- Text: rounded bold caps on white, built word by word, placed to reserve space for the next word (uIG G0040-G0042); large enough for mobile at tile scale (OBSERVED); red for emphasis (MISSION:, f1v G0010). Red X overlay as negation (uIG G0036). No captions track observed. On-screen "KrudTalks" (qB G0044), "KRUD" poster (KyB G0120) are in-video text; meaning INFERRED, not channel identity.
- Ending: none of the 6 shows a CTA or end card (reviewer OBSERVED); videos end on a final joke state.
- Reuse: 2 of 3 Shorts are mainly narration from a long video: f1v in qB 95%, uIG in KyB 85% of ASR words; matching holds 12 and 31 (dHash candidates, MEASURED, not pixel-verified). Third Short IUur has no long sibling in this set (xBJ6suQSt98 is held out and unchecked). Publication order differs per topic, so Short-derived-from-long is not established.
- Landscape vs portrait: same drawings recomposed; portrait keeps tighter holds and higher activity-frame share, landscape higher cut rate (provisional, n=3 each).
- Loudness integrated −14.9 to −17.7 LUFS (MEASURED). Not listening: voice, music, SFX unavailable.

## B. Counterexamples and open items
3As is a list of photo→drawing pairs rather than an explanation chain. KyB opens on a dark scene. 30/390 activities are multi-frame and partly sampled. Unresolved segments listed in each quality_gate.json.

## C. Proposed original production choices (NOT source facts; use new character, script, art)
Own simple mascot with one signature colour; one idea per roughly 1 s drawing; single-frame replacement as default; hold the literal word-picture on the narrated word; word-by-word text with reserved space; blank beat before a reveal. Verify synchronisation by listening before adopting any timing rule.
