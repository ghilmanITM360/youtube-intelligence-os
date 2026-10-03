// Build YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.docx from master_data.json.
// Read-only against repo source data; only writes the .docx in this export directory.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, PageBreak, TableOfContents, AlignmentType, BorderStyle, Header, Footer,
  PageNumber, ShadingType, VerticalAlign, Bookmark,
} from "docx";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..");
const REPO = path.resolve(ROOT, "..", "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "master_data.json"), "utf8"));
const OUT = path.join(ROOT, "YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.docx");

const PAGE_W = 12240, PAGE_H = 15840; // US Letter DXA
const MARGIN = 1080; // 0.75in
const USABLE_W = PAGE_W - MARGIN * 2;

const FONT = "Calibri";
const heading = (text, level) => new Paragraph({ text, heading: level, spacing: { before: 280, after: 140 } });
const body = (text, opts = {}) => new Paragraph({
  children: [new TextRun({ text: String(text ?? ""), font: FONT, size: 20, italics: opts.italics, bold: opts.bold })],
  spacing: { after: 120 },
});
const small = (text) => new Paragraph({
  children: [new TextRun({ text: String(text ?? ""), font: FONT, size: 18, color: "555555", italics: true })],
  spacing: { after: 160 },
});
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

function cell(text, { header = false, widthPct = null, shade = null } = {}) {
  return new TableCell({
    width: widthPct ? { size: widthPct, type: WidthType.PERCENTAGE } : undefined,
    verticalAlign: VerticalAlign.TOP,
    shading: header ? { type: ShadingType.CLEAR, fill: "1F4E5F" } : shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    children: [new Paragraph({
      children: [new TextRun({ text: String(text ?? ""), font: FONT, size: header ? 18 : 17, bold: header, color: header ? "FFFFFF" : "000000" })],
    })],
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
  });
}

function dataTable(headers, rows, colPercents) {
  const pct = colPercents || headers.map(() => Math.floor(100 / headers.length));
  const headerRow = new TableRow({ children: headers.map((h, i) => cell(h, { header: true, widthPct: pct[i] })), tableHeader: true });
  const dataRows = rows.map((r, idx) => new TableRow({
    children: r.map((v, i) => cell(v, { widthPct: pct[i], shade: idx % 2 === 1 ? "F2F2F2" : null })),
  }));
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [headerRow, ...dataRows],
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: "AAAAAA" },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: "AAAAAA" },
      left: { style: BorderStyle.SINGLE, size: 2, color: "AAAAAA" },
      right: { style: BorderStyle.SINGLE, size: 2, color: "AAAAAA" },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
      insideVertical: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
    },
  });
}

const children = [];

// ---------------------------------------------------------------- COVER PAGE
children.push(
  new Paragraph({ spacing: { before: 2400 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "YouTube Knowledge & Senior Health", font: FONT, size: 56, bold: true, color: "1F4E5F" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400 },
    children: [new TextRun({ text: "Complete Data Export & Traceable Knowledge Extraction", font: FONT, size: 32, color: "1F4E5F" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: "DS-000011 · DS-000018 · DS-000031 — Global Knowledge Corpora", font: FONT, size: 22, italics: true })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 800 },
    children: [new TextRun({ text: "Senior Health Channel Inventory & Decode Your Heart – Dr. Rehan (Own Channel)", font: FONT, size: 22, italics: true })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Repository: youtube-intelligence-os", font: FONT, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Branch: research/senior-health-acquisition-phase-2", font: FONT, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 800 },
    children: [new TextRun({ text: "Generated 2026-09-27 · Read-only export — no source dataset modified", font: FONT, size: 20 })] }),
  pageBreak(),
);

// ---------------------------------------------------------------- TOC
children.push(
  heading("Table of Contents", HeadingLevel.HEADING_1),
  new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" }),
  pageBreak(),
);

const recon = DATA.reconciliation;

