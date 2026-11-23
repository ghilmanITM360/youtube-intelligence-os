# V1 Rent R9 independent regression QA (2026-11-21)
Subject: `out_full/V1_RENT_FULL_R9_assembled.mp4`, sha256 `ecc71a215cf1fe70f03eeaa49b47f43e07847ff052e0124600c2a9573f4e6144` (final, after the one repair below). 1920x1080, 30 fps, 8,482 frames, video 282.733 s, audio 282.731 s (2.6 ms, under one AAC frame), full decode clean, constant frame spacing 0.0333 s (no gaps), decoded audio lag vs master v2 = 0.0 ms at 10/100/200/251/270 s.
Reviewer: separate read-only vision subagent on 163 exact-time frames (viewed about 35: every changed scene, all five joins, end frames). It cannot hear. Frames it did not view are NOT covered by that review; my own checks covered edge margins on 565 frames (2 fps, run on the pre-repair file; only the room plate at 18-22 s, which is full-bleed by design, and the "how fast" label, since moved, touched edges).

## Previous P1/P2 items: all RESOLVED (reviewer, frame evidence)
P1-2 tags (t_0193, t_0198, t_0243 and all others viewed); P2-1 quote (t_0213, t_0216); P2-2 strike (t_0147); P2-3 October wording (t_0242/0243); P2-4 descenders (t_0022, t_0034); P2-5 digit 9 (t_0156, t_0160, t_0164, t_0243, t_0055); P2-6 scale note (t_0229/0232); P2-7 BLS olive / Zillow blue; S090 summary beat (t_0250, t_0253.60) has no "matches the market" claim.
P1-1 (spoken S090): fixed in audio v2, verified numerically and by ASR word check, **human listening PENDING**.

## New defect found and fixed in this pass
- P2: "$1,859 [] $1,913" at about 160-166 s showed a hollow tofu box where the arrow character was missing from the new numeral font. Fixed by drawing a real arrow with two separate numbers; segment 4 re-rendered and reassembled; frame t_0163 checked by me (arrow, both numbers, +2.9% and tag all correct). The reviewer did not re-view this frame; my own check did.

## Joins
75, 122.3, 147.6, 199.5, 253.7 s: clean hard cuts. End frame (282.70 s): complete text, nothing cut. 124 s video seam clean (audio seam PENDING human).

## Accepted P3 (not reopened)
Slashed zero in source tags (Atkinson Hyperlegible style); Zillow label near the October note; Zillow +2.9% chip appears under 1 s after the spoken "2.9%"; Zillow figures use level/change colours (orange, red) while BLS olive vs Zillow blue holds in the charts; blank pauses between scenes (about 226 s); hand-font "g" resembles "q" in small words; pie wedge sizes; tight margins; host scale jump at 122.3 s.
Mobile legibility (reviewer, 1/3 scale): big numerals read with high confidence; two-line source tags (about 17 px at 1920 wide, 6 px at 640) and the 54 px captions are borderline on a phone. Source tags are legible on desktop/TV; this is the standing tag style, flagged for the owner.

## Not verified
Audio quality (no hearing); frames the reviewer did not open; whether the owner accepts the chart/colour conventions.
