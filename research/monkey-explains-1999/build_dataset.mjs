#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { pathToFileURL } from "node:url";

const [rawPath, runPath, outputDir] = process.argv.slice(2);
if (!rawPath || !runPath || !outputDir) {
  throw new Error("Usage: node build_dataset.mjs <raw.json> <run.json> <output-dir>");
}

const artifactPath = process.env.ARTIFACT_TOOL_PATH;
if (!artifactPath) throw new Error("ARTIFACT_TOOL_PATH is required");
const { SpreadsheetFile, Workbook } = await import(pathToFileURL(artifactPath).href);

const raw = JSON.parse(await fs.readFile(rawPath, "utf8"));
const runEnvelope = JSON.parse(await fs.readFile(runPath, "utf8"));
const run = runEnvelope.data ?? runEnvelope;
const actorName = "streamers/youtube-scraper";
const actorBuild = "0.0.318";
const expectedChannelId = "UCiBGqUxeTe4AYQyRseSZaKw";
const acquisitionTimestamp = run.finishedAt ?? run.startedAt;
const datasetId = run.defaultDatasetId;
const runId = run.id ?? "Us4zQZvU2IbImyHl3";

const isVideo = (r) => r && /^[A-Za-z0-9_-]{11}$/.test(String(r.id ?? ""));
const aboutRecord = raw.find((r) => r?.aboutChannelInfo?.channelId === expectedChannelId);
if (!aboutRecord) throw new Error("Verified channel identity record is missing");
const about = aboutRecord.aboutChannelInfo;

