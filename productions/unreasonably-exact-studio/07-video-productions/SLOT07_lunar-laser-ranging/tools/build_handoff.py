"""Build codex_handoff/ content that is derived from data: references/ (copies + index), individual_asset_briefs/, MASTER_ASSET_PROMPT_BIBLE.md,
MASTER_ASSET_MANIFEST.csv copy. Hand-written docs in codex_handoff/ are never touched.
Run after: build_manifest.py and merge_references.py.   python3 tools/build_handoff.py
"""
import csv, os, shutil, sys, textwrap
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(ROOT, 'codex_handoff')

FAMREF = {'EARTH': ['earth', 'diagrams'], 'MOON': ['moon'], 'OBS': ['observatory'], 'TEL': ['telescope'], 'ASTRO': ['astronaut'],
          'RETRO': ['reflector', 'optical']}
REFDIR = {'earth': 'earth', 'moon': 'moon', 'observatory': 'observatory', 'telescope': 'telescope', 'astronaut': 'astronaut',
          'reflector': 'retroreflector', 'optical': 'retroreflector', 'diagrams': 'earth', 'stopwatch': None}

MUST_NOT_CHANGE = {
    'EARTH': 'Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).',
    'MOON': 'Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.',
    'OBS': 'Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.',
    'TEL': 'One telescope design across exterior, aperture and cutaway; same proportions, same mount type; not any specific real telescope; no text or logos.',
    'ASTRO': 'Costume, helmet, gold visor, PLSS, gloved hands and boots identical in every pose; no face visible; no named patch; sun from the left; height ratio to the 46 cm reflector panel fixed.',
    'RETRO': 'Exactly 100 round cube faces in a 10x10 grid on a 46 cm panel (Apollo 11 style); cube diameter 3.8 cm = 1/12 of the panel width; same panel colour, frame and tilt toward Earth in every view; sun from the left.',
}
FAILURES = {
    'EARTH': 'baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.',
    'MOON': 'Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.',
    'OBS': 'fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.',
    'TEL': 'invented hardware; mount that cannot rotate; aperture not a true circle; different design in cutaway vs exterior; text on the housing.',
    'ASTRO': 'face visible in the visor; bare hands; extra or fused fingers; detached equipment; cloth billowing; joint caps that are round discs; different boots left/right; proportions drifting between poses.',
    'RETRO': 'wrong cube count; cubes fused into a texture; panel too large relative to the astronaut; perspective that differs between array and cutaway so the match cut cannot line up; baked glow standing for light.',
}
BATCH = {'EARTH': 'Batch 1', 'MOON': 'Batches 1 and 3', 'RETRO': 'Batch 2', 'OBS': 'Batch 4', 'TEL': 'Batch 4', 'ASTRO': 'Batch 5 (Batch 0 = calibration asset)'}
PALETTE = {
    'EARTH': 'Ocean #0A1A3E (night) to #2C6CC4 (lit); land muted greens/ochres, never saturated; clouds #F0F4FA at 85% value; atmosphere rim #60C8FF at low opacity, thin.',
    'MOON': 'Highlights #ACACB0, mid #7E7E84, shadow #3A3A42; maria #55555D to #6A6A72 (cooler, darker); sky black #000000-#05070D.',
    'OBS': 'Night palette: sky #070B1A to #16223F, building/ridges #0B1530-#2A3558, instrument white/grey #E6E9F0 / #AEB4C2 / #6A7080; lit windows warm-dim #C9A877 at ~30% value; no sunlit surfaces.',
    'TEL': 'Instrument white #E6E9F0, grey #AEB4C2, dark grey #6A7080, black glass; cool night light; no sunlit surfaces.',
    'ASTRO': 'Suit white #ECEEF4 (never pure white), gold visor #D6AA46, grey overshoes/gloves #8E929C, connector rings blue/red/silver; hard lunar sunlight from the left, long shadows to the right.',
    'RETRO': 'Silver aluminium frame #AEB4C2-#E6E9F0, bright white base, dark glossy glass faces #1A2030-#2C3550 with faint blue-grey sheen; hard sunlight from the left.'}
TESTS = {
    'texture': 'A1-A8, B5 (light), B6 (reference), B8 (no baked graphics), plus P01 (rotation, seam) when used on a globe.',
    'illustration': 'A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).',
}


def read(path):
    return list(csv.DictReader(open(os.path.join(ROOT, path))))


