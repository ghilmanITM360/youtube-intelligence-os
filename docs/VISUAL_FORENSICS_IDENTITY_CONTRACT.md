# Visual-forensics identity and counting contract

Applies to channels researched under `research/visual-forensics/` that the registry does not fully cover.

## Identity
- A channel is its YouTube channel ID. A video is its YouTube video ID. Names and handles are labels only.
- "Casually Finance" (`@CasuallyFinance`) and "Casual Finance" are one channel, `UCrNfRFWnLC3tCy1TnyhVQ7g`. Registry spelling is canonical. Casual Economics is a different channel.
- A video ID belongs to one channel. The crosswalk build stops on a conflict.

## Counts stay separate and are never added
| Count | Meaning |
|---|---|
| Registry videos | Rows in `videos`, from ingested packages |
| Census or inventory videos | Unique IDs in a dated channel snapshot or source census |
| In both, source only, registry only | The join of the two |
| Local files | Media on one Mac; a file is not a video entity, and one ID can have several files |

Event, frame and evidence-row counts are not video counts.

## xkcd's What If?
83 is the registry count and 91 is the census count from the 2026-11-04T01:43:22Z snapshot. All 83 are in the 91. The other 8 are `35KZm1yiyIE`, `9VG0yqq_PHM`, `NxVdO7M2YdM`, `TIDHee_Q5Gk`, `X97DDWvxaqQ`, `XwJAbyn5uGY`, `alBQCm0QpJg`, `alkJ7xScBiw`. This is a coverage gap in the registry, not an identity conflict.

## Crosswalk
`data/manifests/VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv` is rebuilt by `scripts/build_visual_forensics_crosswalk.py` from pinned commits. It copies only an ID and a source title, and it never writes a database. `in_registry=false` means not registered; it does not mean the video is unavailable or unresearched.

## What the registry database still needs
The crosswalk makes these videos findable. It does not register them. A registry row comes from `scripts/register_supplied_channel.py`, which writes the inventory catalog; the registry is then rebuilt from it. The importer reads a workbook with sheets `Channel Overview` and `All Videos`. No workbook named below has that shape today, so one must be materialized from the source and reviewed, keeping the source bytes unchanged. Fields the source lacks stay empty.

| Channel | Videos to register | Metadata source | Blocked by |
|---|---|---|---|
| Casual Finance | 210 | PR #37, `CASUALLY_FINANCE_VIDEO_INVENTORY.csv`, `metadata_receipt.jsonl` | Not merged. The channel row exists as `IDENTITY_ONLY` |
| Barely Evolved | 4 | PR #43, `VIDEO_MASTER.csv`, raw Apify rows | Not merged. No channel row |
| Primitive Education | 45 | PR #39, `ALL_PUBLIC_VIDEOS.csv`, all 45 census IDs and titles match | Not merged. No channel row |
| xkcd's What If? | 2: `9VG0yqq_PHM`, `X97DDWvxaqQ` | PR #20, `DS-000035` | Not merged |
| xkcd's What If? | 6: the other census-only IDs | `census/census.csv` at the pinned commit | No reviewed workbook yet. The 2026-11-04 snapshot postdates DS-000035 |

Every video here has no transcript evidence in these sources, so each needs `--transcript-pending-id`. Video URL must be the `watch?v=` form even when the census lists a Shorts URL. Transcript File and Transcript Words stay empty, including where PR #37's CSV holds a placeholder. In the xkcd census, likes and comments read `UNAVAILABLE_LOGGED_OUT_PLAYER`: leave them empty, never 0. This route has not been trial-run for these channels.

## Registry pin
`validate_audit_966.py` pins `data/catalog/youtube_channel_registry.db` by SHA-256 (`39e7a28b…`) as immutable Finance audit input, and hosted CI enforces it. Any registry change, including PR #20 (`5538db9f…`), fails with `source drift` once that gate is on the same branch. Do not edit the frozen hash to pass: the owner has to decide how a new registry version relates to the audit baseline. After any registry change, rebuild the crosswalk.
