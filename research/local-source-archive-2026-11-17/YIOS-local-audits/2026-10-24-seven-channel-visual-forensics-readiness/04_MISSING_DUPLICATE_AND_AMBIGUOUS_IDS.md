# 04 — Missing, duplicate and ambiguous IDs (Machine A)

Classification hierarchy applied: (1) verified original ID in a trusted manifest, (2) exact bracketed ID in filename that also exists in registered metadata for that channel, (3) independent title + duration corroboration, (4) manual review. Duration alone was never used; the closest title was never silently chosen.

## Class counts (456 files)
| Class | Files |
|---|---|
| DUPLICATE_MEDIA | 6 |
| EXACT_ID_MATCH | 386 |
| HIGH_CONFIDENCE_NEEDS_REVIEW | 59 |
| SOURCE_NOT_REGISTERED | 5 |
| AMBIGUOUS_IDENTITY | 0 |
| UNREADABLE_MEDIA | 0 |
| REGISTERED_SOURCE_MISSING (registered rows with no local file) | 1 |
| VERIFIED_MANIFEST_MATCH | 0 (no manifest carries an *independently verified* original ID for these files; manifest IDs found were themselves title+duration based, so none were upgraded) |
Additionally 2 files are audio-only (`.m4a`; IDs 2i22ZYPzwk0 and cZYdi9aFv6I) — identity exact, but they are **not eligible for visual analysis**.

## A. HIGH_CONFIDENCE_NEEDS_REVIEW — 65 files (59 unique videos + 6 duplicate files)
All are files with **no bracketed YouTube ID**: 54 CasuallyFinance files (`... - Casual Finance (720p/1080p, h264).mp4`, `*-SnapYT.App.mp4` truncated-title Shorts, a few plain titles) and all 11 casual_economics files (`... - Casual Economics (720p, h264).mp4`). Each resolved to exactly one registered row by normalized title (exact or truncated-prefix) AND duration within 1.5 s; 64 of 65 independently by this run, 1 by an earlier manifest ID (title+duration based). They also agree with: Machine A CF `SOURCE_MEDIA_INVENTORY` (sha-verified, `PRIOR_SHA256_VERIFIED_ID+TITLE+DURATION`), the Casual Economics `LOCAL_SOURCE_MANIFEST` (exact SHA256+size), and Machine B hashes. They are **strong but not cryptographic or ID-embedded**, so an owner confirmation is requested before treating them as final. No contradictory candidates were found. Machine B previously left 67 files unmapped; this reconciliation maps 65 of those with the above caveat and leaves 0 unresolved (the remaining 2-file difference from Machine B's 389-mapped figure is probably the 2 audio-only files, which do carry IDs; not independently verified).

## B. DUPLICATE_MEDIA — 6 files (all CasuallyFinance; canonical copy kept per ID)
- `Why Japan's Economy Is Awful - Casual Finance (720p, h264) (1).mp4` (3,999,999 bytes, sha256 73641860dea2…) → byte-identical copy of: Why Japan's Economy Is Awful - Casual Finance (720p, h264).mp4
- `Americas-Debt-Hasnt-SnapYT.App.mp4` (3,849,371 bytes, sha256 139c73b33a07…) → different-bytes variant of: America's Debt Hasn't Broken... Yet - Casual Finance (720p, h264).mp4
- `Nothing-Forces-the-SnapYT.App.mp4` (5,028,275 bytes, sha256 fac480472f90…) → different-bytes variant of: Nothing Forces the Government to Fix The 40 Trillion Debt - Casual Finance (720p, h264).mp4
- `Were-Fighting-A-SnapYT.App.mp4` (3,581,672 bytes, sha256 077d6fec6cfd…) → different-bytes variant of: We're Fighting A Battle Against the Market - Casual Finance (720p, h264).mp4
- `Somebody-Is-Quietly-SnapYT.App.mp4` (3,857,635 bytes, sha256 c27a1a2a4d96…) → different-bytes variant of: Somebody Is Quietly Repricing America - Casual Finance (720p, h264).mp4
- `Why Japan's Economy Is Awful.mp4` (3,999,910 bytes, sha256 379b7617468d…) → different-bytes variant of: Why Japan's Economy Is Awful - Casual Finance (720p, h264).mp4
Variants share the ID by title+duration only (class A caveat). The canonical choice favours the file already used in prior sha-verified forensics, then higher resolution. Unique CF videos = 210.

## C. SOURCE_NOT_REGISTERED — 5 xkcd What-If files
Filename IDs are well-formed and Machine B maps them with HIGH confidence, but these IDs are **absent from every registered metadata dataset found** (registry DB, 12-channel dataset, other branches):
- `35KZm1yiyIE` — What if all your DNA suddenly vanished？ [35KZm1yiyIE].mp4 (149.81 s, 1080x1920)
- `9VG0yqq_PHM` — If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4 (162.26 s, 1920x1080)
- `TIDHee_Q5Gk` — What if all visible light was a single beam？ [TIDHee_Q5Gk].mp4 (123.92 s, 1080x1920)
- `alBQCm0QpJg` — More weird and worrying questions [alBQCm0QpJg].mp4 (70.031 s, 1080x1920)
- `X97DDWvxaqQ` — Could you power your computer by typing？ [X97DDWvxaqQ].mp4 (100.84 s, 1080x1920)
Two of them (`X97DDWvxaqQ`, `9VG0yqq_PHM`) are listed in the What-If forensic source manifest as `NEW_VERIFIED_CANONICAL` (public owner verified) but "catalog registration remains separate". Consequence: video identity plausible, **registered metadata absent** (no title/date/views in YIOS). Safe resolution: register metadata through the normal YIOS acquisition path (owner-authorized; no paid acquisition was started).

## D. REGISTERED_SOURCE_MISSING — 1
- Barely Evolved `4X3xd3MDZro` "The Most Brutal Punishments in Human History" (654 s, REGULAR) is registered but no local file exists (only 3 of the 4 registered Barely Evolved videos are on disk: GNaBxt_zIRA, mNLNb-Z4T0M, uPQcyookL0Y).

## E. Other discrepancies and limits
- Registered vs local duration: every mapped video is within 2 s (0 outliers).
- Audio-only extras: 2 (see above); MonkeBiznis and PrimitiveEducation each have 1 registered video whose only local copy is audio-only.
- Registered metadata is a **registered snapshot**, not guaranteed full lifetime channel coverage: Barely Evolved has only 4 registered videos; Casual Economics has 11 (rounded UI counts, no exact date/views, 2026-10-12); the 1,612-video Finance universe does not contain these channels' full catalogs (CasuallyFinance has 0 videos in `youtube_channel_registry.db`; its 210 rows come from `research/casually-finance-video-inventory@1adfdeb9`). "monke" (`@monkebiznis`) is distinct from "MonkeyExplains"; the `monkey-explains-1999-metadata` branch was deliberately not used for MonkeBiznis.
- Frozen performance snapshots (views/likes) were read, never refreshed.
