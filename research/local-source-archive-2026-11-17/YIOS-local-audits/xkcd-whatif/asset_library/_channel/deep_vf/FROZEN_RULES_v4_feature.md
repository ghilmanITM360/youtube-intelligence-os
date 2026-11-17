# Frozen feature test v4 — denominators for the two UNTESTED v3 changes (LOCAL ONLY)
Frozen at the stamp in FROZEN_RULES_v4_feature.sha256, after the disclosed screen (v4_screen/SCREEN_PROTOCOL.md) and before any detailed scoring.
v9 result preserved unchanged: 9/9 scorable (9/10 with UNDEFINED), MAP_FILL and merged multi-move scroll UNTESTED. FKXV Short journey M1 stays UNDEFINED (no separate Short JOURNEY_LADDER rule frozen or tested here).

## Feature-specific denominators
- D_MAP = hold tiles, in screened-eligible Shorts, viewed and labelled MAP_FILL (saturated flat geographic fills). Grey/achromatic maps, pastel TINT maps and non-map saturated plates (sky, fire) are excluded.
- D_SCROLL = camera instances with >= 2 whole-frame moves where the viewed frames show a strip/axis/stack translating. Single moves, slide transitions between layouts and zoom+push reveals are excluded.
- Eligible Shorts: the 11 unused local Shorts (reconciled list in v4_screen/SCREEN_RESULTS.md), excluding any whose parent long is in a used set or is the parent of a v9 pick (parent repeat).
## Scoring (only if D > 0)
- MAP: C2 pass rate on D_MAP tiles (MAP_FILL condition of FROZEN_RULES_v3). Holds if 100% of D_MAP tiles pass and D_MAP comes from >= 2 independent Shorts; 1 Short = SINGLE_CASE (reported, not "validated").
- SCROLL: M1 instance share <= limit (v3) on each Short containing a D_SCROLL instance, plus raw-move share reported; same independence rule.
- D = 0 → result is COVERAGE_GAP, never a pass.
