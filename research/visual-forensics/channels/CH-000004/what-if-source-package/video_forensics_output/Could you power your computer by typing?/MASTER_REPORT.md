# Video forensic reconstruction — videoplayback

## Source summary

[videoplayback.mp4 manifest](00_source/SOURCE_MANIFEST.md): 100.791667 seconds, 1080×1920, 9:16, 24 fps, 2,419 frames, H.264. No audio stream.

## Observed production DNA

See [VISUAL_DNA.md](02_analysis/VISUAL_DNA.md) for the evidence-supported drawing, color, typography and motion rules. The source uses held ink illustrations, additive graphics, localized state replacements and short reveals; all shots have locked framing.

## Counts

| Measure | Count |
|---|---:|
| Shots | 13 |
| Meaningful visual states, including reveal endpoints/phases | 97 |
| Unique production asset IDs, variants grouped | 40 |
| Intra-shot motion/change events, excluding hard cuts | 59 |
| Required unique source image prompts | 18 |
| Verified audio assets | 0 |

## WAY 1 — CapCut overview

[LIMITED — CapCut build guide](03_capcut/CAPCUT_REBUILD.md). Every shot and A-ID has a layer/edit recipe. Source-aligned stills and exact graphic overlays are the closest route to the observed pixels. Limitations below apply.

## WAY 2 — Image-to-video overview

[LIMITED — I2V build guide](04_image_to_video/I2V_REBUILD.md). Reuse generated masters; hold static scenes; composite exact labels, masks and abrupt changes. Animation prompts cover observed changes without authorizing invented motion. Limitations below apply.

## Important fidelity limitations

- The supplied file has no audio stream. Narration/music/SFX and spoken synchronization remain UNKNOWN; both workflows reproduce the supplied silent playback only.
- Original source layers, font, software/model and asset provenance are UNKNOWN. Source-derived/traced stills can match visible geometry; freshly generated linework/font/objects are approximate.
- Tiny scientific-body marks are not readable prose; portions of book text and calendar dates are clipped/too small for certain transcription. Preserve the source artwork rather than invent wording.
- Mask paths and soft light falloff are measured visual approximations; original easing/effect values cannot be recovered. Frame onsets are measured; first faint pixels of reveals can differ by about one frame.
- This deliverable is the analysis, evidence and independently usable reconstruction specifications. It does not include a native CapCut project, generated image/video assets or an exported rebuilt video.

## File index

- [Source manifest](00_source/SOURCE_MANIFEST.md) and [raw metadata](00_source/metadata.json)
- [Overview contact sheet](01_evidence/CONTACT_SHEET.jpg), [evidence index](01_evidence/EVIDENCE_INDEX.md), and [source PNGs](01_evidence/frames/)
- [Canonical timeline](02_analysis/TIMELINE.csv), [assets](02_analysis/ASSET_MANIFEST.csv), [motion events](02_analysis/MOTION_EVENTS.csv), [visual DNA](02_analysis/VISUAL_DNA.md)
- [CapCut reconstruction](03_capcut/CAPCUT_REBUILD.md)
- [Image prompts](04_image_to_video/IMAGE_PROMPTS.md), [animation prompts](04_image_to_video/ANIMATION_PROMPTS.md), [I2V reconstruction](04_image_to_video/I2V_REBUILD.md)
- [Audio map](05_audio/AUDIO_MAP.md)
- [Resume state](RUN_STATE.json) and [runnable verification](00_source/verify.py)
