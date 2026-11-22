"""Writes shot_sprites/shot_sprites_manifest.json: sha256 + placement + shots + measured validation + independent-review verdict per sprite.
Sprites are shot-specific whole-figure reproductions (NOT registry assets, NOT a reusable rig). A sprite is listed only if the independent review gave it PASS or PARTIAL."""
import hashlib, json, os, sys
PS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SP = os.path.join(PS, 'shot_sprites')
meta = json.load(open(os.path.join(SP, 'sprites_meta.json'))); rev = json.load(open(os.path.join(SP, 'reviews', 'independent_review_v2.json')))
USES = dict(hips_A_happy=['SH010'], hips_A_neutral=['SH012', 'SH015'], hips_B_happy=['SH008'], earth_A=['SH018'], earth_B=['SH018'], earth_sh004_A=['SH004'], earth_sh004_B=['SH004'],
            man_brown=['SH004'], calendar=['SH005', 'SH017'], arrow_left=['SH005', 'SH017'], dollar_bare=['SH003'], bubble_disc=['SH003'], burst_particles=['SH003'])
VAL = {}
for f in ('hips_validation.json', 'misc_validation.json'):
    p = os.path.join(SP, 'validation', f)
    if os.path.exists(p): VAL[f] = json.load(open(p))
out = dict(_doc='Shot sprites: whole-figure/state reproductions drawn from measured geometry for specific reference shots. Not reusable rig parts. Independent review required for listing.', sprites={})
for n, u in USES.items():
    v = rev.get('sprites', {}).get(n, {}).get('verdict')
    if v not in ('PASS', 'PARTIAL'): print('NOT LISTED (review verdict %s): %s' % (v, n)); continue
    path = os.path.join(SP, n + '.png'); out['sprites'][n] = dict(sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(), placement=meta[n], shots=u, review_verdict=v, review_note=rev['sprites'][n].get('note', ''))
out['validation_files'] = sorted(VAL); out['review_file'] = 'shot_sprites/reviews/independent_review_v2.json'
json.dump(out, open(os.path.join(SP, 'shot_sprites_manifest.json'), 'w'), indent=1); print('listed', len(out['sprites']))