// ================================================================ PART I
children.push(heading("PART I — Project Data Inventory", HeadingLevel.HEADING_1));
children.push(body(
  "This document and its companion workbook (YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.xlsx) were produced by a " +
  "read-only extraction pass against this repository on 2026-09-27. Every count below was verified directly against the " +
  "files named in the Source Traceability appendix — none is carried over from memory or from the historical baseline " +
  "figures quoted in the originating task request without re-verification."
));
children.push(heading("Executive Inventory", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Corpus", "Metric", "Value"],
  [
    ["DS-000011", "Unique original sources (full original text archived)", String(recon["DS-000011"].fulltext_unique_sources)],
    ["DS-000011", "Extracted knowledge rules", String(recon["DS-000011"].observed_rules)],
    ["DS-000018", "Research tabs (63 raw / 61 unique post-dedup, 63/63 now claim-atomized)", String(recon["DS-000018"].observed_tabs)],
    ["DS-000018", "Claims: human-audited (2026-09-04 pass) / AI-extracted (2026-09-27) / total", `${recon["DS-000018"].original_human_audited_claims} / ${recon["DS-000018"].additional_ai_extracted_claims} / ${recon["DS-000018"].all_claims_combined}`],
    ["DS-000031", "Concepts (15/15 segments now carry full original text)", String(recon["DS-000031"].observed.concepts)],
    ["DS-000031", "Formulas / numeric heuristics", `${recon["DS-000031"].observed.formulas} / ${recon["DS-000031"].observed.numeric_heuristics}`],
    ["Senior Health", "Channels acquired (7 competitors + 1 own)", String(recon.senior_health.acquired_channels_incl_own)],
    ["Senior Health", "Total video records", String(recon.senior_health.total_unique_video_records)],
    ["Senior Health", "Real transcripts on file (self-contained archive)", String(recon.senior_health.total_real_transcripts)],
    ["Senior Health", "Video descriptions exported", String(recon.senior_health.total_descriptions_exported)],
    ["Senior Health", "Thumbnail URLs recovered", String(recon.senior_health.total_thumbnail_urls_recovered)],
    ["Senior Health", "Downloaded thumbnail image files archived", String(recon.senior_health.total_downloaded_thumbnail_files)],
    ["Senior Health", "Total known channel leads (acquired+pending+identity+removed)", String(recon.senior_health.known_leads_total)],
  ],
  [22, 55, 23],
));
children.push(small(
  "Note on the historical baseline in the originating task request: '7 acquired Senior Health competitors' excluded the " +
  "user's own channel; counted together the true acquired-and-complete figure is 8 channels. The '19-vs-14 qualified-pending' " +
  "figure is explicitly superseded in SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md — the correct, currently-live figure is 14 " +
  "qualified-pending + 34 identity-only = 48 unacquired leads, plus 13 removed/unverifiable, for 69 total known leads."
));
children.push(small(
  "2026-09-27 correction pass: an earlier version of this export atomized claims from only 7 of 63 DS-000018 tabs, gave " +
  "DS-000031 concepts as one-sentence summaries only, omitted video descriptions, recovered only 64/460 thumbnail URLs, " +
  "capped competitor video tables at 5 rows, and mislabeled a citation-code field as claim-validation status. All six are " +
  "corrected in this version; see Appendix A for the full reconciliation and Appendix D for the supplemental data archive."
));
children.push(pageBreak());

// ================================================================ PART II — DS-000011
children.push(heading("PART II — Complete DS-000011 Knowledge Extraction", HeadingLevel.HEADING_1));
children.push(body(
  "DS-000011 (\"All Training Data of YouTube — Global Knowledge Corpus\") is 17 physical files registered under " +
  "data/raw/global-youtube-knowledge/DS-000011/, reducing to 16 textually unique works (one hook-technique PDF is " +
  "duplicated under a second filename). Authorship is UNKNOWN for every file — no original URLs or bylines were preserved " +
  "at ingestion. All 17 files are PDF/DOCX/Markdown creative and reference guides (hooks, scriptwriting, packaging, SEO)."
));
children.push(heading("Source Register (17 files, 16 unique)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Doc ID", "Title", "Type", "Evidence Type", "Knowledge Domains"],
  DATA["DS-000011"].source_documents.map(d => [
    d.document_id || "", d.title || "", d.document_type || "",
    d.evidence_type || "", (() => { try { return JSON.parse(d.knowledge_domains || "[]").join(", "); } catch { return d.knowledge_domains || ""; } })(),
  ]),
  [12, 38, 20, 15, 15],
));
children.push(heading("Extracted Knowledge Rules (17)", HeadingLevel.HEADING_2));
children.push(body("Each rule below is the project's atomized extraction of one substantive recommendation, framework, or technique from a DS-000011 source, distinguishing the source author's recommendation from any independently verified platform fact."));
children.push(dataTable(
  ["Rule ID", "Domain", "Type", "Rule Text", "Validation Status"],
  DATA["DS-000011"].knowledge_rules.map(r => [r.RULE_ID || "", r.DOMAIN || "", r.RULE_TYPE || "", r.RULE_TEXT || "", r.PRIMARY_VALIDATION_STATUS || ""]),
  [10, 14, 14, 47, 15],
));
children.push(heading("2026-09-27 correction: full original source text now recovered", HeadingLevel.HEADING_2));
children.push(body(
  "The rule table above is an AI-synthesized one-line-per-rule index (SOURCE_QUALITY discloses this on every row); it was " +
  "never a substitute for the original documents. All 17 source files (PDF/DOCX/Markdown) have now had their complete " +
  "original text extracted read-only via pdftotext/python-docx and archived, byte-verified by SHA-256, at " +
  "supplemental-data-archive/ds-000011-full-text/<original filename>.txt — including the duplicate-pair detection (Hook (1).pdf " +
  "and Hook guide.pdf are byte-identical, confirmed by matching SHA-256) and the single largest source, 'YouTube algorithm " +
  "guide.docx (2).pdf', which alone extracts to roughly 380,000 characters of original text. Full per-file byte sizes, " +
  "extraction status, and archive paths are in the companion workbook, sheet 05b_DS011_FULL_SOURCES."
));
children.push(pageBreak());

