"""Build forensic-v2 deliverables from the evidence layers.

Inputs (all in forensic-v2/): VERIFIED-FACTS.json, TRANSCRIPT-FORENSICS.json,
THUMBNAIL-MATRIX.json, MATCHED-PAIRS-SCRIPT-FORENSICS.json, DUPLICATE-NETWORK.json,
trends/TRENDS-LIVE.jsonl, external/*.txt, scripts/synthesis_data.py, plus the pass-1
master table (topic tags) and 07-first-50-videos.json.

Outputs: JSON layers + EVIDENCE-REGISTER-V2.json + SENIOR-HEALTH-FORENSIC-WORKBOOK-V2.xlsx
"""
import json, re, glob, math, statistics as st, sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).parent))
import synthesis_data as S

J = lambda p: json.load(open(HERE / p))
FACTS = J("VERIFIED-FACTS.json")
V = {v["video_id"]: v for v in FACTS["videos"]}
TX = {r["video_id"]: r for r in J("TRANSCRIPT-FORENSICS.json")}
THM = J("THUMBNAIL-MATRIX.json")
TH = {r["video_id"]: r for r in THM["rows"]}
MP = J("MATCHED-PAIRS-SCRIPT-FORENSICS.json")
DUP = J("DUPLICATE-NETWORK.json")["pairs"]
GT = [json.loads(l) for l in open(HERE / "trends/TRENDS-LIVE.jsonl")]
MASTER = {v["video_id"]: v for v in json.load(open(HERE.parent / "01-master-video-table.json"))}
TITLEF = {v["video_id"]: v for v in json.load(open(HERE.parent / "02-VIDEOS-WITH-TITLE-FEATURES.json"))}
SAMPLE = {v["video_id"] for v in json.load(open(HERE.parent / "DEEP-ANALYSIS-SAMPLE.json"))}
F50 = json.load(open(HERE.parent / "07-first-50-videos.json"))
AS_OF = "2026-09-25"


def dump(name, obj):
    json.dump(obj, open(HERE / name, "w"), indent=1, ensure_ascii=False)


# ------------------------------------------------------------------ external benchmarks
def parse_num(s):
    m = re.match(r"([\d.]+)\s*([km]?)", s.strip().lower())
    if not m:
        return None
    return int(float(m.group(1)) * {"": 1, "k": 1e3, "m": 1e6}[m.group(2)])


EXT = []
for f in sorted(glob.glob(str(HERE / "external/C[0-9]*.txt"))):
    cluster = Path(f).stem
    head = open(f).readline().strip()
    for line in open(f):
        if line.startswith("#") or "~" not in line:
            continue
        p = [x.strip() for x in line.split("~")]
        vm = re.search(r"([\d.]+[km]?) views|No views|(\d+) view\b", p[4] if len(p) > 4 else "")
        views = 0 if "No views" in line else parse_num(vm.group(1) or vm.group(2)) if vm else None
        age = (p[4].split("|")[1].strip() if len(p) > 4 and "|" in p[4] else "UNKNOWN")
        internal = p[3] in ("/@Dr.Ares-YT", "/@Dr.EliasYT", "/@Health.Hub.Senior", "/@DrThomasSeniorHealthTips")
        EXT.append({"cluster": cluster, "title": p[0], "video_ref": p[1], "channel": p[2], "handle": p[3],
                    "views_live": views, "age_relative": age, "format": "SHORT" if "short" in p[1] else "LONG",
                    "is_cohort_channel": internal, "retrieved": "2026-09-24T21:05-21:18Z (LIVE YouTube search)",
                    "source_file": f"forensic-v2/external/{Path(f).name}", "query_line": head})


def ext_role(e, cluster_rows):
    t = e["title"].lower()
    same_title = sum(1 for x in cluster_rows if x is not e and x["title"].lower()[:40] == t[:40])
    v = e["views_live"] or 0
    if e["is_cohort_channel"]:
        return "COHORT_CHANNEL_LIVE_RECHECK"
    if v >= 1_000_000 and ("year" in e["age_relative"]):
        return "OLDER_EVERGREEN_WINNER"
    if v >= 500_000:
        return "LARGE_WINNER"
    if v >= 100_000 and ("month" in e["age_relative"] or "week" in e["age_relative"] or "day" in e["age_relative"]):
        return "RECENT_WINNER"
    if v >= 50_000:
        return "MEDIUM_WINNER"
    if v < 1_000 and same_title:
        return "CONTENT_MILL_DUPLICATE"
    if v < 1_000:
        return "FAILED_COPY_OR_LOW_REACH"
    return "MID_PERFORMER"


byc = defaultdict(list)
for e in EXT:
    byc[e["cluster"]].append(e)
