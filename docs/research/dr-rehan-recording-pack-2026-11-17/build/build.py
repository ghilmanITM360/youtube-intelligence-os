# -*- coding: utf-8 -*-
import html, re, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import content_a, content_b, content_c, content_d
from sources import S, ACC

WPM = 130           # assumed natural pace (editorial assumption, NOT measured)
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TITLE = "Dr. Rehan Omer: Recording Pack and Complete Scripts (11 Videos)"
DRAFT = "Draft for Dr. Rehan Omer's clinical review"
CLASS = {"G": "Established clinical guidance", "O": "Observational research finding",
         "I": "Individualized decision / clinician judgment", "U": "Unresolved or insufficient evidence"}

V = content_a.V + content_b.V + content_c.V
for v in V:
    segs = list(v["segs"])
    for ins in content_d.INSERT.get(v["id"], []):
        segs.insert(len(segs) - 1, ins)
    v["segs"] = segs
    v["trim"] = content_d.TRIM.get(v["id"], "")
    pause = 0.5 if v["fmt"] == "Short" else 1.5
    cum = 0; t = 0.0
    for i, s in enumerate(segs):
        s["w"] = len(s["t"].split())
        s["start"] = cum / WPM * 60 + i * pause
        cum += s["w"]
        s["end"] = cum / WPM * 60 + i * pause
        if "open" not in s:
            s["open"] = re.split(r"(?<=[.?!])\s", s["t"])[0]
    v["words"] = cum
    v["sec"] = cum / WPM * 60 + pause * len(segs)
    v["pace_needed"] = cum / (60 - pause * len(segs)) * 60  # wpm needed to finish in 60 s

def mmss(x):
    x = int(round(x)); return f"{x//60}:{x%60:02d}"
def dur(v):
    return mmss(v["sec"])
e = html.escape
def rng(v):
    lo = v["words"] / 150 * 60; hi = v["words"] / 110 * 60
    return f"{mmss(lo)}-{mmss(hi)}"

def src_links(ids):
    out = []
    for p in re.split(r"[,;]\s*", ids):
        p = p.strip()
        if p in S:
            out.append(f'<a href="#{p}">{p}</a>')
        elif p:
            out.append(e(p))
    return ", ".join(out)

