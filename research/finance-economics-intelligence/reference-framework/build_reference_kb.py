"""Rebuild the reference knowledge tables from versioned sources.
Usage: python build_reference_kb.py <db> [--fresh]   (--fresh applies schemas/inventory/*.sql to an empty db first)
Raw text lives only in corpus/REFERENCE_SECTIONS_v1.jsonl.gz (canonical members); alias members keep hashes only."""
import csv, gzip, hashlib, json, pathlib, sqlite3, sys
H = pathlib.Path(__file__).resolve().parent; ROOT = H.parents[2]; FV = 'v1'
CLASS = {'CREATIVE_GUIDANCE': 'CREATIVE_HEURISTIC', 'DESCRIPTIVE_LENS': 'CREATIVE_HEURISTIC', 'NOT_APPLICABLE': 'NOT_APPLICABLE'}
OVERRIDE = {'FR-16C-03': 'DUPLICATED_OR_SUPERSEDED', 'FR-16C-04': 'DUPLICATED_OR_SUPERSEDED', 'FR-16C-06': 'EMPIRICAL_HYPOTHESIS'}
CONFLICTS = [('FR-16C-03', 'FR-BT-01', 'OVERLAP', 'Same BUT/THEREFORE substance restated by the 16 Commandments assistant document.'),
             ('FR-16C-04', 'FR-SCR-03', 'OVERLAP', 'Promise delivery restated; count once.'),
             ('FR-16C-06', 'FR-BT-01', 'DIFFERENT_SCALE', '20-30 second reset (beat scale) and 2-3 minute micro-arc (scene scale) are different scales; not contradictory without context.')]
def build(db, fresh=False):
    con = sqlite3.connect(db); con.execute('PRAGMA foreign_keys=ON')
    if fresh:
        for p in sorted((ROOT / 'schemas/inventory').glob('*.sql')): con.executescript(p.read_text())
    elif con.execute("select count(*) from schema_meta where schema_version=11").fetchone()[0] == 0:
        con.executescript((ROOT / 'schemas/inventory/011_reference_knowledge.sql').read_text())
    for t in ('ref_section_fts', 'ref_plan_application', 'ref_video_assessment', 'ref_analysis_run', 'ref_platform_verification', 'ref_rule_conflict', 'ref_rule', 'ref_constituent_video', 'ref_section'):
        if t == 'ref_section_fts': con.execute("INSERT INTO ref_section_fts(ref_section_fts) VALUES('delete-all')")
        else: con.execute(f'DELETE FROM {t}') if t not in ('ref_video_assessment', 'ref_plan_application', 'ref_analysis_run') else None
    con.execute('DELETE FROM ref_source_member')
    reg = list(csv.DictReader(open(H / 'REFERENCE_ARCHIVE_REGISTER_v1.csv')))
    mid = {r['Member']: 'RM-' + r['SHA256'][:12] for r in reg}
    secs = [json.loads(l) for l in gzip.open(H / 'corpus/REFERENCE_SECTIONS_v1.jsonl.gz', 'rt', encoding='utf8')]
    n = {}; unread = set()
    for s in secs:
        n[s['member']] = n.get(s['member'], 0) + 1
        if s['status'].endswith('IMAGES_UNREAD') or s['status'] == 'IMAGE_ONLY_UNRESOLVED': unread.add(s['member'])
    alias = {s['member']: s['alias_of'] for s in secs if s.get('alias_of')}
    for r in reg:
        m = r['Member']; disp = 'PROCESSED_ALIAS' if m in alias else ('PROCESSED_WITH_UNREAD_IMAGES' if m in unread else 'PROCESSED_CANONICAL')
        con.execute('INSERT INTO ref_source_member VALUES (?,?,?,?,?,?,?,?,?,?,?)', (mid[m], m, r['SHA256'], int(r['Bytes']), n[m], None, r['Existing_SRC_ID_DS000011'] or None, None, r['Duplicate_Group'] or None, disp, r['Extraction_Note']))
    for m, a in alias.items(): con.execute('UPDATE ref_source_member SET canonical_member_id=? WHERE member_id=?', (mid[a], mid[m]))
    for s in secs:
        con.execute('INSERT INTO ref_section (section_id, member_id, locator, ordinal, extraction_status, char_count, image_count, text_sha256, raw_text) VALUES (?,?,?,?,?,?,?,?,?)',
                    (f"{mid[s['member']]}:{s['locator']}", mid[s['member']], s['locator'], s['ordinal'], s['status'], s['chars'], s['images'], s['text_sha256'], s['text']))
    con.execute("INSERT INTO ref_section_fts(rowid, raw_text) SELECT rowid, raw_text FROM ref_section WHERE raw_text IS NOT NULL")
    for c in json.load(open(H / 'ALGO_UPDATE_CONSTITUENT_INDEX_v2.json')):
        con.execute('INSERT INTO ref_constituent_video VALUES (?,?,?,?,?,?)', (f"CV-{c['n']:03d}", mid['2026 Algorithm Update.docx'], c['n'], c['title'], c['start_line'], c['end_line']))
    for r in csv.DictReader(open(H / 'REFERENCE_RULE_INDEX_v1.csv')):
        con.execute('INSERT INTO ref_rule VALUES (?,?,?,?,?,?,?,?,?)', (r['Rule_ID'], FV, mid.get(r['Source_Member']), r['Locator'], r['Meaning'], r['Audit_Dimension'], OVERRIDE.get(r['Rule_ID'], CLASS[r['Rule_Kind']]), r['Evidence_Required'], r['Applicability_Limits']))
    for i, (a, b, rel, note) in enumerate(CONFLICTS, 1): con.execute('INSERT INTO ref_rule_conflict VALUES (?,?,?,?,?,?)', (f'RC-{i:02d}', a, b, FV, rel, note))
    for r in csv.DictReader(open(H / 'REFERENCE_ALGORITHM_CLAIM_VERIFICATION_v1.csv')):
        con.execute('INSERT INTO ref_platform_verification VALUES (?,?,?,?,?,?,?,?,?)', (r['Claim_ID'], None, r['Locator'], r['Assertion'], r['Official_Evidence_URL'], r['Verdict'], r['Evidence_Note'], r['Audit_Use'], r['Accessed']))
    load_assessments(con)
    con.commit(); return con
