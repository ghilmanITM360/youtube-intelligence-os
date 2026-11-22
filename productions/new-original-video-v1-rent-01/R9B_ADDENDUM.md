# R9b addendum (2026-11-21): one on-screen wording fix

R9 (`out_full/V1_RENT_FULL_R9_assembled.mp4`, sha256 ecc71a21...6144) is preserved byte-for-byte as the owner's current candidate. Its on-screen chip at 247.9-253.7 s read "moves in six-month steps", which a viewer could take to mean the whole index updates only twice a year. BLS publishes the rent index monthly; each sampled unit is priced about every six months and the monthly change is the sixth root of the six-month ratio (factsheet; see claim register C-09).

R9b changes only that beat's text (segment 5 re-rendered, same 1626 frames; segments 1-4 and 6 byte-identical copies, audio identical master v2):
- chip 1: "each home is repriced every six months"
- small note: "the index itself is published every month"
- chip 2 unchanged: "cannot tell you the dollar price of renting"
The spoken line "moves in six-month steps" is unchanged (no re-record). Audio remains a wording watch item for the owner.

Files: `out_full/V1_RENT_FULL_R9b_assembled.mp4` (sha256 5a2529d4b176c05890122a709bb88466c0a8196ad01ded703d3f15c4b71c3ce0), `out_r9b/seg5_video.mp4` (sha256 4d19497663de2eb421c2f191e41d2404b7b6941ace59b196df2977aa58dae73f), `tools/v1r9b_render_all.py`. R9b: 8482 frames, video 282.733 s, audio 282.731 s, decode clean, frames at 160 s and 163 s identical to R9.
Not publication-approved: the owner's listen to the 124 s and S090 seams and the final review are still open.
(tools/v1r9_tail.py hash updated for the R9b chip edit; R9 render used the previous version, recoverable from git d4a72761)

## Focused recheck (independent reviewer, 18 frames, no audio; I viewed chip_251.5 and chip_243.0 myself)
- Arrow scene 159.5-165.5 s: PASS. No missing glyph, drawn arrow points $1,859 to $1,913, 9s read as 9, source tags present. P3: arrow thin; slashed zero in Atkinson tags; 161.5 s blank frame is the scene transition.
- Changed beat 247.9-253.7 s: PASS. Text no longer implies a twice-a-year index. P3: the small note is borderline legible on a phone and sits close to chip 2.
- Unchanged scene at 243.0 s (232.9-243.5 beat): P3 crowding, accepted and not re-rendered: the "Zillow" label's descender sits close to the October note, "vs" touches the blue box edge, "Third" is left-offset. All text remains legible and nothing is clipped.
