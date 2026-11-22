#!/usr/bin/env python3
"""Refresh This_Phase columns in PRIOR_RESEARCH_COVERAGE.csv and progress notes in RESEARCH_GAP_REGISTER.csv from validated per-video QA."""
import csv, json, os
RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
done = {}
for v in os.listdir(os.path.join(RDIR, "videos")):
    p = os.path.join(RDIR, "videos", v, "QA.json")
    if os.path.exists(p):
        q = json.load(open(p))
        if q["all_checks_pass"]:
            done[v] = q["analysis_depth"].split(" ")[0]
rows = list(csv.DictReader(open(os.path.join(RDIR, "PRIOR_RESEARCH_COVERAGE.csv"))))
base = [k for k in rows[0].keys() if not k.startswith("This_Phase")]
for r in rows:
    d = done.get(r["Video_ID"])
    r["This_Phase_Forensics"] = ("%s_VALIDATED_AUDIO_LISTENING_BLOCKED" % d) if d else ("BLOCKED_SOURCE_MISSING" if r["Overall_Prior_Coverage"] == "BLOCKED_SOURCE_MISSING" else "NOT_STARTED")
    r["This_Phase_Evidence_Path"] = ("research/casually-finance-editing-forensics/videos/%s/" % r["Video_ID"]) if d else ""
with open(os.path.join(RDIR, "PRIOR_RESEARCH_COVERAGE.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=base + ["This_Phase_Forensics", "This_Phase_Evidence_Path"])
    w.writeheader(); w.writerows(rows)
gaps = list(csv.DictReader(open(os.path.join(RDIR, "RESEARCH_GAP_REGISTER.csv"))))
n = len(done)
prog = {
 "GAP-001": "IN_PROGRESS: %d of 32 uncovered videos have validated per-video forensics (see STATUS.json)" % sum(1 for r in rows if r["Overall_Prior_Coverage"] == "NONE" and r["Video_ID"] in done),
 "GAP-002": "NOT_STARTED: no prior-covered video re-reviewed yet",
 "GAP-003": "PARTIAL: 6 clean easing fits in 3 videos (5 linear, 1 decelerating); not systematic",
 "GAP-004": "PARTIAL: preliminary TYPOGRAPHY_AND_LAYOUT_SPEC.md from %d videos; typeface/weight/size unmeasured" % n,
 "GAP-005": "PARTIAL: ASSET_APPEARANCES per video with variants; cross-video identity is analyst-labelled",
 "GAP-006": "BLOCKED: unchanged",
 "GAP-007": "OPEN: new ASR also uncertified",
 "GAP-008": "IN_PROGRESS: Whisper small.en run for every analysed video (not certified)",
 "GAP-009": "OPEN: limits recorded per video",
 "GAP-010": "BLOCKED: unchanged",
 "GAP-011": "OPEN: unchanged",
 "GAP-012": "PARTIAL: sample result n=%d (77%% of moving frames conventional, 9%% complex, 13%% undetermined); not channel-wide" % n,
 "GAP-013": "PARTIAL: UNRESOLVED_CHANGE rows keep unflagged-but-detected changes visible in depth C videos",
 "GAP-014": "PARTIAL: preliminary recipe library and blueprint from Shorts only",
}
base_g = [k for k in gaps[0].keys() if k != "Progress_Note"]
for g in gaps:
    g["Progress_Note"] = prog.get(g["Gap_ID"], "")
with open(os.path.join(RDIR, "RESEARCH_GAP_REGISTER.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=base_g + ["Progress_Note"]); w.writeheader(); w.writerows(gaps)
print(n, "videos validated; registers refreshed")
