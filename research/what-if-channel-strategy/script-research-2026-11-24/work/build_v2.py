"""Builds the per-video V2 files and the aggregate ledgers from content_*.py (one dict V per video).
Run from this folder: python3 build_v2.py
Writes ../videos/<folder>/{SCRIPT_V2,TITLE_AND_PACKAGING_V2,STORY_AND_VISUAL_BEATS_V2,FACT_CHECK_V2,SEVEN_LENS_REVIEW_V2,STATUS_AND_OPEN_ISSUES_V2}.md
and ../MASTER_SCIENCE_CLAIM_LEDGER_V2.csv, ../TEN_VIDEO_SCRIPT_INDEX_V2.csv.
Spoken-text word count = whitespace tokens of the voice-over paragraphs only. Runtime = estimate (2.5 and 2.75 words/s + 1.5 s per paragraph break); needs real recording."""
import csv, glob, importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CLAIM_STATUSES = {"SOURCE_CHECKED", "CALCULATED_SELF_REVIEW", "ASSUMPTION", "HYPOTHESIS", "UNRESOLVED",
                  "EXPERT_REVIEW_NEEDED", "TIME_SENSITIVE_RECHECK", "REMOVED"}
VIDEO_STATUSES = {"DRAFT_READY_FOR_OWNER_REVIEW", "DRAFT_WITH_OPEN_SCIENCE", "CONDITIONAL_DRAFT"}
LENSES = ["1 Structure and promise", "2 Curiosity and surprise", "3 Wonder and relatability", "4 Pacing and flow",
          "5 Viewer questions and payoff", "6 Clarity and international accessibility", "7 Voice, rhythm and literary quality"]


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.V


