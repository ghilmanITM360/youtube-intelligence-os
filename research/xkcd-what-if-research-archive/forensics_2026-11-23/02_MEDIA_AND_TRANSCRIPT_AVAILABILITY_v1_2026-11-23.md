# 02 Media and transcript availability (this Mac = Machine B)

Source of truth for counts: `03_CHANNEL_MASTER_INVENTORY.csv` (92 rows), `media_probe_88.csv` (ffprobe + SHA-256 of every file), `scripts/*.py`.

## Source video bytes on this machine

| Location | Files | Identity | Notes |
|---|---|---|---|
| `~/Documents/YIOS-Media-Library/xkcd Channel/` | **88 MP4** (44 long, 44 Shorts), 0.557 GB | named `[videoId].mp4` | All 88 IDs are in the 91-video census. 0 duplicate hashes. All 1920x1080 (long) or 1080x1920 (Shorts), **24 fps**, with audio. Durations are within 0.49 s of census. SHA-256 equals the census `local_sha256` for **88 of 88**, and equals the campaign hash list for **64 of 64**. |
| `~/Documents/YIOS-Media-Library/WhatIfCompetitors-MP4/` | 3 MP4 + info.json | Fossil, Minute Zero, Tracer Project | Competitors, not xkcd. Hashes match the 2026-11-18 manifest. |
| `~/GhilmanProjects/video data of what if/videos/` | 14 MP4 | original source of the older "Brain" | **0 of 14 hashes match the 88-file library**: different encodes (smaller 480p/720p/1080p mixes) of mostly the same videos. Not in the screenshot list; found by name search. |
| `docs/LOCAL_MEDIA_AVAILABILITY.md` (repo) | row for `xkcd Channel` | 88 files, 557,421,212 bytes, `LOCAL_COPY_VERIFIED` | Matches what was found (557,421,212 bytes recomputed 0.557 GB). |

**Missing media (4):** alkJ7xScBiw (long, nuke in Mariana Trench), NxVdO7M2YdM (Short), XwJAbyn5uGY (Short), and Aony69nO5kI (uploaded 2026-11-17, after the census; format not yet classified). The census records 100 local-path entries, all on Machine A (`/Users/ghilmankhan/...`); none resolve on this Mac, which is why the library copy is the one to use here.

## Classification (directive tiers)

| Class | Count |
|---|---|
| FULL_MEDIA_AVAILABLE (with catalog transcript or provisional ASR) | 86 |
| FULL_MEDIA_AVAILABLE, no transcript of any kind | 2 (X97DDWvxaqQ, alBQCm0QpJg) |
| MISSING | 4 |
| AUDIO_ONLY / PARTIAL_MEDIA | 0 |

Audio: all 88 MP4s carry an audio stream (aac), so narration audio is available as source bytes. Nothing in this pass listened to it.

## Transcripts

| Source | Count | Quality |
|---|---|---|
| Catalog plaintext (DS-000017, repo `research/what-if-scripts`) | 83 (43 long, 40 Shorts) | 67 user-generated, 16 auto-generated captions; **no timestamps** |
| Local Whisper (provisional ASR) in campaign `videos/<id>/asr` | 64 videos | provisional, not human-verified, not listening |
| Neither | 2 with media (X97DDWvxaqQ, alBQCm0QpJg), 4 without media | Can be produced locally (whisper.cpp is used in this repo) for the two with media; not done in this pass |

The two "pending" IDs in the brief: **9VG0yqq_PHM** has media and a provisional ASR; **X97DDWvxaqQ** has media and no ASR. Neither has a catalog transcript.

## Other audio/visual evidence already stored

- `~/Documents/YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU/`: deep pass of one video (8fADp43wJwU) including audio stems and per-second levels; status `VISUAL_ANALYSIS_PARTIAL`, "human listening pass still required". It used the **Brain** encode (hash prefix `1fb3c0f4`), not the library file.
- `yios-worktree-preservation-2026-10-21/evidence/what-if-forensic/.../v1.0.0/`: 8 JSONL tables of the older Brain (words, sentences, audio events, AV-sync). Byte-identical to the copy inside the repo (`data/raw/forensic-analysis/preserved-worktree-evidence-2026-10-21/...`, hash verified for `MASTER_AUDIO_EVENTS.jsonl`).
