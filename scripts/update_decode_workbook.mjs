import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const file = "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Analytical_Workbook.xlsx";
const register = JSON.parse(await fs.readFile("docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Video_Evidence_Register.json", "utf8"));
const checkpoint = JSON.parse(await fs.readFile("docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json", "utf8"));
const trends = JSON.parse(await fs.readFile("data/raw/competitors/DS-000032/public-browser-2026-09-27/google-trends/trends-analysis.json", "utf8"));
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const headerFmt = { fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" }, wrapText: true, verticalAlignment: "center" };
const bodyFmt = { wrapText: true, verticalAlignment: "top" };

const dash = wb.worksheets.getItem("Dashboard");
dash.getRange("A13:F20").unmerge();
dash.getRange("A13:B20").values = [
  ["Studio analytics", "AUTHORIZED BULK EXPORTS INGESTED — lifetime / 90d / 28d / traffic source"],
  [null, null], ["Executive diagnosis", null],
  ["1", "Discovery volume constrained: 36,159 lifetime thumbnail impressions across 56 videos; Search and Suggested dominate recorded impressions."],
  ["2", "Packaging response uneven: lifetime CTR 3.0%, with material video-level variation. CTR is not sole bottleneck."],
  ["3", "All 56 retained thumbnails recovered and visually inspected. Authority cues strong; repeated template and Shorts frame-grabs limit differentiation."],
  ["4", "Concrete tests, symptoms and practical problems lead several long-form outcomes; topic, age and distribution remain confounded."],
  ["5", `Retention: ${register.counts.retention_exports} exports, ${register.counts.retention_curves} curves. Playback: ${register.counts.investigation_status.RETENTION_ANALYZED} RETENTION_ANALYZED, ${register.counts.investigation_status.PARTIAL_PLAYBACK} PARTIAL_PLAYBACK, ${register.counts.investigation_status.TRANSCRIPT_ONLY} TRANSCRIPT_ONLY; no claim made from transcripts alone.`],
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
  ["YouTube search terms / suggested videos", "MISSING", "Video/query", "Studio export", "Needed to identify discovery pathways"],
  ["New / casual / regular / returning viewers", "MISSING", "Channel/video", "Studio audience report", "Needed to test relationship development"],
  ["Shorts engaged views / stayed to watch", "PARTIAL", "Video rows", "Authenticated Studio table observation 2026-09-28", `${register.counts.studio_extended_rows_observed} extended rows observed; browser-observed, no CSV`],
  ["Geography/language/device", "MISSING", "Channel/video", "Studio audience reports", "Needed to verify intended versus actual audience"],
];
own.getRange("A3:E15").format = bodyFmt;
own.getRange("A3:E3").format = headerFmt;

const thumb = wb.worksheets.getItem("Thumbnail Forensics");
const thHeaders = ["Video ID","Title","Thumbnail URL","URL status","Actual image","Visual inspection","Visible text","Readability","Composition","Subject / imagery","Authority cues","Color / contrast","Focal point / hierarchy","Title relationship","Audience / curiosity","Competitor comparison"];
const thRows = register.records.map(r => { const o=r.thumbnail_observation; return [r.video_id,r.title_at_acquisition,r.thumbnail_image_path,"AVAILABLE","RECOVERED","COMPLETE",o.visible_text,o.text_readability,o.composition,o.subject_and_imagery,o.medical_authority_cues,o.color_and_contrast,o.focal_point+"; "+o.visual_hierarchy,o.title_relationship,o.intended_audience+"; "+o.curiosity_and_disclosure,o.competitor_comparison]; });
thumb.getRange("A1:P57").values = [thHeaders, ...thRows];
thumb.getRange("A1:P57").format = bodyFmt;
thumb.getRange("A1:P1").format = headerFmt;
thumb.getRange("A1:P57").format.font.size = 9;

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
const dx = checkpoint.diagnosis.map((d,i)=>[i+1,d.finding,"EVIDENCE-SYNTHESIS",d.metrics,d.counterexample,d.confidence,"Retention/query/audience exports where stated"]);
root.getRange(`A1:G${dx.length+1}`).values = [["Priority","Hypothesis/finding","Evidence class","Support","Counterevidence / alternatives","Confidence","Data needed"],...dx];
root.getRange(`A1:G${dx.length+1}`).format = bodyFmt;
root.getRange("A1:G1").format = headerFmt;

const gaps = wb.worksheets.getItem("Evidence Gaps");
gaps.getRange("A1:E10").values = [
  ["Gap","Scope","Current evidence","Priority","Required action"],
  ["Individual retention curves","Prioritized winners/failures","Bulk AVD/APV derived; curves not exported","Critical","Owner-authorized Studio inspection/export"],
  ["Shorts stayed-to-watch","29 Shorts","Views/watch time available; swipe behavior missing","Critical","Studio Shorts report"],
  ["Full playback/editing audit","56 videos","Public URLs verified; transcript/thumbnail coverage complete; playback audit incomplete","High","Continue public player review; no owner upload requested"],
  ["Search queries / suggested sources","Channel/video","Traffic-source totals available; query/referrer detail missing","High","Studio query and suggested-video exports"],
  ["Viewer relationship","Channel","Subscriber totals available; new/returning and cross-format overlap missing","High","Studio Audience reports"],
  ["Thumbnail visuals","56 videos","RECOVERED + INSPECTED","CLOSED","None"],
  ["Google Trends","9 configured term series","Official CSVs recovered","CLOSED","None; preserve normalization caveat"],
  ["Current public catalog","Channel","56 current videos; zero new vs retained 56","CLOSED","Observe future snapshots separately"],
  ["Raw source integrity","DS-000032","Raw acquisition preserved","ONGOING","Never overwrite raw source records"],
];
gaps.getRange("A1:E10").format = bodyFmt; gaps.getRange("A1:E1").format = headerFmt;

const ev = wb.worksheets.getItem("Video Evidence Register");
const evHeaders = ["Video ID","URL","Type","Title","Published","Canonical metadata","Description","Transcript","Thumbnail URL","Actual image","Thumbnail inspected","Watch page","Video reviewed","Editing notes","Trends","Studio analytics","Retention curve","Remaining gap"];
const evRows = register.records.map(r=>[r.video_id,r.public_url,r.type,r.title_at_acquisition,r.published_at,"AVAILABLE","AVAILABLE","AVAILABLE","AVAILABLE","AVAILABLE","COMPLETE",r.public_watch_page_accessible,r.investigation_status,r.editing_observations_recorded,r.google_trends_research,r.relevant_private_studio_analytics,r.retention_curve,r.remaining_gap]);
ev.getRange("A1:R57").values = [evHeaders,...evRows]; ev.getRange("A1:R57").format=bodyFmt; ev.getRange("A1:R1").format=headerFmt; ev.getRange("A1:R57").format.font.size=9;

const cp = wb.worksheets.getItem("Research Checkpoint");
const cpRows = Object.entries(checkpoint.phase_status).map(([k,v])=>[k.replaceAll("_"," "),v,"See JSON checkpoint and cited raw evidence"]);
cp.getRange(`A1:C${cpRows.length+1}`).values = [["Work item","Status","Detail"],...cpRows]; cp.getRange(`A1:C${cpRows.length+1}`).format=bodyFmt; cp.getRange("A1:C1").format=headerFmt;

wb.recalculate();
for (const range of ["Dashboard!A1:F22", "Own-Channel Analytics!A1:E15", "Thumbnail Forensics!A1:P8", "Google Trends Research!A1:J12", "Evidence Gaps!A1:E10", "Video Evidence Register!A1:R6"]) {
  const check = await wb.inspect({kind:"table",range,include:"values,formulas",tableMaxRows:20,tableMaxCols:20});
  process.stdout.write(check.ndjson+"\n");
}
const errors = await wb.inspect({kind:"match",searchTerm:"#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",options:{useRegex:true,maxResults:300},summary:"final formula error scan"});
process.stdout.write(errors.ndjson+"\n");
await fs.mkdir("/private/tmp/decode-heart-workbook-render", { recursive: true });
for (const [name, sheetName, range] of [
  ["dashboard", "Dashboard", "A1:F30"], ["analytics", "Own-Channel Analytics", "A1:E15"],
  ["thumbnails", "Thumbnail Forensics", "A1:P10"], ["trends", "Google Trends Research", "A1:J13"],
  ["gaps", "Evidence Gaps", "A1:E10"], ["register", "Video Evidence Register", "A1:R8"],
]) {
  const image = await wb.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(`/private/tmp/decode-heart-workbook-render/${name}.png`, new Uint8Array(await image.arrayBuffer()));
}
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(file);
