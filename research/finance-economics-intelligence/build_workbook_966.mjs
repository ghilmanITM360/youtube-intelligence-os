// Run a copy beside a symlink to the bundled node_modules; pass research directory.
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const base = path.resolve(process.argv[2]);
const rows = (await fs.readFile(path.join(base, 'VIDEO_AUDIT_966.jsonl'), 'utf8')).trim().split('\n').map(JSON.parse);
const wb = Workbook.create();
const cover = wb.worksheets.add('Coverage');
const videos = wb.worksheets.add('Videos');
const readings = wb.worksheets.add('Readings');
const dims = ['TITLE','THUMBNAIL','SCRIPT','TOPIC','PERFORMANCE','VIRALITY'];
function table(sheet, headers, data, name) {
  sheet.showGridLines = false;
  sheet.getRangeByIndexes(3, 0, 1, headers.length).values = [headers];
  sheet.getRangeByIndexes(4, 0, data.length, headers.length).values = data;
  const area = sheet.getRangeByIndexes(3, 0, data.length + 1, headers.length);
  area.format.font = {name: 'Arial', size: 10};
  area.format.verticalAlignment = 'center';
  area.format.columnWidth = 25;
  area.format.rowHeight = 25;
  sheet.getRangeByIndexes(3, 0, 1, headers.length).format = {fill:'#20324A',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:32};
  const t = sheet.tables.add(area.address, true, name);
  t.showFilterButton = true;
  sheet.freezePanes.freezeRows(4);
  return area;
}
cover.showGridLines = false;
cover.getRange('A2').values = [['Finance and Economics: 966-video audit']];
cover.getRange('A2').format.font = {name:'Arial',size:14,bold:true};
cover.getRange('A4').values = [['FULL_POPULATION_RESEARCH_IN_PROGRESS']];
cover.getRange('A6:C6').values = [['Dimension','Expanded review complete','Registered']];
cover.getRange('A7:A12').values = dims.map(d=>[d]);
cover.getRange('C7:C12').values = [[966]];
cover.getRange('A6:C12').format.columnWidth = 29;
cover.getRange('A6:C12').format.font = {name:'Arial',size:10};
cover.getRange('A6:C6').format = {fill:'#20324A',font:{color:'#FFFFFF',bold:true}};
cover.getRange('A6:C12').format.rowHeight = 28;
cover.getRange('A15').values = [['Performance completion is automated revalidation.']];
cover.getRange('A16').values = [['Other completions require individual semantic readings.']];
cover.getRange('A18').values = [['Historical snapshots. Private analytics unavailable.']];
cover.getRange('A19').values = [['Full stored text does not certify complete audio.']];
cover.getRange('A20').values = [['See Readings for individual findings and provenance.']];
cover.getRange('A15:C20').format.font = {name:'Arial',size:10};
videos.getRange('A2').values = [['Canonical population and independent completion indicators']];
const numeric = x => x === '' || x === null ? null : Number(x);
const dated = x => x && !Number.isNaN(Date.parse(x)) ? new Date(x) : x;
const headers = ['Video ID','Channel','Title','Published UTC','Historical views','Snapshot','Format','Duration seconds','Tier','Age-peer ratio',...dims.map(d=>d+' review'),'Batch','Transcript status','Source locator'];
table(videos,headers,rows.map(r=>[r.Video_ID,r.identity.Channel,r.identity.Title,dated(r.identity.Published_at_raw),numeric(r.identity.Views),dated(r.identity.Metric_snapshot_date),r.identity.Format,numeric(r.identity.Duration_seconds),r.performance.Performance_tier,numeric(r.performance.Lifetime_rate_ratio),...dims.map(d=>r.statuses[d+'_REVIEW']),r.batch_id,r.script.source.Status,r.identity.Evidence_locator]),'Population');
videos.getRange('C4:C970').format.columnWidth=66;
videos.getRange('D4:D970').format.columnWidth=29;
videos.getRange('D5:D970').setNumberFormat('yyyy-mm-dd hh:mm');
videos.getRange('F5:F970').setNumberFormat('yyyy-mm-dd');
videos.getRange('E5:E970').setNumberFormat('#,##0');
videos.getRange('H5:H970').setNumberFormat('0');
videos.getRange('J5:J970').setNumberFormat('0.00"x"');
videos.getRange('K4:P970').format.columnWidth=39;
videos.getRange('S4:S970').format.columnWidth=90;
videos.freezePanes.freezeColumns(2);
videos.getRange('K5:P970').conditionalFormats.add('containsText',{text:'NOT_STARTED',format:{fill:'#F6E7C8'}});
videos.getRange('K5:P970').conditionalFormats.add('containsText',{text:'BLOCKED_MISSING_SOURCE',format:{fill:'#F6DCDC',font:{color:'#8A2020'}}});
videos.getRange('K5:P970').conditionalFormats.add('containsText',{text:'IN_PROGRESS',format:{fill:'#F4EDDA'}});
for(let i=0;i<dims.length;i++) {
  const col=String.fromCharCode(75+i);
  cover.getRange(`B${7+i}`).formulas=[[`=COUNTIFS('Videos'!${col}5:${col}970,"COMPLETE_LIMITED_EVIDENCE")+COUNTIFS('Videos'!${col}5:${col}970,"COMPLETE_EVIDENCE_BACKED")`]];
}
const done = rows.filter(r=>r.virality.analysis);
readings.getRange('A2').values=[['Individual readings. Limited evidence.']];
table(readings,['Video ID','Title','Topic','Title reading','Script beats','Script decisions','Claims to verify','Thumbnail reading','Virality assessment','Original test','Source references'],done.map(r=>[r.Video_ID,r.identity.Title,r.topic.analysis,r.title.analysis,r.script.beat_map.join(' → '),r.script.analysis,r.script.claim_audit,r.thumbnail.analysis,r.virality.analysis,r.virality.original_content_lesson.test,r.virality.source_refs.join('\n')]),'IndividualReadings');
readings.getRangeByIndexes(4,0,done.length,11).format.wrapText=true;
readings.getRangeByIndexes(4,0,done.length,11).format.verticalAlignment='top';
readings.getRangeByIndexes(3,1,done.length+1,10).format.columnWidth=74;
readings.getRangeByIndexes(4,0,done.length,11).format.autofitRows();
readings.freezePanes.freezeColumns(1);
wb.recalculate();
const expected = dims.map(d=>rows.filter(r=>r.statuses[d+'_REVIEW'].startsWith('COMPLETE_')).length);
const actual = cover.getRange('B7:B12').values.map(r=>r[0]);
if(JSON.stringify(expected)!==JSON.stringify(actual)) throw new Error('Coverage formula mismatch '+JSON.stringify(actual));
// Mutation test proves the counts read the status cells; restore before export.
const old=videos.getRange('K5').values;
videos.getRange('K5').values=[['COMPLETE_LIMITED_EVIDENCE']];
wb.recalculate();
if(cover.getRange('B7').values[0][0]!==expected[0]+1) throw new Error('Coverage did not recalculate');
videos.getRange('K5').values=old;
wb.recalculate();
console.log((await wb.inspect({kind:'region',sheetId:'Coverage',range:'A6:C12',maxChars:1400,tableMaxRows:8,tableMaxCols:3})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20},maxChars:1000})).ndjson);
for(const [sheetName,range] of [['Coverage','A1:D21'],['Videos','A1:F8'],['Readings','A1:C6']]) {
  const image=await wb.render({sheetName,range,scale:1.4,format:'png'});
  await fs.writeFile(path.join(base,`audit-batches/workbook-${sheetName}.png`),new Uint8Array(await image.arrayBuffer()));
}
const out=await SpreadsheetFile.exportXlsx(wb);
await out.save(path.join(base,'FINANCE_966_VIDEO_INTELLIGENCE.xlsx'));
console.log('Exported 966 population rows and '+done.length+' individual readings.');
