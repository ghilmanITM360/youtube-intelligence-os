"""Forensic workbook v2: required sheets 00-30 plus supporting 31-37, native Excel charts
with plain-English commentary. Values come from the forensic-v2 evidence layers; summary
cells use formulas over 04_VIDEO_MASTER / 29_EVIDENCE_REGISTER so they recalculate."""
import math, statistics as st
from collections import defaultdict, Counter
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, ScatterChart, Reference, Series
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

F = "Arial"
HDR = PatternFill("solid", fgColor="1F3864")
NOTE = PatternFill("solid", fgColor="FFF2CC")


def style_header(ws, row, n):
    for c in range(1, n + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name=F, bold=True, color="FFFFFF")
        cell.fill = HDR
        cell.alignment = Alignment(wrap_text=True, vertical="top")


def table(ws, rows, cols=None, start_row=1, start_col=1, widths=None):
    if not rows:
        ws.cell(row=start_row, column=start_col, value="(no rows)")
        return start_row
    cols = cols or list(rows[0].keys())
    for j, c in enumerate(cols):
        ws.cell(row=start_row, column=start_col + j, value=c)
    style_header(ws, start_row, start_col + len(cols) - 1)
    for i, r in enumerate(rows, 1):
        for j, c in enumerate(cols):
            v = r.get(c) if isinstance(r, dict) else r[j]
            if isinstance(v, (list, dict)):
                v = "; ".join(map(str, v)) if isinstance(v, list) else str(v)
            cell = ws.cell(row=start_row + i, column=start_col + j, value=v)
            cell.font = Font(name=F, size=9)
            cell.alignment = Alignment(wrap_text=isinstance(v, str) and len(v) > 40, vertical="top")
    for j, c in enumerate(cols):
        w = (widths or {}).get(c, min(60, max(10, len(str(c)) + 2)))
        ws.column_dimensions[get_column_letter(start_col + j)].width = w
    ws.freeze_panes = ws.cell(row=start_row + 1, column=start_col)
    return start_row + len(rows)


def note(ws, cell, text, width_cols=8):
    ws[cell] = text
    ws[cell].font = Font(name=F, size=10, italic=True)
    ws[cell].fill = NOTE
    ws[cell].alignment = Alignment(wrap_text=True, vertical="top")


def block(ws, header, rows, r0, c0):
    for j, h in enumerate(header):
        ws.cell(row=r0, column=c0 + j, value=h).font = Font(name=F, bold=True)
    for i, row in enumerate(rows, 1):
        for j, v in enumerate(row):
            ws.cell(row=r0 + i, column=c0 + j, value=v).font = Font(name=F, size=9)
    return r0 + len(rows)


CHARTS = []


def bar(ws, title, r0, c0, n, ncols, anchor, ytitle="", xtitle="", comment="", horizontal=False, stacked=False):
    ch = BarChart()
    ch.type = "bar" if horizontal else "col"
    if stacked:
        ch.grouping = "stacked"; ch.overlap = 100
    ch.title, ch.y_axis.title, ch.x_axis.title = title, ytitle, xtitle
    data = Reference(ws, min_col=c0 + 1, max_col=c0 + ncols, min_row=r0, max_row=r0 + n)
    cats = Reference(ws, min_col=c0, min_row=r0 + 1, max_row=r0 + n)
    ch.add_data(data, titles_from_data=True); ch.set_categories(cats)
    ch.height, ch.width = 9, 18
    ws.add_chart(ch, anchor)
    CHARTS.append((ws.title, title, comment))


def line(ws, title, r0, c0, n, ncols, anchor, ytitle="", comment=""):
    ch = LineChart()
    ch.title, ch.y_axis.title = title, ytitle
    data = Reference(ws, min_col=c0 + 1, max_col=c0 + ncols, min_row=r0, max_row=r0 + n)
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(Reference(ws, min_col=c0, min_row=r0 + 1, max_row=r0 + n))
    ch.height, ch.width = 9, 20
    ws.add_chart(ch, anchor)
    CHARTS.append((ws.title, title, comment))


def scatter(ws, title, r0, xcol, ycol, n, anchor, xt, yt, comment=""):
    ch = ScatterChart()
    ch.title, ch.x_axis.title, ch.y_axis.title = title, xt, yt
    ch.style = 13
    s = Series(Reference(ws, min_col=ycol, min_row=r0 + 1, max_row=r0 + n), Reference(ws, min_col=xcol, min_row=r0 + 1, max_row=r0 + n), title=title)
    s.marker.symbol = "circle"; s.graphicalProperties.line.noFill = True
    ch.series.append(s)
    ch.height, ch.width = 10, 18
    ws.add_chart(ch, anchor)
    CHARTS.append((ws.title, title, comment))


