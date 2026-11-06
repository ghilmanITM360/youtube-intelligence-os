# N19: camera reconciliation side table and R20 manifest v3. Published ledgers and manifest v2 stay unchanged.
# The 11 verdicts below were read by the session 15f69c1b orchestrator from native sheets (b2_native_evidence.py) and
# flagged_region_motion_n19.py. Not blind: the reader knew the M3 and ledger values. Same vendor. Endpoints only.
import csv, hashlib, json, re, sys
from pathlib import Path
B = Path.home() / 'YIOS-local-audits/barely-evolved'; N = B / 'channel_synthesis/nonaudio_completion'; P = N / 'portability'; M = N / 'method_v3'
h = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
V = ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']; NATIVE_BASIS = {'NATIVE_ORCH'}
ADJ = {
 'mNLN-U0189': ('R3_FLAG', 'MIXED', 'CAMERA', 'MED', '38 textured tiles fit one frame-centred zoom of +1.70% (rms 0.75 px) across wall, board, desk and teacher; pointer arm visibly differs at the endpoints.'),
 'mNLN-U0231': ('R3_FLAG', 'MIXED', 'CAMERA_VS_SLIDE_UNRESOLVED', 'MED', 'Both figures fit a +1.5% frame-centred scale, but the arrow grows far more, and the white background gives no static reference. M3 CAMERA_FRAMEWIDE not confirmed here.'),
 'mNLN-U0254': ('R3_FLAG', 'MIXED', 'CAMERA', 'MED', '39 tiles fit a frame-centred zoom of +2.01% (rms 1.33 px) across the painted set; teacher tiles deviate by a few px.'),
 'GNaB-U0109': ('R3_FLAG', 'CAMERA', 'CAMERA', 'MED', 'Sky, hills, ground and foreground fit a frame-centred zoom of +4.94% (rms 3.86 px); man keeps his pose at the endpoints, so the blind CHARACTER label is not supported.'),
 'GNaB-U0192': ('R3_FLAG', 'MIXED', 'CAMERA', 'MED', '39 tiles fit a frame-centred zoom of +1.64% (rms 1.38 px); pointer tiles deviate and the pointer tip differs at the endpoints.'),
 'GNaB-U0239': ('R3_FLAG', 'WHOLE_CONTENT_MOVE', 'CAMERA_VS_SLIDE_UNRESOLVED', 'HIGH', 'Bear translates -16 px per frame uniformly (rms 0.16 px); it is the only object on white, so camera and object slide cannot be separated. Ledger STATIC_HOLD is wrong. M3 CAMERA_FRAMEWIDE not confirmed here.'),
 'mNLN-U0167': ('LEDGER_CAMERA_M3_NOT_CAMERA', 'CHARACTER', 'NOT_CAMERA', 'HIGH', 'All change above threshold lies in x1583-1919 y528-891 around the man; 38 tiles measure 0 px; f8629 is a hard cut. Ledger CAMERA class not supported.'),
 'mNLN-U0222': ('LEDGER_CAMERA_M3_NOT_CAMERA', 'DIGITAL_ZOOM', 'NOT_CAMERA', 'HIGH', 'Room tiles at both frame edges measure 0-1 px while scroll tiles move up to 78 px: the scroll element scales over a held room.'),
 'mNLN-U0276': ('LEDGER_CAMERA_M3_NOT_CAMERA', 'GRAPHIC_TEXT', 'NOT_CAMERA', 'HIGH', 'All change above threshold lies in the x707-1277 y948-1079 text crop: the word Wrong leaves. Ledger CAMERA class not supported.'),
 'GNaB-U0055': ('LEDGER_CAMERA_M3_NOT_CAMERA', 'MIXED', 'CAMERA_VS_SLIDE_UNRESOLVED', 'MED', 'Blurred background shifts strongly, body tiles 0-3 px with limbs repositioned. A tracking move and a background scroll look the same here, so NOT_CAMERA is too strong.'),
 'GNaB-U0061': ('LEDGER_CAMERA_M3_NOT_CAMERA', 'INTRA_SHOT_STATE', 'CAMERA_VS_SLIDE_UNRESOLVED', 'MED', 'Blurred background drifts, body at most 2 px, f3565 is a hard cut. NOT_CAMERA is too strong; a whole-frame camera move is not supported.'),
}
rows = []; mlabel = {}
for v in V:
    for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{v}_v2.csv')):
        mlabel.setdefault(v, []).append(r['camera_m3']); i = r['interval_id']
        base = dict(video=v, interval_id=i, start_frame=r['start_frame'], end_frame=r['end_frame'], ledger_final_class=r['final_event_class'], ledger_final_attribution=r['final_camera_attribution'], final_basis=r['final_basis'], camera_m3=r['camera_m3'])
        if i in ADJ:
            s, c, a, conf, e = ADJ[i]; rows.append(dict(base, scope=s, n19_class=c, n19_attribution=a, confidence=conf, native_inspected='yes', evidence=e))
        elif r['camera_m3'] == 'OBJECT_MOVE' and r['final_basis'] not in NATIVE_BASIS:
            rows.append(dict(base, scope='OBJECT_MOVE_ATTRIBUTION', n19_class=r['final_event_class'], n19_attribution='CAMERA_NOT_ESTABLISHED', confidence='N/A', native_inspected='no', evidence='Ledger NOT_CAMERA came from M3 OBJECT_MOVE, which matched 4/6 on the held-out sample and was declared not validated. Only the attribution wording is corrected; the row was not re-inspected.'))