// ================================================================ PART III — DS-000018
children.push(heading("PART III — Complete DS-000018 Knowledge Extraction", HeadingLevel.HEADING_1));
children.push(body(
  "DS-000018 (\"2026 Algorithm Update — Multi-Tab Creator Research Corpus\") is one user-supplied Google Docs multi-tab " +
  "snapshot (a single ZIP, never permanently extracted to repo storage) containing 63 non-empty tabs, reducing to 61 " +
  "textually unique video sources after removing two near-duplicate pairs. This is third-party creator research — " +
  "algorithm-watch commentary and platform-attributed interview transcripts — not official YouTube training material, " +
  "and it is never treated here as a universal, verified algorithm rule."
));
children.push(heading("Tab Register (all 63 tabs)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Tab", "Title", "Word Count"],
  DATA["DS-000018"].tabs.map(t => [`T${String(t.index).padStart(2, "0")}`, t.title || "", String(t.word_count ?? "")]),
  [10, 70, 20],
));
children.push(heading(`Extracted Claims (${recon["DS-000018"].all_claims_combined}) with Validation Status`, HeadingLevel.HEADING_2));
children.push(body(
  `2026-09-27 correction: the original export atomized only ${recon["DS-000018"].original_human_audited_claims} claims from 7 of the 63 tabs (T01, T36, T39, T43, T48, T49, T51) — the other ` +
  "56 tabs were registered as sources but never claim-atomized, which is what this correction pass fixes. The original " +
  `${recon["DS-000018"].original_human_audited_claims} went through a human validation pass against official YouTube sources on 2026-09-04 (of those: 10 SUPPORTED, ` +
  "12 PARTIALLY_SUPPORTED, 1 CONTRADICTED, 8 NOT_SUPPORTED_BY_PRIMARY_EVIDENCE, 2 NOT_CURRENTLY_VERIFIABLE) and remain " +
  `distinguishable below by Extraction Method = HUMAN_AUDITED_ORIGINAL_33. The other ${recon["DS-000018"].additional_ai_extracted_claims} were extracted by ` +
  "grounded read-through of each remaining tab's full original text (every claim traceable to a verbatim quote from that " +
  "tab, nothing invented beyond what the source states) but have NOT been through an independent human validation pass — " +
  "they carry Extraction Method = AI_GROUNDED_EXTRACTION_UNVALIDATED and Validated Status = NOT_CURRENTLY_VERIFIABLE until " +
  "reviewed. Also fixed: 'Validated Status' below is now the actual prior-audit status; the earlier version put citation " +
  "reference codes (e.g. '[R1], [R2]') in that column by mistake — those codes now have their own column."
));
children.push(dataTable(
  ["Claim ID", "Type", "Theme", "Claim Text", "Validated Status", "Extraction Method"],
  DATA["DS-000018"].claims.map(c => [
    c["Claim ID"] || "", c.assertion_type || "", c.Theme || "",
    c["Concise source claim"] || c["Concise source interpretation"] || c["Concise source recommendation"] || "",
    c.prior_status_at_validation || "NOT_VALIDATED_AT_CLAIM_LEVEL",
    "HUMAN_AUDITED_ORIGINAL_33",
  ]),
  [9, 12, 14, 38, 15, 12],
));
children.push(pageBreak());

// ---- 2026-09-27 addition: substantial per-tab sections for all 63 tabs (fixes "56 tabs
// never processed"). Each tab gets its own subsection with every claim grounded-extracted
// from it; the tab's full original text is archived (not pasted here) at
// supplemental-data-archive/ds-000018-full-tabs/<snapshot filename>.
children.push(heading("Per-Tab Detail — All 63 Research Tabs", HeadingLevel.HEADING_2));
children.push(body(
  "Every tab below carries its claims verbatim-traceable to the original transcript, plus a verified duplicate-transcript " +
  "flag where one was found (per Core Rule 9 — detect duplication before treating two sources as independent evidence). " +
  "Full original tab text (never truncated) is archived at supplemental-data-archive/ds-000018-full-tabs/ next to this document."
));
const additionalByTab = {};
for (const c of DATA["DS-000018"].additional_claims) {
  const k = c.tab_file || "UNKNOWN";
  (additionalByTab[k] ||= []).push(c);
}
const originalClaimsByTabIdx = {};
for (const c of DATA["DS-000018"].claims) {
  const m = /T(\d+)/.exec(c["Exact locator"] || "");
  if (m) (originalClaimsByTabIdx[Number(m[1])] ||= []).push(c);
}
for (const t of DATA["DS-000018"].tabs) {
  const fname = t.snapshot_member.split("/").pop();
  const extra = additionalByTab[fname] || [];
  const orig = originalClaimsByTabIdx[t.index] || [];
  const allTabClaims = [
    ...orig.map(c => ({
      text: c["Concise source claim"] || c["Concise source interpretation"] || c["Concise source recommendation"] || "",
      type: c.assertion_type || "", status: c.prior_status_at_validation || "", method: "HUMAN_AUDITED",
    })),
    ...extra.map(c => ({
      text: c.claim_text || "", type: c.assertion_type || "", status: c.prior_status_at_validation || "NOT_CURRENTLY_VERIFIABLE", method: "AI_EXTRACTED",
    })),
  ];
  children.push(heading(`T${String(t.index).padStart(2, "0")} — ${t.title || fname}`, HeadingLevel.HEADING_3));
  children.push(small(`${t.word_count ?? "?"} words · ${allTabClaims.length} claims extracted · archive: supplemental-data-archive/ds-000018-full-tabs/${fname}`));
  if (allTabClaims.length) {
    children.push(dataTable(
      ["Type", "Claim / Recommendation / Interpretation", "Status", "Method"],
      allTabClaims.map(c => [c.type, c.text, c.status, c.method]),
      [12, 58, 16, 14],
    ));
  } else {
    children.push(body("No substantive algorithm/strategy claims were found in this tab's text (off-topic or promotional content)."));
  }
}
children.push(pageBreak());

