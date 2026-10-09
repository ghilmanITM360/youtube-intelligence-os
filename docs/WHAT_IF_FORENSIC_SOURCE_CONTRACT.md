# What If forensic source contract

The external `production_intelligence_brain` release 1.0.0 remains read-only. Set
`YIOS_WHAT_IF_CORPUS_ROOT` to the directory containing `videos/` and
`production_intelligence_brain/`, then run:

```sh
python scripts/validate_what_if_source_contract.py
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
before forensic observations can join to them. The owner has now authorized an official uploads-playlist refresh; execution is blocked by unavailable API authorization and the absence of an existing official acquisition implementation. A paid Apify fallback still requires a separately approved cost cap.
SRC01 and SRC02 have no independently verified YouTube ID and remain
`UNRESOLVED`; title or slug similarity is insufficient.

This contract does not create videos, import observations, replace metric
snapshots, or copy raw media into Git.

## Implemented consumer and lifecycle

The contract is consumed by the read-only adapter, durable ignored stage, validated promotion index and compact evidence-query layer. Production plans attach source-backed Editing/Visual hypotheses for matching canonical videos. All eight MASTER tables contribute; source-declared observations never become independent channel samples or causal performance evidence.

See [workflow and provenance lifecycle](WHAT_IF_INTEGRATION_WORKFLOW.md) for validation, staging, diff review, promotion, query, update, rollback and privacy commands. Current accepted count is 8,327 rows across ten registered videos; 3,258 rows remain held across two unresolved and two unregistered sources.
