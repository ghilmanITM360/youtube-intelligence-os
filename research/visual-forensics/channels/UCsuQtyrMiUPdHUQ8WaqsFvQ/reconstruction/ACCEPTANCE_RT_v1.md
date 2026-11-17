# Reconstruction acceptance criteria RT v1 (frozen BEFORE any render; sha256 in ACCEPTANCE_RT_v1.sha256)
Rules source: campaign/CHANNEL_PRODUCTION_MANUAL_v1.md (A table + section C) and campaign/aggregate_dev_final.json. Tests: RT_L1 (16:9) and RT_P1 (9:16). Fresh worker receives only reconstruction/<RT>/BRIEF.md + SPEC.md. Render is measured with the SAME pipeline as source videos (pe_measure -> pe_segment -> pe_palette -> pe_sheets -> pe_stroke on one native frame). A failed attempt is kept as attempt_1; fixes go to attempt_2 with the failure retained.

## Measured (deterministic, inclusive DEV range of the format)
| ID | Check | RT_L1 (LONG range) | RT_P1 (SHORT range) |
|---|---|---|---|
| C1 | 50 fps CFR; exact 1920x1080 / 1080x1920; frame count = spec | yes | yes |
| C2 | background exact modal RGB of frame 0 within #FAFAFA-#FFFFFF | yes | yes |
| C3 | median HOLD s | 0.50-1.57 | 0.89-1.34 |
| C4 | single-frame share of ACTIVITY | >=0.833 | >=0.923 |
| C5 | measured events/min | 34.1-59.7 | 35.7-47.9 |
| C6 | mean dark-ink fraction | 0.071-0.104 | 0.079-0.129 |
| C7 | holds containing yellow | 0.24-0.62 | 0.43-0.75 |
| C8 | stroke median px (pe_stroke, mascot native frame) | 10-14 | 10-20 |
| C9 | intended events matched by a measured ACTIVITY onset within +-2 frames | >=0.90 | >=0.90 |
| C10 | unexplained measured onsets / measured activities | <=0.10 | <=0.10 |

## Observed (primary reviewer opens the render contact sheets once each; judgment recorded with sheet/tile locator)
| ID | Check |
|---|---|
| V1 | ORIGINAL mascot: not a caveman, no beard, no spotted tunic, no headdress; thick even black outline; flat fills; no gradient/shadow |
| V2 | single-frame state replacement is the default visible grammar (no tweened motion other than the specified dip-to-white) |
| V3 | text built word by word on white with space reserved for the next word (>=1 instance) |
| V4 | red X negation over a subject (>=1) |
| V5 | ends on a joke state; no CTA / end card |
| V6 | layout fits format (portrait recomposed vertically, nothing cut off, text readable at sheet scale) |

PASS = all C and V checks pass. Audio/narration sync: NOT TESTABLE (silent render; listening BLOCKED_CAPABILITY) - recorded BLOCKED, not PASS.
