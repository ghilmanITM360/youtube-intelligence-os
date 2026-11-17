#!/usr/bin/env python3
"""PDFs 10 and 11: compile existing synthesis markdown (no new claims). Reuses channel-PDF builder helpers."""
import html, importlib.util, subprocess
from pathlib import Path
R = Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location("b", R / "_scripts/build_channel_pdfs_2026-11-13.py"); b = importlib.util.module_from_spec(sp); sp.loader.exec_module(b)
S3, S4 = R / "03_CROSS_CHANNEL_FINDINGS", R / "04_FINAL_SYNTHESIS"
DOCS = [("10_Cross_Channel_Comparative_Analysis", "Cross-Channel Comparative Analysis", [
            (S4 / "NINE_CHANNEL_LIVE_COMPARISON_AND_LAUNCH_MODEL_2026-11-13.md", "Nine-channel live comparison + launch model"),
            (S3 / "CHANNEL_COMPARISON.md", "69-channel database comparison (earlier pass)"),
            (S3 / "SUB_NICHE_COMPARISON.md", "Sub-niche comparison (earlier pass)")]),
        ("11_Winning_Techniques_And_Failure_Patterns", "Winning Techniques and Failure Patterns", [
            (S3 / "REPEATED_WINNING_PATTERNS.md", "Repeated winning patterns (earlier pass)"),
            (S3 / "FAILURE_PATTERNS.md", "Failure patterns (earlier pass)"),
            (S4 / "OPENING_LINE_TEST_2026-11-13.md", "Opening-line test (181 videos)"),
            (S4 / "THUMBNAIL_AND_FRAME_PASS_2026-11-13.md", "Thumbnails, frames, endings"),
            (S4 / "FINANCE_ECONOMICS_WINNING_MODELS.md", "Winning models (earlier pass)")])]
for stem, title, parts in DOCS:
    body = "".join(f"<h2>{i}. {html.escape(t)}</h2><p><code>{p.relative_to(R)}</code></p>{b.md(p.read_text())}" for i, (p, t) in enumerate(parts, 1))
    cover = (f'<div class="cover"><h1>{title}</h1><p>Finance &amp; Economics YouTube study &middot; 2026-11-13</p>'
             '<div class="box"><b>Evidence labels:</b> VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention, traffic UNKNOWN. '
             'Ye maujooda files ka compile hai, naya claim nahi. "Earlier pass" sections 2026-11-12 ke hain aur 2026-11-13 ke live pass se bad mein reconcile hue ya nahi, har file ke andar likha hai.<br><br>'
             '<b>Abhi nahi hua:</b> har technique ke saath video link + timestamp wali table; Playbook page-number validation; blind opening/thumbnail relabel. Opening result (+0.64) label-rule par tika hai, human-blind nahi.</div></div>')
    out = R / "06_PDF_REPORTS" / stem
    out.with_suffix(".html").write_text(f"<!doctype html><meta charset=utf-8><title>{title}</title><style>{b.CSS}</style>{cover}{body}")
    subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}.pdf", f"file://{out}.html"], check=True, capture_output=True, timeout=180)
    print(out.with_suffix(".pdf"))
