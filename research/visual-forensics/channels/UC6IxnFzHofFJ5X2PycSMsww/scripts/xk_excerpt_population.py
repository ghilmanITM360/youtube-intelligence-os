"""Short <-> long narration reuse via text: catalog plaintext captions (DS-000017, all 83 registered IDs) with ASR fallback.
Measures for each selected Short the fraction of its words covered by matching blocks (>=6 words) in each long-form video
of the whole census population. Text reuse suggests excerpt/recut; it does NOT prove visual reuse (verify visually).
Usage: python3 -I xk_excerpt.py <ws>"""
import csv, json, re, sys, pathlib, difflib
W = pathlib.Path(sys.argv[1]); T = pathlib.Path("/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/raw/competitors/DS-000017/apify/mzl5dCHF81LbcBamS/transcripts")
norm = lambda s: re.findall(r"[a-z0-9]+", s.lower().replace("’", "'"))
census = list(csv.DictReader(open(W / "census/census.csv"))); sel = json.load(open(W / "selection/selection_v1.json"))
def text(vid):
    if (T / f"{vid}.txt").exists(): return norm((T / f"{vid}.txt").read_text()), "catalog_caption"
    a = W / "videos" / vid / "asr/asr_small_en.json"
    if a.exists(): return norm(" ".join(s["text"] for s in json.load(open(a))["segments"])), "asr"
    return None, "none"
longs = {r["video_id"]: text(r["video_id"]) for r in census if r["format_class"] == "LONG_FORM"}
rows = []
for sid in [r["video_id"] for r in census if r["format_class"] == "SHORT"]:
    sw, src = text(sid)
    if not sw: rows.append(dict(short=sid, text_source=src)); continue
    best = []
    for lid, (lw, lsrc) in longs.items():
        if not lw: continue
        sm = difflib.SequenceMatcher(None, sw, lw, autojunk=False)
        cov = sum(b.size for b in sm.get_matching_blocks() if b.size >= 6) / len(sw)
        best.append((cov, lid, lsrc))
    best.sort(reverse=True)
    c, lid, lsrc = best[0]
    rows.append(dict(short=sid, text_source=src, short_words=len(sw), best_long=lid, best_long_text_source=lsrc,
                     coverage_by_6word_blocks=round(c, 3), second_best=f"{best[1][1]}:{best[1][0]:.3f}",
                     relation="TEXT_EXCERPT_CANDIDATE" if c >= 0.5 else ("PARTIAL_TEXT_REUSE" if c >= 0.15 else "STANDALONE_TEXT")))
with open(W / "campaign/short_long_text_reuse_population.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)); w.writeheader(); w.writerows(rows)
for r in rows: print(r.get("short"), r.get("relation"), r.get("best_long"), r.get("coverage_by_6word_blocks"), r.get("text_source"))