# ----------------------------------------------------------------------------- CSS
CSS = """
:root{--ink:#16202b;--mute:#566271;--line:#c9d1da;--accent:#0b5c6b;--warn:#8a2b0b;--bg:#f3f7f9;--ok:#1f6f3f}
@page{size:A4;margin:16mm 15mm 18mm 15mm;
 @bottom-center{content:"%(draft)s  |  Page " counter(page) " of " counter(pages);font:9pt Helvetica,Arial,sans-serif;color:#566271}}
@page cue{size:A4 landscape;margin:9mm 12mm 13mm 12mm;
 @bottom-center{content:"%(draft)s  |  Page " counter(page) " of " counter(pages);font:9pt Helvetica,Arial,sans-serif;color:#566271}}
*{box-sizing:border-box}
body{font:11pt/1.5 Helvetica,Arial,sans-serif;color:var(--ink);margin:0}
a{color:#0b4f9c;text-decoration:underline;word-break:break-word}
h1{font-size:26pt;line-height:1.15;margin:0 0 6pt}
h2{font-size:17pt;margin:0 0 6pt;color:var(--accent);border-bottom:2px solid var(--accent);padding-bottom:3pt}
h3{font-size:13pt;margin:12pt 0 4pt}
h4{font-size:11.5pt;margin:8pt 0 3pt;color:var(--accent)}
p{margin:4pt 0}
.draft{display:inline-block;border:2px solid var(--warn);color:var(--warn);padding:4pt 9pt;font-weight:700;border-radius:4pt;letter-spacing:.3pt}
.brk{page-break-before:always}
.cover{padding-top:18mm}
.mute{color:var(--mute)}
.small{font-size:9.5pt}
table{width:100%%;border-collapse:collapse;margin:6pt 0;page-break-inside:auto}
tr{page-break-inside:avoid}
th,td{border:1px solid var(--line);padding:5pt 6pt;vertical-align:top;text-align:left}
th{background:#e6eef2;font-size:10pt}
td{font-size:10pt}
.box{border:1px solid var(--line);background:var(--bg);padding:7pt 10pt;border-radius:4pt;margin:6pt 0}
.warn{border-left:5px solid var(--warn);background:#fbf1ec}
.ok{border-left:5px solid var(--ok);background:#eef7f1}
.must{color:#7a1d1d;font-weight:700}
.q{color:#4a5560;font-style:italic}
.tag{display:inline-block;font-size:8.5pt;font-weight:700;padding:1pt 5pt;border-radius:3pt;margin-right:4pt;background:#e6eef2;color:#16445a}
.cue{page:cue}
.cue h2{font-size:14pt;margin-bottom:2pt;padding-bottom:2pt}
.cue .meta{display:flex;gap:8pt;margin:3pt 0 4pt}
.cue .meta div{flex:1;border:1px solid var(--line);padding:3pt 6pt;background:var(--bg);font-size:9.5pt;line-height:1.25}
.cue .first{border:3px solid var(--accent);padding:4pt 9pt;font-size:14pt;font-weight:700;line-height:1.25;margin:4pt 0;background:#fff}
.cue table{margin:3pt 0}
.cue table td,.cue table th{font-size:9.6pt;line-height:1.22;padding:2.5pt 4pt}
.cue.short table td{font-size:11.2pt;line-height:1.3;padding:4pt 6pt}
.cue.short .first{font-size:17pt;padding:5pt 10pt}
.cue.short .meta div{font-size:11pt}
.cue .legend{font-size:9pt;color:var(--mute);margin:2pt 0}
.cue ul{margin:0;padding-left:12pt}
.cue li{margin:0}
.cue .small{font-size:8.5pt}
.sug{background:#eef7f1}
.pres{background:#fbeeee}
.opt{background:#fff9e6}
.script p{margin:5pt 0}
.ts{display:inline-block;min-width:44pt;color:var(--accent);font-weight:700;font-size:9.5pt}
.hdr{display:flex;justify-content:space-between;align-items:baseline}
.pill{font-size:9pt;padding:2pt 6pt;border-radius:10pt;background:var(--accent);color:#fff}
.toc a{text-decoration:none}
.toc td{font-size:10.5pt}
code{font-size:9pt}
""" % {"draft": DRAFT}

# ----------------------------------------------------------------------------- HTML parts
def cover():
    return f"""
<section class="cover">
<p><span class="draft">{DRAFT.upper()}</span></p>
<h1>{e(TITLE)}</h1>
<p class="mute">Channel: Decode Your Heart (Dr. Rehan Omer). Publishing window: 19 Nov to 16 Dec 2026. Prepared 17 Nov 2026. All durations are <b>ESTIMATED</b> (no timed read has been done).</p>
<div class="box warn"><b>Read this first.</b>
<ul>
<li><b>Nothing here is clinically approved.</b> Dr. Rehan must review every medical statement and the cue sheets before recording.</li>
<li><b>BP pill recall (19 Nov): news-specific version is NOT ready.</b> The owner has not said which recall the slot targets. An evergreen recall-checking script is ready, plus two FDA-verified candidate recalls as optional variants (pending confirmation).</li>
<li><b>Statin Short (20 Nov):</b> the existing long video was not available in the repository, so this is a fresh recording script and no edit timestamps are given.</li>
<li><b>Audience country is unknown.</b> Emergency numbers are stated as "your emergency number" in the spoken scripts. Confirm the country (US 911; Rescue 1122 verified for Punjab only) before on-screen text is made.</li>
<li><b>Source access:</b> several guideline sites blocked automated reading (JACC, Circulation, USPSTF in part). Where only a secondary summary was read, the claim table says so.</li>
</ul></div>
<h3>How this one PDF is organized</h3>
<table class="toc"><tr><th>Part</th><th>What is in it</th><th>Use</th></tr>
<tr><td>Calendar</td><td>All 11 videos, formats, recommended titles, estimated lengths</td><td>Producer / doctor</td></tr>
<tr><td>Part 1</td><td>Doctor recording cue sheets (landscape pages): exact opening, points, must-preserve, optional examples, delivery notes, interviewer questions</td><td>On camera, paper or tablet</td></tr>
<tr><td>Part 2</td><td>Packaging, complete scripts with timestamps and word counts, editor notes, claim-to-source tables, unresolved issues</td><td>Doctor review, editor, producer</td></tr>
<tr><td>Part 3</td><td>Storytelling patterns used, source register with links and access status, verification results</td><td>Reviewer</td></tr></table>
<h3>Timing method (assumption)</h3>
<p class="small">Duration = words / 130 words per minute + 0.5 s (Shorts) or 1.5 s (long videos) per section for pauses. 130 wpm is an editorial assumption for conversational delivery, not a measurement. A 110-150 wpm range is shown for long videos. Shorts also show the minimum speaking pace needed to finish within 60 s. <b>Replace all estimates with a timed read.</b></p>
<h3>Colour key on cue sheets</h3>
<p class="small"><span class="tag" style="background:#eef7f1">Suggested wording</span> you may paraphrase. <span class="tag" style="background:#fbeeee">Must preserve</span> a medical distinction or action that cannot be omitted. <span class="tag" style="background:#fff9e6">Optional</span> only if time permits.</p>
</section>"""

