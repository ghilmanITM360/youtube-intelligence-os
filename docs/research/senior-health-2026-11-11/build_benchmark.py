"""Report 2 benchmark: within-channel outliers, template network, concept families, topic/title-format stats.
Run from repo root: python3 -I docs/research/senior-health-2026-11-11/build_benchmark.py
Reads 01-unified-video-table.csv (built by build_inventory.py). Heuristic regex classifiers: see CONCEPTS/TOPICS.
"""
import csv, re, statistics as st, collections, datetime as dt, json
D = "docs/research/senior-health-2026-11-11"
rows = [r for r in csv.DictReader(open(f"{D}/01-unified-video-table.csv"))]
for r in rows:
    for k in ("views", "likes", "comments", "duration_s", "tx_words", "is_short"): r[k] = int(r[k] or 0)
# ponytail: snapshot dates approximate for the Sept registry batch (per-dataset capture dates differ by days)
SNAP = {"A_NOV_ACQ": dt.date(2026, 11, 11), "B_REGISTRY_SEP": dt.date(2026, 9, 21), "REHAN_NOV_PILOT": dt.date(2026, 11, 11)}
for r in rows:
    r["age_d"] = max((SNAP[r["batch"]] - dt.date.fromisoformat(r["published"])).days, 1)
    r["vpd"] = r["views"] / r["age_d"]
comp = [r for r in rows if r["role"] == "COMPETITOR"]
lf = [r for r in comp if not r["is_short"]]
med = lambda xs: st.median(xs) if xs else 0

