# xkcd's What If? — continuous visual-forensics campaign goal (v1, recorded 2026-11-04T02:05Z before analysis)

- Channel: xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww` @xkcd_whatif (historical YIOS CH-000004). Identity: channel tab pages (externalId + vanity URL, census/raw/page_videos.html) and prior official watch-page/oEmbed evidence `docs/evidence/what-if-identity-2026-10-10/`. Not minutephysics, not other "What If" channels.
- Census (census/census_summary.json, snapshot 2026-11-04T01:43:22Z): 45 long-form, 46 Shorts, 0 livestreams, 0 uncertain, 91 unique IDs.
- Kit: YIOS_Visual_Forensics_Intelligence_Kit_v1.0 packaged SKILL.md sha256 b7baff3e…bfd9 (operative, invoked); installed copy ~/.claude/skills/visual-ct-scan/SKILL.md sha256 d308d87d… = same v1.0 text + local routing/relationship addenda. validate_kit.py: 0 errors.
- Writer: this session (d2a98830) under stream lock `~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock` (vf_lock.sh v3 with VF_LOCK_DIR override). No other xkcd writer found (no xkcd workspace, no live sessions listed).

## Selected population (selection/selection_v1.json)
- Long: 12 = 10 development + 2 held-out (JcXpCyPc2Xw, BnGqPxnQh9A).
- Shorts: 20 = 17 development + 3 held-out (Ny9m2l6h478, jVy3qd70AqU, rGZ6TsXvi8E).
- Unavailable (no local source, not acquired): alkJ7xScBiw (long), NxVdO7M2YdM, XwJAbyn5uGY (Shorts).

## Per-video contract
Kit DEEP mode with frame-precise onsets: all frames measured; every frame in exactly one HOLD/ACTIVITY segment; every segment classified from viewed tiles; kit deliverables + quality_gate.json. Listening BLOCKED (campaign/AUDIO_LISTENING_CAPABILITY.json) → no video can reach CT_SCAN_COMPLETE or FULL_AV_SIGNOFF; best attainable status VISUAL_ANALYSIS_PARTIAL with listed gaps.

## Expansion and adequacy (practical saturation, not proof)
After the initial sample: add long videos in batches of 3 and Shorts in batches of 5 only when a material new production rule or a reconstruction/held-out failure justifies it. Adequacy = (1) observed formats and eras covered, (2) held-out evaluation passes, (3) two consecutive expansion batches with no material new rule OR exhaustive coverage, (4) kit gates satisfied or limitations listed. The goal is never shrunk to declare completion.

## Finding recorded 2026-11-04T02:55Z — Shorts are mostly narration excerpts (campaign/short_long_text_reuse_population.csv)
Text reuse (catalog plaintext captions, >=6-word matching blocks): 38 of 40 caption-available Shorts reuse >=90% of their words from one long-form video (several non-obvious by title, e.g. kNry0bf7eC0<-8fADp43wJwU, sFTRRdHqZIQ<-EsUBRd1O2dU, 5k8ciEx__5w<--1-ldW4kpLM, mEUqVgGf4e0<-DiWFXv9N0Vs). 2 standalone: oLoxdLfB6Gs, SLd4hnmeW_g (both already selected). 6 unregistered Shorts pending ASR-based check. Text reuse is not proof of visual reuse; visual re-layout is compared per pair in the manual. Selection v1 unchanged (both standalone Shorts already included).
