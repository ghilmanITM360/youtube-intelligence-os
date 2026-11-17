#!/usr/bin/env python3
"""PDF 16: owner simple guide (Roman Urdu), same helpers as the other PDFs."""
import html, importlib.util, subprocess
from pathlib import Path
R = Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location("b", R / "_scripts/build_channel_pdfs_2026-11-13.py"); b = importlib.util.module_from_spec(sp); sp.loader.exec_module(b)
p = R / "04_FINAL_SYNTHESIS/OWNER_SIMPLE_GUIDE_2026-11-14.md"
title = "Owner Simple Guide"
out = R / "06_PDF_REPORTS/16_Owner_Simple_Guide"
cover = f'<div class="cover"><h1>{title}</h1><p>Finance &amp; Economics YouTube study &middot; 2026-11-14</p></div>'
out.with_suffix(".html").write_text(f"<!doctype html><meta charset=utf-8><title>{title}</title><style>{b.CSS}</style>{cover}{b.md(p.read_text())}")
subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}.pdf", f"file://{out}.html"], check=True, capture_output=True, timeout=180)
print(out.with_suffix(".pdf"))
