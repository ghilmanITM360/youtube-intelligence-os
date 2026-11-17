# R20 transfer contract: everything a second machine needs, beyond Git, to resume visual review and re-run RT renders.
import json, hashlib, os, subprocess, datetime, glob
from pathlib import Path
B = Path.home() / 'YIOS-local-audits/barely-evolved'; N = B / 'channel_synthesis/nonaudio_completion'
def h(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
inv = json.load(open(N / 'portability/PORTABILITY_INVENTORY.json')); items = []
FR = {'uPQcyookL0Y': 14647, 'mNLNb-Z4T0M': 16689, 'GNaBxt_zIRA': 16319}
for x in inv['not_portable']:
    if x['kind'] not in ('SOURCE_MP4', 'RT_RENDER'): continue
    p = Path(x['path']) if x['path'].startswith('/') else B / x['path']
    rel = f"source_mp4/{p.name}" if x['kind'] == 'SOURCE_MP4' else 'rt_renders/' + str(p.relative_to(B))
    it = dict(kind=x['kind'], local_path=str(p), package_path=rel, bytes=p.stat().st_size, sha256=h(p), required_for='resume any visual review/measurement (sole primary evidence)' if x['kind'] == 'SOURCE_MP4' else 'compare RT evaluations without re-rendering (render.py + spec + timeline are in Git)')
    if x['kind'] == 'SOURCE_MP4': it['expected_decoded_frames'] = next(v for k, v in FR.items() if k in p.name)
    assert it['sha256'] == x['sha256'] and it['bytes'] == x['bytes'], p
    items.append(it)
rt01 = B / '2026-11-02-uPQcyookL0Y-deep-ct-scan/reconstruction_test/RT-01/rt01.mp4'
items.append(dict(kind='RT_RENDER', local_path=str(rt01), package_path='rt_renders/' + str(rt01.relative_to(B)), bytes=rt01.stat().st_size, sha256=h(rt01), required_for='RT-01 render (was listed under DERIVED_LOCAL_ONLY)'))
lock = Path.home() / 'YIOS-local-audits/tooling/visual-ct-scan-requirements.lock'
items.append(dict(kind='DEPENDENCY_FILE', local_path=str(lock), package_path='deps/visual-ct-scan-requirements.lock', bytes=lock.stat().st_size, sha256=h(lock), required_for='recreate python env for scripts and render.py'))
fonts = sorted({f for f in subprocess.run("grep -hoE \"/(System/)?Library/Fonts/[^'\\\"]+\\.tt[cf]\" " + ' '.join(glob.glob(str(B / '*/reconstruction_test/*/render.py'))), shell=True, capture_output=True, text=True).stdout.split('\n') if f})
deps = [dict(kind='SYSTEM_FONT', path=f, sha256=h(f) if os.path.exists(f) else None, bytes=os.path.getsize(f) if os.path.exists(f) else None, note='macOS system font; not copied (licensed with OS); a target Mac must have the same file or RT renders differ') for f in fonts]
py = B.parent / 'tooling/visual-ct-scan-venv/bin/python3'
ver = subprocess.run([str(py), '-c', 'import sys,cv2,numpy,PIL;print(sys.version.split()[0],cv2.__version__,numpy.__version__,PIL.__version__)'], capture_output=True, text=True).stdout.split()
deps.append(dict(kind='RUNTIME', python=ver[0], opencv=ver[1], numpy=ver[2], pillow=ver[3], ffmpeg=subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True).stdout.split('\n')[0]))
deps.append(dict(kind='KNOWN_HARDCODED_PATH', file='2026-11-03-GNaBxt_zIRA-deep-ct-scan/reconstruction_test/RT-V3-S01/render.py', note='contains an absolute /Users/ghilmankhan/... output path; edit or recreate that path on the target before re-rendering'))
man = dict(
    schema='BE_TRANSFER_MANIFEST_v2', built_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), machine='Machine A',
    status='TRANSFER_READY__DESTINATION_REQUIRED', git_portable=dict(branch='research/barely-evolved-visual-forensics', base_commit='0c1eeaadf2d5b4cbcedef9265efd8dd68aeac603', covers='all ledgers, tables, reports, specs, prompts, gates, seals, scripts, briefs, RT render.py/timeline/spec/evaluations'),
    package_items=items, package_bytes=sum(i['bytes'] for i in items), dependencies_not_packaged=deps,
    regenerable_not_packaged='frames, strips, contact sheets, crop sheets, ASR WAVs: regenerable from SOURCE_MP4 with the published scripts (see PORTABILITY_INVENTORY.json DERIVED_LOCAL_ONLY)',
    procedure='scripts/stage_and_verify.sh <DEST> copies package_items to <DEST>/barely-evolved-transfer/, writes SHA256SUMS, re-hashes at the destination, and runs a representative restore (ffprobe decoded frame count of each SOURCE_MP4 + one RT decode). It refuses a destination on the same device as the source unless --same-device-test is given, and such a test is never durable backup.',
    r20_pass_requires='a copy at an owner-approved durable off-device destination, verified by stage_and_verify.sh at that destination (and readable from the second Mac)')
json.dump(man, open(N / 'portability/TRANSFER_MANIFEST_v2.json', 'w'), indent=1)
with open(N / 'portability/TRANSFER_SHA256SUMS.txt', 'w') as f:
    for i in items: f.write(f"{i['sha256']}  {i['package_path']}\n")
print(len(items), man['package_bytes'], [d.get('sha256', '')[:8] if d.get('sha256') else d for d in deps[:len(fonts)]])
