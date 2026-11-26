"""Build MASTER_ASSET_MANIFEST.csv, ASSET_DEPENDENCY_GRAPH.md and storyboard/FULL_VISUAL_STORYBOARD.md.
Inputs: tools/asset_data.py (specs), tools/asset_usage.py (beat -> assets), tools/storyboard_data.py,
narration/NARRATION_BEAT_MAP.csv + NARRATION_TO_VISUAL_MAP.csv. Never hand-edit the outputs.
Run: python3 tools/build_manifest.py   (also runs the consistency checks; exits non-zero on any failure)
"""
import csv, shutil, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from asset_data import A, PROOFS
from asset_usage import USAGE
from storyboard_data import SCENES, COMPOSE

# ---------------------------------------------------------------- load
assets = {x['id']: x for x in A}
assert len(assets) == len(A), 'duplicate asset id'
beats = list(csv.DictReader(open(ROOT / 'narration/NARRATION_BEAT_MAP.csv')))
vis = {r['id']: r for r in csv.DictReader(open(ROOT / 'narration/NARRATION_TO_VISUAL_MAP.csv'))}
bid_order = [b['id'] for b in beats]
bt = {b['id']: b for b in beats}
scene_of = {}
for sid, _, b0, b1, _ in SCENES:
    for k in range(bid_order.index(b0), bid_order.index(b1) + 1):
        scene_of[bid_order[k]] = sid
assert set(scene_of) == set(bid_order), 'scenes must cover every beat'

children = defaultdict(list)
for x in A:
    x.setdefault('deps', [])
    for k in ('sci', 'vis', 'cams', 'canvas', 'transp', 'anim', 'pivots', 'draw', 'gen', 'rig'):
        x.setdefault(k, '')
    if x['parent']:
        assert x['parent'] in assets, (x['id'], 'unknown parent')
        children[x['parent']].append(x['id'])
for x in A:
    for d in x['deps']:
        assert d in assets, (x['id'], 'unknown dep', d)
    if x['kind'] == 'group':
        x['deps'] = list(children[x['id']])          # a group is its children
assert all(assets[a_]['kind'] != 'group' for b in USAGE.values() for a_ in b), 'beats list leaves, not groups'
for b, lst in USAGE.items():
    assert b in bt, b
    assert len(set(lst)) == len(lst), ('duplicate in', b)
    for a_ in lst:
        assert a_ in assets, (b, 'unknown asset', a_)
assert set(USAGE) == set(bid_order), 'every beat needs an asset list'

# ---------------------------------------------------------------- usage closure
# Art and graphics pull their dependencies into the same beats. Rigs do NOT (a rig is a build dependency of the
# art, not evidence that every layer is on screen), and groups roll up from their children afterwards.
used = defaultdict(set)
for b, lst in USAGE.items():
    for a_ in lst:
        used[a_].add(b)
changed = True
while changed:
    changed = False
    for x in A:
        if x['kind'] in ('group', 'rig'):
            continue
        for d in x['deps']:
            if not used[x['id']] <= used[d]:
                used[d] |= used[x['id']]; changed = True
for x in A:
    if x['kind'] == 'group':
        for c in children[x['id']]:
            used[x['id']] |= used[c]


def beats_sorted(s):
    return sorted(s, key=bid_order.index)


# ---------------------------------------------------------------- checks
proof_of = defaultdict(list)
for pid, _, lst in PROOFS:
    for a_ in lst:
        assert a_ in assets, (pid, a_)
        proof_of[a_].append(pid)
problems = []
for x in A:
    if x['kind'] != 'group' and not used[x['id']]:
        problems.append('unused asset: ' + x['id'])
    if x['kind'] in ('illustration', 'texture') and x['owner'] != 'Codex':
        problems.append('art not owned by Codex: ' + x['id'])
    if x['kind'] in ('code', 'model', 'rig') and x['owner'] != 'Claude':
        problems.append('code not owned by Claude: ' + x['id'])
# cycle check + dependency tiers on non-group edges
level = {}


def lv(i, stack=()):
    assert i not in stack, ('dependency cycle', stack + (i,))
    if i not in level:
        ds = [d for d in assets[i]['deps'] if assets[d]['kind'] != 'group']
        level[i] = 0 if not ds else 1 + max(lv(d, stack + (i,)) for d in ds)
    return level[i]


for x in A:
    if x['kind'] != 'group':
        lv(x['id'])