def calendar():
    rows = []
    for v in V:
        t = v["titles"][v["rec"]]
        est = dur(v) + (f' ({rng(v)})' if v["fmt"] == "Long" else "")
        rows.append(f'<tr><td>{e(v["date"])}</td><td>{v["fmt"]}</td><td><b>{e(v["topic"])}</b></td><td>{e(t)}</td><td>{v["words"]}</td><td>{est}</td><td><a href="#v{v["id"]}">script</a> / <a href="#c{v["id"]}">cue sheet</a></td></tr>')
    return f"""
<section class="brk"><h2>Calendar, recommended titles and estimated length</h2>
<table><tr><th>Date</th><th>Format</th><th>Approved topic</th><th>Recommended title</th><th>Words</th><th>Est. length</th><th>Go to</th></tr>{''.join(rows)}</table>
<p class="small mute">Est. length: 130 wpm with pauses; the bracket shows 150 wpm to 110 wpm. Shorts must stay at or under 1:00 including closing line.</p></section>"""

def cuesheet(v):
    short = v["fmt"] == "Short"
    rows = []
    for s in v["segs"]:
        tw = f'{mmss(s["start"])}-{mmss(s["end"])}'
        first = ""
        if s.get("q"):
            first = f'<div class="q">Interviewer (off camera): "{e(s["q"])}"</div>'
        cue = "".join(f"<li>{e(x)}</li>" for x in s.get("cue", []))
        must = "".join(f"<li>{e(x)}</li>" for x in s.get("must", []))
        opt = f'<div class="opt" style="padding:3pt 5pt;margin-top:4pt"><b>Optional:</b> {e(s["opt"])}</div>' if s.get("opt") else ""
        note = f'<div style="margin-top:4pt"><b>Delivery:</b> {e(s["note"])}</div>' if s.get("note") else ""
        rows.append(f"""<tr><td style="width:11%"><b>{tw}</b><br><span class="small mute">{e(s["l"])}</span></td>
<td style="width:24%" class="sug">{first}"{e(s["open"])}"{note}</td>
<td style="width:33%" class="sug"><ul>{cue}</ul>{opt}</td>
<td style="width:32%" class="pres"><b>Must preserve</b><ul>{must}</ul></td></tr>""")
    first_words = " ".join(v["segs"][0]["open"].split()[:9])
    dc = "short" if short else ""
    meta = f"""<div class="meta"><div><b>Main question</b><br>{e(v["question"])}</div><div><b>One-sentence answer</b><br>{e(v["core"])}</div><div><b>Estimated length</b><br>{dur(v)} ({v["words"]} words)<br><span class="small">{'Needs about %d wpm or faster to stay under 60 s' % round(v["pace_needed"]) if short else 'Not timed; range ' + rng(v)}</span></div></div>"""
    interviewer = "" if short else '<p class="legend">Interviewer questions are in the same order as the table. Doctor: answer in full sentences that repeat the question\'s subject, so the answers work after the interviewer\'s voice is removed.</p>'
    variants = ""
    if v["variants"]:
        variants = ("<p class='small' style='margin:2pt 0'><b>Optional news variants (PENDING, not ready):</b> see Part 2, video %d.</p>" % v["id"]) if v["id"] == 1 else ("<p class='small' style='margin:2pt 0'><b>Edit note (existing long video not available):</b> see Part 2, video %d.</p>" % v["id"])
    variants_inline = (" &nbsp;|&nbsp; <b>News variants PENDING: see Part 2</b>" if v["id"] == 1 else (" &nbsp;|&nbsp; <b>Edit note: see Part 2</b>" if v["id"] == 2 else ""))
    variants = ""
    return f"""
<section class="cue brk {dc}" id="c{v['id']}">
<div class="hdr"><h2>{v['id']}. {e(v['topic'])} <span class="pill">{v['fmt']}</span></h2><div><b>{e(v['date'])}</b></div></div>
<div class="small mute">Title (recommended): {e(v['titles'][v['rec']])} &nbsp;|&nbsp; Thumbnail text: <b>{e(v['thumb'])}</b> &nbsp;|&nbsp; {DRAFT}{variants_inline}</div>
{meta}
<div class="first"><span class="small mute" style="font-weight:400">First 3 seconds, say exactly ({len(v['segs'][0]['open'].split())} words):</span> "{e(v['segs'][0]['open'])}"</div>
{interviewer}
<table><tr><th>Time window</th><th>Exact opening / transition</th><th>Points to explain naturally</th><th>Meaning that must remain accurate</th></tr>{''.join(rows)}</table>
{variants}
</section>"""

