# VISUAL DNA

Regenerated from `01_master_data/MASTER_STATES.csv` (581 states). The prior
version of this document had a "Visual State Types" table with headers only
and zero populated rows; this version fills it with the real, computed
distribution.

## Visual Function Distribution

`VISUAL_FUNCTION` is free text per state (398 distinct values across 581 rows — most values are unique, one-off scene descriptions, not a fixed taxonomy). Top recurring values by frequency:

| Visual Function (raw text) | Count | Avg Duration (s) |
|---|---|---|
| Demonstrate rewriting through visual editing | 43 | 0.18 |
| Cut | 23 | 6.68 |
| ESCALATION | 17 | 2.70 |
| Actions-per-minute escalation | 14 | 1.47 |
| SETUP | 11 | 1.78 |
| PAYOFF | 10 | 1.88 |
| Locked | 10 | 7.25 |
| Compare typing and book-related energy | 8 | 1.67 |
| EXPLANATION | 6 | 2.08 |
| Character count of a novel | 5 | 1.16 |

These top 10 cover 147/581 states (25%); the remaining 75% are singleton or near-singleton per-video descriptions, so no corpus-wide "visual state taxonomy" beyond this is claimed.

## Camera State

| Camera state (normalized to lead token) | Count |
|---|---|
| LOCKED | 176 |
| STATIC | 105 |
| LOCKED WIDE | 70 |
| LOCKED FULL FRAME | 66 |
| STATIC, LOCKED | 48 |
| STATIC LOCKED FRAME | 47 |
| LOCKED CLOSE | 6 |
| HARD CUT | 6 |
| HOLD | 4 |
| LOCKED MEDIUM | 3 |

LOCKED-family and STATIC-family values together cover 522/581 states (89.8%) — the corpus is dominated by a fixed, non-moving camera; illustrated content changes within a static frame rather than through camera movement.

## What is NOT supported by current data

- No color palette, hue-coding, or typography measurement exists anywhere in the schema — any claim about "consistent color coding for semantic meaning" or "text hierarchy" would be unsupported and is omitted (the prior version made such claims without backing data).
- No cross-video comparison of state duration by "explanation complexity" is possible: `MASTER_STATES.csv` has no complexity/topic field to correlate against.
