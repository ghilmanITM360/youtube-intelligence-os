# Computes per-channel evidence for 22 testable PDF principles (IDs defined in 00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md)
# and a DRAFT automated verdict. Final verdicts may be overridden in _analysis/NNN.md (section "pdf").
import os, re, numpy as np, pandas as pd
AUD = os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = pd.read_pickle(f'{AUD}/out/forensics_videos.pkl')
Q = pd.read_csv(f'{ROOT}/_work_channel_queue.csv')
shape_n = V.groupby('title_shape').channel_id.nunique()
shape_first = V.dropna(subset=['pub']).sort_values('pub').groupby('title_shape').channel_id.first()

FAM = {
 'F01_mystery': r'what (really )?happened|real reason|nobody (tells|talks)|untold|disappear|hidden world|dark side|than you think|not supposed',
 'F02_downfall': r'rise and fall|killed|why .* failed|destroy|the mistake that|until |will fail|tried to warn|went wrong',
 'F03_contradiction': r'\bwon but|weakness|nobody wanted|supposed to|most hated|refused|shouldn.t exist|no wonder|but (it|they|nobody)',
 'F04_character': r'changed .* forever|completely wrong|the night|the (man|woman|guy|person|family) who|keeping .* alive|incredible|the last |genius of',
 'F05_explain_rank': r'every .* explained|ranked|levels|iceberg|entire history|\bvs\b|remember these|the most |^\s*\d+ ',
 'F06_revelation': r'truth about|secret|actually works|evidence|what .* know|reveal|found inside|only reason|gets wrong|never (get to )?see',
 'F07_time': r'whatever happened|anymore|forgotten|last days|looked like|was everywhere|years ago',
 'F08_small_cause': r'one small|rejection|said no|last.minute|almost never|the moment|it wasn.t|instead',
 'F09_practical': r'how much|so expensive|hidden (cost|economics)|beginner|mistakes?|myth|what happens (when|if|after)|explained|what it takes|how to',
 'F10_conflict': r'battle|surviv|warning|minutes that|what if|closest|one step|turned against|regret|worst enemy',
}
FAM_RE = {k: re.compile(p, re.I) for k, p in FAM.items()}
V['t_family'] = V.title.fillna('').map(lambda t: next((k for k, r in FAM_RE.items() if r.search(t)), ''))
V['t_vague_open'] = V.title.fillna('').str.match(r"(?i)\s*(this|they|these|it|that)\b")
V['t_two_promises'] = V.title.fillna('').str.count(r'\?') >= 2
def caps_words(t): return sum(1 for w in str(t).split() if w.isalpha() and w.isupper() and len(w) >= 3)
V['t_caps_n'] = V.title.map(caps_words)
def thumb_title_overlap(r):
    tw = set(re.findall(r'[a-z]{3,}', str(r.title).lower())); ow = set(re.findall(r'[a-z]{3,}', str(r.th_text).lower()))
    return np.nan if not ow or str(r.th_text) == 'nan' else len(tw & ow) / len(ow)
V['th_title_overlap'] = V.apply(thumb_title_overlap, axis=1)
V['next_tease_end'] = V.ending_60w.fillna('').str.contains(r"(?i)next video|watch (this|next)|on screen|part (2|two)|coming up|in the next|see you (in|next)")

def m(x): return float(np.nanmedian(x)) if len(x) and np.isfinite(np.nanmedian(x)) else np.nan
def rate(s): s = s.dropna().astype(float); return s.mean() if len(s) else np.nan
def p(x): return 'n/a' if pd.isna(x) else f"{100*x:.0f}%"

def contrast(L, col):
    """median PI with vs without a boolean feature (long-form, channel-internal)."""
    a, b = L[L[col] == True].PI, L[L[col] == False].PI
    if len(a) < 4 or len(b) < 4: return None
    return a.median(), b.median(), len(a), len(b)