def part2(v):
    short = v["fmt"] == "Short"
    titles = "".join(f"<li>{'<b>' if i==v['rec'] else ''}{e(t)}{' (recommended)</b>' if i==v['rec'] else ''}</li>" for i, t in enumerate(v["titles"]))
    script = ""
    for s in v["segs"]:
        q = f'<p class="q">[Interviewer] {e(s["q"])}</p>' if s.get("q") else ""
        script += f'{q}<p><span class="ts">{mmss(s["start"])}</span> {e(s["t"])} <span class="small mute">({s["w"]} words, {e(s["l"])})</span></p>'
    variants = ""
    for name, txt in v["variants"]:
        variants += f'<div class="box warn"><b>{e(name)}</b><br>{e(txt)}</div>'
    editor = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in v["editor"])
    claims = "".join(f'<tr><td>{e(c[0])}</td><td><span class="tag">{c[1]}</span> {CLASS[c[1]]}</td><td>{src_links(c[2])}</td><td>{e(c[3])}</td></tr>' for c in v["claims"])
    unres = "".join(f"<li>{e(u)}</li>" for u in v["unresolved"])
    trim = f'<div class="box small"><b>Optional cuts if the timed read is over 58 seconds:</b> {e(v["trim"])}</div>' if v["trim"] else ""
    pace = f'Needs about {round(v["pace_needed"])} wpm or faster to finish in 60 s; at 130 wpm the estimate is {dur(v)}.' if short else f'Estimate {dur(v)} at 130 wpm (range {rng(v)}).'
    return f"""
<section class="brk" id="v{v['id']}">
<div class="hdr"><h2>{v['id']}. {e(v['topic'])} <span class="pill">{v['fmt']}</span></h2><div><b>{e(v['date'])}</b></div></div>
<div class="box {'warn' if 'PENDING' in v['status'] or 'FRESH' in v['status'] else 'ok'}"><b>Status:</b> {e(v['status'])}</div>
<h4>Packaging</h4>
<table><tr><th style="width:22%">Item</th><th>Content</th></tr>
<tr><td>Viewer's main question</td><td>{e(v['question'])}</td></tr>
<tr><td>One-sentence core answer</td><td>{e(v['core'])}</td></tr>
<tr><td>Three title options</td><td><ol style="margin:0;padding-left:16pt">{titles}</ol></td></tr>
<tr><td>Recommended title and why</td><td><b>{e(v['titles'][v['rec']])}</b><br>{e(v['rec_why'])}</td></tr>
<tr><td>Thumbnail text</td><td><b>{e(v['thumb'])}</b> (real photo of Dr. Rehan, one simple medical image, answer not shown)</td></tr>
<tr><td>Estimated duration</td><td>{v['words']} spoken words. {pace} <b>ESTIMATED, not timed.</b></td></tr></table>
<h4>A. Complete reference script (all spoken words)</h4>
<div class="script">{script}</div>
<p class="small mute">Total: {v['words']} spoken words. Timestamps are estimates at 130 wpm.</p>
{trim}{variants}
<h4>B. Editor notes (tied to specific lines)</h4>
<table><tr><th style="width:34%">At this line</th><th>Note</th></tr>{editor}</table>
<h4>C. Claim-to-source table</h4>
<table><tr><th style="width:32%">Claim</th><th style="width:18%">Evidence type</th><th style="width:11%">Source</th><th>Qualification</th></tr>{claims}</table>
<p class="small mute">Evidence type: G established guidance, O observational finding, I individualized decision, U unresolved. Source IDs link to the register in Part 3.</p>
<h4>D. Unresolved verification issues</h4><ul>{unres}</ul>
</section>"""