# the old provisional ids from the first beat map must all still resolve
old = {'EARTH_001_SURFACE', 'EARTH_003_ATMOSPHERE', 'MG_001_STOPWATCH', 'MG_002_RULER', 'MG_003_FORMULA', 'MG_004_HIST',
       'MG_005_LABELS', 'MG_006_HIGHLIGHT', 'MOON_001_GLOBE', 'MOON_002_TERRAIN_SURFACE', 'MOON_003_HORIZON',
       'OBS_001_EXTERIOR', 'OBS_002_DOME', 'OBS_003_INTERIOR', 'OBS_004_MOUNTAINS', 'OBS_005_NIGHT_SKY',
       'OPT_001_LIGHT_PULSE', 'OPT_002_BEAM_SPREAD', 'OPT_003_PHOTON_MARKER', 'OPT_004_CORNER_PATHS',
       'OPT_005_ATMOS_DISTORT', 'OPT_006_ACCUM', 'RETRO_001_ASSEMBLY', 'RETRO_002_CUBE_ARRAY', 'RETRO_003_CUBE_CUTAWAY',
       'TEL_001_HOUSING', 'TEL_003_APERTURE'}
problems += ['provisional id lost: ' + i for i in sorted(old - set(assets))]
# the beat map CSV must carry exactly USAGE (guards against forgetting to re-run build_beat_maps.py)
for b in bid_order:
    if vis[b]['required_assets'].split() != USAGE[b]:
        problems.append('NARRATION_TO_VISUAL_MAP.csv is stale for ' + b + ' (re-run tools/build_beat_maps.py)')
if problems:
    print('\n'.join(problems)); sys.exit(1)

# ---------------------------------------------------------------- manifest
HDR = ['asset_id', 'parent_asset', 'child_layers', 'kind', 'priority', 'description', 'scientific_reference',
       'visual_references', 'research_evidence', 'required_camera_angles', 'canvas_size', 'transparency_requirements',
       'intended_scenes', 'intended_beats', 'first_appears_s', 'animation_requirements', 'pivot_information',
       'draw_order', 'dependencies', 'generation_status', 'rigging_status', 'validation_status', 'responsible_agent',
       'proof_clips']
rows = []
for x in A:
    i = x['id']
    ub = beats_sorted(used[i])
    deps = [d for d in x['deps'] if x['kind'] != 'group']
    first = ('%.2f' % float(bt[ub[0]]['start_s'])) if ub else ''
    rows.append([i, x['parent'], ' '.join(children[i]), x['kind'], x['pri'], x['desc'], x['sci'], x['vis'], x['ev'],
                 x['cams'], x['canvas'], x['transp'], ' '.join(sorted({scene_of[b] for b in ub})), ' '.join(ub), first,
                 x['anim'], x['pivots'], x['draw'], ' '.join(deps),
                 x['gen'] or ('PLANNED' if x['kind'] != 'group' else ''),
                 x['rig'] or ('N/A' if x['kind'] != 'group' else ''),
                 'NOT_STARTED' if x['kind'] != 'group' else '', x['owner'], ' '.join(proof_of[i])])
