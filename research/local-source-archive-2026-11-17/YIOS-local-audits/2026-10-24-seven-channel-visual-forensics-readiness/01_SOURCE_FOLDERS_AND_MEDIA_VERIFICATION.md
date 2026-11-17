# 01 — Source folders and media verification (Machine A, read-only)

Verified at 2026-10-24T08:57:02Z on Machine A (`Ghilmans-Laptop.local`, user `ghilmankhan`). Nothing was renamed, moved, re-encoded, extracted, overwritten or deleted. Media were only probed with `ffprobe` (no decode) and SHA-256 hashed (read).

## 1. Exact directory
`/Users/ghilmankhan/Downloads/videos in mp3/` exists. Name is lower-case with two single spaces and **no trailing space**. It contains: seven channel folders, seven ZIP preservation copies (`BarelyEvolved-MP4.zip`, `CasuallyFinance (2).zip`, `MonkeBiznis-MP4.zip`, `PrimateEconomics-MP4.zip`, `PrimitiveEducation-MP4.zip`, `casual_economics.zip`, `xkcd Channel.zip`), and the extracted `YIOS_Visual_Forensics_Intelligence_Kit_v1.0` folder + `.zip` (not a channel; excluded from all counts). ZIPs were treated as preservation copies and NOT counted as extra videos; they were not opened.

**The folder name "mp3" is misleading:** the content is 454 H.264/AAC MP4 video files and 2 standalone `.m4a` audio-only files (DASH `f140` audio streams): `MonkeBiznis-MP4/4 Signs You_re An NPC [2i22ZYPzwk0].f140-7.m4a` and `PrimitiveEducation-MP4/caveman explain how mortgage work - part 3 [cZYdi9aFv6I].f140.m4a`. No MP3 files exist.

## 2. Per-channel population
| Folder | Channel (registry) | Files | .mp4 | .m4a (audio-only) | Size GB | Hours | Duplicate files | Unique videos (IDs) | Registered metadata rows |
|---|---|---|---|---|---|---|---|---|---|
| CasuallyFinance | Casual Finance | 216 | 216 | 0 | 1.645 | 9.74 | 6 | 210 | 210 |
| casual_economics | Casual Economics | 11 | 11 | 0 | 0.659 | 2.38 | 0 | 11 | 11 |
| xkcd Channel | xkcd's What If? | 88 | 88 | 0 | 0.557 | 3.63 | 0 | 88 | 83 |
| PrimateEconomics-MP4 | Primate Economics | 29 | 29 | 0 | 0.504 | 2.63 | 0 | 29 | 29 |
| MonkeBiznis-MP4 | monke (@monkebiznis) | 64 | 63 | 1 | 0.586 | 3.99 | 0 | 64 | 64 |
| PrimitiveEducation-MP4 | Primitive Education | 45 | 44 | 1 | 0.204 | 0.62 | 0 | 45 | 45 |
| BarelyEvolved-MP4 | Barely Evolved | 3 | 3 | 0 | 0.207 | 0.44 | 0 | 3 | 4 |
| **TOTAL** | | **456** | **454** | **2** | **4.363** | 23.42 | **6** | **450** | 446 |

- 456 files, 4,363,111,708 bytes (4.363 GB). **All 456 files are readable by ffprobe; 0 corrupt/unreadable.** Container for all: `mov,mp4,m4a,3gp,3g2,mj2`. Video codec: H.264 for all 454 video files. Every video file carries ≥1 audio stream (AAC).
- Unique identities: 450 video IDs = 448 with a video stream + 2 audio-only. 6 files are duplicate media (1 byte-identical copy `... (1).mp4`, 5 same-ID different-encode variants), all in CasuallyFinance.
- Resolution mix: {'1080x1920': 248, '1920x1080': 139, '360x640': 24, '720x1280': 20, '1280x720': 18, '1906x1080': 2, '1918x1080': 2, '1914x1080': 1}. Frame rates (avg_frame_rate): {30.0: 217, 24.0: 171, 50.0: 44, 60.0: 8, 29.97: 8, 25.0: 4, 23.976: 2}. Frame count from container `nb_frames` is present for 413 of 456 files; elsewhere it is left blank rather than estimated (unbounded decode was not allowed).
- Aspect ratios are reduced from pixel width/height (1080x1920 = 9:16 Shorts; 1920x1080 / 1280x720 = 16:9).

## 3. Independent hash verification
Machine B's published media-library manifest (`origin/research/local-channel-media-library@78e8fd2d`, `research/media-library/MEDIA_MASTER.csv`) lists 456 files / 4,363,111,708 bytes. **Machine A's own fresh SHA-256 of all 456 files matches that manifest 456/456 (hash and byte count), with zero Machine-B video-ID conflicts.** This is a hash agreement between two machines' copies of the same bytes; it proves byte identity, not YouTube identity.

## 4. What this does and does not prove
- Proven: the seven folders exist locally with playable, byte-verified media.
- Not proven: that any folder is the *complete* channel (registered metadata, see file 03, is the only completeness evidence).
- Per-file detail: `02_SEVEN_CHANNEL_LOCAL_VIDEO_INVENTORY.csv` (path, filename, extension, container, size, duration, fps, frame count where available, resolution, aspect, codecs, audio, readability, embedded tags, candidate ID, identity class/confidence, SHA-256, trusted-hash reference, duplicate status).
- Only 26 files carry an embedded container `title` (with `artist=...`, e.g. Casual Finance long-forms); none carry a YouTube video ID. Identity therefore relies on filename IDs, registered metadata and manifests (see file 04); embedded titles are corroboration only.