STORY = """
<section class="brk" id="story"><h2>Part 3A. Storytelling patterns applied</h2>
<p><b>Where the patterns come from.</b> Internal channel research on the senior-health niche (branch <code>origin/claude/dr-rehan-seniors-health-data-5db7ab</code>, folder <code>docs/research/dr-rehan-content-plan-2026-11-16/</code>, files 05 and 06; plus the repository's 56 Dr. Rehan transcripts). Files 08 and 09 (script-research results and script map) were not re-read line by line for this pack. No YouTube Studio data (retention, CTR) exists, so nothing below is claimed to be "proven".</p>
<table><tr><th>Technique</th><th>What the research shows (label)</th><th>How it is used here</th></tr>
<tr><td>Open with the viewer's own question or situation</td><td>OBSERVED: competitor winners open with a scene, a question or a stat; one analyzed channel used the same opening in both hits and flops, so opening alone is not a cause. HYPOTHESIS: a recognisable question aids clarity.</td><td>Every script opens with the viewer's question in the first sentence; no suspense before urgent advice.</td></tr>
<tr><td>Fast first answer</td><td>INFERRED from the research: real-clinician conversational videos state the answer early. Brief requires an answer within ~20-30 s on long videos.</td><td>Every long script gives the answer or safe action in its first segment (about 20-35 s).</td></tr>
<tr><td>Credential line kept short</td><td>OBSERVED: a real geriatrician's conversational style does well; Dr. Rehan's current transcripts are short and jargon-heavy with no recap.</td><td>Credential is the sign-off name only; jargon is explained immediately (ECG, TIA, ABI, orthostatic).</td></tr>
<tr><td>Three to five connected sections with transitions</td><td>OBSERVED: listicle-style spines are common; re-hooks are rare (0.25 per 1,000 words in the sample).</td><td>Sections are question-driven, not forced numbered lists; the interviewer's next question is the transition.</td></tr>
<tr><td>Concrete examples</td><td>OBSERVED: winners use scenes and patient cases; many "patients" in the niche are composite or unverified personas.</td><td>Only clearly labelled illustrative examples ("not a real patient"). Real anonymized cases are offered as optional cue-sheet items, never invented.</td></tr>
<tr><td>Curiosity followed by a genuine answer</td><td>HYPOTHESIS only (no retention data).</td><td>Titles ask the real question; the answer is delivered, never withheld for suspense.</td></tr>
<tr><td>Recap and one next action</td><td>OBSERVED: recap and a specific next step recur in winning videos.</td><td>Every long video ends with a short recap and an action; no early subscribe request.</td></tr>
<tr><td>Things avoided</td><td>Research flags "Cardiologist Warns" templates, fake numbers and clone wording as saturated or misleading.</td><td>No fear framing, no "doctors hide this", no copied competitor wording.</td></tr></table>
<p class="small mute">Public view counts show reach, not retention, and do not show which storytelling choice caused performance. No new competitor URLs were recorded in this pass, so no new competitor observation dates exist.</p></section>"""