for dst in (ROOT / 'MASTER_ASSET_MANIFEST.csv', ROOT / 'codex_handoff/MASTER_ASSET_MANIFEST.csv'):
    with open(dst, 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(HDR); w.writerows(rows)

leaf = [x for x in A if x['kind'] != 'group']
by_kind = defaultdict(int)
for x in leaf:
    by_kind[x['kind']] += 1
n_codex = sum(1 for x in leaf if x['owner'] == 'Codex')
n_claude = sum(1 for x in leaf if x['owner'] == 'Claude')

# ---------------------------------------------------------------- dependency graph
fam_of = lambda i: i.split('_')[0]
FAMS = ['EARTH', 'MOON', 'OBS', 'TEL', 'ASTRO', 'RETRO', 'OPT', 'MG', 'SCI', 'BG', 'RIG']
FAMNAME = {'EARTH': 'Earth', 'MOON': 'Moon', 'OBS': 'Observatory', 'TEL': 'Telescope', 'ASTRO': 'Astronaut',
           'RETRO': 'Retroreflector', 'OPT': 'Light and optics (code)', 'MG': 'Motion graphics (code)',
           'SCI': 'Scientific models (code)', 'BG': 'Backgrounds (code)', 'RIG': 'Rigs (code)'}
short = lambda i: i.split('_', 2)[1] + ' ' + i.split('_', 2)[2].replace('_', ' ').title()
g = ['flowchart LR']
for f in FAMS:
    g.append('  subgraph %s ["%s"]' % (f, FAMNAME[f]))
    for x in leaf:
        if fam_of(x['id']) == f:
            g.append('    %s["%s"]' % (x['id'], short(x['id'])))
    g.append('  end')
for x in leaf:
    for d in x['deps']:
        if assets[d]['kind'] != 'group':
            g.append('  %s --> %s' % (d, x['id']))
g.append('  classDef codex fill:#f3e3c0,stroke:#9a6b00,color:#000')
g.append('  classDef claude fill:#cfe3f5,stroke:#1f5f99,color:#000')
g.append('  class %s codex' % ','.join(x['id'] for x in leaf if x['owner'] == 'Codex'))
g.append('  class %s claude' % ','.join(x['id'] for x in leaf if x['owner'] == 'Claude'))

tiers = defaultdict(list)
for x in leaf:
    tiers[level[x['id']]].append(x['id'])
md = ['# Asset dependency graph (Slot 07)', '',
      'Generated by `tools/build_manifest.py` from `tools/asset_data.py`. An arrow `A --> B` means **B needs A first** (A is a dependency of B). '
      'Orange = Codex draws it; blue = Claude builds it in code. Rigs are build dependencies of the art, not proof that every layer is on screen.', '',
      '- %d buildable assets (%d Codex art, %d Claude code/model/rig) in %d families; %s.' % (
          len(leaf), n_codex, n_claude, len(FAMS), ', '.join('%d %s' % (v, k) for k, v in sorted(by_kind.items()))),
      '- Longest dependency chain: %d levels (levels below).' % (max(level.values()) + 1), '',
      '```mermaid', *g, '```', '', '## Build order (levels; everything in a level can start once the previous levels are done)', '',
      '| Level | Assets | Why here |', '|---|---|---|']
why = {0: 'no dependencies: models, textures, standalone art, code graphics'}
for k in sorted(tiers):
    md.append('| %d | %s | %s |' % (k, ' '.join('`%s`' % i for i in sorted(tiers[k])), why.get(k, 'needs level %d' % (k - 1) if k else '')))
md += ['', '## Rule that follows from the graph', '',
       '- Codex art in a level must pass its acceptance tests (G3) **before** a rig or a composite that depends on it is built; '
       'that is why the registered pose set and the reflector assembly are late in the order.',
       '- `SCI_004_SCALES` and `SCI_001..005` are level 0 or 1: the graphics and the proof clips read from them, so they are done first and checked by `check.py`.',
       '- `RETRO_002 -> RETRO_005 -> RETRO_003` is deliberate: the real array, the corner view and the cross-section must look like one object.',
       '- `RIG_004_CAMERA_MULTIPLANE` has no art dependencies and can be built and proven (P02, P03) with placeholder layers.', '',
       '## Proof clips (brief Phase 6) and what each one needs', '', '| Proof | Demonstrates | Needs |', '|---|---|---|']
for pid, d, lst in PROOFS:
    md.append('| %s | %s | %s |' % (pid, d, ' '.join('`%s`' % i for i in lst)))
md += ['', 'P13 is **PROPOSED** by me, not given in the brief: B17 to B21 combines the hero reflector, the astronaut and the optics, so it exercises the most families at once.', '']
(ROOT / 'ASSET_DEPENDENCY_GRAPH.md').write_text('\n'.join(md))

# ---------------------------------------------------------------- storyboard
S = ['# Full visual storyboard: Slot 07, Lunar Laser Ranging', '',
     '**Text storyboard, no art yet.** Generated from `narration/NARRATION_TO_VISUAL_MAP.csv`, `NARRATION_BEAT_MAP.csv`, `tools/storyboard_data.py` and `MASTER_ASSET_MANIFEST.csv`. '
     'Times are from the official V2 take (95.39 s, 2026-11-26 10:39; V1 92.53 s is historical). Phrase edges are measured (+-0.02 s); word anchors are estimates (+-0.12 s). '
     'Vertical 9:16, 1080x1920 final. **Nothing here has been watched or listened to by a human**, and there is no animatic yet (G2).', '',
     '## Rules that apply to every shot', '',
     '- **Colour grammar:** outbound light warm, return light cool, for the whole film. Earth is at the bottom and the Moon at the top of every schematic frame.',
     '- **Model classes** (from the beat map): actual object, simplified scientific illustration, time-compressed, magnified, non-scale diagram, artistic, educational symbol. Light and photons are never drawn as real visible objects.',
     '- **Reveal order:** the reflector hardware first appears at B17; B05 shows only a ring on the Moon.',
     '- **No on-screen text** except symbols and numbers from the claims ledger; words appear only if the voice is ever muted.',
     '- **Caption band** at the bottom: exact numbers fixed at G5 (playbook section 13). Key subjects stay out of it.',
     '- **Observatory** is a generic, labelled illustration (never captioned "Apache Point"). **Astronaut** is not named on screen (source only a snippet).', '',
     '## Owner decisions (all settled 2026-11-26; none blocks research or production planning)', '',
     '1. ~~Voice~~ **DECIDED: the generated narration is the production timing reference; the original WAV is preserved.** The human listening check (G1) stays mandatory before publication and is NOT PERFORMED.',
     '2. ~~C06 "tiny fraction"~~ **DECIDED: keep the recorded line.** The footprint inset at B20 is mandatory (picture rule, ledger C06).',
     '3. ~~B29b~~ **DECIDED: keep it, because it is in the recording** ("And somehow those incredibly faint returns let them measure the distance", 68.56 to 72.65 s).',
     '4. ~~Non-scale schematic~~ **DECIDED: a clearly identified not-to-scale Earth-Moon schematic is allowed where necessary** (true spacing is about 30 Earth diameters); disclose it once on screen or in the caption plan.', '',
     '## Scenes', '', '| Scene | Beats | Start | End | Length | Story job |', '|---|---|---|---|---|---|']
for sid, nm, b0, b1, job in SCENES:
    s0, s1 = float(bt[b0]['start_s']), float(bt[b1]['end_s'])
    S.append('| %s %s | %s to %s | %.2f | %.2f | %.1f s | %s |' % (sid, nm, b0, b1, s0, s1, s1 - s0, job))
S.append('')
for sid, nm, b0, b1, job in SCENES:
    ids = bid_order[bid_order.index(b0):bid_order.index(b1) + 1]
    S += ['---', '', '## %s: %s (%s)' % (sid, nm, job), '']
    for b in ids:
        r, v = bt[b], vis[b]
        S += ['### %s  %.2f to %.2f s  (%s, %s)' % (b, float(r['start_s']), float(r['end_s']), r['beat_type'], v['model_class']), '',
              '> %s' % r['spoken_text'], '',
              '| | |', '|---|---|',
              '| Frame (9:16) | %s |' % COMPOSE[b],
              '| Camera | %s |' % v['camera'],
              '| Action | %s |' % v['animation_action'],
              '| Anchor | word "%s" at %.2f s (%s) |' % (r['anchor_word'].split(':', 1)[1], float(r['anchor_s']), 'estimate +-0.12 s'),
              '| Layers | FG: %s / MG: %s / BG: %s |' % (v['foreground'], v['midground'], v['background']),
              '| Graphics | %s |' % v['motion_graphics'],
              '| Science state | %s |' % v['scientific_state'],
              '| Sound | %s |' % v['sound_design'],
              '| Viewer must understand | %s |' % v['viewer_must_understand'],
              '| Reveal / transition | %s / %s |' % (r['reveal_opportunity'], r['transition_opportunity']),
              '| Assets | %s |' % ' '.join('`%s`' % a_ for a_ in USAGE[b]), '']
S += ['---', '', '## Not in this storyboard on purpose', '',
      '- **Control-room workstations, rear/walking/top astronaut views, reflector top view:** the brief lists them, but no beat shows them. Add them only if a beat changes (the manifest has no row for them).',
      '- **Apollo 14 and 15 arrays:** the narration says "Apollo astronauts left special reflectors" and C05 is sourced for all three, but the film shows the Apollo 11 site only.',
      '- **Sound design cue sheet** and **captions**: later phases; the sound column above is the draft.', '']
(ROOT / 'storyboard/FULL_VISUAL_STORYBOARD.md').write_text('\n'.join(S))

# ---------------------------------------------------------------- report
print('assets %d (leaf %d: codex %d, claude %d), groups %d, beats %d, levels %d' % (
    len(A), len(leaf), n_codex, n_claude, len(A) - len(leaf), len(bid_order), max(level.values()) + 1))
print('by kind:', dict(by_kind))
print('manifest rows', len(rows), '| unused 0 | cycles 0 | stale csv 0')
