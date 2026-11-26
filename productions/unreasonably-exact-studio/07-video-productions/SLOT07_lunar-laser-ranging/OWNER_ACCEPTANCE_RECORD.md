# Slot 07 owner acceptance record

**Film:** *How Long Does a Laser Take to Reach the Moon and Back?* (Unreasonably Exact, Top 10 slot 07, vertical Short)
**Version:** V3, 96.000 s, 1080×1920, 30 fps, 2,880 frames
**Recorded:** 2026-11-26, by Claude, from the owner's written directive in the Claude Code chat

## 1. What the owner decided (quoted from the directive)

> "I am satisfied with the visual quality of Slot 07 V3. Designate V3 as the owner-selected final production version … Do not create V4 or unnecessarily redesign the film."

| Decision | Status |
|---|---|
| V3 is the **owner-selected final production version** of Slot 07 | **RECORDED 2026-11-26** |
| **Visual quality** of V3 (picture, artwork, animation, typography, on-screen disclosures) | **OWNER ACCEPTED 2026-11-26** |
| No V4 and no redesign | **BINDING**: the V3 renders are locked. The engine and library copies may change, but the film's files do not |

## 2. What the owner has NOT accepted (still open)

The owner's visual acceptance is kept separate from these. None of them may be marked done by an agent.

| Check | State | Why it is still open |
|---|---|---|
| **Music licence** (Small_Variables.mp3) | **OPEN: owner evidence needed** | The file carries no metadata and no licence or ownership document has been supplied. It is **not** commercially cleared. |
| **Human listening** (headphones and phone speaker) | **NOT PERFORMED** | Claude cannot hear. Items to check: voice always clear, the drop before "About two and a half seconds", the 55.58 s music seam, the F-major accents against the track, the ending resolve. |
| **Muted-viewer test, and Shorts UI overlap** | **NOT PERFORMED** | The disclosure notes are about 12 pt at phone width. Captions have not been tested under the YouTube Shorts UI. |
| **Technical publication checks** | **PARTLY DONE** | Duration, loudness (−16.4 LUFS, −2.0 dBTP) and frame count are measured (`renders/roughcut_v3/FINAL_PRODUCTION_QA.md`). Title, description, thumbnail and upload settings are not prepared. |
| **YouTube upload** | **NOT DONE, and not authorized** | The owner directive says "Do not upload anything to YouTube." |

## 3. Which file may be used for what

| File (`FINAL_MASTERS/`, hard links to `renders/roughcut_v3/`) | Use |
|---|---|
| `UE_SLOT07_LUNAR_LASER_RANGING_V03_FINAL_RIGHTS_CLEAR.mp4` | **The publication candidate.** It has synthesized sound only: the V3 SFX plus the original pad, moved to F. |
| `UE_SLOT07_LUNAR_LASER_RANGING_V03_CAPTIONS_RIGHTS_CLEAR.mp4` | Publication candidate with burned captions. |
| `UE_SLOT07_LUNAR_LASER_RANGING_V03_FINAL_MUSIC_REVIEW.mp4` | **Private review only** (contains Small_Variables.mp3). Promote it to publication only once the licence evidence is on file. |
| `UE_SLOT07_LUNAR_LASER_RANGING_V03_CAPTIONS_MUSIC_REVIEW.mp4` | Private review only. A copy is also in `../../FINAL_CAPTIONED_VIDEOS/`. |
| `UE_SLOT07_LUNAR_LASER_RANGING_V03.srt` | Subtitles for either master: 49 cues, the same text and timing. |

Checksums: `FINAL_PACKAGE_MANIFEST.md` (deliverables) and `qa/FINAL_MANIFEST_SHA256.txt` (every project file).

## 4. Previous versions

V1 (`renders/roughcut/`) and V2 (`renders/roughcut_v2/`) are **retained** as the owner asked ("Retain the previous versions until the final rebuild and dependency checks are complete"). Those checks are now complete: see `REBUILD_INSTRUCTIONS.md` §3, run on 2026-11-26. Deleting V1 or V2 is a separate owner decision. Nothing has been deleted.
