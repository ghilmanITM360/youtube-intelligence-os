import fs from "node:fs/promises";
import { statSync } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { pathToFileURL } from "node:url";

const root = process.argv[2];
if (!root) throw new Error("repository root argument is required");
const artifactToolModule = process.argv[5] ?? "@oai/artifact-tool";
const { SpreadsheetFile, Workbook } = await import(
  artifactToolModule.startsWith("/") ? pathToFileURL(artifactToolModule).href : artifactToolModule
);

const model = JSON.parse(
  await fs.readFile(`${root}/data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json`, "utf8"),
);
const databasePath = `${root}/data/catalog/youtube_channel_registry.db`;
const workbookPath = process.argv[3] ?? `${root}/data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx`;
const renderDir = process.argv[4] ?? "/tmp/youtube-channel-registry-renders";
const githubBase = "https://github.com/ghilmanITM360/youtube-intelligence-os/blob/main/";
const fontName = "Arial";
const navy = "#1F4E78";
const blue = "#D9EAF7";
const green = "#E2F0D9";
const amber = "#FFF2CC";
const red = "#FCE4D6";
const gray = "#E7E6E6";

const sqliteJson = (sql) => {
  const text = execFileSync("sqlite3", ["-json", databasePath, sql], { encoding: "utf8" }).trim();
  return text ? JSON.parse(text) : [];
};

const datasets = sqliteJson(`
  SELECT d.dataset_id,d.dataset_name,d.manifest_path,d.evidence_scope,d.limitations,
         count(distinct dc.canonical_channel_id) channel_count,
         count(distinct dv.youtube_video_id) video_count
  FROM datasets d
  LEFT JOIN dataset_channels dc ON dc.dataset_id=d.dataset_id
  LEFT JOIN dataset_videos dv ON dv.dataset_id=d.dataset_id
  GROUP BY d.dataset_id
  ORDER BY d.dataset_id
`);

const channelById = new Map(model.channels.map((row) => [row.canonical_channel_id, row]));
const submissionsByChannel = new Map();
for (const row of model.submissions) {
  const rows = submissionsByChannel.get(row.canonical_channel_id) ?? [];
  rows.push(row);
  submissionsByChannel.set(row.canonical_channel_id, rows);
}
const coverageByChannel = new Map();
for (const row of model.intelligence_coverage) {
  const rows = coverageByChannel.get(row.canonical_channel_id) ?? new Map();
  rows.set(row.capability_id, row);
  coverageByChannel.set(row.canonical_channel_id, rows);
}

const excelText = (value) => String(value ?? "").replaceAll('"', '""');
const linkFormula = (url, label = "Open") =>
  `=HYPERLINK("${excelText(url)}","${excelText(label)}")`;
const cleanEvidencePath = (value) => {
  const first = String(value ?? "").split("; ")[0].split("#")[0].replace(/:row=.*$/, "");
  if (first.startsWith("https://")) return first;
  const dataset = /^data\/raw\/competitors\/(DS-\d{6})$/.exec(first);
  const candidate = dataset ? `data/manifests/${dataset[1]}.md` : first;
  if (!candidate.startsWith("data/") && !candidate.startsWith("docs/") && !candidate.startsWith("scripts/")) {
    throw new Error(`No repository evidence path: ${value}`);
  }
  if (!statSync(path.join(root, candidate)).isFile()) throw new Error(`Evidence file missing: ${candidate}`);
  return candidate;
};
const repoFormula = (value, label = "Evidence") =>
  linkFormula(String(value ?? "").startsWith("https://") ? value : `${githubBase}${cleanEvidencePath(value)}`, label);
const yes = (condition) => (condition ? "✓" : "No");
const displayStatus = (row, capability) =>
  coverageByChannel.get(row.canonical_channel_id)?.get(capability)?.status ?? "NOT_AVAILABLE";
const shorten = (value, limit = 220) => {
  const text = String(value ?? "").trim();
  return text.length <= limit ? text : `${text.slice(0, limit - 1).trimEnd()}…`;
};
const asDate = (value) => new Date(`${value}T00:00:00`);
const columnName = (index) => {
  let value = index;
  let result = "";
  while (value > 0) {
    value -= 1;
    result = String.fromCharCode(65 + (value % 26)) + result;
    value = Math.floor(value / 26);
  }
  return result;
};