def main():
    man = read('MASTER_ASSET_MANIFEST.csv'); byid = {r['asset_id']: r for r in man}
    refs = read('research/REFERENCE_MANIFEST.csv') if os.path.exists(os.path.join(ROOT, 'research', 'REFERENCE_MANIFEST.csv')) else []
    os.makedirs(os.path.join(H, 'individual_asset_briefs'), exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'MASTER_ASSET_MANIFEST.csv'), os.path.join(H, 'MASTER_ASSET_MANIFEST.csv'))
    # ---- references/ copies + per-family index (saved files only)
    idx = {}
    red = {x['drop']: x['keep'] for x in read('research/redundant_refs.csv')} if os.path.exists(os.path.join(ROOT, 'research', 'redundant_refs.csv')) else {}
    byref = {r['ref_id']: r for r in refs}
    for drop, keep in red.items():  # move asset tags onto the surviving reference, then remove the duplicate from the active handoff
        if drop in byref and keep in byref:
            byref[keep]['asset_ids'] = ' '.join(sorted(set(byref[keep]['asset_ids'].split()) | set(byref[drop]['asset_ids'].split())))
    refs = [r for r in refs if r['ref_id'] not in red and r['viewed'] == 'True']  # active handoff: viewed, non-duplicate only
    shutil.rmtree(os.path.join(H, 'references'), ignore_errors=True)
    for r in refs:
        d = REFDIR.get(r['family'])
        if not d or r['licence_status'] == 'LINK_ONLY' or not r['local_filename']: continue
        dst_dir = os.path.join(H, 'references', d); os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, os.path.basename(r['local_filename']))
        shutil.copy2(os.path.join(ROOT, r['local_filename']), dst)
        r['_handoff'] = os.path.relpath(dst, H); idx.setdefault(d, []).append(r)
    for d, rs in idx.items():
        with open(os.path.join(H, 'references', d, 'REFERENCE_INDEX.md'), 'w') as f:
            f.write('# %s references (saved locally; reference use only, never in the film)\n\n' % d)
            for r in rs:
                f.write('## %s  `%s`\n- source: %s (%s)\n- licence: %s %s\n- perspective: %s\n- what is visible: %s\n- influences: %s\n- assets: %s\n\n' % (
                    r['ref_id'], os.path.basename(r['_handoff']), r['source_page_url'] or r['source_url'], r['source_org'], r['licence_status'], r['credit_line'],
                    r['camera_perspective'], r['visible_characteristics'], r['production_influence'], r['asset_ids']))
    # ---- briefs (16 mandatory sections; see MASTER_STANDARDS_CROSSWALK.md)
    import brief_data
    briefs = []
    audit = []
    for a in man:
        if a['kind'] not in ('illustration', 'texture'): continue
        fam = a['asset_id'].split('_')[0]
        bd = brief_data.get(a['asset_id'])
        if bd is None:
            audit.append('MISSING brief_data for %s' % a['asset_id']); bd = {}
        tagged = [r for r in refs if a['asset_id'] in r['asset_ids'].split() and r.get('_handoff')]
        famrefs = [r for r in refs if r['family'] in FAMREF.get(fam, []) and r.get('_handoff') and r not in tagged]
        L = []
        L.append('# Brief: %s\n' % a['asset_id'])
        L.append('Priority %s | kind %s | batch %s | status %s | first appears %ss in beats %s | construction method: **%s**\n' % (
            a['priority'], a['kind'], BATCH.get(fam, '?'), a['generation_status'], a['first_appears_s'], a['intended_beats'], bd.get('method', '?')))
        L.append('Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.\n')
        L.append('## 1. Real-world object identification\n%s\n\n%s\n' % (bd.get('real', a['description']), 'Manifest description: ' + a['description']))
        L.append('## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)')
        for r in tagged[:10]: L.append('- **%s** `%s` [%s]: %s' % (r['ref_id'], r['_handoff'], r['camera_perspective'], r['production_influence']))
        for r in famrefs[:8]: L.append('- (family context) **%s** `%s` [%s]' % (r['ref_id'], r['_handoff'], r['camera_perspective']))
        if not tagged:
            audit.append('NO TAGGED REF: %s' % a['asset_id'])
            L.append('- **No reference is tagged to this exact asset; the family references above are the only evidence. Research and record what you used in `RESEARCH_NOTES.md`.**')
        L.append('\nWeb pointers (verify independently): %s\n' % a['visual_references'][:500])
        L.append('## 3. Intended camera angles\n%s\n' % a['required_camera_angles'])
        L.append('## 4. Required geometry and proportions\n%s\n' % bd.get('geom', 'See manifest row.'))
        L.append('## 5. Illustration style\n%s, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.\n' % brief_data.P)
        L.append('## 6. Palette and lighting\n%s\nSun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.\n' % PALETTE.get(fam, ''))
        L.append('## 7. Pose or object-state requirements\n%s\n' % bd.get('state', ''))
        L.append('## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)')
        L.append('| Layer file stem | Contents | Parent | Pivot | Draw order |\n|---|---|---|---|---|')
        for ln, content, parent, pivot, order in bd.get('layers', []):
            for pz in (('stand34', 'kneel34', 'side_step') if '<pose>' in (ln + parent) else (None,)):
                L.append('| `%s` | %s | `%s` | %s | %s |' % (ln.replace('<pose>', pz) if pz else ln, content, parent.replace('<pose>', pz) if pz else parent, pivot, order))
        L.append('\nParent group: `%s`. Child layers named in the manifest: %s. Depends on: %s.\n' % (a['parent_asset'], a['child_layers'] or 'none (single asset)', a['dependencies'] or 'none'))
        L.append('## 9. Hidden overlap requirements\n%s\nNever a generic round cap; state the unit used in `PIVOTS.json`.\n' % bd.get('overlap', ''))
        L.append('## 10. Parent-child relationships\nParent group `%s`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent\'s rotation and translation). Rotate children only about their own listed pivot.\n' % a['parent_asset'])
        L.append('## 11. Pivot registration\nCanvas: **%s**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): %s. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**\n' % (a['canvas_size'], a['pivot_information']))
        L.append('## 12. Intended motion\n%s\nThis art is only the starting pose; Claude drives the motion in code.\n' % (bd.get('motion') or a['animation_requirements']))
        L.append('## 13. Required animation proof (Claude renders; extremes are the shot\'s real range)\nProof clips: **%s**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.\n' % bd.get('proof', a['proof_clips'] or 'none'))
        L.append('## 14. Objective acceptance tests\n%s\nA-tests pass numerically: RGBA; canvas exactly %s; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.\nFull definitions: `../ASSET_ACCEPTANCE_TESTS.md`.\n' % (TESTS[a['kind']], a['canvas_size']))
        L.append('## 15. Scientific or historical limitations (what the art must not claim)\n%s\n\nMust not change: %s\n\nKnown failure modes: %s\n' % (bd.get('limits', ''), MUST_NOT_CHANGE.get(fam, ''), FAILURES.get(fam, '')))
        L.append('## 16. Expected deliverable filenames\n`%s`\nPlus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).\n' % bd.get('out', a['asset_id'].lower() + '.png'))
        text = '\n'.join(L)
        open(os.path.join(H, 'individual_asset_briefs', a['asset_id'] + '.md'), 'w').write(text)
        # path existence check
        import re
        for p in re.findall(r'`(references/[^`]+)`', text):
            if not os.path.exists(os.path.join(H, p)): audit.append('BROKEN PATH in %s: %s' % (a['asset_id'], p))
        briefs.append((a, tagged, famrefs))
    # make the package self-contained: copy the files the briefs point at
    for src, dst in [('CODEX_HANDOFF.md', 'CODEX_HANDOFF.md'), ('look_dev/VISION_CARD.md', 'VISION_CARD.md'), ('look_dev/LOOKDEV_DECISION.md', 'LOOKDEV_DECISION.md'),
                     ('storyboard/animatic/ANIMATIC_V1_REFERENCE_INFORMED.mp4', 'ANIMATIC_V1_REFERENCE_INFORMED.mp4')]:
        if os.path.exists(os.path.join(ROOT, src)): shutil.copy2(os.path.join(ROOT, src), os.path.join(H, dst))
        else: audit.append('NOT YET AVAILABLE for package: %s' % src)
    import glob
    os.makedirs(os.path.join(H, 'placement_boards'), exist_ok=True)
    for s in sorted(glob.glob(os.path.join(ROOT, 'storyboard', 'panels', 'S[0-9][0-9]_*.png'))): shutil.copy2(s, os.path.join(H, 'placement_boards', os.path.basename(s)))
    import re
    for a, _, _ in briefs:
        txt = open(os.path.join(H, 'individual_asset_briefs', a['asset_id'] + '.md')).read()
        for q in set(re.findall(r'`(\.\./[A-Za-z_]+\.md)`', txt)):
            if not os.path.exists(os.path.normpath(os.path.join(H, 'individual_asset_briefs', q))): audit.append('BROKEN LINK in %s: %s' % (a['asset_id'], q))
    os.makedirs(os.path.join(ROOT, 'qa'), exist_ok=True)
    open(os.path.join(ROOT, 'qa', 'handoff_audit.txt'), 'w').write('briefs written: %d\n%s\n' % (len(briefs), '\n'.join(audit) or 'no problems found (all section-2 paths exist, every brief has brief_data and a tagged reference)'))
    print('audit:', audit or 'clean')
    # ---- prompt bible
    P = ['# Master asset prompt bible\n',
         'Prompts are *starting points*. Every prompt below is paired with the saved reference images (paths) that must be attached or inspected first. Codex must verify the references, may improve the prompt, and must record the exact prompt used and rejected ones in `IMAGE_GENERATION_PROMPTS.md`.\n',
         '## Prompt structure (use for every asset)',
         '1. **Reference attachment line**: list the reference file paths and what to take from each (silhouette, proportions, colour, material).',
         '2. **Subject and view**: the exact object, camera angle, canvas, and that it is ONE isolated asset.',
         '3. **Geometry and counts**: proportions, numbers (cubes, fingers, struts).',
         '4. **Style**: painterly-clean cinematic illustration, no outlines, no photographic noise.',
         '5. **Light**: sun from the left, about 30 degrees up, hard shadows only where the brief says.',
         '6. **Layering and background**: isolated on transparent or flat neutral background; separate layers requested explicitly.',
         '7. **Negative list**: no text, numbers, arrows, rays, beams, lens flare, motion blur, logos, people\'s faces, cast shadow that is not requested, extra objects.\n',
         '## Global negative prompt (append to every prompt)',
         '"text, letters, numerals, arrows, diagrams, laser beams, light rays, lens flare, glow standing for light, motion blur, depth of field blur, logos, watermarks, signage, faces, extra limbs, extra fingers, fused geometry, floating parts, photographic noise, outlines, cartoon outlines"\n']
    FAMNAME = {'EARTH': 'Earth', 'MOON': 'Moon', 'OBS': 'Observatory environment', 'TEL': 'Telescope', 'ASTRO': 'Apollo astronaut', 'RETRO': 'Lunar retroreflector'}
    for fam in ['EARTH', 'MOON', 'RETRO', 'OBS', 'TEL', 'ASTRO']:
        P.append('## %s' % FAMNAME[fam]); P.append('Must not change: %s\n' % MUST_NOT_CHANGE[fam]); P.append('Failure modes: %s\n' % FAILURES[fam])
        for a, tagged, famrefs in briefs:
            if not a['asset_id'].startswith(fam + '_'): continue
            rp = ['`%s`' % r['_handoff'] for r in (tagged + famrefs)[:5]]
            P.append('### %s\n- attach / inspect first: %s' % (a['asset_id'], ', '.join(rp) if rp else '**no reference saved yet (GAP): research first**'))
            P.append('- prompt skeleton: "%s Canvas %s. Views: %s. Isolated asset, %s. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt' % (
                a['description'], a['canvas_size'], a['required_camera_angles'], a['transparency_requirements'].split(';')[0]))
            P.append('- full brief: `individual_asset_briefs/%s.md`\n' % a['asset_id'])
    open(os.path.join(H, 'MASTER_ASSET_PROMPT_BIBLE.md'), 'w').write('\n'.join(P))
    # ---- root copy of the bible for the documentation list
    shutil.copy(os.path.join(H, 'MASTER_ASSET_PROMPT_BIBLE.md'), os.path.join(ROOT, 'MASTER_ASSET_PROMPT_BIBLE.md'))
    nt = sum(1 for _, t, _ in briefs if t); nf = sum(1 for _, t, f in briefs if not t and f); ng = sum(1 for _, t, f in briefs if not t and not f)
    print('briefs %d (with tagged refs %d, family refs only %d, no refs %d); reference copies %d' % (len(briefs), nt, nf, ng, sum(len(v) for v in idx.values())))


if __name__ == '__main__':
    main()
