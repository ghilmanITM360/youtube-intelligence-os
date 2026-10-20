# Local channel media library

This directory records the private, user-supplied media library used for local
research. On Machine B the durable media bytes live at
`/Users/ghilmanislam360/Documents/YIOS-Media-Library/`; the original
worktree-local path `data/local-channel-media/` remains a supported fallback.
Both locations are excluded from ordinary Git and are **not hosted on GitHub or
Git LFS**. The source files remain
unchanged in their original folders. Inventory does not imply ownership,
redistribution rights, completeness of any YouTube channel, or human review of
the audio/video content.

## Rebuild

From the repository root, with the observed trailing space preserved in the
source directory name:

```bash
python3 scripts/build_local_media_library.py \
  --source-root '/Users/ghilmanislam360/Downloads/all channels data ' \
  --repo-root "$PWD" \
  --media-root "$YIOS_MEDIA_ROOT" \
  --ingest
```

The command hashes every source, records `ffprobe` stream metadata, copies via a
temporary file, re-hashes before atomic rename, and skips a destination whose
hash is already correct. A conflicting destination is never overwritten.

Set `YIOS_MEDIA_ROOT=/Users/ghilmanislam360/Documents/YIOS-Media-Library` on
Machine B. Consumers should resolve `original_relative_path` below this root
when it is configured; otherwise resolve `local_media_path` relative to the
repository root. Fall back to `external_source_path` only when `preservation_status` is
`SOURCE_LINK_ONLY`. A successfully copied or previously present exact match is
recorded as the stable final state `LOCAL_COPY_VERIFIED`. Video IDs are accepted only from an explicit bracketed
11-character filename token; other mappings remain `UNKNOWN`.

## Tracked outputs

- `SOURCE_INVENTORY.jsonl`: full file-level evidence and copy state.
- `MEDIA_MASTER.csv`: spreadsheet-friendly mirror of the inventory.
- `CHANNEL_DIRECTORY.csv`: per-source-folder counts and bytes.
- `VIDEO_ID_CROSSWALK.csv`: conservative filename-to-ID mappings and variants.
- `DUPLICATE_GROUPS.csv`: byte-identical SHA-256 groups.
- `INGEST_REPORT.json`: reconciliation totals and errors.
- `SOURCE_MANIFEST_SHA256.json`: hashes of all generated manifests.
- `SMOKE_TEST_REPORT.json`: one-file-per-channel metadata/frame-read proof;
  representative frames are temporary and are not retained.

No transcoding, normalization, remote acquisition, upload, or deletion is part
of this library.

Run the bounded reader smoke test after ingest:

```bash
python3 scripts/smoke_test_local_media_library.py \
  --repo-root "$PWD" \
  --media-root "$YIOS_MEDIA_ROOT"
```
