#!/usr/bin/env python3
"""Surgically update retained Decode Your Heart report with recovered evidence."""

from pathlib import Path
import json
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Forensic_Report.docx"
REG = json.loads((PATH.parent / "Decode_Your_Heart_Video_Evidence_Register.json").read_text())
CHK = json.loads((PATH.parent / "Decode_Your_Heart_Research_Checkpoint.json").read_text())

doc = Document(PATH)

replacements = {
    "Own-channel thumbnail visuals were not inspected": "All 56 retained own-channel thumbnails were recovered and visually inspected on 27 September 2026",
    "No first-party YouTube Studio analytics were provided": "Authorized YouTube Studio Advanced Mode exports were obtained on 27 September 2026 for lifetime, last 90 days, last 28 days, and lifetime traffic sources",
    "The Google Trends dynamic interface was not accessible": "Official Google Trends CSV exports were recovered through the dynamic interface on 27 September 2026",
}
for p in doc.paragraphs:
    original = p.text
    for old, new in replacements.items():
        if old in original:
            for run in p.runs:
                run.text = ""
            p.add_run(original.replace(old, new))
            break

# Idempotent: drop any prior section 18 (and its leading page break) before re-appending.
body = doc.element.body
start = next((p._p for p in doc.paragraphs if p.text.startswith("18 Evidence Recovery Update")), None)
if start is not None:
    prev = start.getprevious()
    if prev is not None and prev.tag.endswith("}p") and "w:br" in prev.xml and not "".join(prev.itertext()).strip():
        start = prev
    for el in list(body)[list(body).index(start):]:
        if not el.tag.endswith("}sectPr"):
            body.remove(el)

stale_cells = {
    "56 own thumbnail URLs exist, but image bytes were not available for a reliable visual inspection in this pass.": "All 56 own thumbnail images were recovered and visually inspected (see section 18.2).",
    "Word-count/title-form patterns are inconsistent; thumbnail visuals unavailable.": "Word-count/title-form patterns are inconsistent; thumbnail visuals recovered (section 18.2).",
    "Private satisfaction/retention metrics missing.": "Retention exports recovered for all 56 videos (46 with curves); satisfaction metrics not exported.",
    "Google Trends unavailable; traffic sources missing.": "Google Trends CSVs and lifetime traffic sources recovered (section 18).",
    "Own thumbnail URLs exist but image bytes were not available for visual audit; CTR absent.": "Own thumbnails recovered and inspected; lifetime CTR 3.0% from Studio export.",
}
for container in [doc] + [c for t in doc.tables for r in t.rows for c in r.cells]:
    for p in container.paragraphs:
        if p.text in stale_cells:
            new_text = stale_cells[p.text]
            for run in p.runs[1:]:
                run.text = ""
            p.runs[0].text = new_text

doc.add_page_break()
doc.add_heading("18 Evidence Recovery Update", level=1)
doc.add_paragraph(
    "This update closes the repository, thumbnail, public-catalog, Google Trends, and bulk first-party analytics gaps that were recoverable on 27 September 2026. It keeps the 25 September acquisition snapshot separate from the 27 September public observation. It does not claim a visual video audit from transcript or thumbnail evidence."
)

doc.add_heading("18.1 Repository and catalog reconciliation", level=2)
t = doc.add_table(rows=1, cols=3)
t.style = "Table Grid"
for cell, value in zip(t.rows[0].cells, ["Evidence", "Verified result", "Provenance"]):
    cell.text = value
for row in [
    ("Canonical channel", "UCQIzqH7QZ9viBYpOFqgSXMg", "Channel registry and live public channel"),
    ("Retained DS-000032", "56 videos: 27 regular, 29 Shorts", "Raw dataset and manifest; observed 25 September 2026"),
    ("Descriptions", "56 actual descriptions", "Raw dataset text fields"),
    ("Transcripts", "56 original transcript files", "Apify transcript package"),
    ("Current public catalog", "56 videos; no newly identified IDs", "Direct public channel observation; 27 September 2026"),
    ("Subscriber observation", "31 in retained acquisition; 33 in current public/Studio view", "Separate observation dates retained"),
]:
    cells = t.add_row().cells
    for c, value in zip(cells, row): c.text = value

doc.add_heading("18.2 Thumbnail forensics", level=2)
doc.add_paragraph(
    "All 56 retained thumbnail URLs were resolved to image files, bound to the Video ID in each source URL, hashed, dimension-checked, and visually inspected. Long-form packaging usually places Dr. Rehan in scrubs or a white coat beside a large symptom, test, or question. Dark blue or black backgrounds with white, yellow, and red emphasis create strong contrast and a clear authority cue. The repeated doctor-plus-bold-text template improves consistency but reduces differentiation between topics. Many Shorts use vertical in-video frames inside a 16:9 crop; captions and side bars reduce mobile-scale clarity. Full per-video visible text, composition, hierarchy, audience, title relationship, and comparison notes are recorded in the workbook and JSON register."
)
doc.add_paragraph(
    "Quality exceptions include sentence-length frame captions, tiny secondary labels, and the visible misspelling ‘INTIOXIDANTS’ on hUSVbcHVeVw. These are observed image facts. Their effect on performance remains an interpretation because no controlled thumbnail experiment was run."
)

