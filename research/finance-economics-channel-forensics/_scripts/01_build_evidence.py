# Builds per-channel evidence files for the 69-channel forensic study.
# Input: feature table derived read-only from finance_economics_complete.db
#   (branch data/finance-economics-complete-2026-11-11 @933f236e, sha256 fa6fd1b2...d20)
#   via ~/YIOS-local-audits/finance-viral-forensics-2026-11-12 (scripts 01/02).
# Run with that audit's venv:  .venv/bin/python 01_build_evidence.py
import os, re, json, sqlite3, numpy as np, pandas as pd
from urllib.parse import urlparse

AUD = os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = '/Users/ghilmankhan/workprojects/yios-audit-fixes/data/catalog/finance_economics_complete.db'
v = pd.read_pickle(f'{AUD}/out/videos_feat.pkl')
ch = pd.read_pickle(f'{AUD}/out/channels.pkl')
ocr = pd.read_csv(f'{AUD}/out/thumbnail_ocr.csv')
vis = pd.read_csv(f'{AUD}/out/thumbnail_visual_features.csv')
v = v.merge(ocr[['video_id', 'th_text']], on='video_id', how='left').merge(
    vis[['video_id', 'th_has_face', 'th_face_count', 'th_colorfulness', 'th_brightness', 'th_red_share', 'th_text_words']], on='video_id', how='left')
v['thumb_file'] = v.video_id.map(lambda x: os.path.exists(f'{AUD}/thumbs/{x}.jpg'))

# ---------- topic taxonomy (rule-based, title + first 300 transcript words; INFERRED labels) ----------
TOPICS = [
 ('social_security', r'social security|\bssa\b|\bssi\b|\bssdi\b|\bcola\b|survivor benefit|spousal benefit'),
 ('medicare_health_costs', r'medicare|medicaid|part [abd]\b|\birmaa\b|health ?care cost|long.term care'),
 ('uk_pension_benefits', r'\bdwp\b|\bhmrc\b|state pension|pension credit|winter fuel|\bpip\b|universal credit'),
 ('veterans_benefits', r'\bva\b|veteran'),
 ('retirement_accounts_tax', r'\b401\(?k|\bira\b|roth|\brmd|required minimum|pension|annuit|retire'),
 ('taxes_irs', r'\birs\b|\btax|\bw-?2\b|1099|deduction'),
 ('senior_perks_discounts', r'discount|free (for|perks|stuff|things)|perks|seniors? (get|can|over)|benefits? (for|seniors)'),
 ('banking_cash', r'\bbank|cash|withdraw|\bcds?\b|savings account|deposit|\bfdic\b|atm\b|checking'),
 ('housing_real_estate', r'\bhouse|\bhome|mortgage|\brent\b|real estate|property|housing|landlord'),
 ('crypto', r'bitcoin|crypto|\bbtc\b|ethereum'),
 ('investing_stocks', r'\bstock|\betf|dividend|index fund|portfolio|s&p|\bvoo\b|invest|compound'),
 ('macro_economy', r'econom|inflation|\bfed\b|federal reserve|interest rate|recession|\bgdp\b|tariff|dollar|debt ceiling|national debt|unemployment'),
 ('crisis_collapse', r'collapse|crash|crisis|depression|bubble|meltdown|bankrupt'),
 ('geopolitics_country', r'china|japan|russia|india|germany|europe|saudi|dubai|country|countries|nation'),
 ('company_business_case', r'company|companies|brand|\bceo\b|empire|business model|corporat|walmart|amazon|apple|tesla|mcdonald|costco|starbucks|nike|disney|store'),
 ('pov_story', r'\bpov\b'),
 ('wealth_psychology_habits', r'\brich\b|\bpoor\b|wealth|millionaire|billionaire|habit|mindset|middle class|broke|frugal|net worth'),
 ('budgeting_debt', r'budget|\bdebt\b|credit card|credit score|save money|saving|paycheck|salary|income'),
 ('side_hustle_business', r'side hustle|passive income|business idea|start a business|entrepreneur'),
 ('money_history', r'histor|ancient|medieval|\b1[0-9]{3}\b|century|empire'),
 ('scams_fraud', r'scam|fraud|ponzi|con man|stolen'),
]
TOPIC_RE = [(n, re.compile(p, re.I)) for n, p in TOPICS]
def topics_of(title, text):
    s = (title or '') + ' ' + ' '.join(str(text or '').split()[:300])
    t = (title or '')
    hits_title = [n for n, r in TOPIC_RE if r.search(t)]
    hits_all = [n for n, r in TOPIC_RE if r.search(s)]
    hits = hits_title + [h for h in hits_all if h not in hits_title]
    return (hits[0] if hits else 'other_general'), (hits[1] if len(hits) > 1 else '')

