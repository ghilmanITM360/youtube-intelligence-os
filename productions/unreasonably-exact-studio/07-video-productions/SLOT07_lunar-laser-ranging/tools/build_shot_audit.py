"""Writes SHOT_BY_SHOT_VISUAL_EXPLANATION_AUDIT.csv: one row per narration beat (V2), what the ROUGH CUT V1 actually shows.
Rows are Claude's review of rendered frames (stills + filmstrips), not a viewer test."""
import csv, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
beats = list(csv.DictReader(open(os.path.join(ROOT, 'narration/NARRATION_BEAT_MAP.csv'))))
# beat: (viewer understanding, visible subject, action, camera, science relation, payoff, misconception risk, correction needed ('' = none), source)
A = {
'B01': ('A laser is about to be aimed at the Moon from an observatory', 'dome + Moon in one frame from frame 0', 'slit opens, telescope rises toward the Moon', 'locked wide, eased tilt/push landing on "moon."', 'same telescope will send and receive', 'telescope settles pointed at the Moon on "moon."', 'viewer may expect a visible beam', '', 'P03'),
'B02': ('Lighting the Moon up is the WRONG idea', 'floodlight cone + washed-out Moon', 'cone appears, red NO mark, cone collapses', 'hold', 'shows what is NOT done (no beam is drawn later)', 'cone collapses on "up."', 'cone could be read as the real beam', 'none: NO mark + collapse; mute-test it with a viewer', 'P03'),
'B03': ('The laser is a question (a measurement), aimed precisely', 'reticle brackets on the Moon, dashed aim guide', 'brackets converge and lock with a flash on "question."', 'slow drift', 'aiming = measurement intent', 'lock flash on "question."', 'reticle could read as a weapon HUD', '', 'P03'),
'B04': ('One short pulse is fired', 'muzzle ping + single dot at the aperture', 'pulse leaves', 'slow drift', 'pulse, not a beam; drawn as a dot', 'ping on "fire"', 'dot size implies scale', 'badge PULSE DRAWN AS A DOT', 'P03'),
'B05': ('The target is a reflector on the Moon\'s surface', 'pulse reaches the Moon (real time 1.28 s); Moon close-up with Apollo 11 site ring', 'push into the Moon, ring pings on "lunar"', 'match-push from the wide Moon to a close-up', 'reflector site is real (C05); hardware revealed later', 'ring on "lunar surface"', 'ring may look like the hardware', '', 'P03 + G05'),
'B06': ('We time how long the light takes to come home', 'stopwatch at 0.00 with the Earth-Moon schematic', 'stopwatch fades in', 'static schematic', 'timing starts at launch', 'stopwatch ready on "how long"', '', '', 'P11'),
'B07': ('Round trip = about 2.5 s', 'stopwatch runs to 2.56', 'dial sweeps', 'static', 'C01 2.56 s', 'stops on "seconds."', '', '', 'P11'),
'B08': ('That 2.56 s is there AND back', 'out lane (warm) and return lane (cool)', 'two lanes drawn', 'static', 'two legs', 'lanes split on "there and back"', '', '', 'P08'),
'B09': ('Not 2.5 s each way', 'arc on the dial splits in two colours', 'split', 'static', 'each leg ~1.28 s (C02)', 'split on "each way."', '', '', 'P08'),
'B10': ('Outbound takes a little over a second', 'warm pulse climbs, dial half', 'pulse travels (slow-motion badge)', 'static', 'C02 1.28 s', 'arrives on "moon"', 'slow motion vs real time', 'SLOW-MOTION badge present', 'P08'),
'B11': ('Return takes the same again', 'cool pulse descends', 'pulse returns', 'static', 'C02', 'arrives home on "return."', '', '', 'P08'),
'B12': ('The Moon\'s distance changes', 'Moon moves along the path, ruler with km labels', 'Moon swings to 357,000 then 407,000 km', 'static', 'C03, TO SCALE on the schematic (ratio 1.14)', 'ruler label changes', 'motion speed is not real (27.5 d cycle)', 'add "CYCLE: ~27 DAYS" badge? (decide in review)', 'G12'),
'B13': ('So the travel time changes too', 'stopwatch reading follows the distance', '2.38 <-> 2.71 s', 'static', 'C04', 'reading moves with the Moon', '', '', 'G12'),
'B14': ('Pause: a new question', 'everything stops, veil dims', 'freeze', 'tiny settle', '-', 'freeze on "hold"', '', '', 'G12'),
'B15': ('Why would light return at all?', 'a pulse hits bare ground and scatters everywhere', 'diffuse spray', 'static', 'ordinary surfaces scatter light in all directions', 'spray on impact', 'scatter dots small at phone size', 'enlarge scatter in V2', 'G12'),
'B16': ('Maybe a mirror is up there?', 'imagined dashed mirror + "?" on the near side', 'mirror draws, camera pushes in', 'push to the Moon', 'C12: imagined, dashed', '"?" on "mirror"', 'dashed mirror could be taken as real', '', 'G12'),
'B17': ('Yes: real equipment exists', 'ghost mirror replaced by the real array', 'array pops in', 'pull back over lunar ground', 'C05', 'array on "yes."', '', '', 'P13'),
'B18': ('Apollo astronauts left special reflectors', 'array on the lunar surface, dust settle', 'settle + ballistic dust', 'pull back, parallax', 'C05', 'settle on "left"', 'astronaut absent in the cut (P06 exists but is not cut in)', 'cut P06 into B18 in V2', 'P13'),
'B19': ('The corners are the trick', 'push into one corner cube -> cutaway', 'push + match dissolve', 'push (rack focus during the fast part)', 'corner cube geometry', 'dissolve on "trick."', 'strobe in push', 'smoothstep + longer push + rack focus applied', 'P13'),
'B20': ('They send a tiny fraction back', 'rays enter/reflect; footprint inset (C06 rule)', 'rays', 'static cutaway', 'C06', 'inset on "tiny fraction"', 'dense frame', 'consider spreading over B19-B21 (brief item 16)', 'P13'),
'B21': ('Back toward where it came from', 'exit rays antiparallel to entry', 'rays exit', 'static', 'retroreflection', 'exit on "from."', '', '', 'P13'),
'B22': ('We are back at the observatory', 'same dome framing as the opening', 'cut back', 'wide', 'same instrument receives', 'match to opening composition', '', '', 'G22'),
'B23': ('The telescope waits for the return', 'cool pulse descends into the slit (real time)', 'arrival ping at the aperture', 'wide', 'C02 down-leg', 'ping on "return."', '', '', 'G22'),
'B24': ('Something strange is coming', 'push toward the dome', 'anticipation push', 'push', '-', '-', 'push without content', 'add detector glow tease in V2', 'G22'),
'B25': ('Almost none of the light gets back', 'return cone far wider than the telescope; only a tiny disc kept', 'cone widens, aperture glows', 'eased push', 'C07 (no numbers)', 'tiny disc glows', 'cone width not to scale', 'badge WIDTHS NOT TO SCALE', 'G22'),
'B26': ('Only a few photons are collected', 'detector with sparse detections', 'markers', 'static', 'C08', 'markers', '', '', 'P09'),
'B27': ('From many pulses', 'histogram accumulates', 'counts rise', 'static', 'C08', 'peak emerges', '', '', 'P10'),
'B28': ('A few photons', 'individual detections', 'markers', 'static', 'C08', '', '', '', 'P10'),
'B29': ('Atmosphere is accounted for', 'P10 content (no explicit atmosphere layer)', '-', '-', 'C09', '-', 'atmosphere not shown', 'build atmosphere delay tick (C09 rule) in V2', 'P10'),
'B29b': ('Faint returns give the distance', 'histogram peak', 'peak locks', 'static', 'C10', 'peak', '', '', 'P10'),
'B30': ('Precision is about a millimetre', 'mm ruler + caliper closing to 1 mm', 'caliper closes', 'static', 'C10 (one figure allowed)', '"about 1 millimetre" on "precision."', 'scale jump from 384,000 km to 1 mm', '', 'G30'),
'B31': ('Now the method', 'schematic assembles', 'fade in', 'static', '-', '-', '', '', 'G30'),
'B32': ('A cosmic stopwatch', 'stopwatch sweeps to 2.56 and freezes', 'sweep + stop pop', 'static', 'C01', 'freeze on "stopwatch."', '', '', 'G30'),
'B33': ('Take the round-trip time', 'reading becomes a token', 'token moves', 'static', 'C11', '', '', '', 'P12'),
'B34': ('Multiply by c = total path', 'c x t, bar grows to 2D', 'bar grows', 'static', 'C11', '', '', '', 'P12'),
'B35': ('Divide by two', 'bar folds in half onto the Earth-Moon line', 'fold', 'static', 'C11', 'fold on "two."', '', '', 'P12'),
'B36': ('That is the distance', 'half bar = Earth-Moon distance', 'lands', 'static', 'C11', 'lands on "distance."', '', '', 'P12'),
'B37': ('The Moon moves', 'pull back to the orbit; Moon travels', 'pull back', 'pull back', 'illustrative orbit (badge)', '-', 'orbit shape/speed', 'badge ORBIT AND SPEED ILLUSTRATIVE', 'G37'),
'B38': ('Each return is one measurement', 'pulses to the Moon drop points on its path', 'points accumulate', 'static', 'LLR maps the orbit', 'points', 'dots small at phone size', 'enlarge in V2', 'G37'),
'B39': ('So we know where it is', 'reticle from the opening locks on the Moon', 'lock flash', 'static, fade to black', 'bookend', 'lock on "where it is."', '', '', 'G37'),
}
out = os.path.join(ROOT, 'SHOT_BY_SHOT_VISUAL_EXPLANATION_AUDIT.csv')
cols = ['beat', 'spoken_phrase', 'start_s', 'anchor_word', 'intended_viewer_understanding', 'visible_subject', 'required_action', 'camera', 'scientific_relationship',
        'timing_anchor', 'visual_payoff', 'potential_misconception', 'required_correction', 'rough_cut_source', 'review_method']
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(cols)
    for b in beats:
        u, vis, act, cam, sci, pay, mis, cor, src = A[b['id']]
        w.writerow([b['id'], b['spoken_text'], b['start_s'], b['anchor_word'] + ' @' + b['anchor_s'], u, vis, act, cam, sci, b['anchor_s'], pay, mis, cor, src,
                    'Claude: rendered stills + 12-frame filmstrips + frame-difference curve; NOT real-time viewing; NOT a viewer test'])
print('wrote', out, len(beats), 'rows')
