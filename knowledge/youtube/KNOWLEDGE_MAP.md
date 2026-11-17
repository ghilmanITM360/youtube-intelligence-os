# Knowledge map

Evidence flows from original source → extracted claim/measurement → dated validation → niche-specific hypothesis → later owner experiment. A later summary does not create another observation.

| Layer | Locator | Allowed reuse |
|---|---|---|
| Original training | DS-000011, DS-000018, DS-000031 manifests in [master index](MASTER_INDEX.md) | Frameworks and attributed opinions |
| Platform rules | Links in topic documents, checked 2026-10-15 | Official stated behavior, within its scope |
| Channel identity/data | [Registry counts](REGISTRY_COUNTS.json), `data/catalog/youtube_channel_registry.db` | Exact identities and saved metadata; no live-performance assumption |
| Historical catalog | `data/catalog/youtube_inventory.db` | Older ingestion/provenance records; do not sum with registry |
| Forensic research | [Branch source index](BRANCH_SOURCE_INDEX.csv) | Source-backed observations with original QA limits |
| Production | Branch source index / local outputs | Examples and design decisions; not proof of audience response |
| Future analysis | [Preflight](RESEARCH_PREFLIGHT.md) | Explicit hypotheses and missing-data requests |

Finance, health, history and other niches share the methods. They do not share inferred audience behavior or performance baselines automatically. Source: [provenance contract](../../docs/PROVENANCE.md) and [cross-niche calibration](../../data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json).
