# Narration edit decision sheet: Take 2, block 122.72-255.14 s (DECISION REQUIRED, NOT APPLIED)
Date 2026-11-21. Master `audio/take2/v1_rent_take2.wav` sha256 3ef02978...c14b6e is untouched (re-hashed after this work, unchanged). Nothing below is the narration master until the owner approves. Sentence ids and times are from `audio/take2/t2_sentences_timed.tsv` (ASR, about +/-0.1 s). The dossier's old S-numbers belong to Take 1 and are not used here.

## 1. What the proposed cut removes
Cut 124.00 s to 254.80 s (130.80 s, 344 words), both ends inside measured silence (-70 dB or lower; see 4). It removes sentences S030-S060 (31 sentences). "Two more details." (S029, 122.72-123.56 s) is kept: it is the approved script's own lead-in.

| Removed sentences (time) | Content | Status against our evidence |
|---|---|---|
| S030-S031 (124.5-137.4) | "In July 2024 a new rule started adjusting the mix..." and "new construction and old buildings falling out of use can add small monthly shifts of half a percent or less" | Not in the approved script. Not in our claim register, no source read. Unverified. |
| S032-S038 (138.4-158.6) | Zillow series "in September 2024 it was $2,157", "twelve months before, $2,101", "increase of 2.7%" | Not in the approved script. The dollar figures have no source in the register (our Zillow figures are Oct 2026 $1,913 and Sep 2026 +2.7%). Dates and levels conflict with the verified record. Do not show. |
| S039-S046 (164.8-197.3) | "when you hear rent about 3%, this is what it means... speed rather than distance... level vs change... slower than when" | Concept already in the approved script (level vs change, Zillow section). Duplicate wording, no new number; not itself a factual claim, but it repeats a later section. |
| S047-S052 (198.2-224.3) | "We looked for evidence that the measures are intentionally understated... independent academic teams check the data... Zillow matches BLS very closely over many years... BLS explicitly accounts for short-term lease renewals" | No source in the register for any of the four claims. The approved script says the opposite stance ("we did not find a BLS sentence that says rent trails"). Unsupported; the BLS-accounts-for-lease-renewals claim still needs a source check before any reuse. |
| S053-S060 (225.3-254.6) | A premature conclusion, a three-question rule list, "describes the market not your lease", "not individual legal advice" | Duplicates lines that the approved script delivers later (rule questions, disclaimer). A conclusion 4 min into a 7 min video. |

## 2. What verified narration remains
0-123.56 s (S001-S029): approved wording, already built in R4 v4 and R5 v2 (to 122.3 s). After the seam: S061 onward, the approved vacancy and age-adjustment lines, "fixed set of homes observed at six month steps", the Zillow October section, "What we checked", close and disclaimer. TAKE2_CHECK records those as matching the approved script. This was not re-diffed word by word here (780 kept words against about 802 in the approved extract; the difference is minor wording).

## 3. Resulting version
- Duration 416.88 s -> 286.08 s (4:46).
- Seam: "...Two more details." then 0.78 s of silence, then "If a unit is vacant when the BLS checks it..." This is exactly the approved script's order ("Two more details. If a unit is vacant...").
- Unnatural transition? Not on the evidence: the lead-in matches the following sentence in meaning, the pause length is typical (sentence gaps in this recording are 0.5-1.0 s), and the splice is inside silence with a 20 ms crossfade. Listen to `audio/take2_proposed_cut/SEAM_PREVIEW_118-132s_NOT_MASTER.wav` (118-132 s of the result, not a master) before deciding; I have not had a human listen.
- Bridge recording needed? No. No new sentence is created. A re-record is only needed if you want the removed ideas (July 2024 rule, Zillow Sep 2024 series, short-term-lease claim) in the video; each would first need a source.

## 4. Edit specification
| Item | Value |
|---|---|
| Keep A | 0.00-124.00 s (ends 0.44 s after "details", silence -74 dB) |
| Remove | 124.00-254.80 s |
| Keep B | 254.80 s to end (starts 0.34 s before "If", silence -67 dB) |
| Crossfade | 20 ms in silence |
| Remap rule | t_new = t for t <= 124.00; t_new = t - 130.80 for t >= 254.80 |
| Words | 1124 -> 780 kept, 344 dropped (first dropped "In" 124.48, last "say." 254.58) |
| Frozen video | R4 v4 (0-75 s) and R5 v2 (75-122.3 s) are unaffected: everything before 124.00 s keeps its timestamps |
| Needs remapping | every word time at or after 254.80 s in `t2_words_merged.json` (S061 -> 124.34 s onward); every claim-register row and storyboard beat for later segments; the vacancy beat that was prepared for 255.14-265.0 s becomes 124.34-134.2 s |
Proposed remapped word file (preview only, not applied): `audio/take2_proposed_cut/PROPOSED_words_remapped_NOT_APPLIED.json`.

## 5. Options for the owner
1. Approve the cut (recommended by the evidence: no new sentence, no bridge, resolves the unsupported claims). I then produce a new master file next to the original, with a recorded checksum, and rebuild later segments against it.
2. Re-record the block with sourced content (needs the July 2024 and Zillow claims verified first).
3. Keep Take 2 as is: not recommended; it would present unsourced figures.
Until you choose, no later segment is built on the post-block audio.