def build(C, S, out):
    wb = Workbook()
    names = ["00_READ_ME", "01_EXECUTIVE_DASHBOARD", "02_COMPETITOR_COHORT", "03_CHANNEL_SCORECARDS", "04_VIDEO_MASTER",
             "05_PERFORMANCE_NORMALIZATION", "06_OUTLIER_WINNERS", "07_FAILURE_AUTOPSIES", "08_MATCHED_PAIRS", "09_TOPIC_TAXONOMY",
             "10_TOPIC_PERFORMANCE", "11_GOOGLE_TRENDS", "12_TREND_ATTRIBUTION", "13_EXTERNAL_VIRAL_BENCHMARKS", "14_TITLE_ANALYSIS",
             "15_THUMBNAIL_ANALYSIS", "16_HOOK_SCRIPT_ANALYSIS", "17_AUDIENCE_PSYCHOLOGY", "18_CHANNEL_LIFECYCLE", "19_CLUSTER_FOLLOWUPS",
             "20_COMPETITION_MAP", "21_OPPORTUNITY_MATRIX", "22_SATURATION_WHITESPACE", "23_CHANNEL_POSITIONING", "24_CONTENT_PILLARS",
             "25_FIRST_50_VIDEOS", "26_LAUNCH_SEQUENCE", "27_EXPERIMENTATION_PLAN", "28_MEDICAL_VALIDATION", "29_EVIDENCE_REGISTER",
             "30_GLOSSARY", "31_DATA_CORRECTIONS", "32_DUPLICATE_NETWORK", "33_HISTORICAL_CONTEXT", "34_DS000011_TRACE",
             "35_DS000018_CLAIMS", "36_DS000031_FRAMEWORKS", "37_CHART_COMMENTARY"]
    ws = {n: (wb.active if i == 0 else wb.create_sheet(n)) for i, n in enumerate(names)}
    ws["00_READ_ME"].title = "00_READ_ME"
    videos, CH, TX, TH = C["videos"], C["CH"], C["TX"], {r["video_id"]: r for r in C["THM"]["rows"]}

    # ---------------- 04 VIDEO MASTER (first: other sheets reference it)
    w = ws["04_VIDEO_MASTER"]
    cols = ["video_id", "channel", "upload_date", "duration_seconds", "video_type", "views", "channel_median_views", "multiple_formula",
            "topic_tags", "in_deep_sample", "transcript_words", "hook_archetype", "script_archetype", "first_payoff_s_approx", "first_cta_s_approx",
            "thumbnail_text_live", "thumbnail_answer", "title", "transcript_path", "thumbnail_url"]
    for j, c in enumerate(cols, 1):
        w.cell(row=1, column=j, value=c)
    style_header(w, 1, len(cols))
    for i, v in enumerate(videos, 2):
        t = TX.get(v["video_id"], {}); th = TH.get(v["video_id"], {})
        row = [v["video_id"], v["channel"], v["upload_date"], v["duration_seconds"], v["video_type"], v["views"], v["channel_median_views"],
               f"=IFERROR(F{i}/G{i},\"\")", "; ".join(v["topic_tags"] or []), "Y" if t.get("in_deep_sample_149") else "N", t.get("word_count", "ABSENT"),
               t.get("hook_archetype", "ABSENT"), t.get("script_archetype", "ABSENT"),
               (t.get("first_enumerated_payoff") or {}).get("approx_seconds"), (t.get("first_cta") or {}).get("approx_seconds"),
               th.get("exact_thumbnail_text", "NOT_IN_149_SAMPLE"), th.get("answer_revealed_or_withheld", ""), v["title"], v["transcript_path"], v["thumbnail_url"]]
        for j, x in enumerate(row, 1):
            w.cell(row=i, column=j, value=x).font = Font(name=F, size=9)
        w.cell(row=i, column=8).number_format = "0.00"
    for c, wd in zip("ABCDEFGHIJKLMNOPQRST", [13, 22, 11, 9, 9, 11, 11, 9, 24, 7, 8, 16, 16, 8, 8, 40, 12, 60, 40, 40]):
        w.column_dimensions[c].width = wd
    w.freeze_panes = "C2"
    NV = len(videos) + 1
    VM = "'04_VIDEO_MASTER'"

    # ---------------- 02 COHORT
    rows = []
    for cid, c in CH.items():
        m = c["raw_channel_metadata"]
        rows.append({"channel": c["channel"], "channel_id": cid, "videos_in_repository": c["videos_in_repository"], "earliest_upload": c["earliest_available_upload"],
                     "latest_upload": c["latest_available_upload"], "channel_joined (raw)": m.get("channel_joined_date"), "subscribers_at_scrape (raw)": m.get("subscribers_at_scrape"),
                     "transcripts_available": c["transcripts_available"], "thumbnail_urls_known": c["thumbnail_urls_known"], "repository_thumbnail_snapshots": c["thumbnail_repository_snapshots"],
                     "raw_metadata_source": m.get("source")})
    table(ws["02_COMPETITOR_COHORT"], rows)
    note(ws["02_COMPETITOR_COHORT"], "A10", "Source: data/catalog/youtube_channel_registry.db + raw Apify channel fields. UNKNOWN = no raw channel record in repository (Aliza DS-000006, Elias DS-000019). Views are scrape-time snapshots; live counts have since risen (see 13_EXTERNAL).")

    # ---------------- 03 SCORECARDS (formulas)
    w = ws["03_CHANNEL_SCORECARDS"]
    hdr = ["channel", "videos (formula)", "total views (formula)", "max views (formula)", "top-1 share (formula)", "median views (computed)", "recent-10 median (computed)",
           "videos >=3x (formula)", "videos <0.5x (formula)", "hit rate (formula)", "top video", "top video date"]
    for j, h in enumerate(hdr, 1):
        w.cell(row=1, column=j, value=h)
    style_header(w, 1, len(hdr))
    for i, c in enumerate(CH.values(), 2):
        vals = [c["channel"], f"=COUNTIF({VM}!$B$2:$B${NV},A{i})", f"=SUMIF({VM}!$B$2:$B${NV},A{i},{VM}!$F$2:$F${NV})",
                f"=_xlfn.MAXIFS({VM}!$F$2:$F${NV},{VM}!$B$2:$B${NV},A{i})", f"=IFERROR(D{i}/C{i},0)", c["median_views_all"], c["median_views_recent10_by_upload"],
                f"=COUNTIFS({VM}!$B$2:$B${NV},A{i},{VM}!$H$2:$H${NV},\">=3\")", f"=COUNTIFS({VM}!$B$2:$B${NV},A{i},{VM}!$H$2:$H${NV},\"<0.5\")",
                f"=IFERROR(H{i}/B{i},0)", c["top_video"]["title"], c["top_video"]["upload_date"]]
        for j, x in enumerate(vals, 1):
            w.cell(row=i, column=j, value=x).font = Font(name=F, size=9)
        w.cell(row=i, column=5).number_format = "0.0%"; w.cell(row=i, column=10).number_format = "0.0%"
    for j in range(1, 13):
        w.column_dimensions[get_column_letter(j)].width = 16
    w.column_dimensions["K"].width = 60
    note(w, "A10", "Median columns computed in Python from VERIFIED-FACTS.json (MEDIAN over a filtered range needs array formulas that do not survive LibreOffice recalculation). All other columns are live formulas over 04_VIDEO_MASTER.")
    # chart 1: concentration (static block computed)
    blk = [(c["channel"][:18], round(c["top_video"]["share_of_channel_views"], 3)) for c in CH.values()]
    block(w, ["channel", "top-1 share of channel views"], blk, 14, 1)
    bar(w, "Channel view concentration: share of views from the single top video", 14, 1, len(blk), 1, "D13", "share", comment=
        "Every channel depends on one video for 13-78% of its views. Dr. Okoro (78%) and Aliza (74%) are one-hit channels. Dr. Elias (13%) and Dr. Ares (25%) are the least concentrated. Senior Health Hub (30%) spreads its views across a 41-video clove series.")
    # chart 2: Pareto
    ranks = list(range(1, 21))
    cum = {}
    for c in CH.values():
        vs = sorted([v["views"] for v in videos if v["channel"] == c["channel"]], reverse=True)
        tot = sum(vs); run = 0; arr = []
        for k in ranks:
            run += vs[k - 1] if k <= len(vs) else 0
            arr.append(round(run / tot, 3))
        cum[c["channel"][:14]] = arr
    hdr2 = ["rank"] + list(cum)
    block(w, hdr2, [[r] + [cum[k][r - 1] for k in cum] for r in ranks], 24, 1)
    line(w, "Pareto: cumulative share of channel views by video rank (top 20)", 24, 1, 20, len(cum), "D30", "cumulative share", comment=
         "The curves flatten after 3-5 videos: for five of six channels the top 5 videos hold >60% of all views. New-channel planning should assume a few videos will carry the channel.")

    # ---------------- 05 NORMALIZATION
    w = ws["05_PERFORMANCE_NORMALIZATION"]
    bins = [(0, 0.25), (0.25, 0.5), (0.5, 1), (1, 2), (2, 5), (5, 10), (10, 100), (100, 1e9)]
    labels = ["<0.25x", "0.25-0.5x", "0.5-1x", "1-2x", "2-5x", "5-10x", "10-100x", ">=100x"]
    w["A1"] = "Outlier multiple = views / own-channel median (formula in 04_VIDEO_MASTER col H)"; w["A1"].font = Font(name=F, bold=True)
    for j, h in enumerate(["bin", "lower", "upper", "videos (formula)"], 1):
        w.cell(row=3, column=j, value=h)
    style_header(w, 3, 4)
    for i, (lab, (lo, hi)) in enumerate(zip(labels, bins), 4):
        w.cell(row=i, column=1, value=lab); w.cell(row=i, column=2, value=lo); w.cell(row=i, column=3, value=hi)
        w.cell(row=i, column=4, value=f"=COUNTIFS({VM}!$H$2:$H${NV},\">=\"&B{i},{VM}!$H$2:$H${NV},\"<\"&C{i})")
    ch = BarChart(); ch.title = "Outlier multiple distribution (all 306 videos)"
    ch.add_data(Reference(w, min_col=4, min_row=3, max_row=11), titles_from_data=True); ch.set_categories(Reference(w, min_col=1, min_row=4, max_row=11))
    ch.height, ch.width = 9, 16; w.add_chart(ch, "F3")
    CHARTS.append((w.title, "Outlier multiple distribution (all 306 videos)",
                   "41% of videos sit between 0.5x and 2x their channel median. Breakouts of >=10x are 10% of uploads (31 of 306), and most of them cluster on a few channels in short bursts. That is why single-video case studies overstate repeatability."))
    # views distribution (log10 bins)
    lb = [(10 ** k, 10 ** (k + 1)) for k in range(1, 7)]
    rows = [(f"{int(a):,}-{int(b):,}", sum(1 for v in videos if a <= v["views"] < b)) for a, b in lb] + [("<10", sum(1 for v in videos if v["views"] < 10))]
    block(w, ["views band", "videos"], rows, 14, 1)
    bar(w, "Video performance distribution (views, log bands)", 14, 1, len(rows), 1, "F20", comment=
        "Views span five orders of magnitude (32 to 3.09M). Most uploads land at 100-10,000 views; the million-view tail is a handful of videos on three channels.")
    tiers = Counter(v["tier"] for v in videos)
    block(w, ["pass-1 tier", "videos"], sorted(tiers.items()), 26, 1)

    # ---------------- 06 OUTLIERS / 07 FAILURES
    def vrow(v):
        t = TX.get(v["video_id"], {}); th = TH.get(v["video_id"], {})
        return {"video_id": v["video_id"], "channel": v["channel"], "date": v["upload_date"], "views": v["views"], "multiple": v["outlier_multiple_vs_channel_median"],
                "title": v["title"], "hook_archetype": t.get("hook_archetype"), "script_archetype": t.get("script_archetype"),
                "opening_15s_actual": (t.get("opening_first_15s") or "")[:220], "thumbnail_text_live": th.get("exact_thumbnail_text", "NOT_IN_149_SAMPLE"),
                "thumbnail_answer": th.get("answer_revealed_or_withheld", ""), "topic_tags": "; ".join(v["topic_tags"] or [])}
    win = sorted([v for v in videos if v["outlier_multiple_vs_channel_median"] >= 5], key=lambda v: -v["outlier_multiple_vs_channel_median"])
    table(ws["06_OUTLIER_WINNERS"], [vrow(v) for v in win], widths={"title": 50, "opening_15s_actual": 60, "thumbnail_text_live": 40})
    fail = sorted([v for v in videos if v["outlier_multiple_vs_channel_median"] < 0.3 and TX.get(v["video_id"], {}).get("in_deep_sample_149")], key=lambda v: v["outlier_multiple_vs_channel_median"])
    fr = []
    for v in fail:
        r = vrow(v); t = TX.get(v["video_id"], {}); th = TH.get(v["video_id"], {})
        causes = []
        if th.get("answer_revealed_or_withheld", "").startswith("REVEALED"): causes.append("thumbnail reveals answer")
        if t.get("hook_archetype") == "WARNING": causes.append("warning-led hook")
        if any(d["second_channel"] == v["channel"] and d["title"][:30] == v["title"][:30] for d in C["dup"]["rows"]): causes.append("late copy of a sister-channel title")
        if (t.get("per_1000_words") or {}).get("cure_language", 0) > 1: causes.append("cure language density >1/1k")
        if "diabetes" in v["title"].lower() and "if you have" in v["title"].lower(): causes.append("conditional audience gate")
        r["observable_risk_factors"] = "; ".join(causes) or "none of the tested factors - timing/channel state likely"
        fr.append(r)
    table(ws["07_FAILURE_AUTOPSIES"], fr, widths={"title": 50, "opening_15s_actual": 60, "thumbnail_text_live": 40, "observable_risk_factors": 40})

    # ---------------- 08 MATCHED PAIRS
    w = ws["08_MATCHED_PAIRS"]
    rows = [{"pair": p["pair"], "channel": p["channel"], "days_apart": p["days_apart"], "control_validity": p["control_validity"],
             "winner_views": p["winner"]["views"], "loser_views": p["loser"]["views"], "winner_title": p["winner"]["title"], "loser_title": p["loser"]["title"],
             "winner_first30s_actual": p["winner"]["first_30s_actual_text"][:400], "loser_first30s_actual": p["loser"]["first_30s_actual_text"][:400],
             "opening_promise_W": p["opening_promise"]["winner"], "opening_promise_L": p["opening_promise"]["loser"],
             "authority_W": p["authority_setup"]["winner"], "authority_L": p["authority_setup"]["loser"], "specificity_W": p["specificity"]["winner"], "specificity_L": p["specificity"]["loser"],
             "progression_W": p["story_progression"]["winner"], "progression_L": p["story_progression"]["loser"],
             "payoff_s_W": p["payoff_timing_s"]["winner"], "payoff_s_L": p["payoff_timing_s"]["loser"], "cta_s_W": p["cta_timing_s"]["winner"], "cta_s_L": p["cta_timing_s"]["loser"],
             "cta_ending_W": p["winner"]["cta_ending_actual_text"][-220:], "cta_ending_L": p["loser"]["cta_ending_actual_text"][-220:],
             "thumb_W": p["thumbnail_comparison"]["winner"], "thumb_L": p["thumbnail_comparison"]["loser"], "unique_finding": p["unique_finding"]} for p in C["MP"]]
    table(w, rows, widths={k: 45 for k in rows[0]})
    blk = [(f"P{p['pair']}", round(math.log10(max(p['winner']['views'], 1)), 2), round(math.log10(max(p['loser']['views'], 1)), 2)) for p in C["MP"]]
    block(w, ["pair", "winner log10 views", "loser log10 views"], blk, 33, 1)
    bar(w, "Matched pairs: winner vs loser (log10 views)", 33, 1, len(blk), 2, "E33", "log10(views)", comment=
        "Winner/loser gaps range from 8x to 15,452x. Only 14 of 29 pairs are clean controls (18 days apart or less); 14 are time-confounded and pair 15 is invalid. The clean pairs still show 13x to 1,517x gaps, so topic and packaging matter even when channel state is held roughly constant.")

    # ---------------- 09 TAXONOMY / 10 TOPIC PERFORMANCE
    tax = [{"topic_tag": t["topic"], "definition": "Keyword-regex tag from pass-1 master table (REGEX_TOPIC_TAG, not human-verified)", "videos": t["videos"], "channels": t["channels"],
            "strategic_cluster": {"Mobility/Falls/Balance": "Mobility & Falls", "Digestion/Gut": "Digestion & Remedies", "Nutrition/Foods": "Digestion & Remedies",
                                  "Cardiovascular": "Heart & Stroke", "Medication Warnings": "Medication Safety", "Diabetes/Blood Sugar": "Diabetes & Feet",
                                  "Kidney/Bladder": "Kidney & Bladder", "Sleep": "Sleep & Night", "Brain/Memory/Cognitive": "Brain & Memory"}.get(t["topic"], "Other/Unclassified")} for t in C["TOPICS"]]
    table(ws["09_TOPIC_TAXONOMY"], tax, widths={"definition": 50})
    w = ws["10_TOPIC_PERFORMANCE"]
    table(w, C["TOPICS"])
    top = [t for t in C["TOPICS"] if t["videos"] >= 8]
    r0 = len(C["TOPICS"]) + 4
    block(w, ["topic", "median multiple", "hit rate >=3x", "failure rate <0.5x"], [(t["topic"][:22], t["median_multiple"], t["hit_rate_ge3x"], t["failure_rate_lt0_5x"]) for t in top], r0, 1)
    bar(w, "Topic median outlier multiple (topics with >=8 videos)", r0, 1, len(top), 1, "J2", "x channel median", comment=
        "Digestion/Gut (1.75x) and Mobility/Falls (1.67x) lead. Sign-list topics sit lowest: general warning signs, brain, kidney/skin/nail signs and cancer are all 0.54-0.62x, and Cardiovascular is 0.80x. Sleep is bimodal: a 0.68x median but a 38% hit rate.")
    ch = BarChart(); ch.title = "Topic hit rate (>=3x) vs failure rate (<0.5x)"
    ch.add_data(Reference(w, min_col=3, max_col=4, min_row=r0, max_row=r0 + len(top)), titles_from_data=True)
    ch.set_categories(Reference(w, min_col=1, min_row=r0 + 1, max_row=r0 + len(top))); ch.height, ch.width = 9, 18; w.add_chart(ch, "J22")
    CHARTS.append((w.title, "Topic hit rate vs failure rate", "Every topic has both hits and failures; the spread inside a topic is larger than the spread between topics. Treat topic as necessary context, not the cause of a breakout."))

    # ---------------- 11 GOOGLE TRENDS / 12 ATTRIBUTION
    w = ws["11_GOOGLE_TRENDS"]
    grow = [{"id": g["id"], "query": g["query"], "term_type": g["term_type"], "geo": g["geo"], "property": g["property"], "time": g["time"], "retrieved": g["retrieved"],
             "peak_period": g.get("peak_period"), "first_12w_mean": g.get("first_12w_mean"), "last_12w_mean": g.get("last_12w_mean"),
             "top_region": g.get("top_region"), "top_queries": g.get("top_queries"), "rising_queries": g.get("rising_queries"),
             "related_topics_rising": g.get("related_topics_rising"), "note": g.get("note"), "label": "LIVE_GOOGLE_TRENDS"} for g in C["GT"]]
    end = table(w, grow, widths={"note": 60, "top_queries": 45, "rising_queries": 50})
    note(w, f"A{end + 2}", "Google Trends 0-100 is normalized relative interest for that query/geo/window, NOT search volume. Withdrawn (not evidence): " + "; ".join(C["WITHDRAWN"]))
    months = sorted(set(k for g in C["GT"] if g["id"] in ("GT-01", "GT-04", "GT-28", "GT-08") for k in (g.get("monthly") or {})))
    months = [m for m in months if m >= "2024-01"]
    series = {g["id"]: g["monthly"] for g in C["GT"] if g["id"] in ("GT-01", "GT-04", "GT-28", "GT-08")}
    uploads = {"2025-09": "SHH clove 1.09M", "2026-01": "SHH clove 1.06M", "2026-04": "SHH clove 3.09M", "2026-05": "Okoro foot 494K", "2026-06": "Okoro neuropathy 101K; Thomas 1.0M"}
    r0 = end + 5
    hdr = ["month", "clove water (US web)", "neuropathy exercises (US web)", "fall prevention (US web)", "exercises for seniors (US YouTube)", "upload marker (=100 in breakout month)"]
    rows = []
    for m in months:
        rows.append([m] + [series[k].get(m) for k in ("GT-01", "GT-04", "GT-28", "GT-08")] + [100 if m in uploads else None])
    block(w, hdr, rows, r0, 1)
    line(w, "Google Trends (live, monthly means of weekly values) with breakout-upload markers", r0, 1, len(rows), 5, f"H{r0}", "0-100 relative interest", comment=
         "Clove water rose ~7x over five years and peaked in Jan 2026 - SHH's clove hits sit on that wave. Neuropathy and fall-prevention interest hit 5-year highs in mid-2026 when Okoro's neuropathy and Doctor Thomas's fall videos broke out. Marker months (value 100) are uploads, not Trends data.")
    w = ws["12_TREND_ATTRIBUTION"]
    arows = []
    for g in C["GT"]:
        for k, wv in (g.get("upload_windows") or {}).items():
            b, u, a = wv.get("mean_90d_before"), wv.get("mean_upload_pm7d"), wv.get("mean_90d_after")
            state = "UNKNOWN" if None in (b, u) else "UPLOAD_IN_SPIKE" if u >= 1.15 * max(b, 1) else "UPLOAD_IN_DIP" if u <= 0.85 * max(b, 1) else "FLAT"
            arows.append({"trends_id": g["id"], "query": g["query"], "geo/property": f"{g['geo']} / {g['property']}", "video_and_date": k, "mean_90d_before": b, "mean_upload_pm7d": u, "mean_90d_after": a,
                          "window_state": state, "attribution": "Correlation only; Trends cannot prove a video's traffic source"})
    end = table(w, arows, widths={"video_and_date": 45, "attribution": 40})
    blk = [(r["video_and_date"][:26], r["mean_90d_before"], r["mean_upload_pm7d"]) for r in arows if r["mean_90d_before"] is not None][:14]
    block(w, ["upload", "90d before", "upload +-7d"], blk, end + 3, 1)
    bar(w, "Trend state at upload: 90-day baseline vs upload week", end + 3, 1, len(blk), 2, f"L2", comment=
        "Uploads that launched into a spike (upload week >=15% above the prior 90 days): Okoro neuropathy (91-94.5 vs 71-77), SHH colon cleanse 502K (63 vs 51), SHH first clove video Sep 2025 (worldwide 63 vs 54), Doctor Thomas BP-timing (19K), and Doctor Thomas stroke (a heat-stroke artefact; the video failed). Several of the biggest winners launched in dips or zero-interest windows: Ares sleeping 1.48M, Ares bath 507K, Ares anesthesia 613K, Elias eyesight 569K, Ares nocturia 351K.")

    # ---------------- 13 EXTERNAL
    w = ws["13_EXTERNAL_VIRAL_BENCHMARKS"]
    end = table(w, C["EXT"], cols=["cluster", "role", "channel", "handle", "title", "views_live", "age_relative", "format", "video_ref", "is_cohort_channel", "retrieved", "source_file"], widths={"title": 60})
    end2 = table(w, C["SMALL"], start_row=end + 3)
    cl = defaultdict(lambda: [0, 0])
    int_map = {"C01_clove": ["Senior Health Hub"], "C02_neuropathy": ["Dr. Okoro"], "C03_diabetes_feet": ["Dr. Okoro", "Dr. Ares Senior"], "C04_walking_falls": ["Doctor Thomas", "Dr. Aliza Wright | Advice"],
               "C05_nocturia": ["Dr. Ares Senior", "Dr. Elias Senior Health"], "C06_sleep_stroke": ["Dr. Ares Senior"], "C07_bp_meds": ["Dr. Aliza Wright | Advice", "Dr. Elias Senior Health"],
               "C08_kidney": ["Dr. Okoro"], "C09_colon": ["Senior Health Hub"], "C10_bathing": ["Dr. Ares Senior", "Dr. Elias Senior Health"], "C11_eyes": ["Dr. Elias Senior Health"],
               "C12_anesthesia": ["Dr. Ares Senior"], "C13_pills_heart": ["Dr. Ares Senior"]}
    kw = {"C01_clove": "clove", "C02_neuropathy": "neuropathy", "C03_diabetes_feet": "feet|foot", "C04_walking_falls": "walk", "C05_nocturia": "pee", "C06_sleep_stroke": "sleeping position",
          "C07_bp_meds": "amlodipine", "C08_kidney": "creatinine", "C09_colon": "colon", "C10_bathing": "bath", "C11_eyes": "eye", "C12_anesthesia": "anesthesia", "C13_pills_heart": "pills"}
    blk = []
    for c in sorted(int_map):
        imax = max([v["views"] for v in videos if v["channel"] in int_map[c] and any(k in v["title"].lower() for k in kw[c].split("|"))] or [0])
        emax = max([e["views_live"] or 0 for e in C["EXT"] if e["cluster"] == c and not e["is_cohort_channel"]] or [0])
        blk.append((c[4:], round(math.log10(max(imax, 1)), 2), round(math.log10(max(emax, 1)), 2)))
    r0 = end2 + 3
    block(w, ["cluster", "internal best (log10 views)", "external best (log10 views)"], blk, r0, 1)
    bar(w, "Internal vs external topic evidence: best video per cluster (log10 views)", r0, 1, len(blk), 2, f"E{r0}", comment=
        "In 11 of 13 clusters an external video beats the cohort's best (cohort at scrape-time views), so the cohort is not the demand ceiling. Only anesthesia and common-pills are led by a cohort video, and both are recent Dr. Ares originals. Colon cleanse demand is served mostly by clinician Shorts; clove's top video is Dr. Berg's 5.9M.")

    # ---------------- 14 TITLE
    w = ws["14_TITLE_ANALYSIS"]
    end = table(w, C["TF"])
    tf = [t for t in C["TF"] if t["n_with"] >= 15 and not t["note"]]
    block(w, ["feature", "with", "without"], [(t["feature"][4:], t["median_multiple_with"], t["median_multiple_without"]) for t in tf], end + 3, 1)
    bar(w, "Title feature performance (within-channel median multiple, n>=15)", end + 3, 1, len(tf), 2, "H2", comment=
        "Once channel size is removed, title features move medians by less than 1x. Mechanism, named food and time promise lean positive; list, named drug and 'specificity' regex lean negative. The pass-1 '3.5x' effects were channel-mix artefacts (DQ-12).")

    # ---------------- 15 THUMBNAIL
    w = ws["15_THUMBNAIL_ANALYSIS"]
    end = table(w, C["THM"]["rows"], widths={"exact_thumbnail_text": 50, "dominant_visual_elements": 35, "analyst_note": 50, "title": 45})
    fp = C["THM"]["feature_performance"]
    r0 = end + 3
    block(w, ["feature", "median multiple with", "median multiple without"], [(f["feature"][:30], f["median_multiple_with"], f["median_multiple_without"]) for f in fp], r0, 1)
    bar(w, "Thumbnail feature performance (LIVE_WEB_VISUAL, within-channel median multiple)", r0, 1, len(fp), 2, f"E{r0}", horizontal=True, comment=
        "Withholding the answer is the clearest thumbnail signal (1.90x vs 0.47x; none of 14 answer-revealing thumbnails reached 3x). Large numbers help; warning icons and cluttered infographics hurt. Illustrated-sketch results are confounded with the Ares/Elias channel template.")

    # ---------------- 16 HOOK / SCRIPT
    w = ws["16_HOOK_SCRIPT_ANALYSIS"]
    block(w, ["hook archetype", "n", "median multiple", "hit rate", "fail rate"], [(h["archetype"], h["n"], h["median_multiple"], h["hit_rate_ge3x"], h["fail_rate_lt0_5x"]) for h in C["HOOKS"]], 1, 1)
    bar(w, "Hook archetype (first ~30s, actual transcript) - median multiple", 1, 1, len(C["HOOKS"]), 1, "H1", comment=
        "Direct-command openings ('look at your feet right now') perform best (1.65x); warning-led openings are the worst (0.32x, 14 of 22 below half of channel median). Archetype is a lexical heuristic on the actual first ~30 seconds.")
    r0 = len(C["HOOKS"]) + 4
    block(w, ["script archetype", "n", "median multiple", "hit rate", "fail rate"], [(h["archetype"], h["n"], h["median_multiple"], h["hit_rate_ge3x"], h["fail_rate_lt0_5x"]) for h in C["SCRIPTS"]], r0, 1)
    bar(w, "Script archetype (whole transcript) - median multiple", r0, 1, len(C["SCRIPTS"]), 1, "H20", comment=
        "Story-led scripts (>=1 story beat per 1,000 words) edge out list-led and explainer scripts; evidence-claim-heavy scripts do not outperform. Differences are modest - structure is not a standalone lever.")
    deep = []
    for vid, r in TX.items():
        if not r.get("in_deep_sample_149"):
            continue
        g = lambda k: (r.get(k) or {}).get("approx_seconds") if isinstance(r.get(k), dict) else None
        p = r.get("per_1000_words") or {}
        f30 = r.get("opening_30s_flags") if isinstance(r.get("opening_30s_flags"), dict) else {}
        deep.append({"video_id": vid, "channel": r["channel"], "views": r["views"], "multiple": r["outlier_multiple_vs_channel_median"], "transcript_status": r.get("transcript_status"),
                     "words": r.get("word_count"), "wpm": r.get("words_per_minute"), "hook_archetype": r.get("hook_archetype"), "script_archetype": r.get("script_archetype"),
                     "first_15s_actual": r.get("opening_first_15s"), "first_30s_actual": r.get("opening_first_30s"), "first_60s_actual": r.get("opening_first_60s"),
                     "audience_id_30s": f30.get("audience_id"), "authority_30s": f30.get("authority"), "credibility_30s": f30.get("credibility"), "fear_30s": f30.get("fear"),
                     "hope_30s": f30.get("hope"), "curiosity_30s": f30.get("curiosity"), "open_loop_30s": f30.get("open_loop"), "story_30s": f30.get("story"),
                     "first_authority_s": g("first_authority_cue"), "first_credibility_s": g("first_credibility_cue"), "first_open_loop_s": g("first_open_loop"),
                     "first_payoff_s": g("first_enumerated_payoff"), "first_cta_s": g("first_cta"), "first_bridge_s": g("first_bridge"),
                     "enumerations": (r.get("counts") or {}).get("enumeration"), "story_per_1k": p.get("story"), "fear_per_1k": p.get("fear"), "hope_per_1k": p.get("hope"),
                     "evidence_cited_per_1k": p.get("credibility"), "specific_study_claims_per_1k": p.get("specific_study_claim"), "pattern_interrupts_per_1k": p.get("pattern_interrupt"),
                     "fear_escalation_ratio": r.get("fear_escalation_ratio_2nd_half_vs_1st"), "medical_claim_count": (r.get("counts") or {}).get("medical_claim"),
                     "cure_language_per_1k": p.get("cure_language"), "disclaimers": (r.get("counts") or {}).get("disclaimer"), "ai_disclosure": r.get("transcript_ai_disclosure_present"),
                     "information_density_numbers_per_100w": r.get("information_density_numbers_per_100w"), "ending_actual": r.get("ending_last_60_words"),
                     "time_label": "APPROXIMATED_FROM_WORD_POSITION", "transcript_path": r.get("transcript_path")})
    table(w, deep, start_row=40, widths={"first_15s_actual": 45, "first_30s_actual": 50, "first_60s_actual": 55, "ending_actual": 50})

    # ---------------- 17 AUDIENCE PSYCHOLOGY
    aud = []
    for g in C["GT"]:
        for q in (g.get("rising_queries") or [])[:6]:
            aud.append({"trends_id": g["id"], "seed_query": g["query"], "geo": g["geo"], "property": g["property"], "rising_or_breakout_query": q,
                        "use_as": "audience language / emerging topic", "evidence_label": "LIVE_GOOGLE_TRENDS"})
    end = table(ws["17_AUDIENCE_PSYCHOLOGY"], aud, widths={"rising_or_breakout_query": 60})
    psych = [("Lived-moment opening", "Winners open inside a nightly/daily moment (2:47 a.m., pills on the nightstand, feet under the breakfast table)", "Pairs 1, 4, 17, 24"),
             ("Independence fear > death fear", "Falls/walking and 'stay independent' framing beat death-threat framing; extreme-fear thumbnails n=6 are channel-confounded", "Thomas cluster; pair 11"),
             ("Permission/relief", "Topics that relieve a worry (bathing less often is fine; timing of pills) travel without search demand", "GT-20; Ares 507K"),
             ("Identity/pride", "Age-band flattery ('Ages 75-85... you're rare') beat jargon on the same channel", "Pair 21"),
             ("Doctor distrust", "Distrust hooks ('doctors won't tell you') appear in both winners and losers; not a separator; ethically avoid", "Pairs 3, 4, 9, 26"),
             ("Hair/women clove audience", "Clove's Trends rising intent is hair and women's wellness - not seniors", "GT-01, GT-30")]
    block(ws["17_AUDIENCE_PSYCHOLOGY"], ["pattern", "finding", "evidence"], psych, end + 3, 1)

    # ---------------- 18 LIFECYCLE
    w = ws["18_CHANNEL_LIFECYCLE"]
    months = sorted({v["upload_date"][:7] for v in videos})
    chn = [c["channel"] for c in CH.values()]
    block(w, ["month"] + [c[:14] for c in chn], [[m] + [sum(1 for v in videos if v["channel"] == c and v["upload_date"][:7] == m) for c in chn] for m in months], 1, 1)
    bar(w, "Upload timeline: uploads per month by channel", 1, 1, len(months), len(chn), "I1", stacked=True, comment=
        "Senior Health Hub is the only channel with a 12-month history; the other five launched between March and August 2026, so their 'lifecycle' is 1-5 months. The cohort is young - long-term decay patterns are mostly unobservable.")
    r0 = len(months) + 4
    block(w, ["month"] + [c[:14] for c in chn], [[m] + [sum(1 for v in videos if v["channel"] == c and v["upload_date"][:7] == m and v["outlier_multiple_vs_channel_median"] >= 10) for c in chn] for m in months], r0, 1)
    bar(w, "Breakout timeline: videos >=10x channel median per month", r0, 1, len(months), len(chn), "I22", stacked=True, comment=
        "Breakouts cluster in short bursts: Doctor Thomas's three hits within 10 days of June 2026, Okoro's two in May-June, Ares/Elias in August-September. Bursts suggest topic clusters or distribution windows rather than steady improvement.")
    r1 = r0 + len(months) + 3
    life = [{"channel": c["channel"], "joined": c["raw_channel_metadata"].get("channel_joined_date"), "first_upload": c["earliest_available_upload"],
             "breakout_video": c["top_video"]["title"], "breakout_date": c["top_video"]["upload_date"],
             "videos_before_breakout": sum(1 for v in videos if v["channel"] == c["channel"] and v["upload_date"] < c["top_video"]["upload_date"]),
             "median_before": st.median([v["views"] for v in videos if v["channel"] == c["channel"] and v["upload_date"] < c["top_video"]["upload_date"]] or [0]),
             "median_after": st.median([v["views"] for v in videos if v["channel"] == c["channel"] and v["upload_date"] > c["top_video"]["upload_date"]] or [0])} for c in CH.values()]
    table(w, life, start_row=r1)

    # ---------------- 19 FOLLOW-UPS
    fu = []
    for h in [v for v in videos if v["outlier_multiple_vs_channel_median"] >= 10]:
        d0 = h["upload_date"]
        nxt = [v for v in videos if v["channel"] == h["channel"] and d0 < v["upload_date"] <= str(__import__("datetime").date.fromisoformat(d0) + __import__("datetime").timedelta(days=30))]
        fu.append({"hit_video": h["video_id"], "channel": h["channel"], "hit_date": d0, "hit_views": h["views"], "hit_multiple": h["outlier_multiple_vs_channel_median"], "hit_title": h["title"],
                   "follow_ups_30d": len(nxt), "follow_up_median_multiple": round(st.median([v["outlier_multiple_vs_channel_median"] for v in nxt]), 2) if nxt else None,
                   "follow_ups_>=3x": sum(v["outlier_multiple_vs_channel_median"] >= 3 for v in nxt),
                   "follow_up_titles": " | ".join(f"{v['title'][:50]} ({v['views']:,})" for v in nxt[:6])})
    table(ws["19_CLUSTER_FOLLOWUPS"], sorted(fu, key=lambda r: r["hit_date"]), widths={"hit_title": 45, "follow_up_titles": 90})

    # ---------------- 20 COMPETITION MAP / 22 SATURATION
    comp = []
    tmap = {"C01_clove": "GT-01", "C02_neuropathy": "GT-04", "C03_diabetes_feet": "GT-05", "C04_walking_falls": "GT-28", "C05_nocturia": "GT-10", "C06_sleep_stroke": "GT-17", "C07_bp_meds": "GT-12",
            "C08_kidney": "GT-14", "C09_colon": "GT-15", "C10_bathing": "GT-20", "C11_eyes": "GT-21", "C12_anesthesia": "GT-18", "C13_pills_heart": None}
    gtd = {g["id"]: g for g in C["GT"]}
    for c in sorted(int_map):
        rows_c = [e for e in C["EXT"] if e["cluster"] == c]
        roles = Counter(e["role"] for e in rows_c)
        g = gtd.get(tmap[c]) if tmap[c] else None
        comp.append({"cluster": c[4:], "external_videos_sampled": len(rows_c), "large_or_evergreen_winners": roles["LARGE_WINNER"] + roles["OLDER_EVERGREEN_WINNER"],
                     "recent_winners": roles["RECENT_WINNER"], "medium_winners": roles["MEDIUM_WINNER"], "mill_duplicates_or_failed_copies": roles["CONTENT_MILL_DUPLICATE"] + roles["FAILED_COPY_OR_LOW_REACH"],
                     "shorts_share": round(sum(e["format"] == "SHORT" for e in rows_c) / len(rows_c), 2), "trends_id": tmap[c] or "NONE",
                     "trends_last12w_mean": g.get("last_12w_mean") if g else None, "trends_5y_change": round(g["last_12w_mean"] / max(g["first_12w_mean"], 1), 2) if g and g.get("first_12w_mean") is not None else None})
    w = ws["20_COMPETITION_MAP"]
    end = table(w, comp)
    sc = [r for r in comp if r["trends_last12w_mean"] is not None]
    block(w, ["cluster", "copies/failed (competition proxy)", "Trends last-12w mean (demand)"], [(r["cluster"], r["mill_duplicates_or_failed_copies"], r["trends_last12w_mean"]) for r in sc], end + 3, 1)
    scatter(w, "Demand vs competition by cluster (live Trends vs copy count)", end + 3, 2, 3, len(sc), "M2", "copy/failed-copy count in search sample", "Trends last-12-week mean", comment=
            "Clusters in the upper-left (high demand, few copies) are the best openings: neuropathy and creatinine. Nocturia, foot-signs and anesthesia sit right - flooded with copies within days of a hit. Bathing shows the demand proxy failing: near-zero search, yet 600K-view videos.")
    sat = [{"cluster": r["cluster"], "saturation": "SATURATED (copies >=5)" if r["mill_duplicates_or_failed_copies"] >= 5 else "CONTESTED" if r["large_or_evergreen_winners"] >= 3 else "OPEN",
            "evidence": f"{r['mill_duplicates_or_failed_copies']} low-reach copies; {r['large_or_evergreen_winners']} large winners; Trends {r['trends_last12w_mean']}"} for r in comp]
    sat += [{"cluster": n[2], "saturation": "WHITESPACE (no cohort coverage)", "evidence": n[3]} for n in S.NEW_CONCEPTS if n[0] in ("N05", "N06", "N10", "N11", "N16")]
    table(ws["22_SATURATION_WHITESPACE"], sat, widths={"cluster": 50, "evidence": 90})

    # ---------------- 21 OPPORTUNITY MATRIX
    risk = {"LOW": 1, "LOW-MEDIUM": 2, "MEDIUM": 3, "HIGH": 4}
    opp = []
    for t in S.FIRST10:
        ev_n = sum(t[k].count(";") + 1 for k in ("winners", "external", "evidence"))
        opp.append({"concept": t["topic"], "source": "FIRST_10", "evidence_items": ev_n, "medical_risk_score": risk.get(t["medical"].split(" ")[0], 3) if t["medical"].split(" ")[0] in risk else (2 if t["medical"].startswith("SUPPORTED") else 3),
                    "competition": t["competition"][:60]})
    for n in S.NEW_CONCEPTS:
        opp.append({"concept": n[2], "source": n[0], "evidence_items": n[3].count(";") + 1, "medical_risk_score": risk.get(n[4].split(" ")[0], 3), "competition": "see 20_COMPETITION_MAP"})
    w = ws["21_OPPORTUNITY_MATRIX"]
    end = table(w, opp, widths={"concept": 70})
    scatter(w, "Opportunity matrix: evidence depth vs medical risk", 1, 3, 4, len(opp), "H2", "evidence items (count)", "medical risk (1 low - 4 high)", comment=
            "Top-left = strong evidence, low risk (falls/walking, nocturia, bathing, creatinine explainer). High-evidence but high-risk items (named BP drugs, common pills) are kept only with pharmacist review and non-alarmist wording.")

    # ---------------- 23 POSITIONING / 24 PILLARS
    pos = [("Audience", "Adults 65-85 (and adult children) managing 1+ chronic condition or daily medication; US first, UK/CA/AU secondary (GT-09, GT-24, GT-29)"),
           ("Promise", "Plain-English answers to the questions older adults actually search and live with - with the source on screen"),
           ("Differentiator vs cohort", "Evidence-first (linked sources, no fabricated studies, no composite patients presented as real), original demonstrations; cohort channels share templates, typos and unsupported claims (MV-03/07/08/09/19)"),
           ("Persona", "Real, named clinician or clearly labelled presenter; avoid persona names shared across channels (Aliza/Ares/Elias clones)"),
           ("Tone", "Lived-moment openings, curiosity with withheld answers, no death-threat thumbnails, no doctor-distrust framing"),
           ("Format", "Long-form 10-20 min core; chair/seated follow-along series; Shorts as separate experiment (ALG26-CLM-005)"),
           ("What we will not copy", "Exact titles from the network, 'heals/reverses/flush' claims, 'I tried X for 7 days' fabrications, 'stop walking' contrarianism")]
    block(ws["23_CHANNEL_POSITIONING"], ["element", "positioning (evidence-backed)"], pos, 1, 1)
    ws["23_CHANNEL_POSITIONING"].column_dimensions["B"].width = 120
    w = ws["24_CONTENT_PILLARS"]
    pil = Counter()
    for t in S.FIRST10:
        pil[t["topic"].split(":")[0][:30]] += 1
    pill = [("Mobility & Falls", 3, "Thomas 1.0M/596K/329K; Cochrane; GT-07/08/28; TopHealthTips 1.9M/1.5M"),
            ("Medication Safety", 3, "Aliza persona 941K; Ares 647K; GT-12/13/32; TIME trial"),
            ("Sleep & Night", 3, "Ares 1.48M/404K; Elias 387K; GT-10/16/17"),
            ("Diabetes, Feet & Kidneys", 3, "Okoro 494K/101K/11K; GT-04/05/14/24"),
            ("Daily Living & Surgery", 2, "Ares 507K/613K; Elias 556K; GT-18/20"),
            ("Digestion & Remedies (non-launch)", 1, "SHH clove franchise 3.09M; saturated; MV-03/07")]
    block(w, ["pillar", "evidence strength (1-3)", "key evidence"], pill, 1, 1)
    w.column_dimensions["C"].width = 90; w.column_dimensions["A"].width = 30
    bar(w, "Launch-pillar evidence strength", 1, 1, len(pill), 1, "E1", comment=
        "Four pillars have multi-channel, multi-source evidence (internal winners + external winners + live Trends). Digestion/remedies has the largest single video but the weakest safe path - it is kept out of the launch 10.")
    # First-10 pillar evidence chart
    lp = [(t["topic"][:28], len(t["evidence"].split(";")) + len(t["winners"].split(";")) + len(t["external"].split(";"))) for t in S.FIRST10]
    block(w, ["launch video", "evidence items"], lp, 12, 1)
    bar(w, "First 10: evidence items per launch video", 12, 1, len(lp), 1, "E20", horizontal=True, comment=
        "Every launch video rests on at least 5 independent evidence items (internal winners, external winners, live Trends, medical sources). Anesthesia and bathing have the thinnest search evidence and are flagged as browse-dependent bets.")

    # ---------------- 25 FIRST 50 / 26 LAUNCH / 27 EXPERIMENTS
    w = ws["25_FIRST_50_VIDEOS"]
    end = table(w, C["f50"], cols=["video_number", "decision", "decision_evidence", "pillar", "topic", "angle", "title_dir", "risk", "confidence"], widths={"decision_evidence": 70, "title_dir": 55, "angle": 40})
    table(w, [dict(zip(["id", "pillar", "concept", "evidence", "medical_risk", "discovered_from"], n)) for n in S.NEW_CONCEPTS], start_row=end + 3, widths={"concept": 55, "evidence": 70})
    table(ws["26_LAUNCH_SEQUENCE"], S.FIRST10, widths={k: 45 for k in S.FIRST10[0]})
    exp = [{"launch": t["n"], "topic": t["topic"], "hypothesis": t["hypothesis"], "invalidated_if": t["invalidate"], "measure": "28-day views vs channel median; first-party CTR/AVD/traffic source once available",
            "one_variable_changed": "packaging variant only if <1x at day 14 (one change at a time, CS-024)"} for t in S.FIRST10]
    end = table(ws["27_EXPERIMENTATION_PLAN"], exp, widths={"hypothesis": 50, "invalidated_if": 60, "topic": 40})
    rules = [("Allocation", "~70% evidenced pillars / ~30% whitespace (N05, N06, N10, N11, N16) - CS-012 heuristic"),
             ("Success threshold", ">=3x channel median at 28 days = hit; <0.5x = failure (same thresholds as cohort analysis)"),
             ("Follow-up rule", "Publish mapped follow-up #1 within 7 days of any >=3x video; #2 within 21 days (Okoro bridge evidence, ALG26-CLM-006)"),
             ("No-copy rule", "Never reuse an existing title verbatim (ALG26-CLM-009; C03/C12/C13 copies fail)"),
             ("Medical gate", "Every UNSUPPORTED/PARTIAL claim in 28_MEDICAL_VALIDATION must use its safe reframing before publishing"),
             ("Data gate", "Ingest first-party YouTube Analytics export after video 5 (pipeline READY_FOR_REAL_DATA)")]
    block(ws["27_EXPERIMENTATION_PLAN"], ["rule", "definition"], rules, end + 3, 1)

    # ---------------- 28 MEDICAL, 29 EVIDENCE, 30 GLOSSARY, 31-36
    table(ws["28_MEDICAL_VALIDATION"], [dict(zip(["id", "claim", "appears_in", "source", "source_type", "verdict", "safe_reframing"], m)) for m in S.MEDICAL],
          widths={"claim": 50, "appears_in": 35, "source": 70, "safe_reframing": 60})
    table(ws["29_EVIDENCE_REGISTER"], C["EV"], widths={"claim_or_observation": 90, "source_path_or_url": 60, "evidence_label": 30})
    NE = len(C["EV"]) + 1
    gl = [("Outlier multiple", "views / own-channel median views (all repository videos of that channel)"), ("Hit", ">=3x channel median"), ("Failure", "<0.5x channel median"),
          ("APPROXIMATED_FROM_WORD_POSITION", "seconds estimated as word index x (duration / word count); transcripts have no timestamps"),
          ("TRANSCRIPT_LEXICAL_HEURISTIC", "regex detection on actual transcript text; detects wording, not intent"),
          ("LIVE_WEB_VISUAL", "thumbnail inspected in a browser from its i.ytimg.com URL on 2026-09-25"),
          ("LIVE_GOOGLE_TRENDS", "value read from Google Trends widget data on 2026-09-24/25; 0-100 relative, not volume"),
          ("CLEAN / TIME_CONFOUNDED / INVALID_CONTROL", "matched-pair validity: <=18 days apart / >18 days / not a like-for-like topic"),
          ("Content-mill duplicate", "near-verbatim title from a low-reach channel appearing after an original hit"),
          ("Persona clone", "same presenter name used by more than one channel"),
          ("SUPPORTED / PARTIAL / UNSUPPORTED / CONTRADICTED", "medical verdict against authoritative sources"),
          ("Creator claim vs platform fact", "DS-000018 statuses from repository primary validation (2026-09-04/24)")]
    block(ws["30_GLOSSARY"], ["term", "definition"], gl, 1, 1)
    ws["30_GLOSSARY"].column_dimensions["A"].width = 40; ws["30_GLOSSARY"].column_dimensions["B"].width = 110
    table(ws["31_DATA_CORRECTIONS"], [dict(zip(["id", "location", "previous_claim", "verified_value", "evidence"], d)) for d in C["DQ"]], widths={"previous_claim": 45, "verified_value": 80, "evidence": 35})
    table(ws["32_DUPLICATE_NETWORK"], C["dup"]["rows"], widths={"title": 60})
    table(ws["33_HISTORICAL_CONTEXT"], [dict(zip(["id", "event", "date", "source", "video", "distance_from_upload", "possible_relevance", "confidence"], h)) for h in S.HISTORY],
          widths={"event": 45, "source": 50, "video": 45, "possible_relevance": 60})
    table(ws["34_DS000011_TRACE"], [dict(zip(["knowledge_unit", "framework", "videos_tested_against", "observed_evidence", "counterexample", "result", "contributes_to"], r)) for r in S.DS11], widths={k: 40 for k in ["framework", "videos_tested_against", "observed_evidence", "counterexample"]})
    table(ws["35_DS000018_CLAIMS"], [dict(zip(["claim_id", "claim", "original_source", "claim_status", "official_youtube_support", "internal_senior_health_evidence", "external_evidence", "counterexample", "practical_implication"], r)) for r in S.DS18], widths={k: 40 for k in ["claim", "official_youtube_support", "internal_senior_health_evidence", "external_evidence", "counterexample", "practical_implication"]})
    table(ws["36_DS000031_FRAMEWORKS"], [dict(zip(["framework", "concept_ids", "internal_supporting_example", "internal_counterexample", "external_supporting_example", "limitation", "senior_health_implication"], r)) for r in S.DS31], widths={k: 45 for k in ["internal_supporting_example", "internal_counterexample", "external_supporting_example", "senior_health_implication"]})

    # ---------------- 01 DASHBOARD (formulas)
    w = ws["01_EXECUTIVE_DASHBOARD"]
    ER = "'29_EVIDENCE_REGISTER'"
    kpi = [("Videos in cohort", f"=COUNTA({VM}!A2:A{NV})"), ("Channels", 6), ("Total views (scrape)", f"=SUM({VM}!F2:F{NV})"),
           ("Transcripts analysed (words>0)", f"=COUNTIF({VM}!K2:K{NV},\">0\")"), ("Videos >=3x channel median", f"=COUNTIF({VM}!H2:H{NV},\">=3\")"),
           ("Videos <0.5x channel median", f"=COUNTIF({VM}!H2:H{NV},\"<0.5\")"), ("Evidence records", f"=COUNTA({ER}!A2:A{NE})"),
           ("Live Trends investigations", f"=COUNTIF({ER}!B2:B{NE},\"GOOGLE_TRENDS_QUERY\")"), ("Live thumbnail observations", f"=COUNTIF({ER}!B2:B{NE},\"THUMBNAIL_OBSERVATION\")"),
           ("External videos mapped", f"=COUNTIF({ER}!B2:B{NE},\"EXTERNAL_VIDEO\")"), ("Deep transcript records", f"=COUNTIF({ER}!B2:B{NE},\"DEEP_TRANSCRIPT\")"),
           ("Medical fact-checks", f"=COUNTIF({ER}!B2:B{NE},\"MEDICAL_FACT_CHECK\")"), ("Data-quality corrections", f"=COUNTIF({ER}!B2:B{NE},\"DATA_QUALITY_CORRECTION\")")]
    block(w, ["KPI", "value (formula)"], kpi, 1, 1)
    w.column_dimensions["A"].width = 40; w.column_dimensions["B"].width = 18
    block(w, ["id", "major conclusion", "confidence", "evidence"], C["CONCLUSIONS"], 17, 1)
    w.column_dimensions["B"].width = 18; w.column_dimensions["C"].width = 30
    for r in range(18, 18 + len(C["CONCLUSIONS"])):
        w.cell(row=r, column=2).alignment = Alignment(wrap_text=True)
    w.column_dimensions["B"].width = 90

    # ---------------- 00 README / 37 chart commentary
    w = ws["00_READ_ME"]
    lines = ["SENIOR HEALTH COMPETITIVE INTELLIGENCE - FORENSIC WORKBOOK V2 (2026-09-25)",
             "Built by docs/research/senior-health-2026-09-25/forensic-v2/scripts/build_outputs.py from repository evidence + live web research.",
             "Cohort: 6 channels, 306 videos (registry DB). Deep population: 149 videos (DEEP-ANALYSIS-SAMPLE.json).",
             "Evidence labels: REPOSITORY_FACT, ACTUAL_TRANSCRIPT_TEXT, TRANSCRIPT_LEXICAL_HEURISTIC, APPROXIMATED_FROM_WORD_POSITION, LIVE_WEB_VISUAL, LIVE_GOOGLE_TRENDS, LIVE_WEB_SEARCH_RESULT, WEB_RESEARCH, ANALYTICAL_CONCLUSION.",
             "Causation is never proven: no first-party CTR, retention, impressions or traffic-source data exist for any cohort video.",
             "Pass-1 files are preserved unchanged; corrections are listed in 31_DATA_CORRECTIONS.",
             "Formulas: 01 dashboard, 03 scorecards, 04 multiple column, 05 bins recalculate from 04_VIDEO_MASTER / 29_EVIDENCE_REGISTER. Chart source blocks are static values computed by the build script (documented beside each chart).", "", "SHEETS:"] + names
    for i, l in enumerate(lines, 1):
        w.cell(row=i, column=1, value=l).font = Font(name=F, bold=(i == 1))
    w.column_dimensions["A"].width = 150
    table(ws["37_CHART_COMMENTARY"], [{"sheet": a, "chart": b, "plain_english_commentary": c} for a, b, c in CHARTS], widths={"chart": 55, "plain_english_commentary": 120})
    for sh, title, com in CHARTS:
        pass
    from openpyxl.workbook.properties import CalcProperties
    wb.calculation = CalcProperties(fullCalcOnLoad=True)
    wb.save(out)
    print("workbook:", out, "sheets:", len(names), "charts:", len(CHARTS))