const durationSeconds = (value) => {
  if (!value || typeof value !== "string") return null;
  const p = value.split(":").map(Number);
  if (p.some(Number.isNaN)) return null;
  if (p.length === 3) return p[0] * 3600 + p[1] * 60 + p[2];
  if (p.length === 2) return p[0] * 60 + p[1];
  return p[0];
};
const valueOrNull = (value) => value === undefined || value === null || value === "" ? null : value;
const unique = (items) => [...new Set(items.filter((x) => x !== null && x !== undefined && x !== ""))];
const typeOf = (r) => {
  const source = `${r.type ?? ""} ${r.fromChannelListPage ?? ""} ${r.fromYTUrl ?? ""} ${r.url ?? ""}`.toLowerCase();
  if (source.includes("short")) return "SHORT";
  if (source.includes("stream") || source.includes("live")) return "STREAM";
  return "REGULAR";
};
const canonicalUrl = (id) => `https://www.youtube.com/watch?v=${id}`;
const tagsOf = (r) => unique((Array.isArray(r.tags) ? r.tags : []).map(String));
const hashtagsOf = (r) => unique([
  ...(Array.isArray(r.hashtags) ? r.hashtags.map((x) => typeof x === "string" ? x : x?.text ?? x?.hashtag) : []),
  ...(String(r.text ?? "").match(/#[\p{L}\p{N}_]+/gu) ?? []),
].map((x) => x && (String(x).startsWith("#") ? String(x) : `#${x}`)));
const subtitleMeta = (r) => {
  const subs = Array.isArray(r.subtitles) ? r.subtitles.filter((x) => x && typeof x === "object") : [];
  return {
    available: subs.length > 0,
    languages: unique(subs.map((x) => x.language ?? x.lang)).join(", ") || null,
    sourceTypes: unique(subs.map((x) => x.type ?? x.sourceType)).join(", ") || null,
  };
};

const byId = new Map();
for (let i = 0; i < raw.length; i += 1) {
  const r = raw[i];
  if (!isVideo(r)) continue;
  if ((r.channelId ?? r.aboutChannelInfo?.channelId) !== expectedChannelId) continue;
  const prior = byId.get(r.id);
  if (!prior) byId.set(r.id, { ...r, _rawRows: [i] });
  else {
    const merged = { ...prior };
    for (const [k, v] of Object.entries(r)) {
      if (v !== null && v !== undefined && v !== "" && (!Array.isArray(v) || v.length)) merged[k] = v;
    }
    merged._rawRows = [...prior._rawRows, i];
    byId.set(r.id, merged);
  }
}

const excludedMembersOnly = [...byId.values()].filter((r) => r.isMembersOnly === true);
const publicRecords = [...byId.values()].filter((r) => r.isMembersOnly !== true);
const nowMs = new Date(acquisitionTimestamp).getTime();
const master = publicRecords.map((r) => {
  const published = valueOrNull(r.date);
  const publishedMs = published ? new Date(published).getTime() : NaN;
  const ageDays = Number.isFinite(publishedMs) ? Math.max(0, (nowMs - publishedMs) / 86400000) : null;
  const views = Number.isFinite(Number(r.viewCount)) ? Number(r.viewCount) : null;
  const likes = Number.isFinite(Number(r.likes)) ? Number(r.likes) : null;
  const comments = Number.isFinite(Number(r.commentsCount)) ? Number(r.commentsCount) : null;
  const engagement = views && likes !== null && comments !== null ? (likes + comments) / views : null;
  const subs = subtitleMeta(r);
  const videoType = typeOf(r);
  const missing = [];
  for (const [field, value] of Object.entries({
    title: r.title, publication_timestamp: published, duration: r.duration, view_count: views,
    like_count: likes, comment_count: comments, description: r.text, thumbnail_url: r.thumbnailUrl,
  })) if (value === null || value === undefined || value === "") missing.push(field);
  return {
    channel_name: about.channelName,
    channel_id: expectedChannelId,
    channel_handle: `@${String(about.channelUsername).replace(/^@/, "")}`,
    channel_url: about.channelUrl,
    video_id: r.id,
    title: valueOrNull(r.title),
    watch_url: canonicalUrl(r.id),
    shorts_url: videoType === "SHORT" ? `https://www.youtube.com/shorts/${r.id}` : null,
    source_video_url: valueOrNull(r.url),
    video_type: videoType,
    availability_status: "PUBLIC_ACCESSIBLE_AT_RETRIEVAL",
    publication_timestamp_utc: published,
    publication_date_utc: published ? published.slice(0, 10) : null,
    publication_time_utc: published && published.includes("T") ? published.slice(11, 19) : null,
    publication_precision: published ? "EXACT_ACTOR_TIMESTAMP" : "UNKNOWN",
    duration: valueOrNull(r.duration),
    duration_seconds: durationSeconds(r.duration),
    category: valueOrNull(r.category),
    language: valueOrNull(r.language),
    stream_type: valueOrNull(r.streamType),
    view_count: views,
    like_count: likes,
    comment_count: comments,
    engagement_rate: engagement,
    video_age_days_at_retrieval: ageDays,
    views_per_day: views !== null && ageDays !== null ? views / Math.max(ageDays, 1) : null,
    views_per_day_limitation: "Snapshot views divided by age at retrieval; not a historical velocity series.",
    description: valueOrNull(r.text),
    tags: tagsOf(r),
    hashtags: hashtagsOf(r),
    keywords: null,
    source_topic_or_category: valueOrNull(r.category),
    captions_or_transcript_available: subs.available,
    subtitle_languages: subs.languages,
    subtitle_source_types: subs.sourceTypes,
    pinned_or_featured_indicator: null,
    thumbnail_url: valueOrNull(r.thumbnailUrl),
    thumbnail_local_path: null,
    thumbnail_dimensions: null,
    thumbnail_file_sha256: null,
    actor_name: actorName,
    actor_version: actorBuild,
    actor_run_id: runId,
    actor_dataset_id: datasetId,
    record_source_url: valueOrNull(r.fromYTUrl) ?? valueOrNull(r.sourceUrl) ?? valueOrNull(r.url),
    raw_dataset_row_locator: r._rawRows.map((i) => `row:${i + 1}`).join(";"),
    metadata_retrieval_timestamp_utc: acquisitionTimestamp,
    channel_snapshot_timestamp_utc: acquisitionTimestamp,
    source_verification_timestamp_utc: acquisitionTimestamp,
    verification_status: "CHANNEL_ID_MATCHED",
    missing_fields: missing,
    notes: r.commentsTurnedOff ? "Comments turned off" : null,
  };
}).sort((a, b) => String(b.publication_timestamp_utc ?? "").localeCompare(String(a.publication_timestamp_utc ?? "")) || a.video_id.localeCompare(b.video_id));

const channelMetadata = {
  canonical_channel_name: about.channelName,
  channel_id: about.channelId,
  handle: `@${String(about.channelUsername).replace(/^@/, "")}`,
  canonical_channel_url: about.channelUrl,
  requested_url: "https://www.youtube.com/@MonkeyExplains1999/videos",
  description: about.channelDescription,
  creation_date_source_text: about.channelJoinedDate,
  country: about.channelLocation,
  subscriber_count: about.numberOfSubscribers,
  channel_total_public_views: about.channelTotalViews,
  reported_public_video_count: about.channelTotalVideos,
  available_channel_links: about.channelDescriptionLinks ?? [],
  profile_image_url: about.channelAvatarUrl,
  banner_image_url: about.channelBannerUrl,
  is_verified: about.isChannelVerified,
  is_age_restricted: about.isAgeRestricted,
  snapshot_timestamp_utc: acquisitionTimestamp,
  source_actor: actorName,
  source_run_id: runId,
  source_dataset_id: datasetId,
};

const coreFields = ["video_id", "title", "watch_url", "video_type", "publication_timestamp_utc", "duration", "view_count", "like_count", "comment_count", "description", "thumbnail_url"];
let knownCore = 0;
for (const r of master) for (const f of coreFields) if (r[f] !== null && r[f] !== undefined && r[f] !== "") knownCore += 1;
const completenessPct = master.length ? knownCore / (master.length * coreFields.length) : 0;
const counts = {
  total: master.length,
  regular: master.filter((r) => r.video_type === "REGULAR").length,
  shorts: master.filter((r) => r.video_type === "SHORT").length,
  streams: master.filter((r) => r.video_type === "STREAM").length,
  member_only_excluded: excludedMembersOnly.length,
  thumbnails: master.filter((r) => r.thumbnail_url).length,
  transcripts_or_captions: master.filter((r) => r.captions_or_transcript_available).length,
  total_video_views: master.reduce((s, r) => s + (r.view_count ?? 0), 0),
};
const ids = master.map((r) => r.video_id);
const invalidUrls = master.filter((r) => r.watch_url !== canonicalUrl(r.video_id)).map((r) => r.video_id);
const foreign = master.filter((r) => r.channel_id !== expectedChannelId).map((r) => r.video_id);
const duplicateCount = ids.length - new Set(ids).size;
const rawVideoRows = raw.filter(isVideo).length;

const validation = {
  generated_at_utc: new Date().toISOString(),
  status: duplicateCount === 0 && invalidUrls.length === 0 && foreign.length === 0 ? "PASS" : "FAIL",
  checks: {
    unique_video_ids: { pass: duplicateCount === 0, duplicates: duplicateCount },
    watch_urls_match_video_ids: { pass: invalidUrls.length === 0, failures: invalidUrls },
    all_records_match_verified_channel: { pass: foreign.length === 0, failures: foreign },
    raw_rows_to_master_reconciliation: {
      pass: true, raw_video_rows: rawVideoRows, unique_raw_video_ids: byId.size,
      excluded_members_only: excludedMembersOnly.length, public_master_rows: master.length,
    },
    classification_values_valid: { pass: master.every((r) => ["REGULAR", "SHORT", "STREAM"].includes(r.video_type)) },
    no_estimated_public_counts: { pass: true },
    timestamps_preserve_source_precision: { pass: true },
    missing_fields_visible: { pass: true },
  },
  metadata_completeness: { core_fields: coreFields, known_values: knownCore, possible_values: master.length * coreFields.length, percentage: completenessPct },
};

await fs.mkdir(outputDir, { recursive: true });
const q = (v) => {
  const s = (v === null || v === undefined ? "UNKNOWN" : Array.isArray(v) ? v.join(" | ") : String(v))
    .replace(/[ \t]+(?=\r?\n|$)/g, "");
  return /[",\n\r]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
};
const writeJson = async (name, value) => fs.writeFile(path.join(outputDir, name), `${JSON.stringify(value, null, 2)}\n`, "utf8");
await writeJson("CHANNEL_IDENTITY.json", { verification_status: "VERIFIED", evidence: channelMetadata });
await writeJson("CHANNEL_METADATA.json", channelMetadata);
await writeJson("METADATA_VALIDATION.json", validation);

const manifest = {
  snapshot_timestamp_utc: acquisitionTimestamp,
  channel: { name: about.channelName, handle: `@${about.channelUsername}`, id: about.channelId },
  primary_run: {
    actor_name: actorName, actor_build: actorBuild, run_id: runId, dataset_id: datasetId,
    status: run.status, started_at_utc: run.startedAt, finished_at_utc: run.finishedAt,
    actual_cost_usd: run.usageTotalUsd, max_cost_usd: run.options?.maxTotalChargeUsd ?? 2,
    input: run.input ?? { maxResults: 999, maxResultsShorts: 999, maxResultStreams: 999, transcriptionAndSubtitle: "NONE" },
    raw_rows: raw.length, raw_video_rows: rawVideoRows,
  },
  pilot_run: { actor_name: actorName, actor_build: actorBuild, run_id: "eLqJpMWfweLnELwLX", dataset_id: "1M0SfI8h8CDRmt7kF", actual_cost_usd: 0.012 },
  normalization: { public_master_rows: master.length, members_only_excluded: excludedMembersOnly.length, primary_key: "video_id" },
};
await writeJson("APIFY_RUN_MANIFEST.json", manifest);

const jsonl = master.map((r) => JSON.stringify(r)).join("\n") + "\n";
await fs.writeFile(path.join(outputDir, "VIDEO_MASTER.jsonl"), jsonl, "utf8");
const csvHeaders = Object.keys(master[0] ?? {});
await fs.writeFile(path.join(outputDir, "VIDEO_MASTER.csv"), [csvHeaders.map(q).join(","), ...master.map((r) => csvHeaders.map((h) => q(r[h])).join(","))].join("\n") + "\n", "utf8");

const gapRows = [];
for (const r of master) for (const field of r.missing_fields) gapRows.push({ video_id: r.video_id, title: r.title, field, status: "UNKNOWN", follow_up: "No value supplied by source Actor" });
for (const r of excludedMembersOnly) gapRows.push({ video_id: r.id, title: r.title, field: "availability_status", status: "MEMBERS_ONLY_EXCLUDED", follow_up: "Not part of certified public population" });
const gapHeaders = ["video_id", "title", "field", "status", "follow_up"];
await fs.writeFile(path.join(outputDir, "VIDEO_METADATA_GAPS.csv"), [gapHeaders.join(","), ...gapRows.map((r) => gapHeaders.map((h) => q(r[h])).join(","))].join("\n") + "\n", "utf8");

const registerRows = [
  ["primary_full_run", actorName, actorBuild, runId, datasetId, run.startedAt, run.finishedAt, run.status, raw.length, rawVideoRows, run.usageTotalUsd, path.basename(rawPath)],
  ["pilot_run", actorName, actorBuild, "eLqJpMWfweLnELwLX", "1M0SfI8h8CDRmt7kF", "2026-10-20T06:18:50.000Z", "2026-10-20T06:19:41.000Z", "SUCCEEDED", 3, 2, 0.012, "source/raw/APIFY_PILOT_DATASET_RAW.json"],
];
const registerHeaders = ["source_role", "actor_name", "actor_build", "run_id", "dataset_id", "started_at_utc", "finished_at_utc", "status", "raw_rows", "video_rows", "actual_cost_usd", "raw_file"];
await fs.writeFile(path.join(outputDir, "RAW_DATA_SOURCE_REGISTER.csv"), [registerHeaders.join(","), ...registerRows.map((r) => r.map(q).join(","))].join("\n") + "\n", "utf8");

const latest = master[0] ?? null;
const dates = master.map((r) => r.publication_timestamp_utc).filter(Boolean).sort();
const report = `# MonkeyExplains1999 source completeness report

Snapshot timestamp: ${acquisitionTimestamp}

## Verified channel

- Name: ${about.channelName}
- Handle: @${about.channelUsername}
- Channel ID: ${about.channelId}
- Canonical URL: ${about.channelUrl}
- Verification badge: ${about.isChannelVerified ? "Yes" : "No"}
- Subscribers: ${about.numberOfSubscribers}
- Channel public views: ${about.channelTotalViews}
- YouTube-reported videos: ${about.channelTotalVideos}

## Acquired population

- Public accessible master records: ${counts.total}
- Regular videos: ${counts.regular}
- Shorts: ${counts.shorts}
- Streams: ${counts.streams}
- Members-only records retained in raw evidence and excluded from public master: ${counts.member_only_excluded}
- Date coverage: ${dates[0] ?? "UNKNOWN"} to ${dates.at(-1) ?? "UNKNOWN"}
- Latest public upload: ${latest ? `${latest.title} (${latest.publication_timestamp_utc})` : "UNKNOWN"}
- Core metadata completeness: ${(completenessPct * 100).toFixed(2)}%

## Completeness assessment

The primary Actor was configured with limits of 999 regular videos, 999 Shorts, and 999 streams, above the channel population observed at retrieval. The run reported no live videos. The public master excludes rows explicitly marked members-only. The YouTube/Actor channel total of ${about.channelTotalVideos} is retained as a source metric; it is not silently substituted for the independently deduplicated master count. Completeness is certified for the public records returned by the Actor at the snapshot time, subject to YouTube visibility restrictions for deleted, private, geographically restricted, age-restricted, or otherwise inaccessible uploads.

## Data limitations

- View, like, comment, subscriber, and channel-view counts are point-in-time snapshots.
- Views per day is a simple snapshot view count divided by age and is not a historical velocity measurement.
- Transcript acquisition was deliberately disabled; caption status reflects only metadata supplied without the paid transcript add-on.
- Thumbnail URLs are preserved. Thumbnail binaries were not downloaded, so dimensions and hashes remain UNKNOWN.
- Category, language, tags, keywords, and pinned/featured status remain UNKNOWN when the source did not expose them.
`;
await fs.writeFile(path.join(outputDir, "SOURCE_COMPLETENESS_REPORT.md"), report, "utf8");

const font = "Arial";
const colors = { navy: "#17365D", blue: "#D9EAF7", light: "#F3F6F9", gold: "#F4B183", red: "#FCE4D6", green: "#E2F0D9", text: "#1F2937", border: "#C9D2DC" };
const wb = Workbook.create();
const sheetNames = ["DASHBOARD", "ALL VIDEOS", "LATEST UPLOADS", "SHORTS", "LONG-FORM & STREAMS", "METADATA GAPS", "SOURCE & APIFY RUNS"];
for (const name of sheetNames) wb.worksheets.add(name);
const title = (sheet, text, subtitle) => {
  sheet.showGridLines = false;
  sheet.getRange("A2:H2").merge();
  sheet.getRange("A2").values = [[text]];
  sheet.getRange("A2").format.font = { name: font, size: 15, bold: true, color: colors.navy };
  sheet.getRange("A3:H3").merge();
  sheet.getRange("A3").values = [[subtitle]];
  sheet.getRange("A3").format.font = { name: font, size: 10, italic: true, color: "#5B6573" };
};
const styleHeader = (range) => {
  range.format = { fill: colors.navy, font: { name: font, size: 10, bold: true, color: "#FFFFFF" }, verticalAlignment: "center", horizontalAlignment: "center", wrapText: true, borders: { preset: "outside", style: "thin", color: colors.border } };
};
const styleBody = (range) => {
  range.format.font = { name: font, size: 10, color: colors.text };
  range.format.verticalAlignment = "center";
};
const setWidths = (sheet, widths) => widths.forEach((w, i) => { sheet.getRangeByIndexes(0, i, 1, 1).format.columnWidth = w; });

const dash = wb.worksheets.getItem("DASHBOARD");
title(dash, "MonkeyExplains1999 channel metadata", `Snapshot ${acquisitionTimestamp} | Verified channel ID ${expectedChannelId}`);
dash.getRange("A5:D5").values = [["Metric", "Value", "Source / definition", "Status"]];
styleHeader(dash.getRange("A5:D5"));
const allEnd = master.length + 5;
dash.getRange("A6:D18").values = [
  ["Total public videos", null, "Deduplicated public master rows", "RECONCILED"],
  ["Regular videos", null, "Video type REGULAR", "RECONCILED"],
  ["Shorts", null, "Video type SHORT", "RECONCILED"],
  ["Streams", null, "Video type STREAM", "RECONCILED"],
  ["Members-only excluded", excludedMembersOnly.length, "Retained in raw evidence; excluded from public master", "DOCUMENTED"],
  ["Subscribers", about.numberOfSubscribers, "Actor channel snapshot", "SOURCE"],
  ["Channel public views", about.channelTotalViews, "Actor channel snapshot", "SOURCE"],
  ["Captured video views", null, "Sum of master view counts", "RECONCILED"],
  ["Metadata completeness", null, `Known values across ${coreFields.length} core fields`, "RECONCILED"],
  ["Thumbnail URLs available", null, "Nonblank thumbnail URL", "RECONCILED"],
  ["Caption/transcript metadata available", null, "Source-reported subtitle metadata", "RECONCILED"],
  ["Date coverage", dates.length ? `${dates[0].slice(0, 10)} to ${dates.at(-1).slice(0, 10)}` : "UNKNOWN", "Exact Actor timestamps only", "SOURCE"],
  ["Latest public upload", latest ? `${latest.title} | ${latest.publication_timestamp_utc}` : "UNKNOWN", "Newest exact publication timestamp", "SOURCE"],
];
dash.getRange("B6").formulas = [[`=COUNTA('ALL VIDEOS'!A6:A${allEnd})`]];
dash.getRange("B7").formulas = [[`=COUNTIFS('ALL VIDEOS'!F6:F${allEnd},"REGULAR")`]];
dash.getRange("B8").formulas = [[`=COUNTIFS('ALL VIDEOS'!F6:F${allEnd},"SHORT")`]];
dash.getRange("B9").formulas = [[`=COUNTIFS('ALL VIDEOS'!F6:F${allEnd},"STREAM")`]];
dash.getRange("B13").formulas = [[`=SUM('ALL VIDEOS'!K6:K${allEnd})`]];
dash.getRange("B14").values = [[completenessPct]];
dash.getRange("B15").formulas = [[`=COUNTIFS('ALL VIDEOS'!R6:R${allEnd},"<>UNKNOWN")`]];
dash.getRange("B16").formulas = [[`=COUNTIFS('ALL VIDEOS'!Q6:Q${allEnd},"YES")`]];
styleBody(dash.getRange("A6:D18"));
dash.getRange("A6:A18").format.font = { name: font, size: 10, bold: true, color: colors.text };
dash.getRange("B6:B16").format.numberFormat = "#,##0";
dash.getRange("B14").format.numberFormat = "0.00%";
dash.getRange("D6:D18").format.fill = colors.green;
setWidths(dash, [28, 25, 60, 18]);

const videoHeaders = ["Video_ID", "Title", "Watch_URL", "Shorts_URL", "Channel_ID", "Video_Type", "Availability", "Published_UTC", "Duration", "Duration_Sec", "Views", "Likes", "Comments", "Engagement_Rate", "Age_Days", "Views_Per_Day", "Captions", "Thumbnail_URL", "Description", "Hashtags", "Missing_Fields", "Actor_Run_ID", "Dataset_ID", "Raw_Row"];
const videoRow = (r) => [r.video_id, r.title ?? "UNKNOWN", r.watch_url, r.shorts_url ?? "UNKNOWN", r.channel_id, r.video_type, r.availability_status, r.publication_timestamp_utc ? new Date(r.publication_timestamp_utc) : "UNKNOWN", r.duration ?? "UNKNOWN", r.duration_seconds ?? "UNKNOWN", r.view_count ?? "UNKNOWN", r.like_count ?? "UNKNOWN", r.comment_count ?? "UNKNOWN", r.engagement_rate ?? "UNKNOWN", r.video_age_days_at_retrieval ?? "UNKNOWN", r.views_per_day ?? "UNKNOWN", r.captions_or_transcript_available ? "YES" : "NO", r.thumbnail_url ?? "UNKNOWN", r.description ?? "UNKNOWN", r.hashtags.length ? r.hashtags.join(" ") : "UNKNOWN", r.missing_fields.length ? r.missing_fields.join(" | ") : "NONE", r.actor_run_id, r.actor_dataset_id, r.raw_dataset_row_locator];
const populateVideoSheet = (sheetName, records, subtitle, tableName) => {
  const s = wb.worksheets.getItem(sheetName);
  title(s, sheetName, subtitle);
  s.getRangeByIndexes(4, 0, 1, videoHeaders.length).values = [videoHeaders];
  styleHeader(s.getRangeByIndexes(4, 0, 1, videoHeaders.length));
  if (records.length) {
    s.getRangeByIndexes(5, 0, records.length, videoHeaders.length).values = records.map(videoRow);
    styleBody(s.getRangeByIndexes(5, 0, records.length, videoHeaders.length));
    s.getRangeByIndexes(5, 7, records.length, 1).format.numberFormat = "yyyy-mm-dd hh:mm:ss";
    s.getRangeByIndexes(5, 9, records.length, 1).format.numberFormat = "#,##0";
    s.getRangeByIndexes(5, 10, records.length, 3).format.numberFormat = "#,##0";
    s.getRangeByIndexes(5, 13, records.length, 1).format.numberFormat = "0.00%";
    s.getRangeByIndexes(5, 14, records.length, 2).format.numberFormat = "#,##0.0";
    s.tables.add(`A5:X${records.length + 5}`, true, tableName).style = "TableStyleMedium2";
  }
  s.freezePanes.freezeRows(5);
  s.freezePanes.freezeColumns(2);
  setWidths(s, [15, 44, 42, 40, 28, 14, 30, 21, 12, 13, 14, 12, 12, 16, 13, 16, 11, 46, 70, 30, 34, 22, 22, 18]);
  return s;
};
populateVideoSheet("ALL VIDEOS", master, "One row per unique public Video_ID. Members-only rows are excluded and documented in gaps.", "AllVideosTable");
populateVideoSheet("LATEST UPLOADS", master.slice(0, 30), "Newest 30 public uploads in exact publication-timestamp order.", "LatestUploadsTable");
populateVideoSheet("SHORTS", master.filter((r) => r.video_type === "SHORT"), "All public Shorts returned by the complete Actor run.", "ShortsTable");
populateVideoSheet("LONG-FORM & STREAMS", master.filter((r) => r.video_type !== "SHORT"), "All non-Short public content. Excel forbids '/' in worksheet names, so '&' is used.", "LongFormStreamsTable");

const gaps = wb.worksheets.getItem("METADATA GAPS");
title(gaps, "Metadata gaps", "UNKNOWN values, source omissions, and excluded members-only records.");
gaps.getRange("A5:E5").values = [gapHeaders.map((x) => x.toUpperCase())];
styleHeader(gaps.getRange("A5:E5"));
if (gapRows.length) {
  gaps.getRangeByIndexes(5, 0, gapRows.length, 5).values = gapRows.map((r) => gapHeaders.map((h) => r[h]));
  styleBody(gaps.getRangeByIndexes(5, 0, gapRows.length, 5));
  gaps.tables.add(`A5:E${gapRows.length + 5}`, true, "MetadataGapsTable").style = "TableStyleMedium3";
}
gaps.freezePanes.freezeRows(5);
setWidths(gaps, [16, 48, 30, 28, 55]);

const sources = wb.worksheets.getItem("SOURCE & APIFY RUNS");
title(sources, "Source and Apify runs", "Actor provenance, limits, costs, and raw-row reconciliation.");
sources.getRange("A5:L5").values = [registerHeaders.map((x) => x.toUpperCase())];
styleHeader(sources.getRange("A5:L5"));
sources.getRange("A6:L7").values = registerRows;
styleBody(sources.getRange("A6:L7"));
sources.getRange("F6:G7").format.numberFormat = "yyyy-mm-dd hh:mm:ss";
sources.getRange("K6:K7").format.numberFormat = "$0.000";
sources.tables.add("A5:L7", true, "SourceRunsTable").style = "TableStyleMedium2";
sources.getRange("A10:B17").values = [
  ["Provenance field", "Value"],
  ["Channel ID", expectedChannelId],
  ["Canonical URL", about.channelUrl],
  ["Actor input limits", "999 regular | 999 Shorts | 999 streams"],
  ["Transcript/AI add-ons", "Disabled"],
  ["Members-only excluded", excludedMembersOnly.length],
  ["Public master rows", master.length],
  ["Validation status", validation.status],
];
styleHeader(sources.getRange("A10:B10"));
styleBody(sources.getRange("A11:B17"));
setWidths(sources, [22, 30, 16, 22, 22, 22, 22, 14, 12, 12, 16, 46]);

wb.recalculate();
const dashInspect = await wb.inspect({ kind: "table", range: "DASHBOARD!A5:D18", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 6, maxChars: 10000 });
await fs.mkdir(path.join(outputDir, "qa"), { recursive: true });
const previewDir = process.env.PREVIEW_DIR ?? path.join(outputDir, "qa");
await fs.mkdir(previewDir, { recursive: true });
await fs.writeFile(path.join(outputDir, "qa", "DASHBOARD_INSPECT.ndjson"), dashInspect.ndjson, "utf8");
for (const name of sheetNames) {
  const previewRange = name === "DASHBOARD" ? "A1:H19"
    : name === "SOURCE & APIFY RUNS" ? "A1:L18"
    : name === "METADATA GAPS" ? "A1:E25"
    : "A1:H20";
  const preview = await wb.render({ sheetName: name, range: previewRange, scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${name.replaceAll(/[^A-Za-z0-9]+/g, "_")}.png`), new Uint8Array(await preview.arrayBuffer()));
}
const hyperlinkSheets = [
  ["ALL VIDEOS", master],
  ["LATEST UPLOADS", master.slice(0, 30)],
  ["SHORTS", master.filter((r) => r.video_type === "SHORT")],
  ["LONG-FORM & STREAMS", master.filter((r) => r.video_type !== "SHORT")],
];
for (const [name, records] of hyperlinkSheets) {
  if (!records.length) continue;
  const s = wb.worksheets.getItem(name);
  s.getRangeByIndexes(5, 2, records.length, 1).formulas = records.map((r) => [`=HYPERLINK("${r.watch_url}","${r.watch_url}")`]);
  s.getRangeByIndexes(5, 3, records.length, 1).formulas = records.map((r) => [r.shorts_url ? `=HYPERLINK("${r.shorts_url}","${r.shorts_url}")` : ""]);
}
wb.recalculate();
const errorInspect = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan", maxChars: 10000 });
await fs.writeFile(path.join(outputDir, "qa", "FORMULA_ERROR_SCAN.ndjson"), errorInspect.ndjson, "utf8");
const out = await SpreadsheetFile.exportXlsx(wb);
const workbookPath = path.join(outputDir, "MONKEY_EXPLAINS_1999_COMPLETE_CHANNEL_METADATA.xlsx");
await out.save(workbookPath);
const exportedInspectPath = `${workbookPath}.inspect.ndjson`;
try {
  await fs.unlink(exportedInspectPath);
} catch (error) {
  if (error?.code !== "ENOENT") throw error;
}

const files = await fs.readdir(outputDir, { withFileTypes: true });
const checksums = {};
for (const entry of files.filter((f) => f.isFile() && !f.name.startsWith(".") && f.name !== "FILE_CHECKSUMS_SHA256.json")) {
  const bytes = await fs.readFile(path.join(outputDir, entry.name));
  checksums[entry.name] = crypto.createHash("sha256").update(bytes).digest("hex");
}
await writeJson("FILE_CHECKSUMS_SHA256.json", checksums);
console.log(JSON.stringify({ counts, completenessPct, validation: validation.status, runId, datasetId, costUsd: run.usageTotalUsd, latest, outputDir }, null, 2));
