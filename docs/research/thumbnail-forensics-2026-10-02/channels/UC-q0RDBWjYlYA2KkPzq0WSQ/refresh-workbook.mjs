import fs from 'node:fs/promises';
import pathModule from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,SpreadsheetFile,Workbook} from '@oai/artifact-tool';
const here=process.env.YIOS_CHANNEL_DIR||pathModule.dirname(fileURLToPath(import.meta.url));
const root=pathModule.resolve(here,'../..');
const path=root+'/PACKAGING-PROGRESS.xlsx';
const csvWb=await Workbook.fromCSV(await fs.readFile(here+'/packaging-progress.csv','utf8'),{sheetName:'Manifest'});
const matrix=csvWb.worksheets.getItem('Manifest').getUsedRange().values;
const rows=matrix.slice(1).map(row=>Object.fromEntries(matrix[0].map((key,i)=>[key,row[i]??''])));
const summary=JSON.parse(await fs.readFile(root+'/packaging-progress-summary.json','utf8'));
const latest=process.argv[2];if(!latest)throw Error('Supply latest completed Video_ID');
const latestRow=rows.find(r=>r.Video_ID===latest);if(!latestRow)throw Error('Missing latest video');
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(path));
const now=new Date();
const video=wb.worksheets.getItem('02_VIDEO_PROGRESS');
for(const r of rows){
 const index=1+Number(r.Video_Order);
 if(video.getRange(`D${index}`).values[0][0]!==r.Video_ID) throw Error('Video row mapping mismatch');
 const set=(col,value)=>video.getRange(`${col}${index}`).values=[[value]];
 set('K',r.Thumbnail_Status); set('N',r.Package_Status);set('O',r.QA_Status);
 set('R',r.Thumbnail_Score===''?null:Number(r.Thumbnail_Score));set('S',r.Package_Score===''?null:Number(r.Package_Score));
 set('T',r.Medical_Packaging_Status);set('V',r.Current_Status);
 if(r.Video_ID===latest) set('Y',now);
}
const counts={verified:rows.filter(r=>r.Thumbnail_Status==='THUMBNAIL_VERIFIED').length,drafts:rows.filter(r=>r.Thumbnail_Status==='THUMBNAIL_DRAFT').length,
 packages:rows.filter(r=>r.Package_Status==='PACKAGE_AUDITED').length,qa:rows.filter(r=>['PASS','HISTORICAL_SAMPLE'].includes(r.QA_Status)).length,complete:rows.filter(r=>r.Current_Status==='COMPLETE').length};
const ch=wb.worksheets.getItem('01_CHANNEL_PROGRESS');
for(const [col,val] of Object.entries({L:counts.verified,M:counts.drafts,O:counts.packages,P:counts.qa,X:latest,Y:latestRow.Thumbnail_ID,AA:now}))ch.getRange(`${col}2`).values=[[val]];
const dash=wb.worksheets.getItem('00_DASHBOARD');dash.getRange('B4').values=[['Channel-by-channel research • primary sequential QA • public performance is observational']];
dash.getRange('B27').values=[['CURRENT CHANNEL • SEQUENTIAL VIDEO ANALYSIS']];dash.getRange('F33').values=[[now]];
dash.getRange('F35').values=[['Short-window '+summary.resource.latest_short_window_used_percent+'% / weekly '+summary.resource.weekly_used_percent+'% at latest check']];
const current=wb.worksheets.getItem('03_CURRENT_CHANNEL');current.getRange('A1').values=[['CURRENT CHANNEL / ACTIVE WORKLIST']];
current.getRange('B13').values=[[10-counts.complete]];
// Existing formulas own the dynamic channel/video list; preserve their references.
const qa=wb.worksheets.getItem('08_QA_PROGRESS');
const audit=JSON.parse(await fs.readFile(here+'/package-audits.json','utf8')).find(r=>r.Video_ID===latest);
const reviews=JSON.parse(await fs.readFile(here+'/qa.json','utf8')).reviews.filter(r=>r.microbatch===audit.batch_id||(!r.microbatch&&audit.batch_id==='CHANNEL-001-M01'));
const sum=field=>reviews.reduce((total,r)=>total+(r[field]||0),0);
const qaRow=['Genius History',latestRow.Legacy_B002_Batch+' provenance',audit.batch_id,1,reviews.length,sum('material'),sum('minor_factual'),sum('classification'),sum('subjective'),sum('style_only'),0,reviews.filter(r=>r.corrections.some(c=>['word_count','text','typography'].includes(c.field))).length,0,reviews.some(r=>r.corrections.length)?'PASS_WITH_CORRECTIONS':'PASS',null,'channels/'+pathModule.basename(here)+'/qa.json; primary sequential, not independent reviewer'];
const existing=qa.getUsedRange().values.findIndex(row=>row[2]===audit.batch_id);
if(existing<0)qa.tables.items[0].rows.add(null,[qaRow]);
else {
 const oldSha=qa.getRange(`O${existing+1}`).values[0][0];qaRow[14]=oldSha;
 qa.getRange(`A${existing+1}:P${existing+1}`).values=[qaRow];
}
wb.recalculate();
const found=(await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},maxChars:1200})).ndjson;
console.log(found);
console.log((await wb.inspect({kind:'table',range:'03_CURRENT_CHANNEL!A7:B19',tableMaxRows:13,tableMaxCols:2,maxChars:2200})).ndjson);
await fs.mkdir('/tmp/yios-channel-resume',{recursive:true});
for(const [name,range,file] of [['00_DASHBOARD','B6:M25','dashboard'],['03_CURRENT_CHANNEL','A3:B19','current']]){
 const img=await wb.render({sheetName:name,range,scale:1});await fs.writeFile(`/tmp/yios-channel-resume/${file}.png`,new Uint8Array(await img.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(wb)).save(path);
console.log(JSON.stringify(counts));
