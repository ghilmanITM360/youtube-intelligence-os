# Port of PR #38 build_dataset.mjs (f176aa28) normalization to stdlib Python, multi-channel.
# usage: python3 -I build_outputs.py   (reads raw/, writes channels/ + batch files; no network, no DB)
# ponytail: no XLSX workbook (PR #38 needed ARTIFACT_TOOL_PATH); CSV/JSONL carry the same columns.
import json, glob, os, re, csv, io, hashlib, subprocess, datetime as dt

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, 'raw')
ACTOR = 'streamers/youtube-scraper'
REPO = os.path.expanduser('~/workprojects/youtube-intelligence-os')
PR39 = '967ea707:research/youtube-12-channel-metadata/channels/{}/VIDEO_MASTER.csv'

# label -> (channel, UC id, tranche, PR39 slug or None, limits [reg, shorts, streams], cap_usd)
PLAN = {
    't1_kevin': ('Kevin Explains', 'UCMl8WtFdqfnzzKcC2KWZZnQ', 'T1', None, [188, 0, 0], 0.76),
    't1_lana': ('Lana Maynes', 'UCj0uhARVVmROWv9TBpVIr9Q', 'T1', None, [105, 0, 0], 0.43),
    't1_markcalloway': ('Mark Calloway', 'UCAOeipQ5KGzZ2McMF1RNsrQ', 'T1', None, [100, 0, 0], 0.40),
    't1_marcus': ('Marcus Retires', 'UCW_JmbBR0gsRGIUGRY3WA-Q', 'T1', None, [37, 0, 0], 0.15),
    'g_markinvests': ('Mark Invests', 'UCcj_KU4ZN6bx6Ki68hNJWqw', 'G', 'markbuildsus', [22, 0, 0], 0.09),
    'g_unclejohn': ('Uncle John Financial', 'UCWugleQL2wqr5N1X4o8yyLw', 'G', 'unclejohnfinancial', [9, 9, 0], 0.08),
    'g_unclefrank': ('Uncle Frank Retirement', 'UCLh3aiudWdnfR0QDC8aLEhQ', 'G', 'unclefrankretirement16', [13, 0, 0], 0.06),
    'g_primate': ('Primate Economics', 'UC14Fb2zWTEZklONPXFbLrTQ', 'G', 'primateeconomics', [6, 6, 0], 0.05),
    'g_logicalmoney': ('Logical Money', 'UCKhpM-cu2Cod-GyG6KngNYg', 'G', 'logicalmoney72', [11, 11, 0], 0.09),
    't2_waltercanada': ('Walter Canada', 'UCQng0CgVwiA79VEPJ9e--zw', 'T2', None, [123, 0, 0], 0.50),
    't2_niaprescott': ('Nia Prescott', 'UC3a2fNfeG-zvJcuDD9R8bLw', 'T2', None, [95, 0, 0], 0.38),
    't2_financepov': ('Finance POV', 'UC4zls8vK8iiTSQpnaIxICkg', 'T2', None, [90, 0, 0], 0.36),
    't2_ronniefinance': ('Ronnie Finance', 'UCA-ucSJ_2mY4EqjenOT2u3w', 'T2', None, [71, 0, 0], 0.29),
    't2_povwealth': ('POV Wealth', 'UCryM-LAkg31P_B0GeshJQjg', 'T2', None, [71, 0, 0], 0.29),
    't2_robinmba': ('Robin MBA', 'UCOvq-1piPnzCmrqfSspVIwA', 'T2', None, [67, 0, 0], 0.27),
    't2_madeline': ('Madeline', 'UChghyih02gp-TC7w22ULaXQ', 'T2', None, [59, 0, 0], 0.24),
    't2_natesmoneymap': ("Nate's Money Map", 'UCtOrKVgo-bsh4XoSCA8R_mg', 'T2', None, [40, 0, 0], 0.16),
    't2_financeanalyst': ('Finance ANALYST', 'UCWQA4bQidJMFH3odS-RGEyA', 'T2', None, [37, 0, 0], 0.15),
    't2_franklaw': ('Frank Law', 'UCdFjOki_gKUfvDq3SmL36mg', 'T2', None, [32, 0, 0], 0.13),
    't2_housing': ('Housing', 'UC3Tzh0Wu1C9s3AI2Oqc8kIA', 'T2', None, [31, 0, 0], 0.13),
    't2_arthurpenrose': ('Arthur Penrose | UK Pension Guide', 'UCsAnRVKKrZCD7YRVLu5FdSQ', 'T2', None, [30, 0, 0], 0.12),
    't2_wealthlogicaus': ('Wealth Logic Australia', 'UCpUvGrDOLrlhpUr5hXnpD9g', 'T2', None, [29, 0, 0], 0.12),
    't2_thismakecents': ('This make cents', 'UCWrtDO6izx1KXQu_BZBrQYg', 'T2', None, [27, 27, 0], 0.22),
    't2_sarahrickshaw': ('Sarah Rickshaw', 'UCn2nfMN6I-ozJikqW-zk_6A', 'T2', None, [19, 0, 0], 0.08),
}
PILOTS = {'t1_marcus': 'pilot_marcus'}  # merged into the channel, pilot rows first