FORMATS = [
 ('pov_story', r'\bpov\b|\bstory\b|i (was|made|lost|quit|became)'),
 ('rise_fall_case', r'rise and fall|what happened to|how .+ (became|built|lost|destroyed|went)|why .+ (failed|collapsed|disappeared)|downfall'),
 ('list_countdown', r'^\s*(top\s*)?\d+\s|\b\d+ (ways|things|reasons|mistakes|tips|stocks|etfs|rules|habits|signs|items|perks|benefits|changes|states|cities|places|jobs|steps|levels|discounts)\b'),
 ('warning_mistake', r'warning|\bstop\b|don\'t|do not|mistake|avoid|never|trap|before you|danger|beware'),
 ('news_change_update', r'\bnew\b|just|announce|starting|changes?\b|update|breaking|confirmed|approved|20(25|26|27)|this (month|week|year)|deadline|begins'),
 ('explainer', r'explained|how .+ (works|work)|\bwhy\b|what is|the truth|the real|actually|meaning'),
 ('comparison', r'\bvs\.?\b|versus|\bor\b .+\?|better than|compared'),
 ('how_to', r'how to|guide|step.by.step|strategy|plan\b'),
 ('question', r'\?'),
]
FORMAT_RE = [(n, re.compile(p, re.I)) for n, p in FORMATS]
def format_of(title):
    t = title or ''
    for n, r in FORMAT_RE:
        if r.search(t): return n
    return 'statement_other'

SRC_PAT = {
 'Social Security Administration (SSA)': r'social security administration|\bssa\b|ssa\.gov',
 'IRS': r'\birs\b|internal revenue|irs\.gov',
 'CMS / Medicare.gov': r'\bcms\b|centers for medicare|medicare\.gov',
 'Federal Reserve': r'federal reserve|\bthe fed\b|fomc|jerome powell|powell',
 'BLS / CPI data': r'bureau of labor|\bbls\b|consumer price index|\bcpi\b',
 'Congress / legislation': r'congress|senate|house bill|\bbill\b passed|legislation|act of 20',
 'CBO / Treasury': r'congressional budget office|\bcbo\b|treasury',
 'Trustees report': r'trustees report|trustees',
 'Census / government statistics': r'census bureau|census data',
 'Company filings / earnings': r'annual report|earnings|10-k|quarterly report|shareholder letter|sec filing',
 'News outlets': r'bloomberg|reuters|wall street journal|\bwsj\b|cnbc|new york times|financial times|forbes|the economist',
 'Academic / research study': r'\bstudy\b|research(ers)?|university|survey|journal',
 'DWP / HMRC / gov.uk': r'\bdwp\b|\bhmrc\b|gov\.uk',
 'VA': r'department of veterans|\bva\b',
 'World Bank / IMF / OECD': r'world bank|\bimf\b|\boecd\b',
}
SRC_RE = {k: re.compile(p, re.I) for k, p in SRC_PAT.items()}
URL_RE = re.compile(r'https?://[^\s)\]>"\']+')

def words(s): return re.findall(r"\S+", re.sub(r'\[[^\]]*\]|>>', '', str(s or '')))
def excerpt(text, a, b):
    W = words(text); return ' '.join(W[a:b]) if len(W) > a else ''

def slug(s): return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')[:40]

def st(x): return 'AVAILABLE' if (x is not None and not (isinstance(x, float) and np.isnan(x)) and str(x).strip() not in ('', 'nan', 'None')) else 'MISSING'

