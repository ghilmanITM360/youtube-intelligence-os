// Run a copy beside a node_modules symlink to bundled dependencies; pass research directory.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
import { beatMapForDisplay, structuredValueForDisplay } from './workbook_formatting.mjs';

const base = path.resolve(process.argv[2]);
const payload = JSON.parse(execFileSync('python3',[path.join(base,'build_combined_workbook_data.py')],{cwd:base,encoding:'utf8',maxBuffer:80*1024*1024}));
const rows = payload.all_videos, channels = payload.channels, details = payload.details, summary = payload.summary;
const wb = Workbook.create();
const dashboard = wb.worksheets.add('Combined Dashboard');
const videos = wb.worksheets.add('All Finance Videos');
const directory = wb.worksheets.add('Channel Directory');
const research = wb.worksheets.add('Detailed Research');
const navy='#20324A', blue='#DCE6F1', amber='#F6E7C8', red='#F6DCDC', green='#E2F0D9', font='Arial';
function writeTable(sheet, headers, data, name) {
  sheet.showGridLines=false;
  sheet.getRangeByIndexes(3,0,1,headers.length).values=[headers];
  sheet.getRangeByIndexes(4,0,data.length,headers.length).values=data;
  const area=sheet.getRangeByIndexes(3,0,data.length+1,headers.length);
  area.format.font={name:font,size:10}; area.format.verticalAlignment='center'; area.format.rowHeight=24;
  sheet.getRangeByIndexes(3,0,1,headers.length).format={fill:navy,font:{name:font,size:10,bold:true,color:'#FFFFFF'},rowHeight:34,wrapText:true,horizontalAlignment:'center'};
  const t=sheet.tables.add(area.address,true,name); t.showFilterButton=true; t.style='TableStyleMedium2';
  sheet.freezePanes.freezeRows(4); return area;
}
function jsonCell(v){return JSON.stringify(v ?? {},null,0)}
function setWidths(sheet, widths, lastRow) {
  widths.forEach((width,i)=>sheet.getRangeByIndexes(3,i,lastRow-3,1).format.columnWidth=width);
}

dashboard.showGridLines=false;
dashboard.getRange('A2').values=[['Finance and Economics combined research universe']];
dashboard.getRange('A2').format.font={name:font,size:14,bold:true};
dashboard.getRange('A4:B9').values=[
  ['Metric','Count'],['Unique Finance videos',summary.total],['Deep-audited',summary.deep_audited],['Pending deep audit',summary.pending],
  ['Included data-ready channels',summary.channel_status.VIDEO_DATASET_INCLUDED],['Registered channels',channels.length]
];
dashboard.getRange('A12:D17').values=[
  ['Research layer','Videos','Deep-audited','Pending'],
  ['Frozen original 966',966,summary.deep_audited,966-summary.deep_audited],
  ['First expansion',197,0,197],['MonkeyExplains1999',63,0,63],['Landscape + Casually Finance',386,0,386],['Combined',summary.total,summary.deep_audited,summary.pending]
];
const dims=['Title','Thumbnail','Script','Topic','Performance','Virality'];
const coverage=dims.map(d=>rows.filter(r=>String(r[`${d.toLowerCase()}_review_status`]).startsWith('COMPLETE_')).length);
dashboard.getRange('F4:H10').values=[['Research dimension','Complete','Pending'],...dims.map((d,i)=>[d,coverage[i],summary.total-coverage[i]])];
dashboard.getRange('B5').formulas=[[`=COUNTA('All Finance Videos'!A5:A1616)`]];
dashboard.getRange('B6').formulas=[[`=COUNTIF('All Finance Videos'!AA5:AA1616,"DEEP_AUDIT_COMPLETE")`]];
dashboard.getRange('B7').formulas=[['=B5-B6']];
dashboard.getRange('B8').formulas=[[`=COUNTIF('Channel Directory'!D5:D46,"VIDEO_DATASET_INCLUDED")`]];
dashboard.getRange('B9').formulas=[[`=COUNTA('Channel Directory'!A5:A46)`]];
for(let i=0;i<dims.length;i++) {
  const sourceCol=String.fromCharCode('U'.charCodeAt(0)+i);
  dashboard.getRange(`G${5+i}`).formulas=[[`=COUNTIFS('All Finance Videos'!${sourceCol}5:${sourceCol}1616,"COMPLETE_LIMITED_EVIDENCE")+COUNTIFS('All Finance Videos'!${sourceCol}5:${sourceCol}1616,"COMPLETE_EVIDENCE_BACKED")`]];
  dashboard.getRange(`H${5+i}`).formulas=[[`=$B$5-G${5+i}`]];
}
dashboard.getRange('F13:G18').values=[['Evidence/blocker','Records'],['Transcript unavailable or unregistered',rows.filter(r=>!['TEXT_AVAILABLE','PARTIAL_SELECTED_FORENSICS'].includes(r.transcript_status)).length],['Thumbnail unavailable or remote-only',rows.filter(r=>!['AVAILABLE','REFERENCE_AVAILABLE'].includes(r.thumbnail_status)).length],['Local media not registered',rows.filter(r=>r.local_media_status==='NOT_REGISTERED').length],['Identity-only channels',summary.channel_status.IDENTITY_ONLY_NEEDS_DATA],['Excluded channels',summary.channel_status.VIDEO_DATASET_EXCLUDED_AFTER_INDIVIDUAL_CLASSIFICATION]];
for(const range of ['A4:B9','A12:D17','F4:H10','F13:G18']){dashboard.getRange(range).format.font={name:font,size:10}; dashboard.getRange(range).format.rowHeight=26; dashboard.getRange(range).format.borders={preset:'outside',style:'thin',color:'#B7C3D0'};}
for(const range of ['A4:B4','A12:D12','F4:H4','F13:G13']) dashboard.getRange(range).format={fill:navy,font:{name:font,size:10,bold:true,color:'#FFFFFF'},horizontalAlignment:'center'};
dashboard.getRange('A20').values=[['Expansion rows are metadata-only until individual evidence-based audits are completed. This is the sole current Excel research deliverable.']];
dashboard.getRange('A20:H20').merge(); dashboard.getRange('A20').format={font:{name:font,size:10,italic:true,color:'#555555'},wrapText:true};
dashboard.getRange('A1:H22').format.columnWidth=24;