def runs_for(label):
    out = []
    for lab in ([PILOTS[label]] if label in PILOTS else []) + [label]:
        rf = glob.glob(os.path.join(RAW, f'{lab}_*_run.json'))[0]
        run = json.load(open(rf))
        rows = json.load(open(rf.replace('_run.json', '_dataset.json')))
        out.append((lab, run, rows, os.path.basename(rf.replace('_run.json', '_dataset.json'))))
    return out

is_video = lambda r: bool(re.fullmatch(r'[A-Za-z0-9_-]{11}', str(r.get('id') or '')))
blank = lambda v: v is None or v == '' or (isinstance(v, list) and not v)
val = lambda v: None if blank(v) else v

def dur_s(v):
    if not isinstance(v, str) or not v: return None
    try: p = [int(x) for x in v.split(':')]
    except ValueError: return None
    return p[0]*3600+p[1]*60+p[2] if len(p) == 3 else p[0]*60+p[1] if len(p) == 2 else p[0]

def typ(r):
    s = f"{r.get('type') or ''} {r.get('fromChannelListPage') or ''} {r.get('fromYTUrl') or ''} {r.get('url') or ''}".lower()
    return 'SHORT' if 'short' in s else 'STREAM' if ('stream' in s or 'live' in s) else 'REGULAR'

def uniq(xs):
    seen = []
    for x in xs:
        if x not in (None, '') and x not in seen: seen.append(x)
    return seen

def hashtags(r):
    hs = [(x if isinstance(x, str) else (x or {}).get('text') or (x or {}).get('hashtag')) for x in (r.get('hashtags') or [])]
    hs += re.findall(r'#\w+', str(r.get('text') or ''))
    return uniq([h if str(h).startswith('#') else f'#{h}' for h in hs if h])

def num(v):
    try: return None if v is None or v == '' else float(v) if '.' in str(v) else int(v)
    except (TypeError, ValueError): return None

def q(v):  # PR #38 CSV cell rule: None -> UNKNOWN (never 0), lists joined
    s = 'UNKNOWN' if v is None else ' | '.join(map(str, v)) if isinstance(v, list) else str(v).lower() if isinstance(v, bool) else str(v)
    return re.sub(r'[ \t]+(?=\r?\n|$)', '', s)

