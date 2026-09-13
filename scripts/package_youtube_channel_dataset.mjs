#!/usr/bin/env node
/** Build and validate canonical YouTube data packages for any channel count. */

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import crypto from "node:crypto";
import { pathToFileURL } from "node:url";

let DATASET_ID;
let DATASET_NAME;
let ACTOR;
let COLLECTION_DATE;
let RUN_ID;
let APIFY_DATASET_ID;
let RECOVERY_RUN_ID = "Not applicable";
let RECOVERY_DATASET_ID = "Not applicable";
let CHANNELS = [];
let TOTAL_VIDEOS = 0;

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
    if (["--help", "--validate-config-only", "--validate-record-merge-only"].includes(token)) args[token.slice(2)] = true;
    else if (token.startsWith("--")) {
      const key = token.slice(2);
      if (!argv[index + 1] || argv[index + 1].startsWith("--")) throw new Error(`Missing value for ${token}`);
      args[key] = argv[index + 1];
      index += 1;
    } else throw new Error(`Unexpected argument: ${token}`);
  }
  return args;
}

function slugify(value) {
  return String(value).normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[^A-Za-z0-9]+/g, "-").replace(/^-+|-+$/g, "").toLowerCase();
}

function safeChannelName(value) {
  return String(value).normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[^A-Za-z0-9]+/g, " ").trim().split(/\s+/).join("") || "Channel";
}

function normalizeConfig(config) {
  if (!config || typeof config !== "object") throw new Error("Config must be a JSON object");
  for (const key of ["datasetId", "datasetName", "collectionDate", "actor", "run", "channels"]) {
    if (config[key] === undefined || config[key] === null) throw new Error(`Config missing ${key}`);
  }
  if (!Array.isArray(config.channels) || config.channels.length === 0) throw new Error("Config channels must be non-empty");
  const ids = new Set();
  const handles = new Set();
  const channels = config.channels.map((channel, index) => {
    for (const key of ["name", "handle", "channelId", "expectedCount"]) {
      if (channel[key] === undefined || channel[key] === null || channel[key] === "") throw new Error(`Channel ${index + 1} missing ${key}`);
    }
    const id = String(channel.channelId);
    const handle = `@${String(channel.handle).replace(/^@/, "")}`;
    if (ids.has(id)) throw new Error(`Duplicate channel ID: ${id}`);
    if (handles.has(handle.toLowerCase())) throw new Error(`Duplicate channel handle: ${handle}`);
    ids.add(id);
    handles.add(handle.toLowerCase());
    const count = Number(channel.expectedCount);
    if (!Number.isInteger(count) || count < 0) throw new Error(`Invalid expectedCount for ${channel.name}`);
    const safeName = safeChannelName(channel.name);
    return {
      ...channel,
      handle,
      channelId: id,
      expectedCount: count,
      count,
      slug: channel.slug || slugify(channel.name),
      workbook: channel.workbook || `${safeName}_Master_Data.xlsx`,
      zip: channel.zip || `${safeName}_Transcripts_${count}_Videos.zip`,
      runId: channel.runId || config.run.id,
      datasetId: channel.datasetId || config.run.datasetId,
    };
  });
  return {
    ...config,
    channels,
    channelCount: channels.length,
    totalExpectedVideos: channels.reduce((sum, channel) => sum + channel.expectedCount, 0),
  };
}

function usage() {
  return `Usage:
  node scripts/package_youtube_channel_dataset.mjs \\
    --config <dataset-config.json> --repo-root <path> --raw-json <path> \\
    --preflight-json <path> --sample-verification-json <path> \\
    --template-xlsx <path> \\
    --artifact-tool-module <path-to-artifact_tool.mjs> \\
    --jszip-module <path-to-jszip-module> \\
    --raw-output-dir <repo-relative-path> \\
    --extracted-output-dir <repo-relative-path> \\
    --manifest-dir <repo-relative-path> \\
    --qa-output-dir <path>

Optional: --recovery-raw-json <path> --description-verification-json <path>

Outputs: immutable raw copies, clean records, combined JSON/CSV/XLSX,
per-channel five-sheet workbooks and transcript ZIPs, validation evidence,
checksums, and manifest/lineage files. Input artifacts are read only.`;
}

const args = parseArgs(process.argv.slice(2));
if (args["normalize-csv-value"] !== undefined) {
  console.log(csvEscape(args["normalize-csv-value"]));
  process.exit(0);
}
if (args["validate-config-only"]) {
  if (!args.config) throw new Error("Required argument missing: --config");
  const normalized = normalizeConfig(JSON.parse(await fs.readFile(path.resolve(args.config), "utf8")));
  console.log(JSON.stringify({
    datasetId: normalized.datasetId,
    channelCount: normalized.channelCount,
    totalExpectedVideos: normalized.totalExpectedVideos,
    channels: normalized.channels,
  }));
  process.exit(0);
}
if (args["validate-record-merge-only"]) {
  for (const key of ["config", "raw-json", "recovery-raw-json"]) {
    if (!args[key]) throw new Error(`Required argument missing: --${key}`);
  }
  const normalized = normalizeConfig(JSON.parse(await fs.readFile(path.resolve(args.config), "utf8")));
  const rawRecords = JSON.parse(await fs.readFile(path.resolve(args["raw-json"]), "utf8"));
  const recoveryRecords = JSON.parse(await fs.readFile(path.resolve(args["recovery-raw-json"]), "utf8"));
  const merged = mergeActorVideoRecords(rawRecords, recoveryRecords);
  assert(merged.byId.size === normalized.totalExpectedVideos,
    `Merged video count must be ${normalized.totalExpectedVideos}; got ${merged.byId.size}`);
  console.log(JSON.stringify({
    mergedVideoCount: merged.byId.size,
    recoveryAddedVideoIds: merged.recoveryAddedVideoIds,
  }));
  process.exit(0);
}
if (args.help) {
  console.log(usage());
  process.exit(0);
}
const requiredArgs = [
  "config", "repo-root", "raw-json", "preflight-json", "sample-verification-json", "template-xlsx", "artifact-tool-module", "jszip-module",
  "raw-output-dir", "extracted-output-dir", "manifest-dir", "qa-output-dir",
];
for (const key of requiredArgs) if (!args[key]) throw new Error(`Required argument missing: --${key}`);