for c, rows in byc.items():
    for e in rows:
        e["role"] = ext_role(e, rows)
dump("EXTERNAL-BENCHMARKS.json", {"method": "Live YouTube search result pages parsed in the in-app browser; views as displayed (rounded by YouTube); roles assigned by rule (see build_outputs.ext_role). Channel pages in external/CH_channel_pages.txt.",
                                  "videos": EXT})

SMALL_BREAKOUTS = [
    {"id": "SB-01", "channel": "Fit Lit Health (@FitLitHealth)", "subs": "65.9k", "baseline_before": "70-2,900 views on 18 uploads 8-9 months ago (6-7 min)",
     "breakout": "~11 of ~20 uploads >250K in 5 weeks (max 785K)", "topic": "kidney/gut/teeth/eyesight 'Eat THIS 1 food' remedies", "title": "Eat THIS 1 Food That Flushes Kidney Toxins Before It's Too Late! (785K)",
     "thumbnail": "LIVE_WEB_VISUAL J8zNi4_CqgA: Urdu text ('this fruit fixes the eyes! cataract gone overnight!'), woman in hijab, cataract eye + dates", "script_opening": "UNKNOWN (captions hi:asr; transcript panel unavailable unsigned) - audience is South-Asian-language, not a like-for-like US comparator", "trend_state": "creatinine interest at 5-yr high (GT-14); eyesight copy published 2026-08-27, 11 days after the Elias original",
     "competition": "copied titles from Dr. Elias (eyesight) and cohort templates", "channel_age": "UNKNOWN exact; >=9 months", "follow_up": "Sustained - not one hit",
     "next_videos_benefited": "YES (streak)", "formula_replicated": "PARTIAL (misses: 3.9K, 8.4K, 34K)", "evidence": "external/CH_channel_pages.txt"},
    {"id": "SB-02", "channel": "Dr. Aliza Wright Senior Health (@Dr.AlizaWrightSeniorHealth)", "subs": "22.9k", "baseline_before": "86-4,300 views on early hypertension uploads (~4 months ago)",
     "breakout": "941K on 'Taking Amlodipine, Losartan, or Lisinopril...' (~3 months ago); 175K, 103K", "topic": "named BP medications", "title": "Taking Amlodipine, Losartan, or Lisinopril for Blood Pressure? Here's What Many Seniors Don't Know",
     "thumbnail": "LIVE_WEB_VISUAL 6nyp-aRcyNs: identical to cohort thumbnail #39 incl. typo 'LOSARTON'", "script_opening": "UNKNOWN (transcript panel unavailable unsigned); YouTube 'AI' label shown", "trend_state": "published 2026-05-31; GT-12 flat-high evergreen; HX-03 recall classified 2026-06-02 (2 days AFTER upload - not a trigger)", "competition": ">=9 same-title copies (3-5.1K); cohort persona channel re-posted title+thumbnail 5 days later (160 views)",
     "channel_age": "~4 months", "follow_up": "Later uploads 469-10K", "next_videos_benefited": "PARTIAL (2 more >100K then decline)", "formula_replicated": "NO on cohort persona channel (160 views)",
     "evidence": "external/CH_channel_pages.txt; external/C07_bp_meds.txt"},
    {"id": "SB-03", "channel": "Gentle Health (@GentleHealth)", "subs": "29.4k", "baseline_before": "typical 300-10K",
     "breakout": "602K bath video (~1 y); 385K peanut butter; 145K walking copy", "topic": "daily-living + nutrition in 2-4 minute format", "title": "How Often Should Seniors Take a Bath After 70? 7 Shocking Facts You Need to Know! (602K)",
     "thumbnail": "LIVE_WEB_VISUAL kzKfVeosHS4: photoreal older male doctor, 'How often Should Seniors Shower' + arrow", "script_opening": "UNKNOWN (transcript panel unavailable unsigned); 150-second video published 2025-07-06", "trend_state": "bathing: zero web search (GT-20)", "competition": "its own title later copied by Ares (527K) and Elias (188K)",
     "channel_age": "UNKNOWN (273 videos)", "follow_up": "Re-runs 33K-39K and 555", "next_videos_benefited": "NO (re-runs decayed)", "formula_replicated": "PARTIAL", "evidence": "external/C10_bathing.txt; CH_channel_pages.txt"},
    {"id": "SB-04", "channel": "Dr. Okoro (cohort, UCMJxAeBJ0d1JC937de1eZ0Q)", "subs": "3,800 at scrape", "baseline_before": "25 uploads, 114-801 views (median ~200)",
     "breakout": "494,473 foot-signs (2026-05-16); 100,852 neuropathy (2026-06-03)", "topic": "diabetes feet; neuropathy exercises", "title": "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60",
     "thumbnail": "LIVE_WEB_VISUAL #93", "script_opening": "ACTUAL: 'Stop what you're doing for 30 seconds and look down at your feet...' + Walter case (A1C 9.2)", "trend_state": "GT-05/GT-27 elevated but flat; neuropathy GT-24 peak week",
     "competition": "neuropathy title pre-existed at 1.3M (TopHealthTips)", "channel_age": "58 days at breakout (joined 2026-03-19)", "follow_up": "11.3K kidney (bridge to breakout); then decay to ~75 median",
     "next_videos_benefited": "SHORT-LIVED (~3 weeks)", "formula_replicated": "NO (form copies 205-460)", "evidence": "VERIFIED-FACTS.json; TRANSCRIPT-FORENSICS.json"},
    {"id": "SB-05", "channel": "Dr. Aliza Wright | Advice (cohort, UCXZi5JVeuTluazF-fYqQgNA)", "subs": "UNKNOWN", "baseline_before": "median 217",
     "breakout": "219,009 (1,009x) on copied Doctor Thomas title, 7 days after the original", "topic": "walking/falls", "title": "One SIMPLE Change to How You Walk That Could Save Your Life | After 70",
     "thumbnail": "LIVE_WEB_VISUAL #22 (copies Thomas #3 text)", "script_opening": "ACTUAL: 'Look down at your feet right now. If your toes hit the floor before your heel...'", "trend_state": "GT-28 fall-prevention plateau",
     "competition": "Thomas original 1.0M", "channel_age": "~3 weeks at breakout (first upload 2026-06-05)", "follow_up": "'Walk straight' copy 20.7K (95x); then 31-1,143",
     "next_videos_benefited": "ONE follow-up", "formula_replicated": "NO", "evidence": "VERIFIED-FACTS.json; DUPLICATE-NETWORK.json"},
]
dump("SMALL-CHANNEL-BREAKOUTS.json", SMALL_BREAKOUTS)