doc.add_heading("18.3 First-party YouTube Studio evidence", level=2)
t = doc.add_table(rows=1, cols=6)
t.style = "Table Grid"
for cell, value in zip(t.rows[0].cells, ["Period", "Views", "Watch hours", "Subscribers", "Impressions", "CTR"]): cell.text = value
for row in [
    ("Lifetime", "8,366", "45.6", "+33", "36,159", "3.0%"),
    ("Last 90 days", "2,507", "22.7", "+10", "18,579", "3.0%"),
    ("Last 28 days", "1,158", "8.0", "+4", "4,360", "3.2%"),
]:
    cells=t.add_row().cells
    for c,value in zip(cells,row): c.text=value
doc.add_paragraph(
    "Lifetime traffic sources show 5,355 Shorts-feed views, 1,175 YouTube Search views, 1,031 Suggested-video views, and 405 Browse views. Search supplied 11,245 recorded thumbnail impressions at 2.71% CTR; Suggested supplied 19,841 at 2.90%; Browse supplied 4,028 at 3.28%. These figures support a discovery-volume constraint, but they also show that packaging response varies by source and video. Channel-wide CTR alone cannot identify one universal cause."
)
doc.add_paragraph(
    "The strongest exported long-form examples include CZ3gAUzdTAg at 367 lifetime views, 5.71 watch hours, 5,737 impressions and 3.70% CTR; EB3_A2b4a6o at 158 views, 4.3 watch hours, 3,703 impressions and 1.8% CTR; and BCNWQ3uuSuE at 145 views, 2.8 watch hours, 1,730 impressions, 4.2% CTR and two subscribers gained. These examples contradict any diagnosis that treats exposure, click response, or viewing response as a single channel-wide constant."
)

doc.add_heading("18.4 Google Trends evidence", level=2)
doc.add_paragraph(
    "Three official CSV exports used United States geography, YouTube Search, all categories, and a five-year range. Within the broad comparison, mean normalized scores were 34.94 for blood pressure, 15.05 for cholesterol, 2.49 for heart health, 1.71 for the ambiguous ‘Lp a’ string, and 0.03 for heart failure symptoms. Within the GLP-1 comparison, Ozempic averaged 31.45, semaglutide 7.71, and GLP-1 2.99. A separate niche comparison included walking exercise seniors, chair stand test, coffee blood pressure, and lipoprotein a. Scores are comparison-normalized, not absolute search volume."
)
doc.add_paragraph(
    "The Ozempic series contradicts a simple ‘no public demand’ explanation for weak early Ozempic long-form results. It does not prove that demand reached this channel, that the selected audience saw the videos, or that publication timing caused views. Those questions require query, source, and retention evidence."
)

doc.add_heading("18.5 Updated growth diagnosis", level=2)
for finding in CHK["diagnosis"]:
    p=doc.add_paragraph(style="List Bullet")
    p.add_run(finding["finding"] + ". ").bold=True
    p.add_run(finding["metrics"] + ". Counterevidence: " + finding["counterexample"] + ". Confidence: " + finding["confidence"] + ".")

doc.add_heading("18.6 Evidence completeness and remaining limits", level=2)
doc.add_paragraph(
    "The machine-readable register contains one record for every canonical Video ID and tracks metadata, description, transcript, thumbnail URL, actual image, completed thumbnail inspection, watch-page status, video-review status, editing observations, topic-level Trends evidence, competitor comparison, Studio row coverage, retention, and remaining action independently."
)
t = doc.add_table(rows=1, cols=3)
t.style="Table Grid"
for cell,value in zip(t.rows[0].cells,["Evidence category","Coverage","Status"]): cell.text=value
for row in [
    ("Metadata / descriptions / transcripts", "56 / 56 / 56", "Complete"),
    ("Thumbnail URLs / images / inspections", "56 / 56 / 56", "Complete"),
    ("Current catalog", "56 IDs; zero new", "Complete at observation date"),
    ("Google Trends", "Three official exports; 12 series", "Complete at topic level"),
    ("Studio bulk analytics", "Lifetime, 90d, 28d, traffic source", "Complete for exported metrics"),
    ("Actual playback and editing", "; ".join(f"{k} {v}" for k, v in REG["counts"]["investigation_status"].items() if v), "Status definitions in evidence register"),
    ("Individual retention curves", "Not exported", "Private evidence still required"),
    ("Returning viewers / cross-format overlap / queries / geography / device", "Not exported", "Private evidence still required"),
]:
    cells=t.add_row().cells
    for c,value in zip(cells,row): c.text=value
doc.add_paragraph(
    "No original raw evidence was modified. Recovered public images and official CSV/ZIP exports are stored as dated acquisition outputs. Playback and editing conclusions remain open where no real video review occurred."
)

for table in doc.tables:
    for row_index, row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(8.5)
                    if row_index == 0:
                        run.bold = True
                        run.font.color.rgb = RGBColor(255,255,255)
            if row_index == 0:
                tcPr=cell._tc.get_or_add_tcPr()
                from docx.oxml import OxmlElement
                from docx.oxml.ns import qn
                shd=OxmlElement("w:shd"); shd.set(qn("w:fill"),"1F4E78"); tcPr.append(shd)

doc.save(PATH)