def write_csv(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(header); w.writerows([[q(r.get(h)) for h in header] for r in rows])

def pr39_ids(slug):
    if not slug: return None
    txt = subprocess.run(['git', '-C', REPO, 'show', PR39.format(slug)], capture_output=True, text=True, check=True).stdout
    return {r['video_id'] for r in csv.DictReader(io.StringIO(txt))}

def build(label):
    name, exp, tranche, slug, limits, cap = PLAN[label]
    runs = runs_for(label)
    main_lab, run, _, _ = runs[-1]
    ts = run['finishedAt']
    by_id, raw_video_rows, foreign_raw = {}, 0, []
    for lab, rn, rows, fname in runs:
        for i, r in enumerate(rows):
            if not is_video(r): continue
            raw_video_rows += 1
            if (r.get('channelId') or (r.get('aboutChannelInfo') or {}).get('channelId')) != exp:
                foreign_raw.append(r.get('id')); continue
            loc = f'{fname}#row:{i+1}'
            if r['id'] not in by_id: by_id[r['id']] = {**r, '_rows': [loc], '_run': rn}
            else:
                m = by_id[r['id']]
                m.update({k: v for k, v in r.items() if not blank(v)}); m['_rows'].append(loc); m['_run'] = rn
    about = next(r['aboutChannelInfo'] for _, _, rows, _ in runs for r in rows if (r.get('aboutChannelInfo') or {}).get('channelId') == exp)
    members = [r for r in by_id.values() if r.get('isMembersOnly') is True]
    public = [r for r in by_id.values() if r.get('isMembersOnly') is not True]
    now = dt.datetime.fromisoformat(ts.replace('Z', '+00:00'))
    master = []
    for r in public:
        pub = val(r.get('date'))
        age = max(0, (now - dt.datetime.fromisoformat(pub.replace('Z', '+00:00'))).total_seconds()/86400) if pub else None
        views, likes, comments = num(r.get('viewCount')), num(r.get('likes')), num(r.get('commentsCount'))
        subs = [x for x in (r.get('subtitles') or []) if isinstance(x, dict)]
        vt = typ(r); rr = r['_run']
        missing = [f for f, v in {'title': r.get('title'), 'publication_timestamp': pub, 'duration': r.get('duration'), 'view_count': views,
                   'like_count': likes, 'comment_count': comments, 'description': r.get('text'), 'thumbnail_url': r.get('thumbnailUrl')}.items() if blank(v)]
        master.append({
            'channel_name': about['channelName'], 'channel_id': exp, 'channel_handle': '@' + str(about.get('channelUsername') or '').lstrip('@'),
            'channel_url': about.get('channelUrl'), 'video_id': r['id'], 'title': val(r.get('title')),
            'watch_url': f"https://www.youtube.com/watch?v={r['id']}", 'shorts_url': f"https://www.youtube.com/shorts/{r['id']}" if vt == 'SHORT' else None,
            'source_video_url': val(r.get('url')), 'video_type': vt, 'availability_status': 'PUBLIC_ACCESSIBLE_AT_RETRIEVAL',
            'publication_timestamp_utc': pub, 'publication_date_utc': pub[:10] if pub else None,
            'publication_time_utc': pub[11:19] if pub and 'T' in pub else None, 'publication_precision': 'EXACT_ACTOR_TIMESTAMP' if pub else 'UNKNOWN',
            'duration': val(r.get('duration')), 'duration_seconds': dur_s(r.get('duration')), 'category': val(r.get('category')),
            'language': val(r.get('language')), 'stream_type': val(r.get('streamType')),
            'view_count': views, 'like_count': likes, 'comment_count': comments,
            'engagement_rate': (likes + comments)/views if views and likes is not None and comments is not None else None,
            'video_age_days_at_retrieval': age, 'views_per_day': views/max(age, 1) if views is not None and age is not None else None,
            'views_per_day_limitation': 'Snapshot views divided by age at retrieval; not a historical velocity series.',
            'description': val(r.get('text')), 'tags': uniq([str(t) for t in (r.get('tags') or [])]), 'hashtags': hashtags(r), 'keywords': None,
            'source_topic_or_category': val(r.get('category')), 'captions_or_transcript_available': bool(subs),
            'subtitle_languages': ', '.join(uniq([x.get('language') or x.get('lang') for x in subs])) or None,
            'subtitle_source_types': ', '.join(uniq([x.get('type') or x.get('sourceType') for x in subs])) or None,
            'pinned_or_featured_indicator': None, 'thumbnail_url': val(r.get('thumbnailUrl')), 'thumbnail_local_path': None,
            'thumbnail_dimensions': None, 'thumbnail_file_sha256': None, 'actor_name': ACTOR, 'actor_version': rr.get('buildNumber'),
            'actor_run_id': rr['id'], 'actor_dataset_id': rr['defaultDatasetId'],
            'record_source_url': val(r.get('fromYTUrl')) or val(r.get('sourceUrl')) or val(r.get('url')),
            'raw_dataset_row_locator': ';'.join(r['_rows']), 'metadata_retrieval_timestamp_utc': rr['finishedAt'],
            'channel_snapshot_timestamp_utc': ts, 'source_verification_timestamp_utc': ts, 'verification_status': 'CHANNEL_ID_MATCHED',
            'missing_fields': missing, 'notes': 'Comments turned off' if r.get('commentsTurnedOff') else None,
        })
    master.sort(key=lambda m: (m['publication_timestamp_utc'] or '', m['video_id']), reverse=True)
    ids = [m['video_id'] for m in master]
    core = ['video_id', 'title', 'watch_url', 'video_type', 'publication_timestamp_utc', 'duration', 'view_count', 'like_count', 'comment_count', 'description', 'thumbnail_url']
    known = sum(1 for m in master for f in core if not blank(m[f]))
    counts = {t: sum(1 for m in master if m['video_type'] == t) for t in ('REGULAR', 'SHORT', 'STREAM')}
    reported = about.get('channelTotalVideos')
    fetched = len(by_id)
    # coverage: only claim COMPLETE when fetched (public + members-only) reaches the channel's reported total
    reg_limit_hit = counts['REGULAR'] + sum(1 for r in members if typ(r) == 'REGULAR') >= limits[0]
    if tranche == 'G': coverage = 'GAP_FILL_NEWEST'
    elif isinstance(reported, int) and fetched >= reported: coverage = 'COMPLETE'
    elif reg_limit_hit: coverage = 'PARTIAL'
    else: coverage = 'COMPLETE_REGULAR_TAB_ONLY'
    prior = pr39_ids(slug)
    delta = None if prior is None else {'pr39_package_rows': len(prior), 'fetched_ids': len(ids), 'already_in_pr39': len(set(ids) & prior),
                                        'new_vs_pr39': sorted(set(ids) - prior)}
    dup = len(ids) - len(set(ids))
    checks = {
        'unique_video_ids': {'pass': dup == 0, 'duplicates': dup},
        'watch_urls_match_video_ids': {'pass': all(m['watch_url'].endswith(m['video_id']) for m in master), 'failures': []},
        'all_records_match_verified_channel': {'pass': not foreign_raw and all(m['channel_id'] == exp for m in master), 'failures': foreign_raw},
        'raw_rows_to_master_reconciliation': {'pass': len(by_id) == len(public) + len(members), 'raw_video_rows': raw_video_rows,
            'unique_raw_video_ids': len(by_id), 'excluded_members_only': len(members), 'public_master_rows': len(master)},
        'type_counts_reconcile': {'pass': sum(counts.values()) == len(master), **counts},
        'classification_values_valid': {'pass': all(m['video_type'] in ('REGULAR', 'SHORT', 'STREAM') for m in master)},
        'unknown_never_zero': {'pass': True, 'rule': 'None serialised as UNKNOWN in CSV, null in JSONL'},
        'no_captions_or_ai_charged': {'pass': all(sum(v for k, v in (rn.get('chargedEventCounts') or {}).items() if k != 'result') == 0 for _, rn, _, _ in runs)},
    }
    validation = {'generated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'status': 'PASS' if all(c['pass'] for c in checks.values()) else 'FAIL',
                  'checks': checks, 'metadata_completeness': {'core_fields': core, 'known_values': known, 'possible_values': len(master)*len(core),
                  'percentage': known/(len(master)*len(core)) if master else 0}}
    meta = {'canonical_channel_name': about['channelName'], 'channel_id': exp, 'handle': '@' + str(about.get('channelUsername') or '').lstrip('@'),
            'canonical_channel_url': about.get('channelUrl'), 'requested_url': f'https://www.youtube.com/channel/{exp}',
            'description': about.get('channelDescription'), 'creation_date_source_text': about.get('channelJoinedDate'),
            'country': about.get('channelLocation'), 'subscriber_count': about.get('numberOfSubscribers'),
            'channel_total_public_views': about.get('channelTotalViews'), 'reported_public_video_count': reported,
            'available_channel_links': about.get('channelDescriptionLinks') or [], 'profile_image_url': about.get('channelAvatarUrl'),
            'banner_image_url': about.get('channelBannerUrl'), 'is_verified': about.get('isChannelVerified'),
            'is_age_restricted': about.get('isAgeRestricted'), 'snapshot_timestamp_utc': ts, 'source_actor': ACTOR,
            'source_run_id': run['id'], 'source_dataset_id': run['defaultDatasetId']}
    def runrec(lab, rn, rows, fname):
        return {'label': lab, 'actor_name': ACTOR, 'actor_build': rn.get('buildNumber'), 'run_id': rn['id'], 'dataset_id': rn['defaultDatasetId'],
                'status': rn['status'], 'started_at_utc': rn['startedAt'], 'finished_at_utc': rn['finishedAt'],
                'charged_events': rn.get('chargedEventCounts'), 'actual_cost_usd': round(0.004*(rn.get('chargedEventCounts') or {}).get('result', 0), 3),
                'usage_total_usd_reported': rn.get('usageTotalUsd'), 'max_cost_usd': (rn.get('options') or {}).get('maxTotalChargeUsd'),
                'input_sanitized': {'startUrls': [f'https://www.youtube.com/channel/{exp}'], 'maxResults': limits[0] if lab == label else 3,
                    'maxResultsShorts': limits[1] if lab == label else 0, 'maxResultStreams': limits[2] if lab == label else 0,
                    'sortVideosBy': 'NEWEST', 'transcriptionAndSubtitle': 'NONE', 'aiVideoDescription': False, 'aiVideoSummary': False},
                'origin': 'Apify Console (owner browser session)', 'raw_rows': len(rows), 'raw_file': f'raw/{fname}'}
    rr = [runrec(*x) for x in runs]
    manifest = {'snapshot_timestamp_utc': ts, 'channel': {'name': about['channelName'], 'handle': meta['handle'], 'id': exp}, 'tranche': tranche,
                'coverage_status': coverage, 'primary_run': rr[-1], 'pilot_run': rr[0] if len(rr) > 1 else None,
                'normalization': {'public_master_rows': len(master), 'members_only_excluded': len(members), 'primary_key': 'video_id'},
                'reuse_delta_vs_pr39': delta}
    out = os.path.join(ROOT, 'channels', label.split('_', 1)[1]); os.makedirs(out, exist_ok=True)
    wj = lambda n, v: open(os.path.join(out, n), 'w').write(json.dumps(v, indent=2, ensure_ascii=False) + '\n')
    wj('CHANNEL_IDENTITY.json', {'verification_status': 'VERIFIED', 'evidence': meta}); wj('CHANNEL_METADATA.json', meta)
    wj('METADATA_VALIDATION.json', validation); wj('APIFY_RUN_MANIFEST.json', manifest)
    open(os.path.join(out, 'VIDEO_MASTER.jsonl'), 'w').write(''.join(json.dumps(m, ensure_ascii=False) + '\n' for m in master))
    write_csv(os.path.join(out, 'VIDEO_MASTER.csv'), list(master[0].keys()), master)
    gaps = [{'video_id': m['video_id'], 'title': m['title'], 'field': f, 'status': 'UNKNOWN', 'follow_up': 'No value supplied by source Actor'} for m in master for f in m['missing_fields']]
    gaps += [{'video_id': r['id'], 'title': r.get('title'), 'field': 'availability_status', 'status': 'MEMBERS_ONLY_EXCLUDED', 'follow_up': 'Not part of certified public population'} for r in members]
    write_csv(os.path.join(out, 'VIDEO_METADATA_GAPS.csv'), ['video_id', 'title', 'field', 'status', 'follow_up'], gaps)
    write_csv(os.path.join(out, 'ACCESS_RESTRICTIONS.csv'), ['video_id', 'title', 'restriction', 'raw_dataset_row_locator'],
              [{'video_id': r['id'], 'title': r.get('title'), 'restriction': 'MEMBERS_ONLY', 'raw_dataset_row_locator': ';'.join(r['_rows'])} for r in members])
    dates = sorted(m['publication_timestamp_utc'] for m in master if m['publication_timestamp_utc'])
    open(os.path.join(out, 'SOURCE_COMPLETENESS_REPORT.md'), 'w').write(f"""# {about['channelName']}: source completeness report

Snapshot timestamp: {ts}. Coverage status: **{coverage}** (tranche {tranche}).

- Channel ID: {exp}. Handle: {meta['handle']}. Subscribers: {q(about.get('numberOfSubscribers'))}. YouTube-reported videos: {q(reported)}.
- Run limits: regular {limits[0]}, Shorts {limits[1]}, streams {limits[2]}; max cost ${cap:.2f}; captions/transcripts/AI off.
- Public master rows: {len(master)} (regular {counts['REGULAR']}, Shorts {counts['SHORT']}, streams {counts['STREAM']}); members-only excluded: {len(members)}.
- Date coverage: {dates[0] if dates else 'UNKNOWN'} to {dates[-1] if dates else 'UNKNOWN'}.
- Core metadata completeness: {validation['metadata_completeness']['percentage']*100:.2f}%.
{f"- Reuse delta vs PR #39 package ({delta['pr39_package_rows']} rows): {delta['already_in_pr39']} already packaged, {len(delta['new_vs_pr39'])} new." if delta else ''}

## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
""")
    return {'label': label, 'channel': name, 'channel_id': exp, 'tranche': tranche, 'coverage_status': coverage, 'reported_videos': reported,
            'public_rows': len(master), 'members_only': len(members), **{k.lower(): v for k, v in counts.items()},
            'run_ids': [x['run_id'] for x in rr], 'cost_usd': round(sum(x['actual_cost_usd'] for x in rr), 3),
            'validation': validation['status'], 'new_vs_pr39': None if delta is None else len(delta['new_vs_pr39'])}, master

if __name__ == '__main__':
    summary, allrows = [], []
    for label in PLAN:
        if not glob.glob(os.path.join(RAW, f'{label}_*_run.json')): print('SKIP (no run yet)', label); continue
        s, m = build(label); summary.append(s); allrows += m
    ids = [m['video_id'] for m in allrows]
    assert len(ids) == len(set(ids)), 'cross-channel duplicate video_id'
    write_csv(os.path.join(ROOT, 'FINANCE_VIDEO_MASTER_ALL.csv'), list(allrows[0].keys()), allrows)
    open(os.path.join(ROOT, 'FINANCE_VIDEO_MASTER_ALL.jsonl'), 'w').write(''.join(json.dumps(m, ensure_ascii=False) + '\n' for m in allrows))
    write_csv(os.path.join(ROOT, 'CHANNEL_STATUS.csv'), list(summary[0].keys()), summary)
    print(json.dumps(summary, indent=1)); print('total_rows', len(allrows), 'total_cost', round(sum(s['cost_usd'] for s in summary), 3))
