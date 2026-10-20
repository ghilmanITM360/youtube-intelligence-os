# Resume here — local channel media library

Issue: #40
Branch: `research/local-channel-media-library`

Completed local ingest state:

- Source root: `/Users/ghilmanislam360/Downloads/all channels data ` (the
  trailing space is part of the directory name).
- Local-only project path: `data/local-channel-media/`.
- Seven folders present; 456 files; 4,363,111,708 bytes; 454 video and two
  standalone audio files.
- 456 local copies SHA-256 verified; zero copy conflicts; zero `ffprobe`
  errors. A second run produced the same manifest hash.
- 389 files have high-confidence bracketed YouTube IDs; 67 remain unmapped.
- One byte-identical duplicate group contains two CasuallyFinance files. The
  folder currently contains 216 physical CasuallyFinance files (162 mapped,
  54 unmapped), so it must not be rewritten to the older 54/48 checkpoint.
- One temporary representative frame per channel was successfully extracted
  and deleted. No caption or transcript files were present in the seven source
  folders.
- Machine B durable root:
  `/Users/ghilmanislam360/Documents/YIOS-Media-Library/`. All 456 files and
  4,363,111,708 bytes were independently re-hashed there with zero mismatches.
  Set `YIOS_MEDIA_ROOT` to that path. The worktree-local copy and original
  Downloads source were retained pending owner-directed cleanup; neither is
  GitHub/LFS-hosted.

Do not upload media bytes or infer channel completeness from the local folders.
The next bounded action is evidence-led reconciliation of the 67 unmapped files
against registered source metadata; filename similarity alone is insufficient.