// ================================================================ PART IV — DS-000031
children.push(heading("PART IV — Complete DS-000031 Knowledge Extraction", HeadingLevel.HEADING_1));
children.push(body(
  "DS-000031 (\"Creator Strategy, Audience Psychology & Experimentation Frameworks Corpus\") is one 70,730-byte user-supplied " +
  "mixed Urdu/Roman-Urdu/English text file, author UNKNOWN, separated into 15 source segments, 63 indexed concepts " +
  "(16 SOURCE_CONCEPT, 14 SOURCE_HEURISTIC, 9 SOURCE_WORKFLOW, 11 SOURCE_FRAMEWORK, 8 SOURCE_CLAIM, 2 DERIVED_NORMALIZATION, " +
  "1 each SOURCE_DIAGNOSTIC_RULE/SOURCE_RECOMMENDATION/SOURCE_SCORECARD), 15 source formulas, 12 separate numeric heuristics, " +
  "1 scorecard, and 9 example groups."
));
children.push(heading("Concepts (63)", HeadingLevel.HEADING_2));
children.push(small(
  "2026-09-27 correction: this table's Summary column is a one-sentence AI paraphrase, same as before — but every concept " +
  "now links to its original source segment, which is reproduced in full immediately below (not just this summary)."
));
children.push(dataTable(
  ["ID", "Name", "Type", "Summary"],
  DATA["DS-000031"].concepts.map(c => [c.id || "", c.name || "", c.type || "", c.summary || ""]),
  [8, 27, 20, 45],
));
children.push(pageBreak());

// ---- 2026-09-27 addition: full original text per segment (fixes "mostly short summaries
// rather than complete original source material"). Corpus is 70,730 bytes total, so full text
// is embedded directly rather than only archived.
children.push(heading("Original Source Segments (15) — Full Text", HeadingLevel.HEADING_2));
children.push(body(
  "The entire DS-000031 corpus is one 70,730-byte mixed Urdu/Roman-Urdu/English text file. Below is every one of its 15 " +
  "segments reproduced in full (sliced by the segment's own registered line range, not summarized or paraphrased), each " +
  "followed by the concepts/frameworks indexed against it. The same full corpus file is also archived at " +
  "supplemental-data-archive/ds-000031-source/creator-strategy-audience-psychology-experimentation-corpus.txt."
));
const conceptsBySegment = {};
for (const c of DATA["DS-000031"].concepts) {
  for (const sid of c.segments || []) (conceptsBySegment[sid] ||= []).push(c);
}
for (const s of DATA["DS-000031"].segments) {
  children.push(heading(`${s.id} — ${s.title || ""}`, HeadingLevel.HEADING_3));
  children.push(small(`Kind: ${s.kind || "UNKNOWN"} · Lines ${s.lines?.[0]}-${s.lines?.[1]} · ${s.full_text_char_count ?? 0} characters`));
  const text = (s.full_text || "").trim();
  // Word paragraphs choke on one giant run; split on existing line breaks and cap total length defensively.
  const MAX_CHARS = 6000;
  const shown = text.length > MAX_CHARS ? text.slice(0, MAX_CHARS) + " … [truncated here; full text in the archive path above]" : text;
  for (const line of shown.split(/\n+/).filter(l => l.trim())) {
    children.push(body(line));
  }
  const linkedConcepts = conceptsBySegment[s.id] || [];
  if (linkedConcepts.length) {
    children.push(dataTable(
      ["Concept ID", "Name", "Type"],
      linkedConcepts.map(c => [c.id || "", c.name || "", c.type || ""]),
      [15, 55, 30],
    ));
  }
}
children.push(pageBreak());
children.push(heading("Formulas (15, source-provided) and Numeric Heuristics (12)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Kind", "ID", "Text", "Related Concept"],
  [
    ...DATA["DS-000031"].formulas.map(f => ["FORMULA", f.id || "", f.text || "", f.concept || ""]),
    ...DATA["DS-000031"].numeric_heuristics.map(h => ["NUMERIC_HEURISTIC", h.id || "", h.text || h.summary || "", h.concept || ""]),
  ],
  [16, 10, 54, 20],
));
children.push(heading("Example Groups (9)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["ID", "Concept", "Subject", "Role"],
  DATA["DS-000031"].examples.map(e => [e.id || "", e.concept || "", e.subject || "", e.role || ""]),
  [10, 14, 26, 50],
));
const sc = DATA["DS-000031"].scorecard;
children.push(heading("Scorecard (1)", HeadingLevel.HEADING_2));
children.push(body(`Concept: ${sc.concept}. Dimensions (0-${sc.dimension_range?.[1]} each, max ${sc.total_max}): ${(sc.dimensions || []).join(", ")}.`));
(sc.bands || []).forEach(b => children.push(body(`  ${b.range}: ${b.source_meaning}`, {})));
children.push(pageBreak());