const vHeaders=['Video ID','Channel','Channel ID','Channel URL','Title','Watch URL','Research layer','Source dataset','Source commit','Source row','Niche','Sub-niche','Decision confidence','Published','Duration seconds/display','Format','Views/display','Likes','Comments','Metric snapshot','Title status','Thumbnail status','Script status','Topic status','Performance status','Virality status','Deep-audit status','Transcript evidence','Thumbnail evidence','Local media evidence','Metadata status','Blocker','Description'];
writeTable(videos,vHeaders,rows.map(r=>[r.video_id,r.channel_name,r.channel_id,r.channel_url,r.title,r.video_url,r.population_layer,r.source_dataset,r.source_commit,r.source_row,r.niche,r.sub_niche,r.decision_confidence,r.publication_date,r.duration,r.format,r.views,r.likes,r.comments,r.metric_snapshot,r.title_review_status,r.thumbnail_review_status,r.script_review_status,r.topic_review_status,r.performance_review_status,r.virality_review_status,r.audit_status,r.transcript_status,r.thumbnail_status,r.local_media_status,r.metadata_status,r.blocker,r.description]),'AllFinanceVideos');
videos.getRange('A2').values=[['All eligible Finance videos. One row per approved Video ID.']]; videos.getRange('A2').format.font={name:font,size:14,bold:true};
videos.freezePanes.freezeColumns(2); setWidths(videos,[18,25,28,48,58,48,42,42,42,48,24,36,22,25,22,18,18,14,14,25,32,32,32,32,32,32,34,34,40,28,24,50,72],1616); videos.getRange('A4:AG1616').format.wrapText=false;
videos.getRange('E5:E1616').format.wrapText=true; videos.getRange('AG5:AG1616').format.wrapText=true; videos.getRange('N5:N1616').setNumberFormat('yyyy-mm-dd hh:mm'); videos.getRange('Q5:S1616').setNumberFormat('#,##0');
videos.getRange('U5:AA1616').conditionalFormats.add('containsText',{text:'NOT_STARTED',format:{fill:amber}}); videos.getRange('AA5:AA1616').conditionalFormats.add('containsText',{text:'DEEP_AUDIT_COMPLETE',format:{fill:green}}); videos.getRange('AF5:AF1616').conditionalFormats.add('notContainsBlanks',{format:{fill:red,font:{color:'#8A2020'}}});

writeTable(directory,['Channel ID','Channel','Channel URL','Classification','Eligible videos','Dataset/source','Notes'],channels.map(r=>[r.channel_id,r.channel_name,r.channel_url,r.status,Number(r.eligible_video_count),r.source,r.notes]),'FinanceChannels');
directory.getRange('A2').values=[['Registered Finance and Economics channel directory']]; directory.getRange('A2').format.font={name:font,size:14,bold:true}; setWidths(directory,[30,32,58,48,18,58,58],46); directory.getRange('A5:G46').format.wrapText=true; directory.freezePanes.freezeColumns(2);

