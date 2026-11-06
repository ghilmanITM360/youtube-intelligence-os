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
The crosswalk makes these videos findable. It does not register them. A registry row needs an ingested metadata package, so that no field is invented:
- Casual Finance: inventory in draft PR #37, not merged.
- Barely Evolved: metadata in draft PR #43, not merged; the channel is not in the registry.
- Primitive Education: only a source census is on its branch, so full video metadata must be sourced first.
- xkcd's What If? 8 videos: census metadata only. PR #20 has a transcript-pending route to review.