# ---------- derived per-video columns ----------
tp = v.apply(lambda r: topics_of(r.title, r.text), axis=1)
v['topic'] = [a for a, b in tp]; v['subtopic'] = [b for a, b in tp]
v['content_format'] = v.title.map(format_of)
v['hook_5s'] = v.text.map(lambda t: excerpt(t, 0, 13))      # ~150 wpm => 13 words ~ 5 s (INFERRED timing)
v['hook_15s'] = v.text.map(lambda t: excerpt(t, 0, 38))
v['hook_30s'] = v.text.map(lambda t: excerpt(t, 0, 75))
v['ending_60w'] = v.text.map(lambda t: ' '.join(words(t)[-60:]) if len(words(t)) > 120 else '')
v['desc_urls'] = v.description.map(lambda d: ' '.join(sorted({urlparse(u).netloc.replace('www.', '') for u in URL_RE.findall(str(d or ''))})))
v['tx_sources'] = (v.text.fillna('') + ' ' + v.description.fillna('')).map(lambda s: '; '.join(k for k, r in SRC_RE.items() if r.search(s)))
v['pub_date'] = v.pub.dt.strftime('%Y-%m-%d')

# cross-channel title-shape sharing (for competitor-topic behaviour)
def shape(t): return ' '.join(sorted(set(w for w in re.findall(r'[a-z]{4,}', str(t).lower()))))
v['title_shape'] = v.title.map(shape)

# ---------- channel ordering (investigation priority, NOT quality ranking) ----------
g = v.groupby('channel_id')
agg = pd.DataFrame({
 'videos': g.size(), 'long': g.fmt.apply(lambda s: (s == 'long').sum()), 'shorts': g.fmt.apply(lambda s: (s == 'short').sum()),
 'with_views': g.views.apply(lambda s: s.notna().sum()), 'with_tx': g.has_transcript.sum(),
 'with_thumb_img': g.thumb_file.sum(), 'pi_long': g.apply(lambda d: ((d.fmt == 'long') & d.PI.notna()).sum()),
 'full_meta': g.metadata_level.apply(lambda s: (s == 'FULL').mean()),
 'first': g.pub.min(), 'latest': g.pub.max(), 'median_views': g.views.median(),
}).reset_index()
c = ch.merge(agg, on='channel_id', how='left').fillna({'videos': 0, 'long': 0, 'shorts': 0, 'pi_long': 0, 'with_tx': 0})
def tier(r):
    if r.videos == 0: return 5
    if r.pi_long >= 40 and r.full_meta >= .9 and r.with_tx / max(r.videos, 1) >= .8: return 1
    if r.pi_long >= 20: return 2
    if r.pi_long >= 12 or (r.median_views or 0) >= 50000: return 3
    return 4
c['priority_tier'] = c.apply(tier, axis=1)
c = c.sort_values(['priority_tier', 'pi_long', 'videos', 'name'], ascending=[True, False, False, True]).reset_index(drop=True)
c['num'] = range(1, len(c) + 1)
c['folder'] = c.apply(lambda r: f"{r.num:03d}_{slug(r['name'])}", axis=1)

REP = f'{ROOT}/01_CHANNEL_REPORTS'; os.makedirs(REP, exist_ok=True)
CAT_COLS = ['video_id', 'url', 'title', 'pub_date', 'duration_seconds', 'fmt', 'views', 'likes', 'comments', 'PI', 'perf_class',
            'topic', 'subtopic', 'content_format', 'tx_source', 'tx_status', 'tx_words', 'thumbnail_url', 'thumbnail_source', 'metadata_level', 'dup_script_flag']

