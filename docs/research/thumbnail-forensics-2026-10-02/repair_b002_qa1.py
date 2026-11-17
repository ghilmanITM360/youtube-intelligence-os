"""QA round 1 (B002-01..03) repairs: field edits for every row the independent reviewers flagged (reviews in qa-review-B002-0N.json)."""
import json
EDITS = {
 ('01', 1): dict(arrow_present='Y'),
 ('01', 13): dict(mechanism_secondary='contradiction (the stick figure is the tallest element and the fleeing group includes deer and a rabbit, not only predators)',
                  typography='Three words in yellow outlined caps across the top, with a black outline against the green/blue; legible at 160x90 even from a 360x202 source. The question is voiced from the human side ("US"), so it restates the title question rather than speaking for the animals.',
                  partnership='Title asks why animals fear humans so much; the thumbnail answers visually with a symmetrical flight scene and the text "RUN FROM US?", complementing the title with the animals\' reaction seen from the human side but offering no cause.'),
 ('01', 24): dict(mechanism_primary='curiosity',
                  typography='Four words in white and green bold caps with two emojis inside a dark rounded box; the box spans about 69% of the centre strip (about 22% of the full frame width), so the small type is unreadable at 160x90. The caption states the result of the test, not the 10-second test from the title.',
                  mechanism='Outcome label on a stock-style portrait: a reassuring healthy-senior image and pass-style wording (GOOD BALANCE, STRONG LEGS) hint at a quick balance check, but the test itself is not depicted.',
                  composition='A vertical portrait with the face roughly centred in the strip and the caption box directly under the chin across the upper chest as a secondary focal point; the side bars are filler. Negative space is limited to a blurred bokeh background.'),
 ('02', 7): dict(warning_color_used='Y', psychology='The smug, relaxed pose reads as confidence rather than anxiety. The red alarm clock adds a time-pressure cue, but the cartoon\'s calm face softens it.',
                 typography='Three words: ALMOST AT in large bold black caps, about 60% of the height of the giant $1,000,000 beneath it, tightly set. Contrast on white is maximal and the number reads at 160x90. The title adds the one-third math and the surprising angle that the thumbnail leaves out.'),
 ('02', 9): dict(colors='Warm tan background and grey slab with a yellow headline as the only saturated colour. The tiny town with red roofs on a green circular base is the one colourful accent among beige slots, which draws attention to the lone survivor.',
                 mobile_readability_160='PARTIAL', mobile_readability_score=6,
                 weakness='The town icon that carries the concept shrinks to a few pixels at 160x90; the slab has six recesses (one filled, five empty), so the counting cue is clear only on a larger view.'),
 ('02', 23): dict(scene='A shaggy-haired caveman stick figure with wide eyes and a small open mouth stands at the left with an open black hand pressed flat against the left of two rocks side by side in the centre, with yellow curved sound-wave arcs radiating on both sides and small impact ticks above the rocks. The setting is a flat brown desert with pale hills and a sky-blue background.',
                 mechanism='Visible sound waves around two struck rocks turn the abstract origin-of-music question into a literal first-note moment.', hero_object='two rocks with sound arcs', face_scale='LARGE',
                 counterexample='Seq 12 centres a tiger as the large subject with only a medium-sized face and no explanatory graphic.',
                 typography='Two words in huge yellow outlined capitals fill the top band; the type is very large and highly legible at 160x90. The title adds the idea that humans accidentally invented music, absent from the thumbnail.'),
 ('02', 14): dict(psychology='Sweat, wide eyes and an open mouth signal anxiety. Tightly clutching the money bag adds a fear-of-losing cue.',
                  art='Clean vector illustration with uniform line weight; the grey-bearded character is drawn coherently. The hands gripping the case and the sweat drop are coherent, and nothing is cut off, so it is crisp on mobile.',
                  title_partnership_score=9, score_100=None),
 ('02', 3): dict(title_relation='COMPLEMENTS', art='Screenshot-style composition from a recorded call with rounded-corner tiles on a flat fill. Lighting and framing differ between the two webcams, which is natural for a call and not an editing artefact.'),
 ('02', 19): dict(psychology='The builder\'s focused frown signals competence while the hard-hatted worker\'s wide-eyed worry signals alarm. The crack adds a failure cue that quietly flatters the ancient method.',
                  mechanism='An ancient builder succeeding in the water next to a cracked block suggests a lost technique, framing the content as a hidden-knowledge reveal.'),
 ('03', 22): dict(title_relation='COMPLEMENTS', mechanism_secondary='',
                  partnership='Title \'This 1 Normal Symptom Means Your Heart Is Failing #heartdisease #danger #shorts\' makes a strong fear claim; the thumbnail shows a mid-sentence caption about persistent fatigue at rest, the same topic, but it does not back the title\'s urgency.'),
 ('03', 24): dict(scene='A grocery checkout scene: a figure in a navy cap and grey hoodie with a drawn smiling face (eyebrows, dot eyes) presses a finger to his lips in a shushing gesture and holds an open brown wallet at the counter; a phone with a teal glow and green chart sits on the counter beside coins. Beside him a woman in a green top who points, a man in a red jacket covering his mouth and a woman in a blue hoodie laugh; a smiling cashier in a blue uniform stands at left. Lane sign \'6\' and an EXPRESS sign appear in the background.',
                  composition='The shushing figure sits at centre-left as the focal point; the three laughing bystanders form a cluster beside and to the right of him, the cashier a smaller group at left, and the phone-and-coins at lower left of centre beside the counter form a small third focal point. Perspective lines of the counter lead inwards. The whole frame is full with no blank space.',
                  action='Hypothesis: shrink the background lane/EXPRESS signs and add a big \'NEVER TELL\' overlay over the ceiling band to test whether a text anchor sharpens the hook at 160px.', face_scale='MEDIUM'),
 ('03', 3): dict(psychology='The furrowed brows, wide round open eyes and downturned mouth read as a scowl, grumpy or suspicious rather than relaxed, which conflicts with the effortless-wealth idea in the headline and arm-chair pose.', expression_label='scowl, wide eyes, furrowed brows'),
 ('03', 4): dict(art_style='STICK_FIGURE', typography='25 words of small serif text in a card, regular weight and black on light grey, far too small to read at 160x90; the card is an unreadable grey box and the bold byline is not distinguishable. The text does not duplicate the title and carries the whole question.',
                 psychology='The line-drawn figure sipping coffee is neutral; no face detail, no fear or authority cues.'),
 ('03', 21): dict(psychology='The left ape\'s grimace and sweat drops show strain and struggle; the right ape\'s small smile and relaxed muscular stance show ease and confidence. It sets up aspiration through contrast.', before_after='N',
                  mechanism='A wrong-versus-right split (not a true before/after): strained running is crossed out while calm walking gets a tick. It communicates a better method visually in one glance, without text.'),
 ('03', 16): dict(title_relation='COMPLEMENTS',
                  partnership='Title \'Why Everything Changes After You Lose Your Job In 2026\' is about personal job loss; the thumbnail shares the job-loss theme but reframes it with a macro declining job-openings graph, and the headline \'IT\'S HAPPENING...\' adds urgency the title lacks (debatable escalation).'),
}
for b in ('01', '02', '03'):
    p = f'audit-batch-B002-{b}.json'
    rows = json.load(open(p))
    for r in rows:
        e = EDITS.get((b, r['seq']))
        if not e: continue
        for k, v in e.items():
            if k == 'score_100': continue
            assert k in r, (b, r['seq'], k)
            r[k] = v
        r['score_100'] = sum(r[k] for k in ('story_score', 'psychological_hook_score', 'title_partnership_score', 'hierarchy_score', 'mobile_readability_score', 'composition_score', 'emotion_subject_alignment_score', 'credibility_score', 'distinctiveness_score'))
        r['qa_status'] = 'QA1_REPAIRED_REVIEWED_ROW'
    for r in rows: r.setdefault('qa_status', 'QA1_SAMPLED_PASS' if r['Thumbnail_ID'] in json.load(open('qa-selection-B002-01+B002-02+B002-03.json'))[f'B002-{b}'] else 'NOT_SAMPLED')
    json.dump(rows, open(p, 'w'), indent=1)
print('repaired')
