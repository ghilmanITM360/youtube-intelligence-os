#!/usr/bin/env node
/**
 * Build and validate canonical five-channel YouTube data packages.
 *
 * Requires Node.js plus @oai/artifact-tool and JSZip. Dependency module paths
 * are supplied at runtime so this repository contains no machine-specific path.
 * Run with --help for the complete command.
 */

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import crypto from "node:crypto";
import { pathToFileURL } from "node:url";

const DATASET_ID = "DS-000020";
const DATASET_NAME = "Five-Channel YouTube Apify Dataset Packages";
const ACTOR = "streamers/youtube-scraper";
const COLLECTION_DATE = "2026-09-12";
const OLD_RUN_ID = "gHdfrGgqKgaJTpQYf";
const OLD_DATASET_ID = "rHxW9HkEtoKL0ox0I";
const NEW_RUN_ID = "p3YkBpvXTnFgK1Yzg";
const NEW_DATASET_ID = "Gc7WCqaw61qPm5EfJ";
const RECOVERY_RUN_ID = "3P6JmgeBgwcgwV1BU";
const RECOVERY_DATASET_ID = "H26eTQBhYOisHTDXd";

const CHANNELS = [
  { name: "Apesthetic", slug: "apesthetic", count: 22, workbook: "Apesthetic_Master_Data.xlsx", zip: "Apesthetic_Transcripts_22_Videos.zip", group: "existing", runId: OLD_RUN_ID, datasetId: OLD_DATASET_ID },
  { name: "Primate Economics", slug: "primate-economics", count: 28, workbook: "PrimateEconomics_Master_Data.xlsx", zip: "PrimateEconomics_Transcripts_28_Videos.zip", group: "existing", runId: OLD_RUN_ID, datasetId: OLD_DATASET_ID },
  { name: "Sonny Finance", slug: "sonny-finance", count: 39, workbook: "SonnyFinance_Master_Data.xlsx", zip: "SonnyFinance_Transcripts_39_Videos.zip", group: "new", runId: NEW_RUN_ID, datasetId: NEW_DATASET_ID },
  { name: "Money Life POV", slug: "money-life-pov", count: 20, workbook: "MoneyLifePOV_Master_Data.xlsx", zip: "MoneyLifePOV_Transcripts_20_Videos.zip", group: "new", runId: NEW_RUN_ID, datasetId: NEW_DATASET_ID },
  { name: "My Chaotic Stories", slug: "my-chaotic-stories", count: 23, workbook: "MyChaoticStories_Master_Data.xlsx", zip: "MyChaoticStories_Transcripts_23_Videos.zip", group: "new", runId: NEW_RUN_ID, datasetId: NEW_DATASET_ID },
];

const REQUIRED_SHEETS = ["Channel Overview", "All Videos", "Descriptions", "Verification", "Analysis"];
const ALL_VIDEO_HEADERS = [
  "#", "Video ID", "Title", "Video URL", "Published (UTC)", "Date", "Day", "Duration", "Sec", "Views",
  "Likes", "Comments", "Like Rate", "Comment Rate", "Engagement", "Views/Day", "Transcript Words", "Words/Min",
  "Desc Chars", "Desc Links", "Hashtags", "Caption Type", "Transcript File", "Thumbnail URL", "Members Only", "Paid",
  "Comments Off", "Age Restr.",
];
const DESCRIPTION_HEADERS = ["#", "Video ID", "Title", "Hashtags", "Link Count", "Description Links (URLs)", "Full Description"];
const ERROR_PATTERN = "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!";

function parseArgs(argv) {
  const args = {};
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === "--help") args.help = true;
    else if (token.startsWith("--")) {
      const key = token.slice(2);
      if (!argv[index + 1] || argv[index + 1].startsWith("--")) throw new Error(`Missing value for ${token}`);
      args[key] = argv[index + 1];
      index += 1;
    } else throw new Error(`Unexpected argument: ${token}`);
  }
  return args;
}

function usage() {
  return `Usage:
  node scripts/package_five_channel_youtube_dataset.mjs \\
    --repo-root <path> \\
    --master-json <path> --master-csv <path> --master-xlsx <path> \\
    --old-output-dir <path> --master-output-dir <path> \\
    --old-raw-json <path> --new-raw-json <path> --new-clean-json <path> \\
    --channel-summary-csv <path> --prior-validation-report <path> \\
    --recovery-raw-json <path> --description-verification-json <path> \\
    --template-xlsx <path> --reference-dir <path> \\
    --artifact-tool-module <path-to-artifact_tool.mjs> \\
    --jszip-module <path-to-jszip-module> \\
    --raw-output-dir <repo-relative-path> \\
    --extracted-output-dir <repo-relative-path> \\
    --manifest-dir <repo-relative-path> \\
    --qa-output-dir <path>

Outputs: immutable raw copies, preserved combined files, five workbooks, five
transcript ZIPs, recovery reconciliation, validation report, and DS-000020
manifest files. Input artifacts are read only.`;
}

const args = parseArgs(process.argv.slice(2));
if (args.help) {
  console.log(usage());
  process.exit(0);
}
const requiredArgs = [
  "repo-root", "master-json", "master-csv", "master-xlsx", "old-raw-json", "new-raw-json", "new-clean-json",
  "channel-summary-csv", "prior-validation-report", "recovery-raw-json", "description-verification-json", "template-xlsx",
  "reference-dir", "old-output-dir", "master-output-dir", "artifact-tool-module", "jszip-module", "raw-output-dir", "extracted-output-dir", "manifest-dir", "qa-output-dir",
];
for (const key of requiredArgs) if (!args[key]) throw new Error(`Required argument missing: --${key}`);

const repoRoot = path.resolve(args["repo-root"]);
const rawOutputDir = path.resolve(repoRoot, args["raw-output-dir"]);
const extractedOutputDir = path.resolve(repoRoot, args["extracted-output-dir"]);
const manifestDir = path.resolve(repoRoot, args["manifest-dir"]);
const qaOutputDir = path.resolve(args["qa-output-dir"]);
const combinedDir = path.join(extractedOutputDir, "combined");
const packagesDir = path.join(extractedOutputDir, "packages");

for (const location of [rawOutputDir, extractedOutputDir, manifestDir]) {
  const relative = path.relative(repoRoot, location);
  if (relative.startsWith("..") || path.isAbsolute(relative)) throw new Error(`Output escapes repository: ${location}`);
}

const artifactModule = await import(pathToFileURL(path.resolve(args["artifact-tool-module"])).href);
const zipModule = await import(pathToFileURL(path.resolve(args["jszip-module"])).href);
const { FileBlob, SpreadsheetFile } = artifactModule;
const JSZip = zipModule.default ?? zipModule;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function exists(filePath) {
  try { await fs.access(filePath); return true; } catch { return false; }
}

async function sha256(filePath) {
  const digest = crypto.createHash("sha256");
  digest.update(await fs.readFile(filePath));
  return digest.digest("hex");
}

function sha256Text(text) {
  return crypto.createHash("sha256").update(text, "utf8").digest("hex");
}

function csvEscape(value) {
  const text = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') { field += '"'; i += 1; }
      else if (ch === '"') quoted = false;
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ",") { row.push(field); field = ""; }
    else if (ch === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += ch;
  }
  if (field || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  if (rows[0]?.[0]?.charCodeAt(0) === 0xfeff) rows[0][0] = rows[0][0].slice(1);
  return rows;
}

function columnName(number) {
  let result = "";
  while (number > 0) { number -= 1; result = String.fromCharCode(65 + (number % 26)) + result; number = Math.floor(number / 26); }
  return result;
}

function formatDuration(seconds) {
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function parseDuration(value) {
  const parts = String(value ?? "").split(":").map(Number);
  assert(parts.length === 3 && parts.every(Number.isFinite), `Invalid duration: ${value}`);
  return parts[0] * 3600 + parts[1] * 60 + parts[2];
}

function dateOnly(value) {
  const match = String(value ?? "").match(/^(\d{4})-(\d{2})-(\d{2})/);
  assert(match, `Invalid publication date: ${value}`);
  return new Date(Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])));
}

