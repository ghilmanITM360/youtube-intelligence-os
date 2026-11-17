# Cold-start retrieval test - Video 005 package (PARTIAL)

Unrelated ORIGINAL script (bread prices) was mapped using only `dna_statistics_v2.json` and the blueprint. This tests that the package yields usable guidance; it does not prove the resulting video would look good.

| Script line | Family retrieved | Median hold (s, MEASURED) |
|---|---|---|
| Bread now costs forty percent more than it did in 2021. | F6 chart/graph | 1.12 |
| Farmers are not the ones getting rich. | F2 character+prop | 0.85 |
| A single mill controls most of the flour in the region. | F3 object/icon cluster | 1.1 |
| Imagine a baker staring at an invoice and sighing. | F1 character-only | 1.21 |
| So what can a household actually do about it? | F1 character-only | 1.21 |
| Buy from local bakeries and compare unit prices. | F7 text card | 1.27 |

Planned base holds total 6.8 s for 6 lines; the blueprint adds 2-5 element entries at 0.3-1.5 s per composition and an emphasis beat (ORIGINAL_CREATIVE_INSTRUCTION).
All families resolved from the package: True. Per-state prompt template exists for all 478 states (`per_state_specs_v2.csv`); colours, typeface and easing are UNAVAILABLE, so the agent must choose original ones.
Limitation: line-to-family mapping used simple keyword rules written by me, not a validated classifier. Result: PASS for retrieval completeness only.