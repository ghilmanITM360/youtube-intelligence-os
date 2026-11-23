# V1 Rent segment 2 (75.0-122.3 s): on-screen facts and sources (no new narration)

Narration: Take 2 (`audio/take2/v1_rent_take2.wav`, sha256 3ef02978...c14b6e), S016-S028; the cut ends at 122.3 s, inside the silence before S029 (122.72 s, the unsupported block, not used). Timing: `audio/take2/t2_words_merged.json` (ASR, about +/-0.1 s). Build: `tools/v1r5_seg2.py`. Source on screen for every beat: "BLS factsheet: Owners' equivalent rent and rent" (https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm). Page re-read 2026-11-21 (WebFetch); quotes below are from that read.

| Beat (s) | Narration | On screen | Basis | Status |
|---|---|---|---|---|
| 79.9-84.7 | BLS does not look at every apartment; takes a sample | 12 houses, 3 turn blue, labelled 'illustration, not to scale' | "BLS data collectors visit a small number (usually 5) of renter-occupied housing units selected to represent each segment." The 3 blue houses of 12 are illustrative only and labelled so | V (concept); count illustrative |
| 84.7-87.3 | each sampled unit priced every six months | house + "price" + "every 6 months" | "collects rent data from each sampled unit every 6 months" (C-07) | V |
| 87.3-90.1 | because a lease fixes the rent for a term | LEASE paper, "fixes the rent for a term" | "Many rents change infrequently, being locked in place for a given lease term". The page links this to the 6-month interval only indirectly | V (indirect "because") |
| 90.1-93.3 | split into six groups, called panels | six boxes "Panel 1..6" | "divides each area's rent sample into six subsamples called panels" (C-08) | V |
| 93.3-99.5 | panel in January and July; next February and August | Panel 1: January, July; Panel 2: February, August; "and so on" | "panel 1 ... January and July; panel 2, in February and August, etc." (C-08) | V |
| 99.5-103.6 | every month one-sixth gets a new price | months step Jan then Feb (0.5 s each), one panel lit; "1/6" | not stated on the page; follows from six panels collected in a rotating schedule | D (derived; the months 3-6 follow the "etc." pattern) |
| 105.9-109.3 | monthly change is the sixth root of this ratio | "monthly change = sixth root of ratio" | "The sixth root of this relative is the 1-month change" (C-09) | V |
| 109.3-114.6 | today's average rent in the panel / average rent of the same units 6 months earlier | fraction | narration; the page calls it a "relative"; "same units" is the narrator's wording, not a BLS quote (QA R4v4/R5v2) | V (as narrated) |
| 114.6-118.9 | a sixth root turns a six-month change into a one-month change | 6-month change -> 1-month change | C-09 | V |
| 118.9-122.3 | monthly changes chained to build the index | Jan -> Apr chain to "the index" | "The index for period t is computed by multiplying the index for period t-1 by the relative of price change from t-1 to t." | V |

Not shown: any numeric example (no figure is in the narration), anything from 122.72 s on (C-24..C-29 unverified), the vacancy/age adjustments (S061+).