# ---- recurring concept families (exact template ideas reused across channels)
CONCEPTS = [
 ("peanut_butter_daily", r"peanut butter"), ("stool_stuck", r"stool.{0,12}stuck|stuck.{0,8}(stool|poop)|can't pass stool"),
 ("sleep_position_stroke", r"sleep(ing)? (position|like this|on your)|snore like"), ("morning_habit_heart", r"(every|this|these \d|dangerous|30.second|\d) ?morning (habit|mistake)|do this every morning|millions (still )?(do|make) this|morning habits"),
 ("shower_bath_frequency", r"(shower|bath)"), ("hygiene_smell", r"hygiene mistakes"), ("golden_habits", r"golden habits"),
 ("drink_water_night_pee", r"drink water.{0,40}(night|getting up)|wake up to pee|waking up to pee|pee at night|bladder will calm|nighttime bathroom"),
 ("throat_mucus", r"mucus|phlegm"), ("dry_mouth", r"dry mouth"), ("turn_80", r"turn(ing)? 80|reach 80|after 80\b|things happen.{0,30}80"),
 ("deadly_surgeries", r"surger(y|ies)|surgical"), ("checkups_never", r"(checkups|medical tests).{0,40}(never|think twice|unnecessary)|medical checkups"),
 ("fruit_eyes", r"(fruit|food|vegetable|seed).{0,40}(eye|vision)"), ("fruit_kidneys", r"(fruit|vegetable|drink|food|snack)s?.{0,45}(kidney|creatinine)|kidneys (are begging|will thank|love)"),
 ("reheat_foods", r"reheat"), ("feet_diabetes_signs", r"(feet|foot).{0,40}diabet"), ("pills_heart_risk", r"pills.{0,60}(heart|stroke)|pain ?(pill|killer).{0,40}heart"),
 ("bp_med_names", r"amlodipine|losartan|lisinopril|metoprolol|beta blockers"), ("ideal_blood_pressure", r"(ideal|safest|target|too high|normal).{0,30}blood pressure|blood pressure target|is 150 normal"),
 ("stroke_day_before", r"stroke looks like"), ("walk_change", r"(change|walk).{0,25}(how you walk|walk like|walking change)|how you walk"),
 ("anesthesia", r"anesthesia|going under"), ("eggs", r"\beggs?\b"), ("died_in_sleep", r"died in his sleep"), ("bedtime_elderly", r"what time should the elderly"),
 ("nails_signs", r"nails?\b"), ("choking_alone", r"choking"), ("magnesium", r"magnesium"), ("plain_water_bloodflow", r"plain water"),
 ("cloves", r"clove"), ("colon_flush", r"(flush|kg of|lbs of|colon cleanse|cleanse your).{0,40}(stool|waste|colon|poop)|toxic waste"),
 ("ages_75_85", r"ages 75"), ("cant_walk_straight", r"walk straight"), ("meds_memory", r"(med(ication)?s|drugs|pills).{0,45}(memory|dementia)|memory.{0,30}(drugs|medications)"),
 ("muscle_loss_food", r"(muscle|sarcopenia|legs weaken)"), ("collagen_skin_hair", r"collagen|wrinkle|hair"),
]
TOPICS = [
 ("heart_bp_stroke", r"heart|blood pressure|stroke|cardiolog|arter|cholesterol|afib|atrial|hypotension|\bbp\b|circulation|blood flow"),
 ("digestion_bowel", r"stool|constipat|poop|colon|gut|bowel|laxative|diverticul|reflux|diarrhea"),
 ("urinary_bladder", r"pee\b|bladder|urin|urolog|prostate|incontinence|uti"), ("kidney", r"kidney|creatinine|nephrolog"),
 ("diabetes_sugar", r"diabet|blood sugar|metformin|insulin"), ("brain_memory", r"memory|dementia|alzheimer|brain|cognitive|parkinson|tremor|delirium"),
 ("mobility_falls_exercise", r"walk|exercise|fall|balance|legs?\b|knee|chair|muscle|sarcopenia|neuropathy|steps|stand up|numb"),
 ("medications", r"pill|medication|\bmeds\b|drug|amlodipine|losartan|lisinopril|statin|tylenol|aspirin|painkiller|supplement|vitamin|b12|magnesium"),
 ("sleep", r"sleep|bed ?time|go to bed|nap|3 ?am|wake up at"), ("eyes_hearing", r"eye|vision|cataract|hearing|earwax"),
 ("hygiene_daily_living", r"shower|bath|hygiene|smell|driving"), ("procedures_tests_hospital", r"surger|anesthesia|checkup|medical test|lab test|hospital|blood test|vaccine|covid|flu"),
 ("food_remedy", r"\beat|food|fruit|vegetable|egg|peanut|clove|garlic|spice|seed|oil|juice|drink|coffee|water|turmeric|honey|sardine|olive|cheese|banana|onion|pepper|breakfast"),
 ("aging_longevity", r"aging|longevity|long life|turn 80|after 80|ages 75|golden habits|shrink|103"),
 ("skin_hair", r"skin|wrinkle|collagen|hair"), ("caregiving_admin", r"parent|medicare|senior care|adl|care manager"),
]
FORMATS = [
 ("authority_prefix", r"^(cardiologist|doctor|doctors|urologist|neurologist|nephrologist|surgeon|kidney doctor|heart surgeon|orthopedic surgeon)[^:—-]{0,25}(warn|reveal|explain|alert|beg)"),
 ("authority_any", r"cardiologist|doctor|urologist|neurologist|nephrologist|surgeon|geriatrician|\bdr\b"),
 ("age_qualifier", r"(after|over|past|at) \d{2}\b|ages \d{2}|\d{2}\+|turn \d{2}|\d{2}-year"), ("number_list", r"(^|\s)#?\d{1,2} (\w+ ){0,3}(signs|habits|mistakes|foods|things|pills|facts|ways|exercises|fruits|vegetables|drinks|causes|reasons|tests|checkups|surgeries|medications|tips|steps|symptoms|changes|traps|rules|seeds|types)"),
 ("warning_negative", r"never|stop\b|deadly|danger|warn|mistake|risk|kill|fatal|avoid|beware|don.t|destroy|poison|wrong"),
 ("question", r"\?"), ("this_pointer", r"\bTHIS\b|\bthis (one|1|simple|food|fruit|seed|way|morning|sleeping)"), ("caps_word", None),
 ("multiplier_claim", r"\d[\d,]*x\b|100%|99%|irreversible|instantly|overnight|in \d+ (minutes|hour)"),
 ("not_what_you_think", r"not what you think|real reason|\breal\b|truth|nobody|no one tells|won.t tell|never told|doctors hide|secret"),
 ("explainer_colon", r"^[^:?!]{8,60}: (causes|symptoms|what|how|when|which)|explained|understanding|what.s the difference"),
]
for r in rows:
    t = r["title"]; tl = t.lower()
    r["concepts"] = [n for n, p in CONCEPTS if re.search(p, tl)]
    r["topics"] = [n for n, p in TOPICS if re.search(p, tl)] or ["other"]
    r["formats"] = [n for n, p in FORMATS if p and re.search(p, t if n == "this_pointer" else tl)]
    if re.search(r"\b[A-Z]{4,}\b", t): r["formats"].append("caps_word")
    r["title_len"] = len(t)

# ---- within-channel baseline and outliers (long-form only; baseline = median of the channel's OTHER long-form videos)
bych = collections.defaultdict(list)
for r in rows:
    if not r["is_short"]: bych[r["channel"]].append(r)
