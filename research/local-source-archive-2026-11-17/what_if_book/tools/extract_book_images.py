#!/usr/bin/env python3
"""Extract every non-page-sized embedded image from the source PDF."""
import csv
import hashlib
import json
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = next(ROOT.glob("Randall-Munroe-What-If*.pdf"))
OUT = ROOT / "WhatIf_Complete_Extraction" / "04_FIGURES_AND_DIAGRAMS"
FIG = OUT / "figures"
FIG.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
rows = []
backgrounds = []
for page_no, page in enumerate(doc, 1):
    figure_no = 0
    items = page.get_images(full=True)
    primary_scan_xref = max(items, key=lambda item: item[2] * item[3])[0]
    for item in items:
        xref, _, width, height = item[:4]
        rects = page.get_image_rects(xref)
        page_filling = any(abs(r.x0 - page.rect.x0) < 1 and
                           abs(r.y0 - page.rect.y0) < 1 and
                           abs(r.x1 - page.rect.x1) < 1 and
                           abs(r.y1 - page.rect.y1) < 1 for r in rects)
        if xref == primary_scan_xref and (page_filling or len(items) == 1):
            backgrounds.append({"pdf_page": page_no, "xref": xref,
                                "width_px": width, "height_px": height})
            continue
        figure_no += 1
        data = doc.extract_image(xref)
        name = f"page_{page_no:03d}_image_{figure_no:02d}.{data['ext']}"
        target = FIG / name
        target.write_bytes(data["image"])
        rows.append({
            "figure_id": f"FIG-{len(rows)+1:04d}",
            "pdf_page": page_no,
            "page_image_number": figure_no,
            "filename": name,
            "relative_path": f"figures/{name}",
            "xref": xref,
            "width_px": data["width"],
            "height_px": data["height"],
            "format": data["ext"],
            "sha256": hashlib.sha256(data["image"]).hexdigest(),
            "page_rects_pt": json.dumps([[round(v, 2) for v in r] for r in rects]),
        })

with (OUT / "figure_index.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
(OUT / "image_extraction_manifest.json").write_text(json.dumps({
    "source_pdf": str(PDF),
    "source_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
    "pdf_pages": len(doc),
    "full_page_scan_objects": len(backgrounds),
    "extracted_embedded_images": len(rows),
    "pages_with_images": len({r["pdf_page"] for r in rows}),
    "full_page_scans": backgrounds,
}, indent=2), encoding="utf-8")
print(f"Extracted {len(rows)} images from {len({r['pdf_page'] for r in rows})} pages; {len(backgrounds)} page scans retained in PDF")