def register():
    rows = ""
    for k, (org, title, url, date, status) in S.items():
        cls = "warn" if status.startswith(("BLOCKED", "NOT", "SUMMARY")) else ""
        rows += f'<tr id="{k}"><td><b>{k}</b></td><td>{e(org)}<br><b>{e(title)}</b><br><a href="{e(url)}">{e(url)}</a></td><td>{e(date)}</td><td>{ACC}</td><td class="{cls}">{e(status)}</td></tr>'
    return f"""
<section class="brk" id="reg"><h2>Part 3B. Source register</h2>
<p class="small">Access date for all sources: {ACC}. Dates are shown exactly as seen; "not captured" means the date was not read, and none has been invented. READ = the page was opened and read in this pass. SUMMARY = only a search summary or secondary report was read, so the claim is flagged. BLOCKED = the site refused automated reading.</p>
<table><tr><th style="width:6%">ID</th><th>Organization, title, link</th><th style="width:20%">Published / updated</th><th style="width:9%">Accessed</th><th style="width:16%">Read status</th></tr>{rows}</table></section>"""

def checks():
    rows = ""
    def row(a, b, c):
        return f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>"
    rows += row("All 11 topics included", "Yes: 4 Shorts + 7 long videos in the calendar order", "PASS (automated)")
    for v in V:
        if v["fmt"] == "Short":
            ok = 105 <= v["words"] <= 125 and v["sec"] <= 60
            rows += row(f"Short {v['id']} ({v['topic']})", f"{v['words']} words; estimate {dur(v)}; needs >= {round(v['pace_needed'])} wpm to stay under 60 s", "PASS on estimate" if ok else "CHECK")
        else:
            ok = 5*60 <= v["sec"] <= 8*60
            rows += row(f"Long {v['id']} ({v['topic']})", f"{v['words']} words; estimate {dur(v)}; range {rng(v)}", "PASS on estimate" if ok else "CHECK")
    rows += row("Every title answered", "Each recommended title is delivered by the first segment or the full script", "PASS (manual review)")
    rows += row("Unsupported statistics", "Only figures with a source: ASA 'nearly 1 in 5 suspected TIAs, 90 days'; BP thresholds (AHA, CDC); ABI categories; recall lots from FDA; no invented numbers", "PASS (manual review)")
    rows += row("Observational vs causal", "Winter, walking speed and TIA statements use 'association' wording", "PASS (manual review)")
    rows += row("Medication qualifications", "No script tells viewers to stop, start or change a medicine; 'do not stop suddenly' is stated where relevant", "PASS (manual review)")
    rows += row("Emergency instructions match audience", "Spoken: 'your emergency number'. On-screen number needs the owner's country decision", "OPEN (owner decision)")
    rows += row("Recall date/country/product/batches verified", "Two FDA-verified candidates; intended recall unconfirmed; news-specific version not marked ready", "OPEN (owner decision)")
    rows += row("Cue sheets preserve essential meaning", "Each segment lists must-preserve items taken from the full script", "PASS (manual review)")
    rows += row("Timed read completed", "Not done: durations are estimates", "OPEN (needs Dr. Rehan or a timed rehearsal)")
    rows += row("Clinical review by Dr. Rehan", "Not done", "OPEN")
    rows += row("Rendered PDF inspected", "See delivery message; pages rendered to images and checked for clipping, fonts and links", "Done by producer of this pack")
    return f"""
<section class="brk"><h2>Part 3C. Pre-delivery verification results</h2>
<table><tr><th style="width:30%">Check</th><th>Result</th><th style="width:20%">Status</th></tr>{rows}</table>
<h3>Open questions for the owner</h3><ol>
<li>Which recall is the 19 Nov Short about (Macleods olmesartan/amlodipine/HCTZ, Advagen metoprolol, or another)? Which country is the audience?</li>
<li>Can the existing statin long video (file or URL) be supplied so exact edit timestamps can be produced?</li>
<li>Audience country for emergency numbers and on-screen text.</li>
<li>Dr. Rehan to confirm: clinician-judgment lines (urgent low-BP actions, stroke aspirin and last-known-well lines, ABI procedure description, 2026 cholesterol-guideline statements).</li></ol></section>"""