for c, vs in bych.items():
    for r in vs:
        others = [x["views"] for x in vs if x is not r]
        b = med(others) or 1
        r["base"] = b; r["mult"] = r["views"] / b
        r["immature"] = int(r["age_d"] < 7)
        r["tier"] = "OUTLIER_10X" if r["mult"] >= 10 else "OUTLIER_5X" if r["mult"] >= 5 else "ABOVE_2X" if r["mult"] >= 2 else "BASELINE" if r["mult"] >= 0.5 else "BELOW_HALF"
for r in rows:
    r.setdefault("base", ""); r.setdefault("mult", ""); r.setdefault("tier", "SHORT"); r.setdefault("immature", 0)

# ---- template network (channels linked by identical normalized titles)
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
tm = collections.defaultdict(set)
for r in comp: tm[norm(r["title"])].add(r["channel"]); find(r["channel"])
for t, cs in tm.items():
    cs = list(cs)
    cs = sorted(cs)  # deterministic root label (set order varies with hash seed)
    for c in cs[1:]: par[find(c)] = find(cs[0])
# concept-level sharing: channel pairs sharing >=4 of the template concepts
NETC = {"peanut_butter_daily","stool_stuck","sleep_position_stroke","hygiene_smell","golden_habits","throat_mucus","dry_mouth","turn_80","deadly_surgeries","checkups_never","fruit_eyes","reheat_foods","feet_diabetes_signs","stroke_day_before","died_in_sleep","bedtime_elderly","nails_signs","choking_alone","shower_bath_frequency","walk_change","ages_75_85","cant_walk_straight"}
cc = collections.defaultdict(set)
for r in comp:
    for k in r["concepts"]:
        if k in NETC: cc[r["channel"]].add(k)
chs = sorted(bych.keys() - {"Decode Your Heart - Dr. Rehan"})
soft = {c: [d for d in chs if d != c and len(cc[c] & cc[d]) >= 4] for c in chs}
groups = collections.defaultdict(list)
for c in chs: groups[find(c)].append(c)