assert sum(r['native_inspected'] == 'yes' for r in rows) == 11
F = list(rows[0]); F = ['scope', 'video', 'interval_id', 'start_frame', 'end_frame', 'ledger_final_class', 'ledger_final_attribution', 'final_basis', 'camera_m3', 'n19_class', 'n19_attribution', 'confidence', 'native_inspected', 'evidence']
with open(M / 'CAMERA_RECONCILIATION_N19.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=F); w.writeheader(); w.writerows(rows)
print('rows', len(rows), {s: sum(r['scope'] == s for r in rows) for s in {r['scope'] for r in rows}})
NE = {'WHOLE_CONTENT_MOVE', 'OBJECT_MOVE', 'UNRESOLVED', 'UNRESOLVED_PARTIAL', 'UNRESOLVED_OSCILLATION'}
print('M3 label counts vs audit v3 "camera not established"', {v: (sum(x in NE for x in mlabel[v]), sum(x == 'OBJECT_MOVE' for x in mlabel[v])) for v in V})

m = json.loads((P / 'TRANSFER_MANIFEST_v2.json').read_text())
for i in m['package_items']:
    assert h(i['local_path']) == i['sha256'], i['local_path']
m['schema'] = 'BE_TRANSFER_MANIFEST_v3'; m['supersedes'] = 'TRANSFER_MANIFEST_v2.json'; m['built_session'] = '15f69c1b N19'
m['git_portable']['base_commit'] = sys.argv[1]; m['git_portable']['note'] = 'use the branch head at or after this commit'
for x in sorted((N / 'style_rt/source_calibration_local_only').glob('src_*.mp4')):
    m['package_items'].append(dict(kind='CALIBRATION_EXTRACT', local_path=str(x), package_path='style_rt/source_calibration_local_only/' + x.name, bytes=x.stat().st_size, sha256=h(x), required_for='SOURCE_CALIBRATION results cite these exact extracts; packaged so they are byte-verified, not regenerated'))
m['package_bytes'] = sum(i['bytes'] for i in m['package_items'])
for d in m['dependencies_not_packaged']:
    if d.get('path') == '/Library/Fonts/Bradley Hand Bold.ttf':
        d.update(kind='SYSTEM_FONT_MUST_BE_ABSENT', note='Not a missing dependency. RT-V2-S02/render.py prefers this path and falls back to Noteworthy.ttc. The published rt.mp4 used the fallback: it re-renders byte-identically on Machine A with this path absent. If this file exists on a target Mac, RT-V2-S02 renders differently.')
    if d.get('path') and d.get('sha256'):
        assert h(d['path']) == d['sha256'], d['path']
    if d.get('kind') == 'KNOWN_HARDCODED_PATH':
        d['note'] = 'absolute /Users/ghilmankhan/... path in variable D; set D to the render folder before re-rendering. The N19 re-render did this in a scratch copy.'
m['regenerable_not_packaged'] = 'frames, strips, contact sheets, crop sheets, QC images, ASR WAVs: regenerable from SOURCE_MP4 with the published scripts'
m['procedure'] = m['procedure'].replace('scripts/stage_and_verify.sh', 'scripts/stage_and_verify_v3.sh')
(P / 'TRANSFER_MANIFEST_v3.json').write_text(json.dumps(m, indent=1))
(P / 'TRANSFER_SHA256SUMS_v3.txt').write_text(''.join(f"{i['sha256']}  {i['package_path']}\n" for i in m['package_items']))
s = (N / 'scripts/stage_and_verify.sh').read_text().replace('TRANSFER_MANIFEST_v2.json', 'TRANSFER_MANIFEST_v3.json').replace('TRANSFER_SHA256SUMS.txt', 'TRANSFER_SHA256SUMS_v3.txt').replace('stage_and_verify.sh', 'stage_and_verify_v3.sh')
s = s.replace('cp "$M" "$N/portability/TRANSFER_SHA256SUMS_v3.txt" "$T/"', 'cp -f "$M" "$N/portability/TRANSFER_SHA256SUMS_v3.txt" "$T/"')
(N / 'scripts/stage_and_verify_v3.sh').write_text(s); (N / 'scripts/stage_and_verify_v3.sh').chmod(0o755)
print('package items', len(m['package_items']), 'bytes', m['package_bytes'])