def build_html():
    parts = [cover(), calendar()]
    parts.append('<section class="brk"><h1 style="font-size:22pt">Part 1. Doctor recording cue sheets</h1><p>Landscape pages for reading on paper or a tablet. Each Short is one page; each long video is one or two pages. Speak naturally; do not memorize the script. Ask the interviewer to keep questions in this order.</p></section>')
    for v in V: parts.append(cuesheet(v))
    parts.append('<section class="brk"><h1 style="font-size:22pt">Part 2. Complete scripts and medical sources</h1><p>Each video: packaging, full reference script with estimated timestamps, editor notes, claim-to-source table, unresolved issues.</p></section>')
    for v in V: parts.append(part2(v))
    parts += [STORY, register(), checks()]
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(TITLE)}</title><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'

# ----------------------------------------------------------------------------- Markdown
def build_md():
    L = [f"# {TITLE}", f"**{DRAFT}.** Prepared 17 Nov 2026. All durations ESTIMATED (130 wpm assumption).", ""]
    L += ["## Calendar", "| Date | Format | Topic | Recommended title | Words | Est. length |", "|---|---|---|---|---|---|"]
    for v in V: L.append(f"| {v['date']} | {v['fmt']} | {v['topic']} | {v['titles'][v['rec']]} | {v['words']} | {dur(v)} |")
    for v in V:
        L += ["", f"## {v['id']}. {v['topic']} ({v['fmt']}, {v['date']})", f"**Status:** {v['status']}", f"- Viewer question: {v['question']}", f"- Core answer: {v['core']}",
              "- Titles: " + " / ".join(f"{'**' if i==v['rec'] else ''}{t}{'**' if i==v['rec'] else ''}" for i, t in enumerate(v['titles'])), f"- Why: {v['rec_why']}", f"- Thumbnail text: {v['thumb']}",
              f"- Spoken words: {v['words']}; estimated {dur(v)} (not timed)", "", "### Reference script"]
        for s in v["segs"]:
            if s.get("q"): L.append(f"> *[Interviewer]* {s['q']}")
            L.append(f"**[{mmss(s['start'])}]** {s['t']}  \n*({s['w']} words, {s['l']})*"); L.append("")
        if v["trim"]: L.append(f"**Optional cuts:** {v['trim']}\n")
        for n, t in v["variants"]: L.append(f"**{n}:** {t}\n")
        L += ["### Doctor cue sheet", "| Time | Exact opening | Points | Must preserve |", "|---|---|---|---|"]
        for s in v["segs"]:
            q = f"*Interviewer: {s['q']}* " if s.get("q") else ""
            extra = (f" Optional: {s['opt']}" if s.get("opt") else "") + (f" Delivery: {s['note']}" if s.get("note") else "")
            L.append(f"| {mmss(s['start'])}-{mmss(s['end'])} | {q}\"{s['open']}\" | {'; '.join(s.get('cue', []))}{extra} | {'; '.join(s.get('must', []))} |")
        L += ["", "### Editor notes"] + [f"- At \"{a}\": {b}" for a, b in v["editor"]]
        L += ["", "### Claim-to-source", "| Claim | Type | Source | Qualification |", "|---|---|---|---|"]
        for c in v["claims"]: L.append(f"| {c[0]} | {CLASS[c[1]]} | {c[2]} | {c[3]} |")
        L += ["", "### Unresolved"] + [f"- {u}" for u in v["unresolved"]]
    L += ["", "## Source register (accessed " + ACC + ")", "| ID | Organization / title | Date shown | Read status |", "|---|---|---|---|"]
    for k, (o, t, u, d, st) in S.items(): L.append(f"| {k} | {o}: [{t}]({u}) | {d} | {st} |")
    return "\n".join(L)