const config = normalizeConfig(JSON.parse(await fs.readFile(path.resolve(args.config), "utf8")));
DATASET_ID = config.datasetId;
DATASET_NAME = config.datasetName;
ACTOR = config.actor;
COLLECTION_DATE = config.collectionDate;
RUN_ID = config.run.id;
APIFY_DATASET_ID = config.run.datasetId;
RECOVERY_RUN_ID = config.recoveryRun?.id ?? "Not applicable";
RECOVERY_DATASET_ID = config.recoveryRun?.datasetId ?? "Not applicable";
CHANNELS = config.channels;
TOTAL_VIDEOS = config.totalExpectedVideos;

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
const { FileBlob, SpreadsheetFile, Workbook } = artifactModule;
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
  const text = value === null || value === undefined
    ? ""
    : String(value).replace(/[ \t]+(?=\r?\n|$)/g, "");
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

function dateTime(value) {
  const parsed = new Date(String(value ?? ""));
  assert(!Number.isNaN(parsed.getTime()), `Invalid publication timestamp: ${value}`);
  return parsed;
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

const sourcePaths = {
  "raw-json": path.resolve(args["raw-json"]),
  "preflight-json": path.resolve(args["preflight-json"]),
  "sample-verification-json": path.resolve(args["sample-verification-json"]),
  "template-xlsx": path.resolve(args["template-xlsx"]),
};
if (args["recovery-raw-json"]) sourcePaths["recovery-raw-json"] = path.resolve(args["recovery-raw-json"]);
if (args["description-verification-json"]) sourcePaths["description-verification-json"] = path.resolve(args["description-verification-json"]);
for (const source of Object.values(sourcePaths)) assert(await exists(source), `Input missing: ${source}`);

const raw = JSON.parse(await fs.readFile(sourcePaths["raw-json"], "utf8"));
const preflight = JSON.parse(await fs.readFile(sourcePaths["preflight-json"], "utf8"));
const sampleVerification = JSON.parse(await fs.readFile(sourcePaths["sample-verification-json"], "utf8"));
assert(Array.isArray(raw), "Raw Actor export must be a JSON array");
assert(Array.isArray(preflight.channels) && preflight.channels.length === CHANNELS.length, "Preflight channel count mismatch");

function isVideoLike(record) { return record && typeof record === "object" && /^[A-Za-z0-9_-]{11}$/.test(record.id ?? ""); }
function isAboutRecord(record) { return !isVideoLike(record) && /\/about(?:$|[?#])/.test(String(record?.url ?? record?.input ?? "")); }
function mergeRecord(base, incoming) {
  const output = structuredClone(base);
  for (const [key, value] of Object.entries(incoming)) {
    if (value !== null && value !== undefined && value !== "" && (!Array.isArray(value) || value.length)) output[key] = structuredClone(value);
  }
  output._sourceTabs = unique([...(base._sourceTabs ?? []), base.sourceTab, base.fromChannelListPage, incoming.sourceTab, incoming.fromChannelListPage].filter(Boolean));
  output.sourceTab = output._sourceTabs.join(", ") || null;
  return output;
}

function mergeActorVideoRecords(rawRecords, recoveryRecords) {
  assert(Array.isArray(rawRecords), "Raw Actor export must be a JSON array");
  assert(Array.isArray(recoveryRecords), "Recovery raw export must be a JSON array");
  const byId = new Map();
  for (const record of rawRecords.filter(isVideoLike)) {
    byId.set(record.id, byId.has(record.id) ? mergeRecord(byId.get(record.id), record) : structuredClone(record));
  }
  const recoveryAddedVideoIds = [];
  for (const record of recoveryRecords.filter(isVideoLike)) {
    if (byId.has(record.id)) byId.set(record.id, mergeRecord(byId.get(record.id), record));
    else {
      byId.set(record.id, structuredClone(record));
      recoveryAddedVideoIds.push(record.id);
    }
  }
  return { byId, recoveryAddedVideoIds };
}

const rawVideoRecords = raw.filter(isVideoLike);
const aboutRecords = raw.filter(isAboutRecord);
const statusRecords = raw.filter(record => !isVideoLike(record) && !isAboutRecord(record) && (record?.error || record?.status || record?.note));
const unknownRecords = raw.filter(record => !isVideoLike(record) && !isAboutRecord(record) && !statusRecords.includes(record));
const recoveryRaw = sourcePaths["recovery-raw-json"] ? JSON.parse(await fs.readFile(sourcePaths["recovery-raw-json"], "utf8")) : [];
assert(Array.isArray(recoveryRaw), "Recovery raw export must be a JSON array");
const mergedActorRecords = mergeActorVideoRecords(raw, recoveryRaw);
const initialById = mergedActorRecords.byId;
const recoveryAddedVideoIds = mergedActorRecords.recoveryAddedVideoIds;
const duplicateRawVideoIds = rawVideoRecords.length - new Set(rawVideoRecords.map(record => record.id)).size;
const recoveryVerification = sourcePaths["description-verification-json"]
  ? JSON.parse(await fs.readFile(sourcePaths["description-verification-json"], "utf8")) : { items: [] };
assert(Array.isArray(recoveryVerification.items), "Description verification items must be an array");
const recoveryById = new Map(recoveryVerification.items.map(item => [item.video_id, item]));

const master = [...initialById.values()].map(record => ({
  ...record,
  url: canonicalVideoUrl(record),
  sourceTab: record.sourceTab ?? record.fromChannelListPage ?? null,
  _descriptionRecovery: recoveryById.has(record.id) ? recoveryById.get(record.id) : { status: String(record.text ?? "").trim() ? "Not required" : "Unknown" },
  _provenance: { datasetId: DATASET_ID, actor: ACTOR, runId: RUN_ID, apifyDatasetId: APIFY_DATASET_ID, collectionDate: COLLECTION_DATE },
})).sort((a, b) => String(a.channelName).localeCompare(String(b.channelName)) || String(b.date).localeCompare(String(a.date)) || String(a.id).localeCompare(String(b.id)));
assert(master.length === TOTAL_VIDEOS, `Master JSON record count must be ${TOTAL_VIDEOS}; got ${master.length}`);
assert(master.every(validVideoRecord), "Master contains invalid required video fields");
const masterIds = master.map(videoId);
assert(new Set(masterIds).size === TOTAL_VIDEOS, "Master video IDs are not unique");
for (const channel of CHANNELS) {
  const records = master.filter(record => record.channelId === channel.channelId);
  assert(records.length === channel.count, `${channel.name} expected ${channel.count}; got ${records.length}`);
  assert(records.every(record => `@${String(record.channelUsername ?? "").replace(/^@/, "")}`.toLowerCase() === channel.handle.toLowerCase()), `${channel.name} Actor handle mismatch`);
}
assert(Array.isArray(sampleVerification.channels) && sampleVerification.channels.length === CHANNELS.length, "Sample verification must cover every configured channel");
const sampledIds = [];
for (const channel of CHANNELS) {
  const entry = sampleVerification.channels.find(item => item.channel === channel.name);
  assert(entry, `Sample verification missing channel ${channel.name}`);
  const expectedSamples = Math.min(5, channel.count);
  assert(Array.isArray(entry.observations) && entry.observations.length === expectedSamples, `${channel.name} sample verification must contain ${expectedSamples} observations`);
  for (const observation of entry.observations) {
    assert(observation.valid === true, `${channel.name} browser verification failed for ${observation.videoId}`);
    assert(masterIds.includes(observation.videoId), `${channel.name} sampled video ${observation.videoId} is absent from master`);
    assert(String(observation.resolvedUrl).includes(`watch?v=${observation.videoId}`), `${channel.name} sampled video URL mismatch for ${observation.videoId}`);
    sampledIds.push(observation.videoId);
  }
}
assert(new Set(sampledIds).size === sampledIds.length, "Sample verification contains duplicate video IDs");

await fs.mkdir(rawOutputDir, { recursive: true });
await fs.mkdir(combinedDir, { recursive: true });
await fs.mkdir(packagesDir, { recursive: true });
await fs.mkdir(manifestDir, { recursive: true });
await fs.mkdir(qaOutputDir, { recursive: true });

const rawCopies = [{
  source: sourcePaths["raw-json"], destination: path.join(rawOutputDir, "apify", RUN_ID, "youtube_actor_raw.json"),
  records: raw.length, videos: rawVideoRecords.length, runId: RUN_ID, datasetId: APIFY_DATASET_ID,
  channels: CHANNELS.map(channel => channel.name).join("; "), date: COLLECTION_DATE,
}];
if (sourcePaths["recovery-raw-json"]) rawCopies.push({
  source: sourcePaths["recovery-raw-json"], destination: path.join(rawOutputDir, "apify", RECOVERY_RUN_ID, "youtube_recovery_actor_raw.json"),
  records: recoveryRaw.length, videos: recoveryRaw.filter(isVideoLike).length, runId: RECOVERY_RUN_ID,
  datasetId: RECOVERY_DATASET_ID, channels: CHANNELS.map(channel => channel.name).join("; "), date: COLLECTION_DATE,
});
for (const item of rawCopies) await copyExact(item.source, item.destination);

const preflightPath = path.join(manifestDir, `${DATASET_ID}_PREFLIGHT.json`);
await fs.writeFile(preflightPath, `${JSON.stringify(preflight, null, 2)}\n`, "utf8");
const sampleVerificationPath = path.join(manifestDir, `${DATASET_ID}_VIDEO_SAMPLE_VERIFICATION.json`);
await fs.writeFile(sampleVerificationPath, `${JSON.stringify(sampleVerification, null, 2)}\n`, "utf8");
const cleanPath = path.join(combinedDir, `youtube_${CHANNELS.length}_channels_clean.json`);
const masterJsonPath = path.join(combinedDir, `youtube_${CHANNELS.length}_channels_master.json`);
await fs.writeFile(cleanPath, `${JSON.stringify(master, null, 2)}\n`, "utf8");
await fs.writeFile(masterJsonPath, `${JSON.stringify(master, null, 2)}\n`, "utf8");

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
    published: dateTime(record.date),
    publishedText: record.date,
    date: dateOnly(record.date),
    day: dateOnly(record.date).toLocaleDateString("en-US", { weekday: "long", timeZone: "UTC" }),
    seconds,
    duration: formatDuration(seconds),
    views: Number(record.viewCount),
    likes: Number(record.likes),
    comments: Number(record.commentsCount),
    words: wordCount(text),
    description: String(record.text ?? ""),
    descriptionStatus: record._descriptionRecovery?.status ?? (String(record.text ?? "").trim() ? "Available" : "Unknown"),
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

function missingDescriptionText(video) {
  if (/no public description/i.test(video.descriptionStatus)) return "No public description (verified on YouTube).";
  return `Description unavailable: ${video.descriptionStatus || "Unknown"}`;
}

function verificationRows(channel, videos) {
  const ids = videos.map(video => video.id);
  const duplicateCount = ids.length - new Set(ids).size;
  const withDescriptions = videos.filter(video => video.description.trim()).length;
  const genuineNoDescription = videos.filter(video => /no public description/i.test(video.descriptionStatus)).length;
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
    ["Genuine no-description videos", genuineNoDescription, genuineNoDescription ? `Verified on YouTube${RECOVERY_RUN_ID === "Not applicable" ? "" : ` and recovery run ${RECOVERY_RUN_ID}`}` : "None"],
    ["Videos with transcript", videos.filter(video => video.transcript.trim()).length, "Complete subtitles[].plaintext"],
    ["Transcript text files written", videos.length, "One file per video"],
    ["Total transcript words", videos.reduce((sum, video) => sum + video.words, 0), "Unicode word count across transcript plaintext"],
    ["Longest description length", Math.max(...videos.map(video => video.description.length)), "Characters; zero means verified absent description where documented"],
    ["Total description links", videos.reduce((sum, video) => sum + video.links.length, 0), "Unique URLs from Actor output and description text"],
    ["Videos containing hashtags", videos.filter(video => video.tags.length).length, "Complete unique hashtag set"],
    ["Valid video URLs", videos.filter(video => /^https:\/\/www\.youtube\.com\/watch\?v=[A-Za-z0-9_-]{11}$/.test(video.url)).length, "Canonical watch URLs"],
    ["Video IDs matching combined master", videos.filter(video => masterIds.includes(video.id)).length, `Exact channel subset of ${TOTAL_VIDEOS}-video master`],
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
  const noDescriptions = videos.filter(video => /no public description/i.test(video.descriptionStatus)).length;
  overview.mergeCells("A1:B1"); overview.mergeCells("A2:B2");
  overview.getRange("A1").values = [[`${meta.name} — Full Channel Data Export`]];
  overview.getRange("A2").values = [[`Source: Apify ${ACTOR} | Packaged ${COLLECTION_DATE} | ${videos.length} videos, ${videos.length - noDescriptions} public descriptions, ${videos.length} transcripts`]];
  overview.getRange("A4:B4").values = [["Field", "Value"]];
  const overviewRows = [
    ["Channel Name", meta.name], ["Handle", meta.handle], ["Channel ID", meta.id], ["Canonical Channel URL", meta.url],
    ["Subscribers", meta.subscribers], ["Total Videos Reported by YouTube", meta.reportedVideos], ["Videos Captured", videos.length],
    ["Total Channel Views", meta.lifetimeViews], ["Joined Date", meta.joined], ["Channel Location", meta.location],
    ["Verified Status", meta.verified === true ? "Yes" : meta.verified === false ? "No" : "Unavailable"],
    ["Shorts Count", shorts], ["Live-Video Count", live], ["Avatar URL", meta.avatar], ["Banner URL", meta.banner],
    ["Complete Channel Description", meta.description], ["Source Actor", ACTOR], ["Scrape Date", new Date(`${COLLECTION_DATE}T00:00:00Z`)],
    ["Relevant Run ID", RECOVERY_RUN_ID === "Not applicable" ? channel.runId : `${channel.runId}; recovery ${RECOVERY_RUN_ID}`],
    ["Relevant Dataset ID", RECOVERY_DATASET_ID === "Not applicable" ? channel.datasetId : `${channel.datasetId}; recovery ${RECOVERY_DATASET_ID}`],
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
  all.getRange(`E5:E${totalRow - 1}`).format.numberFormat = "yyyy-mm-dd hh:mm:ss";
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
    video.description || missingDescriptionText(video),
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
  verification.getRange("A2").values = [[`Every value below is computed from the registered ${TOTAL_VIDEOS}-video master and channel package data.`]];
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
  analysis.getRange("D6:F15").values = top.map(video => [video.title, video.views, video.views / Math.max(1, Math.floor((new Date(`${COLLECTION_DATE}T00:00:00Z`) - video.date) / 86400000))]);
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
  await fs.rm(`${workbookPath}.inspect.ndjson`, { force: true });

  const zip = new JSZip();
  const fixedDate = new Date(`${COLLECTION_DATE}T00:00:00Z`);
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
    const description = video.description || missingDescriptionText(video);
    const body = [
      `Channel      : ${meta.name}`,
      `Title        : ${video.title}`,
      `Video ID     : ${video.id}`,
      `URL          : ${video.url}`,
      `Published    : ${video.publishedText}`,
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

const actorKeys = unique(master.flatMap(record => Object.keys(record).filter(key => !key.startsWith("_")))).sort();
const standardHeaders = [
  "dataset_id", "actor_run_id", "actor_dataset_id", "raw_record_sha256", "input_channel_url",
  "channel_name", "channel_id", "channel_handle_or_username", "canonical_channel_url", "channel_description",
  "subscriber_count", "total_channel_views", "reported_channel_video_count", "video_title", "video_id",
  "canonical_youtube_video_url", "content_type", "source_tab", "description", "publication_date_time", "duration",
  "duration_seconds", "view_count", "like_count", "comment_count", "comments_disabled", "thumbnail_url", "hashtags",
  "description_links", "paid_content", "members_only", "age_restricted", "location", "subtitle_languages",
  "subtitle_types", "transcript_plaintext", "transcript_unavailable_reason", "subtitles_json", "ai_summary", "ai_description",
];
const flatHeaders = [...standardHeaders, ...actorKeys.map(key => `actor_${key}`)];

function flatValue(value) {
  if (value === null || value === undefined) return null;
  if (typeof value === "object") return JSON.stringify(value);
  return value;
}

function flattenRecord(record) {
  const missingTranscript = transcript(record).trim() ? null : (record._transcriptUnavailableReason ?? "Unknown");
  const standard = {
    dataset_id: DATASET_ID, actor_run_id: RUN_ID, actor_dataset_id: APIFY_DATASET_ID,
    raw_record_sha256: sha256Text(JSON.stringify(record)), input_channel_url: record.inputChannelUrl ?? null,
    channel_name: record.channelName ?? null, channel_id: record.channelId ?? null,
    channel_handle_or_username: record.channelUsername ?? null, canonical_channel_url: record.channelUrl ?? null,
    channel_description: record.channelDescription ?? record.aboutChannelInfo?.channelDescription ?? null,
    subscriber_count: record.numberOfSubscribers ?? record.aboutChannelInfo?.numberOfSubscribers ?? null,
    total_channel_views: record.channelTotalViews ?? record.aboutChannelInfo?.channelTotalViews ?? null,
    reported_channel_video_count: record.channelTotalVideos ?? record.aboutChannelInfo?.channelTotalVideos ?? null,
    video_title: record.title ?? null, video_id: record.id, canonical_youtube_video_url: canonicalVideoUrl(record),
    content_type: contentType(record), source_tab: record.sourceTab ?? null, description: record.text ?? null,
    publication_date_time: record.date ?? null, duration: record.duration ?? null,
    duration_seconds: record.duration ? parseDuration(record.duration) : null, view_count: record.viewCount ?? null,
    like_count: record.likes ?? null, comment_count: record.commentsCount ?? null,
    comments_disabled: record.commentsTurnedOff ?? null, thumbnail_url: record.thumbnailUrl ?? null,
    hashtags: hashtags(record).join(", "), description_links: descriptionLinks(record).join("\n"),
    paid_content: record.isPaidContent ?? null, members_only: record.isMembersOnly ?? null,
    age_restricted: record.isAgeRestricted ?? null, location: record.location ?? null,
    subtitle_languages: subtitleLanguages(record), subtitle_types: captionType(record),
    transcript_plaintext: transcript(record) || null, transcript_unavailable_reason: missingTranscript,
    subtitles_json: JSON.stringify(subtitles(record)), ai_summary: record.aiVideoSummary ?? null,
    ai_description: record.aiVideoDescription ?? null,
  };
  return [...standardHeaders.map(header => flatValue(standard[header])), ...actorKeys.map(key => flatValue(record[key]))];
}

const flatRows = master.map(flattenRecord);
const masterCsvPath = path.join(combinedDir, `youtube_${CHANNELS.length}_channels_master.csv`);
await fs.writeFile(masterCsvPath, `\uFEFF${flatHeaders.map(csvEscape).join(",")}\n${flatRows.map(row => row.map(csvEscape).join(",")).join("\n")}\n`, "utf8");

const combinedWorkbook = Workbook.create();
const combinedSheet = combinedWorkbook.worksheets.add("Videos");
combinedSheet.getRange("A1").write([flatHeaders, ...flatRows]);
combinedSheet.getRange(`A1:${columnName(flatHeaders.length)}1`).format = {
  fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" }, wrapText: true, rowHeight: 36,
};
combinedSheet.getRange(`A1:${columnName(flatHeaders.length)}${flatRows.length + 1}`).format.verticalAlignment = "top";
combinedSheet.freezePanes.freezeRows(1);
const combinedTable = combinedSheet.tables.add(`A1:${columnName(flatHeaders.length)}${flatRows.length + 1}`, true, "CombinedVideosTable");
combinedTable.style = "TableStyleMedium2";
combinedSheet.getRange(`A1:${columnName(flatHeaders.length)}${flatRows.length + 1}`).format.autofitColumns();
for (const width of [15, 16, 17, 18, 19, 36, 37]) combinedSheet.getRange(`${columnName(width)}:${columnName(width)}`).format.columnWidth = 28;
combinedWorkbook.recalculate();
const masterXlsxPath = path.join(combinedDir, `youtube_${CHANNELS.length}_channels_master.xlsx`);
await (await SpreadsheetFile.exportXlsx(combinedWorkbook)).save(masterXlsxPath);

const results = [];
for (const channel of CHANNELS) {
  const records = master.filter(record => record.channelId === channel.channelId).map(record => structuredClone(record));
  results.push(await buildChannelPackage(channel, records));
}

const allPackageIds = results.flatMap(result => result.videos.map(video => video.id));
assert(allPackageIds.length === TOTAL_VIDEOS && new Set(allPackageIds).size === TOTAL_VIDEOS, `Package ID union must contain ${TOTAL_VIDEOS} unique videos`);
assert(masterIds.every(id => allPackageIds.includes(id)), "Package ID union differs from combined master");
assert(results.reduce((sum, result) => sum + result.videos.length, 0) === TOTAL_VIDEOS, "Per-channel workbook record sum differs from master");

const channelSummaryRows = results.map(result => {
  const observed = preflight.channels.find(item => String(item.handle).toLowerCase() === result.channel.handle.toLowerCase());
  const scraped = result.videos.length;
  return {
    channel_name: result.channel.name, supplied_handle: result.channel.handle, channel_id: result.channel.channelId,
    canonical_channel_url: result.meta.url, live_public_count: observed?.combinedUniquePublicVideos ?? result.channel.count,
    scraped_unique_videos: scraped, missing: Math.max(0, (observed?.combinedUniquePublicVideos ?? result.channel.count) - scraped),
    duplicate_ids: 0, regular_videos: result.videos.filter(video => video.type === "regular video").length,
    shorts: result.videos.filter(video => video.type === "Short").length,
    livestreams: result.videos.filter(video => video.type === "livestream").length,
    with_transcripts: result.videos.filter(video => video.transcript.trim()).length,
    without_transcripts: result.videos.filter(video => !video.transcript.trim()).length,
    missing_descriptions: result.videos.filter(video => !video.description.trim()).length,
  };
});
const summaryHeaders = Object.keys(channelSummaryRows[0]);
const summaryPath = path.join(combinedDir, `youtube_${CHANNELS.length}_channels_channel_summary.csv`);
await fs.writeFile(summaryPath, `${summaryHeaders.join(",")}\n${channelSummaryRows.map(row => summaryHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");

const masterCsvRows = parseCsv(await fs.readFile(masterCsvPath, "utf8"));
const csvIdIndex = masterCsvRows[0].indexOf("video_id");
const csvIds = masterCsvRows.slice(1).filter(row => row.some(value => value !== "")).map(row => row[csvIdIndex]);
assert(csvIds.length === TOTAL_VIDEOS && new Set(csvIds).size === TOTAL_VIDEOS, "Combined CSV ID validation failed");
const xlsxCheck = await SpreadsheetFile.importXlsx(await FileBlob.load(masterXlsxPath));
const xlsxValues = xlsxCheck.worksheets.getItem("Videos").getUsedRange(true).values;
const xlsxIdIndex = xlsxValues[0].indexOf("video_id");
const xlsxIds = xlsxValues.slice(1).filter(row => row[xlsxIdIndex]).map(row => String(row[xlsxIdIndex]));
assert(xlsxIds.length === TOTAL_VIDEOS && new Set(xlsxIds).size === TOTAL_VIDEOS, "Combined XLSX ID validation failed");
assert(new Set(csvIds).size === new Set(xlsxIds).size && masterIds.every(id => csvIds.includes(id) && xlsxIds.includes(id)), "Combined JSON/CSV/XLSX ID sets differ");
await fs.rm(`${masterXlsxPath}.inspect.ndjson`, { force: true });

const totalRegular = results.flatMap(result => result.videos).filter(video => video.type === "regular video").length;
const totalShorts = results.flatMap(result => result.videos).filter(video => video.type === "Short").length;
const totalLive = results.flatMap(result => result.videos).filter(video => video.type === "livestream").length;
const totalTranscripts = master.filter(record => transcript(record).trim()).length;
const transcriptCellsOverExcelLimit = master.filter(record => transcript(record).length > 32767).length;
const missingDescriptions = master.filter(record => !String(record.text ?? "").trim()).length;
const verifiedNoDescriptions = master.filter(record => /no public description/i.test(record._descriptionRecovery?.status ?? "")).length;
assert(totalTranscripts === TOTAL_VIDEOS, `Transcript coverage ${totalTranscripts}/${TOTAL_VIDEOS}; targeted recovery required`);
assert(missingDescriptions === verifiedNoDescriptions, "Every missing description requires verified no-public-description evidence");
assert(channelSummaryRows.every(row => row.missing === 0), "Live-count reconciliation has missing videos");

const validationPath = path.join(extractedOutputDir, `youtube_${CHANNELS.length}_channels_packaging_validation_report.md`);
const validationLines = [
  `# ${CHANNELS.length}-Channel YouTube Packaging Validation`, "",
  `- Dataset: ${DATASET_ID} — ${DATASET_NAME}`, `- Generated: ${COLLECTION_DATE}`, `- Actor: ${ACTOR}`,
  `- Run: ${RUN_ID}`, `- Apify dataset: ${APIFY_DATASET_ID}`, `- Status: ${config.run.status}`,
  `- Requests: ${config.run.requestsSucceeded} succeeded; ${config.run.requestsFailed} failed`,
  `- Original estimated cost: $${config.run.estimatedCostUsd}`, `- Original actual cost: $${config.run.actualCostUsd}`,
  `- Recovery run: ${RECOVERY_RUN_ID}; dataset: ${RECOVERY_DATASET_ID}`,
  `- Recovery records: ${recoveryRaw.length}; recovery-added video IDs: ${recoveryAddedVideoIds.join(", ") || "none"}`,
  `- Recovery actual cost: $${config.recoveryRun?.actualCostUsd ?? 0}`,
  `- Total estimated cost: $${config.budget?.totalEstimatedCostUsd ?? config.run.estimatedCostUsd}`,
  `- Total actual cost: $${config.budget?.totalActualCostUsd ?? config.run.actualCostUsd}`, "",
  "## Count reconciliation", "",
  "| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |",
  "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
  ...channelSummaryRows.map(row => `| ${row.channel_name} | ${row.live_public_count} | ${row.scraped_unique_videos} | ${row.missing} | ${row.duplicate_ids} | ${row.regular_videos} | ${row.shorts} | ${row.livestreams} | ${row.with_transcripts} |`),
  `| **Total** | **${channelSummaryRows.reduce((sum, row) => sum + Number(row.live_public_count), 0)}** | **${TOTAL_VIDEOS}** | **0** | **0** | **${totalRegular}** | **${totalShorts}** | **${totalLive}** | **${totalTranscripts}** |`, "",
  "## Record classification", "",
  `- Raw records: ${raw.length}`, `- Raw video records: ${rawVideoRecords.length}`,
  `- Recovery raw records: ${recoveryRaw.length}`, `- Recovery video records: ${recoveryRaw.filter(isVideoLike).length}`,
  `- Unique video IDs: ${TOTAL_VIDEOS}`, `- Duplicate video discoveries merged: ${duplicateRawVideoIds}`,
  `- Channel-about records: ${aboutRecords.length}`, `- Status/error records: ${statusRecords.length}`,
  `- Unknown records: ${unknownRecords.length}`, "",
  "## Validation evidence", "",
  `- Combined JSON, CSV, and XLSX contain identical ${TOTAL_VIDEOS}-video ID sets.`,
  `- ${CHANNELS.length} workbook counts sum to ${TOTAL_VIDEOS}; package union equals combined master.`,
  `- ${totalTranscripts}/${TOTAL_VIDEOS} records contain plaintext transcripts.`,
  `- ${missingDescriptions} descriptions remain empty; ${verifiedNoDescriptions} have live YouTube no-description evidence.`,
  `- ${sampledIds.length}/${sampledIds.length} sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).`,
  `- ${TOTAL_VIDEOS}/${TOTAL_VIDEOS} video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.`,
  `- ${TOTAL_VIDEOS} workbook publication cells use real spreadsheet date-time values; ${TOTAL_VIDEOS * 5} metric formulas and ${TOTAL_VIDEOS * 2} HYPERLINK formulas were generated.`,
  `- Transcript packs contain ${TOTAL_VIDEOS + CHANNELS.length} root text files: ${TOTAL_VIDEOS} video files plus ${CHANNELS.length} INDEX.txt files.`,
  "- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.",
  "- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.",
  "- Immutable raw source/destination SHA-256 hashes match.",
  "- Channel descriptions were never substituted for video descriptions.",
  "- Phase 1 descriptive summaries only; no strategy or recommendations.", "",
];
await fs.writeFile(validationPath, validationLines.join("\n"), "utf8");

const configPath = path.join(manifestDir, `${DATASET_ID}_CONFIG.json`);
await fs.writeFile(configPath, `${JSON.stringify(config, null, 2)}\n`, "utf8");
const sourceArtifactPath = path.join(manifestDir, `${DATASET_ID}_SOURCE_ARTIFACTS.csv`);
const sourceArtifactRows = [];
for (const item of rawCopies) {
  const stat = await fs.stat(item.source);
  sourceArtifactRows.push({ filename: path.basename(item.source), absolute_source_path: item.source, size_bytes: stat.size,
    sha256: await sha256(item.source), format: "JSON", row_or_record_count: item.records,
    unique_video_id_count: new Set((JSON.parse(await fs.readFile(item.source, "utf8"))).filter(isVideoLike).map(videoId)).size,
    source_run_id: item.runId, source_dataset_id: item.datasetId, raw_or_derived_status: "RAW",
    channels_represented: item.channels, processing_date: item.date, missing_data_notes: "Immutable Actor export; source left unchanged." });
}
const sourceHeaders = Object.keys(sourceArtifactRows[0]);
await fs.writeFile(sourceArtifactPath, `${sourceHeaders.join(",")}\n${sourceArtifactRows.map(row => sourceHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");

const artifacts = [];
function addArtifact(spec) { artifacts.push(spec); }
for (const item of rawCopies) addArtifact({ path: item.destination, type: "JSON", description: "Immutable Apify Actor output", source: item.source,
  runId: item.runId, datasetId: item.datasetId, channel: item.channels, fileCount: 1, recordCount: item.records,
  duplicate: "VIDEO_IDS_DEDUPED_IN_DERIVED_MASTER", status: "RAW_REGISTERED", classification: "RAW", parent: "Apify Actor dataset",
  notes: `${item.videos} video records; non-video records preserved.` });
for (const [filePath, type, description, count] of [
  [cleanPath, "JSON", "Clean unique video records", TOTAL_VIDEOS], [masterJsonPath, "JSON", "Combined master preserving Actor fields", TOTAL_VIDEOS],
  [masterCsvPath, "CSV", "Flattened combined master", TOTAL_VIDEOS], [masterXlsxPath, "XLSX", "Combined analysis workbook", TOTAL_VIDEOS],
  [summaryPath, "CSV", "Per-channel count and coverage summary", CHANNELS.length], [validationPath, "Markdown", "Packaging validation evidence", TOTAL_VIDEOS],
]) addArtifact({ path: filePath, type, description, source: sourcePaths["raw-json"], runId: RUN_ID, datasetId: APIFY_DATASET_ID,
  channel: `All ${CHANNELS.length} channels`, fileCount: 1, recordCount: count, duplicate: count === TOTAL_VIDEOS ? `${TOTAL_VIDEOS}_UNIQUE_VIDEO_IDS` : "NOT_APPLICABLE",
  status: "VALIDATED", classification: "DERIVED", parent: "Immutable Actor raw export", notes: "Generated reproducibly; source raw unchanged." });
for (const result of results) {
  addArtifact({ path: result.workbookPath, type: "XLSX", description: `${result.channel.name} five-sheet master workbook`, source: masterJsonPath,
    runId: RUN_ID, datasetId: APIFY_DATASET_ID, channel: result.channel.name, fileCount: 1, recordCount: result.videos.length,
    duplicate: "UNIQUE_VIDEO_IDS", status: "VALIDATED", classification: "DERIVED", parent: path.relative(repoRoot, masterJsonPath),
    notes: "Reference-format workbook; formulas, filters, panes, hyperlinks, and five rendered sheets validated." });
  addArtifact({ path: result.zipPath, type: "ZIP/TXT", description: `${result.channel.name} transcript package`, source: masterJsonPath,
    runId: RUN_ID, datasetId: APIFY_DATASET_ID, channel: result.channel.name, fileCount: result.videos.length + 1, recordCount: result.videos.length,
    duplicate: "UNIQUE_VIDEO_IDS_AND_FILENAMES", status: "VALIDATED", classification: "DERIVED", parent: path.relative(repoRoot, masterJsonPath),
    notes: "ZIP root contains one UTF-8 transcript file per video plus INDEX.txt." });
}
for (const [filePath, type, description] of [[preflightPath, "JSON", "Live browser identity/count preflight"], [sampleVerificationPath, "JSON", "Live browser video sample verification"], [configPath, "JSON", "Reproducible dataset configuration"], [sourceArtifactPath, "CSV", "Source artifact inventory"]])
  addArtifact({ path: filePath, type, description, source: filePath === preflightPath ? sourcePaths["preflight-json"] : filePath === sampleVerificationPath ? sourcePaths["sample-verification-json"] : "Repository workflow",
    runId: RUN_ID, datasetId: APIFY_DATASET_ID, channel: `All ${CHANNELS.length} channels`, fileCount: 1,
    recordCount: filePath === preflightPath ? CHANNELS.length : filePath === sampleVerificationPath ? sampledIds.length : null, duplicate: "NOT_APPLICABLE", status: "VALIDATED",
    classification: "MANIFEST", parent: "Live browser observations and Actor run", notes: "Phase 1 provenance evidence." });
const generatorPath = path.join(repoRoot, "scripts", path.basename(new URL(import.meta.url).pathname));
addArtifact({ path: generatorPath, type: "JavaScript", description: "Channel-count-independent YouTube package generator", source: "Repository implementation",
  runId: "Not applicable", datasetId: "Not applicable", channel: "Any configured channel set", fileCount: 1, recordCount: null,
  duplicate: "NOT_APPLICABLE", status: "VALIDATED", classification: "CODE", parent: "DS-000020 packaging format",
  notes: "Config-driven; no secrets or local absolute paths; DS-000020 reproduction script remains byte-identical." });
for (const [relativePath, type, description, classification] of [
  ["tests/test_youtube_dataset_packager_generalization.py", "Python", "Generator generalization and DS-000020 immutability tests", "TEST"],
  ["scripts/README.md", "Markdown", "Generator usage documentation", "DOCUMENTATION"],
  ["docs/DATA_INVENTORY.md", "Markdown", "Dataset-level inventory index update", "DOCUMENTATION"],
  [".gitignore", "Git ignore rules", "Narrow authorization for checksum-registered DS-000021 raw evidence", "REPOSITORY_CONFIGURATION"],
  [".gitattributes", "Git attributes", "Verbatim multiline CSV whitespace preservation", "REPOSITORY_CONFIGURATION"],
]) {
  const filePath = path.join(repoRoot, relativePath);
  assert(await exists(filePath), `Repository support artifact missing: ${relativePath}`);
  addArtifact({ path: filePath, type, description, source: "Repository workflow", runId: "Not applicable", datasetId: "Not applicable",
    channel: `All ${CHANNELS.length} channels`, fileCount: 1, recordCount: null, duplicate: "NOT_APPLICABLE",
    status: "VALIDATED", classification, parent: DATASET_ID, notes: "Task-scoped repository support artifact." });
}

const manifestRows = [];
for (let index = 0; index < artifacts.length; index += 1) {
  const artifact = artifacts[index];
  const stat = await fs.stat(artifact.path);
  manifestRows.push({ dataset_id: DATASET_ID, artifact_id: `${DATASET_ID}-F${String(index + 1).padStart(3, "0")}`,
    dataset_name: DATASET_NAME, filename: path.basename(artifact.path), repository_relative_path: path.relative(repoRoot, artifact.path),
    file_type: artifact.type, semantic_class: artifact.classification === "RAW" || artifact.classification === "DERIVED" || artifact.classification === "MANIFEST" ? "B — Competitor Evidence" : "Repository workflow", description: artifact.description, source: artifact.source,
    apify_actor: ACTOR, apify_run_id: artifact.runId, apify_dataset_id: artifact.datasetId, associated_channel: artifact.channel,
    collection_date: COLLECTION_DATE, file_count: artifact.fileCount, record_count: artifact.recordCount, size_bytes: stat.size,
    sha256: await sha256(artifact.path), duplicate_status: artifact.duplicate, processing_status: artifact.status,
    raw_or_derived_classification: artifact.classification, parent_source_artifact: artifact.parent, notes_and_limitations: artifact.notes });
}
const manifestCsvPath = path.join(manifestDir, `${DATASET_ID}_FILES.csv`);
const manifestHeaders = Object.keys(manifestRows[0]);
await fs.writeFile(manifestCsvPath, `${manifestHeaders.join(",")}\n${manifestRows.map(row => manifestHeaders.map(header => csvEscape(row[header])).join(",")).join("\n")}\n`, "utf8");

const manifestMdPath = path.join(manifestDir, `${DATASET_ID}.md`);
const manifestMd = [
  `# ${DATASET_ID} — ${DATASET_NAME}`, "", "## Dataset identity", "", `- Dataset ID: ${DATASET_ID}`,
  "- Semantic class: B — Competitor Evidence", "- Processing status: STRUCTURED_REGISTERED",
  `- Collection/packaging date: ${COLLECTION_DATE}`, `- Actor: ${ACTOR}`, `- Run: ${RUN_ID}`,
  `- Apify dataset: ${APIFY_DATASET_ID}`, `- Canonical videos: ${TOTAL_VIDEOS} (${TOTAL_VIDEOS} unique IDs; 0 duplicates)`,
  `- Channel counts: ${CHANNELS.map(channel => `${channel.name} ${channel.count}`).join("; ")}.`,
  `- Content types: ${totalRegular} regular videos; ${totalShorts} Shorts; ${totalLive} livestreams.`,
  `- Transcript coverage: ${totalTranscripts}/${TOTAL_VIDEOS} plaintext transcripts.`,
  `- Actor recovery: ${recoveryRaw.filter(isVideoLike).length} targeted video; ${recoveryAddedVideoIds.length} added to the derived master.`,
  `- Missing descriptions: ${missingDescriptions}; verified no-public-description videos: ${verifiedNoDescriptions}.`, "",
  "## Lineage", "", "```text", "Original Apify Actor raw export + immutable targeted recovery export", "  -> classified and deduplicated clean video records",
  `  -> verified ${CHANNELS.length}-channel ${TOTAL_VIDEOS}-video master`, "  -> channel-specific master workbooks",
  "  -> channel-specific transcript packs", "```", "",
  "Raw Actor exports are immutable. Raw source/destination SHA-256 hashes match. Derived artifacts retain run/dataset provenance.", "",
  "## Artifact inventory", "", `Detailed file-level manifest: [${DATASET_ID}_FILES.csv](./${DATASET_ID}_FILES.csv)`,
  `Source artifact inventory: [${DATASET_ID}_SOURCE_ARTIFACTS.csv](./${DATASET_ID}_SOURCE_ARTIFACTS.csv)`, "",
  `Browser sample verification: [${DATASET_ID}_VIDEO_SAMPLE_VERIFICATION.json](./${DATASET_ID}_VIDEO_SAMPLE_VERIFICATION.json)`, "",
  "## Limitations", "", `- ${missingDescriptions} videos have no verified public description.`,
  `- ${transcriptCellsOverExcelLimit} combined-workbook transcript cells exceed Excel's 32,767-character display limit; complete text remains byte-preserved in JSON, CSV, raw Actor evidence, and transcript ZIPs.`,
  "- Per-video location and transcript/SRT URLs may be unavailable; plaintext transcripts are canonical when present.",
  "- Public metrics are point-in-time Actor observations and may change on YouTube.",
  "- Manifest does not hash itself or its file ledger because self-checksums are circular.", "",
];
await fs.writeFile(manifestMdPath, manifestMd.join("\n"), "utf8");

console.log(JSON.stringify({ datasetId: DATASET_ID, rawRecords: raw.length, uniqueVideoIds: TOTAL_VIDEOS,
  rawVideoRecords: rawVideoRecords.length, aboutRecords: aboutRecords.length, statusRecords: statusRecords.length,
  unknownRecords: unknownRecords.length, duplicateDiscoveriesMerged: duplicateRawVideoIds, transcripts: totalTranscripts,
  missingDescriptions, channelPackages: results.map(result => ({ channel: result.channel.name, videos: result.videos.length,
    workbook: path.relative(repoRoot, result.workbookPath), transcriptZip: path.relative(repoRoot, result.zipPath) })),
  combined: [masterJsonPath, masterCsvPath, masterXlsxPath].map(file => path.relative(repoRoot, file)),
  manifest: path.relative(repoRoot, manifestMdPath), manifestFiles: path.relative(repoRoot, manifestCsvPath),
  validationReport: path.relative(repoRoot, validationPath), qaRenders: REQUIRED_SHEETS.length * results.length }, null, 2));
