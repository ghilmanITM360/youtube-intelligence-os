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
    "Channel-level: traffic-source detail (Browse, Suggested, Search, Shorts feed, External), YouTube search terms, geography, language/subtitles, device, unique viewers, new/casual/regular/returning viewers, and viewers-across-formats.": "Channel-level: traffic sources, YouTube search terms, Suggested sources, geography, device, age/gender and 28-day new/casual/regular viewers were exported on 27-28 September 2026 (section 18.3a). Still unavailable: language/subtitles, viewers-across-formats and per-video source drill-downs.",
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

SUP = CHK["studio_supplementary_2026_09_28"]
REC = CHK["studio_live_observation"]["browser_vs_export_reconciliation"]
doc.add_heading("18.3a Studio reports recovered on 28 September 2026", level=2)
doc.add_paragraph(
    "Seven further Studio CSV exports were archived byte-for-byte (SHA-256 of each archive equals its original download) in the private first-party folder, with a provenance manifest. "
    f"The extended lifetime content table covers all 56 canonical videos with no duplicate IDs and one noncanonical community Post row, which is excluded. The nine rows missing from the earlier browser observation "
    f"({', '.join(REC['previously_missing_now_exported'])}) are present. All {REC['browser_observed_rows']} browser-observed rows agree with the export within one-decimal display rounding, and views equal the 27 September lifetime export. Browser observations and exported values are kept as separate evidence fields."
)
a = SUP["audience_28_day"]; sr = SUP["search_terms"]; sg = SUP["suggested_sources"]; ages = SUP["age_views_percent"]
geo = ", ".join(f"{g['country']} {g['share_percent']}%" for g in SUP["geography"]["disclosed"][:4])
t = doc.add_table(rows=1, cols=3)
t.style = "Table Grid"
for cell, value in zip(t.rows[0].cells, ["Report", "Verified result", "Limit"]): cell.text = value
for row in [
    ("New / casual / regular viewers (28 days)", f"Monthly audience {a['monthly_audience_latest']}: {a['new_viewers_latest']} new, {a['casual_viewers_latest']} casual, {a['regular_viewers_latest']} regular (regular max {a['regular_viewers_max_in_period']} in the window); subscribers {a['subscribers_start']} to {a['subscribers_latest']}", f"Window {a['period']} only; Studio estimate"),
    ("YouTube Search terms", f"{sr['total_search_views']:,} views, {sr['total_search_impressions']:,} impressions, CTR {sr['search_ctr_percent']}%; {sr['disclosed_terms']} disclosed terms carry {sr['views_in_disclosed_terms']} views, maximum {sr['max_views_single_term']} per term", "Long tail below disclosure; per-term CTR not interpretable"),
    ("Suggested sources", f"{sg['total_suggested_views']:,} views, {sg['total_suggested_impressions']:,} impressions, CTR {sg['suggested_ctr_percent']}%; {sg['external_sources']} external source videos gave {sg['external_views']} views, own-channel videos {sg['own_channel_views']}", "Channel-level; top sources only"),
    ("Geography", f"Disclosed: {geo}; {SUP['geography']['undisclosed_views']:,} views undisclosed", "Most views below the disclosure threshold"),
    ("Device", "; ".join(f"{d['device']} {d['views']:,} views, AVD {d['average_view_duration']}" for d in SUP["device"]), "Lifetime"),
    ("Age (share of views)", "; ".join(f"{k} {v}%" for k, v in ages.items()), "Signed-in viewers only; shares, not counts"),
]:
    cells = t.add_row().cells
    for c, value in zip(cells, row): c.text = value
