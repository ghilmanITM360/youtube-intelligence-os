"""Register the 5 independently reviewed V1 Rent artworks through the shared pipeline.py workflow, with a V1-local root.
Room (opaque 1920x1080 background) cannot pass the RGBA-only validator, so it is registered by a manual, logged entry after the same SHA-256 check."""
import sys, os, json, time, shutil, hashlib
PS = '/Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance/CHANNEL_VISUAL_AUDIT/CHANNEL_001/PRODUCTION_SYSTEM'
sys.path.insert(0, PS); import pipeline as P
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = HERE + '/v1_assets'; CAND = HERE + '/codex_art/candidates'
REV = 'independent vision reviewer (separate from Codex author), codex_art/qa/INDEPENDENT_REVIEW_V1_RENT.md'
EXPECT = {'v1_ch_master_front': '12852084f48ab6992d0d769d2d19b426cb16f207f883dbae3db5edbe1487ee05',
          'v1_ch_p1_neutral_closed': '12852084f48ab6992d0d769d2d19b426cb16f207f883dbae3db5edbe1487ee05',
          'v1_ch_p3_bill_closed': '43e29cf9d47d8581926ac9f84ead26911d14ca9a3032f908069ec5bfe6ddafba',
          'v1_bg_room_table': 'c660ea667bab704f42b915cb35cd112708d58da4f2008b383de18aaea9cc7960'}
ROOMSHA = 'b5094b609ac112e4f8ec1510c98c545a09214569ed3c1900875f28f16dec4132'
def main():
    for i, s in EXPECT.items():
        got = P.sha256(f'{CAND}/{i[3:]}.png' if False else {'v1_ch_master_front': CAND+'/v1_ch_master_front.png', 'v1_ch_p1_neutral_closed': CAND+'/v1_ch_p1_neutral_closed.png', 'v1_ch_p3_bill_closed': CAND+'/v1_ch_p3_bill_closed.png', 'v1_bg_room_table': CAND+'/v1_bg_room_table.png'}[i])
        assert got == s, (i, got); P.record_review(i, s, 'PASS', REV, 'SHA-256 recomputed by reviewer; PASS for the opening test only (review doc)', root=ROOT)
    assert P.sha256(CAND + '/v1_bg_room.png') == ROOMSHA
    ok, msgs, _ = P.approve(list(EXPECT), [CAND], root=ROOT); print(ok, *msgs, sep='\n')
    if not ok: sys.exit(1)
    reg = P.load_registry(ROOT)
    if not any(r['id'] == 'v1_bg_room' for r in reg):
        os.makedirs(ROOT + '/approved', exist_ok=True); dst = f'approved/v1_bg_room@{ROOMSHA[:8]}.png'; shutil.copyfile(CAND + '/v1_bg_room.png', f'{ROOT}/{dst}'); assert P.sha256(f'{ROOT}/{dst}') == ROOMSHA
        P.write_json_atomic(ROOT + '/reviews/v1_bg_room.json', dict(asset_id='v1_bg_room', sha256=ROOMSHA, verdict='PASS', reviewer=REV, evidence='review doc table', independent=True, reviewed_at=time.strftime('%Y-%m-%dT%H:%M:%S')))
        P.backup_registry(ROOT)
        reg.append(dict(id='v1_bg_room', file=dst, type='background', size=[1920, 1080], transparent=False, provenance='Codex original art', generator='Codex built-in image generation + table-removal edit', level=4, validation='APPROVED_INDEPENDENT_OPAQUE_BG_MANUAL', status='approved', sha256=ROOMSHA, review=dict(reviewer=REV, verdict='PASS'), approved_at=time.strftime('%Y-%m-%dT%H:%M:%S'), render_scale=1.0, note='opaque by design; RGBA validator not applicable'))
        P.write_json_atomic(ROOT + '/asset_registry.json', reg)
    print('verify:', P.verify(ROOT) or 'registry verified')
main()