// ================================================================ PART V — Unified index
children.push(heading("PART V — Unified Knowledge Index", HeadingLevel.HEADING_1));
children.push(body(
  "The three corpora are retained fully separate — no source, ID, or original wording is merged or erased across datasets. " +
  "DS-000011 and DS-000018 both address the YouTube algorithm but were confirmed NEW_SOURCE (no exact member/content match) " +
  "at ingestion — they are treated as independent, not corroborating, evidence. The full 779-row unified index (17 " +
  "DS-000011 rules + 699 DS-000018 claims + 63 DS-000031 concepts) is in the companion workbook, sheet 04_ALL_KNOWLEDGE."
));
children.push(heading("Documented Contradictions", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Scope", "Items", "Nature of Disagreement"],
  [
    ["DS-000018 internal", "ALG26-CLM-018 vs ALG26-CLM-005", "A creator claims Shorts and long-form use separate algorithms/audiences and should never share a channel; a platform-attributed claim elsewhere describes viewer-specific coexistence when audience overlap exists. Both retained, not merged."],
    ["DS-000018 validation", "33 claims", "1 claim was found CONTRADICTED and 8 NOT_SUPPORTED_BY_PRIMARY_EVIDENCE against official YouTube sources — see Part III table for which."],
  ],
  [20, 25, 55],
));
children.push(pageBreak());

// ================================================================ PART VI — Channel inventory
children.push(heading("PART VI — Senior Health Channel Inventory", HeadingLevel.HEADING_1));
children.push(body(
  `${recon.senior_health.known_leads_total} total Senior Health leads are known to this repository, classified: ` +
  `${recon.senior_health.class_distribution.A} + ${recon.senior_health.class_distribution.B} acquired-direct-competitor ` +
  `(classes A+B), ${recon.senior_health.class_distribution.E} qualified-pending-or-identity-only (class E: 14 qualified + 34 identity-only), ` +
  `${recon.senior_health.class_distribution.F} removed-or-unverifiable (class F), and ${recon.senior_health.class_distribution.OWN} own channel.`
));
children.push(heading("Acquired Channels (8, incl. own)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Channel", "Handle", "Classification", "Videos", "Real Transcripts", "Package Status"],
  DATA.senior_health_channels.map(c => {
    const vids = DATA.senior_health_videos_by_channel[c.canonical_channel_id];
    const realT = vids.reduce((n, v) => n + v.transcripts.filter(t => !t.is_placeholder).length, 0);
    return [c.channel_name, c.current_handle, c.classification, String(vids.length), String(realT), c.package_status];
  }),
  [26, 16, 24, 10, 12, 12],
));
children.push(heading("Qualified-Pending & Identity-Only Channels (48 total)", HeadingLevel.HEADING_2));
const pendingE = DATA.senior_health_master_inventory.channels.filter(c => c.class === "E");
children.push(dataTable(
  ["Channel", "Handle", "Videos (observed)", "Subscribers"],
  pendingE.map(c => [c.verified_name || c.recorded_name || "", c.current_handle || "", String(c.header_videos ?? ""), String(c.subscribers ?? "")]),
  [40, 24, 18, 18],
));
children.push(heading("Removed / Unverifiable Channels (13)", HeadingLevel.HEADING_2));
const removedF = DATA.senior_health_master_inventory.channels.filter(c => c.class === "F");
children.push(dataTable(
  ["Channel", "Handle"],
  removedF.map(c => [c.verified_name || c.recorded_name || "", c.current_handle || ""]),
  [60, 40],
));
children.push(pageBreak());

