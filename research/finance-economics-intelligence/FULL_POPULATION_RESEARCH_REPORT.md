# Finance and Economics: 966-video audit

Status: **FULL_POPULATION_RESEARCH_IN_PROGRESS**. Scope is all 966 canonical videos across 13 channels. The old 30-video sampling ceiling is revoked. File presence does not establish analytical completion.

The immutable universe is `audit-baseline/VIDEO_IDS.csv`; the source master is preserved byte-for-byte in `audit-baseline/VIDEO_MASTER.csv`. `MANIFEST.json` records 26 source hashes. One row per ID exists in each requested audit table. Pending rows contain identity/source/status, not invented interpretations.

The first new batch, `audit-batches/PRIMATE_001.json`, contains individual full-stored-text, actual-title, actual-image, topic and public-evidence virality readings for **all 28 Primate Economics videos**. Thirteen Shorts and fifteen long-form videos stay separate. Six of these had legacy contextual reviews; twenty-two are new to semantic coverage. All 28 actual images were inspected at 320px using four labeled contact sheets. Twenty-two images were newly fetched and six reused.

Crayon continuation adds individual title and image readings for all 30 channel IDs, with NVIDIA and Petrodollar expanded across all dimensions; 28 Crayon records remain in progress. Combined distinct coverage: 79 title readings, 54 topic readings, 76 image reviews and 41 full-stored-text readings. Expanded six-dimension rubric completion is 30, all limited evidence. Eleven transcript gaps remain blocked. Stored-text reading is not audio verification or proof the export covers the entire narration; the April 9 inflation Short ends mid-sentence. All metrics are historical snapshots.

Performance was revalidated for all 966 records under `METHODS.md`: 179 strong, 383 typical, 161 weak, 243 insufficient. This is deterministic performance review, distinct from 30 new individual virality interpretations. Five-peer sensitivity retains 598/723 labels; 125 change. Event context and Google Trends are not interchangeable: 13 shared historical context/reference records are registered, but the attempted Trends series was inaccessible and no values were inferred.

Important contrasts and editorial hypotheses are in `STRONG_TYPICAL_WEAK_COMPARISONS.md` and `VIRALITY_PATTERNS_AND_COUNTEREXAMPLES.md`. Scope limitations remain decisive: a fully interpreted channel and two additional videos are not a representative result across all thirteen. Reused Casually Finance/Casual Economics sources retain their old source register and distinct performance methods; they are not extra canonical IDs.

Rebuild with `build_audit_966.py`, validate with `validate_audit_966.py`. `VALIDATION_966.json` is the authoritative machine coverage report; the legacy `VALIDATION.json` describes only legacy tables. Research validation is explicit and separate from general repository CI.

The missing-URL acquisition pass stopped on its first metadata HTTP 429 (`-UdMJ-EtLDI`); 158 remaining requests were not attempted. No retry/bypass or permanent unavailability inference. See LEGACY_THUMBNAIL_RECOVERY_001.json.
