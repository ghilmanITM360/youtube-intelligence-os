# Slot 02 V15 retrospective (pointer and summary)

**Film:** *Why Can a Skydiver Slow Down Without a Parachute?*, V15. The owner approved it as the final production master on 2026-11-25. Its files are in `07-video-productions/SLOT02_skydiver-slowdown/v15/`.

The full reverse-engineering audit of V15 and its V8–V14 history is the master playbook:
- [`02-production-playbooks/UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md`](../02-production-playbooks/UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md): §3 lifecycle, §4 version history and defect lifecycle, §18 root causes and gates G0–G8.

This file does not repeat it. The comparison with Slot 07 is in [SLOT07_PRODUCTION_RETROSPECTIVE_AND_LESSONS.md](SLOT07_PRODUCTION_RETROSPECTIVE_AND_LESSONS.md).

## Five lessons that carried into Slot 07

1. **Acceptance tests on art.** Art without tests caused most of the 15 versions (playbook §18).
2. **Narration first.** The late switch from the 78.2 s to the 110 s take forced a 0.26–1.40× warp.
3. **Separation, not loudness.** The median voice-minus-background gap went from 10.5 dB to 20.7 dB, while both versions were at −16 LUFS.
4. **Continuous anatomy.** The character became one drawing with mesh deformation, after four architecture changes.
5. **One scale, one disclosed lens** for small scientific quantities: net force at 0.9–3.6 % of weight, shown with a ×8 lens.

## Checked during the 2026-11-26 consolidation

- The V15 folder moved, as a whole, to `07-video-productions/SLOT02_skydiver-slowdown/v15/`.
- **Manifest.** `qa/FINAL_MANIFEST_SHA256.txt` (765 entries) verifies OK everywhere except one file. `tools/mix_v15.py` changed by one line: its review-only SFX library path now points to `06-audio-library/sound-effects/SFX_Library_UNVERIFIED_LICENCE`. The new hash is in `qa/FINAL_MANIFEST_ADDENDUM_2026-11-26.txt`.
- **Self-check.** `.venv/bin/python tools/v15.py --check` passes from the new location: 2,641 frames, monotone warp, all 25 shots, minimum altitude 445 m.
- **Final masters.** Hard links with standard names are in `07-video-productions/SLOT02_skydiver-slowdown/FINAL_MASTERS/`; the checksums are unchanged.

## Still open (owner)

- Human listening of the publication mix.
- A Shorts-UI caption test.
- YouTube upload (waiting for an owner instruction).