# ------------------------------------------------------------------ duplicate network summary
sister = []
for p in DUP:
    if p["same_channel"] or p["title_similarity"] < 0.8:
        continue
    a = (p["date_a"], p["channel_a"], p["views_a"], p["multiple_a"], p["title_a"])
    b = (p["date_b"], p["channel_b"], p["views_b"], p["multiple_b"], p["title_b"])
    first, second = sorted([a, b])
    sister.append({"first_date": first[0], "first_channel": first[1], "first_views": first[2], "first_multiple": first[3],
                   "second_date": second[0], "second_channel": second[1], "second_views": second[2], "second_multiple": second[3],
                   "title": first[4], "days_apart": p["days_apart"], "title_similarity": p["title_similarity"],
                   "transcript_5gram_jaccard": p["transcript_5gram_jaccard"], "second_mover_won": second[2] > first[2],
                   "classification": "SAME_TITLE_DIFFERENT_SCRIPT" if (p["transcript_5gram_jaccard"] or 0) < 0.08 else p["classification"]})
sister.sort(key=lambda r: r["first_date"])
sm = [r for r in sister if r["first_channel"] != r["second_channel"]]
dup_summary = {"pairs_checked": len(DUP), "cross_channel_same_title_pairs": len(sm),
               "second_mover_won": sum(r["second_mover_won"] for r in sm),
               "second_mover_lost": sum(not r["second_mover_won"] for r in sm),
               "max_transcript_jaccard_cross_channel": max((p["transcript_5gram_jaccard"] for p in DUP if not p["same_channel"] and isinstance(p["transcript_5gram_jaccard"], float)), default=None),
               "thumbnail_text_duplicates_observed": ["Thomas #3 -> Aliza #22/#24 (identical text)", "Ares #49 = Elias #76", "Ares #62 = Elias #77", "Ares #53 = Elias #79 (same title mismatch)",
                                                      "Ares #60 = Elias #80", "Ares #50 = Elias #81 (same typo 'ONES')", "Ares #65 ~ Elias #72", "Okoro #93 ~ Ares #59", "Okoro #96 = Elias #88 ~ Ares #71"],
               "external_copy_clusters": ["C03 foot-signs: >=6 copies 2-53 views", "C05 nocturia: >=6 copies 1-762 views", "C07 amlodipine: >=9 channels 3-5.1K (origin 941K)",
                                          "C12 anesthesia: >=9 copies 1-2.3K", "C13 pills: >=8 copies 1-142K", "C10 bathing: >=7 channels 89-602K"],
               "persona_clones": ["'Dr. Aliza Wright' on 2 channels (941K vs 160 on same title)", "'Dr. Ares Smith Senior Health!' (1 view)", "'Wellness After 70 - Dr. Elias' (122 views)",
                                  "Real public-figure names attached to unaffiliated channels in titles/channel names ('Dr. William Li', 'Dr. Jason Fung') - identity/affiliation NOT verified"],
               "rows": sm}
