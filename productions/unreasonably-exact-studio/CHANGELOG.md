# Changelog

## 2026-11-26: consolidation (Claude, owner directive)

- **Slot 07 V3** is designated the owner-selected final production version; its visual quality is accepted (`07-video-productions/SLOT07_lunar-laser-ranging/OWNER_ACCEPTANCE_RECORD.md`). Listening, the music licence and the publication checks stay open. There is no V4.
- **Workspace reorganised** into numbered folders `01`–`11` and `99`. Every move is in `MIGRATION_MANIFEST.csv`. Moves were atomic renames: all 95 MP4 checksums match their pre-move values.
- **Path fixes, so each project is self-contained.** Three paths changed:
  - Slot 07 `tools/sound_design_v3.py` now reads the music from `audio/music/` inside the project.
  - Slot 02 `tools/mix_v15.py` reads the review-only SFX library from `06-audio-library/sound-effects/SFX_Library_UNVERIFIED_LICENCE`.
  - `.claude/launch.json` points at the new V15 folder.
- **Verification:**
  - the Slot 07 rebuild check passes before and after the move (19 frames, 1.38–1.88/255);
  - Slot 07 `selftest.py` and `render_proofs.py --selftest` pass;
  - Slot 02 `v15.py --check` passes;
  - the V15 manifest is OK except for the one edited tool, which is recorded in an addendum.
- **New:**
  - `FINAL_MASTERS/` with UE_ names (hard links) in both productions;
  - the shared asset library (`04-shared-assets/`, 41 index entries);
  - the engine snapshot and guide (`05-animation-engine/`), with a smoke test PASS;
  - the audio licence register;
  - templates, retrospectives, the tracker, the dashboard and the Slot 03 brief;
  - the project guide.
- **Playbooks:**
  - UE master playbook 1.1 adds §21 (16 Slot 07 lessons, verified kept apart from proposed);
  - HumanCraft 4.1 adds Part VI;
  - new: the Claude–Codex protocol 1.0 and the production standards 1.0.
- **Published** to GitHub branch `production/unreasonably-exact-studio`; the commit is recorded in `11-production-management/MASTER_PRODUCTION_DASHBOARD.md`.

## 2026-11-26 (earlier)

- Slot 07 V1, V2 and V3 produced. The captioned finals were copied to `FINAL_CAPTIONED_VIDEOS/`.

## 2026-11-25

- Slot 02 V15 approved by the owner as the final production master. V13 and V14 were moved to the macOS Trash.
- Top 10 V3 lineup and script package published to GitHub (`5ee988ce`).