def fmt_time(sec):
    sec = int(round(sec))
    return "%d:%02d" % (sec // 60, sec % 60)


def stats(V):
    paras = V["script"]
    words = sum(len(p.split()) for p in paras)
    breaks = len(paras) - 1
    lo = words / 2.75 + 1.5 * breaks   # faster delivery
    hi = words / 2.5 + 1.5 * breaks    # calmer delivery
    return words, lo, hi


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf8") as fh:
        fh.write(text.rstrip() + "\n")


def build_video(V):
    d = os.path.join(ROOT, "videos", V["folder"])
    words, lo, hi = stats(V)
    V["_words"], V["_lo"], V["_hi"] = words, lo, hi
    assert V["status"] in VIDEO_STATUSES, V["status"]
    for c in V["claims"]:
        assert c[2] in CLAIM_STATUSES, (V["slot"], c[0], c[2])
    ids = {c[0] for c in V["claims"]}
    for b in V["beats"]:
        for cid in re.findall(r"V\d\d-C\d\d", b[3]):
            assert cid in ids, (V["slot"], "beat cites unknown claim", cid)
    voice = "\n\n".join(V["script"])
    script = f"""---
title: {V['title']}
channel: UNREGISTERED (Unreasonably Exact; CH-id pending)
images: none (no images or media were created or stored)
---

# Slot {V['slot']} · {V['fmt'].upper()} · {V['title']}

- **Recommended title:** {V['title']}
- **Calendar slot / day / format:** slot {V['slot']} · day {V['day']} · {V['fmt']} ({V['band']})
- **Version:** V2 (2026-11-24). Replaces nothing silently: the v1 text is preserved in `../../v1_baseline/`.
- **Word count (spoken text only, counted by script):** {words}
- **Estimated runtime:** {fmt_time(lo)}–{fmt_time(hi)} (planning rate 2.5–2.75 words/second plus 1.5 s per paragraph break). **An estimate only: it must be confirmed by recording and listening.** {V['runtime_note']}
- **Status:** {V['status']}. Claude self-review only: no expert, human-listener or independent review has happened.
- **Required science checks before any release:** {'; '.join(V['checks'])}

## Voice-over

{voice}

## Sources
Claim-level sources, calculations and access dates: `FACT_CHECK_V2.md` and `../../MASTER_SCIENCE_CLAIM_LEDGER_V2.csv`. {V.get('sources_note', '')}
"""
    write(os.path.join(d, "SCRIPT_V2.md"), script)

    pk = V["packaging"]
    alt = "\n".join(f"- {t}" for t in pk["alternatives"])
    five = md_table(["Part", "This video"], pk["five_part"])
    labels = "\n".join(f"- {t}" for t in pk["labels"])
    desc = "\n".join(f"- {t}" for t in pk["description"])
    tp = f"""# Title and packaging V2 · slot {V['slot']}

**Recommended title:** {V['title']}
**Alternatives (same question, different wording):**
{alt}

## Five-part title check (Playbook title engine, used as a checklist)
{five}

## Promise check
{pk['promise']}

## Title rules applied
- One dominant question; no unqualified absolutes ("every", "only", "first", "best", "last", "real reason").
- No manufactured mystery, no fear framing, no invented statistic.
- Title and thumbnail text must not claim more than the script answers. Scorecard numbers are not used: they are not a CTR predictor.

## On-screen honesty labels (proposal, owner to confirm)
{labels}

## Description, first two lines (draft)
{desc}

## Thumbnail idea (text description only; no image was made)
{pk['thumbnail']}

{pk.get('overlap', '')}
"""
    write(os.path.join(d, "TITLE_AND_PACKAGING_V2.md"), tp)

    beats = md_table(["#", "Viewer question", "What the script reveals", "Claims", "Original visual (explanatory)"], V["beats"])
    bt = f"""# Story and visual beats V2 · slot {V['slot']}

Section test used for every beat: does it deepen, complicate, escalate, humanise or move closer to the answer? Visuals are original diagrams described in words; **nothing was drawn, rendered or stored**, and no xkcd art, wording or sequence is imitated. No fixed interval timer is used: a change of presentation happens when the explanation changes.

{beats}

## Shape of this script
{V['shape']}
"""
    write(os.path.join(d, "STORY_AND_VISUAL_BEATS_V2.md"), bt)

    claims = md_table(["ID", "Claim as spoken or implied", "Status", "Value / calculation", "Source or method", "Accessed", "Reading depth", "Note"], V["claims"])
    fc = f"""# Fact check V2 · slot {V['slot']}

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

{claims}

## Title promise check
{V['promise_check']}

## Removed or rewritten from v1
{V['removed']}
"""
    write(os.path.join(d, "FACT_CHECK_V2.md"), fc)

    lens_rows = []
    for name, (issue, sent, change) in zip(LENSES, V["lenses"]):
        lens_rows.append([name, issue, sent, change])
    lr = md_table(["Lens", "Issue found", "Affected sentence or beat", "Change made"], lens_rows)
    sl = f"""# Seven-lens review V2 · slot {V['slot']}

**This is a Claude self-review (one model, one session). It is not seven independent reviewers, not an expert review and not a listener test.** The Playbook/DS-000011 title, intro and script analyzer prompts were used as checklists inside these lenses; their numeric scores are not reproduced because they are not measurements.

{lr}

## Analyzer notes
- **Title analyzer:** {V['analyzers'][0]}
- **Intro analyzer:** {V['analyzers'][1]}
- **Script analyzer:** {V['analyzers'][2]}

## Re-read after changes
{V['reread']}
"""
    write(os.path.join(d, "SEVEN_LENS_REVIEW_V2.md"), sl)

    fnd = md_table(["Finding", "Status", "What the V2 script does"], V["findings"]) if V.get("findings") else "No owner finding is attached to this slot beyond general checks."
    st = f"""# Status and open issues V2 · slot {V['slot']}

**Video status:** {V['status']} (one of DRAFT_READY_FOR_OWNER_REVIEW, DRAFT_WITH_OPEN_SCIENCE, CONDITIONAL_DRAFT). Not publication-ready, not expert-approved, no performance claim.

## Owner findings for this slot
{fnd}

## Main remaining issue
{V['main_issue']}

## Open issues
{chr(10).join('- ' + x for x in V['open'])}

## Required human or expert review (none has happened)
{chr(10).join('- ' + x for x in V['review_needed'])}

## Time-sensitive rechecks on production day
{chr(10).join('- ' + x for x in V['timesensitive']) if V['timesensitive'] else '- none beyond a general check of cited records.'}

## Relation to other slots
{V['relations']}
"""
    write(os.path.join(d, "STATUS_AND_OPEN_ISSUES_V2.md"), st)


def main():
    vids = [load(p) for p in sorted(glob.glob(os.path.join(HERE, "content_[0-9][0-9].py")))]
    vids.sort(key=lambda v: v["slot"])
    for V in vids:
        build_video(V)
    # aggregate ledgers
    with open(os.path.join(ROOT, "MASTER_SCIENCE_CLAIM_LEDGER_V2.csv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh)
        w.writerow(["claim_id", "slot", "claim", "status", "value_or_calculation", "source_or_method", "accessed", "reading_depth", "note"])
        for V in vids:
            for c in V["claims"]:
                w.writerow([c[0], V["slot"], c[1], c[2], c[3], c[4], c[5], c[6], c[7]])
    with open(os.path.join(ROOT, "TEN_VIDEO_SCRIPT_INDEX_V2.csv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh)
        w.writerow(["slot", "day", "format", "recommended_title", "folder", "words", "runtime_estimate_low", "runtime_estimate_high", "status", "main_remaining_issue"])
        for V in vids:
            w.writerow([V["slot"], V["day"], V["fmt"], V["title"], "videos/" + V["folder"], V["_words"], fmt_time(V["_lo"]), fmt_time(V["_hi"]), V["status"], V["main_issue"]])
    print("built", len(vids), "videos;", sum(len(v['claims']) for v in vids), "claims")


if __name__ == "__main__":
    main()
