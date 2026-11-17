# Assembles CHANNEL_REPORT.md (22 sections) from computed evidence + analyst text in _analysis/<folder>.md,
# and refreshes MASTER_TRACKER.csv / PDF_PRINCIPLE_EVALUATION.csv. Re-runnable; never edits evidence files.
import os, re, sys, datetime, numpy as np, pandas as pd
AUD = os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = f'{ROOT}/01_CHANNEL_REPORTS'; AN = f'{ROOT}/_analysis'
V = pd.read_pickle(f'{AUD}/out/forensics_videos.pkl')
Q = pd.read_csv(f'{ROOT}/_work_channel_queue.csv')
P = pd.read_csv(f'{ROOT}/02_SHARED_EVIDENCE/PDF_PRINCIPLE_EVALUATION_AUTO.csv')

PRINCIPLES = {  # id: (PDF location, what the PDF says — paraphrased, not new principles)
 'P01': ('Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35', 'Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers.'),
 'P02': ('Module 2.2 Niche vs Format vs Template, p.11', 'A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel.'),
 'P03': ('Module 2.2, pp.12-13', 'One niche can carry many formats; add formats to grow without changing niche.'),
 'P04': ('Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555', 'Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy).'),
 'P05': ('Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26', 'Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches.'),
 'P06': ('Module 2.7 Competitor Research pp.28-30; Method 1 p.34', 'Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content.'),
 'P07': ('Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64', 'Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver.'),
 'P08': ('100 Title Formats p.53 (five-part engine), p.66 scorecard', 'A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes.'),
 'P09': ('100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345', 'Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty.'),
 'P10': ('100 Title Formats p.66 (title+thumbnail one promise), p.68 #11', 'Thumbnail should add a complementary clue, not repeat the title.'),
 'P11': ('Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP)', 'Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea.'),
 'P12': ('Engagement Playbook §1 p.265; Masterclass Zone 1 p.320', 'The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge.'),
 'P13': ('Masterclass Zone 2 p.320; Engagement §18 p.283', 'Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity.'),
 'P14': ('Masterclass Zone 3 p.320; Ch.23 p.350', 'Open at least one curiosity loop before ~30 s and keep it open.'),
 'P15': ('Engagement §2 & §7 pp.267, 272', 'Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off.'),
 'P16': ('Engagement §8 p.273', 'Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers.'),
 'P17': ('Engagement §6 p.271', 'Second-person address makes the viewer a participant (“if you own…”, “imagine you…”).'),
 'P18': ('Engagement §15-16 pp.280-281; Deployment p.284', 'Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end.'),
 'P19': ('Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555', 'Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story.'),
 'P20': ('Module 2.7 Posting cadence p.29', 'Check upload frequency, consistency, dead periods and growth inflection points.'),
 'P21': ('Topic Selection Masterclass intro p.33', '“A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever.'),
 'P22': ('Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345', 'Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise.'),
}

def sections(path):
    if not os.path.exists(path): return {}
    S, cur = {}, None
    for line in open(path).read().splitlines():
        m = re.match(r'^## (\w+)\s*$', line)
        if m: cur = m.group(1); S[cur] = []; continue
        if cur: S[cur].append(line)
    return {k: '\n'.join(v).strip() for k, v in S.items()}

def esc(s): return str(s).replace('|', '/').replace('\n', ' ')
def fnum(x): return 'n/a' if pd.isna(x) else f"{x:,.0f}"

REQUIRED = ['key', 'identity', 'winners', 'failures', 'comparison', 'research', 'trend', 'thumbnails', 'titles', 'hooks', 'script',
            'engagement', 'publishing', 'strengths', 'model', 'copy', 'avoid', 'limitations', 'diagnosis']