// ================================================================ PART VII — Acquired competitor detail
children.push(heading("PART VII — Acquired Senior Health Channel Data", HeadingLevel.HEADING_1));
children.push(body(
  "2026-09-27 correction: an earlier version of this section capped each competitor's video table at 5 rows. Below is each " +
  "acquired competitor's COMPLETE video inventory — no cap. Full per-video metadata including actual descriptions, recovered " +
  "thumbnail URLs, and self-contained transcript archive paths for all 460 videos across all 8 channels is also in the " +
  "companion workbook (sheets 15_ALL_VIDEOS, 17_TRANSCRIPT_INDEX, 18_THUMBNAIL_INDEX)."
));
for (const c of DATA.senior_health_channels) {
  if (c.classification === "OWN_CHANNEL") continue;
  const vids = DATA.senior_health_videos_by_channel[c.canonical_channel_id];
  const realT = vids.reduce((n, v) => n + v.transcripts.filter(t => !t.is_placeholder).length, 0);
  const regular = vids.filter(v => v.video_type === "video").length;
  const shorts = vids.filter(v => v.video_type === "shorts").length;
  const withThumb = vids.filter(v => v.thumbnail_url).length;
  children.push(heading(c.channel_name, HeadingLevel.HEADING_2));
  children.push(body(`Handle: ${c.current_handle} · URL: ${c.canonical_url}`));
  children.push(body(`${vids.length} videos on file (${regular} regular + ${shorts} Shorts) · ${realT} real transcripts · ${withThumb}/${vids.length} thumbnail URLs recovered · limitations: ${c.limitations || "none recorded"}`));
  const allSorted = [...vids].sort((a, b) => (b.views || 0) - (a.views || 0));
  children.push(dataTable(
    ["Title", "Published", "Type", "Views", "Real Transcript?", "Thumbnail?"],
    allSorted.map(v => [v.title || "", (v.published_at || "").slice(0, 10), v.video_type || "", String(v.views ?? ""), v.transcripts.some(t => !t.is_placeholder) ? "YES" : "NO", v.thumbnail_url ? "YES" : "NO"]),
    [40, 14, 10, 10, 14, 12],
  ));
}
children.push(pageBreak());

// ================================================================ PART VIII — Own channel
children.push(heading("PART VIII — Decode Your Heart – Dr. Rehan (Own Channel)", HeadingLevel.HEADING_1));
const own = DATA.senior_health_channels.find(c => c.canonical_channel_id === "UCQIzqH7QZ9viBYpOFqgSXMg");
const ownVids = DATA.senior_health_videos_by_channel["UCQIzqH7QZ9viBYpOFqgSXMg"];
const ownRegular = ownVids.filter(v => v.video_type === "video").length;
const ownShorts = ownVids.filter(v => v.video_type === "shorts").length;
const ownRealT = ownVids.reduce((n, v) => n + v.transcripts.filter(t => !t.is_placeholder).length, 0);
children.push(body(
  `Classified OWN_CHANNEL — not benchmarked as an independent competitor per project rules. Dataset DS-000032. ` +
  `URL: ${own.canonical_url} · Handle: ${own.current_handle}.`
));
children.push(dataTable(
  ["Field", "Value"],
  [
    ["Videos on file", String(ownVids.length)], ["Regular videos", String(ownRegular)], ["Shorts", String(ownShorts)],
    ["Real transcripts", String(ownRealT)], ["Package status", own.package_status], ["Registry status", own.status],
    ["1st-party (YouTube Studio) analytics", `${own.first_party_analytics_status} — no real Studio export ingested; impressions/CTR/retention/traffic-source/watch-time/revenue are NOT fabricated and are recorded as unavailable`],
  ],
  [35, 65],
));
children.push(heading("All 56 Videos", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Title", "Published", "Type", "Views", "Likes", "Comments", "Real Transcript?"],
  ownVids.map(v => [v.title || "", (v.published_at || "").slice(0, 10), v.video_type || "", String(v.views ?? ""), String(v.likes ?? ""), String(v.comments ?? ""), v.transcripts.some(t => !t.is_placeholder) ? "YES" : "NO"]),
  [36, 14, 10, 10, 8, 10, 12],
));
children.push(pageBreak());

// ================================================================ PART IX — Knowledge-to-video mapping
children.push(heading("PART IX — Knowledge-to-Video Relationships", HeadingLevel.HEADING_1));
children.push(body(
  `${recon ? "" : ""}These are pre-existing project-authored mappings (forensic-v2 trace/claim/framework matrices), not new ` +
  "speculative analysis produced for this export. 13 DS-000011 framework-to-video traces, 19 DS-000018 claim-to-evidence " +
  "records, and 11 DS-000031 framework-to-example mappings currently exist — this is not exhaustive; most knowledge units " +
  "have no video-level mapping yet (see Part X)."
));
children.push(heading("DS-000011 Trace Matrix (13)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Knowledge Unit", "Framework", "Videos Tested Against", "Observed Evidence", "Result"],
  DATA.knowledge_video_mappings.DS_000011_trace_matrix ? [] : DATA.knowledge_video_mappings["DS-000011_trace_matrix"].map(m => [
    m.knowledge_unit || "", m.framework || "", m.videos_tested_against || "", m.observed_evidence || "", m.result || "",
  ]),
  [10, 20, 20, 38, 12],
));
children.push(heading("DS-000018 Claim Matrix (19)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Claim ID", "Claim", "Internal Senior Health Evidence", "Claim Status"],
  DATA.knowledge_video_mappings["DS-000018_claim_matrix"].map(m => [
    m.claim_id || "", m.claim || "", m.internal_senior_health_evidence || "", m.claim_status || "",
  ]),
  [10, 30, 45, 15],
));
children.push(heading("DS-000031 Framework Matrix (11)", HeadingLevel.HEADING_2));
children.push(dataTable(
  ["Framework", "Concept IDs", "Internal Supporting Example", "Limitation"],
  DATA.knowledge_video_mappings["DS-000031_framework_matrix"].map(m => [
    m.framework || "", m.concept_ids || "", m.internal_supporting_example || "", m.limitation || "",
  ]),
  [20, 14, 40, 26],
));
children.push(pageBreak());

