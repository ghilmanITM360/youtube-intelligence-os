# Canonical identity with transcript evidence pending

## Contract decision

A transcript is not a prerequisite for a canonical video identity. Migration 002 defines videos and transcripts separately, and `register_structured_source.py` already registers workbook-only videos without a transcript row. The complete-transcript requirement in `register_supplied_channel.py/1` was a contract of that acquisition package, not an inventory-wide invariant. Forensic MASTER_WORDS and MASTER_SENTENCES remain derived source declarations; they are not relabeled as acquired YouTube captions.

The supplied-channel importer now supports an explicit, exact-ID declaration of pending transcripts. Its default still requires a complete, reconciled, nonempty transcript pack. This is a controlled extension of the existing importer, not a direct catalog-write bypass or a separate identity system.

## Registration semantics

Use the reviewed source workbook, an existing transcript directory (which may be empty), and repeat `--transcript-pending-id` for each missing video ID:

```sh
python scripts/register_supplied_channel.py \
  --workbook /path/to/reviewed/Master.xlsx \
  --transcripts /path/to/reviewed/transcripts \
  --transcript-pending-id <exact-video-id>
```

The declaration must exactly equal workbook IDs without transcript files. Unknown, duplicate, already-transcribed or incompletely declared IDs fail before registration. A pending workbook row must have no Transcript File and no Transcript Words value. Empty or malformed files still fail; the flag cannot turn them into evidence. Existing duplicate-source and duplicate-video protection remains active.

Identity and metadata retain workbook cell provenance and unchanged source copies/hashes. Pending videos receive no transcript row, no transcript hash, no caption type, no language and no invented word count. Pending identity-only records also leave content format unclassified; duration or a downloaded filename is not a format observation. A `TranscriptPending` ingestion record identifies each gap and the source workbook; the dataset manifest lists the exact pending IDs. Supplied source identity is still subject to the existing channel identity reconciliation. This flag does not independently verify ownership or create a workbook from search results.

## Validation and compatibility

No schema migration or historical data rewrite is needed. Producer version 2 declares the new semantics. Version 1 provenance and manifest contracts remain recognized. Version 2 verification permits absent optional public observations without pretending they were observed, requires exact identity and title plus provenance for each populated observation, reconciles exact pending gap records and manifest IDs, and verifies all copied source hashes, SQLite integrity and foreign keys. Existing-channel registrations validate linked channel provenance rather than requiring the new dataset to have originally created the channel.

Coverage reports explicitly distinguish available, unavailable and pending transcripts. The hook/script consumer retains canonical snapshot identities with a left transcript join, reports missing records as unavailable evidence, and skips their analysis. A missing record cannot become script/hook evidence. Forensic promotion still requires exact catalog identity and the reviewed source contract; the new flag does not promote, alter a crosswalk, guess a title join or regenerate a stage.

Repeated registration is rejected by duplicate source/video checks instead of duplicating evidence. Later transcript acquisition is separate append-only evidence registration; this change does not introduce a transcript-recovery acquisition service or update historical snapshots.

## What If application boundary

At the audited baseline, 9VG0yqq_PHM and X97DDWvxaqQ remain IDENTITY_VERIFIED, TRANSCRIPT_BLOCKED and NOT_REGISTERED. This change supplies an architecture-compatible pending path, but has not registered either video. Their existing official identity evidence is preserved. A reviewed source workbook with provenance for the required metadata must be assembled and validated before any canonical registration and downstream stage/index update. Missing public metrics must not be invented merely to satisfy a package format. No raw media, fabricated transcript, paid acquisition or caption API download is required by this change.

## Review verification

The pending-only hook/script regression reproduces the prior corpus-mismatch failure and now returns an explicit unavailable transcript with no invented hook or script. Existing canonical snapshot/transcript joins were compared directly: the left join returns exactly the same rows as the former inner join on the current inventory. Only the affected reporter dependency fingerprint is updated; existing intelligence output bytes remain unchanged.
