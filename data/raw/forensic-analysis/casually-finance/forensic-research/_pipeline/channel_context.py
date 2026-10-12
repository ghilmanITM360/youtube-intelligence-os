"""Deterministic channel-relative context from the dated public metadata snapshot -> 06_REPORTS/WINNERS_LOSERS_COUNTEREXAMPLES.md (+ 05 data json).
Usage: python3 -B channel_context.py <OUT_DIR>"""
import csv, json, re, sys, statistics as st
from pathlib import Path
import numpy as np
out = Path(sys.argv[1]); rows = list(csv.DictReader(open(out / "01_CHANNEL_METADATA/all-videos-metadata.csv")))
SEL = {r["video_id"] for r in csv.DictReader(open(out / "00_MANIFEST/SELECTED_18.csv"))}
for r in rows:
    r["views"] = float(r["views"] or 0); r["vpd"] = float(r["views_per_day"] or 0); r["age"] = float(r["age_days_at_collection"] or 0); r["dur"] = float(r["duration_sec"] or 0); r["sel"] = r["video_id"] in SEL
MIN_AGE = 7.0
def rank(a): o = np.argsort(np.argsort(a)); return o.astype(float)
def spear(x, y): return float(np.corrcoef(rank(np.array(x)), rank(np.array(y)))[0, 1]) if len(x) > 3 else float("nan")
feat = {"has a digit/number": lambda t: bool(re.search(r"\d", t)), "has '?'": lambda t: "?" in t, "has ellipsis": lambda t: "..." in t or "…" in t, "has parentheses": lambda t: "(" in t,
        "starts with 'Why'": lambda t: t.lower().startswith("why"), "title >= 8 words": lambda t: len(t.split()) >= 8, "has colon": lambda t: ":" in t}
L = ["# WINNERS, LOSERS AND COUNTEREXAMPLES — public-metadata context (channel catalog)\n",
     f"_Snapshot `{rows[0]['snapshot']}` · {len(rows)} unique upload IDs. Associations below use videos aged ≥ {MIN_AGE:.0f} days at collection (younger videos carry launch-window velocity). All findings are **MEASURED_ASSOCIATION**; CTR, impressions, retention, traffic source and thumbnail tests are **NOT_TESTABLE_WITH_PUBLIC_DATA**. The 18 selected videos were chosen by the user as popular/recent, so they are a biased sample (survivorship)._\n"]
data = {}
for fmt, label in (("LONG_FORM", "Long-form"), ("SHORT", "Shorts")):
    g = [r for r in rows if r["format_class"] == fmt]; ga = [r for r in g if r["age"] >= MIN_AGE]
    L.append(f"\n## {label} (n={len(g)}, aged ≥{MIN_AGE:.0f}d: {len(ga)})\n")
    vs = [r["views"] for r in g]; vp = [r["vpd"] for r in ga]
    L.append(f"- Views: median {st.median(vs):,.0f} · mean {st.mean(vs):,.0f} · max {max(vs):,.0f}. Views/day (aged ≥{MIN_AGE:.0f}d): median {st.median(vp):,.0f} · p25 {np.percentile(vp,25):,.0f} · p75 {np.percentile(vp,75):,.0f} · p90 {np.percentile(vp,90):,.0f}.")
    L.append(f"- Spearman(views/day, duration) = {spear([r['vpd'] for r in ga],[r['dur'] for r in ga]):+.2f}; Spearman(views/day, age) = {spear([r['vpd'] for r in ga],[r['age'] for r in ga]):+.2f}; Spearman(views, age) = {spear([r['views'] for r in ga],[r['age'] for r in ga]):+.2f} (n={len(ga)}).")
    def tbl(rs, n):
        s = ["| Video | Title | Pub | Age d | Dur s | Views | Views/day | Sel |", "|---|---|---|---:|---:|---:|---:|:-:|"]
        for r in rs[:n]: s.append(f"| {r['video_id']} | {r['title'][:60]} | {r['published_at'][:10]} | {r['age']:.0f} | {r['dur']:.0f} | {r['views']:,.0f} | {r['vpd']:,.0f} | {'✓' if r['sel'] else ''} |")
        return s
    top = sorted(ga, key=lambda r: -r["vpd"]); L += ["\n**Top by views/day**\n"] + tbl(top, 8)
    L += ["\n**Bottom by views/day (counterexamples)**\n"] + tbl(top[::-1], 8)
    L += ["\n**Title-feature associations (median views/day; group n shown; groups with n<5 are anecdotal)**\n", "| Feature | With (median, n) | Without (median, n) |", "|---|---:|---:|"]
    for k, f in feat.items():
        a = [r["vpd"] for r in ga if f(r["title"])]; b = [r["vpd"] for r in ga if not f(r["title"])]
        if a and b: L.append(f"| {k} | {st.median(a):,.0f} (n={len(a)}) | {st.median(b):,.0f} (n={len(b)}) |")
    tp = {}
    for r in ga: tp.setdefault(r["topic_derived_heuristic"], []).append(r["vpd"])
    L += ["\n**Topic heuristic groups (keyword-derived, coarse)**\n", "| Topic | n | Median views/day |", "|---|---:|---:|"] + [f"| {k} | {len(v)} | {st.median(v):,.0f} |" for k, v in sorted(tp.items(), key=lambda kv: -len(kv[1]))]
    sel = sorted([r for r in g if r["sel"]], key=lambda r: -r["vpd"])
    L += ["\n**Where the selected videos sit** (percentile within format; includes young videos)\n", "| Video | Title | Age d | Views pct | Views/day pct |", "|---|---|---:|---:|---:|"] + [f"| {r['video_id']} | {r['title'][:55]} | {r['age']:.0f} | {r['views_percentile_in_format']} | {r['vpd_percentile_in_format']} |" for r in sel]
    data[fmt] = dict(n=len(g), n_aged=len(ga), median_views=st.median(vs), median_vpd_aged=st.median(vp))
L += ["\n## Reading guide\n", "- **OBSERVED**: the tables above are direct computations on the public snapshot.", "- **MEASURED_ASSOCIATION**: feature/topic/duration groupings; small groups, overlapping features and a strong age/time confound (template and topic changes coincide with publication date). No causal claim is supported.",
      "- **PLAUSIBLE_HYPOTHESIS**: see `VIRALITY_HYPOTHESES.md` (to be written after more videos are analysed).", "- **NOT_TESTABLE_WITH_PUBLIC_DATA**: CTR, impressions, retention, recommendation traffic, A/B tests, revenue."]
(out / "06_REPORTS/WINNERS_LOSERS_COUNTEREXAMPLES.md").write_text("\n".join(L) + "\n"); json.dump(data, open(out / "03_MASTER_DATA/_channel_context_summary.json", "w"), indent=1); print("ok", data)