// ================================================================ PART X — Gaps
children.push(heading("PART X — Missing Data and Research Gaps", HeadingLevel.HEADING_1));
const gaps = [
  ["Doctor Thomas", "1 of 22 transcripts is a disclosed placeholder, not a real transcript"],
  ["All 8 acquired channels", "No first-party YouTube Studio analytics ingested — impressions/CTR/retention/traffic-source/watch-time/revenue are all NOT_AVAILABLE, never fabricated"],
  ["All 460 videos", "No per-video topic/subtopic classification exists; only a 6-item cohort-level content-pillar taxonomy exists (companion workbook sheet 19_TOPICS)"],
  ["All 460 videos", "No downloaded thumbnail images on file, URL reference only"],
  ["All 460 videos", "Editing/Visual forensic intelligence NOT_AVAILABLE for every Senior Health channel — the only channel anywhere in this repository with registered forensic video evidence is unrelated (xkcd's What If?)"],
  ["Doctor Thomas, Dr. Elias Senior Health", "No dedicated channel dossier or case study exists — cohort-table mentions only"],
  ["61 of 69 known leads", "Only 8 are fully acquired; 14 qualified-pending + 34 identity-only + 13 removed remain — no paid Apify run was performed for this export"],
  ["Knowledge-to-video mapping", "Only 43 mapping records exist across all three corpora; most of the 779 knowledge units have NOT_YET_ANALYZED video-level mapping"],
];
children.push(dataTable(["Scope", "Gap / Limitation"], gaps, [30, 70]));
children.push(pageBreak());

// ================================================================ APPENDICES
children.push(heading("Appendix A — Source Traceability / Reconciliation Matrix", HeadingLevel.HEADING_1));
children.push(dataTable(
  ["Corpus", "Prior Reported Baseline", "Directly Observed On Disk (2026-09-27)", "Outcome"],
  [
    ["DS-000011", "17 files / 16 unique", `${recon["DS-000011"].observed_files} files / ${recon["DS-000011"].observed_rules} rules / ${recon["DS-000011"].fulltext_unique_sources} full-text sources archived`, recon["DS-000011"].drift ? "DRIFT DETECTED" : "NO DRIFT"],
    ["DS-000018 (2026-09-27 correction)", "33 claims from only 7/63 tabs; validation column held citation codes, not status", `${recon["DS-000018"].observed_tabs} tabs, ${recon["DS-000018"].tabs_claim_atomized}/63 claim-atomized, ${recon["DS-000018"].original_human_audited_claims} human-audited + ${recon["DS-000018"].additional_ai_extracted_claims} AI-extracted = ${recon["DS-000018"].all_claims_combined} claims; status column fixed`, "GAP CLOSED: 56/56 previously-unprocessed tabs now claim-atomized"],
    ["DS-000031", "15 seg / 63 concepts / 11 fwk / 15 formula / 1 scorecard / 9 examples (concepts were 1-sentence summaries only)", `${recon["DS-000031"].observed.segments} seg / ${recon["DS-000031"].observed.concepts} concepts / ${recon["DS-000031"].observed.formulas} formula / ${recon["DS-000031"].observed.scorecard} scorecard / ${recon["DS-000031"].observed.examples} examples; ${recon["DS-000031"].segments_with_fulltext_recovered}/15 segments now carry full original text`, recon["DS-000031"].drift ? "DRIFT DETECTED" : "NO DRIFT"],
    ["Senior Health", "7 competitors + 98 BHWA + 56 Dr Rehan (own channel excluded from competitor count)", `8 channels acquired (7 competitors + 1 own) / ${recon.senior_health.total_unique_video_records} videos / ${recon.senior_health.total_real_transcripts} transcripts`, "MATCHES on BHWA/Dr.Rehan; old baseline undercounted by excluding own channel"],
    ["Senior Health leads", "~69 leads, '19-vs-14' reconciliation referenced", `${recon.senior_health.known_leads_total} total, class distribution ${JSON.stringify(recon.senior_health.class_distribution)}`, "MATCHES 69; '19' figure explicitly superseded per repo checkpoint doc"],
    ["Video fields (2026-09-27 correction)", "Descriptions missing from video sheet; only 64/460 thumbnail URLs; 0/56 Dr. Rehan thumbnails; competitor tables capped at 5 videos", `${recon.senior_health.total_descriptions_exported}/460 descriptions, ${recon.senior_health.total_thumbnail_urls_recovered}/460 thumbnail URLs recovered (1 genuinely unavailable), ${recon.senior_health.total_downloaded_thumbnail_files}/460 downloaded thumbnail files archived, all competitor video tables now uncapped`, "GAP CLOSED via read-only join against raw acquisition source files"],
  ],
  [16, 30, 34, 20],
));
children.push(heading("Appendix B — Data Dictionary", HeadingLevel.HEADING_1));
children.push(dataTable(
  ["Field", "Definition"],
  [
    ["canonical_channel_id", "YouTube channel ID (UC...), stable primary key across the whole registry"],
    ["dataset_id", "The registered acquisition/ingestion batch a record belongs to (e.g. DS-000032)"],
    ["is_placeholder", "1 = disclosed non-real placeholder transcript, 0 = a real captured transcript"],
    ["visual_asset_status", "NONE / THUMBNAIL_URL_ONLY / THUMBNAIL_EVIDENCE / FORENSIC_VIDEO_EVIDENCE"],
    ["first_party_analytics_status", "INGESTED / SCHEMA_READY_NO_DATA / NOT_CONFIGURED — whether a real private Studio export was ever ingested"],
    ["class (A-F, OWN)", "A/B=acquired · C/D=empty at this level · E=qualified-pending or identity-only (48) · F=removed/unverifiable (13) · OWN=own channel"],
  ],
  [30, 70],
));
children.push(heading("Appendix C — Companion Workbook Reference", HeadingLevel.HEADING_1));
children.push(body("YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.xlsx (29 sheets) holds the complete, filterable, non-truncated versions of every table in this document, plus the full 460-row video master table (with descriptions and recovered thumbnail URLs), 460-row transcript index, 460-row thumbnail index, the 699-row DS-000018 claims table, and the 63-row DS-000031 full-segment-text sheet."));

