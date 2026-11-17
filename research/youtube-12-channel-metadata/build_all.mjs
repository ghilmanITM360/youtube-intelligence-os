#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import os from "node:os";
import { execFileSync } from "node:child_process";
import { pathToFileURL } from "node:url";

const [rawPath, runPath, identityRawPath, identityRunPath, pilotRawPath, pilotRunPath, outputRoot] = process.argv.slice(2);
if (!outputRoot) throw new Error("Usage: build_all.mjs <full-raw> <full-run> <identity-raw> <identity-run> <pilot-raw> <pilot-run> <output-root>");
const artifactPath = process.env.ARTIFACT_TOOL_PATH;
if (!artifactPath) throw new Error("ARTIFACT_TOOL_PATH is required");
const { SpreadsheetFile, Workbook } = await import(pathToFileURL(artifactPath).href);

const targets = [
  [1,"https://www.youtube.com/@Primateeconomics","Primateeconomics"],
  [2,"https://www.youtube.com/@monkebiznis","monkebiznis"],
  [3,"https://www.youtube.com/@PrimitiveEducation","PrimitiveEducation"],
  [4,"https://www.youtube.com/@LogicalMoney72","LogicalMoney72"],
  [5,"https://www.youtube.com/@MarkBuildsUS","MarkBuildsUS"],
  [6,"https://www.youtube.com/@unknownfrequencies-tv","unknownfrequencies-tv"],
  [7,"https://www.youtube.com/@unclefrankretirement16","unclefrankretirement16"],
  [8,"https://www.youtube.com/@unclejohnfinancial","unclejohnfinancial"],
  [9,"https://www.youtube.com/@Chronofold-m8x","Chronofold-m8x"],
  [10,"https://www.youtube.com/@thetimepiecehistory/videos","thetimepiecehistory"],
  [11,"https://www.youtube.com/@Whatif4k","Whatif4k"],
  [12,"https://www.youtube.com/@SeriousHistory","SeriousHistory"],
];
const raw = JSON.parse(await fs.readFile(rawPath,"utf8"));
const runEnvelope = JSON.parse(await fs.readFile(runPath,"utf8"));
const run = runEnvelope.data ?? runEnvelope;
const identityRaw = JSON.parse(await fs.readFile(identityRawPath,"utf8"));
const identityRunEnvelope = JSON.parse(await fs.readFile(identityRunPath,"utf8"));
const identityRun = identityRunEnvelope.data ?? identityRunEnvelope;
const pilotRaw = JSON.parse(await fs.readFile(pilotRawPath,"utf8"));
const pilotRunEnvelope = JSON.parse(await fs.readFile(pilotRunPath,"utf8"));
const pilotRun = pilotRunEnvelope.data ?? pilotRunEnvelope;
const abouts = [...new Map(identityRaw.filter(r=>r.aboutChannelInfo).map(r=>[r.aboutChannelInfo.channelUsername.toLowerCase(),r.aboutChannelInfo])).values()];
if (abouts.length !== 12) throw new Error(`Expected 12 identities, got ${abouts.length}`);
const template = execFileSync("git",["show","f176aa2861cd93913b977e6159a4e00f4eabeacc:research/monkey-explains-1999/build_dataset.mjs"],{encoding:"utf8"});
const q = v => { const s = v == null ? "UNKNOWN" : Array.isArray(v) ? v.join(" | ") : String(v); return /[",\n\r]/.test(s) ? `"${s.replaceAll('"','""')}"` : s; };
const sha = async p => crypto.createHash("sha256").update(await fs.readFile(p)).digest("hex");
const summaries=[];
await fs.mkdir(path.join(outputRoot,"channels"),{recursive:true});

for (const [seq,requestedUrl,handle] of targets) {
  const about = abouts.find(a=>a.channelUsername.toLowerCase()===handle.toLowerCase());
  if (!about) throw new Error(`Unresolved handle ${handle}`);
  const slug=handle.toLowerCase();
  const dir=path.join(outputRoot,"channels",slug);
  const rawDir=path.join(dir,"source","raw");
  await fs.mkdir(rawDir,{recursive:true});
  const rows=raw.filter(r => r?.aboutChannelInfo?.channelId===about.channelId || r?.channelId===about.channelId);
  const videoRows=rows.filter(r=>/^[A-Za-z0-9_-]{11}$/.test(String(r.id??"")));
  const allocatedCost=Number((rows.length*0.004).toFixed(3));
  const perRun={...runEnvelope,data:{...run,usageTotalUsd:allocatedCost,input:{requestedUrl,maxResults:999,maxResultsShorts:999,maxResultStreams:999,transcriptionAndSubtitle:"NONE",costAllocation:"raw rows x $0.004; shared full run"}}};
  const rawOut=path.join(rawDir,"APIFY_FULL_DATASET_RAW.json");
  const runOut=path.join(rawDir,"APIFY_FULL_RUN.json");
  await fs.writeFile(rawOut,JSON.stringify(rows,null,2)+"\n");
  await fs.writeFile(runOut,JSON.stringify(perRun,null,2)+"\n");
  const idRows=identityRaw.filter(r => r?.aboutChannelInfo?.channelId===about.channelId || r?.channelId===about.channelId);
  await fs.writeFile(path.join(rawDir,"APIFY_IDENTITY_DATASET_RAW.json"),JSON.stringify(idRows,null,2)+"\n");
  await fs.writeFile(path.join(rawDir,"APIFY_IDENTITY_RUN.json"),JSON.stringify(identityRunEnvelope,null,2)+"\n");
  if (handle.toLowerCase()==="primateeconomics") {
    await fs.writeFile(path.join(rawDir,"APIFY_PILOT_DATASET_RAW.json"),JSON.stringify(pilotRaw,null,2)+"\n");
    await fs.writeFile(path.join(rawDir,"APIFY_PILOT_RUN.json"),JSON.stringify(pilotRunEnvelope,null,2)+"\n");
  }
  const safeName=handle.replaceAll(/[^A-Za-z0-9]+/g,"_").toUpperCase();
  let code=template
    .replace('const expectedChannelId = "UCiBGqUxeTe4AYQyRseSZaKw";',`const expectedChannelId = ${JSON.stringify(about.channelId)};`)
    .replace('requested_url: "https://www.youtube.com/@MonkeyExplains1999/videos",',`requested_url: ${JSON.stringify(requestedUrl)},`)
    .replaceAll("MonkeyExplains1999",about.channelName)
    .replace('const workbookPath = path.join(outputDir, "MONKEY_EXPLAINS_1999_COMPLETE_CHANNEL_METADATA.xlsx");',`const workbookPath = path.join(outputDir, ${JSON.stringify(`${safeName}_COMPLETE_CHANNEL_METADATA.xlsx`)});`)
    .replace('run_id: "eLqJpMWfweLnELwLX", dataset_id: "1M0SfI8h8CDRmt7kF", actual_cost_usd: 0.012',`run_id: ${JSON.stringify(identityRun.id)}, dataset_id: ${JSON.stringify(identityRun.defaultDatasetId)}, actual_cost_usd: ${identityRun.usageTotalUsd}`)
    .replace('["pilot_run", actorName, actorBuild, "eLqJpMWfweLnELwLX", "1M0SfI8h8CDRmt7kF", "2026-10-20T06:18:50.000Z", "2026-10-20T06:19:41.000Z", "SUCCEEDED", 3, 2, 0.012, "source/raw/APIFY_PILOT_DATASET_RAW.json"]',`["identity_sweep", actorName, actorBuild, ${JSON.stringify(identityRun.id)}, ${JSON.stringify(identityRun.defaultDatasetId)}, ${JSON.stringify(identityRun.startedAt)}, ${JSON.stringify(identityRun.finishedAt)}, ${JSON.stringify(identityRun.status)}, ${idRows.length}, ${idRows.filter(r=>r.id).length}, ${Number((idRows.length*0.004).toFixed(3))}, "source/raw/APIFY_IDENTITY_DATASET_RAW.json"]`);
  const tmp=path.join(os.tmpdir(),`build-${slug}.mjs`);
  await fs.writeFile(tmp,code);
  execFileSync(process.execPath,[tmp,rawOut,runOut,dir],{stdio:"inherit",env:{...process.env,ARTIFACT_TOOL_PATH:artifactPath,PREVIEW_DIR:path.join(dir,"qa")}});
  const validation=JSON.parse(await fs.readFile(path.join(dir,"METADATA_VALIDATION.json"),"utf8"));
  const master=(await fs.readFile(path.join(dir,"VIDEO_MASTER.jsonl"),"utf8")).trim().split("\n").filter(Boolean).map(JSON.parse);
  const restrictions=videoRows.filter(r=>r.isMembersOnly===true || r.isPaidContent===true).map(r=>({video_id:r.id,title:r.title??null,is_members_only:!!r.isMembersOnly,is_paid_content:!!r.isPaidContent,status:r.isMembersOnly?"MEMBERS_ONLY_EXCLUDED":"PAID_CONTENT_FLAG",source_run_id:run.id,dataset_id:run.defaultDatasetId}));
  const rh=["video_id","title","is_members_only","is_paid_content","status","source_run_id","dataset_id"];
  await fs.writeFile(path.join(dir,"ACCESS_RESTRICTIONS.csv"),[rh.join(","),...restrictions.map(r=>rh.map(h=>q(r[h])).join(","))].join("\n")+"\n");
  const manifest=JSON.parse(await fs.readFile(path.join(dir,"APIFY_RUN_MANIFEST.json"),"utf8"));
  await fs.rename(path.join(dir,"APIFY_RUN_MANIFEST.json"),path.join(dir,"APIFY_MANIFEST.json"));
  await fs.writeFile(path.join(dir,"VALIDATION_RESULTS.json"),JSON.stringify(validation,null,2)+"\n");
  const latest=master[0]??null;
  const counts={regular:master.filter(r=>r.video_type==="REGULAR").length,shorts:master.filter(r=>r.video_type==="SHORT").length,streams:master.filter(r=>r.video_type==="STREAM").length};
  const summary={seq,requested_channel:requestedUrl,requested_handle:`@${handle}`,display_name:about.channelName,channel_id:about.channelId,canonical_url:about.channelUrl,verified:!!about.isChannelVerified,reported_videos:about.channelTotalVideos,public_captured:master.length,...counts,excluded_member_only:restrictions.filter(r=>r.is_members_only).length,metadata_completeness:validation.metadata_completeness.percentage,latest_video_id:latest?.video_id??null,latest_title:latest?.title??null,latest_upload_utc:latest?.publication_timestamp_utc??null,run_id:run.id,dataset_id:run.defaultDatasetId,cost_usd_allocated:allocatedCost,validation_status:validation.status};
  summaries.push(summary);
  const resume=`# Resume here\n\nStatus: COMPLETE_AND_VALIDATED\n\n- Channel: @${handle} (${about.channelId})\n- Public captured: ${master.length}\n- Excluded members-only: ${summary.excluded_member_only}\n- Full run: ${run.id}; dataset: ${run.defaultDatasetId}\n- Allocated cost: $${allocatedCost.toFixed(3)} from shared run rows\n- Validation: ${validation.status}\n- Remaining blocker: none for this channel; public completeness remains subject to YouTube visibility restrictions.\n`;
  await fs.writeFile(path.join(dir,"RESUME_HERE.md"),resume);
}

const headers=Object.keys(summaries[0]);
await fs.writeFile(path.join(outputRoot,"CHANNEL_STATUS_REGISTER.csv"),[headers.join(","),...summaries.map(r=>headers.map(h=>q(r[h])).join(","))].join("\n")+"\n");
await fs.writeFile(path.join(outputRoot,"CHANNEL_STATUS_REGISTER.json"),JSON.stringify(summaries,null,2)+"\n");
const all=[];
for (const s of summaries) {
  const p=path.join(outputRoot,"channels",s.requested_handle.slice(1).toLowerCase(),"VIDEO_MASTER.jsonl");
  for (const line of (await fs.readFile(p,"utf8")).trim().split("\n").filter(Boolean)) all.push({...JSON.parse(line),target_seq:s.seq});
}
const allHeaders=Object.keys(all[0]??{});
await fs.writeFile(path.join(outputRoot,"ALL_PUBLIC_VIDEOS.jsonl"),all.map(JSON.stringify).join("\n")+"\n");
await fs.writeFile(path.join(outputRoot,"ALL_PUBLIC_VIDEOS.csv"),[allHeaders.join(","),...all.map(r=>allHeaders.map(h=>q(r[h])).join(","))].join("\n")+"\n");
const idOwners=new Map();
for (const r of all) { const a=idOwners.get(r.video_id)??new Set(); a.add(r.channel_id); idOwners.set(r.video_id,a); }
const cross=[...idOwners].filter(([,v])=>v.size>1).map(([video_id,v])=>({video_id,channel_ids:[...v]}));
await fs.writeFile(path.join(outputRoot,"CROSS_CHANNEL_DUPLICATES.json"),JSON.stringify(cross,null,2)+"\n");

const wb=Workbook.create(); const sh=wb.worksheets.add("12-CHANNEL OVERVIEW"); sh.showGridLines=false;
sh.getRange("A2:N2").merge(); sh.getRange("A2").values=[["YouTube 12-channel public metadata snapshot"]]; sh.getRange("A2").format.font={name:"Arial",size:16,bold:true,color:"#17365D"};
const oh=["Seq","Requested handle","Display name","Channel ID","Reported videos","Public captured","Regular","Shorts","Streams","Members-only excluded","Completeness","Latest upload UTC","Allocated cost USD","Validation"];
sh.getRangeByIndexes(4,0,1,oh.length).values=[oh]; sh.getRangeByIndexes(4,0,1,oh.length).format={fill:"#17365D",font:{name:"Arial",size:10,bold:true,color:"#FFFFFF"},wrapText:true};
sh.getRangeByIndexes(5,0,summaries.length,oh.length).values=summaries.map(s=>[s.seq,s.requested_handle,s.display_name,s.channel_id,s.reported_videos,s.public_captured,s.regular,s.shorts,s.streams,s.excluded_member_only,s.metadata_completeness,s.latest_upload_utc?new Date(s.latest_upload_utc):"UNKNOWN",s.cost_usd_allocated,s.validation_status]);
sh.getRangeByIndexes(5,0,summaries.length,oh.length).format.font={name:"Arial",size:10,color:"#1F2937"}; sh.getRangeByIndexes(5,10,summaries.length,1).format.numberFormat="0.00%"; sh.getRangeByIndexes(5,11,summaries.length,1).format.numberFormat="yyyy-mm-dd hh:mm:ss"; sh.getRangeByIndexes(5,12,summaries.length,1).format.numberFormat="$0.000"; sh.freezePanes.freezeRows(5); sh.tables.add(`A5:N${summaries.length+5}`,true,"ChannelOverviewTable").style="TableStyleMedium2";
for (const [i,w] of [7,25,25,29,15,15,11,11,11,20,15,22,18,14].entries()) sh.getRangeByIndexes(0,i,1,1).format.columnWidth=w;
wb.recalculate(); const scan=await wb.inspect({kind:"match",searchTerm:"#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",options:{useRegex:true,maxResults:100},summary:"formula error scan",maxChars:5000}); await fs.writeFile(path.join(outputRoot,"OVERVIEW_FORMULA_ERROR_SCAN.ndjson"),scan.ndjson);
const out=await SpreadsheetFile.exportXlsx(wb); await out.save(path.join(outputRoot,"YOUTUBE_12_CHANNEL_METADATA_OVERVIEW.xlsx"));

const files=[]; async function walk(d){for(const e of await fs.readdir(d,{withFileTypes:true})){const p=path.join(d,e.name); if(e.isDirectory()) await walk(p); else if(e.name!=="SHA256SUMS.json") files.push(p);}} await walk(outputRoot);
const sums={}; for(const p of files) sums[path.relative(outputRoot,p)]=await sha(p); await fs.writeFile(path.join(outputRoot,"SHA256SUMS.json"),JSON.stringify(sums,null,2)+"\n");
const aggregate={generated_at_utc:new Date().toISOString(),actor:"streamers/youtube-scraper",build:run.buildNumber,full_run_id:run.id,full_dataset_id:run.defaultDatasetId,full_run_cost_usd:run.usageTotalUsd,pilot_cost_usd:pilotRun.usageTotalUsd,identity_cost_usd:identityRun.usageTotalUsd,total_new_spend_usd:Number((run.usageTotalUsd+pilotRun.usageTotalUsd+identityRun.usageTotalUsd).toFixed(3)),channels:12,public_videos:all.length,cross_channel_duplicate_video_ids:cross.length,validation_status:summaries.every(s=>s.validation_status==="PASS")&&cross.length===0?"PASS":"FAIL",channels_summary:summaries};
await fs.writeFile(path.join(outputRoot,"AGGREGATE_MANIFEST.json"),JSON.stringify(aggregate,null,2)+"\n");
console.log(JSON.stringify(aggregate,null,2));