dump("DUPLICATE-NETWORK-SUMMARY.json", dup_summary)

# ------------------------------------------------------------------ trends register
WITHDRAWN = ["'walking posture seniors' (Pass-1 'estimated')", "'fall prevention' seasonal estimate", "'digestion problems seniors' estimate", "'gut health remedies' rising estimate",
             "'foot signs diabetes' Unknown", "'diabetes symptoms' Estimated 40-60", "'warning signs + diabetes' Estimated 50-70", "+2 unnamed partial estimates (FORENSIC-EXPANSION-FINAL-STATUS.md)"]
dump("TRENDS-REGISTER.json", {"note": "Google Trends 0-100 = normalized relative interest within the query/geo/time window, NOT absolute search volume. Only live, observed queries count as evidence.",
                               "live_investigations": GT, "withdrawn_estimated_observations": WITHDRAWN,
                               "pass1_live_queries_status": "Pass-1 'clove water (US,12mo)' and 'balance exercises for seniors (US,12mo)' superseded by GT-01/GT-07 (5y, same terms)"})

# ------------------------------------------------------------------ simple synthesis dumps
dump("MEDICAL-VALIDATION.json", [dict(zip(["id", "claim", "appears_in", "source", "source_type", "verdict", "safe_reframing"], m)) for m in S.MEDICAL])
dump("HISTORICAL-CONTEXT.json", [dict(zip(["id", "event", "date", "source", "video", "distance_from_upload", "possible_relevance", "confidence"], h)) for h in S.HISTORY])
dump("DS-000011-TRACE-MATRIX.json", [dict(zip(["knowledge_unit", "framework", "videos_tested_against", "observed_evidence", "counterexample", "result", "contributes_to"], r)) for r in S.DS11])
dump("DS-000018-CLAIM-MATRIX.json", [dict(zip(["claim_id", "claim", "original_source", "claim_status", "official_youtube_support", "internal_senior_health_evidence", "external_evidence", "counterexample", "practical_implication"], r)) for r in S.DS18])
dump("DS-000031-FRAMEWORK-MATRIX.json", [dict(zip(["framework", "concept_ids", "internal_supporting_example", "internal_counterexample", "external_supporting_example", "limitation", "senior_health_implication"], r)) for r in S.DS31])
f50 = []
for v in F50:
    d, why = S.FIRST50_EVAL[v["video_number"]]
    f50.append({**v, "decision": d, "decision_evidence": why})
dump("FIRST-50-REEVALUATED.json", {"existing": f50, "new_concepts": [dict(zip(["id", "pillar", "concept", "evidence", "medical_risk", "discovered_from"], n)) for n in S.NEW_CONCEPTS],
                                   "counts": dict(Counter(x["decision"] for x in f50))})
dump("FIRST-10-FINAL.json", S.FIRST10)

