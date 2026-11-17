# alkJ7xScBiw acquisition — BLOCKED (owner-authorized; no approved method available on this Mac)
- **Checked at:** 2026-11-08T23:34:49Z.
- **Target:** alkJ7xScBiw, "What if you set off a nuke in the Mariana Trench?", published 2026-10-27, 210 s, LONG_FORM. The census shows local_files=0 and playability UNPLAYABLE (logged-out player).
- **Existing method:** the 88 local sources in "~/Downloads/videos in mp3/xkcd Channel/" are yt-dlp copies (named "<title> [<id>].mp4"; see selection_v1.json "local yt-dlp copy").
- **What was found on this machine:**
  - yt-dlp is not on PATH and is not in /opt/homebrew/bin or ~/Library/Python/*/bin;
  - the yt_dlp module cannot be imported in system python3, Homebrew python3.12, the visual-ct-scan venv or the asr venv;
  - this matches the 2026-10-22 readiness audit ("yt-dlp ... Not found on PATH");
  - Spotlight finds no file named with alkJ7xScBiw.
- **Not done:**
  - No install was made: installs are out of scope, and the brief allows only the existing approved method.
  - No browser or screen capture was used. That would not be the approved method, and no source identity hash would exist.
  - Nothing was downloaded, so there is no SHA to verify.
- **Unblock (owner):** either
  - put the yt-dlp file into the source folder from the machine that made the other 88 copies, or
  - approve installing yt-dlp here.

  Then run: xk_ingest.sh alkJ7xScBiw → shasum against the new census row → M0 label on the holds sheet → FROZEN_RULES_v2 journey arm (M1 ≤ 0.13, M2 ruler ≥ 3) if it is JOURNEY_LADDER.
- **2026 verdict:** the 2026 long stratum stays **UNCOVERED**.
- **Journey verdict:** the long JOURNEY_LADDER arm stays **UNTESTED**. A Short ladder (FKXV, v9) was observed, but it is descriptive only.
