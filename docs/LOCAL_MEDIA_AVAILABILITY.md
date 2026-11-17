# Local media availability

This document is the discovery entry point for original channel media already
registered for local research. The file-level authority remains the tracked
manifests under [`research/media-library/`](../research/media-library/README.md);
this page does not duplicate their 456 rows.

## Verified Machine B library

- Durable root: `/Users/ghilmanislam360/Documents/YIOS-Media-Library/`
- Consumer configuration: set `YIOS_MEDIA_ROOT` to the durable root. Scripts
  must not hardcode this machine-specific path.
- Inventory: **456 files** — **454 video** and **2 audio**.
- Size: **4,363,111,708 bytes (4.06 GiB)**.
- Integrity: **all 456 files SHA-256 verified** against the tracked inventory.
- Identity coverage: **389 high-confidence Video ID mappings** and **67
  unresolved mappings**. An unresolved mapping must not be inferred from a
  title or filename.
- Availability: every row is `LOCAL_COPY_VERIFIED` on Machine B. The media
  bytes are **not on GitHub**. Machine A has only its separately verified local
  subset. Never silently assume that original media is present on every Mac.

| Source folder | Canonical Channel ID | Files | Media | High-confidence IDs | Unresolved | Bytes | Availability |
|---|---|---:|---|---:|---:|---:|---|
| `CasuallyFinance` | `UCrNfRFWnLC3tCy1TnyhVQ7g` | 216 | 216 video | 162 | 54 | 1,645,018,552 | `LOCAL_COPY_VERIFIED` |
| `casual_economics` | Not established in this media registry | 11 | 11 video | 0 | 11 | 659,321,738 | `LOCAL_COPY_VERIFIED` |
| `xkcd Channel` | `UC6IxnFzHofFJ5X2PycSMsww` | 88 | 88 video | 88 | 0 | 557,421,212 | `LOCAL_COPY_VERIFIED` |
| `PrimateEconomics-MP4` | `UC14Fb2zWTEZklONPXFbLrTQ` | 29 | 29 video | 29 | 0 | 504,214,667 | `LOCAL_COPY_VERIFIED` |
| `BarelyEvolved-MP4` | `UCH59TmQhPOPhC3M17jCWpRQ` | 3 | 3 video | 3 | 0 | 207,354,224 | `LOCAL_COPY_VERIFIED` |
| `PrimitiveEducation-MP4` | `UCsuQtyrMiUPdHUQ8WaqsFvQ` | 45 | 44 video, 1 audio | 44 | 1 | 203,774,483 | `LOCAL_COPY_VERIFIED` |
| `MonkeBiznis-MP4` | `UCC2nLqBUIy8bagyNMDRiRcA` | 64 | 63 video, 1 audio | 63 | 1 | 586,006,832 | `LOCAL_COPY_VERIFIED` |

Canonical IDs are included only where they are supported by the canonical
channel registry or a published channel-identity record. Folder names remain
source labels and are not silently normalized into channel identities.

## File-level registry

- [`SOURCE_INVENTORY.jsonl`](../research/media-library/SOURCE_INVENTORY.jsonl)
  is the authoritative file-level evidence. It records source folder,
  filename/path, media type, byte count, duration, width, height, codecs,
  SHA-256, Video ID, mapping confidence/evidence, copy verification and
  preservation status.
- [`MEDIA_MASTER.csv`](../research/media-library/MEDIA_MASTER.csv) is the same
  456-entry inventory in spreadsheet-friendly form, including duration and
  resolution fields.
- [`VIDEO_ID_CROSSWALK.csv`](../research/media-library/VIDEO_ID_CROSSWALK.csv)
  is the conservative Video ID-to-filename/path/SHA-256 mapping. Blank IDs and
  `UNKNOWN` confidence remain unresolved.
- [`CHANNEL_DIRECTORY.csv`](../research/media-library/CHANNEL_DIRECTORY.csv)
  is the seven-folder count and byte summary.
- [`SOURCE_MANIFEST_SHA256.json`](../research/media-library/SOURCE_MANIFEST_SHA256.json)
  records hashes for generated registry artifacts.

Before video, thumbnail, animation, script, editing or forensic work acquires a
source, check these registries and resolve the requested Video ID or channel
under `YIOS_MEDIA_ROOT`. If the root or requested file is absent, report it as
locally unavailable; do not treat the manifest as proof that the bytes exist on
the current machine. Do not upload or redistribute these private,
user-supplied third-party media files without separate authorization and rights
verification.
