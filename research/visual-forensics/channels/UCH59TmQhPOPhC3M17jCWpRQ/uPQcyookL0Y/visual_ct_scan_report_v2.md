# Visual CT-scan report v2 — Barely Evolved `uPQcyookL0Y` (checkpoint P) — status `VISUAL_ANALYSIS_PARTIAL`

Source: sha256 `1416669f…c69d`, 1920x1080, 30000/1001 CFR, 14,647 decoded frames (source_manifest.json). v1 report (visual_ct_scan_report.md) preserved.
Audio: ASR only (`ASR_UNCERTIFIED`). Listening `BLOCKED_CAPABILITY` (../AUDIO_LISTENING_CAPABILITY_2026-11-03.json). No AV sign-off.

## 1. Coverage (MEASURED / OBSERVED)
| Domain | Coverage | Evidence |
|---|---|---|
| Timeline | 89 contiguous states v6, 0–14646, all frames measured (FULL_FRAME_MEASUREMENTS.csv) | tables/states_v6_draft.csv, n_v6_validation.json |
| Native art direction | 89/89 states, 2–4 sparse native PNGs each (W001 11) | tables/o_art_consolidated.csv; reviewers 12–21 |
| Intra-state motion | 133 measured-peak strips (8 consecutive frames) reviewed, 178 motion events; states without a ≥1.0 peak have no strip | o_motion_events_W041_W088.csv, agents/reviewer_22,23/motion_events.csv |
| Narration relation | ASR segments 0–75 (76/76) partially assessed against sampled frames; 0 audio-verified | tables/o_narration_consolidated.csv |
| Per-state prompts | 89/89 original image + image-to-video prompts | o_state_prompts_W051_W088.csv, reviewer_22/23 state_prompts.csv |
| Reconstruction | RT-01: M1/M3/M5 timing+geometry PASS, style omitted | reconstruction_test/RT-01/RESULT.json |
Blind spots: frames between sparse samples and outside strips; W001 (28 s) has only 2 strips; 4 states lack strips; audio entirely.

## 2. Observed visual grammar (OBSERVED from viewed frames; counts are of reviewed strip events, not of all frames)
- **Canvas & palette:** recurring near-white card (#fcfcfc 98–100% kmeans share) with near-black ink (#050505) for titles/labels; illustrated scenes use flat saturated fills (greens/sky blues/ochres) with dark outlines (o_art_consolidated palette_observed).
- **Characters:** outlined cartoon heads with textured hair/beard masses, flat torsos, thin single-stroke stick arms; a recurring glasses-wearing teacher in a classroom with chalkboard, pointer and projector (families in tables/o_asset_family_crosswalk_ext.csv — keyword links, INFERRED).
- **Motion vocabulary (178 events):** character motion 36, element enter 29, camera scale 27, camera pan 16, fade 10, element exit 9, text reveal 9, single-frame cut/swap 8, other 9, no visible change 25.
- **Typographic events:** hard-edge left-to-right clip reveals in 3–6 frames (W018 f3127–3129; W045 f8028–8033); trailing-end-first slides from behind an occluder (W022 f3802–3809; W054 f9520–9526, primary-corrected); pop-in with overshoot (W034 f6284–6286).
- **Transitions:** 4–5-frame fades (W002 f844–848 background-only to black; W067 f10859–10863 board picture fade-in); vertical collapse-to-sliver exit (W080 f12982–12985); single-frame pose/prop swaps (W040 mouth f7229/7230, f7298/7299; W039 book f6894/6895).
- **Board/projection motif:** classroom board inserts are photoreal-style images staged with a desk projector (primary check W080 f13085).

## 3. Narration ↔ visual (ASR-based, `SPARSE_PARTIAL_ASR_ONLY_NOT_LISTENED`)
Effective relation counts across 98 assessment rows: LITERAL 44, ILLUSTRATIVE 14, MIXED 13, UNCERTAIN 5, others ≤3. Pattern (INFERRED): literal title/number cards for list structure, illustrative comic beats inside sections. Open: seg 67 ocean insert vs ASR "rivers"; preserved uncertainties 8, 11, 22; seg 25 head/tail; seg 0/4/27 adjudications.

## 4. Unresolved boundary candidates (not applied to v6)
UBC-001 W062 f10316→10317; UBC-002 W016 f2835; UBC-003 W032 f5428→5429; W085b fade-out not observed.

## 5. Interpretation (INFERRED, hypotheses only)
Short fixed-length text/graphic events (3–6 frames) and ~4–5 s median state length suggest a dense "caption-as-punchline" cadence; no retention/CTR claim is made (no first-party analytics).

## 6. Status
`VISUAL_ANALYSIS_PARTIAL` (sparse native + peak-strip coverage; not every motion interval inspected). `CT_SCAN_COMPLETE`: **NOT AWARDED** — audio gate blocked, sparse temporal coverage, untested full-scene reconstruction.
