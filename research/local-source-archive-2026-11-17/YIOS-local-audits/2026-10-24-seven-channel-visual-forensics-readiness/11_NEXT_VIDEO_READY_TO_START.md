# 11 — Next video ready to start (NOT started)

**Queue position 1 · Casual Finance · `o3FQcd91MIs` — "Why The Dumbest Investors Win (it's not why you think)"** · long-form · 278.09 s · 1280x720 · 30 fps · H.264 + AAC 44.1 kHz stereo

- Source: `/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/Why The Dumbest Investors Win (it's not why you think) - Casual Finance (720p, h264).mp4`
- Size 5,896,501 bytes · SHA-256 `82ab2b63ce250723f37e569d15ecf0a8b67c22f1841ec14637216d34e4a89c85` (matches Machine B manifest and the Casually-Finance forensic source inventory).
- Registered metadata (`research/casually-finance-video-inventory@1adfdeb9`, snapshot 2026-10-19): published 2025-07-28, 278 s, 237,893 views, thumbnail URL `https://i.ytimg.com/vi/o3FQcd91MIs/maxresdefault.jpg` (not stored locally).
- Existing research: STRUCTURAL_SAMPLED only — `codex/casually-finance-forensic-research@043b85bf` rows: 47 shots, 76 states, 75 motions, 77 assets, 139 audio events, 122 sync rows, 777 ASR words (Whisper-base; uncertified). Evidence images are not in Git; full-duration continuous visual review NOT_STARTED; AV sign-off BLOCKED (listening unavailable). Machine A's own CF long-form procedure (`STATUS.json` → `longform_procedure`) designated this the **pilot** (shortest long-form).
- Why first: unfinished work with sha-verified prior evidence, lowest long-form workload (HEAVY, 4.6 min), 720p source, and an existing written procedure; Shorts and long-form remain separately identifiable in the queue.

## Identity status — owner decision needed
Class `HIGH_CONFIDENCE_NEEDS_REVIEW`: filename has no embedded ID. Evidence: exact normalized title match to the registered row; duration 278.09 s vs registered 278 s; prior CF source inventory records `PRIOR_SHA256_VERIFIED_ID+TITLE+DURATION`; Machine B hash equal; no competing candidate. Please confirm this identity (or choose the first `EXACT_ID_MATCH` alternative: queue #22, xkcd What-If `8fADp43wJwU`, "If all humans died, when would the last light go out?", 303.86 s, 1920x1080, historical claim unverified, official transcript registered).

## Prerequisites to fully analyze it
1. Owner authorization for exactly this one video (and confirmation of identity above).
2. Load the validated skill externally (SKILL.md + 14 references + templates) — no install.
3. Transcript: no official one; run local whisper (`small.en`/`base` cached) → `ASR_UNCERTIFIED`; or acquire captions separately (not authorized).
4. Scripts: obtain the CF forensic scripts from Git (`090f84b3`) into an owner-approved external folder (no worktree), or re-implement with ffmpeg + numpy/Pillow.
5. Dense native-frame review windows from 30 fps source; dedicated check for 24→30 fps conform and VFR before claiming timing.
6. Human listening for any AV sign-off (agent cannot hear).
7. Disk: ~11 GB free; budget ≈ 1–2 GB scratch; evidence in a new `/Users/ghilmankhan/YIOS-local-audits/…` folder.
8. Resource gate before starting: re-read five-hour/weekly/context (last: 10 % / 7 % / 26 %).

Expected honest outcome: `CT_SCAN_COMPLETE_WITH_EVIDENCE` within declared coverage + `AUDIO_LISTENING_PENDING`; never `FULL_AV_SIGNOFF_COMPLETE` without a human listener.