def fstat(r):
    return {
      'f_title': st(r.title), 'f_description': st(r.description), 'f_published': st(r.published), 'f_duration': st(r.duration_seconds),
      'f_views': st(r.views), 'f_likes': st(r.likes), 'f_comments': st(r.comments),
      'f_thumbnail_url': ('UNVERIFIED' if r.thumbnail_source == 'derived_standard_pattern' else st(r.thumbnail_url)),
      'f_thumbnail_image': 'AVAILABLE' if r.thumb_file else 'MISSING',
      'f_transcript': ('AVAILABLE' if r.has_transcript and str(r.tx_status) in ('COMPLETE', 'COMPLETE_ASR') else 'UNVERIFIED' if r.has_transcript else 'MISSING'),
      'transcript_location': (f"finance_economics_complete.db:transcripts[video_id='{r.video_id}', source='{r.tx_source}']" if r.has_transcript else ''),
    }

dossier_all = {}
for _, C in c.iterrows():
    d = v[v.channel_id == C.channel_id].copy().sort_values('pub')
    folder = f'{REP}/{C.folder}'; os.makedirs(folder, exist_ok=True)
    inv = d[CAT_COLS].copy()
    F = pd.DataFrame([fstat(r) for r in d.itertuples()], index=d.index)
    inv = pd.concat([inv, F], axis=1)
    inv.round(3).to_csv(f'{folder}/VIDEO_INVENTORY.csv', index=False)
    L = d[(d.fmt == 'long') & d.PI.notna()].sort_values('PI', ascending=False)
    WCOLS = ['video_id', 'url', 'title', 'pub_date', 'duration_seconds', 'views', 'PI', 'perf_class', 'topic', 'content_format',
             'th_text', 'th_has_face', 'hook_5s', 'hook_15s', 'hook_30s', 'ending_60w', 'tx_sources', 'desc_urls', 'dup_script_flag']
    nwin = min(8, max(3, len(L) // 6)) if len(L) else 0
    W = L.head(nwin); U = L.tail(nwin).iloc[::-1] if len(L) >= 6 else L.iloc[0:0]
    W[WCOLS].round(3).to_csv(f'{folder}/WINNING_VIDEOS.csv', index=False)
    U[WCOLS].round(3).to_csv(f'{folder}/FAILED_VIDEOS.csv', index=False)
    # topic map
    T = d.groupby('topic').agg(videos=('video_id', 'size'), long=('fmt', lambda s: (s == 'long').sum()), median_views=('views', 'median'),
                               median_PI=('PI', 'median'), breakout_or_success=('perf_class', lambda s: s.isin(['Breakout', 'Successful']).sum()),
                               underperforming=('perf_class', lambda s: (s == 'Underperforming').sum()), first=('pub_date', 'min'), last=('pub_date', 'max')).reset_index()
    T.sort_values('videos', ascending=False).round(3).to_csv(f'{folder}/TOPIC_MAP.csv', index=False)
    # source map
    S = d[['video_id', 'title', 'topic', 'tx_sources', 'desc_urls']].copy()
    S['evidence_type'] = np.where(S.desc_urls != '', 'CREATOR-PROVIDED REFERENCE (description URL domains)',
                          np.where(S.tx_sources != '', 'STRONGLY INFERRED (institution named in transcript/description)', 'UNKNOWN'))
    S['confidence'] = np.where(S.desc_urls != '', 'MEDIUM (domain only; claim-level match not verified)', np.where(S.tx_sources != '', 'LOW-MEDIUM', 'NONE'))
    S.to_csv(f'{folder}/SOURCE_MAP.csv', index=False)
    dossier_all[C.folder] = dict(C=C, d=d, L=L, W=W, U=U, T=T)

c[['num', 'folder', 'channel_id', 'name', 'handle', 'url', 'sub_niche', 'subscribers', 'videos', 'long', 'shorts', 'with_views', 'with_tx',
   'with_thumb_img', 'pi_long', 'full_meta', 'first', 'latest', 'median_views', 'priority_tier', 'availability', 'availability_note']].to_csv(f'{ROOT}/_work_channel_queue.csv', index=False)
v.drop(columns=['text']).to_pickle(f'{AUD}/out/forensics_videos.pkl')
pd.to_pickle(dossier_all, f'{AUD}/out/forensics_dossier.pkl')
print(c[['num', 'name', 'videos', 'long', 'shorts', 'pi_long', 'priority_tier']].to_string())
