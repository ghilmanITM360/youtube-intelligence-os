"""Reconcile (2026-11-23, continuation): rebuild 03_CHANNEL_MASTER_INVENTORY.csv from ALL evidence now on disk, keeping v1 (saved as 03_CHANNEL_MASTER_INVENTORY_v1_2026-11-23T1043.csv).
Layers are joined by logical video ID; media identity by SHA-256 (media_probe_88.csv == census local_sha256 for 88/88). Different encodes of one video are ONE logical ID.
Status axes are kept apart: machine_measured / sampled_and_viewed / deep_visual. A video is never raised in tier merely because it was processed automatically.
Read-only on the repo. Run: python3 -I scripts/reconcile_v2.py"""
import csv, json, os, re, shutil, collections
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RP = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/'
V = RP + 'research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/'
v1 = A + '/03_CHANNEL_MASTER_INVENTORY_v1_2026-11-23T1043.csv'
if not os.path.exists(v1): shutil.copy(A + '/03_CHANNEL_MASTER_INVENTORY.csv', v1)
old = list(csv.DictReader(open(v1)))
cen = {r['video_id']: r for r in csv.DictReader(open(V + 'census/census.csv'))}
asrv = collections.defaultdict(list)
for r in csv.DictReader(open(A + '/03_ASR_VALIDATION.csv')): asrv[r['video_id']].append(r)
live = json.load(open(A + '/live_channel_ids_2026-11-23.json')); livefmt = {**{v: 'LONG' for v in live['long']}, **{v: 'SHORT' for v in live['shorts']}}
arch = json.load(open(A + '/what_if_xkcd_archive_2026-11-23.json'))['articles']
inv = {i['id']: i for i in json.load(open(RP + 'research/what-if-scripts/analysis/inventory.json'))}
def cnt(path, key='video_id'):
    c = collections.Counter()
    if os.path.exists(path):
        for r in csv.DictReader(open(path)): c[r[key]] += 1
    return c
rr = cnt(A + '/ct_scan_batch/run_review/REVIEWED_RUNS.csv') + cnt(A + '/ct_scan_batch/run_review/scat_REVIEWED_RUNS.csv')
small = cnt(A + '/ledgers_measured/SMALL_ADDITIONS_ALL.csv'); rs = cnt(A + '/review_sample/REVIEWED_SAMPLE.csv')
p7 = collections.Counter()
for f in ('07_SAMPLE_FRAMES.csv', '07_HOLDOUT_FRAMES.csv', '07b_SAMPLE_FRAMES.csv', '07c_SAMPLE_FRAMES.csv'):
    p7 += cnt(A + '/' + f)
brain = {r['video_id'] for r in csv.DictReader(open(A + '/06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv'))}
STOP = set('the a an of to in on is if what would how could can you your we and or for at by with from it its as be do does did are was were that this'.split())
def tk(s): return [w[:-1] if w.endswith('s') and len(w) > 3 else w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP]
def art_candidates(vid, title):
    """Returns (strength, [articles]). TITLE = every content word of the article title occurs in the video title (still only a candidate, never a verified link).
    WEAK_BODY = the words occur in video title + first 140 script words; often wrong (checked by eye: e.g. 'Lava Lamp' for the last-light video), so it is reported as WEAK only."""
    tt = set(tk(title)); body = set(tt)
    if vid in inv:
        try: body |= set(tk(' '.join((open(RP + 'research/what-if-scripts/' + inv[vid]['script']).read().split('## Script\n', 1)[1]).split()[:140])))
        except Exception: pass
    for strength, pool in (('TITLE', tt), ('WEAK_BODY', body)):
        out = [a for a in arch if len([w for w in tk(a['title']) if len(w) > 2]) >= 2 and all(w in pool for w in tk(a['title']) if len(w) > 2)]
        if out: return strength, out
    return '', []
