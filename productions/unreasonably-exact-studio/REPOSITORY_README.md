# Unreasonably Exact studio (version-controlled copy)

This folder mirrors the production system kept in the owner's local workspace (`~/workprojects/unreasonably-exact/` on Machine B). It contains:
- the documents;
- the source code;
- the rig data;
- the small reusable artwork that is approved in a film.

**Start with** [`START_HERE.md`](START_HERE.md), then [`UNREASONABLY_EXACT_PROJECT_GUIDE.md`](UNREASONABLY_EXACT_PROJECT_GUIDE.md). Every path in those documents is relative to the workspace root, which is this folder.

## What is here

- Both master playbooks, updated 2026-11-26: UE 1.1 and HumanCraft 4.1.
- The Claude–Codex protocol and the production standards.
- The project guide, the tracker, the dashboard and the Slot 03 brief.
- The retrospectives.
- The templates.
- The reusable asset cards and index. The `APPROVED_IN_FILM` PNG layers (≤ 2.2 MB each) and the OFL fonts are committed.
- The engine (`05-animation-engine/`) and the full **source** of both finished productions: code, rig JSON, CSV/JSON/MD records and QA reports.

## What is NOT here (handled separately)

| Not committed | Why | Where it is |
|---|---|---|
| Final MP4s, stems, narration WAV/MP3 | large media | local workspace; checksums in [`EXTERNAL_MEDIA_MANIFEST.csv`](EXTERNAL_MEDIA_MANIFEST.csv) |
| 4096×2048 Earth/Moon textures | large-resolution source textures | local `04-shared-assets/celestial/`; checksums in the manifest |
| Small_Variables.mp3 and the SFX Library | **no licence evidence** | local `06-audio-library/`; see `06-audio-library/licensing/MUSIC_AND_SFX_LICENCE_REGISTER.md` |
| Reference photographs, Codex run PNGs, candidate and rejected art | licence mix (some are CC BY-SA), duplicates, not approved | local projects (`codex_handoff/`, `research/`) |
| Codex run logs (`*.log`) | ignored by the repo `.gitignore` | local `codex_handoff/runs/*/codex.log` |
| Files whose names contain "script" or "transcript" (narration transcripts, historical scripts) | they would enter the AI-slop gate as production scripts. The approved scripts already live in `productions/unreasonably-exact-script-rewrite-v3/` | local workspace |
| Python virtual environments, whisper models | reproducible from `requirements` files | local |

The rebuild instructions (`07-video-productions/SLOT07_lunar-laser-ranging/REBUILD_INSTRUCTIONS.md`, and `v15/START_HERE.md` for Slot 02) need the local media. This copy is enough to read, review and reuse the code and documents, but not to re-render a film by itself.
