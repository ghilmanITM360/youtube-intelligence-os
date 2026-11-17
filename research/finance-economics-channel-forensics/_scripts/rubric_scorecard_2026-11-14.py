#!/usr/bin/env python3
"""Compile the Playbook rubric scorecard from the §16 tables in the 7 DB channel reports (no new scoring)."""
import re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
CH = [("066","066_econ_in_a_nutshell","Nutshell"),("037","037_casual_finance","Casual Fin."),("055","055_primate_economics","Primate"),
      ("039","039_crayon_capital","Crayon"),("024","024_monkeyexplains","Monkey"),("040","040_economics_explained","Econ Expl."),("059","059_capital_case","Capital Case")]
ABBR = {"FOLLOWED":"F","PARTIALLY FOLLOWED":"P","NOT FOLLOWED":"N","NOT TESTABLE":"-","NOT TESTABLE HERE":"-"}
rows, pages, names, counts = {}, {}, {}, {c[2]: {"F":0,"P":0,"N":0,"-":0,"?":0} for c in CH}
for num, d, short in CH:
    t = (R/"01_CHANNEL_REPORTS"/d/"CHANNEL_REPORT.md").read_text()
    sec = t.split("## 16.")[1].split("## 17.")[0]
    for l in sec.splitlines():
        m = re.match(r"^\| (P\d\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|", l)
        if not m: continue
        pid, loc = m.group(1), m.group(2)
        v = re.sub(r"[*_]", "", m.group(5)).strip().upper()
        v = ABBR.get(v) or ("P" if v.startswith("PARTIAL") else "N" if v.startswith("NOT FOLLOWED") else "F" if v.startswith("FOLLOWED") else "-" if v.startswith("NOT TEST") else "?")
        rows.setdefault(pid, {})[short] = v; pages[pid] = loc; counts[short][v] += 1
out = ["# Playbook rubric scorecard (2026-11-14)", "",
 "Labels: VERIFIED (the per-channel verdicts below are copied from each channel report's section 16, scored 2026-11-12 from DB text proxies) / INFERRED (the proxies) / UNKNOWN. Judge: *YouTube Automation: Complete Master Playbook*, 556 pp, sha256 `c630c24b...576d`, page numbers in the Playbook column are the report's own references.",
 "",
 "**Not scored:** PENNY and Paper Billions (not in the DB, so no transcripts and no section 16). This table is **not** a measure of how good a channel is: F/P/N says whether a channel's behaviour matches a Playbook rule, and several rules are only proxied by text patterns. Studio CTR/retention are UNKNOWN, so rules that depend on them are '-'.",
 "", "Key: F = FOLLOWED, P = PARTIALLY FOLLOWED, N = NOT FOLLOWED, - = NOT TESTABLE, ? = verdict text not parsed.", "",
 "| ID | Playbook rule (pages) | " + " | ".join(c[2] for c in CH) + " |", "|---|---|" + "---|"*len(CH)]
for pid in sorted(rows):
    out.append(f"| {pid} | {pages[pid]} | " + " | ".join(rows[pid].get(c[2], "") for c in CH) + " |")
out += ["", "## Counts per channel (22 rules)", "", "| channel | F | P | N | - | ? |", "|---|---|---|---|---|---|"]
for c in CH: k = counts[c[2]]; out.append(f"| {c[2]} | {k['F']} | {k['P']} | {k['N']} | {k['-']} | {k['?']} |")
(R/"04_FINAL_SYNTHESIS"/"PLAYBOOK_RUBRIC_SCORECARD_2026-11-14.md").write_text("\n".join(out)+"\n")
print("\n".join(out[-12:]))
