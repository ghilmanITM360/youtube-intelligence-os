# Continuation handoff - 8fADp43wJwU
- Source SHA-256: 1fb3c0f4f510fe724749105425e31c8d7f5e9a6053d41e8b67e21f6a2c0a11d9 (copy: GhilmanProjects/video data of what if/videos/...). Other copy sha 973bb97a... differs by 51 bytes.
- Status: VISUAL_ANALYSIS_PARTIAL; audio not listened; no AV sign-off. No YIOS ledger/status was modified; repository untouched.
- Next work (in order): (1) native dense windows (4-24 fps) at S02 logo motion (8.7-10.7 s), S16 nacelle (128-137 s), S23 (194-200 s), S25 lane steps (210-219 s), and 4 weak boundaries (78.9, 172.1, 191.2, 200.2 s); (2) human listening pass (timed ASR transcript now in audio/; ASR is not hearing); (3) resolve 76,000,000 vs 'six million'; (4) compare with prior run `video_forensics_output/if_all_humans_died`; (5) re-run gates.
- Tools used: ffmpeg per-frame detector `build/` (ydiff in detector/), 1fps frames in frames_1fps, sheets in sheets/.
- Evidence folder: /Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU
- Owner of canonical branch: not touched. Disk free was ~26 GiB (98% used).

- Audio added 2026-11-17: whisper medium.en timed transcript (audio/), demucs stems (audio/demucs/), per-second stem levels CSV. Human listening of both stems still required for the audio gate. Venv: .venv-demucs (uv Python 3.12; Homebrew python venv/ensurepip is broken on this Mac).
