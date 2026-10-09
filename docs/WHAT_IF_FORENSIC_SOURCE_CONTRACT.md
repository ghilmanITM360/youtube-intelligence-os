# What If forensic source contract

The external `production_intelligence_brain` release 1.0.0 remains read-only. Set
`YIOS_WHAT_IF_CORPUS_ROOT` to the directory containing `videos/` and
`production_intelligence_brain/`, then run:

```sh
python3 scripts/validate_what_if_source_contract.py
```

The [crosswalk](../data/manifests/what-if-forensic-source-v1.json) records all
14 source files, their actual SHA-256 and size, the source-to-forensic slug,
candidate YouTube ID, identity status, and evidence. The validator rehashes
the MP4 bytes through portable relative paths. It rejects changed source
release artifacts, missing media, duplicate source IDs, and invalid duplicate
canonical assignments. The stale `ABSOLUTE_PATH` column in the source package
is never used or rewritten.

Ten IDs already exist in the CH-000004 catalog. On 2026-10-09, the public
YouTube video pages for [9VG0yqq_PHM](https://www.youtube.com/watch?v=9VG0yqq_PHM)
and [X97DDWvxaqQ](https://www.youtube.com/watch?v=X97DDWvxaqQ) displayed
`xkcd's What If?` as owner and linked to `@xkcd_whatif`. They are verified
external identities but are **not yet registered** in the local YIOS catalog.
They must enter through the existing controlled channel acquisition path,
which requires a cost cap, before forensic observations can join to them.
SRC01 and SRC02 have no independently verified YouTube ID and remain
`UNRESOLVED`; title or slug similarity is insufficient.

This contract does not create videos, import observations, replace metric
snapshots, or copy raw media into Git.
