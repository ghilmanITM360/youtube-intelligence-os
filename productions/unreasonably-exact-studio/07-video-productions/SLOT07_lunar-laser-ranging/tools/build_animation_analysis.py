"""Build ANIMATION_REFERENCE_ANALYSIS.md from research/ANIMATION_EXAMPLES.csv (+ the hand-written browser reviews).
Review modes are printed exactly as recorded; nothing is upgraded.  python3 tools/build_animation_analysis.py"""
import csv, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'research', 'ANIMATION_EXAMPLES.csv'))))
    modes = collections.Counter(r['review_mode'] for r in rows)
    L = ['# Animation reference analysis: Slot 07 (GENERATED; browser reviews are hand-written in research/video_analysis/BROWSER_REVIEWS.md)\n',
         '## How to read the review modes',
         '- **WATCHED**: played in a real player and observed (only the entries in `research/video_analysis/BROWSER_REVIEWS.md`, and even those are *seek-sampled*, never end to end, and silent: no audio was heard).',
         '- **FRAME_SAMPLED**: a public-domain video was downloaded, frames were extracted with ffmpeg at the timestamps shown and each frame was opened and looked at. Not "watched": motion and timing between frames are not judged.',
         '- **METADATA_ONLY**: only the page, title, description or transcript was read. These entries are *leads*, not evidence of technique; the "technique" text is what the page says or what the researcher infers, and must be verified before it drives a design decision.\n',
         'Counts: %s  (total %d)\n' % (dict(modes), len(rows)),
         'Browser reviews (played / seek-sampled with screenshots): `research/video_analysis/BROWSER_REVIEWS.md` (BR-01 Smarter Every Day 73 corner-reflector chapter; BR-02 Apache Point documentary).\n',
         '## Examples by family\n']
    fams = []
    for r in rows:
        if r['family'] not in fams: fams.append(r['family'])
    for fam in fams:
        L.append('### %s\n' % fam)
        for r in [x for x in rows if x['family'] == fam]:
            L.append('**%s  %s**  [%s]' % (r['id'], r['title'], r['review_mode']))
            L.append('- Video / source: %s (%s, %s)' % (r['url'], r['org'], r['kind']))
            L.append('- Timestamp or frame: %s' % r['timestamp_or_frame'])
            L.append('- Evidence: %s' % (r['evidence_files'] or 'none saved (METADATA_ONLY)'))
            L.append('- Technique: %s' % r['technique']); L.append('- Why it helps the audience: %s' % r['why_it_helps_viewers'])
            L.append('- Application in Slot 07: %s\n' % r['application_slot07'])
    L.append('## Techniques adopted (verified entries only)\nSee `ANIMATION_TECHNIQUE_DECISIONS.md` (written after the reviews; each decision names the example it rests on and its review mode).\n')
    open(os.path.join(ROOT, 'ANIMATION_REFERENCE_ANALYSIS.md'), 'w').write('\n'.join(L)); print('wrote analysis,', len(rows), 'examples', dict(modes))

if __name__ == '__main__':
    main()
