"""Writes review_sample/REVIEWED_SAMPLE.csv from SAMPLE.csv + my manual coding (stills: before/keyframe/after) and prints tallies."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = R + '/review_sample'
T, F = 'TRUE_CUT', 'FALSE_PROGRESSIVE'
# n: (boundary, subject, setting, framing, graphics_text, narrative_function, note)
C = {
1: (T, 'committee of figures at a long desk with speech bubbles', 'white, meeting-room desk', 'full-frame flat line drawing, wide', 'speech bubbles (3 short exclamations)', 'GAG', 'before: presenter at board with question card'),
2: (T, 'sun icon with duration label above a figure at a desk', 'white', 'full-frame, figure bottom-centre, icon top-left', '"6 MONTHS"', 'QUANTITY', 'before: dark photo-style render of sun and Earth (style change)'),
3: (T, 'horseshoe magnet, wire and meter', 'white', 'full-frame diagram, object centre-right', 'N / S pole letters', 'EXPLAIN_MECH', 'before: dark field-line diagram with a year label'),
4: (T, 'molasses tank beside an elevated train, street figures, car', 'white, city street', 'wide strip, art band across full width', '"1919, BOSTON", "MOLASSES", "15m"', 'CONTEXT_EVENT', 'tank intact then bursting inside the shot (state swap); before: flash-forward wave mound scene'),
5: (T, 'tall stack of paper with a hanging sign, two figures', 'white', 'full-frame, figures lower-left, stack right', 'sign text, red "300 m3"', 'QUANTITY_SCALEREF', 'figures rescaled versus before, so a cut not an add-on'),
6: (T, 'grid of twelve seated diners at tables with covered plates', 'white, repeated tables', 'full-frame tiled', 'none', 'GAG_QUANTITY', 'before: single diner with a short exclamation'),
7: (T, 'explosion cloud over a water tank, then an empty box', 'white', 'full-frame, object lower-centre', 'red "2.6 MJ/L", then "1 LITER"', 'QUANTITY', 'two label states inside the shot; before: two figures in dialogue'),
8: (T, 'black space with small black hole, then debris and planets flying', 'black background, white line art', 'full-frame', 'red "DARK ENERGY" with question marks', 'EXPLAIN_COSMIC', 'before: white scene (wave, car, tilted house)'),
9: (T, 'grey map of a coastline with a figure in the foreground', 'grey map, white figure', 'full-frame, figure lower-left', 'red place-name callout with circle', 'MAP', 'before: chalkboard with lightning and a figure'),
10: (T, 'figure at a sink with pipework, faucet burst mark', 'white, bathroom sink', 'full-frame, figure right', '"CLUNK"', 'EXPLAIN_MECH', 'before: three glasses with a time stamp and a splash'),
11: (F, 'eye beside a monitor, then an equals sign and a bracket with a second eye', 'black background, white line art', 'full-frame', '"1 NANOSECOND"', 'COMPARISON_QUANTITY', 'monitor stays in the same place; new elements arrive on the same scene, so not a hard cut'),
12: (T, 'world map with grey seas, red dots and a red circle on one island group', 'grey and white map', 'full-frame map, 41 s shot', '"-200 m" then "-1000 m", "DRAIN" dots, place callout', 'MAP_AXIS', 'many label states inside one long shot; before: black cliff silhouette with a water line'),
13: (T, 'three plates (bacon, toast, salad) in a column', 'white', 'portrait, full-frame stack', '"PART OF THIS COMPLETE BREAKFAST" x3 (later removed)', 'GAG_LIST', 'before: liver versus steak comparison table with ticks'),
14: (T, 'poster of a rocket with labelled parts and two talking figures', 'white', 'portrait, poster top, figures below', 'part labels (astronauts, pool water, fuel)', 'EXPLAIN_SETUP', 'before: black scene with a water-park slide and sign'),
15: (T, 'figure with six arrows in the directions of acceleration', 'white', 'portrait, centred', '"UPWARD / FORWARD / BACKWARD / DOWNWARD"', 'EXPLAIN_MECH', 'before: large oval track with limit label; after: small track with speed graph'),
16: (T, 'film strip with a tilted boat silhouette on a skyline', 'white, film perforations top and bottom', 'portrait, art in a middle band', 'none', 'GAG_CULTURAL_REF', 'before: colour continental map with inset'),
17: (T, 'three stacked image tiles added together', 'white', 'portrait, vertical stack', '"PROBLEM: RESOLUTION", "PROBLEM: MOTION", "BIGGER PROBLEM"', 'EXPLAIN_EQUATION', 'before: blurred motion streaks (photographic)'),
18: (T, 'figure in an inflatable ring before a safety sign', 'white', 'portrait, figure lower, sign above', '"SWIM SAFE!" with "- NO DIVING"', 'GAG_RESULT', 'before: grey scene of a diver with ripples'),
19: (T, 'tilted houses on a slope with wind lines', 'white and grey ground', 'portrait, art band centre', 'none', 'CONTEXT_SCENARIO', 'before: black ground silhouette with debris in the sky'),
20: (T, 'small hose machine inside a large dome of concentric circles', 'grey background', 'portrait, centred', 'none', 'UNCLEAR', 'meaning not clear from stills; before: same machine on white'),
21: (T, 'two-panel split screen: desk with a window, then a lower desk scene', 'grey and white panels', 'portrait, two stacked panels', 'none', 'CONTEXT_SPLIT', 'before: text card "EASIER TRADE"'),
22: (T, 'orbit diagrams of a moon and a black-hole moon, then a title card', 'white', 'portrait, diagrams stacked', '"MOON", "BLACK HOLE MOON"', 'COMPARISON', 'before: blackboard with two sun images and a figure'),
23: (F, 'search-box mock with a formula and a red result', 'white, brand UI of a third party', 'portrait, UI across middle', '"2.6 MJ/L * 0.5 in/h", red "9.17 kW/m2", vendor logo', 'QUANTITY_EQUATION', 'tank diagrams and labels stay in place, the search UI is added; third-party logo on screen'),
24: (T, 'black space with sun, half-lit Earth and a small moon', 'black background', 'portrait', 'none', 'CONTEXT_COSMIC', 'before: world map with clouds'),
}
rows = []
for r in csv.DictReader(open(O + '/SAMPLE.csv')):
    c = C[int(r['n'])]
    rows.append(dict(r, boundary_check=c[0], subject=c[1], setting=c[2], framing=c[3],
                     camera_motion='NOT_ASSESSED_STILLS', graphics_text=c[4], narrative_function=c[5], note=c[6],
                     interpretation_status='VIEWED_SELF_REVIEW_3_STILLS'))
w = csv.DictWriter(open(O + '/REVIEWED_SAMPLE.csv', 'w', newline=''), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(rows)
n = len(rows); t = sum(r['boundary_check'] == T for r in rows)
print('boundary true', t, '/', n)
for f in ('LONG', 'SHORT'):
    s = [r for r in rows if r['fmt'] == f]; print(f, sum(r['boundary_check'] == T for r in s), '/', len(s))
print('false strengths', [r['boundary_strength'] for r in rows if r['boundary_check'] == F])
print('true strengths sorted', sorted(float(r['boundary_strength']) for r in rows if r['boundary_check'] == T)[:6])