const dHeaders=['Video ID','Channel','Title','Batch','Deep-audit status','Script scope','Topic reading','Title reading','Script beats','Script analysis','Claims to verify','Thumbnail reading','Virality assessment','Original test','Source references','Dimension statuses JSON','Title research JSON','Thumbnail research JSON','Script research JSON','Topic research JSON','Performance research JSON','Virality research JSON','Event research JSON','Private metrics JSON'];
writeTable(research,dHeaders,details.map(r=>[
  r.video_id,r.channel,r.title,r.batch_id,r.deep_audit_status,r.script_research.review_scope,
  r.topic_research.analysis || r.topic_research.legacy_review?.Audience_problem || 'PENDING',
  r.title_research.analysis || jsonCell(r.title_research.legacy_review || {}),
  beatMapForDisplay(r.script_research.beat_map,r.script_research.legacy_beat_map?.Narrative_chain),
  r.script_research.analysis || (r.script_research.legacy_review ? `LEGACY ${r.script_research.review_scope}: ${r.script_research.legacy_review.Narrative_angle}` : 'PENDING'),
  structuredValueForDisplay(r.script_research.claim_audit),
  r.thumbnail_research.analysis || (r.thumbnail_research.legacy_review ? jsonCell(r.thumbnail_research.legacy_review) : 'PENDING'),
  r.virality_research.analysis || 'PENDING',r.virality_research.original_content_lesson?.test || 'PENDING',
  (r.virality_research.source_refs || r.title_research.source_refs || [r.title_research.legacy_review?.Source].filter(Boolean)).join('\n'),
  jsonCell(r.statuses),jsonCell(r.title_research),jsonCell(r.thumbnail_research),jsonCell(r.script_research),jsonCell(r.topic_research),jsonCell(r.performance_research),jsonCell(r.virality_research),jsonCell(r.event_research),jsonCell(r.private_metrics)
]),'OriginalDetailedResearch');
research.getRange('A2').values=[['Original 966-video audit detail. Expansion records remain metadata-only until audited.']]; research.getRange('A2').format.font={name:font,size:14,bold:true}; research.freezePanes.freezeColumns(2); setWidths(research,[18,25,55,18,28,72,72,72,72,72,72,72,72,48],970); research.getRange('A5:N970').format.wrapText=true; research.getRange('A5:N970').format.verticalAlignment='top';
research.getRange('F4:X970').format.columnWidth=72; research.getRange('A5:X970').format.wrapText=true; research.getRange('A5:X970').format.verticalAlignment='top';

const sourceHash=createHash('sha256').update(await fs.readFile(path.join(base,'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv'))).digest('hex');
dashboard.getRange('A23:B27').values=[['Checkpoint','2026-10-22'],['Universe SHA-256',sourceHash],['Generated UTC',new Date()],['Base Git HEAD',execFileSync('git',['rev-parse','HEAD'],{cwd:base,encoding:'utf8'}).trim()],['Source of truth','FINANCE_UNIVERSE.csv + original audit JSONL + approved expansion ledgers']];
dashboard.getRange('B25').setNumberFormat('yyyy-mm-dd hh:mm:ss'); dashboard.getRange('A23:B27').format.font={name:font,size:10}; dashboard.getRange('B24:B27').format.columnWidth=88;
wb.recalculate();
if(summary.total!==1612 || new Set(rows.map(r=>r.video_id)).size!==1612) throw new Error('Combined population contract failed');
if(details.length!==966 || details.filter(r=>r.deep_audit_status==='DEEP_AUDIT_COMPLETE').length!==summary.deep_audited) throw new Error('Original detail preservation failed');
if(rows.filter(r=>r.population_layer!=='FROZEN_ORIGINAL_966'&&r.audit_status==='DEEP_AUDIT_COMPLETE').length) throw new Error('Metadata-only row marked complete');
if(dashboard.getRange('B5:B9').values.flat().join('|')!==[summary.total,summary.deep_audited,summary.pending,summary.channel_status.VIDEO_DATASET_INCLUDED,channels.length].join('|')) throw new Error('Dashboard formula reconciliation failed');
if(JSON.stringify(dashboard.getRange('G5:G10').values.flat())!==JSON.stringify(coverage)) throw new Error('Coverage formula reconciliation failed');
console.log((await wb.inspect({kind:'region',sheetId:'Combined Dashboard',range:'A4:H18',maxChars:5000,tableMaxRows:20,tableMaxCols:8})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},maxChars:2000})).ndjson);
for(const [sheetName,range] of [['Combined Dashboard','A1:H27'],['All Finance Videos','A1:H10'],['Channel Directory','A1:G12'],['Detailed Research','A1:F8']]){
  const image=await wb.render({sheetName,range,scale:1.2,format:'png'}); await fs.writeFile(path.join('/tmp',`finance-1612-${sheetName.replaceAll(' ','-')}.png`),new Uint8Array(await image.arrayBuffer()));
}
const out=await SpreadsheetFile.exportXlsx(wb); await out.save(path.join(base,'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'));
console.log(`Exported ${rows.length} videos, ${channels.length} channels and ${details.length} original detail rows.`);
