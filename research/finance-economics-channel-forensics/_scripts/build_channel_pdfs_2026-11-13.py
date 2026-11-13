#!/usr/bin/env python3
"""Build the 9 channel PDFs from existing report markdown (no new claims).
Usage: build_channel_pdfs_2026-11-13.py [only_prefix]   e.g. 059
Pipeline: small md->html, inline-SVG views chart (from VIDEO_INVENTORY.csv), headless Chrome -> PDF.
"""
import csv, html, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REP = ROOT / "01_CHANNEL_REPORTS"
OUT = ROOT / "06_PDF_REPORTS"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CH = [("01", "066_econ_in_a_nutshell", "Econ_in_a_Nutshell", "Econ in a Nutshell"),
      ("02", "037_casual_finance", "Casual_Finance", "Casual Finance"),
      ("03", "055_primate_economics", "Primate_Economics", "Primate Economics"),
      ("04", "039_crayon_capital", "Crayon_Capital", "Crayon Capital"),
      ("05", "024_monkeyexplains", "MonkeyExplains", "MonkeyExplains"),
      ("06", "040_economics_explained", "Economics_Explained", "Economics Explained"),
      ("07", "059_capital_case", "Capital_Case", "Capital Case"),
      ("08", "070_pennyexplainsfinance", "Penny_Explains_Finance", "PENNY (Penny Explains Finance)"),
      ("09", "071_paperbillionstv", "Paper_Billions_TV", "Paper Billions TV")]

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\w)", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    return re.sub(r"(?<![\"'>=])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)

def md(text):
    out, lines, i, para, lst = [], text.split("\n"), 0, [], None
    def flush():
        nonlocal para, lst
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if lst: out.append(f"</{lst}>"); lst = None
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            flush(); j = i + 1; buf = []
            while j < len(lines) and not lines[j].startswith("```"): buf.append(lines[j]); j += 1
            out.append("<pre>" + html.escape("\n".join(buf)) + "</pre>"); i = j + 1; continue
        if l.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            flush(); rows = [l]; i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"): rows.append(lines[i]); i += 1
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells(rows[0])) + "</tr></thead><tbody>"
            for r in rows[1:]: t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>"
            out.append(t + "</tbody></table>"); continue
        m = re.match(r"^(#{1,6})\s+(.*)", l)
        if m: flush(); n = min(len(m.group(1)) + 1, 6); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif re.match(r"^\s*[-*]\s+", l):
            if lst != "ul": flush(); out.append("<ul>"); lst = "ul"
            out.append("<li>" + inline(re.sub(r"^\s*[-*]\s+", "", l)) + "</li>")
        elif re.match(r"^\s*\d+[.)]\s+", l):
            if lst != "ol": flush(); out.append("<ol>"); lst = "ol"
            out.append("<li>" + inline(re.sub(r"^\s*\d+[.)]\s+", "", l)) + "</li>")
        elif l.startswith(">"): flush(); out.append("<blockquote>" + inline(l.lstrip("> ")) + "</blockquote>")
        elif not l.strip(): flush()
        else:
            if lst: flush()
            para.append(l.strip())
        i += 1
    flush(); return "\n".join(out)

def chart(d):
    f = REP / d / "VIDEO_INVENTORY.csv"
    if not f.exists(): return "<p><i>Chart: UNAVAILABLE (is channel ka VIDEO_INVENTORY.csv DB mein nahi).</i></p>"
    v = sorted((float(r["views"]) for r in csv.DictReader(f.open()) if r["fmt"] == "long" and r["views"]), reverse=True)
    if not v: return ""
    W, H, mx = 680, 150, max(v); bw = W / len(v)
    bars = "".join(f'<rect x="{k*bw+1:.1f}" y="{H-x/mx*H:.1f}" width="{bw-2:.1f}" height="{x/mx*H:.1f}" fill="#2b5fa8"/>' for k, x in enumerate(v))
    med = sorted(v)[len(v) // 2]
    return (f'<figure><svg viewBox="0 0 {W} {H+4}" width="100%">{bars}</svg>'
            f'<figcaption>Figure 1. Long-video views (DB snapshot), high to low, n={len(v)}. Max {mx:,.0f}, median {med:,.0f}. '
            f'Source: VIDEO_INVENTORY.csv (fmt=long). Views alag dates par collect hue ho sakte hain.</figcaption></figure>')

CSS = """@page{size:A4;margin:18mm 15mm 18mm 15mm;@bottom-center{content:counter(page) " / " counter(pages);font-size:9pt;color:#666}}
body{font:10.5pt/1.45 -apple-system,Helvetica,Arial,sans-serif;color:#1a1a1a}
h1{font-size:22pt;margin:0 0 4pt}h2{font-size:15pt;border-bottom:2px solid #2b5fa8;padding-bottom:2pt;margin-top:18pt;break-after:avoid}
h3,h4{break-after:avoid;margin-bottom:3pt}table{border-collapse:collapse;width:100%;font-size:8.5pt;margin:6pt 0}
th,td{hyphens:none;border:1px solid #bbb;padding:3pt 4pt;vertical-align:top;overflow-wrap:break-word}th{background:#eef2f8}tr{break-inside:avoid}
code{font-size:8.5pt;background:#f2f2f2;padding:0 2pt;overflow-wrap:anywhere}pre{font-size:8pt;background:#f6f6f6;padding:5pt;white-space:pre-wrap;overflow-wrap:anywhere}
blockquote{border-left:3px solid #c90;margin:6pt 0;padding:2pt 8pt;background:#fff8e6}a{color:#1a4f9c;overflow-wrap:anywhere}
.cover{break-after:page;padding-top:60mm}.box{border:1px solid #c90;background:#fff8e6;padding:6pt 10pt;margin-top:14pt;font-size:9.5pt}
figure{margin:8pt 0;break-inside:avoid}figcaption{font-size:8.5pt;color:#555}"""

def build(num, d, slug, name):
    live = (REP / d / "LIVE_EVIDENCE_2026-11-13.md").read_text()
    rep = REP / d / "CHANNEL_REPORT.md"
    body = (f"<h2>1. Views overview</h2>{chart(d)}<h2>2. Live evidence pass (2026-11-13)</h2>{md(live)}")
    if rep.exists():
        body += f"<h2>3. Database forensic report (earlier pass, 2026-11-12)</h2>{md(rep.read_text())}"
    else:
        body += "<h2>3. Database forensic report</h2><p>UNAVAILABLE: channel DB mein nahi hai; sirf Apify + live pass bana hai.</p>"
    cover = (f'<div class="cover"><h1>{html.escape(name)}</h1><p>Forensic Report {num} of 9 &middot; Finance &amp; Economics YouTube study &middot; 2026-11-13</p>'
             f'<p>Source folder: <code>research/finance-economics-channel-forensics/01_CHANNEL_REPORTS/{d}/</code></p>'
             '<div class="box"><b>Evidence labels:</b> VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention aur traffic-source is channel ke liye UNKNOWN hain. '
             'Ye PDF maujooda reports ka compile hai; is mein naya claim nahi joda gaya.<br><br>'
             '<b>Abhi nahi hua (PDF spec ke muqabil):</b> Playbook rubric ka page-numbered score; har video ka full watch log '
             '(sirf sample dekha gaya, baaqi NOT WATCHED); thumbnail sirf jahan report mein likha wahan VERIFIED; Studio data.</div></div>')
    h = f"<!doctype html><meta charset=utf-8><title>{html.escape(name)}</title><style>{CSS}</style>{cover}{body}"
    OUT.mkdir(exist_ok=True)
    stem = OUT / f"{num}_{slug}_Forensic_Report"
    stem.with_suffix(".html").write_text(h)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={stem}.pdf", f"file://{stem}.html"], check=True, capture_output=True, timeout=180)
    return stem.with_suffix(".pdf")

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    for num, d, slug, name in CH:
        if only and not d.startswith(only): continue
        print(build(num, d, slug, name))
