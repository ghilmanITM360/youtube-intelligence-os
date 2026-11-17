# WI-0081 physics / chemistry / biology audit — 2026-11-15
Rule (owner): every image, asset, animation keeps real physics; simplify art, never the science; change only the condition the script changes (here: stirring a mug of water).

## A. Script numbers (recomputed)
- 0.25 kg x 4186 J/kg.K x 80 K = 83,720 J (script "about 84,000 J") OK.  /120 s = 698 W (script 700) OK = 7 x 100 W bulbs OK; 1 hp = 746 W OK ("about one horsepower").
- Niagara: g*h/c = 9.81 x 51 / 4186 = 0.12 C OK (51 m is my figure, book gives 0.12). Assumes all fall energy becomes heat; say "at most".
- Spoon "well under 1 W" and "less than a hundredth of a bulb" consistent (1/100). Source for the wattage is the book only.
- Cavitation: bubbles form where local pressure falls below vapor pressure (about 2.3 kPa at 20 C); they are vapor, they collapse, they do not carry heat. Script wording correct. "Tens of thousands of strokes a second" is an extreme hypothetical, not a source-checked threshold (flag stays C-weak).
- Steady state "cup leaks heat as fast as spoon adds" OK (Newton cooling). Splash cools faster: larger surface + evaporation OK.
- Event 23-24 (three mugs cooling): those mugs must be HOT tea (steam, needle starting high), not the 20 C water of shot 1. Dip a hair faster is the book's claim only; keep "illustrative".

## B. Asset verdicts (viewed at zoom)
OK: MUG-01/02 (handle, rim, base), JUG-01 (spout opposite handle, flat level), WTR-02 (rim-high, centre-low vortex), WTR-03 (central dip = correct vortex surface), MWV-01 (mug inside on turntable, no metal, steam from hot mug), THM-03 (probe in liquid, cable over rim), CAV-02 (bubbles on the trailing side, speed lines behind), CAV-03 (bubbles rise from bottom, flame under pot), SPN-05 (spoon rests on rim, bowl submerged), WTR-04 (droplets leave the surface on arcs).
FIX (regenerate by Codex):
1. NIA-02 waterfall: bottom ends in icicle-like drips = looks frozen. Water at the base must end in a straight cut hidden by spray (NIA-04) or fan into mist.
2. HRS-01 horse: legs are straight pipes with no knee/hock; add joints, 4 legs clearly distinct, hooves.
3. CLK-01: shaded wedge = 120 deg only fits a 6-minute face; for "2 min" on a 60-minute face the wedge is 12 deg. Redraw as a thin 12 deg wedge.
4. CAV-03: flame floating under the pot; add a small burner ring so the flame has fuel and the pot has support.
5. THM-01/02: sweep ~270 deg with a gap at the bottom (real dial gauge), needle clockwise with rising temperature; needle drawn by code from 20 C to 100 C.
Keep as code job: SUG cubes must start IN the water, sink, dissolve (sugar is denser than water); steam/heat marks go up only from hot water; frame 1 water (20 C) has NO steam.

## C. Draft-shot errors (compositor, mine to fix; none is a Codex issue)
- S01,S03,S05,S16,S19,S20,S27: mug floats about 30 px above the table top -> mug base must sit ON the table line (support).
- Torso/legs drawn over the table top: alien stands behind the table -> table top must occlude the legs, or place the table beside him.
- S16,S19,S20,S23: grey water band (WTR-03) extends beyond the mug walls -> liquid outside the container. Clip all water to the mug interior (MSK-01 is empty: rebuild it from MUG-01 interior).
- S22: pot, flame and the cavitation slab float in mid air; slab has no container. Put pot on a burner, put cavitation inside the mug cross-section.
- S23: hot mug hovers at head height above another mug; red heat squiggles are drawn through the mug. Three mugs sit on the table in a row.
- S14: waterfall column must reach the pool (draft stops short); a cup at the foot must be tiny next to 51 m.
- Text overlap in S19/S20/S22 and stray "W" on shots without the ruler.
- Floor line in all table shots: remove (spec: no floor line) or keep one global ground line; decide once. Recommendation: no floor line, table legs end at the plate bottom.
- Scale: mug is about 1/6 of the alien height (cartoon scale). Allowed as xkcd-style prop enlargement; keep it identical in all shots.

## D. Motion physics (animations, my code)
- Spoon: constant-speed circular stir at the mug (speed lines trail behind), no overshoot. Vortex dip follows the spoon.
- Droplets (S23): parabolic arcs, accelerate downward at constant g, land on the table not through it.
- Needle: rises a hair then holds (steady state), thermometer needle clockwise.
- Cavitation bubbles: appear behind the blade, collapse within a few frames, do not rise like boiling.
- Waterfall: streaks fall straight down, spray at the base.
- Hot-mug cooling: needle falls fast at first then slower (exponential), three needles nearly same.
- Pop-in assets stay a house style (1-frame), but never a prop appearing without support.