doc.add_paragraph(
    "Interpretation (corrected in section 19): the channel is built for viewers over 60, but signed-in age data put most views at ages 25 to 54, and India and Pakistan lead the 32.8% of views that have a disclosed country; the other 67% is undisclosed and is not extrapolated. "
    "Zero regular viewers is structurally expected: YouTube counts a regular viewer only after monthly viewing in more than 6 of the past 12 months, and this channel began in February 2026 with an almost inactive April. These are channel-level reports; they cannot show which video attracted which viewer, and they do not show individual viewers moving between Shorts and long-form."
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

doc.add_heading("18.5a Matched playback comparisons", level=2)
c = REG["counts"]
doc.add_paragraph(
    f"{c['investigation_status']['RETENTION_ANALYZED']} videos have numeric playback anchors read against their exported retention curve. "
    f"{c['playback_reported_full']} come from the previous session's reported full playback (its completion evidence is a text record only). "
    f"{c['playback_seek_sampled']} were seek-sampled on 28 September 2026: muted, with frames viewed and on-screen captions read at each retention event, "
    "so they are not continuous playback and audio was not heard. "
    f"{c['continuous_signal_passes']} of the seek-sampled videos were also played continuously at 2x to the end through a level meter and hard-cut counter; "
    "that measures loudness, silence and cuts, not what was said or whether music played. "
    f"Verified complete audiovisual editing reviews: {c['complete_audiovisual_audits_verified']}. "
    "Each comparison below is associative; samples are small and distribution is uncontrolled."
)
for m in REG["matched_comparisons"]:
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(f"{m['pair']} ({m['stronger_id']} vs {m['comparison_id']}). ").bold = True
    p.add_run(m["evidence"] + " " + m["interpretation"])
doc.add_paragraph(
    "Recurring observations across these pairs (interpretation, not proof): openings that begin with a textbook definition or a statistic "
    "(YVjbjcVo1is, TPVOIfcJl-k) or that pause for a credential introduction (5oPzZjfNgII at 0:27, VrbLuTNi0qE at 0:31) coincide with visible "
    "curve drops, while openings that qualify the viewer or pose a test they can perform (fArHBQo6Ggw, t1j-p9pkw3Y) hold more viewers at 30 seconds. "
    "iltS1TPt4jo re-edits the YVjbjcVo1is footage with an illustrated cold open; it stopped slightly more swipes but held far fewer viewers, and its "
    "uploaded captions show raw timecodes such as (0:00) to viewers, as do TPVOIfcJl-k's. Every retained retention export reports organic traffic only."
)
doc.add_paragraph(
    "Batch 4 adds a counterexample to pace-driven advice: NznebmgFwXI is almost a single take (2 hard cuts in 151 s) yet kept 87.1% of viewers at 3 s, "
    "while the fast-cut KPYHy7MDmLM (33 cuts in 117 s) kept 57.89%; the stronger video opens on a concrete self-check symptom, the weaker on a generic warning "
    "under three text layers. The ankle/calf pair is not interpretable (18 versus 805 views). A scan of all 56 caption transcripts found raw timecodes in 10 "
    "and emoji or heading lines in 2 more; affected videos show no consistent retention direction, so this is a quality fix rather than a growth lever. "
    "Transcript overlap shows the coffee Shorts are excerpts of the long-form fAwh2svMARM; the same footage produced both the strongest and a weaker coffee Short."
)

doc.add_heading("18.5b Earlier findings re-tested against the full dataset", level=2)
for head, body in [
    ("Slow or generic openings", "Supported as an association in 9 of 22 matched pairs (for example qbwCkH_GqhU vs TPVOIfcJl-k, t1j-p9pkw3Y vs VrbLuTNi0qE, 78JR_U-6HfQ vs 3dRcNqiLHgY). Batch 7 adds four long-form curves (tf7f4RhQwtc, xI-KdZ96xcI, qC8BKb8Fh5Q, Nf9pCrPYWyQ) where the steepest loss falls during setup before the promised item. Contradiction: r9ZyUWyY4Lc and HzFdyjyEFTY have near-identical early curves despite different openings. Status: supported hypothesis, not a cause."),
    ("Fast versus slow editing", "Not supported as a rule. NznebmgFwXI (2 cuts) outheld KPYHy7MDmLM (33 cuts) early; 78JR_U-6HfQ (60 cuts) outheld 3dRcNqiLHgY, but also had a more specific opening. Pace and opening specificity are confounded in every pair."),
    ("Reused footage", "Verified: the coffee Shorts are excerpts of fAwh2svMARM, and YVjbjcVo1is and iltS1TPt4jo share footage. The same source produced both stronger and weaker Shorts, so reuse is neutral in this sample."),
    ("Raw timecodes in captions", "Verified in 10 of 56 retained caption tracks, including phSq6PkPtIg (impossible 0:21 and 0:27 markers in a 14.86-second video). No consistent retention direction. Fix as a quality defect, not as a growth lever."),
    ("Title/content mismatch", "Verified for 7MXBh2hjfto (title promises an appetite-suppressant comparison) and hUSVbcHVeVw (title says reverse, captions say support); RD7ugxaBHSQ shifts from calf to push-ups mid-video. sC_0XjL2z_Y's title has changed since acquisition, so its packaging cannot be evaluated historically."),
    ("Black video sections", "Verified only in UeGxF8-hb2s (black and near-silent 0:50 to 1:28). The suspected black tail in Uq3T8YZgyTw was checked and is not present: it ends on a white engagement card. No other black section was found at sampled anchors."),
    ("Direct viewer-focused hooks", "Openings that name a test or symptom the viewer can check (t1j-p9pkw3Y, fArHBQo6Ggw, NznebmgFwXI, jxoMnTrVziA) coincide with better early holding where curves exist; high-CTR titles (8JdBlF-ragM 4.89%, 5oPzZjfNgII 4.72%, r9ZyUWyY4Lc 4.64%) pose a concrete question. Sample sizes of 10 to 400 views keep confidence moderate."),
]:
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(head + ". ").bold = True
    p.add_run(body)

doc.add_heading("18.6 Recommendations and 30/60/90-day plan", level=2)
doc.add_paragraph("Superseded by section 19 (final forensic validation, 28 September 2026). The earlier plan targeted regular viewers above zero, which YouTube's definition makes unattainable within the plan window, and treated a Short's CTR as packaging evidence; both are corrected in section 19.")

doc.add_heading("18.7 Evidence completeness and remaining limits", level=2)
doc.add_paragraph(
    "The machine-readable register contains one record for every canonical Video ID and tracks metadata, description, transcript, thumbnail URL, actual image, completed thumbnail inspection, watch-page status, video-review status, editing observations, topic-level Trends evidence, competitor comparison, Studio row coverage, retention, and remaining action independently."
)
c = REG["counts"]
t = doc.add_table(rows=1, cols=3)
t.style="Table Grid"
for cell,value in zip(t.rows[0].cells,["Evidence category","Coverage","Status"]): cell.text=value
for row in [
    ("Metadata / descriptions / transcripts", "56 / 56 / 56", "Complete"),
    ("Thumbnail URLs / images / inspections", "56 / 56 / 56", "Complete"),
    ("Current catalog", "56 IDs; zero new", "Complete at observation date"),
    ("Google Trends", "Three official exports; 12 series", "Complete at topic level"),
    ("Studio bulk analytics", "Lifetime, 90d, 28d, traffic source", "Complete for exported metrics"),
    ("Studio extended per-video rows", f"{REG['counts']['studio_extended_rows_observed']} of 56 from the 28 September CSV export", "Complete; reconciled with the browser observation"),
    ("Actual playback and editing", "; ".join(f"{k} {v}" for k, v in REG["counts"]["investigation_status"].items() if v), "Status definitions in evidence register"),
    ("Individual retention curves", f"{c['retention_curves']} curves in {c['retention_exports']} exports", "Exported; 10 disclosed no rows"),
    ("New vs returning viewers", f"{REG['counts']['retention_new_vs_returning_split']} retention-by-segment splits; channel 28-day new/casual/regular counts", "Channel-level counts exported; per-video counts unavailable"),
    ("Search terms / suggested sources / geography / device / age", "Channel-level exports, 28 September", "Complete at channel level; per-video drill-downs not exported"),
    ("Cross-format viewer overlap", "Not exported", "Unavailable"),
    ("Priority reviews (full-length storyboard frames plus transcript)", f"{c['priority_reviews']} videos", "Section 19.2; audio not heard"),
    ("Medical claim review", f"{c['medical_claim_reviews']} claims in {c['videos_with_medical_claim_review']} videos; {c['medical_claims_requiring_action']} need action", "Section 19.3"),
    ("Spoken audio heard / complete audiovisual audit", "0 / 0 of 56", "Not possible in this environment"),
]:
    cells=t.add_row().cells
    for c,value in zip(cells,row): c.text=value
doc.add_paragraph(
    "No original raw evidence was modified. Recovered public images and official CSV/ZIP exports are stored as dated acquisition outputs. Every video now has at least a seek-sampled or reported playback record, but none has a verified heard, continuous audiovisual audit, and seek-sampled records are not claims of continuous playback."
)

FV = CHK["final_validation_2026_09_28"]


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    for cell, value in zip(t.rows[0].cells, headers):
        cell.text = value
    for row in rows:
        for cell, value in zip(t.add_row().cells, row):
            cell.text = "" if value is None else str(value)
    return t


def bullet(head, body):
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(head + ". ").bold = True
    p.add_run(body)


doc.add_page_break()
doc.add_heading("19 Final Forensic Validation and Actionable Diagnosis", level=1)
doc.add_paragraph(
    "This section supersedes any earlier statement it contradicts. It re-audits every active conclusion against the original private exports and YouTube's "
    "official definitions, adds 12 priority reviews and 15 medical claim reviews, and replaces the earlier plan. Every performance explanation below is an "
    "association from small cohorts (tens to a few hundred viewers per video), not a demonstrated cause. " + FV["residual_uncertainty"]
)

doc.add_heading("19.1 What the measurements establish", level=2)
for head, body in [
    ("Scale", "8,366 lifetime views, 36,159 thumbnail impressions, 45.6 watch hours and 33 subscribers across 56 videos published from 3 February to 25 September 2026."),
    ("Format mix", "The Shorts feed supplied 5,355 views (64%). Long-form reach came from Search (1,175 views, CTR 2.71%), Suggested (1,031, CTR 2.9%) and Browse (405, CTR 3.28%). Search overtook Suggested in August and September."),
    ("Discovery shape", "114 disclosed search terms carry 170 views (no term above 7); 472 disclosed Suggested source videos, of which the channel's own videos supplied 70 views (6.8%)."),
    ("Audience", "Latest 28 days: 505 monthly viewers, 495 new, 10 casual, 0 regular. Geography is disclosed for only 32.8% of views; within that disclosed third, India 48.7%, Pakistan 15.0%, US 11.9%, UK 11.1%."),
    ("Video-level variation", "Mature long-form CTR spans roughly 2.5-4.9% (EB3_A2b4a6o 1.81% is the outlier); 30-second retention spans 31-67%. Variation is real; single causes are not identifiable."),
]:
    bullet(head, body)

doc.add_heading("19.2 Corrected claim audit", level=2)
table(["Claim", "Period / sample", "Confounders and counterexamples", "Corrected interpretation", "Status"],
      [(c["id"] + ". " + c["previous_claim"], c["period"] + "; " + c["sample_size"], c["confounders"] + " Counterexample: " + c["counterexamples"], c["corrected_interpretation"], c["status"]) for c in FV["claim_audit"]])
doc.add_paragraph("YouTube definitions used (" + FV["youtube_definitions"]["source"] + "): casual = " + FV["youtube_definitions"]["casual_viewers"] + " Regular = " + FV["youtube_definitions"]["regular_viewers"])

doc.add_heading("19.3 Priority audiovisual reviews", level=2)
m = FV["priority_review_method"]
doc.add_paragraph("Method. Visual: " + m["visual"] + " Speech: " + m["speech"] + " Audio: " + m["audio"])
recs = {r["video_id"]: r for r in REG["records"]}
for vid in FV["priority_review_video_ids"]:
    pr = recs[vid]["priority_review_2026_09_28"]
    doc.add_heading(f"{vid}: {recs[vid]['title_at_acquisition'][:80]}", level=3)
    doc.add_paragraph(f"Why selected: {pr['why_selected']}. Coverage: {pr['coverage']}.")
    doc.add_paragraph("Timestamped observations: " + "; ".join(pr["timestamps"]) + ".")
    doc.add_paragraph(f"Retention link: {pr['retention_link']} Title promise: {pr['title_promise']} Pacing and visuals: {pr['pacing_visuals']} Medical: {pr['medical']}")
    doc.add_paragraph("Finding: " + pr["finding"])
doc.add_paragraph("Sufficiency: the 12 cases cover the highest-reach, strongest, weakest and defect cases across cardiology, broader senior health, long-form and Shorts. They are sufficient for the corrections and experiments below; they do not justify another full 56-video playback campaign, because the remaining uncertainty is about audience and distribution data, not unseen footage.")

doc.add_heading("19.4 Medical claim review", level=2)
table(["Video", "Claim", "Verdict", "Evidence", "Suggested wording", "Priority"],
      [(c["video_id"], c["claim"], c["verdict"], c["evidence"] + ". " + c["analysis"], c["alternative_wording"] or "No change needed", c["priority"]) for c in FV["medical_claim_reviews"]])
doc.add_paragraph("References: " + " ".join(f"[{k}] {v}" for k, v in FV["medical_references"].items()))
doc.add_paragraph("Published content was not changed; wording is proposed for the channel owner's review.")

doc.add_heading("19.5 Root-cause investigation matrix", level=2)
table(["Constraint", "Observation / scope", "Evidence", "Counterexamples / confounders", "Interpretation / confidence", "Practical response"],
      [(r["constraint"], r["observation"] + " Scope: " + r["scope"], r["supporting_evidence"], r["counterexamples"] + " Confounders: " + r["confounders"], r["interpretation"] + " Confidence: " + r["confidence"], r["practical_response"]) for r in FV["root_cause_matrix"]])
doc.add_paragraph("No overall channel score is assigned. Quality defects are local to specific videos; packaging weakness is local to specific videos; no constraint is shown to be channel-wide and causal.")

doc.add_heading("19.6 Suspected problems not supported by the data", level=2)
for item in FV["not_supported_by_data"]:
    doc.add_paragraph(item, style="List Bullet")

doc.add_heading("19.7 Knowledge datasets applied", level=2)
table(["Source", "Passage", "Applied to", "Verdict", "Contradiction"],
      [(k["source"], k["passage"], k["applied_to"], k["verdict"], k["contradiction"] or "None found") for k in FV["knowledge_applications"]])

doc.add_heading("19.8 Immediate quality corrections", level=2)
table(["ID", "Video", "Action", "Evidence"], [(q["id"], q["video_id"], q["action"], q["evidence"]) for q in FV["immediate_corrections"]])

doc.add_heading("19.9 Controlled experiments", level=2)
table(["ID", "Experiment", "Eligible videos", "Evidence basis", "Window", "Metrics", "Interpretation rule"],
      [(e["id"], e["name"] + ": " + e["purpose"], "; ".join(e["eligible_videos"]), e["evidence_basis"], e["window"], e["metrics"], e["interpretation"]) for e in FV["experiments"]])
doc.add_paragraph("Shorts are judged on stayed-to-watch and engaged views; long-form on Test & Compare verdicts, impressions CTR from the same period, and 30/60-second retention. No view-count target is set and no growth is promised.")

doc.add_heading("19.10 Future research", level=2)
table(["ID", "Question", "Requires"], [(r["id"], r["question"], r["requires"]) for r in FV["future_research"]])

doc.add_heading("19.11 30/60/90-day plan", level=2)
table(["Window", "Actions", "Useful evidence"], [(p["window"], p["actions"], p["success_evidence"]) for p in FV["plan_30_60_90"]])

doc.add_heading("19.12 Answers to the acceptance questions", level=2)
for head, body in [
    ("What the measurements establish", "A small, Shorts-heavy channel whose long-form reach is fragmented across many search terms and external Suggested sources, with a new-viewer-dominated audience and real video-level variation in click and retention response."),
    ("What separates stronger and weaker videos", "Associations only: a specific question answered early (BCNWQ3uuSuE vs SBrMW71O69U), concrete body-signal or test framing, and exact promise delivery. Editing pace, topic label and production polish do not separate them."),
    ("Not supported", "See 19.6: regular-viewer failure, returning-viewer advantage, South Asian majority, Shorts CTR, fast cutting, caption-defect effects, cardiology under-performance, algorithm preference."),
    ("Needs immediate attention", "HzFdyjyEFTY's instruction to avoid aspirin without clinician advice; hUSVbcHVeVw's 'reverse' title; 7MXBh2hjfto's mismatched title; 8JdBlF-ragM's speculative side-effect claim; UeGxF8-hb2s's black tail; caption defects."),
    ("Still hypotheses", "Audience development, audience alignment with the 'After 60' target, and any packaging or opening rule until E1-E3 produce verdicts."),
    ("Next experiments and what counts", "E1 Test & Compare verdicts; E2 30-second retention differences above ~15 points; E3 group-median stayed-to-watch; E4 own-channel Suggested share above the 6.8% baseline."),
]:
    bullet(head, body)

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
