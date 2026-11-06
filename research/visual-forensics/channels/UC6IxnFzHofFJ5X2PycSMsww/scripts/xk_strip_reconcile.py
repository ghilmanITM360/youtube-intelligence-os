"""Reconcile strip_rv2 vs STRUCTURED ledgers (shot_ledger starts + SHOT_CUT events) per segment; no ledger writes.
ledger_cuts = distinct frames in (seg_start, seg_end] that are a shot_ledger start_frame or a SHOT_CUT-class event start_frame.
rv2 internal_cuts excludes the segment-boundary cut-in. new_cuts = max(0, rv2 - ledger_cuts). token_prior = SHOT_CUT tokens in prior class (heuristic, kept for transparency).
Writes campaign/strip_review/strip_rv2/reconcile.csv"""
import csv, collections, pathlib
B = pathlib.Path("campaign/strip_review"); V = pathlib.Path("videos")
T = {(r["video"], r["seg"]): r for r in csv.DictReader(open(B / "strip_tasks_rv2.csv"))}
A = {(r["video"], r["seg"]): r for r in csv.DictReader(open(B / "strip_rv2/strip_annotations.csv"))}
assert set(T) == set(A), "task/annotation key mismatch"
out = []; per = collections.Counter(); tot = collections.Counter()
for (v, s), t in T.items():
    a = A[(v, s)]
    seg = next(r for r in csv.DictReader(open(V / v / "tables/segments_v1.csv")) if r["seg"] == s)
    lo, hi = int(seg["start_frame"]), int(seg["end_frame"])
    fr = {int(r["start_frame"]) for r in csv.DictReader(open(V / v / "shot_ledger.csv")) if lo < int(r["start_frame"]) <= hi}
    fr |= {int(r["start_frame"]) for r in csv.DictReader(open(V / v / "visual_event_ledger.csv")) if "SHOT_CUT" in r["event_class"] and lo < int(r["start_frame"]) <= hi}
    rv = int(a["internal_cuts"]); new = max(0, rv - len(fr)); tok = t["prior_class"].split("+").count("SHOT_CUT")
    out.append(dict(video=v, seg=s, verdict=a["verdict"], seg_frames=f"{lo}-{hi}", ledger_cuts_inside=len(fr), token_prior=tok, rv2_internal_cuts=rv,
                    already_recorded=min(len(fr), rv), new_cuts=new, integrate=("YES_NEW_CUTS" if new else "YES_REFINE_TEXT_ONLY" if a["verdict"] == "REFINES" else "NO_CONFIRMED")))
    per[v] += new; tot["ledger"] += len(fr); tot["rv2"] += rv; tot["already"] += min(len(fr), rv); tot["new"] += new; tot[a["verdict"]] += 1
w = csv.DictWriter(open(B / "strip_rv2/reconcile.csv", "w", newline=""), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print(dict(tot), {k: x for k, x in per.items() if x})