rows = []
for _, C in Q.iterrows():
    d = V[V.channel_id == C.channel_id].sort_values('pub'); L = d[(d.fmt == 'long') & d.PI.notna()].copy()
    n, nl = len(d), len(L)
    def add(pid, verdict, ev): rows.append(dict(num=C.num, folder=C.folder, channel=C['name'], principle=pid, auto_verdict=verdict, evidence=ev))
    if n == 0:
        for i in range(1, 23): add(f'P{i:02d}', 'INSUFFICIENT DATA', 'no videos in database')
        continue
    few = nl < 12
    # P01 outlier exploitation: after a Successful/Breakout upload, do the next 10 uploads repeat its topic more than base rate?
    if not few:
        Ls = L.sort_values('pub').reset_index(drop=True); hits = []; base = Ls.topic.value_counts(normalize=True)
        for i, r in Ls[Ls.perf_class.isin(['Breakout', 'Successful'])].iterrows():
            nxt = Ls.iloc[i + 1:i + 11]
            if len(nxt) >= 5: hits.append(((nxt.topic == r.topic).mean(), base.get(r.topic, 0)))
        if hits:
            obs, exp = np.mean([h[0] for h in hits]), np.mean([h[1] for h in hits])
            add('P01', 'FOLLOWED' if obs > exp * 1.25 else 'PARTIALLY FOLLOWED' if obs > exp * 0.9 else 'NOT FOLLOWED',
                f"{(L.PI>=5).sum()} long-form ≥5x and {(L.PI>=10).sum()} ≥10x own baseline; after {len(hits)} winners, next-10 uploads repeat the winner's topic {p(obs)} vs base rate {p(exp)}")
        else: add('P01', 'INSUFFICIENT DATA', f"{(L.PI>=2).sum()} videos ≥2x baseline; too few later uploads to test follow-up")
    else: add('P01', 'INSUFFICIENT DATA', f'only {nl} PI-classified long-form videos')
    # P02 niche coherence
    tc = d.topic.value_counts(normalize=True); top2 = tc.head(2).sum()
    aud = d.title.str.contains(r"(?i)senior|retiree|retire|over (50|60|65)|\b6[0-9]\b|your (20s|30s|40s|50s)|boomer|gen z|millennial|veteran|widow|uk|canada|australia").mean()
    add('P02', 'FOLLOWED' if top2 >= .6 else 'PARTIALLY FOLLOWED' if top2 >= .4 else 'NOT FOLLOWED',
        f"top-2 topics ({', '.join(tc.head(2).index)}) = {p(top2)} of uploads; explicit audience marker in {p(aud)} of titles")
    # P03 format variety
    fc = d.content_format.value_counts(normalize=True); nf = (fc >= .1).sum()
    add('P03', 'FOLLOWED' if nf >= 3 else 'PARTIALLY FOLLOWED' if nf == 2 else 'NOT FOLLOWED',
        f"{nf} title-format types each ≥10% of uploads ({', '.join(f'{k} {p(v)}' for k, v in fc.head(4).items())})")
    # P04 repetition / inauthentic-content risk
    dup = d.dup_script_flag.mean(); same_shape = d.title_shape.duplicated(keep=False).mean()
    add('P04', 'CONTRADICTED BY EVIDENCE' if dup >= .2 else 'PARTIALLY FOLLOWED' if (dup >= .05 or same_shape >= .1) else 'FOLLOWED',
        f"near-duplicate-script flag on {p(dup)} of videos; repeated title word-sets within channel {p(same_shape)}")
    # P05 format arbitrage / niche bending -> analyst judgement
    add('P05', 'NOT TESTABLE', 'requires historical competitor-format landscape at launch; analyst note in report if a bend is visible')
    # P06 competitor-topic overlap
    sh = d.title_shape.map(shape_n) > 1; first = d.title_shape.map(shape_first) == C.channel_id
    add('P06', 'FOLLOWED' if sh.mean() >= .1 else 'PARTIALLY FOLLOWED' if sh.mean() > 0 else 'NOT FOLLOWED',
        f"{p(sh.mean())} of titles share a word-set with another channel; this channel published first on {int((sh & first).sum())} of {int(sh.sum())}")
    # P07 title-format library use
    L['fam'] = L.t_family != ''; fam = (d.t_family != '').mean(); ct = contrast(L, 'fam') if not few else None
    add('P07', ('FOLLOWED' if fam >= .5 else 'PARTIALLY FOLLOWED' if fam >= .2 else 'NOT FOLLOWED') if True else '',
        f"{p(fam)} of titles match a 100-format family" + (f"; median PI with {ct[0]:.2f} (n={ct[2]}) vs without {ct[1]:.2f} (n={ct[3]})" if ct else ''))
    # P08 specificity & stakes
    L['spec'] = L.t_number | L.t_dollar | L.t_named_entity; spec = (d.t_number | d.t_dollar | d.t_named_entity).mean(); ct = contrast(L, 'spec') if not few else None
    add('P08', 'FOLLOWED' if spec >= .5 else 'PARTIALLY FOLLOWED' if spec >= .25 else 'NOT FOLLOWED',
        f"{p(spec)} of titles carry a number/$/named entity" + (f"; median PI with {ct[0]:.2f} vs without {ct[1]:.2f}" if ct else ''))
    # P09 title mistakes
    capsall = (d.t_caps_n >= 3).mean(); vague = d.t_vague_open.mean(); two = d.t_two_promises.mean()
    bad = max(capsall, vague)
    add('P09', 'FOLLOWED' if bad < .1 else 'PARTIALLY FOLLOWED' if bad < .3 else 'NOT FOLLOWED',
        f"titles with ≥3 ALL-CAPS words {p(capsall)}; vague 'this/they' opener {p(vague)}; double-question {p(two)}")
    # P10 title-thumbnail complementarity
    ov = m(d.th_title_overlap); cov = d.th_title_overlap.notna().mean()
    add('P10', 'INSUFFICIENT DATA' if cov < .3 else 'FOLLOWED' if ov <= .34 else 'PARTIALLY FOLLOWED' if ov <= .6 else 'NOT FOLLOWED',
        f"OCR thumbnail text found on {p(cov)}; median share of thumbnail words repeated from title {('n/a' if pd.isna(ov) else f'{ov:.2f}')}")
    # P11 thumbnail one idea / few words
    tw = m(d.th_text_words); thc = d.thumb_file.mean()
    add('P11', 'INSUFFICIENT DATA' if thc < .3 else 'FOLLOWED' if tw <= 4 else 'PARTIALLY FOLLOWED' if tw <= 7 else 'NOT FOLLOWED',
        f"thumbnail images {p(thc)}; median OCR words {tw if pd.notna(tw) else 'n/a'} (OCR undercounts stylised text); face/character detected {p(rate(d.th_has_face))} (cartoon faces often missed)")
    tx = d[d.has_transcript == 1]
    if len(tx) < 5:
        for i in range(12, 19): add(f'P{i:02d}', 'INSUFFICIENT DATA', f'only {len(tx)} transcripts')
    else:
        hook = (tx.h_first_sentence_q | tx.h_number_30s | tx.h_contrarian_30s | tx.h_story_open | tx.h_you_open).mean(); greet = tx.h_greeting_open.mean()
        add('P12', 'FOLLOWED' if hook >= .7 and greet < .2 else 'PARTIALLY FOLLOWED' if hook >= .4 else 'NOT FOLLOWED',
            f"opening ~75 words contain question/number/contradiction/story/you-hook in {p(hook)}; greeting/channel-intro opening {p(greet)}")
        stake = (tx.h_stakes_30s | tx.h_why_matters_150).mean(); ct = contrast(L.assign(stk=L.h_stakes_30s | L.h_why_matters_150), 'stk') if not few else None
        add('P13', 'FOLLOWED' if stake >= .5 else 'PARTIALLY FOLLOWED' if stake >= .25 else 'NOT FOLLOWED',
            f"explicit stakes/why-it-matters language early in {p(stake)}" + (f"; median PI with {ct[0]:.2f} vs without {ct[1]:.2f}" if ct else ''))
        loop = tx.h_open_loop_30s.mean()
        add('P14', 'FOLLOWED' if loop >= .5 else 'PARTIALLY FOLLOWED' if loop >= .25 else 'NOT FOLLOWED', f"explicit open-loop/promise phrase in first ~150 words of {p(loop)}")
        ld = m(tx.s_loop_density)
        add('P15', 'FOLLOWED' if ld >= .08 else 'PARTIALLY FOLLOWED' if ld >= .03 else 'NOT FOLLOWED', f"bridge/cliffhanger phrases per 100 words (median) {ld:.3f}")
        dd = m(tx.s_data_density); srcs = (d.tx_sources.fillna('') != '').mean()
        add('P16', 'FOLLOWED' if dd >= 1.0 and srcs >= .5 else 'PARTIALLY FOLLOWED' if dd >= .5 or srcs >= .3 else 'NOT FOLLOWED',
            f"data/citation terms per 100 words {dd:.2f}; videos naming an institution/source {p(srcs)}")
        yd = m(tx.s_you_density)
        add('P17', 'FOLLOWED' if yd >= 2.5 else 'PARTIALLY FOLLOWED' if yd >= 1.2 else 'NOT FOLLOWED', f"'you/your' per 100 words (median) {yd:.2f}")
        ft = tx.next_tease_end.mean(); cta = rate(tx.s_cta_end)
        add('P18', 'FOLLOWED' if ft >= .4 else 'PARTIALLY FOLLOWED' if (ft >= .1 or cta >= .4) else 'NOT FOLLOWED', f"next-video tease in final ~60 words {p(ft)}; any CTA in final 10% {p(cta)}")
    dm = m(d[d.fmt == 'long'].duration_seconds) / 60 if (d.fmt == 'long').any() else np.nan
    rd = L[['duration_seconds', 'PI']].corr(method='spearman').iloc[0, 1] if not few else np.nan
    add('P19', 'INSUFFICIENT DATA' if pd.isna(dm) else 'FOLLOWED' if dm >= 8 else 'NOT FOLLOWED',
        f"median long-form length {dm:.1f} min" + (f"; Spearman(duration, PI) {rd:.2f}" if pd.notna(rd) else '') + ' — 8+ min is an ad-eligibility rule, not a success rule (PDF p555)')
    gaps = d.pub.diff().dt.days.dropna()
    if len(gaps) >= 8:
        cv = gaps.std() / max(gaps.mean(), .1)
        add('P20', 'FOLLOWED' if cv <= 1.0 else 'PARTIALLY FOLLOWED' if cv <= 2.0 else 'NOT FOLLOWED', f"median gap {gaps.median():.1f} d, gap CV {cv:.2f}, longest pause {gaps.max():.0f} d")
    else: add('P20', 'INSUFFICIENT DATA', f'{len(gaps)} dated gaps')
    if not few:
        tm = L.groupby('topic').PI.median()[L.topic.value_counts() >= 3]; fm = L.groupby('content_format').PI.median()[L.content_format.value_counts() >= 3]
        if len(tm) >= 2 and len(fm) >= 2:
            ts, fs = tm.max() / tm.min(), fm.max() / fm.min()
            add('P21', 'FOLLOWED' if ts > fs * 1.2 else 'CONTRADICTED BY EVIDENCE' if fs > ts * 1.2 else 'PARTIALLY FOLLOWED',
                f"spread of median PI across topics {ts:.2f}x (best {tm.idxmax()}) vs across title formats {fs:.2f}x (best {fm.idxmax()})")
        else: add('P21', 'INSUFFICIENT DATA', 'fewer than two topics/formats with ≥3 videos')
    else: add('P21', 'INSUFFICIENT DATA', f'{nl} classified long-form')
    po = m(tx.h_title_overlap_150) if len(tx) >= 5 else np.nan
    add('P22', 'INSUFFICIENT DATA' if pd.isna(po) else 'FOLLOWED' if po >= .5 else 'PARTIALLY FOLLOWED' if po >= .3 else 'NOT FOLLOWED',
        f"median share of title keywords that appear in the first ~150 spoken words {('n/a' if pd.isna(po) else f'{po:.2f}')}")

R = pd.DataFrame(rows)
os.makedirs(f'{ROOT}/02_SHARED_EVIDENCE', exist_ok=True)
R.to_csv(f'{ROOT}/02_SHARED_EVIDENCE/PDF_PRINCIPLE_EVALUATION_AUTO.csv', index=False)
V[['video_id', 't_family', 't_vague_open', 't_caps_n', 'th_title_overlap', 'next_tease_end']].to_pickle(f'{AUD}/out/forensics_principle_feats.pkl')
print(pd.crosstab(R.principle, R.auto_verdict))
