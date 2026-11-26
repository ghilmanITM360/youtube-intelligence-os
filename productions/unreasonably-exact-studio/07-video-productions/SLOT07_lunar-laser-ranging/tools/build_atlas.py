"""Rebuild REAL_WORLD_VISUAL_REFERENCE_ATLAS.md from research/REFERENCE_MANIFEST.csv + fragments' gaps.  python3 tools/build_atlas.py"""
import csv, glob, json, os, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['earth', 'moon', 'observatory', 'telescope', 'astronaut', 'reflector', 'optical', 'stopwatch', 'diagrams']
NOTE = {'earth': 'EARTH_RESEARCH.md', 'moon': 'MOON_RESEARCH.md', 'observatory': 'OBSERVATORY_RESEARCH.md', 'telescope': 'TELESCOPE_RESEARCH.md',
        'astronaut': 'ASTRONAUT_RESEARCH.md', 'reflector': 'REFLECTOR_RESEARCH.md', 'optical': 'OPTICAL_RESEARCH.md', 'stopwatch': 'STOPWATCH_RESEARCH.md', 'diagrams': 'DIAGRAMS_RESEARCH.md'}

def main():
    atlas = os.path.join(ROOT, 'REAL_WORLD_VISUAL_REFERENCE_ATLAS.md'); arch = os.path.join(ROOT, 'research', 'asset_research', 'ATLAS_PASS1_ARCHIVE.md')
    if os.path.exists(atlas) and not os.path.exists(arch) and 'GENERATED' not in open(atlas).read(300): shutil.copy(atlas, arch)
    refs = list(csv.DictReader(open(os.path.join(ROOT, 'research', 'REFERENCE_MANIFEST.csv'))))
    gaps = {}
    for fn in glob.glob(os.path.join(ROOT, 'research', 'reference_fragments', '*.json')):
        d = json.load(open(fn)); gaps[d.get('family')] = d.get('gaps', [])
    L = ['# Real-world visual reference atlas (GENERATED from research/REFERENCE_MANIFEST.csv; do not hand-edit)\n',
         'Every row is a locally saved, lawfully usable image that was opened and described (`viewed`). The pass-1 URL-only atlas is archived at `research/asset_research/ATLAS_PASS1_ARCHIVE.md`. Reference images are for study only; the film uses original redrawn art.\n',
         'Totals: %d references (%d saved locally, %d link-only).\n' % (len(refs), sum(r['licence_status'] != 'LINK_ONLY' for r in refs), sum(r['licence_status'] == 'LINK_ONLY' for r in refs))]
    for fam in ORDER:
        rs = [r for r in refs if r['family'] == fam]
        if not rs and fam not in gaps: continue
        L.append('\n## %s  (%d refs)  | research note: `research/asset_research/%s`\n' % (fam, len(rs), NOTE[fam]))
        for r in rs:
            L.append('### %s  %s' % (r['ref_id'], r['title']))
            if r['licence_status'] != 'LINK_ONLY' and r['local_filename']:
                L.append('![%s](%s)\n' % (r['ref_id'], r['local_filename']))
            L.append('- file: `%s` (%sx%s, sha256 `%s`)' % (r['local_filename'] or 'LINK ONLY', r['local_w'], r['local_h'], (r['sha256_local'] or '')[:16]))
            L.append('- source: %s | %s | licence **%s** %s' % (r['source_page_url'] or r['source_url'], r['source_org'], r['licence_status'], r['credit_line']))
            L.append('- perspective: %s' % r['camera_perspective']); L.append('- visible: %s' % r['visible_characteristics'])
            L.append('- science: %s' % r['scientific_relevance']); L.append('- production: %s' % r['production_influence']); L.append('- assets: %s\n' % r['asset_ids'])
        if gaps.get(fam):
            L.append('**Gaps (not found lawfully or not yet done):**'); [L.append('- %s' % g) for g in gaps[fam]]
    open(atlas, 'w').write('\n'.join(L)); print('atlas written, %d refs' % len(refs))

if __name__ == '__main__':
    main()
