GIT SOURCE origin/codex/casually-finance-forensic-research:data/raw/forensic-analysis/casually-finance/README.md
# Casual Finance — channel videos and forensic research (unregistered drop)

Source: public YouTube channel Casual Finance (@CasuallyFinance), downloaded by the user into `~/Downloads/CasuallyFinance`. Research produced 2026-10-11/12 outside this repository.

- `source-videos/` — 17 MP4 files (16 unique videos + one byte-identical duplicate, see `SOURCE_VIDEOS_SHA256.csv`). Raw source evidence: do not modify, recompress or rename. Stored through Git LFS. The two Shorts `turJ6VMfUjI` and `Qof71Ef-3EU` have no local media.
- `forensic-research/` — audiovisual forensic study output (00_MANIFEST … 07_VALIDATION, `_pipeline` scripts and annotations). Start at `forensic-research/07_VALIDATION/HANDOFF.md` and `forensic-research/00_MANIFEST/PROGRESS.json`.

## Status (honest)
- Structural forensics: 14 of 18 selected videos complete (`PASS_STRUCTURAL`); `0ll9rEtoRrs` is in progress (`forensic-research/_work/0ll9rEtoRrs`, partial, not counted complete); `-X6YzlY_8tM` not started; 2 Shorts MISSING_LOCAL.
- Not full sign-off: ASR is Whisper-base (numbers and proper nouns unverified), audio analysed by signal processing only (`AUDIO_LISTENING_UNVERIFIED`), easing not assessed.
- Channel-level DNA/pattern/report files are not yet written.
- Not registered in the dataset catalog, not promoted, and not part of any registry-backed intelligence layer. Facts, observations and hypotheses are labelled inside the research files; never treat them as CH-000004 (What If) evidence.
- Excluded from the drop: regenerable scratch of the in-progress video (`gray.u8`, two decoded `.wav` files, ~580 MB), the duplicate `CasuallyFinance*.zip` archives and the volatile frame staging.