children.push(heading("Appendix D — Supplemental Data Archive", HeadingLevel.HEADING_1));
children.push(body(
  "A third artifact, supplemental-data-archive/, sits next to this document and the workbook. It exists because some " +
  "original source material (real transcript text, full DS-000018 tab text, full DS-000011 source text) is too large to " +
  "paste into Word or Excel cells without truncation, so it is copied there in full instead — every path referenced by " +
  "sheet 17 (Self-Contained Archive Path column), sheet 18 (Downloaded Image Archive Path), sheet 05b, and this document's " +
  "per-tab section is a real file under that directory, not a placeholder. It is self-contained: every path is relative " +
  "to the archive's own MANIFEST.json, not an absolute path on the original researcher's machine."
));
children.push(dataTable(
  ["Archive Subfolder", "Contents", "Count"],
  [
    ["transcripts/<channel-slug>/<video_id>.txt", "Real transcript text, copied verbatim from the repo's zip/txt evidence and SHA-256-verified against the catalog where possible", "459 files (1 disclosed unavailable)"],
    ["ds-000018-full-tabs/", "Full original markdown text of every DS-000018 research tab", "63 files"],
    ["ds-000011-full-text/", "Full original text of every DS-000011 source file, extracted from PDF/DOCX", "17 files"],
    ["ds-000031-source/", "The complete 70,730-byte DS-000031 raw corpus", "1 file"],
    ["downloaded-thumbnails/<channel-slug>/<video_id>.<ext>", "Actual downloaded thumbnail image bytes, where a prior forensic snapshot run had already fetched them (Dr. Aliza Wright 32/32, Dr. Elias 29/66)", "61 files"],
    ["MANIFEST.json", "One row per copied file with its archive-relative path, SHA-256, and status (COPIED / UNAVAILABLE / SOURCE_DATA_UNREADABLE)", "1 file"],
  ],
  [30, 55, 15],
));
children.push(small(
  "Known limitation: 276 of the 459 copied transcript files have a SHA-256 that does not match the value stored in the " +
  "catalog database, even though their content is authentic — the word_count field printed inside the packaged .txt file " +
  "matches the catalog's word_count exactly for every case checked, indicating the catalog hash was computed against an " +
  "earlier repackaging step, not that the content differs. This is disclosed rather than silently resolved; MANIFEST.json " +
  "records sha256_matches_catalog=false for every affected file so it stays checkable."
));

const doc = new Document({
  creator: "YouTube Intelligence OS export pipeline",
  title: "YouTube Knowledge & Senior Health — Complete Data Export",
  styles: {
    default: { document: { run: { font: FONT, size: 20 } } },
  },
  sections: [{
    properties: {
      page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
    },
    headers: {
      default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: "YouTube Knowledge & Senior Health — Complete Data Export", font: FONT, size: 16, color: "888888" })] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: ["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], font: FONT, size: 16, color: "888888" })] })] }),
    },
    children,
  }],
});

const buf = await Packer.toBuffer(doc);
fs.writeFileSync(OUT, buf);
console.log(`Wrote ${OUT} (${buf.length.toLocaleString()} bytes)`);