# ----------------------------------------------------------------------------- DOCX
def build_docx(path):
    from docx import Document
    from docx.shared import Pt
    d = Document()
    d.styles["Normal"].font.size = Pt(11)
    d.add_heading(TITLE, 0); d.add_paragraph(DRAFT + ". All durations are estimated (130 wpm assumption).")
    t = d.add_table(rows=1, cols=6); t.style = "Table Grid"
    for i, h in enumerate(["Date", "Format", "Topic", "Recommended title", "Words", "Est. length"]): t.rows[0].cells[i].text = h
    for v in V:
        r = t.add_row().cells
        for i, x in enumerate([v["date"], v["fmt"], v["topic"], v["titles"][v["rec"]], str(v["words"]), dur(v)]): r[i].text = x
    for v in V:
        d.add_page_break(); d.add_heading(f"{v['id']}. {v['topic']} ({v['fmt']}, {v['date']})", 1)
        d.add_paragraph("Status: " + v["status"]); d.add_paragraph("Viewer question: " + v["question"]); d.add_paragraph("Core answer: " + v["core"])
        d.add_paragraph("Titles: " + " | ".join(v["titles"]) + f"  (recommended: {v['titles'][v['rec']]}). {v['rec_why']}")
        d.add_paragraph(f"Thumbnail text: {v['thumb']}.  Spoken words: {v['words']}; estimated {dur(v)} (not timed).")
        d.add_heading("Complete reference script", 2)
        for s in v["segs"]:
            if s.get("q"): d.add_paragraph("[Interviewer] " + s["q"]).italic = True
            d.add_paragraph(f"[{mmss(s['start'])}] {s['t']} ({s['w']} words)")
        if v["trim"]: d.add_paragraph("Optional cuts: " + v["trim"])
        for n, tx in v["variants"]: d.add_paragraph(n + ": " + tx)
        d.add_heading("Doctor cue sheet", 2)
        tb = d.add_table(rows=1, cols=4); tb.style = "Table Grid"
        for i, h in enumerate(["Time", "Exact opening / transition", "Points to explain", "Must preserve"]): tb.rows[0].cells[i].text = h
        for s in v["segs"]:
            c = tb.add_row().cells
            c[0].text = f"{mmss(s['start'])}-{mmss(s['end'])} {s['l']}"
            c[1].text = (f"Interviewer: {s['q']}\n" if s.get("q") else "") + f"\"{s['open']}\"" + (f"\nDelivery: {s['note']}" if s.get("note") else "")
            c[2].text = "\n".join("- " + x for x in s.get("cue", [])) + (f"\nOptional: {s['opt']}" if s.get("opt") else "")
            c[3].text = "\n".join("- " + x for x in s.get("must", []))
        d.add_heading("Editor notes", 2)
        for a, b in v["editor"]: d.add_paragraph(f"At \"{a}\": {b}", style="List Bullet")
        d.add_heading("Claim-to-source", 2)
        tb = d.add_table(rows=1, cols=4); tb.style = "Table Grid"
        for i, h in enumerate(["Claim", "Evidence type", "Source", "Qualification"]): tb.rows[0].cells[i].text = h
        for c in v["claims"]:
            r = tb.add_row().cells; r[0].text, r[1].text, r[2].text, r[3].text = c[0], CLASS[c[1]], c[2], c[3]
        d.add_heading("Unresolved", 2)
        for u in v["unresolved"]: d.add_paragraph(u, style="List Bullet")
    d.add_page_break(); d.add_heading(f"Source register (accessed {ACC})", 1)
    for k, (o, t, u, dt, st) in S.items(): d.add_paragraph(f"{k}: {o}. {t}. {u}. Date shown: {dt}. Status: {st}.")
    d.save(path)

if __name__ == "__main__":
    h = build_html()
    open(os.path.join(OUT, "Dr_Rehan_Recording_Pack_and_Scripts.html"), "w").write(h)
    open(os.path.join(OUT, "Dr_Rehan_Recording_Pack_and_Scripts_EDITABLE.md"), "w").write(build_md())
    build_docx(os.path.join(OUT, "Dr_Rehan_Recording_Pack_and_Scripts_EDITABLE.docx"))
    for v in V: print(v["id"], v["fmt"], v["words"], dur(v), round(v["pace_needed"]))