def load_assessments(con):
    led = H.parent / 'reanalysis'; fz = json.load(open(led / 'REANALYSIS_POPULATION_v1.json'))
    con.execute('DELETE FROM ref_video_assessment'); con.execute('DELETE FROM ref_analysis_run')
    con.execute('INSERT INTO ref_analysis_run VALUES (?,?,?,?,?,?)', ('RUN-REANALYSIS-v1', FV, fz['population_sha256'], fz['baseline_commit'], fz['frozen_utc'], 'Historical reanalysis; one row per video-rule judgment'))
    for f in sorted((led / 'videos').glob('*.json')):
        d = json.load(open(f))
        for i, c in enumerate(d['comparisons']):
            w = c.get('witness') or {}
            con.execute('INSERT INTO ref_video_assessment VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (f"{d['video_id']}:{c['rule_id']}:{i}", 'RUN-REANALYSIS-v1', d['video_id'], c['rule_id'], FV, c['judgment'], w.get('kind'), w.get('start_char'), w.get('end_char'), w.get('text'), c['rationale'], c['uncertainty']))
def search(con, q, k=5):
    return con.execute("SELECT s.section_id, s.locator, snippet(ref_section_fts,0,'[',']','…',12) FROM ref_section_fts f JOIN ref_section s ON s.rowid=f.rowid WHERE ref_section_fts MATCH ? ORDER BY rank LIMIT ?", (q, k)).fetchall()
if __name__ == '__main__':
    con = build(sys.argv[1], '--fresh' in sys.argv)
    for t in ('ref_source_member', 'ref_section', 'ref_constituent_video', 'ref_rule', 'ref_rule_conflict', 'ref_platform_verification', 'ref_video_assessment'): print(t, con.execute(f'select count(*) from {t}').fetchone()[0])
    print(con.execute('PRAGMA foreign_key_check').fetchall(), con.execute('PRAGMA integrity_check').fetchone())
