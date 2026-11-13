#!/usr/bin/env python3
"""PDFs 12 to 15: compile existing synthesis markdown (reuses the channel-PDF builder helpers)."""
import html, importlib.util, subprocess
from pathlib import Path
R = Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location("b", R / "_scripts/build_channel_pdfs_2026-11-13.py"); b = importlib.util.module_from_spec(sp); sp.loader.exec_module(b)
S4 = R / "04_FINAL_SYNTHESIS"
DOCS = [("12_Topic_Discovery_And_Competition_Research", "Topic Discovery and Competition Research",
         [(S4/"TOPIC_DISCOVERY_PILOT_2026-11-13.md", "Topic discovery pilot, sections 1 to 16 (16 candidates, 0 strict PASS, 1 PASS-DEPTH conditional)")]),
        ("13_Approved_First_10_Videos", "Approved First 10 Videos",
         [(S4/"APPROVED_FIRST_10_VIDEOS_2026-11-14.md", "Result: 0 of 10 approved, with the screening table")]),
        ("14_New_Channel_Launch_Blueprint", "New Channel Launch Blueprint",
         [(S4/"CHANNEL_BLUEPRINT_2026-11-14.md", "Blueprint (HYPOTHESIS, with test and kill rule)")]),
        ("15_Complete_Research_Executive_Report", "Complete Research Executive Report",
         [(S4/"EXECUTIVE_REPORT_2026-11-14.md", "Executive report"),
          (S4/"PLAYBOOK_RUBRIC_SCORECARD_2026-11-14.md", "Playbook rubric scorecard")])]
for stem, title, parts in DOCS:
    body = "".join(f"<h2>{i}. {html.escape(t)}</h2><p><code>{p.relative_to(R)}</code></p>{b.md(p.read_text())}" for i, (p, t) in enumerate(parts, 1))
    cover = (f'<div class="cover"><h1>{title}</h1><p>Finance &amp; Economics YouTube study &middot; 2026-11-14</p>'
             '<div class="box"><b>Evidence labels:</b> VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention, traffic UNKNOWN. '
             'Strict screen: 0 PASS of 16 candidates; 1 conditional PASS-DEPTH (not approved); nothing was force-filled. The launch model is a HYPOTHESIS with a test and a kill rule.</div></div>')
    out = R / "06_PDF_REPORTS" / stem
    out.with_suffix(".html").write_text(f"<!doctype html><meta charset=utf-8><title>{title}</title><style>{b.CSS}</style>{cover}{body}")
    subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}.pdf", f"file://{out}.html"], check=True, capture_output=True, timeout=180)
    print(out.with_suffix(".pdf"))