track, final = [], []
for _, C in Q.iterrows():
    folder = C.folder; A = sections(f'{AN}/{folder}.md')
    dos = open(f'{REP}/{folder}/EVIDENCE_DOSSIER.md').read()
    d = V[V.channel_id == C.channel_id].sort_values('pub')
    Pc = P[P.folder == folder].set_index('principle')
    over = {}
    for line in A.get('pdf', '').splitlines():
        m = re.match(r'^(P\d\d):\s*([A-Z ]+?)\s*[—-]\s*(.*)$', line.strip())
        if m: over[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    done = all(A.get(k) for k in REQUIRED)
    if A:
        def sec(k): return A.get(k, '_Not written._')
        head = [l for l in dos.splitlines() if l.startswith('- ')]
        topic_tbl = dos.split('## Topic map')[1].split('## Title format mix')[0].strip() if '## Topic map' in dos else '_No videos._'
        fmt_mix = dos.split('## Title format mix')[1].split('\n## ')[0].strip() if '## Title format mix' in dos else ''
        win_blk = dos.split('## Top PI long-form (winners)')[1].split('\n## ')[0].strip() if '## Top PI' in dos else '_None classified._'
        los_blk = dos.split('## Bottom PI long-form (underperformers)')[1].split('\n## ')[0].strip() if '## Bottom PI' in dos else '_None classified._'
        con_blk = ('## Upper-half' in dos) and dos.split('## Upper-half vs lower-half PI contrast (long-form; text proxies, correlation only)')[1].split('\n## ')[0].strip() or '_Too few classified videos for a contrast._'
        shorts_blk = ('## Shorts' in dos) and ('## Shorts' + dos.split('## Shorts')[1].split('\n## ')[0]) or ''
        src_blk = ('## Sources named' in dos) and dos.split('## Sources named (transcript/description) — counts of videos')[1].split('\nThumbnail montage')[0].strip() or ''
        cat = ['| # | date | title | min | views | PI | class | topic | title format | transcript |', '|---|---|---|---|---|---|---|---|---|---|']
        for i, r in enumerate(d.itertuples(), 1):
            cat.append(f"| {i} | {r.pub_date if isinstance(r.pub_date, str) else 'n/a'} | [{esc(r.title)[:90]}]({r.url}) | {('' if pd.isna(r.duration_seconds) else f'{r.duration_seconds/60:.1f}')} | {fnum(r.views)} | {('' if pd.isna(r.PI) else f'{r.PI:.2f}')} | {r.perf_class if r.fmt=='long' else 'SHORT'} | {r.topic} | {r.content_format} | {'Y' if r.has_transcript else 'N'} |")
        pdf = ['| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |', '|---|---|---|---|---|---|']
        for pid, (loc, says) in PRINCIPLES.items():
            auto_v, ev = (Pc.loc[pid, 'auto_verdict'], Pc.loc[pid, 'evidence']) if pid in Pc.index else ('INSUFFICIENT DATA', '')
            fv, note = over.get(pid, (auto_v, ''))
            pdf.append(f"| {pid} | {loc} | {esc(says)} | {esc(ev)} | **{fv}** | {esc(note)} |")
            final.append(dict(num=C.num, folder=folder, channel=C['name'], principle=pid, pdf_location=loc, verdict=fv, auto_verdict=auto_v, evidence=ev, analyst_note=note))
        R = [f"# {C['name']} — Channel Forensic Report", '',
             f"Channel #{C.num:03d} of 69 · investigation tier {C.priority_tier} (data-availability order, not a quality rank) · research date {datetime.date.today()} · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).",
             '', 'Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.', '',
             f"**Key conclusion:** {sec('key')}", '',
             '## 1. Channel identity and positioning', sec('identity'), '',
             '## 2. Database inventory and coverage', *head, '', 'Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.', '',
             '## 3. Complete video catalogue', f"All {len(d)} videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).", '', *cat, '',
             '## 4. Topic and sub-niche map', topic_tbl, '', f"Title-format mix (INFERRED tags): {fmt_mix}", '', sec('topics') if A.get('topics') else '', '',
             '## 5. Winning video analysis', sec('winners'), '', '### Evidence: top-PI long-form videos', win_blk, '',
             '## 6. Underperforming video analysis', sec('failures'), '', '### Evidence: bottom-PI long-form videos', los_blk, '',
             '## 7. Successful vs failed comparison', sec('comparison'), '', con_blk, '', shorts_blk, '',
             '## 8. Topic discovery and research sources', sec('research'), '', f"Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): {src_blk}", 'Per-video source map: `SOURCE_MAP.csv`.', '',
             '## 9. Trend behaviour', sec('trend'), '',
             '## 10. Thumbnail strategy', sec('thumbnails'), '',
             '## 11. Title strategy', sec('titles'), '',
             '## 12. Hook and introduction strategy', sec('hooks'), '',
             '## 13. Script and storytelling strategy', sec('script'), '',
             '## 14. Audience engagement model', sec('engagement'), '',
             '## 15. Upload and publishing strategy', sec('publishing'), '',
             '## 16. PDF principle evaluation', 'Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.', '', *pdf, '',
             '## 17. Strengths and weaknesses', sec('strengths'), '',
             '## 18. Replicable working model', sec('model'), '',
             '## 19. What to copy', sec('copy'), '',
             '## 20. What not to copy', sec('avoid'), '',
             '## 21. Missing evidence and limitations', sec('limitations'), '', '- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).', '',
             '## 22. Final channel diagnosis', sec('diagnosis'), '']
        open(f'{REP}/{folder}/CHANNEL_REPORT.md', 'w').write('\n'.join(R))
    status = 'COMPLETE' if done else ('ANALYSIS IN PROGRESS' if A else 'INVENTORY COMPLETE')
    if len(d) == 0 and A: status = 'COMPLETE' if done else 'BLOCKED'
    track.append(dict(channel_number=C.num, channel_name=C['name'], channel_id=C.channel_id, sub_niche=C.sub_niche, database_video_count=int(C.videos),
                      long_form_count=int(C.long), shorts_count=int(C.shorts),
                      transcript_coverage=f"{int(C.with_tx)} ({(C.with_tx/C.videos*100 if C.videos else 0):.0f}%)",
                      thumbnail_coverage=f"{int(C.with_thumb_img) if pd.notna(C.with_thumb_img) else 0} ({(C.with_thumb_img/C.videos*100 if C.videos and pd.notna(C.with_thumb_img) else 0):.0f}%)",
                      metadata_coverage=('complete' if C.full_meta == 1 else 'partial' if C.videos else 'none'),
                      inventory='INVENTORY COMPLETE', video_analysis=('COMPLETE' if done else 'PENDING'), pdf_evaluation=('COMPLETE' if done else 'AUTO-DRAFT'),
                      external_research=('SEE REPORT §8' if done else 'PENDING'), report_saved=('YES' if A else 'NO'), analysis_status=status,
                      report_location=f"01_CHANNEL_REPORTS/{folder}/CHANNEL_REPORT.md", key_conclusion=A.get('key', '')))
pd.DataFrame(track).to_csv(f'{ROOT}/00_PROJECT_OVERVIEW/MASTER_TRACKER.csv', index=False)
if final: pd.DataFrame(final).to_csv(f'{ROOT}/02_SHARED_EVIDENCE/PDF_PRINCIPLE_EVALUATION.csv', index=False)
T = pd.DataFrame(track); print(T.analysis_status.value_counts().to_string())