# ------------------------------------------------------------------ analytics tables
def med(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return round(st.median(xs), 3) if xs else None


CH = FACTS["channels"]
videos = sorted(FACTS["videos"], key=lambda v: (v["channel"], v["published_at_raw"]))
for v in videos:
    v["topic_tags"] = MASTER.get(v["video_id"], {}).get("topic_tags", ["UNCLASSIFIED"])
    v["tier"] = MASTER.get(v["video_id"], {}).get("performance_tier", "UNKNOWN")

topic_rows = defaultdict(list)
for v in videos:
    for t in v["topic_tags"] or ["UNCLASSIFIED"]:
        topic_rows[t].append(v)
TOPICS = []
for t, vs in sorted(topic_rows.items(), key=lambda x: -len(x[1])):
    m = [v["outlier_multiple_vs_channel_median"] for v in vs]
    TOPICS.append({"topic": t, "videos": len(vs), "channels": len({v["channel"] for v in vs}), "median_multiple": med(m),
                   "hit_rate_ge3x": round(sum(x >= 3 for x in m) / len(m), 3), "failure_rate_lt0_5x": round(sum(x < 0.5 for x in m) / len(m), 3),
                   "max_views": max(v["views"] for v in vs), "total_views": sum(v["views"] for v in vs)})

# title features recomputed within-channel (regex flags from pass-1 file; has_age_marker flagged as duplicate of has_number)
TF = []
feats = [k for k in next(iter(TITLEF.values())) if k.startswith("has_")]
for f in feats:
    a = [V[k]["outlier_multiple_vs_channel_median"] for k, r in TITLEF.items() if r[f]]
    b = [V[k]["outlier_multiple_vs_channel_median"] for k, r in TITLEF.items() if not r[f]]
    TF.append({"feature": f, "n_with": len(a), "median_multiple_with": med(a), "median_multiple_without": med(b),
               "hit_rate_with": round(sum(x >= 3 for x in a) / len(a), 3) if a else None,
               "note": "REGEX BUG: identical to has_number on all 306 rows" if f == "has_age_marker" else ""})

# hook / script archetypes
def script_arch(r):
    p = r.get("per_1000_words") or {}
    if p.get("story", 0) >= 1.0:
        return "STORY_LED"
    if p.get("enumeration", 0) >= 4.0:
        return "LIST_LED"
    if p.get("specific_study_claim", 0) >= 1.0 or p.get("credibility", 0) >= 5:
        return "EVIDENCE_CLAIM_LED"
    return "EXPLAINER"


HK, SC = defaultdict(list), defaultdict(list)
for r in TX.values():
    if r.get("transcript_status") != "PRESENT":
        continue
    r["script_archetype"] = script_arch(r)
    HK[r["hook_archetype"]].append(r["outlier_multiple_vs_channel_median"])
    SC[r["script_archetype"]].append(r["outlier_multiple_vs_channel_median"])
arch = lambda D: [{"archetype": k, "n": len(v), "median_multiple": med(v), "hit_rate_ge3x": round(sum(x >= 3 for x in v) / len(v), 3), "fail_rate_lt0_5x": round(sum(x < 0.5 for x in v) / len(v), 3)} for k, v in sorted(D.items(), key=lambda x: -len(x[1]))]
HOOKS, SCRIPTS = arch(HK), arch(SC)
dump("ARCHETYPE-PERFORMANCE.json", {"hook_archetypes": HOOKS, "script_archetypes": SCRIPTS, "topic_performance": TOPICS, "title_features_within_channel": TF,
                                    "note": "All archetypes are TRANSCRIPT_LEXICAL_HEURISTIC; multiples are views / own-channel median, so channel size is removed but channel era/timing is not."})

# ------------------------------------------------------------------ data-quality corrections
DQ = [
    ("DQ-01", "SENIOR-HEALTH-CASE-STUDIES.md CS1", "Dr. Okoro launch '~2026-07'", "Channel joined 2026-03-19 (raw Apify channelJoinedDate); first upload 2026-03-20 (EnSloA7tU3Q); breakout 2026-05-16 = day 58", "VERIFIED_FACTS channels.UCMJx...; raw DS-000028 dataset.json"),
    ("DQ-02", "CS1", "Duration 'estimated 10-15 min'", "911 s (15:11) - registry videos.duration_seconds", "registry DB"),
    ("DQ-03", "CS1", "'48 pre-breakout videos'; '18 post'", "25 before, 40 after (66 total incl. 1 Short)", "registry DB"),
    ("DQ-04", "CS1/CS4", "'4 Heart Warning Signs...Face' posted 5-20 as immediate follow-up", "Posted 2026-07-11 (56 days later); '6 Everyday Foods...' 2026-07-19; the actual immediate follow-ups were 'Unnecessary tests' (05-17, 8.0x), neuropathy (06-03, 100,852)", "registry DB"),
    ("DQ-05", "CS1/CS4", "'Subsequent attempts = near-total failure'; 'luck more than formula'", "Second hit neuropathy 100,852 (507x) and kidney 11,319 (57x) followed within 20 days; decay came later", "registry DB"),
    ("DQ-06", "CS1", "'Channel median 199 (recent-10)'", "199 = all-video median; recent-10 median = 75", "VERIFIED-FACTS.json"),
    ("DQ-07", "CS1", "Title authority 'Cardiologist'", "Script self-identifies as 'a heart surgeon' ('Dr. Marcus Acuora/Acord' ASR spellings); authority wording inconsistent between title and script", "TRANSCRIPT CJxCjygEnmo"),
    ("DQ-08", "CS2", "Clove duration 'estimated 8-12 min'", "542 s (9:02)", "registry DB"),
    ("DQ-09", "CS2", "Clove video treated as novel one-off; 'Phase 1 20-50K median'; 'maintains higher baseline post-hit'", "4th clove hit in an 8-month franchise (1.09M Sep-2025, 1.06M Jan-2026, 555K Feb-2026); Sep-Nov 2025 monthly medians 2.3K-3.2K; median before 9,539 vs after 9,418 (no lift)", "registry DB"),
    ("DQ-10", "CS2", "Script 'expected structure'", "Replaced by actual transcript: conspiracy hook, symptom checklist, eugenol+chlorogenic 'synergy', dated benefit ladder, mid-video subscribe ask at ~43%, protocol, contraindications; title '10 minutes' vs script '15 minutes'", "TRANSCRIPT KPigGh9_gbU"),
    ("DQ-11", "CS3", "Kidney pair 11,370 vs 46 views, 247x", "11,319 vs 45 = 251.5x; loser posted 42 days later in channel decay; stored transcript for loser concatenated 8 caption tracks (21,447 words) - parser now keeps first (English) track (2,573 words)", "registry DB; transcript_forensics.first_track"),
    ("DQ-12", "FORENSIC-DEEP-DIVE Part 2 + status", "Title features 'curiosity gap 3.5x, named food 3.1x, doctor specialty 3.5x'", "Raw-view comparisons were channel-confounded; within-channel medians: curiosity 1.22x, named food 1.49x, doctor specialty 0.99x; evidence register EV-017 already said 0.5x (contradiction)", "ARCHETYPE-PERFORMANCE.json"),
    ("DQ-13", "02-VIDEOS-WITH-TITLE-FEATURES.json", "has_age_marker", "Identical to has_number on all 306 rows - regex bug; feature invalid", "build_outputs TF note"),
    ("DQ-14", "02-matched-pairs.json", "Pair 1 topic 'Cardiovascular'", "Foot-signs video is a diabetes topic (regex mis-tag)", "title"),
    ("DQ-15", "02-matched-pairs.json pair 15", "Topic control", "Loser (K2-A lime + charcoal) is an off-niche legacy upload with no transcript - INVALID_CONTROL", "LIVE thumbnail #21"),
    ("DQ-16", "FINAL-STATUS 'transcripts require API/scraping'", "Transcript access", "305/306 transcripts are stored in the registry DB; only 1 absent (fj4TaPrLl8U, no caption track)", "registry DB"),
    ("DQ-17", "Deep-dive/Case studies Trends tables", "Estimated Trends values", "Withdrawn; replaced by 32 live investigations (TRENDS-REGISTER.json)", "TRENDS-REGISTER.json"),
    ("DQ-18", "CS1 'Medical Accuracy: Solid'", "Medical verdict", "Replaced by MV-01 UNSUPPORTED / MV-02 PARTIAL", "MEDICAL-VALIDATION.json"),
    ("DQ-19", "Aliza thumbnail URLs", "DB thumbnail_url null for Aliza/Okoro/Thomas/SHH", "Raw Apify thumbnailUrl used (Okoro/Thomas/SHH); Aliza from canonical i.ytimg pattern + repository snapshots (DS-000006 manifest)", "VERIFIED-FACTS.json"),
]
dump("DATA-QUALITY-CORRECTIONS.json", [dict(zip(["id", "location", "previous_claim", "verified_value", "evidence"], d)) for d in DQ])

CONCLUSIONS = [
    ("C-01", "Channel growth is hit-concentrated: top video = 13-78% of channel views", "HIGH", "VERIFIED-FACTS top_video.share_of_channel_views"),
    ("C-02", "A hit does not raise the channel floor (SHH 9,539 -> 9,418 median; Okoro recent-10 median 75)", "HIGH", "VERIFIED-FACTS; DQ-09"),
    ("C-03", "Same title on a different channel yields radically different results (2 to 1.6M); same persona + identical title + identical thumbnail (incl. typo) 5 days apart: 941,154 vs 160", "HIGH", "DUPLICATE-NETWORK-SUMMARY; C03-C13; CH_channel_pages"),
    ("C-04", "Cohort channels share packaging but not scripts (max cross-channel transcript 5-gram Jaccard 0.024)", "HIGH", "DUPLICATE-NETWORK.json"),
    ("C-05", "Ares and Elias show same-operator signals (identical thumbnail text incl. typos, same mismatched thumbnail on a different title)", "MEDIUM-HIGH (ownership UNVERIFIED)", "THUMBNAIL-MATRIX notes #49-#81"),
    ("C-06", "Copy outcome depends on the copying channel, not order: across 37 cross-channel same-title pairs second movers won 22; at >=29 days they won 14/16 (stronger channels re-running weak channels' titles); inside the Ares-Elias twin, re-runs >=15 days later lost 4/6", "MEDIUM", "DUPLICATE-NETWORK-SUMMARY; C11"),
    ("C-07", "Thumbnails that withhold the answer outperform those that reveal it (1.90x vs 0.47x; 0/14 revealed reached 3x)", "MEDIUM (stratified sample)", "THUMBNAIL-MATRIX feature_performance"),
    ("C-08", "Warning-hook openings and warning icons underperform within channel (0.32x hooks, 14 of 22 below 0.5x; 0.55x icons)", "MEDIUM", "ARCHETYPE-PERFORMANCE; THUMBNAIL-MATRIX"),
    ("C-09", "Many large winners had little or no web-search demand at upload (bathing 0/100, eyesight 0, anesthesia dip) - discovery appears non-search", "MEDIUM (traffic sources UNKNOWN)", "GT-18, GT-20, GT-21"),
    ("C-10", "Trend alignment helped some winners (neuropathy peak week; garlic Jan peak; clove multi-year rise) but high interest did not rescue losers (stroke Jun 2026, sleeping-position Okoro)", "MEDIUM", "GT-01, GT-11, GT-17, GT-22, GT-24"),
    ("C-11", "Generic stroke warning content failed on all 3 channels that ran it", "HIGH", "Pairs 11, 25; Thomas 2,078"),
    ("C-12", "Conditional audience gating is not fatal (eggs-if-diabetes 127.6K) - pass-1 '247x from narrowing' over-attributed", "MEDIUM", "Pair 7, pair 28, DQ-11"),
    ("C-13", "Series/franchise behavior drives the largest absolute results (SHH: 41 clove entries = 73.1% of channel views, 14 of 41 >=3x; exact repeats of the 3.09M format returned to ~1x)", "HIGH", "VERIFIED-FACTS; CH_channel_pages"),
    ("C-14", "Winning openings place the viewer inside a lived moment within ~20 s and set an open loop within ~100 s", "MEDIUM (lexical heuristic + 29 reads)", "MATCHED-PAIRS-SCRIPT-FORENSICS"),
    ("C-15", "Several category winners carry unsupported medical claims; performance lessons must be separated from the claims", "HIGH", "MEDICAL-VALIDATION MV-03/07/08/09/10"),
    ("C-16", "AI-assisted production is disclosed in 26/32 Aliza transcripts; composite patients disclosed", "HIGH", "TRANSCRIPT-FORENSICS transcript_ai_disclosure_present"),
    ("C-17", "Small channels can break out quickly (Aliza persona channel, Okoro, Fit Lit - the latter serves a South-Asian-language audience), usually on proven topics with new packaging", "MEDIUM", "SMALL-CHANNEL-BREAKOUTS.json"),
    ("C-18", "Whitespace with rising demand and no cohort coverage: GLP-1 brand shift, creatine, BP-timing trial, mini-stroke in women, supplement interactions", "MEDIUM", "GT-13, GT-25, GT-29, GT-32, GT-11"),
]
dump("MAJOR-CONCLUSIONS.json", [dict(zip(["id", "conclusion", "confidence", "evidence"], c)) for c in CONCLUSIONS])

# ------------------------------------------------------------------ granular evidence register
EV = []
def ev(eid, etype, claim, source, label, conf, url=""):
    EV.append({"evidence_id": eid, "evidence_type": etype, "claim_or_observation": claim, "source_path_or_url": source,
               "evidence_label": label, "confidence": conf, "url": url, "recorded": AS_OF})

for i, vid in enumerate(sorted(SAMPLE), 1):
    r = TX[vid]
    if r.get("transcript_status") != "PRESENT":
        ev(f"EV-TX-{i:03d}", "DEEP_TRANSCRIPT", f"{vid}: transcript ABSENT ({r.get('transcript_status')})", "data/catalog/youtube_channel_registry.db:transcripts", "REPOSITORY_FACT", "HIGH")
        continue
    ev(f"EV-TX-{i:03d}", "DEEP_TRANSCRIPT",
       f"{vid} ({r['channel']}, {r['views']:,} views, {r['outlier_multiple_vs_channel_median']}x): hook={r['hook_archetype']}, script={r.get('script_archetype')}, words={r['word_count']}, first payoff ~{(r.get('first_enumerated_payoff') or {}).get('approx_seconds')}s, first CTA ~{(r.get('first_cta') or {}).get('approx_seconds')}s; opens: \"{r['opening_first_15s'][:110]}\"",
       r["transcript_path"], "ACTUAL_TRANSCRIPT_TEXT + TRANSCRIPT_LEXICAL_HEURISTIC (times APPROXIMATED_FROM_WORD_POSITION)", "MEDIUM")
for p in MP:
    ev(f"EV-MP-{p['pair']:02d}", "MATCHED_PAIR_SCRIPT", f"Pair {p['pair']} ({p['channel']}; {p['control_validity'].split(' ')[0]}): {p['unique_finding']}",
       f"{p['winner']['transcript_path']} | {p['loser']['transcript_path']}", "ACTUAL_TRANSCRIPT_TEXT + LIVE_WEB_VISUAL", "MEDIUM")
for i, r in enumerate(THM["rows"], 1):
    ev(f"EV-TH-{i:03d}", "THUMBNAIL_OBSERVATION", f"{r['video_id']} ({r['channel']}, {r['outlier_multiple']}x): text='{r['exact_thumbnail_text'][:90]}'; face={r['face'][:20]}; answer={r['answer_revealed_or_withheld']}; {r['analyst_note'][:100]}",
       r["thumbnail_url_observed"], "LIVE_WEB_VISUAL", "HIGH (observation) / n.a. (effect)")
for g in GT:
    ev(f"EV-{g['id']}", "GOOGLE_TRENDS_QUERY", f"'{g['query']}' {g['geo']} {g['property']} {g['time']}: peak {g.get('peak_period')}, first-12w {g.get('first_12w_mean')}, last-12w {g.get('last_12w_mean')}. {g.get('note', '')[:160]}",
       g.get("url", "https://trends.google.com/trends/explore"), "LIVE_GOOGLE_TRENDS (0-100 relative, not volume)", "HIGH (observation)")
for i, e in enumerate(EXT, 1):
    ev(f"EV-EXT-{i:03d}", "EXTERNAL_VIDEO", f"[{e['cluster']}] {e['channel']}: '{e['title'][:80]}' - {e['views_live']} views, {e['age_relative']}, role={e['role']}",
       e["source_file"], "LIVE_WEB_SEARCH_RESULT", "HIGH (as displayed)", f"https://www.youtube.com/watch?v={e['video_ref']}" if "/" not in e["video_ref"] else f"https://www.youtube.com/{e['video_ref']}")
for s in SMALL_BREAKOUTS:
    ev(f"EV-{s['id']}", "SMALL_CHANNEL_BREAKOUT", f"{s['channel']}: baseline {s['baseline_before']}; breakout {s['breakout']}", s["evidence"], "LIVE_WEB_CHANNEL_PAGE / REPOSITORY_FACT", "MEDIUM")
for h in S.HISTORY:
    ev(f"EV-{h[0]}", "HISTORICAL_EVENT", f"{h[1]} ({h[2]}) vs {h[4]}: {h[6]}", h[3], "WEB_RESEARCH", h[7])
for m in S.MEDICAL:
    ev(f"EV-{m[0]}", "MEDICAL_FACT_CHECK", f"{m[1]} -> {m[5]}", m[3], "WEB_RESEARCH (authoritative where available)", "HIGH" if m[5] in ("SUPPORTED", "UNSUPPORTED", "CONTRADICTED") else "MEDIUM")
for d in DQ:
    ev(f"EV-{d[0]}", "DATA_QUALITY_CORRECTION", f"{d[1]}: '{d[2]}' -> {d[3]}", d[4], "REPOSITORY_FACT", "HIGH")
for c in CONCLUSIONS:
    ev(f"EV-{c[0]}", "MAJOR_CONCLUSION", c[1], c[3], "ANALYTICAL_CONCLUSION (inference, not fact)", c[2])
for r in S.DS18:
    ev(f"EV-DS18-{r[0]}", "CORPUS_CLAIM_TEST", f"{r[1]} [{r[3]}] -> {r[8]}", "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-24.json; " + r[2], "CREATOR_CLAIM_vs_PLATFORM_FACT", r[3])
for r in S.DS11:
    ev(f"EV-DS11-{r[0]}", "CORPUS_FRAMEWORK_TEST", f"{r[1]} -> {r[5]}", "data/raw/global-youtube-knowledge/DS-000011", "FRAMEWORK_TESTED_AGAINST_COHORT", "MEDIUM")
for r in S.DS31:
    ev(f"EV-DS31-{r[0][:18].replace(' ', '_')}", "CORPUS_FRAMEWORK_TEST", f"{r[0]}: {r[6]}", "data/intelligence/global/creator-strategy-knowledge-DS-000031.json " + r[1], "FRAMEWORK_TESTED_AGAINST_COHORT", "MEDIUM")
dump("EVIDENCE-REGISTER-V2.json", {"as_of": AS_OF, "count": len(EV), "by_type": dict(Counter(e["evidence_type"] for e in EV)), "records": EV})
print("evidence records:", len(EV), dict(Counter(e["evidence_type"] for e in EV)))

# expose for workbook module
CTX = dict(FACTS=FACTS, CH=CH, videos=videos, TX=TX, THM=THM, MP=MP, GT=GT, EXT=EXT, SMALL=SMALL_BREAKOUTS, TOPICS=TOPICS, TF=TF,
           HOOKS=HOOKS, SCRIPTS=SCRIPTS, DQ=DQ, CONCLUSIONS=CONCLUSIONS, EV=EV, f50=f50, dup=dup_summary, WITHDRAWN=WITHDRAWN)

if __name__ == "__main__":
    import build_workbook
    build_workbook.build(CTX, S, HERE / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V2.xlsx")