rows = []
for r in old:
    v = r['video_id']; n = dict(r); c = cen.get(v, {})
    n['visual_tier_v1'] = r['visual_tier']
    # transcript / ASR
    has_cat = r['catalog_transcript'] != 'NONE'; av = asrv.get(v, [])
    srcs = sorted({a['asr_source'] for a in av})
    n['asr_status_v2'] = ('ASR_PROVISIONAL_IDENTITY_CONFIRMED_VS_CATALOG' if has_cat and av else 'ASR_PROVISIONAL_NO_CATALOG_TEXT_DURATION_OK' if av else 'NONE')
    n['asr_sources'] = ';'.join(srcs)
    n['asr_identity_note'] = ''
    if av and not has_cat:
        a = av[0]; n['asr_identity_note'] = f"asr_end/media={a['end_over_dur']}; best 8-gram containment {a['best_8g_containment_in_catalog']} in {a['best_8g_video']}"
    n['transcript_status_v2'] = 'CATALOG_UNTIMED' if has_cat else ('ASR_ONLY_PROVISIONAL' if av else 'NONE')
    n['any_transcript_v2'] = 'YES' if (has_cat or av) else 'NO'
    n['exact_transcript_note'] = ('catalog: ' + r['caption_type']) if has_cat else ''
    # layers
    camp = os.path.exists(f'{V}videos/{v}/shot_ledger.csv'); aud = os.path.exists(f'{A}/ledgers_measured/{v}/shot_ledger.csv')
    ct = os.path.exists(f'{A}/ct_scan_batch/{v}/summary.json')
    n['layer_campaign_ledger'] = 'YES' if camp else 'NO'; n['layer_audit_measured_ledger'] = 'YES' if aud else 'NO'; n['layer_ct_machine_scan'] = 'YES' if ct else 'NO'
    n['layer_brain_encode'] = 'YES (different encode; 0/14 hash match)' if v in brain else 'NO'
    n['viewed_hold_runs'] = rr.get(v, 0); n['viewed_small_additions'] = small.get(v, 0); n['viewed_review_sample_shots'] = rs.get(v, 0); n['viewed_science_frames'] = p7.get(v, 0)
    pilot = v == '9VG0yqq_PHM'
    n['machine_measured'] = '+'.join(x for x, ok in (('campaign_ledger', camp), ('audit_ledger', aud), ('ct_all_frames', ct)) if ok) or 'none'
    sv = [f'{n["viewed_science_frames"]} frame(s)' if n['viewed_science_frames'] else '', f'{n["viewed_review_sample_shots"]} shot(s)' if n['viewed_review_sample_shots'] else '', f'{n["viewed_hold_runs"]} residual run(s)' if n['viewed_hold_runs'] else '']
    n['sampled_and_viewed'] = '; '.join(x for x in sv if x) or 'none'
    n['deep_visual_review'] = 'VISUAL_ONLY_ALL_3893_FRAMES_VIEWED_ONE_CODER_NO_AUDIO' if pilot else 'NO'
    # tier v2 (directive scale). Rule: DEEP only where every native frame was viewed; TARGETED where a model reviewer classified segments (campaign gate);
    # STRUCTURAL where shot/event measurement exists; TRANSCRIPT_ONLY if only text; else MEDIA_ONLY. Processing alone never raises the tier above STRUCTURAL.
    media = r['local_media_status'] != 'MISSING'
    if not media: t = 'UNAVAILABLE'
    elif pilot: t = 'DEEP_VISUAL (visual-only; one coder; no audio; sub-15px not examined)'
    elif camp and r['per_video_gate']: t = 'TARGETED_VISUAL'
    elif camp or aud or ct: t = 'STRUCTURAL_ONLY'
    elif r['any_transcript_v2'] if False else (has_cat or av): t = 'TRANSCRIPT_ONLY'
    else: t = 'MEDIA_ONLY_NO_ANALYSIS'
    n['visual_tier_v2'] = t
    # phase 4 fields
    res = r['res']; n['aspect_ratio'] = '16:9' if res == '1920x1080' else '9:16' if res == '1080x1920' else ('UNKNOWN' if not res else res)
    n['format_live_2026_11_23'] = livefmt.get(v, 'NOT_LISTED')
    n['live_listed_2026_11_23'] = 'YES' if v in livefmt else 'NO'
    n['metadata_observed_utc'] = c.get('snapshot_utc', '') or '2026-11-23 (RSS only)'
    n['views_note'] = 'views_2026_11_04 is a historical census value, not current'
    n['audio_available'] = ('YES (aac stream; never listened)' if r['has_audio'] == 'True' else 'UNKNOWN' if not media else 'NO')
    st_, cands = art_candidates(v, r['title']); n['article_correspondence'] = (f'CANDIDATE_{st_} (not verified): ' + '; '.join(f"#{a['n']} {a['title']}" for a in cands[:3])) if cands else 'UNKNOWN (no match found; not verified)'
    n['source_legal_status'] = 'OWNER_HELD_LOCAL_COPY_FOR_ANALYSIS; third-party copyright; reference only' if media else 'NOT_AVAILABLE_LOCALLY'
    n['classification_v2'] = ('FULL_MEDIA_AVAILABLE' if media else 'MISSING')
    rows.append(n)
w = csv.DictWriter(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
C = collections.Counter
print(len(rows), C(r['visual_tier_v2'].split(' ')[0] for r in rows), C(r['transcript_status_v2'] for r in rows), C(r['asr_status_v2'] for r in rows))
print('layers camp/aud/ct/brain', *(sum(r[k].startswith('YES') for r in rows) for k in ('layer_campaign_ledger', 'layer_audit_measured_ledger', 'layer_ct_machine_scan', 'layer_brain_encode')))
print('camp&aud', sum(r['layer_campaign_ledger'] == 'YES' and r['layer_audit_measured_ledger'] == 'YES' for r in rows), 'neither', sum(r['layer_campaign_ledger'] == 'NO' and r['layer_audit_measured_ledger'] == 'NO' and r['local_media_status'] != 'MISSING' for r in rows))
print('article candidates', sum(r['article_correspondence'].startswith('CANDIDATE') for r in rows), 'live listed', sum(r['live_listed_2026_11_23'] == 'YES' for r in rows))
print('viewed runs videos', sum(r['viewed_hold_runs'] > 0 for r in rows), 'sci frames videos', sum(r['viewed_science_frames'] > 0 for r in rows), 'review sample videos', sum(r['viewed_review_sample_shots'] > 0 for r in rows))
print(C((r['format'], r['visual_tier_v2'].split(' ')[0]) for r in rows))
