# Senior Health 16-channel acquisition (entry point)

Acquired 2026-11-11 via Apify `streamers/youtube-scraper`. Neal K. Shah excluded by owner; Dr Rehan Omar (DS-000032) is a separate dataset and not included.
Canonical location (this replaces the earlier ~/YIOS-local-audits copy, which is kept until the owner approves its removal).

| Layer | Path |
|---|---|
| Raw Apify JSON (immutable; pilot/, probe/, full/) | data/raw/channel-data/senior-health-16-acquisition/apify/ (git-ignored by data/raw/** rule) |
| Extracted CSV/JSONL/XLSX | data/extracted/channel-data/senior-health-16-acquisition/ |
| Manifest, validation, checksums | data/manifests/senior-health-16-acquisition/ |

Status: 15 of 16 channels, 308 videos (all regular; 0 Shorts, 0 streams found), 308/308 metadata, 307/308 plain-text transcripts
(3 creator, 304 auto). Registry NOT updated; no DS-ID allocated.

## Open gaps (do not claim more than this)
- DoctorLaura-e1w1o (UCBLbqhYNAve3LmpThhB4OXA): 67 videos, NOT acquired. See DOCTORLAURA_PENDING_PLAN.md.
- Transcripts are plaintext only: NO timestamped segments for any video (timestamps = NOT_PROVIDED_BY_ACTOR_PLAINTEXT_MODE). Timestamped SRT coverage: 0/308, unverified.
- pZ_TXPAngLA (DrVitalisHealth): no captions returned by the actor -> TRANSCRIPTION_PENDING.
- Possible orphan billed run from a 502 during the batch: unverified.

Integrity: SHA256SUMS.txt (paths relative to the original package root: raw/ -> apify/, CSV/JSONL/XLSX -> extracted/, others -> manifests/).