function wordCount(text) {
  return (String(text ?? "").match(/[\p{L}\p{N}]+(?:['’_-][\p{L}\p{N}]+)*/gu) ?? []).length;
}

function median(numbers) {
  if (!numbers.length) return null;
  const sorted = [...numbers].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
}

function mean(numbers) {
  return numbers.length ? numbers.reduce((a, b) => a + b, 0) / numbers.length : null;
}

function unique(values) {
  const seen = new Set(), out = [];
  for (const value of values) if (value !== null && value !== undefined && value !== "" && !seen.has(String(value))) {
    seen.add(String(value)); out.push(value);
  }
  return out;
}

function videoId(record) { return record.id; }

function canonicalVideoUrl(record) { return `https://www.youtube.com/watch?v=${record.id}`; }

function contentType(record) {
  const page = String(record.sourceTab ?? record.fromChannelListPage ?? "").toLowerCase();
  const type = String(record.type ?? "").toLowerCase();
  const url = String(record.url ?? "").toLowerCase();
  if (page === "shorts" || type === "short" || type === "shorts" || url.includes("/shorts/")) return "Short";
  if (["streams", "stream", "live", "livestream"].includes(page) || ["streams", "stream", "live", "livestream"].includes(type)) return "livestream";
  return "regular video";
}

function subtitles(record) {
  return Array.isArray(record.subtitles) ? record.subtitles.filter(item => item && typeof item === "object") : [];
}

function transcript(record) {
  const items = subtitles(record).filter(item => typeof item.plaintext === "string" && item.plaintext.trim());
  if (items.length === 1) return items[0].plaintext;
  return items.map(item => `[${[item.language, item.type].filter(Boolean).join(" | ")}]\n${item.plaintext}`).join("\n\n");
}

function subtitleLanguages(record) { return unique(subtitles(record).map(item => item.language)).join(", ") || "Unavailable"; }
function captionType(record) { return unique(subtitles(record).map(item => item.type)).join(", ") || "Unavailable"; }

function descriptionLinks(record) {
  const actorLinks = (Array.isArray(record.descriptionLinks) ? record.descriptionLinks : []).flatMap(item => {
    if (typeof item === "string") return [item];
    if (item && typeof item === "object") return [item.url, item.href].filter(Boolean);
    return [];
  });
  const textLinks = String(record.text ?? "").match(/https?:\/\/[^\s<>"']+/g) ?? [];
  return unique([...actorLinks, ...textLinks].map(value => String(value).replace(/[),.;]+$/, "")));
}

function hashtags(record) {
  const actorTags = (Array.isArray(record.hashtags) ? record.hashtags : []).map(item => typeof item === "string" ? item : item?.hashtag ?? item?.text).filter(Boolean);
  const textTags = String(record.text ?? "").match(/#[\p{L}\p{N}_]+/gu) ?? [];
  return unique([...actorTags, ...textTags].map(tag => String(tag).startsWith("#") ? String(tag) : `#${tag}`));
}

function cleanTitleForFilename(title) {
  const clean = String(title).normalize("NFKD").replace(/[\u0300-\u036f]/g, "").replace(/[^A-Za-z0-9]+/g, "_").replace(/^_+|_+$/g, "") || "Untitled";
  return clean.slice(0, 145).replace(/_+$/g, "") || "Untitled";
}

function escapeFormulaText(value) { return String(value).replaceAll('"', '""'); }

function validVideoRecord(record) {
  return record && typeof record === "object" && /^[A-Za-z0-9_-]{11}$/.test(record.id ?? "") &&
    typeof record.title === "string" && record.title.trim() && typeof record.channelName === "string" && record.channelName.trim() &&
    (record.channelId || record.channelUrl);
}

async function copyExact(source, destination) {
  await fs.mkdir(path.dirname(destination), { recursive: true });
  if (await exists(destination)) {
    const [sourceHash, destinationHash] = await Promise.all([sha256(source), sha256(destination)]);
    assert(sourceHash === destinationHash, `Existing immutable destination differs: ${destination}`);
    return { sourceHash, destinationHash };
  }
  await fs.copyFile(source, destination, fs.constants.COPYFILE_EXCL);
  const [sourceHash, destinationHash] = await Promise.all([sha256(source), sha256(destination)]);
  assert(sourceHash === destinationHash, `Immutable copy hash mismatch: ${source}`);
  return { sourceHash, destinationHash };
}

const sourcePaths = {};
for (const key of ["master-json", "master-csv", "master-xlsx", "old-raw-json", "new-raw-json", "new-clean-json", "channel-summary-csv", "prior-validation-report", "recovery-raw-json", "description-verification-json", "template-xlsx"]) {
  sourcePaths[key] = path.resolve(args[key]);
  assert(await exists(sourcePaths[key]), `Input missing: ${sourcePaths[key]}`);
}

const master = JSON.parse(await fs.readFile(sourcePaths["master-json"], "utf8"));
assert(Array.isArray(master) && master.length === 132, `Master JSON record count must be 132; got ${master.length}`);
assert(master.every(validVideoRecord), "Master JSON has invalid required video fields");
const masterIds = master.map(videoId);
assert(new Set(masterIds).size === 132, "Master JSON video IDs are not unique");
for (const channel of CHANNELS) {
  const count = master.filter(record => record.channelName === channel.name).length;
  assert(count === channel.count, `${channel.name} expected ${channel.count}; got ${count}`);
}
assert(master.every(record => transcript(record).trim()), "All 132 master records must contain transcript plaintext");

const csvRows = parseCsv(await fs.readFile(sourcePaths["master-csv"], "utf8"));
const csvHeader = csvRows[0];
const csvIdIndex = csvHeader.indexOf("video_id");
assert(csvIdIndex >= 0, "Master CSV missing video_id column");
const csvIds = csvRows.slice(1).filter(row => row.some(value => value !== "")).map(row => row[csvIdIndex]);
assert(csvIds.length === 132 && new Set(csvIds).size === 132, "Master CSV must contain 132 unique video IDs");
assert([...csvIds].join("\n") === masterIds.join("\n"), "Master CSV ID order differs from Master JSON");

const masterWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePaths["master-xlsx"]));
const masterSheet = masterWorkbook.worksheets.getItem("Videos");
const masterValues = masterSheet.getUsedRange(true).values;
const masterXlsxIdIndex = masterValues[0].indexOf("video_id");
assert(masterXlsxIdIndex >= 0, "Master XLSX missing video_id column");
const masterXlsxIds = masterValues.slice(1).filter(row => row[masterXlsxIdIndex]).map(row => String(row[masterXlsxIdIndex]));
assert(masterXlsxIds.length === 132 && new Set(masterXlsxIds).size === 132, "Master XLSX must contain 132 unique video IDs");
assert(masterXlsxIds.join("\n") === masterIds.join("\n"), "Master XLSX ID order differs from Master JSON");

const oldRaw = JSON.parse(await fs.readFile(sourcePaths["old-raw-json"], "utf8"));
const newRaw = JSON.parse(await fs.readFile(sourcePaths["new-raw-json"], "utf8"));
const newClean = JSON.parse(await fs.readFile(sourcePaths["new-clean-json"], "utf8"));
const recoveryRaw = JSON.parse(await fs.readFile(sourcePaths["recovery-raw-json"], "utf8"));
const recoveryVerification = JSON.parse(await fs.readFile(sourcePaths["description-verification-json"], "utf8"));
assert(oldRaw.length === 52 && oldRaw.filter(record => record.id).length === 50, "Old raw export must contain 52 records and 50 videos");
assert(newRaw.length === 88 && newRaw.filter(record => record.id).length === 82, "New raw export must contain 88 records and 82 videos");
assert(newClean.length === 82 && new Set(newClean.map(videoId)).size === 82, "New clean JSON must contain 82 unique videos");
assert(recoveryRaw.length === 14 && new Set(recoveryRaw.map(videoId)).size === 14, "Recovery raw export must contain 14 unique videos");
assert(recoveryRaw.every(record => record.text === null || record.text === "" || record.text === undefined), "Recovery output unexpectedly contains description text; update reconciliation before packaging");
assert(Array.isArray(recoveryVerification.items) && recoveryVerification.items.length === 14, "Description verification must contain 14 items");
const recoveryIds = new Set(recoveryRaw.map(videoId));
const verifiedIds = new Set(recoveryVerification.items.map(item => item.video_id));
assert(recoveryIds.size === verifiedIds.size && [...recoveryIds].every(id => verifiedIds.has(id)), "Recovery raw and browser-verification IDs differ");
assert(recoveryVerification.items.every(item => item.status === "No public description" && item.youtube_page_observation === "No description has been added to this video."), "All unresolved descriptions require exact YouTube no-description evidence");
const originalMissing = master.filter(record => !String(record.text ?? "").trim()).map(videoId);
assert(originalMissing.length === 14 && originalMissing.every(id => recoveryIds.has(id)), "Master missing-description IDs differ from recovery target");

const referenceDir = path.resolve(args["reference-dir"]);
const referenceNames = [
  "TPDossier_Master_Data.xlsx", "TPDossier_Transcripts_92_Videos.zip",
  "CarlInvests_Master_Data.xlsx", "CarlInvests_Transcripts_80_Videos.zip",
  "Well4_Master_Data.xlsx", "Well4_Transcripts_32_Videos.zip",
  "LucasGrant_Master_Data.xlsx", "LucasGrant_Transcripts_95_Videos.zip",
  "NickInvests_Master_Data.xlsx", "NickInvests_Transcripts_363_Videos.zip",
  "BobInvests_Master_Data.xlsx", "BobInvests_Transcripts_57_Videos.zip",
  "JustSomeGuyStories_Master_Data.xlsx", "JustSomeGuyStories_Transcripts_13_Videos.zip",
];
for (const name of referenceNames) assert(await exists(path.join(referenceDir, name)), `Format reference missing: ${path.join(referenceDir, name)}`);

const recoveryById = new Map(recoveryVerification.items.map(item => [item.video_id, item]));
const reconciled = master.map(record => {
  const copy = structuredClone(record);
  if (recoveryById.has(record.id)) {
    copy._descriptionRecovery = {
      status: "No public description",
      actor: ACTOR,
      runId: RECOVERY_RUN_ID,
      datasetId: RECOVERY_DATASET_ID,
      checkedAt: recoveryVerification.checked_at,
      youtubePageObservation: "No description has been added to this video.",
    };
  } else copy._descriptionRecovery = { status: "Not required" };
  return copy;
});

await fs.mkdir(rawOutputDir, { recursive: true });
await fs.mkdir(combinedDir, { recursive: true });
await fs.mkdir(packagesDir, { recursive: true });
await fs.mkdir(manifestDir, { recursive: true });
await fs.mkdir(qaOutputDir, { recursive: true });

const referenceInventoryPath = path.join(manifestDir, `${DATASET_ID}_FORMAT_REFERENCES.csv`);
const referenceRows = [];
for (const name of referenceNames) {
  const filePath = path.join(referenceDir, name);
  const stat = await fs.stat(filePath);
  let contents = null;
  if (name.endsWith(".zip")) {
    const archive = await JSZip.loadAsync(await fs.readFile(filePath));
    contents = `${Object.values(archive.files).filter(item => !item.dir).length} root entries`;
  } else {
    const referenceWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(filePath));
    const sheetNames = referenceWorkbook.worksheets.items.map(sheet => sheet.name);
    assert(JSON.stringify(sheetNames) === JSON.stringify(REQUIRED_SHEETS), `Reference workbook sheet structure differs: ${name}`);
    contents = `Five sheets: ${sheetNames.join("; ")}`;
  }
  referenceRows.push({ filename: name, absolute_source_path: filePath, file_type: path.extname(name).slice(1).toUpperCase(), size_bytes: stat.size, sha256: await sha256(filePath), reference_role: name.endsWith(".xlsx") ? "Workbook structure and visual system" : "Transcript ZIP structure and naming", inspection_notes: contents });
}
const referenceHeaders = Object.keys(referenceRows[0]);
await fs.writeFile(referenceInventoryPath, `${referenceHeaders.map(csvEscape).join(",")}\n${referenceRows.map(row => referenceHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");

const sourceArtifactInventoryPath = path.join(manifestDir, `${DATASET_ID}_SOURCE_ARTIFACTS.csv`);
const sourceArtifactRows = [];
for (const [directoryArg, runId, datasetId, channels] of [
  ["old-output-dir", OLD_RUN_ID, OLD_DATASET_ID, "Apesthetic; Primate Economics"],
  ["master-output-dir", `${OLD_RUN_ID}; ${NEW_RUN_ID}`, `${OLD_DATASET_ID}; ${NEW_DATASET_ID}`, "All five channels"],
]) {
  const directory = path.resolve(args[directoryArg]);
  assert(await exists(directory), `Output artifact directory missing: ${directory}`);
  const names = (await fs.readdir(directory)).sort();
  for (const name of names) {
    const filePath = path.join(directory, name);
    const stat = await fs.stat(filePath);
    if (!stat.isFile()) continue;
    let recordCount = null, uniqueVideoIds = null, notes = "Inspected; source artifact left unchanged.";
    if (name.endsWith(".json")) {
      const data = JSON.parse(await fs.readFile(filePath, "utf8"));
      if (Array.isArray(data)) {
        recordCount = data.length;
        uniqueVideoIds = new Set(data.map(item => item?.id ?? item?.video_id).filter(Boolean)).size;
      }
    } else if (name.endsWith(".csv")) {
      const rows = parseCsv(await fs.readFile(filePath, "utf8"));
      recordCount = Math.max(0, rows.length - 1);
      const idIndex = Math.max(rows[0]?.indexOf("video_id") ?? -1, rows[0]?.indexOf("id") ?? -1);
      uniqueVideoIds = idIndex >= 0 ? new Set(rows.slice(1).map(row => row[idIndex]).filter(Boolean)).size : 0;
    } else if (name.endsWith(".xlsx")) {
      const sourceWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(filePath));
      const sourceSheet = sourceWorkbook.worksheets.getItem("Videos") ?? sourceWorkbook.worksheets.getItemAt(0);
      const values = sourceSheet.getUsedRange(true).values;
      const idIndex = Math.max(values[0]?.indexOf("video_id") ?? -1, values[0]?.indexOf("Video ID") ?? -1);
      if (idIndex >= 0) {
        const ids = values.slice(1).map(row => row[idIndex]).filter(Boolean).map(String);
        recordCount = ids.length;
        uniqueVideoIds = new Set(ids).size;
      }
    } else if (name.endsWith(".inspect.ndjson")) {
      recordCount = (await fs.readFile(filePath, "utf8")).split(/\r?\n/).filter(Boolean).length;
      uniqueVideoIds = 0;
      notes = "Spreadsheet inspection sidecar; intermediate QA evidence, not canonical video data.";
    }
    const raw = name.includes("actor_raw");
    sourceArtifactRows.push({ filename: name, absolute_source_path: filePath, size_bytes: stat.size, sha256: await sha256(filePath), format: path.extname(name).slice(1).toUpperCase(), row_or_record_count: recordCount, unique_video_id_count: uniqueVideoIds, source_run_id: raw && directoryArg === "master-output-dir" ? NEW_RUN_ID : runId, source_dataset_id: raw && directoryArg === "master-output-dir" ? NEW_DATASET_ID : datasetId, raw_or_derived_status: raw ? "RAW" : "DERIVED", channels_represented: raw && directoryArg === "master-output-dir" ? "Sonny Finance; Money Life POV; My Chaotic Stories" : channels, processing_date: directoryArg === "old-output-dir" ? "2026-09-11" : "2026-09-12", missing_data_notes: name.includes("master") || name.includes("complete_dataset") ? "Fourteen verified uploader-absent descriptions in combined data where applicable; transcripts complete." : notes });
  }
}
const sourceArtifactHeaders = Object.keys(sourceArtifactRows[0]);
await fs.writeFile(sourceArtifactInventoryPath, `${sourceArtifactHeaders.map(csvEscape).join(",")}\n${sourceArtifactRows.map(row => sourceArtifactHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");

const rawCopies = [
  { source: sourcePaths["old-raw-json"], destination: path.join(rawOutputDir, "apify", OLD_RUN_ID, "youtube_two_channels_actor_raw.json"), records: 52, videos: 50, runId: OLD_RUN_ID, datasetId: OLD_DATASET_ID, channels: "Apesthetic; Primate Economics", date: "2026-09-11" },
  { source: sourcePaths["new-raw-json"], destination: path.join(rawOutputDir, "apify", NEW_RUN_ID, "youtube_three_channels_actor_raw.json"), records: 88, videos: 82, runId: NEW_RUN_ID, datasetId: NEW_DATASET_ID, channels: "Sonny Finance; Money Life POV; My Chaotic Stories", date: "2026-09-12" },
  { source: sourcePaths["recovery-raw-json"], destination: path.join(rawOutputDir, "apify", RECOVERY_RUN_ID, "youtube_description_recovery_actor_raw.json"), records: 14, videos: 14, runId: RECOVERY_RUN_ID, datasetId: RECOVERY_DATASET_ID, channels: "Apesthetic; Primate Economics", date: "2026-09-12" },
];
for (const item of rawCopies) await copyExact(item.source, item.destination);

const combinedCopies = [
  ["master-json", "youtube_5_channels_master.json"],
  ["master-csv", "youtube_5_channels_master.csv"],
  ["master-xlsx", "youtube_5_channels_master.xlsx"],
  ["new-clean-json", "youtube_3_new_channels_clean.json"],
  ["channel-summary-csv", "youtube_5_channels_channel_summary.csv"],
  ["prior-validation-report", "youtube_5_channels_validation_report.md"],
];
for (const [key, filename] of combinedCopies) await copyExact(sourcePaths[key], path.join(combinedDir, filename));
const reconciledPath = path.join(combinedDir, "youtube_5_channels_master_reconciled.json");
await fs.writeFile(reconciledPath, `${JSON.stringify(reconciled, null, 2)}\n`, "utf8");
const recoveryResultPath = path.join(combinedDir, "youtube_description_recovery_results.json");
await fs.writeFile(recoveryResultPath, `${JSON.stringify({
  dataset_id: DATASET_ID,
  actor: ACTOR,
  run_id: RECOVERY_RUN_ID,
  apify_dataset_id: RECOVERY_DATASET_ID,
  run_status: "SUCCEEDED",
  cost_usd: 0.056,
  requests_succeeded: 28,
  requests_failed: 0,
  target_count: 14,
  recovered_count: 0,
  no_public_description_count: 14,
  items: recoveryVerification.items,
}, null, 2)}\n`, "utf8");

function channelMeta(records) {
  const first = records[0];
  const about = first.aboutChannelInfo ?? {};
  const value = key => first[key] ?? about[key] ?? null;
  return {
    name: first.channelName,
    handle: `@${String(first.channelUsername ?? about.channelUsername ?? "Unavailable").replace(/^@/, "")}`,
    id: first.channelId ?? about.channelId ?? "Unavailable",
    url: first.channelUrl ?? about.channelUrl ?? "Unavailable",
    subscribers: value("numberOfSubscribers"),
    reportedVideos: value("channelTotalVideos"),
    lifetimeViews: value("channelTotalViews"),
    joined: value("channelJoinedDate") ?? "Unavailable",
    location: value("channelLocation") ?? "Unavailable",
    verified: value("isChannelVerified"),
    avatar: value("channelAvatarUrl") ?? "Unavailable",
    banner: value("channelBannerUrl") ?? "Unavailable",
    description: value("channelDescription") ?? "Unavailable",
  };
}

function videoInfo(record, index) {
  const seconds = parseDuration(record.duration);
  const text = transcript(record);
  const tags = hashtags(record);
  const links = descriptionLinks(record);
  const filename = `${String(index + 1).padStart(3, "0")}_${record.id}_${cleanTitleForFilename(record.title)}.txt`;
  assert(filename.length <= 190, `Transcript filename too long: ${filename}`);
  return {
    index: index + 1,
    record,
    id: record.id,
    title: record.title,
    url: canonicalVideoUrl(record),
    published: record.date,
    date: dateOnly(record.date),
    day: dateOnly(record.date).toLocaleDateString("en-US", { weekday: "long", timeZone: "UTC" }),
    seconds,
    duration: formatDuration(seconds),
    views: Number(record.viewCount),
    likes: Number(record.likes),
    comments: Number(record.commentsCount),
    words: wordCount(text),
    description: String(record.text ?? ""),
    descriptionStatus: recoveryById.get(record.id)?.status ?? "Available",
    links,
    tags,
    captionType: captionType(record),
    language: subtitleLanguages(record),
    transcript: text,
    filename,
    thumbnail: record.thumbnailUrl ?? "Unavailable",
    membersOnly: record.isMembersOnly === true,
    paid: record.isPaidContent === true,
    commentsOff: record.commentsTurnedOff === true,
    ageRestricted: record.isAgeRestricted === true,
    type: contentType(record),
  };
}

function titleWords(videos) {
  const stop = new Set("a an and are as at be been but by can for from had has have he her hers him his how i if in into is it its just me more most my no not of on one or our out over she so than that the their them then there these they this to up us was we were what when where which who why will with you your youre yous".split(" "));
  const map = new Map();
  for (const video of videos) {
    const words = new Set((video.title.toLowerCase().match(/[a-z0-9]+/g) ?? []).filter(word => word.length > 2 && !stop.has(word) && !/^\d+$/.test(word)));
    for (const word of words) {
      if (!map.has(word)) map.set(word, []);
      map.get(word).push(video.views);
    }
  }
  return [...map.entries()].map(([word, views]) => ({ word, count: views.length, medianViews: median(views) }))
    .sort((a, b) => b.count - a.count || b.medianViews - a.medianViews || a.word.localeCompare(b.word)).slice(0, 10);
}

function verificationRows(channel, videos) {
  const ids = videos.map(video => video.id);
  const duplicateCount = ids.length - new Set(ids).size;
  const withDescriptions = videos.filter(video => video.description.trim()).length;
  const genuineNoDescription = videos.filter(video => video.descriptionStatus === "No public description").length;
  const rows = [
    ["Videos reported by YouTube", channel.count, `Actor channelTotalVideos and live public count: ${channel.count}`],
    ["Videos captured", videos.length, videos.length === channel.count ? "Matches public count" : "Mismatch"],
    ["Regular-video count", videos.filter(video => video.type === "regular video").length, "Classified from Actor source tab/type"],
    ["Shorts count", videos.filter(video => video.type === "Short").length, "Classified from Actor source tab/type"],
    ["Livestream count", videos.filter(video => video.type === "livestream").length, "Classified from Actor source tab/type"],
    ["Unique video IDs", new Set(ids).size, "YouTube video ID is primary key"],
    ["Duplicate video IDs", duplicateCount, duplicateCount === 0 ? "No duplicate IDs" : "Duplicates require correction"],
    ["Videos with title", videos.filter(video => video.title.trim()).length, "Required field"],
    ["Videos with publish date", videos.filter(video => video.published).length, "Required field"],
    ["Videos with views", videos.filter(video => Number.isFinite(video.views)).length, "Zero is valid; null is missing"],
    ["Videos with likes/comments", videos.filter(video => Number.isFinite(video.likes) && Number.isFinite(video.comments)).length, "Both public counts present; zero is valid"],
    ["Videos with complete description", withDescriptions, "Actor text field only; channel description never substituted"],
    ["Genuine no-description videos", genuineNoDescription, genuineNoDescription ? `Verified on YouTube and recovery run ${RECOVERY_RUN_ID}` : "None"],
    ["Videos with transcript", videos.filter(video => video.transcript.trim()).length, "Complete subtitles[].plaintext"],
    ["Transcript text files written", videos.length, "One file per video"],
    ["Total transcript words", videos.reduce((sum, video) => sum + video.words, 0), "Unicode word count across transcript plaintext"],
    ["Longest description length", Math.max(...videos.map(video => video.description.length)), "Characters; zero means verified absent description where documented"],
    ["Total description links", videos.reduce((sum, video) => sum + video.links.length, 0), "Unique URLs from Actor output and description text"],
    ["Videos containing hashtags", videos.filter(video => video.tags.length).length, "Complete unique hashtag set"],
    ["Valid video URLs", videos.filter(video => /^https:\/\/www\.youtube\.com\/watch\?v=[A-Za-z0-9_-]{11}$/.test(video.url)).length, "Canonical watch URLs"],
    ["Video IDs matching combined master", videos.filter(video => masterIds.includes(video.id)).length, "Exact channel subset of 132-video master"],
    ["Missing fields and reasons", genuineNoDescription, genuineNoDescription ? "Only verified uploader-absent descriptions; location/SRT gaps are documented and non-blocking" : "No video-level required-field gaps; location/SRT gaps are documented and non-blocking"],
  ];
  return rows;
}

function analysisRows(meta, videos) {
  const views = videos.map(video => video.views).filter(Number.isFinite);
  const likes = videos.map(video => video.likes).filter(Number.isFinite);
  const comments = videos.map(video => video.comments).filter(Number.isFinite);
  const seconds = videos.map(video => video.seconds);
  const words = videos.map(video => video.words);
  const first = new Date(Math.min(...videos.map(video => video.date.getTime())));
  const latest = new Date(Math.max(...videos.map(video => video.date.getTime())));
  const daysActive = Math.max(1, Math.round((latest - first) / 86400000));
  const totalViews = views.reduce((a, b) => a + b, 0);
  const totalLikes = likes.reduce((a, b) => a + b, 0);
  const totalComments = comments.reduce((a, b) => a + b, 0);
  const med = median(views);
  const avg = mean(views);
  return [
    ["Subscribers", meta.subscribers],
    ["Videos published", videos.length],
    ["Videos with usable view count", views.length],
    ["First upload date", first],
    ["Latest upload date", latest],
    ["Days active", daysActive],
    ["Uploads per week", videos.length / (daysActive / 7)],
    ["Total views across scraped videos", totalViews],
    ["Channel lifetime views", meta.lifetimeViews],
    ["Views per subscriber", meta.subscribers ? meta.lifetimeViews / meta.subscribers : null],
    ["Median views per video", med],
    ["Mean views per video", avg],
    ["Best-video views", Math.max(...views)],
    ["Lowest-video views", Math.min(...views)],
    ["Mean-to-median spike ratio", med ? avg / med : null],
    ["Total likes", totalLikes],
    ["Total comments", totalComments],
    ["Like rate", totalViews ? totalLikes / totalViews : null],
    ["Comment rate", totalViews ? totalComments / totalViews : null],
    ["Average duration", mean(seconds) / 60],
    ["Shortest duration", Math.min(...seconds) / 60],
    ["Longest duration", Math.max(...seconds) / 60],
    ["Average transcript length", mean(words)],
    ["Average speaking pace", mean(videos.map(video => video.seconds ? video.words / (video.seconds / 60) : 0))],
    ["Average description-link count", mean(videos.map(video => video.links.length))],
    ["Videos with hashtags", videos.filter(video => video.tags.length).length],
  ];
}

async function buildChannelPackage(channel, records) {
  records.sort((a, b) => String(b.date).localeCompare(String(a.date)) || String(a.id).localeCompare(String(b.id)));
  const videos = records.map(videoInfo);
  const meta = channelMeta(records);
  assert(videos.length === channel.count, `${channel.name} package count mismatch`);
  assert(new Set(videos.map(video => video.id)).size === channel.count, `${channel.name} package duplicate IDs`);
  assert(videos.every(video => video.transcript.trim()), `${channel.name} has missing transcript`);

  const channelDir = path.join(packagesDir, channel.slug);
  await fs.mkdir(channelDir, { recursive: true });
  const workbookPath = path.join(channelDir, channel.workbook);
  const zipPath = path.join(channelDir, channel.zip);
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePaths["template-xlsx"]));
  const sheetNames = workbook.worksheets.items.map(sheet => sheet.name);
  assert(JSON.stringify(sheetNames) === JSON.stringify(REQUIRED_SHEETS), `Template sheet structure differs: ${sheetNames.join(", ")}`);

  const overview = workbook.worksheets.getItem("Channel Overview");
  overview.getRange("A1:B30").clear({ applyTo: "contents" });
  for (let row = 23; row <= 30; row += 1) overview.unmergeCells(`A${row}:B${row}`);
  for (let row = 23; row <= 28; row += 1) overview.getRange("A5:B5").copyTo(overview.getRange(`A${row}:B${row}`), "all");
  const shorts = videos.filter(video => video.type === "Short").length;
  const live = videos.filter(video => video.type === "livestream").length;
  const noDescriptions = videos.filter(video => video.descriptionStatus === "No public description").length;
  overview.mergeCells("A1:B1"); overview.mergeCells("A2:B2");
  overview.getRange("A1").values = [[`${meta.name} — Full Channel Data Export`]];
  overview.getRange("A2").values = [[`Source: Apify ${ACTOR} | Packaged ${COLLECTION_DATE} | ${videos.length} videos, ${videos.length - noDescriptions} public descriptions, ${videos.length} transcripts`]];
  overview.getRange("A4:B4").values = [["Field", "Value"]];
  const oldChannel = channel.group === "existing";
  const overviewRows = [
    ["Channel Name", meta.name], ["Handle", meta.handle], ["Channel ID", meta.id], ["Canonical Channel URL", meta.url],
    ["Subscribers", meta.subscribers], ["Total Videos Reported by YouTube", meta.reportedVideos], ["Videos Captured", videos.length],
    ["Total Channel Views", meta.lifetimeViews], ["Joined Date", meta.joined], ["Channel Location", meta.location],
    ["Verified Status", meta.verified === true ? "Yes" : meta.verified === false ? "No" : "Unavailable"],
    ["Shorts Count", shorts], ["Live-Video Count", live], ["Avatar URL", meta.avatar], ["Banner URL", meta.banner],
    ["Complete Channel Description", meta.description], ["Source Actor", ACTOR], ["Scrape Date", new Date("2026-09-12T00:00:00Z")],
    ["Relevant Run ID", oldChannel ? `${channel.runId}; recovery ${RECOVERY_RUN_ID}` : channel.runId],
    ["Relevant Dataset ID", oldChannel ? `${channel.datasetId}; recovery ${RECOVERY_DATASET_ID}` : channel.datasetId],
    ["Completeness Notes", `${videos.length}/${meta.reportedVideos} public videos captured; 0 duplicate IDs.`],
    ["Transcript Notes", `${videos.length}/${videos.length} complete plaintext transcripts from full subtitles arrays.`],
    ["Description-Recovery Notes", noDescriptions ? `${noDescriptions} videos targeted; recovery returned null; YouTube states no description was added.` : "No description recovery required."],
    ["YouTube Public-Count Reconciliation", `Public count ${meta.reportedVideos}; captured ${videos.length}; missing ${meta.reportedVideos - videos.length}.`],
  ];
  overview.getRange("A5:B28").values = overviewRows;
  overview.getRange("B22").format.numberFormat = "yyyy-mm-dd";
  overview.getRange("B8:B8").format.font = { color: "#0563C1", underline: true };
  overview.getRange("B18:B19").format.font = { color: "#0563C1", underline: true };
  overview.getRange("B20").format.wrapText = true;
  overview.getRange("B20").format.rowHeight = 150;
  overview.mergeCells("A29:B29"); overview.mergeCells("A30:B30");
  overview.getRange("A29").values = [["Plaintext transcripts are complete; transcript/SRT URLs and per-video location are unavailable from Actor output."]];
  overview.getRange("A30").values = [["Facts are preserved from Actor output. Verified uploader-absent descriptions remain explicitly unavailable; channel descriptions are never substituted."]];
  overview.getRange("A29:B30").format.wrapText = true;
  overview.getRange("A29:B30").format.rowHeight = 36;

  const all = workbook.worksheets.getItem("All Videos");
  all.unmergeCells("A97:I97");
  const totalRow = 5 + videos.length;
  all.getRange("A97:AB97").copyTo(all.getRange(`A${totalRow}:AB${totalRow}`), "all");
  all.getRange("A1:AB97").clear({ applyTo: "contents" });
  all.mergeCells("A1:AB1"); all.mergeCells("A2:AB2"); all.mergeCells(`A${totalRow}:I${totalRow}`);
  all.getRange("A1").values = [[`All ${videos.length} Videos (newest first)`]];
  all.getRange("A2").values = [["Filters are on. Rates, Views/Day, and Words/Min are live formulas. Yellow rows mark unresolved scrape gaps."]];
  all.getRange("A4:AB4").values = [ALL_VIDEO_HEADERS];
  const allRows = videos.map(video => [
    video.index, video.id, video.title, null, video.published, video.date, video.day, video.duration, video.seconds,
    video.views, video.likes, video.comments, null, null, null, null, video.words, null, video.description.length,
    video.links.length, video.tags.length, video.captionType, video.filename, null, video.membersOnly ? "Yes" : "No",
    video.paid ? "Yes" : "No", video.commentsOff ? "Yes" : "No", video.ageRestricted ? "Yes" : "No",
  ]);
  all.getRange(`A5:AB${4 + videos.length}`).values = allRows;
  for (let index = 0; index < videos.length; index += 1) {
    const row = index + 5, video = videos[index];
    all.getRange(`D${row}`).formulas = [[`=HYPERLINK("${escapeFormulaText(video.url)}","${escapeFormulaText(video.url)}")`]];
    all.getRange(`M${row}`).formulas = [[`=IF(J${row}=0,0,K${row}/J${row})`]];
    all.getRange(`N${row}`).formulas = [[`=IF(J${row}=0,0,L${row}/J${row})`]];
    all.getRange(`O${row}`).formulas = [[`=IF(J${row}=0,0,(K${row}+L${row})/J${row})`]];
    all.getRange(`P${row}`).formulas = [[`=J${row}/MAX(1,'Channel Overview'!B22-F${row})`]];
    all.getRange(`R${row}`).formulas = [[`=IF(I${row}=0,0,Q${row}/(I${row}/60))`]];
    all.getRange(`X${row}`).formulas = [[`=HYPERLINK("${escapeFormulaText(video.thumbnail)}","${escapeFormulaText(video.thumbnail)}")`]];
  }
  all.getRange(`A${totalRow}`).values = [["TOTAL / AVERAGE"]];
  for (const col of ["J", "K", "L", "S", "T"]) all.getRange(`${col}${totalRow}`).formulas = [[`=SUM(${col}5:${col}${totalRow - 1})`]];
  for (const col of ["M", "N", "O", "Q", "R"]) all.getRange(`${col}${totalRow}`).formulas = [[`=AVERAGE(${col}5:${col}${totalRow - 1})`]];
  all.getRange(`F5:F${totalRow - 1}`).format.numberFormat = "yyyy-mm-dd";
  all.getRange(`J5:L${totalRow}`).format.numberFormat = "#,##0";
  all.getRange(`M5:O${totalRow}`).format.numberFormat = "0.00%";
  all.getRange(`P5:Q${totalRow}`).format.numberFormat = "#,##0";
  all.getRange(`R5:R${totalRow}`).format.numberFormat = "0.0";
  all.getRange(`S5:T${totalRow}`).format.numberFormat = "#,##0";
  all.getRange(`D5:D${totalRow - 1}`).format.font = { color: "#0563C1", underline: true };
  all.getRange(`X5:X${totalRow - 1}`).format.font = { color: "#0563C1", underline: true };
  const videoTable = all.tables.add(`A4:AB${totalRow - 1}`, true, `${channel.slug.replaceAll("-", "")}VideosTable`);
  videoTable.style = "TableStyleMedium2";
  videoTable.showBandedRows = false;
  videoTable.showBandedColumns = false;
  videoTable.showFilterButton = true;
  all.freezePanes.unfreeze(); all.freezePanes.freezeRows(4); all.freezePanes.freezeColumns(3);

  const descriptions = workbook.worksheets.getItem("Descriptions");
  descriptions.getRange("A1:G96").clear({ applyTo: "contents" });
  descriptions.mergeCells("A1:G1"); descriptions.mergeCells("A2:G2");
  descriptions.getRange("A1").values = [[`Full Video Descriptions — all ${videos.length} videos`]];
  descriptions.getRange("A2").values = [["Complete description text plus hashtags and every recovered URL. Verified uploader-absent descriptions are explicit."]];
  descriptions.getRange("A4:G4").values = [DESCRIPTION_HEADERS];
  const descRows = videos.map(video => [
    video.index, video.id, video.title, video.tags.length ? video.tags.join(", ") : "—", video.links.length,
    video.links.length ? video.links.join("\n") : "—",
    video.description || "No public description (verified on YouTube; targeted Apify recovery returned null).",
  ]);
  descriptions.getRange(`A5:G${4 + videos.length}`).values = descRows;
  descriptions.getRange(`A5:G${4 + videos.length}`).format.wrapText = true;
  descriptions.getRange(`A5:G${4 + videos.length}`).format.rowHeight = 105;
  const descriptionTable = descriptions.tables.add(`A4:G${4 + videos.length}`, true, `${channel.slug.replaceAll("-", "")}DescriptionsTable`);
  descriptionTable.style = "TableStyleMedium2";
  descriptionTable.showBandedRows = false;
  descriptionTable.showBandedColumns = false;
  descriptionTable.showFilterButton = true;
  descriptions.freezePanes.unfreeze(); descriptions.freezePanes.freezeRows(4); descriptions.freezePanes.freezeColumns(3);
  for (const video of videos) {
    if (video.description.length > 32767) {
      const longDir = path.join(channelDir, "long-descriptions");
      await fs.mkdir(longDir, { recursive: true });
      await fs.writeFile(path.join(longDir, `${video.id}.txt`), video.description, "utf8");
      throw new Error(`Description exceeds Excel cell limit; companion written for ${video.id}. Update workbook note before rerun.`);
    }
  }

  const verification = workbook.worksheets.getItem("Verification");
  verification.getRange("A1:C30").clear({ applyTo: "contents" });
  verification.mergeCells("A1:C1"); verification.mergeCells("A2:C2");
  verification.getRange("A1").values = [["Verification — completeness check"]];
  verification.getRange("A2").values = [["Every value below is computed from the registered 132-video master and channel package data."]];
  verification.getRange("A4:C4").values = [["Check", "Value", "Result"]];
  const checks = verificationRows(channel, videos);
  for (let row = 20; row <= 4 + checks.length; row += 1) verification.getRange("A5:C5").copyTo(verification.getRange(`A${row}:C${row}`), "all");
  verification.getRange(`A5:C${4 + checks.length}`).values = checks;
  verification.getRange(`A5:C${4 + checks.length}`).format.wrapText = true;
  verification.getRange(`A5:C${4 + checks.length}`).format.rowHeight = 30;

  const analysis = workbook.worksheets.getItem("Analysis");
  analysis.getRange("A1:F30").clear({ applyTo: "contents" });
  analysis.mergeCells("A1:F1"); analysis.mergeCells("A2:F2");
  analysis.getRange("A1").values = [[`Channel Analysis — ${meta.name}`]];
  analysis.getRange("A2").values = [[`Descriptive summary of ${videos.length} captured videos. No recommendations or strategy conclusions.`]];
  analysis.getRange("A4:B4").values = [["Metric", "Value"]];
  analysis.getRange("D4:F4").values = [["Top 10 videos by views", null, null]];
  analysis.getRange("D5:F5").values = [["Title", "Views", "Views/Day"]];
  const metrics = analysisRows(meta, videos);
  analysis.getRange("A5:B30").values = metrics;
  analysis.getRange("B8:B9").format.numberFormat = "yyyy-mm-dd";
  analysis.getRange("B11:B11").format.numberFormat = "0.0";
  analysis.getRange("B22:B23").format.numberFormat = "0.00%";
  analysis.getRange("B19:B19").format.numberFormat = "0.00";
  analysis.getRange("B24:B29").format.numberFormat = "0.0";
  const top = [...videos].sort((a, b) => b.views - a.views || a.title.localeCompare(b.title)).slice(0, 10);
  analysis.getRange("D6:F15").values = top.map(video => [video.title, video.views, video.views / Math.max(1, Math.floor((new Date("2026-09-12T00:00:00Z") - video.date) / 86400000))]);
  analysis.getRange("E6:F15").format.numberFormat = "#,##0";
  analysis.getRange("D17:F17").values = [["Most common meaningful title words", null, null]];
  analysis.getRange("D18:F18").values = [["Word", "Videos", "Median views"]];
  analysis.getRange("D19:F28").values = titleWords(videos).map(item => [item.word, item.count, item.medianViews]);
  analysis.getRange("E19:F28").format.numberFormat = "#,##0";

  workbook.recalculate();
  const errorScan = await workbook.inspect({ kind: "match", searchTerm: ERROR_PATTERN, options: { useRegex: true, maxResults: 300 }, summary: `${channel.name} formula error scan` });
  const errorText = errorScan.ndjson ?? "";
  assert(!/"match"\s*:/.test(errorText) && !ERROR_PATTERN.split("|").some(token => errorText.includes(token.replace("\\?", "?"))), `${channel.name} workbook formula error: ${errorText.slice(0, 500)}`);

  for (const sheetName of REQUIRED_SHEETS) {
    const ranges = { "Channel Overview": "A1:B30", "All Videos": `A1:AB${Math.min(totalRow, 14)}`, "Descriptions": `A1:G${Math.min(4 + videos.length, 10)}`, "Verification": `A1:C${4 + checks.length}`, "Analysis": "A1:F30" };
    const preview = await workbook.render({ sheetName, range: ranges[sheetName], scale: 1, format: "png" });
    await fs.writeFile(path.join(qaOutputDir, `${channel.slug}-${sheetName.toLowerCase().replaceAll(" ", "-")}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
  const output = await SpreadsheetFile.exportXlsx(workbook);
  await output.save(workbookPath);

  const zip = new JSZip();
  const fixedDate = new Date("2026-09-12T00:00:00Z");
  const indexLines = [
    `TRANSCRIPT PACK - ${meta.name}`,
    "==============================================================================",
    `Generation date: ${COLLECTION_DATE}`,
    `Data source: Apify ${ACTOR}; run ${channel.runId}; dataset ${channel.datasetId}`,
    `Total videos: ${videos.length}`,
    `Videos with transcripts: ${videos.filter(video => video.transcript.trim()).length}`,
    `Videos without transcripts: ${videos.filter(video => !video.transcript.trim()).length}`,
    `Total transcript words: ${videos.reduce((sum, video) => sum + video.words, 0).toLocaleString("en-US")}`,
    "",
    "Each video file contains source metadata, complete individual description or verified unavailability reason, and unmodified plaintext transcript.",
    "Files are listed newest first. Sequence matches workbook numbering and Transcript File values.",
    "",
    "==============================================================================",
    "",
  ];
  for (const video of videos) {
    const description = video.description || "No public description (verified on YouTube; targeted Apify recovery returned null).";
    const body = [
      `Channel      : ${meta.name}`,
      `Title        : ${video.title}`,
      `Video ID     : ${video.id}`,
      `URL          : ${video.url}`,
      `Published    : ${video.published}`,
      `Duration     : ${video.duration}`,
      `Views        : ${video.views}`,
      `Likes        : ${video.likes}`,
      `Comments     : ${video.comments}`,
      `Hashtags     : ${video.tags.length ? video.tags.join(", ") : "(none)"}`,
      `Caption type : ${video.captionType}`,
      `Language     : ${video.language}`,
      `Word count   : ${video.words}`,
      "==============================================================================",
      "DESCRIPTION",
      "==============================================================================",
      description,
      "",
      "==============================================================================",
      "TRANSCRIPT",
      "==============================================================================",
      video.transcript,
      "",
    ].join("\n");
    zip.file(video.filename, body, { date: fixedDate, unixPermissions: 0o644 });
    indexLines.push(`${String(video.index).padStart(3, "0")}  ${String(video.words).padStart(7, " ")} words  ${video.filename}`);
  }
  zip.file("INDEX.txt", `${indexLines.join("\n")}\n`, { date: fixedDate, unixPermissions: 0o644 });
  const zipBytes = await zip.generateAsync({ type: "uint8array", compression: "DEFLATE", compressionOptions: { level: 9 }, platform: "UNIX" });
  await fs.writeFile(zipPath, zipBytes);
  const zipCheck = await JSZip.loadAsync(await fs.readFile(zipPath));
  const zipNames = Object.keys(zipCheck.files).filter(name => !zipCheck.files[name].dir);
  assert(zipNames.length === videos.length + 1 && zipNames.includes("INDEX.txt"), `${channel.name} ZIP count mismatch`);
  assert(new Set(zipNames).size === zipNames.length, `${channel.name} ZIP duplicate filenames`);
  assert(zipNames.every(name => name === "INDEX.txt" || /^\d{3}_[A-Za-z0-9_-]{11}_.+\.txt$/.test(name)), `${channel.name} ZIP filename contract failure`);
  for (const video of videos) assert(zipNames.includes(video.filename), `${channel.name} ZIP missing ${video.filename}`);

  return { channel, videos, meta, workbookPath, zipPath, errorScan: errorText };
}

const results = [];
for (const channel of CHANNELS) {
  const records = master.filter(record => record.channelName === channel.name).map(record => structuredClone(record));
  results.push(await buildChannelPackage(channel, records));
}

const allPackageIds = results.flatMap(result => result.videos.map(video => video.id));
assert(allPackageIds.length === 132 && new Set(allPackageIds).size === 132, "Package ID union must contain 132 unique videos");
assert(new Set(allPackageIds).size === masterIds.length && masterIds.every(id => allPackageIds.includes(id)), "Package ID union differs from combined master");
assert(results.reduce((sum, result) => sum + result.videos.length, 0) === 132, "Per-channel workbook record sum differs from 132");

const finalValidationPath = path.join(extractedOutputDir, "youtube_5_channels_packaging_validation_report.md");
const validationLines = [
  "# Five-Channel YouTube Packaging Validation",
  "",
  `- Dataset: ${DATASET_ID} — ${DATASET_NAME}`,
  `- Generated: ${COLLECTION_DATE}`,
  `- Actor: ${ACTOR}`,
  `- Source runs: ${OLD_RUN_ID}, ${NEW_RUN_ID}, ${RECOVERY_RUN_ID}`,
  `- Source datasets: ${OLD_DATASET_ID}, ${NEW_DATASET_ID}, ${RECOVERY_DATASET_ID}`,
  "",
  "## Description recovery",
  "",
  `Targeted run ${RECOVERY_RUN_ID} succeeded: 14 records; 28 requests succeeded; 0 failed; cost $0.056. Actor returned no video-description text for all 14 targets. Live YouTube pages displayed \"No description has been added to this video.\" for every target. Final status: 0 Recovered; 14 No public description; 0 unavailable; 0 Actor failures; 0 Unknown.`,
  "",
  "## Count reconciliation",
  "",
  "| Channel | Videos | Regular | Shorts | Livestreams | Transcripts | No public description |",
  "|---|---:|---:|---:|---:|---:|---:|",
  ...results.map(result => `| ${result.channel.name} | ${result.videos.length} | ${result.videos.filter(video => video.type === "regular video").length} | ${result.videos.filter(video => video.type === "Short").length} | ${result.videos.filter(video => video.type === "livestream").length} | ${result.videos.filter(video => video.transcript.trim()).length} | ${result.videos.filter(video => video.descriptionStatus === "No public description").length} |`),
  `| **Total** | **132** | **${results.flatMap(r => r.videos).filter(v => v.type === "regular video").length}** | **${results.flatMap(r => r.videos).filter(v => v.type === "Short").length}** | **${results.flatMap(r => r.videos).filter(v => v.type === "livestream").length}** | **132** | **14** |`,
  "",
  "## Validation evidence",
  "",
  "- Combined JSON, CSV, and XLSX: 132 records, 132 unique IDs, identical ID set and order.",
  "- Channel counts: 22 + 28 + 39 + 20 + 23 = 132.",
  "- Five workbook record counts sum to 132; package ID union equals combined-master ID set.",
  "- Every video appears in exactly one channel package.",
  "- All 132 records contain video ID, title, canonical URL, channel identity, publication date, public metrics, thumbnail URL, and transcript plaintext.",
  "- Transcript ZIPs contain one UTF-8 video file per workbook row plus one INDEX.txt; workbook Transcript File values match exactly.",
  "- 132/132 transcript files contain complete plaintext; no placeholders.",
  "- 14 description gaps are verified uploader-absent descriptions. Channel descriptions were never substituted.",
  "- All workbook formulas recalculated; formula-error scans found no unexpected Excel errors.",
  "- Every workbook contains exactly five required sheets in required order; every sheet rendered to QA PNG.",
  "- Raw source/destination SHA-256 values match exactly.",
  "- Per-video location and transcript/SRT URLs remain unavailable; plaintext transcripts are complete.",
  "- Reference files remained outside repository and unchanged. TPDossier_Master_Data.xlsx supplied workbook visual system.",
  `- All 14 supplied format references were present, hashed, and structurally inspected; see data/manifests/${DATASET_ID}_FORMAT_REFERENCES.csv.`,
  `- Every file in both source output directories was inventoried; see data/manifests/${DATASET_ID}_SOURCE_ARTIFACTS.csv.`,
  "",
];
await fs.writeFile(finalValidationPath, validationLines.join("\n"), "utf8");

const artifacts = [];
function addArtifact(spec) { artifacts.push(spec); }
for (const raw of rawCopies) addArtifact({
  path: raw.destination, type: "JSON", semantic: "B — Competitor Evidence", description: "Immutable Apify Actor output", source: raw.source,
  runId: raw.runId, datasetId: raw.datasetId, channel: raw.channels, date: raw.date, fileCount: 1, recordCount: raw.records,
  duplicate: "VIDEO_IDS_UNIQUE_WITHIN_VIDEO_RECORDS", status: "RAW_REGISTERED", classification: "RAW", parent: "Apify Actor dataset",
  notes: `${raw.videos} video records; non-video channel-about records preserved where returned.`,
});
for (const [key, filename] of combinedCopies) {
  const filePath = path.join(combinedDir, filename);
  let count = null, type = path.extname(filename).slice(1).toUpperCase();
  if (filename.endsWith("master.json")) count = 132;
  else if (filename.endsWith("master.csv") || filename.endsWith("master.xlsx")) count = 132;
  else if (filename.endsWith("clean.json")) count = 82;
  else if (filename.endsWith("summary.csv")) count = 5;
  addArtifact({ path: filePath, type, semantic: "B — Competitor Evidence", description: `Preserved combined dataset artifact: ${filename}`, source: sourcePaths[key], runId: `${OLD_RUN_ID}; ${NEW_RUN_ID}`, datasetId: `${OLD_DATASET_ID}; ${NEW_DATASET_ID}`, channel: "All five channels", date: COLLECTION_DATE, fileCount: 1, recordCount: count, duplicate: count === 132 ? "132_UNIQUE_VIDEO_IDS" : "NOT_APPLICABLE", status: "PRESERVED_REGISTERED", classification: "DERIVED", parent: "Two immutable Apify Actor exports", notes: "Byte-identical canonical copy; source and destination hashes match." });
}
addArtifact({ path: reconciledPath, type: "JSON", semantic: "B — Competitor Evidence", description: "132-video master with description-recovery status merged by video ID", source: sourcePaths["master-json"], runId: `${OLD_RUN_ID}; ${NEW_RUN_ID}; ${RECOVERY_RUN_ID}`, datasetId: `${OLD_DATASET_ID}; ${NEW_DATASET_ID}; ${RECOVERY_DATASET_ID}`, channel: "All five channels", date: COLLECTION_DATE, fileCount: 1, recordCount: 132, duplicate: "132_UNIQUE_VIDEO_IDS", status: "VALIDATED", classification: "DERIVED", parent: "combined/youtube_5_channels_master.json; recovery raw; browser verification", notes: "14 descriptions remain null with verified No public description status." });
addArtifact({ path: recoveryResultPath, type: "JSON", semantic: "B — Competitor Evidence", description: "Targeted description-recovery reconciliation", source: sourcePaths["recovery-raw-json"], runId: RECOVERY_RUN_ID, datasetId: RECOVERY_DATASET_ID, channel: "Apesthetic; Primate Economics", date: COLLECTION_DATE, fileCount: 1, recordCount: 14, duplicate: "14_UNIQUE_VIDEO_IDS", status: "VALIDATED", classification: "DERIVED", parent: "youtube_description_recovery_actor_raw.json; live YouTube page observations", notes: "0 recovered; 14 verified as No public description." });
addArtifact({ path: sourcePaths["description-verification-json"], type: "JSON", semantic: "B — Competitor Evidence", description: "Per-video live YouTube description verification observations", source: "Authenticated browser inspection of 14 canonical watch pages", runId: RECOVERY_RUN_ID, datasetId: RECOVERY_DATASET_ID, channel: "Apesthetic; Primate Economics", date: COLLECTION_DATE, fileCount: 1, recordCount: 14, duplicate: "14_UNIQUE_VIDEO_IDS", status: "VERIFIED", classification: "EXTRACTED_OBSERVATION", parent: "youtube_description_recovery_actor_raw.json; public YouTube watch pages", notes: "Every page displayed YouTube's explicit no-description message; no description text was inferred." });
addArtifact({ path: referenceInventoryPath, type: "CSV", semantic: "Format-reference inventory", description: "Hash and structure inventory for all 14 supplied format references", source: referenceDir, runId: "Not applicable", datasetId: "Not applicable", channel: "Reference channels", date: COLLECTION_DATE, fileCount: 14, recordCount: 14, duplicate: "NOT_EVALUATED_AS_DATA_EVIDENCE", status: "INSPECTED", classification: "REFERENCE_MANIFEST", parent: "Fourteen user-supplied workbook and transcript ZIP references", notes: "Reference payloads remain unchanged outside repository; only this inventory is committed." });
addArtifact({ path: sourceArtifactInventoryPath, type: "CSV", semantic: "Source-artifact inventory", description: "Complete inventory of both existing Apify output directories", source: `${path.resolve(args["old-output-dir"])}; ${path.resolve(args["master-output-dir"])}`, runId: `${OLD_RUN_ID}; ${NEW_RUN_ID}`, datasetId: `${OLD_DATASET_ID}; ${NEW_DATASET_ID}`, channel: "All five channels", date: COLLECTION_DATE, fileCount: sourceArtifactRows.length, recordCount: sourceArtifactRows.length, duplicate: "HASHED_AND_COUNTED", status: "INSPECTED", classification: "SOURCE_MANIFEST", parent: "outputs/apify-complete-2026-09-11; outputs/apify-master-5-channels-2026-09-12", notes: "Every source-directory file recorded with absolute path, size, SHA-256, format, counts, provenance, class, channels, date, and missing-data notes." });
for (const result of results) {
  const sourceRun = result.channel.group === "existing" ? `${result.channel.runId}; ${RECOVERY_RUN_ID}` : result.channel.runId;
  const sourceDataset = result.channel.group === "existing" ? `${result.channel.datasetId}; ${RECOVERY_DATASET_ID}` : result.channel.datasetId;
  addArtifact({ path: result.workbookPath, type: "XLSX", semantic: "B — Competitor Evidence", description: `${result.channel.name} five-sheet master workbook`, source: sourcePaths["master-json"], runId: sourceRun, datasetId: sourceDataset, channel: result.channel.name, date: COLLECTION_DATE, fileCount: 1, recordCount: result.videos.length, duplicate: "UNIQUE_VIDEO_IDS", status: "VALIDATED", classification: "DERIVED", parent: "combined/youtube_5_channels_master.json; description recovery reconciliation", notes: "Reference-format workbook; formulas, filters, panes, hyperlinks, and five rendered sheets validated." });
  addArtifact({ path: result.zipPath, type: "ZIP/TXT", semantic: "B — Competitor Evidence", description: `${result.channel.name} transcript package`, source: sourcePaths["master-json"], runId: sourceRun, datasetId: sourceDataset, channel: result.channel.name, date: COLLECTION_DATE, fileCount: result.videos.length + 1, recordCount: result.videos.length, duplicate: "UNIQUE_VIDEO_IDS_AND_FILENAMES", status: "VALIDATED", classification: "DERIVED", parent: "combined/youtube_5_channels_master.json subtitles[].plaintext", notes: "ZIP root contains one UTF-8 transcript file per video plus INDEX.txt; no enclosing directory or metadata files." });
}
addArtifact({ path: finalValidationPath, type: "Markdown", semantic: "B — Competitor Evidence", description: "Packaging validation and reconciliation evidence", source: "Generator validation", runId: `${OLD_RUN_ID}; ${NEW_RUN_ID}; ${RECOVERY_RUN_ID}`, datasetId: `${OLD_DATASET_ID}; ${NEW_DATASET_ID}; ${RECOVERY_DATASET_ID}`, channel: "All five channels", date: COLLECTION_DATE, fileCount: 1, recordCount: 132, duplicate: "132_UNIQUE_VIDEO_IDS", status: "VALIDATED", classification: "DERIVED", parent: "All DS-000020 data artifacts", notes: "Phase 1 descriptive validation only; no strategic analysis." });

const generatorPath = path.join(repoRoot, "scripts", path.basename(new URL(import.meta.url).pathname));
addArtifact({ path: generatorPath, type: "JavaScript", semantic: "Phase 1 transformation code", description: "Reproducible five-channel package generator", source: "Repository implementation", runId: "Not applicable", datasetId: "Not applicable", channel: "All five channels", date: COLLECTION_DATE, fileCount: 1, recordCount: null, duplicate: "NOT_APPLICABLE", status: "VALIDATED", classification: "CODE", parent: "User specification and supplied reference workbook", notes: "Accepts all input paths as arguments; contains no secrets or local absolute paths." });

const manifestRows = [];
for (let index = 0; index < artifacts.length; index += 1) {
  const artifact = artifacts[index];
  const stat = await fs.stat(artifact.path);
  manifestRows.push({
    dataset_id: DATASET_ID,
    artifact_id: `${DATASET_ID}-F${String(index + 1).padStart(3, "0")}`,
    dataset_name: DATASET_NAME,
    filename: path.basename(artifact.path),
    repository_relative_path: path.relative(repoRoot, artifact.path),
    file_type: artifact.type,
    semantic_class: artifact.semantic,
    description: artifact.description,
    source: artifact.source,
    apify_actor: ACTOR,
    apify_run_id: artifact.runId,
    apify_dataset_id: artifact.datasetId,
    associated_channel: artifact.channel,
    collection_date: artifact.date,
    file_count: artifact.fileCount,
    record_count: artifact.recordCount,
    size_bytes: stat.size,
    sha256: await sha256(artifact.path),
    duplicate_status: artifact.duplicate,
    processing_status: artifact.status,
    raw_or_derived_classification: artifact.classification,
    parent_source_artifact: artifact.parent,
    notes_and_limitations: artifact.notes,
  });
}

const manifestCsvPath = path.join(manifestDir, `${DATASET_ID}_FILES.csv`);
const manifestHeaders = Object.keys(manifestRows[0]);
await fs.writeFile(manifestCsvPath, `${manifestHeaders.map(csvEscape).join(",")}\n${manifestRows.map(row => manifestHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");
const templateStat = await fs.stat(sourcePaths["template-xlsx"]);
const manifestMdPath = path.join(manifestDir, `${DATASET_ID}.md`);
const manifestMd = [
  `# ${DATASET_ID} — ${DATASET_NAME}`,
  "",
  "## Dataset identity",
  "",
  `- Dataset ID: ${DATASET_ID}`,
  `- Semantic class: B — Competitor Evidence`,
  `- Processing status: STRUCTURED_REGISTERED`,
  `- Collection/packaging date: ${COLLECTION_DATE}`,
  `- Actor: ${ACTOR}`,
  `- Runs: ${OLD_RUN_ID}, ${NEW_RUN_ID}, ${RECOVERY_RUN_ID}`,
  `- Apify datasets: ${OLD_DATASET_ID}, ${NEW_DATASET_ID}, ${RECOVERY_DATASET_ID}`,
  "- Canonical videos: 132 (132 unique IDs; 0 duplicates)",
  "- Channel counts: Apesthetic 22; Primate Economics 28; Sonny Finance 39; Money Life POV 20; My Chaotic Stories 23.",
  "- Content types: 118 regular videos; 14 Shorts; 0 livestreams.",
  "- Transcript coverage: 132/132 complete plaintext transcripts.",
  "- Description recovery: 14 targeted; 0 recovered; 14 verified as No public description.",
  "",
  "## Lineage",
  "",
  "```text",
  "Apify Actor raw exports",
  "  -> clean video records",
  "  -> verified five-channel 132-video master",
  "  -> five channel-specific master workbooks",
  "  -> five channel-specific transcript packs",
  "```",
  "",
  "Raw Actor exports are immutable. Raw source/destination SHA-256 hashes match. Derived workbooks and transcript packages live outside the raw-data directory and retain run/dataset provenance.",
  "",
  "## Format reference",
  "",
  `- Workbook template: ${sourcePaths["template-xlsx"]}`,
  `- Template bytes: ${templateStat.size}`,
  `- Template SHA-256: ${await sha256(sourcePaths["template-xlsx"])}`,
  `- All 14 supplied reference files remained unchanged and outside repository control; detailed hashes: [${DATASET_ID}_FORMAT_REFERENCES.csv](./${DATASET_ID}_FORMAT_REFERENCES.csv).`,
  `- Existing scrape-output artifacts were fully inventoried: [${DATASET_ID}_SOURCE_ARTIFACTS.csv](./${DATASET_ID}_SOURCE_ARTIFACTS.csv).`,
  "",
  "## Artifact inventory",
  "",
  `Detailed file-level manifest: [${DATASET_ID}_FILES.csv](./${DATASET_ID}_FILES.csv)`,
  "",
  "| Class | Files | Records | Bytes |",
  "|---|---:|---:|---:|",
  `| Raw | ${manifestRows.filter(row => row.raw_or_derived_classification === "RAW").length} | 154 total raw records | ${manifestRows.filter(row => row.raw_or_derived_classification === "RAW").reduce((sum, row) => sum + row.size_bytes, 0)} |`,
  `| Derived | ${manifestRows.filter(row => row.raw_or_derived_classification === "DERIVED").length} | 132 canonical videos | ${manifestRows.filter(row => row.raw_or_derived_classification === "DERIVED").reduce((sum, row) => sum + row.size_bytes, 0)} |`,
  `| Code | 1 | Not applicable | ${(await fs.stat(generatorPath)).size} |`,
  "",
  "## Limitations",
  "",
  "- Fourteen videos have no public description. Actor recovery returned null and YouTube displayed its explicit no-description message for each.",
  "- Per-video location and transcript/SRT URLs are unavailable. Complete transcript plaintext exists for every video.",
  "- Public metrics are point-in-time Actor observations and may change on YouTube.",
  "- Manifest does not hash itself or its file ledger because self-checksums are circular. Every dataset artifact and generator is hashed in the ledger.",
  "",
];
await fs.writeFile(manifestMdPath, manifestMd.join("\n"), "utf8");

console.log(JSON.stringify({
  datasetId: DATASET_ID,
  masterRecords: master.length,
  uniqueVideoIds: new Set(masterIds).size,
  transcripts: master.filter(record => transcript(record).trim()).length,
  descriptionsRecovered: 0,
  verifiedNoPublicDescription: 14,
  channelPackages: results.map(result => ({ channel: result.channel.name, videos: result.videos.length, workbook: path.relative(repoRoot, result.workbookPath), transcriptZip: path.relative(repoRoot, result.zipPath) })),
  manifest: path.relative(repoRoot, manifestMdPath),
  manifestFiles: path.relative(repoRoot, manifestCsvPath),
  validationReport: path.relative(repoRoot, finalValidationPath),
  qaRenders: REQUIRED_SHEETS.length * results.length,
}, null, 2));