const workbook = Workbook.create();
const sheetNames = [
  "Dashboard",
  "All Channels",
  "Pending Channels",
  "Data Coverage",
  "Visual Evidence",
  "Datasets",
  "Submitted URLs",
  "Intelligence Coverage",
  "Definitions",
];
for (const name of sheetNames) workbook.worksheets.add(name);

function title(sheet, text, note = "") {
  sheet.showGridLines = false;
  sheet.getRange("A2").values = [[text]];
  sheet.getRange("A2").format.font = { name: fontName, size: 14, bold: true, color: navy };
  if (note) {
    sheet.getRange("A3").values = [[note]];
    sheet.getRange("A3").format.font = { name: fontName, size: 10, italic: true, color: "#595959" };
  }
}

function addTable(sheet, headers, rows, tableName) {
  const endColumn = columnName(headers.length);
  const endRow = 4 + rows.length;
  sheet.getRange(`A4:${endColumn}4`).values = [headers];
  if (rows.length) sheet.getRange(`A5:${endColumn}${endRow}`).values = rows;
  const table = sheet.tables.add(`A4:${endColumn}${endRow}`, true, tableName);
  table.style = "TableStyleMedium2";
  table.showFilterButton = true;
  sheet.getRange(`A4:${endColumn}${endRow}`).format.font = { name: fontName, size: 10, color: "#1F1F1F" };
  sheet.getRange(`A4:${endColumn}4`).format = {
    fill: navy,
    font: { name: fontName, size: 10, bold: true, color: "#FFFFFF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "inside", style: "thin", color: "#FFFFFF" },
  };
  sheet.getRange(`A4:${endColumn}4`).format.rowHeight = 44;
  sheet.getRange(`A5:${endColumn}${endRow}`).format.verticalAlignment = "center";
  sheet.freezePanes.freezeRows(4);
  return { endColumn, endRow };
}

function setWidths(sheet, widths, endRow) {
  widths.forEach((width, index) => {
    const column = columnName(index + 1);
    sheet.getRange(`${column}1:${column}${endRow}`).format.columnWidth = width;
  });
}

function setDateColumn(sheet, column, startRow, endRow) {
  sheet.getRange(`${column}${startRow}:${column}${endRow}`).format.numberFormat = "yyyy-mm-dd";
}

const allChannels = workbook.worksheets.getItem("All Channels");
title(
  allChannels,
  "YouTube channel registry",
  "Identity, extraction, package, transcript, visual, intelligence, and first-party analytics states are independent.",
);
const allHeaders = [
  "Canonical Channel ID",
  "Channel Name",
  "Current Handle",
  "YouTube Link",
  "Target Membership",
  "Target Batch",
  "Identity Verified",
  "Video Data Available",
  "Extraction Status",
  "Standard Package Available",
  "Historical-Format Data Available",
  "Saved Video Count",
  "Real Transcripts",
  "Transcript Placeholders",
  "Missing Descriptions",
  "Transcript Status",
  "Thumbnail URLs Available",
  "Downloaded Thumbnail Evidence",
  "Forensic Video Evidence",
  "Topic Intelligence",
  "Packaging Intelligence",
  "Hook Intelligence",
  "Script Intelligence",
  "Editing/Visual Intelligence",
  "Unified Orchestration",
  "Channel Strategy",
  "First-Party Analytics",
  "Evidence Links",
  "Dataset IDs",
  "Limitations",
  "Last Verified",
];
const allRows = model.channels.map((row) => {
  const submissions = submissionsByChannel.get(row.canonical_channel_id) ?? [];
  const batches = [...new Set(submissions.map((item) => item.batch))].join(", ") || "—";
  const evidence = row.workbook_path || row.visual_coverage.evidence_path || row.identity_evidence_source;
  return [
    row.canonical_channel_id,
    row.channel_name,
    row.current_handle || "—",
    null,
    row.target_group,
    batches,
    yes(row.identity_status === "VERIFIED"),
    yes(row.video_count > 0),
    row.extraction_status,
    yes(row.package_status === "STANDARD_PACKAGE"),
    yes(row.package_status === "HISTORICAL_FORMAT"),
    row.video_count,
    row.real_transcripts,
    row.placeholders,
    row.descriptions === null ? 0 : row.video_count - row.descriptions,
    row.transcript_status,
    yes(row.visual_coverage.thumbnail_url_count > 0),
    yes(row.visual_coverage.downloaded_thumbnail_count > 0),
    yes(row.visual_coverage.visual_evidence_level === "FORENSIC_VIDEO_EVIDENCE"),
    displayStatus(row, "TOPIC_OPPORTUNITY"),
    displayStatus(row, "PACKAGING"),
    displayStatus(row, "HOOK"),
    displayStatus(row, "SCRIPT"),
    displayStatus(row, "EDITING_VISUAL"),
    displayStatus(row, "UNIFIED_ORCHESTRATION"),
    displayStatus(row, "CHANNEL_STRATEGY"),
    row.first_party_analytics_status,
    null,
    row.dataset_ids.join(", ") || "—",
    shorten(row.limitations || row.handle_unavailable_reason),
    asDate(row.verified_at),
  ];
});
const allBounds = addTable(allChannels, allHeaders, allRows, "AllChannelsTable");
allChannels.getRange(`D5:D${allBounds.endRow}`).formulas = model.channels.map((row) => [linkFormula(row.canonical_url, "YouTube")]);
allChannels.getRange(`AB5:AB${allBounds.endRow}`).formulas = model.channels.map((row) => {
  const evidence = row.workbook_path || row.visual_coverage.evidence_path || row.identity_evidence_source;
  return [repoFormula(evidence)];
});
allChannels.getRange(`D5:D${allBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
allChannels.getRange(`AB5:AB${allBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
setDateColumn(allChannels, "AE", 5, allBounds.endRow);
setWidths(allChannels, [26, 25, 21, 12, 19, 12, 13, 15, 24, 16, 18, 13, 13, 13, 13, 24, 14, 17, 14, 18, 18, 16, 16, 19, 18, 18, 22, 13, 24, 55, 13], allBounds.endRow);
allChannels.getRange(`AD5:AD${allBounds.endRow}`).format.wrapText = true;
allChannels.getRange(`A5:AE${allBounds.endRow}`).format.rowHeight = 42;
allChannels.freezePanes.freezeColumns(3);
allChannels.getRange(`I5:I${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "COMPLETE_WITH_LIMITATIONS", format: { fill: amber, font: { color: "#7F6000", bold: true } } });
allChannels.getRange(`I5:I${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "COMPLETE", format: { fill: green, font: { color: "#375623" } } });
allChannels.getRange(`I5:I${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "PARTIAL", format: { fill: amber, font: { color: "#7F6000" } } });
allChannels.getRange(`I5:I${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "NOT_EXTRACTED", format: { fill: red, font: { color: "#9C0006", bold: true } } });
allChannels.getRange(`T5:AA${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "VALIDATED", format: { fill: green } });
allChannels.getRange(`T5:AA${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "DATA_READY", format: { fill: blue } });
allChannels.getRange(`T5:AA${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "PARTIAL", format: { fill: amber } });
allChannels.getRange(`T5:AA${allBounds.endRow}`).conditionalFormats.add("containsText", { text: "NOT_AVAILABLE", format: { fill: gray } });

const pending = workbook.worksheets.getItem("Pending Channels");
title(pending, "Channels awaiting extraction", "Identity is verified for all 29 rows. Video extraction and package creation have not started.");
const pendingRows = model.channels
  .filter((row) => row.source_group === "IDENTITY_ONLY")
  .map((row) => [
    row.channel_name,
    null,
    row.canonical_channel_id,
    row.target_group,
    "No video data",
    "Run authorized channel extraction; then build and validate a standard package.",
    row.extraction_status,
    row.package_status,
    "NOT_GENERATED",
    row.visual_asset_status,
  ]);
const pendingBounds = addTable(pending, ["Channel Name", "Channel URL", "Canonical ID", "Target Group", "Video Data Status", "Required Next Action", "Extraction Status", "Package Status", "Intelligence Status", "Visual Evidence"], pendingRows, "PendingChannelsTable");
pending.getRange(`B5:B${pendingBounds.endRow}`).formulas = model.channels.filter((row) => row.source_group === "IDENTITY_ONLY").map((row) => [linkFormula(row.canonical_url, "YouTube")]);
pending.getRange(`B5:B${pendingBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
setWidths(pending, [26, 13, 27, 18, 17, 52, 20, 18, 19, 24], pendingBounds.endRow);
pending.getRange(`F5:F${pendingBounds.endRow}`).format.wrapText = true;
pending.getRange(`A5:J${pendingBounds.endRow}`).format.rowHeight = 36;
pending.getRange(`G5:J${pendingBounds.endRow}`).conditionalFormats.add("containsText", { text: "NOT_", format: { fill: red, font: { color: "#9C0006" } } });
pending.freezePanes.freezeColumns(3);

const dataCoverage = workbook.worksheets.getItem("Data Coverage");
title(dataCoverage, "Channel data coverage", "Availability marks are evidence-derived. A raw input does not imply a generated intelligence artifact.");
const actorDatasets = new Set(["DS-000017", "DS-000020", "DS-000021", "DS-000023", "DS-000024", "DS-000025", "DS-000027"]);
const dataCoverageRows = model.channels.map((row) => {
  const capabilityRows = [...(coverageByChannel.get(row.canonical_channel_id)?.values() ?? [])];
  return [
    row.canonical_channel_id,
    row.channel_name,
    yes(row.identity_status === "VERIFIED"),
    yes(Boolean(row.channel_name && row.canonical_url)),
    yes(row.video_count > 0),
    row.description_status,
    yes(row.video_count > 0),
    row.transcript_status,
    yes(row.package_status === "STANDARD_PACKAGE"),
    yes(row.package_status === "HISTORICAL_FORMAT"),
    yes(row.dataset_ids.some((id) => actorDatasets.has(id))),
    row.dataset_ids.length ? "✓" : "Identity evidence only",
    yes(capabilityRows.some((item) => item.generated_artifact_available)),
  ];
});
const dataBounds = addTable(dataCoverage, ["Canonical ID", "Channel", "Identity", "Channel Metadata", "Video Metadata", "Descriptions", "Metrics", "Transcripts", "Standard Package", "Historical Data", "Raw Actor Evidence", "Manifest / Checksums", "Intelligence Artifacts"], dataCoverageRows, "DataCoverageTable");
setWidths(dataCoverage, [27, 25, 12, 17, 16, 24, 12, 24, 17, 16, 18, 22, 20], dataBounds.endRow);
dataCoverage.getRange(`C5:M${dataBounds.endRow}`).conditionalFormats.add("containsText", { text: "✓", format: { fill: green } });
dataCoverage.getRange(`C5:M${dataBounds.endRow}`).conditionalFormats.add("containsText", { text: "No", format: { fill: gray } });
dataCoverage.freezePanes.freezeColumns(2);

const visual = workbook.worksheets.getItem("Visual Evidence");
title(visual, "Visual evidence coverage", "Thumbnail URLs, downloaded thumbnails, screenshots, and forensic video evidence are not interchangeable.");
const visualHeaders = ["Channel / Subject", "Canonical ID", "YouTube Link", "Thumbnail URL Count", "Downloaded Thumbnails", "Screenshots", "Keyframes", "Source Videos", "Timestamped Observations", "Evidence Level", "Editing/Visual Intelligence", "Evidence Link", "Limitation"];
const visualRows = model.channels.map((row) => [
  row.channel_name,
  row.canonical_channel_id,
  null,
  row.visual_coverage.thumbnail_url_count,
  row.visual_coverage.downloaded_thumbnail_count,
  row.visual_coverage.screenshot_count,
  row.visual_coverage.keyframe_count,
  row.visual_coverage.registered_source_video_count,
  row.visual_coverage.timestamped_visual_observation_count,
  row.visual_coverage.visual_evidence_level,
  row.visual_coverage.editing_visual_intelligence_status,
  null,
  shorten(row.visual_coverage.limitation_reason),
]);
const visualBounds = addTable(visual, visualHeaders, visualRows, "ChannelVisualEvidenceTable");
visual.getRange(`C5:C${visualBounds.endRow}`).formulas = model.channels.map((row) => [linkFormula(row.canonical_url, "YouTube")]);
visual.getRange(`L5:L${visualBounds.endRow}`).formulas = model.channels.map((row) => [repoFormula(row.visual_coverage.evidence_path)]);
visual.getRange(`C5:C${visualBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
visual.getRange(`L5:L${visualBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
const subjectTitleRow = visualBounds.endRow + 2;
const subjectHeaderRow = subjectTitleRow + 1;
const subjectStartRow = subjectHeaderRow + 1;
const subjectEndRow = subjectStartRow + model.subjects.length - 1;
visual.getRange(`A${subjectTitleRow}`).values = [["Unmapped screenshot-only subjects"]];
visual.getRange(`A${subjectTitleRow}`).format.font = { name: fontName, size: 12, bold: true, color: navy };
visual.getRange(`A${subjectHeaderRow}:M${subjectHeaderRow}`).values = [visualHeaders];
const subjectRows = model.subjects.map((row) => [row.subject_name, "—", "—", 0, 0, row.screenshot_count, 0, 0, 0, row.visual_evidence_level, "NOT_APPLICABLE", null, shorten(row.limitation)]);
visual.getRange(`A${subjectStartRow}:M${subjectEndRow}`).values = subjectRows;
visual.getRange(`L${subjectStartRow}:L${subjectEndRow}`).formulas = model.subjects.map((row) => [repoFormula(row.evidence_path)]);
visual.getRange(`L${subjectStartRow}:L${subjectEndRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
const subjectTable = visual.tables.add(`A${subjectHeaderRow}:M${subjectEndRow}`, true, "UnmappedScreenshotSubjectsTable");
subjectTable.style = "TableStyleMedium4";
subjectTable.showFilterButton = true;
visual.getRange(`A${subjectHeaderRow}:M${subjectHeaderRow}`).format = { fill: "#548235", font: { name: fontName, size: 10, bold: true, color: "#FFFFFF" }, horizontalAlignment: "center", verticalAlignment: "center", wrapText: true };
visual.getRange(`A${subjectHeaderRow}:M${subjectHeaderRow}`).format.rowHeight = 44;
visual.getRange(`A${subjectStartRow}:M${subjectEndRow}`).format.font = { name: fontName, size: 10 };
setWidths(visual, [26, 27, 12, 15, 17, 12, 12, 13, 18, 28, 23, 13, 58], subjectEndRow);
visual.getRange(`M5:M${subjectEndRow}`).format.wrapText = true;
visual.getRange(`A5:M${visualBounds.endRow}`).format.rowHeight = 42;
visual.getRange(`A${subjectStartRow}:M${subjectEndRow}`).format.rowHeight = 42;
visual.getRange(`J5:K${visualBounds.endRow}`).conditionalFormats.add("containsText", { text: "FORENSIC", format: { fill: green, font: { color: "#375623", bold: true } } });
visual.getRange(`J5:K${visualBounds.endRow}`).conditionalFormats.add("containsText", { text: "THUMBNAIL_EVIDENCE", format: { fill: blue } });
visual.getRange(`J5:K${visualBounds.endRow}`).conditionalFormats.add("containsText", { text: "THUMBNAIL_URL_ONLY", format: { fill: amber } });
visual.freezePanes.freezeColumns(2);

const datasetSheet = workbook.worksheets.getItem("Datasets");
title(datasetSheet, "Registered datasets", "Registered manifest datasets through DS-000027 are included. Channel and video counts preserve many-to-many membership.");
const datasetRows = datasets.map((row) => [row.dataset_id, row.dataset_name, row.channel_count, row.video_count, null, row.evidence_scope || "—", shorten(row.limitations)]);
const datasetBounds = addTable(datasetSheet, ["Dataset ID", "Dataset Name", "Channel Count", "Video Count", "Manifest", "Evidence Scope", "Limitations"], datasetRows, "DatasetsTable");
datasetSheet.getRange(`E5:E${datasetBounds.endRow}`).formulas = datasets.map((row) => [repoFormula(row.manifest_path, "Manifest")]);
datasetSheet.getRange(`E5:E${datasetBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
setWidths(datasetSheet, [14, 67, 14, 13, 13, 25, 45], datasetBounds.endRow);
datasetSheet.getRange(`B5:B${datasetBounds.endRow}`).format.wrapText = true;
datasetSheet.getRange(`A5:G${datasetBounds.endRow}`).format.rowHeight = 42;

const submitted = workbook.worksheets.getItem("Submitted URLs");
title(submitted, "Submitted YouTube URLs", "All 67 rows remain in authoritative order. Exact duplicates retain their prior-row references.");
const submittedRows = model.submissions.map((row) => [
  row.global_row,
  row.batch,
  row.batch_row,
  row.original_url,
  null,
  null,
  yes(row.is_exact_duplicate),
  row.duplicate_of_global_row ?? "—",
  row.canonical_channel_id,
  channelById.get(row.canonical_channel_id)?.channel_name ?? "",
  row.identity_status,
  null,
  asDate(row.verified_at),
]);
const submittedBounds = addTable(submitted, ["Global Row", "Batch", "Batch Row", "Original URL", "Original Link", "Normalized Link", "Exact Duplicate", "Duplicate Of Global Row", "Canonical ID", "Channel Name", "Identity Status", "Evidence Link", "Verified At"], submittedRows, "SubmittedUrlsTable");
submitted.getRange(`E5:E${submittedBounds.endRow}`).formulas = model.submissions.map((row) => [linkFormula(row.original_url, "Original")]);
submitted.getRange(`F5:F${submittedBounds.endRow}`).formulas = model.submissions.map((row) => [linkFormula(row.normalized_url, "Normalized")]);
submitted.getRange(`L5:L${submittedBounds.endRow}`).formulas = model.submissions.map((row) => [repoFormula(row.evidence_source)]);
submitted.getRange(`E5:F${submittedBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
submitted.getRange(`L5:L${submittedBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
setDateColumn(submitted, "M", 5, submittedBounds.endRow);
setWidths(submitted, [12, 8, 11, 56, 13, 14, 15, 18, 27, 26, 16, 13, 13], submittedBounds.endRow);
submitted.getRange(`D5:D${submittedBounds.endRow}`).format.wrapText = true;
submitted.getRange(`G5:G${submittedBounds.endRow}`).conditionalFormats.add("containsText", { text: "✓", format: { fill: amber, font: { color: "#7F6000", bold: true } } });
submitted.freezePanes.freezeColumns(3);

const intelligence = workbook.worksheets.getItem("Intelligence Coverage");
title(intelligence, "Intelligence capability coverage", `${model.intelligence_coverage.length} rows represent eight capabilities for ${model.channels.length} channels; they do not represent completed reports.`);
const intelligenceRows = model.intelligence_coverage.map((row) => [
  row.canonical_channel_id,
  channelById.get(row.canonical_channel_id)?.channel_name ?? "",
  row.capability_id,
  row.status,
  yes(row.input_data_available),
  yes(row.generated_artifact_available),
  cleanEvidencePath(row.evidence_path),
  null,
  shorten(row.limitation_reason),
  asDate(row.last_verified_at),
]);
const intelligenceBounds = addTable(intelligence, ["Canonical ID", "Channel", "Capability", "Status", "Input Data Available", "Analysis Artifact Generated", "Evidence Path", "Evidence Link", "Limitation", "Last Verified"], intelligenceRows, "IntelligenceCoverageTable");
intelligence.getRange(`H5:H${intelligenceBounds.endRow}`).formulas = model.intelligence_coverage.map((row) => [repoFormula(row.evidence_path)]);
intelligence.getRange(`H5:H${intelligenceBounds.endRow}`).format.font = { name: fontName, size: 10, color: "#0563C1" };
setDateColumn(intelligence, "J", 5, intelligenceBounds.endRow);
setWidths(intelligence, [27, 25, 26, 18, 17, 19, 57, 13, 62, 13], intelligenceBounds.endRow);
intelligence.getRange(`G5:I${intelligenceBounds.endRow}`).format.wrapText = true;
intelligence.getRange(`A5:J${intelligenceBounds.endRow}`).format.rowHeight = 42;
intelligence.getRange(`D5:D${intelligenceBounds.endRow}`).conditionalFormats.add("containsText", { text: "VALIDATED", format: { fill: green } });
intelligence.getRange(`D5:D${intelligenceBounds.endRow}`).conditionalFormats.add("containsText", { text: "DATA_READY", format: { fill: blue } });
intelligence.getRange(`D5:D${intelligenceBounds.endRow}`).conditionalFormats.add("containsText", { text: "PARTIAL", format: { fill: amber } });
intelligence.getRange(`D5:D${intelligenceBounds.endRow}`).conditionalFormats.add("containsText", { text: "NOT_AVAILABLE", format: { fill: gray } });
intelligence.freezePanes.freezeColumns(2);

const definitions = workbook.worksheets.getItem("Definitions");
title(definitions, "Definitions and status rules", "These definitions prevent identity resolution, extraction, packages, visual evidence, intelligence, and analytics from being conflated.");
const definitionsRows = [
  ["Identity verified", "Canonical YouTube channel ID is proven by repository or official-page evidence."],
  ["Video data available", "One or more unique videos are stored for the canonical channel."],
  ["STANDARD_PACKAGE", "Validated new-style workbook and transcript ZIP package."],
  ["HISTORICAL_FORMAT", "Stored historical catalog data; not a new-style standard package."],
  ["NO_PACKAGE", "No standardized or historical channel package is registered."],
  ["COMPLETE", "Extraction evidence meets the applicable package or historical controls."],
  ["COMPLETE_WITH_LIMITATIONS", "Stored extraction is usable but an explicit transcript, description, or format limitation remains."],
  ["PARTIAL", "Some required extraction evidence exists; coverage is incomplete."],
  ["NOT_EXTRACTED", "Identity is verified, but channel video extraction has not started."],
  ["COMPLETE_REAL", "Every stored video has a real transcript."],
  ["COMPLETE_WITH_PLACEHOLDERS", "Every stored video has a transcript row, but one or more are explicit placeholders."],
  ["THUMBNAIL_URL_ONLY", "Thumbnail metadata URL exists; no downloaded thumbnail evidence is registered."],
  ["THUMBNAIL_EVIDENCE", "Downloaded thumbnail or screenshot evidence is registered."],
  ["FORENSIC_VIDEO_EVIDENCE", "Registered source video and timestamped/keyframe observations support editing analysis."],
  ["SCREENSHOT_ONLY_UNMAPPED", "Screenshot subject remains separate because no canonical YouTube channel identity is proven."],
  ["VALIDATED", "Generated capability artifact passed its documented validation scope."],
  ["AVAILABLE", "Generated capability artifact exists; validation is not universal."],
  ["PARTIAL", "Generated capability output exists with a material documented limitation."],
  ["DATA_READY", "Required input data or schema exists, but no channel-specific analysis artifact is generated."],
  ["NOT_AVAILABLE", "Required input or generated artifact is unavailable."],
  ["SCHEMA_READY_NO_DATA", "First-party ingestion schema is ready; no real YouTube Studio/Analytics export is ingested."],
  ["Public metrics", "Public views, likes, comments, and subscriber counts are not first-party YouTube Analytics."],
  ["Completion tick", "A check mark applies only to the specific availability column in which it appears."],
];
const definitionBounds = addTable(definitions, ["Term", "Definition"], definitionsRows, "DefinitionsTable");
setWidths(definitions, [34, 112], definitionBounds.endRow);
definitions.getRange(`B5:B${definitionBounds.endRow}`).format.wrapText = true;
definitions.getRange(`A5:B${definitionBounds.endRow}`).format.rowHeight = 42;

const dashboard = workbook.worksheets.getItem("Dashboard");
title(dashboard, "YouTube channel registry dashboard", "Formula-linked controls as of 2026-09-14. Each card measures one evidence layer.");
dashboard.showGridLines = false;
dashboard.getRange("A5:A11").values = [["Canonical registry channels"], ["Target channels"], ["Channels with video data"], ["Standard package channels"], ["Historical-format channels"], ["Identity-only channels"], ["Full forensic visual channels"]];
dashboard.getRange("D5:D11").values = [["Thumbnail-evidence intelligence channels"], ["Title-only packaging channels"], ["Unmapped screenshot subjects"], ["Stored unique videos"], ["Real transcripts"], ["Transcript placeholders"], ["Missing public descriptions"]];
dashboard.getRange("B5:B11").formulas = [
  [`=COUNTA('All Channels'!$A$5:$A$${allBounds.endRow})`],
  [`=COUNTIFS('All Channels'!$E$5:$E$${allBounds.endRow},\"<>OUTSIDE_TARGET\")`],
  [`=COUNTIFS('All Channels'!$H$5:$H$${allBounds.endRow},\"✓\")`],
  [`=COUNTIFS('All Channels'!$J$5:$J$${allBounds.endRow},\"✓\")`],
  [`=COUNTIFS('All Channels'!$K$5:$K$${allBounds.endRow},\"✓\")`],
  [`=COUNTIFS('All Channels'!$I$5:$I$${allBounds.endRow},\"NOT_EXTRACTED\")`],
  [`=COUNTIFS('All Channels'!$S$5:$S$${allBounds.endRow},\"✓\")`],
];
dashboard.getRange("E5:E11").formulas = [
  [`=COUNTIFS('All Channels'!$R$5:$R$${allBounds.endRow},\"✓\")`],
  [`=COUNTIFS('All Channels'!$K$5:$K$${allBounds.endRow},\"✓\",'All Channels'!$Q$5:$Q$${allBounds.endRow},\"No\")`],
  [`=COUNTA('Visual Evidence'!$A$${subjectStartRow}:$A$${subjectEndRow})`],
  [`=SUM('All Channels'!$L$5:$L$${allBounds.endRow})`],
  [`=SUM('All Channels'!$M$5:$M$${allBounds.endRow})`],
  [`=SUM('All Channels'!$N$5:$N$${allBounds.endRow})`],
  [`=SUM('All Channels'!$O$5:$O$${allBounds.endRow})`],
];
for (const range of ["A5:B11", "D5:E11"]) {
  dashboard.getRange(range).format = {
    font: { name: fontName, size: 10, color: "#1F1F1F" },
    fill: "#F7F9FC",
    borders: { preset: "outside", style: "thin", color: "#B4C6E7" },
    verticalAlignment: "center",
  };
}
dashboard.getRange("B5:B11").format = { fill: blue, font: { name: fontName, size: 14, bold: true, color: navy }, horizontalAlignment: "center", verticalAlignment: "center" };
dashboard.getRange("E5:E11").format = { fill: green, font: { name: fontName, size: 14, bold: true, color: "#375623" }, horizontalAlignment: "center", verticalAlignment: "center" };
dashboard.getRange("A5:E11").format.rowHeight = 32;
setWidths(dashboard, [42, 14, 5, 47, 14], 16);
dashboard.getRange("A14:E16").values = [
  ["Interpretation", null, null, null, null],
  ["Raw data availability is not the same as generated intelligence.", null, null, null, null],
  ["Public scraped metrics are not first-party YouTube Analytics.", null, null, null, null],
];
dashboard.getRange("A14:E14").format = { fill: navy, font: { name: fontName, size: 10, bold: true, color: "#FFFFFF" } };
dashboard.getRange("A15:E16").format.font = { name: fontName, size: 10, italic: true, color: "#595959" };

workbook.recalculate();

const overview = await workbook.inspect({
  kind: "table",
  range: "Dashboard!A1:E16",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 8,
  maxChars: 8000,
});
console.log(overview.ndjson);
const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log(errors.ndjson);

await fs.mkdir(renderDir, { recursive: true });
const splitRenderRanges = (endColumn, endRow) => {
  const ranges = [];
  for (let startRow = 1; startRow <= endRow; startRow += 140) {
    ranges.push(`A${startRow}:${endColumn}${Math.min(startRow + 139, endRow)}`);
  }
  return ranges;
};
const renderRanges = {
  Dashboard: ["A1:E16"],
  "All Channels": splitRenderRanges("AE", allBounds.endRow),
  "Pending Channels": splitRenderRanges("J", pendingBounds.endRow),
  "Data Coverage": splitRenderRanges("M", dataBounds.endRow),
  "Visual Evidence": splitRenderRanges("M", subjectEndRow),
  Datasets: splitRenderRanges("G", datasetBounds.endRow),
  "Submitted URLs": splitRenderRanges("M", submittedBounds.endRow),
  "Intelligence Coverage": splitRenderRanges("J", intelligenceBounds.endRow),
  Definitions: [`A1:B${definitionBounds.endRow}`],
};
for (const [sheetName, ranges] of Object.entries(renderRanges)) {
  for (const [index, range] of ranges.entries()) {
    const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
    await fs.writeFile(`${renderDir}/${sheetName.replaceAll(" ", "_")}-${index + 1}.png`, new Uint8Array(await preview.arrayBuffer()));
  }
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await fs.mkdir(path.dirname(workbookPath), { recursive: true });
await output.save(workbookPath);
execFileSync(process.env.PYTHON ?? "python3", [
  `${root}/scripts/normalize_tracker_hyperlinks.py`,
  workbookPath,
]);
console.log(JSON.stringify({ workbookPath, renderDir, sheets: sheetNames.length }));
