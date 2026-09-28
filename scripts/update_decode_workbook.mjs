import fs from "node:fs/promises";
import { homedir } from "node:os";
const { FileBlob, SpreadsheetFile } = await import(process.env.ARTIFACT_TOOL_PATH ?? `${homedir()}/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs`);

const file = "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Analytical_Workbook.xlsx";
const register = JSON.parse(await fs.readFile("docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Video_Evidence_Register.json", "utf8"));
const checkpoint = JSON.parse(await fs.readFile("docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json", "utf8"));
const trends = JSON.parse(await fs.readFile("data/raw/competitors/DS-000032/public-browser-2026-09-27/google-trends/trends-analysis.json", "utf8"));
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const headerFmt = { fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" }, wrapText: true, verticalAlignment: "center" };
const bodyFmt = { wrapText: true, verticalAlignment: "top" };

const sup = checkpoint.studio_supplementary_2026_09_28;
const dash = wb.worksheets.getItem("Dashboard");
dash.getRange("A13:F20").unmerge();
dash.getRange("A13:B20").values = [
  ["Studio analytics", "AUTHORIZED EXPORTS INGESTED — lifetime / 90d / 28d / traffic source; 2026-09-28 extended content, search, suggested, geography, device, age, audience"],
  [null, null], ["Executive diagnosis", null],
  ["1", "Reach is small and fragmented: 36,159 lifetime impressions; 114 disclosed search terms carry 170 views; own videos supplied 70 of 1,031 Suggested views. No evidence of algorithmic preference or penalty."],
  ["2", "Packaging weakness is video-specific, not channel-wide: EB3_A2b4a6o CTR 1.81% on 3,703 impressions despite 60.0% 30 s retention. Shorts CTR is excluded (feed views carry no impressions)."],
  ["3", "Associations, not causes: early specific payoff (BCNWQ3uuSuE 60.5% vs SBrMW71O69U 38.46% at 30 s) holds viewers; cutting pace, topic label and caption defects do not separate videos."],
  ["4", `Medical review: ${register.counts.medical_claim_reviews} claims in ${register.counts.videos_with_medical_claim_review} videos; ${register.counts.medical_claims_requiring_action} need action (HzFdyjyEFTY aspirin stop advice, hUSVbcHVeVw reverse title, 7MXBh2hjfto title, 8JdBlF-ragM speculative side effect).`],
  ["5", `Audience development is unproven: ${sup.audience_28_day.new_viewers_latest} new, ${sup.audience_28_day.casual_viewers_latest} casual, ${sup.audience_28_day.regular_viewers_latest} regular in 28 days; regular = 0 is expected for an 8-month channel. Geography disclosed for 32.8% of views only. Audio not heard; complete AV audits ${register.counts.complete_audiovisual_audits_verified}.`],
];
dash.getRange("A1:A30").format.columnWidth = 28;
dash.getRange("B1:B30").format.columnWidth = 115;
dash.getRange("A13:B20").format.wrapText = true;
dash.getRange("A13:B20").format.autofitRows();
dash.getRange("A15:F15").merge();
for (let row = 16; row <= 20; row++) dash.getRange(`B${row}:F${row}`).merge();
dash.getRange("B16:F20").format = { wrapText: true, horizontalAlignment: "left", verticalAlignment: "center", font: { color: "#000000", size: 10 } };
dash.getRange("A16:F20").format.rowHeight = 42;

const own = wb.worksheets.getItem("Own-Channel Analytics");
own.getRange("A3:E15").values = [
  ["Metric", "Status", "Scope", "Source", "Interpretation"],
  ["Public views", "AVAILABLE", "56 videos", "DS-000032 + Studio", "Public snapshot and first-party lifetime views kept distinct"],
  ["Publication date/duration/type", "AVAILABLE", "56 videos", "DS-000032", "Verified in retained source package"],
  ["Impressions", "AVAILABLE", "Channel + video rows", "Studio Advanced Mode exports", "36,159 lifetime; 18,579 last 90d; 4,360 last 28d"],
  ["Impressions CTR", "AVAILABLE", "Channel + video rows", "Studio Advanced Mode exports", "3.0% lifetime/90d; 3.2% last 28d; interpret with source"],
  ["Watch time", "AVAILABLE", "Channel + video rows", "Studio Advanced Mode exports", "45.6 lifetime hours; 22.7 last 90d; 8.0 last 28d"],
  ["Average view duration / % viewed", "DERIVED FROM EXPORT", "Video rows", "Views + watch hours + duration", "Rounding-sensitive; not replacement for retention curve"],
  ["Audience retention / first 30s", "AVAILABLE", "Per video", "Studio individual retention exports", `${register.counts.retention_curves} curves of ${register.counts.retention_exports} exports; remainder disclosed no rows`],
  ["Traffic sources", "AVAILABLE", "Lifetime channel", "Studio traffic-source export", "Shorts feed 5,355 views; Search 1,175; Suggested 1,031; Browse 405"],
  ["YouTube search terms / suggested videos", "AVAILABLE (CHANNEL)", "Channel drill-down", "Studio exports 2026-09-28", `Search ${sup.search_terms.total_search_views} views, CTR ${sup.search_terms.search_ctr_percent}%, ${sup.search_terms.disclosed_terms} terms carry ${sup.search_terms.views_in_disclosed_terms} views; Suggested ${sup.suggested_sources.total_suggested_views} views, own-channel sources ${sup.suggested_sources.own_channel_views}`],
  ["New / casual / regular / returning viewers", "AVAILABLE (CHANNEL, 28 DAYS)", "Channel + per-video retention segments", "Studio audience export 2026-09-28 + retention exports", `${sup.audience_28_day.new_viewers_latest} new, ${sup.audience_28_day.casual_viewers_latest} casual, ${sup.audience_28_day.regular_viewers_latest} regular; ${register.counts.retention_new_vs_returning_split} videos carry a new-vs-returning retention split`],
  ["Shorts engaged views / stayed to watch", "AVAILABLE", "Video rows", "Studio CSV export 2026-09-28", `${register.counts.studio_extended_rows_observed} of 56 extended rows exported; reconciled with 47 browser-observed rows`],
  ["Geography/device/age", "AVAILABLE (CHANNEL)", "Channel", "Studio exports 2026-09-28", `Disclosed IN ${sup.geography.disclosed[0].share_percent}%; ${sup.geography.undisclosed_views} views undisclosed; language and per-video audience unavailable`],
];
own.getRange("A3:E15").format = bodyFmt;
own.getRange("A3:E3").format = headerFmt;

const thumb = wb.worksheets.getItem("Thumbnail Forensics");
const thHeaders = ["Video ID","Title","Thumbnail URL","URL status","Actual image","Visual inspection","Visible text","Readability","Composition","Subject / imagery","Authority cues","Color / contrast","Focal point / hierarchy","Title relationship","Audience / curiosity","Competitor comparison","Image-specific observation (2026-09-28)"];
const thRows = register.records.map(r => { const o=r.thumbnail_observation; return [r.video_id,r.title_at_acquisition,r.thumbnail_image_path,"AVAILABLE","RECOVERED","COMPLETE",o.visible_text,o.text_readability,o.composition,o.subject_and_imagery,o.medical_authority_cues,o.color_and_contrast,o.focal_point+"; "+o.visual_hierarchy,o.title_relationship,o.intended_audience+"; "+o.curiosity_and_disclosure,o.competitor_comparison,o.revalidation_observation ?? "NOT REVALIDATED"]; });
thumb.getRange("A1:Q57").values = [thHeaders, ...thRows];
thumb.getRange("A1:Q57").format = bodyFmt;
thumb.getRange("A1:Q1").format = headerFmt;
thumb.getRange("A1:Q57").format.font.size = 9;
thumb.getRange("Q1:Q57").format.columnWidth = 60;

const gt = wb.worksheets.getItem("Google Trends Research");
gt.getRange("A1:J30").unmerge();
const gtRows = [["Query","Geo","Range","Property","Observation date","Status","Mean normalized score","Max","Evidence file","Interpretation limit"]];
for (const [name, item] of Object.entries(trends.files)) for (const [query, s] of Object.entries(item.series)) gtRows.push([query.replace(": (United States)",""),"United States","Past 5 years","YouTube Search","2026-09-27","OFFICIAL CSV RECOVERED",s.mean,s.max,name,"0–100 normalized within comparison; not absolute volume or causal proof"]);
gt.getRange(`A1:J${gtRows.length}`).values = gtRows;
gt.getRange(`A1:J${gtRows.length}`).format = bodyFmt;
gt.getRange(`A2:J${gtRows.length}`).format.fill = "#FFFFFF";
gt.getRange(`A2:J${gtRows.length}`).format.font = { color: "#000000", size: 10 };
for (let row = 2; row <= gtRows.length; row += 2) gt.getRange(`A${row}:J${row}`).format.fill = "#D9EAF7";
gt.getRange("A1:J1").format = headerFmt;
for (const [col,width] of [["A",26],["B",18],["C",16],["D",20],["E",16],["F",26],["G",20],["H",10],["I",38],["J",48]]) gt.getRange(`${col}1:${col}${gtRows.length}`).format.columnWidth = width;
gt.getRange(`A1:J${gtRows.length}`).format.rowHeight = 34;

const root = wb.worksheets.getItem("Root-Cause Hypotheses");
const FV = checkpoint.final_validation_2026_09_28;
const dx = FV.root_cause_matrix.map(r=>[r.constraint,r.observation+" Scope: "+r.scope,r.supporting_evidence,r.counterexamples+" Confounders: "+r.confounders,r.interpretation,r.confidence,r.practical_response]);
root.getRange("A1:G40").values = Array.from({length:40},()=>Array(7).fill(null));
root.getRange(`A1:G${dx.length+1}`).values = [["Constraint","Observation / scope","Supporting evidence","Counterexamples / confounders","Interpretation","Confidence","Practical response"],...dx];
root.getRange(`A1:G${dx.length+1}`).format = bodyFmt;
root.getRange("A1:G1").format = headerFmt;

const gaps = wb.worksheets.getItem("Evidence Gaps");
gaps.getRange("A1:E12").values = [
  ["Gap","Scope","Current evidence","Priority","Required action"],
  ["Individual retention curves","56 videos",`${register.counts.retention_curves} curves in ${register.counts.retention_exports} retained exports; 10 disclosed no rows`,"CLOSED","None; all 46 curves are content-linked"],
  ["Shorts stayed-to-watch","29 Shorts",`${register.counts.studio_extended_rows_observed} of 56 extended rows in the 2026-09-28 CSV export`,"CLOSED","None"],
  ["Playback/editing audit","56 videos",`${register.counts.investigation_status.RETENTION_ANALYZED} RETENTION_ANALYZED, ${register.counts.investigation_status.LIMITED_BY_UNAVAILABLE_EVIDENCE} limited by no curve (${register.counts.playback_reported_full} reported full, ${register.counts.playback_seek_sampled} seek-sampled, ${register.counts.continuous_signal_passes} level/cut passes); ${register.counts.complete_audiovisual_audits_verified} verified complete audiovisual reviews; audio not heard`,"Medium","Heard continuous review only if a complete audiovisual audit is required"],
  ["Search queries / suggested sources","Channel/video","Channel-level drill-downs exported 2026-09-28; per-video drill-downs not exported","Low","Per-video drill-down only if a video-level source question arises"],
  ["Viewer relationship","Channel",`28-day: ${sup.audience_28_day.new_viewers_latest} new, ${sup.audience_28_day.casual_viewers_latest} casual, ${sup.audience_28_day.regular_viewers_latest} regular; regular requires >6 active months of the past 12, so 0 is expected at channel age`,"OPEN (hypothesis)","Re-export monthly from 2026-10-26 (R1); viewers-across-formats not exported"],
  ["Medical claim review","12 priority videos",`${register.counts.medical_claim_reviews} claims reviewed; ${register.counts.medical_claims_requiring_action} need action; 44 videos not reviewed`,"HIGH","Apply corrections Q1-Q4; review remaining 44 before any re-use"],
  ["Heard audio / complete AV audit","56 videos","Audio not heard; 12 priority reviews used storyboard frames plus transcripts","MEDIUM","Person-led listening review, or approval for local speech recognition (R4)"],
  ["Thumbnail visuals","56 videos","RECOVERED + INSPECTED","CLOSED","None"],
  ["Google Trends","9 configured term series","Official CSVs recovered","CLOSED","None; preserve normalization caveat"],
  ["Current public catalog","Channel","56 current videos; zero new vs retained 56","CLOSED","Observe future snapshots separately"],
  ["Raw source integrity","DS-000032","Raw acquisition preserved","ONGOING","Never overwrite raw source records"],
];
gaps.getRange("A1:E12").format = bodyFmt; gaps.getRange("A1:E1").format = headerFmt;

const ev = wb.worksheets.getItem("Video Evidence Register");
const evHeaders = ["Video ID","URL","Type","Title","Published","Canonical metadata","Description","Transcript","Thumbnail URL","Actual image","Thumbnail inspected","Watch page","Video reviewed","Editing notes","Trends","Studio analytics","Retention curve","Remaining gap"];
const evRows = register.records.map(r=>[r.video_id,r.public_url,r.type,r.title_at_acquisition,r.published_at,"AVAILABLE","AVAILABLE","AVAILABLE","AVAILABLE","AVAILABLE","COMPLETE",r.public_watch_page_accessible,r.investigation_status,r.editing_observations_recorded,r.google_trends_research,r.relevant_private_studio_analytics,r.retention_curve,r.remaining_gap]);
ev.getRange("A1:R57").values = [evHeaders,...evRows]; ev.getRange("A1:R57").format=bodyFmt; ev.getRange("A1:R1").format=headerFmt; ev.getRange("A1:R57").format.font.size=9;

const cp = wb.worksheets.getItem("Research Checkpoint");
const cpRows = Object.entries(checkpoint.phase_status).map(([k,v])=>[k.replaceAll("_"," "),v,"See JSON checkpoint and cited raw evidence"]);
for (const [dim, counts] of Object.entries(register.completeness_matrix)) cpRows.push([`evidence: ${dim.replaceAll("_"," ")}`, Object.entries(counts).map(([k,v])=>`${k} ${v}`).join("; "), "Per-video values in Video Evidence Register JSON (evidence_dimensions)"]);
cp.getRange(`A1:C${cpRows.length+1}`).values = [["Work item","Status","Detail"],...cpRows]; cp.getRange(`A1:C${cpRows.length+1}`).format=bodyFmt; cp.getRange("A1:C1").format=headerFmt;

function sheet(name) {
  let ws;
  try { ws = wb.worksheets.getItem(name); ws.getRange("A1:H120").values = Array.from({length:120},()=>Array(8).fill(null)); ws.charts.deleteAll(); }
  catch { ws = wb.worksheets.add(name); }
  return ws;
}
function writeTable(ws, headers, rows, widths) {
  const end = String.fromCharCode(64 + headers.length);
  ws.getRange(`A1:${end}${rows.length + 1}`).values = [headers, ...rows.map(r => r.map(v => v ?? ""))];
  ws.getRange(`A1:${end}${rows.length + 1}`).format = bodyFmt;
  ws.getRange(`A1:${end}1`).format = headerFmt;
  widths.forEach((w, i) => ws.getRange(`${String.fromCharCode(65 + i)}1:${String.fromCharCode(65 + i)}${rows.length + 1}`).format.columnWidth = w);
  ws.freezePanes.freezeRows(1);
}
writeTable(sheet("Claim Audit"), ["ID","Previous claim","Period / sample","Confounders","Counterexamples","Corrected interpretation","Status"],
  FV.claim_audit.map(c=>[c.id,c.previous_claim,c.period+"; "+c.sample_size,c.confounders,c.counterexamples,c.corrected_interpretation,c.status]), [6,40,34,40,40,50,16]);
const recs = Object.fromEntries(register.records.map(r=>[r.video_id,r]));
writeTable(sheet("Priority AV Reviews"), ["Video ID","Why selected","Coverage (audio not heard)","Timestamped observations","Retention link","Title promise","Finding"],
  FV.priority_review_video_ids.map(v=>{const p=recs[v].priority_review_2026_09_28;return [v,p.why_selected,p.coverage,p.timestamps.join("; "),p.retention_link,p.title_promise,p.finding];}), [14,34,30,70,40,34,40]);
writeTable(sheet("Medical Claim Review"), ["Video ID","Claim","Verdict","Evidence and analysis","Suggested wording","Priority"],
  FV.medical_claim_reviews.map(c=>[c.video_id,c.claim,c.verdict,c.evidence+". "+c.analysis,c.alternative_wording ?? "No change needed",c.priority]), [14,45,24,55,45,11]);
writeTable(sheet("Action Plan"), ["Type","ID","Item","Videos / scope","Evidence basis","Window","Metrics","Interpretation rule"], [
  ...FV.immediate_corrections.map(q=>["Immediate correction",q.id,q.action,q.video_id,q.evidence,"Days 1-30","Correction live","Quality fix; not a growth test"]),
  ...FV.experiments.map(e=>["Controlled experiment",e.id,e.name+": "+e.purpose,e.eligible_videos.join("; "),e.evidence_basis,e.window,e.metrics,e.interpretation]),
  ...FV.future_research.map(r=>["Future research",r.id,r.question,"Channel","Open question",r.requires,"",""]),
  ...FV.plan_30_60_90.map(p=>["30/60/90 plan","",p.actions,"",p.success_evidence,p.window,"",""]),
], [20,5,50,30,40,20,34,40]);
const lf = register.records.filter(r=>r.type==="video" && (r.studio_metrics?.impressions ?? 0) >= 500).map(r=>[r.video_id, r.studio_metrics.ctr_percent, Number(r.retention_evidence?.retention_at_30_seconds_percent ?? 0) || null, r.studio_metrics.impressions, r.studio_metrics.views, r.published_at.slice(0,10), r.published_at.slice(0,10) < "2026-08-28" ? "Mature (>30 days)" : "Immature (<30 days)"]).sort((a,b)=>b[3]-a[3]);
const perf = sheet("Long-form CTR vs Retention");
writeTable(perf, ["Video ID","CTR (%)","Retention at 30 s (%)","Impressions","Views","Published","Maturity at export"], lf, [14,10,14,12,10,12,18]);
const n = lf.length + 1;
perf.getRange(`A${n+2}:G${n+4}`).values = [
  ["Commentary", "Long-form videos with at least 500 lifetime impressions. Click response and 30-second retention do not move together: EB3_A2b4a6o and HzFdyjyEFTY combine low CTR with strong early retention, so for them packaging, not content, is the testable weakness (experiment E1).", null, null, null, null, null],
  ["Caution", "Lifetime CTR mixes Search and Suggested surfaces and video ages; 30-second retention rests on about 30-370 viewers per video (roughly +/-10 points at 100 viewers). Associations only.", null, null, null, null, null],
  ["Source", "Private Studio extended content export and retention exports (2026-09-27/28); see Video Evidence Register JSON.", null, null, null, null, null],
];
for (let r = n+2; r <= n+4; r++) perf.getRange(`B${r}:G${r}`).merge();
perf.getRange(`A${n+2}:G${n+4}`).format = { wrapText: true, verticalAlignment: "top" };
perf.getRange(`A${n+2}:G${n+4}`).format.rowHeight = 48;
const chart = perf.charts.add("scatter", [perf.getRange(`B1:B${n}`), perf.getRange(`C1:C${n}`)]);
chart.setPosition(`I2`, `Q22`);
chart.title = "Long-form: CTR vs 30-second retention (>=500 impressions)";
chart.xAxis = { title: { text: "Lifetime impressions CTR (%)" } };
chart.yAxis = { title: { text: "Retention at 30 s (%)" } };
chart.legend = { position: "bottom" };

wb.recalculate();
for (const range of ["Dashboard!A1:F22", "Own-Channel Analytics!A1:E15", "Thumbnail Forensics!A1:P8", "Google Trends Research!A1:J12", "Evidence Gaps!A1:E12", "Video Evidence Register!A1:R6", "Claim Audit!A1:G4", "Medical Claim Review!A1:F4", "Long-form CTR vs Retention!A1:G17"]) {
  const check = await wb.inspect({kind:"table",range,include:"values,formulas",tableMaxRows:20,tableMaxCols:20});
  process.stdout.write(check.ndjson+"\n");
}
const errors = await wb.inspect({kind:"match",searchTerm:"#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",options:{useRegex:true,maxResults:300},summary:"final formula error scan"});
process.stdout.write(errors.ndjson+"\n");
await fs.mkdir(process.env.RENDER_DIR ?? "/private/tmp/decode-heart-workbook-render", { recursive: true });
for (const [name, sheetName, range] of [
  ["dashboard", "Dashboard", "A1:F30"], ["analytics", "Own-Channel Analytics", "A1:E15"],
  ["thumbnails", "Thumbnail Forensics", "A1:P10"], ["trends", "Google Trends Research", "A1:J13"],
  ["gaps", "Evidence Gaps", "A1:E12"], ["register", "Video Evidence Register", "A1:R8"],
  ["ctr-retention", "Long-form CTR vs Retention", "A1:Q22"], ["medical", "Medical Claim Review", "A1:F8"],
]) {
  const image = await wb.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(`${process.env.RENDER_DIR ?? "/private/tmp/decode-heart-workbook-render"}/${name}.png`, new Uint8Array(await image.arrayBuffer()));
}
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(file);