# ---- outputs
cols = ["role","channel","video_id","title","published","age_d","duration_s","is_short","views","vpd","base","mult","tier","immature","likes","comments","tx_words","title_len","topics","concepts","formats"]
with open(f"{D}/02-benchmark-video-table.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols)
    for r in sorted(rows, key=lambda r: (r["role"], r["channel"], -r["views"])):
        w.writerow([("|".join(r[c]) if isinstance(r[c], list) else (round(r[c], 2) if isinstance(r[c], float) else r[c])) for c in cols])

P = print
P("=== CHANNEL BENCHMARK (long-form) ===")
P("channel | n | median | mean | top1 | top1_share% | >=10k% | >=100k% | <1k% | out5x | out10x | uploads/wk | med_dur_min | med_words")
cov = {r["channel"]: r for r in csv.DictReader(open(f"{D}/01-channel-coverage.csv"))}
chan_stats = {}
for c in sorted(bych, key=lambda c: -med([x["views"] for x in bych[c]])):
    vs = bych[c]; v = sorted((x["views"] for x in vs), reverse=True); n = len(v)
    d0 = min(dt.date.fromisoformat(x["published"]) for x in vs); d1 = max(dt.date.fromisoformat(x["published"]) for x in vs)
    wk = max((d1 - d0).days / 7, 1)
    s = dict(n=n, median=int(med(v)), mean=int(st.mean(v)), top1=v[0], top1_share=round(100 * v[0] / max(sum(v), 1)),
             p10k=round(100 * sum(x >= 10000 for x in v) / n), p100k=round(100 * sum(x >= 100000 for x in v) / n), lt1k=round(100 * sum(x < 1000 for x in v) / n),
             o5=sum(1 for x in vs if x["mult"] >= 5), o10=sum(1 for x in vs if x["mult"] >= 10), upw=round(n / wk, 1),
             dur=round(med([x["duration_s"] for x in vs]) / 60), words=int(med([x["tx_words"] for x in vs if x["tx_words"]])))
    chan_stats[c] = s
    P(c, "|", " | ".join(str(x) for x in s.values()), "| subs", cov[c]["subscribers"] or "-", "| views/sub(median)", round(s["median"] / int(cov[c]["subscribers"]), 2) if cov[c]["subscribers"] else "-")
P("\n=== TEMPLATE NETWORK ===")
for g, m in sorted(groups.items(), key=lambda x: -len(x[1])): P(len(m), m)
P("soft links (>=4 shared template concepts):"); [P("  ", c, "->", len(cc[c]), "concepts; linked to", len(s)) for c, s in soft.items()]

P("\n=== CONCEPT FAMILIES (long-form competitor) ===")
P("concept | videos | channels | median | max | >=100k | <1k | first_mover_is_top | spearman(order,views)")
fam = {}
for name, _ in CONCEPTS:
    vs = [r for r in lf if name in r["concepts"]]
    if len(vs) < 3: continue
    v = [x["views"] for x in vs]; chn = {x["channel"] for x in vs}
    o = sorted(vs, key=lambda x: x["published"]); top = max(vs, key=lambda x: x["views"])
    # rank correlation between publish order and views
    n = len(o); rv = {id(x): i for i, x in enumerate(sorted(o, key=lambda x: -x["views"]))}
    rho = 1 - 6 * sum((i - rv[id(x)]) ** 2 for i, x in enumerate(o)) / (n * (n * n - 1)) if n > 2 else 0
    fam[name] = dict(videos=n, channels=len(chn), median=int(med(v)), max=max(v), ge100k=sum(x >= 100000 for x in v), lt1k=sum(x < 1000 for x in v), first_is_top=int(o[0] is top), rho=round(rho, 2), top=f'{top["channel"]}|{top["video_id"]}|{top["published"]}')
for k, s in sorted(fam.items(), key=lambda x: -x[1]["ge100k"]): P(k, "|", " | ".join(str(x) for x in s.values()))

def table(label, key, pool):
    P(f"\n=== {label} ===\nname | n | channels | median_views | median_mult | share_out5x% | >=100k%")
    agg = collections.defaultdict(list)
    for r in pool:
        for k in r[key]: agg[k].append(r)
    for k, vs in sorted(agg.items(), key=lambda x: -med([y["mult"] for y in x[1]])):
        P(k, "|", len(vs), "|", len({x["channel"] for x in vs}), "|", int(med([x["views"] for x in vs])), "|", round(med([x["mult"] for x in vs]), 2), "|", round(100 * sum(x["mult"] >= 5 for x in vs) / len(vs)), "|", round(100 * sum(x["views"] >= 100000 for x in vs) / len(vs)))
mature = [r for r in lf if not r["immature"]]
P("\nmature long-form competitor videos:", len(mature), "of", len(lf), "| overall share out5x%", round(100 * sum(r["mult"] >= 5 for r in mature) / len(mature)), "| >=100k%", round(100 * sum(r["views"] >= 100000 for r in mature) / len(mature)))
table("TOPICS (mature long-form)", "topics", mature)
table("TITLE FORMAT FEATURES (mature long-form)", "formats", mature)
P("\n=== DURATION BANDS ===")
for lo, hi in [(1, 8), (8, 12), (12, 16), (16, 20), (20, 25), (25, 30), (30, 45), (45, 999)]:
    vs = [r for r in mature if lo * 60 <= r["duration_s"] < hi * 60]
    if vs: P(f"{lo}-{hi}m | n {len(vs)} | channels {len({x['channel'] for x in vs})} | median views {int(med([x['views'] for x in vs]))} | median mult {round(med([x['mult'] for x in vs]),2)} | out5x% {round(100*sum(x['mult']>=5 for x in vs)/len(vs))}")
P("\n=== TITLE LENGTH ===")
for lo, hi in [(0, 50), (50, 70), (70, 90), (90, 200)]:
    vs = [r for r in mature if lo <= r["title_len"] < hi]
    P(f"{lo}-{hi} chars | n {len(vs)} | median mult {round(med([x['mult'] for x in vs]),2)} | out5x% {round(100*sum(x['mult']>=5 for x in vs)/len(vs))}")
P("\n=== UPLOAD ORDER WITHIN CHANNEL (does position in channel life matter?) ===")
q = collections.defaultdict(list)
for c, vs in bych.items():
    if c.startswith("Decode"): continue
    o = sorted(vs, key=lambda x: x["published"])
    for i, r in enumerate(o): q[min(int(4 * i / len(o)), 3)].append(r["mult"])
for k in sorted(q): P(f"quartile {k+1} of channel timeline | n {len(q[k])} | median mult {round(med(q[k]),2)} | out5x% {round(100*sum(x>=5 for x in q[k])/len(q[k]))}")
P("\n=== TOP 40 OUTLIERS (mult>=5, views>=50k) ===")
for r in sorted([r for r in lf if r["mult"] >= 5 and r["views"] >= 50000], key=lambda r: -r["views"])[:40]:
    P(f'{r["views"]} | x{round(r["mult"],1)} | {r["channel"]} | {r["video_id"]} | {r["published"]} | {r["duration_s"]//60}m | {r["title"][:80]}')
json.dump(dict(channels=chan_stats, families=fam, network={k: v for k, v in groups.items()}), open(f"{D}/02-benchmark-summary.json", "w"), indent=1)
