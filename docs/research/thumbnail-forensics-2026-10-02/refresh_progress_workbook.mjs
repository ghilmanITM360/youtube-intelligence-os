import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';
const file=process.argv[2], mode=process.argv[3], payload=process.argv[4] || '/tmp/yios-packaging-workbook/payload.json';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
if(mode==='before'){
 const image=await wb.render({sheetName:'00_DASHBOARD',range:'B6:M25',scale:1});
 await fs.writeFile('/tmp/yios-packaging-workbook/before.png',new Uint8Array(await image.arrayBuffer()));
}else{
 const data=JSON.parse(await fs.readFile(payload,'utf8'));
 await fs.mkdir('/tmp/yios-packaging-workbook',{recursive:true});
 const baseline='/tmp/yios-packaging-workbook/native-baseline.xlsx';
 await fs.copyFile(file,baseline);
 const channel=wb.worksheets.getItem('01_CHANNEL_PROGRESS');
 const cids=channel.getRange(`B2:B${data.queue.length+1}`).values;
 for(const q of data.queue){
  const n=cids.findIndex(row=>row[0]===q.Channel_ID)+2;if(n<2)throw Error('Missing channel '+q.Channel_ID);
  for(const [col,key] of [['J','Existing_Title_Audits'],['L','Existing_Verified_Thumbnail_Audits'],['O','Existing_Package_Audits'],['P','Existing_Package_QA']]){const cell=channel.getRange(`${col}${n}`);if(cell.values[0][0]!==Number(q[key]))cell.values=[[Number(q[key])]];}
  if(channel.getRange(`V${n}`).values[0][0]!==q.Channel_Status)channel.getRange(`V${n}`).values=[[q.Channel_Status]];
  if(q.Channel_Status==='COMPLETE')channel.getRange(`W${n}`).values=[['NONE']];
 }
 const video=wb.worksheets.getItem('02_VIDEO_PROGRESS');
 const ids=video.getRange(`D2:D${data.master.length+1}`).values;
 const qa=new Set(data.qa_ids);
 for(const m of data.master){
  const n=ids.findIndex(row=>row[0]===m.Video_ID)+2;if(n<2)throw Error('Missing video '+m.Video_ID);
  const set=(col,value)=>{const cell=video.getRange(`${col}${n}`);if(cell.values[0][0]!==value)cell.values=[[value]];};
  set('H',m.Title_Status);
  if(qa.has(m.Video_ID)&&!['PASS','PASS_WITH_CORRECTIONS'].includes(video.getRange(`O${n}`).values[0][0]))set('O','PASS');
  if(m.Current_Status==='COMPLETE')set('V','COMPLETE');
  if(m.Thumbnail_Audit_Status.startsWith('AUDITED')){
   {const cell=video.getRange(`K${n}`);if(cell.values[0][0]!=='THUMBNAIL_VERIFIED')cell.values=[['THUMBNAIL_VERIFIED']];}
   {const cell=video.getRange(`R${n}`);if(cell.values[0][0]!==Number(m.Thumbnail_Diagnostic_Score))cell.values=[[Number(m.Thumbnail_Diagnostic_Score)]];}
  }
  if(m.Packaging_Audit_Status.startsWith('AUDITED')){
   {const cell=video.getRange(`N${n}`);if(cell.values[0][0]!=='PACKAGE_AUDITED')cell.values=[['PACKAGE_AUDITED']];}
   {const cell=video.getRange(`S${n}`);if(cell.values[0][0]!==Number(m.EXPERT_PACKAGING_DIAGNOSTIC_SCORE))cell.values=[[Number(m.EXPERT_PACKAGING_DIAGNOSTIC_SCORE)]];}
  }
 }
 const current=wb.worksheets.getItem('03_CURRENT_CHANNEL');
 current.getRange('B13').values=[[data.current_channel.remaining_videos]];
 current.getRange('B19').formulas=[[data.current_channel.next_Video_ID?`=MATCH("${data.current_channel.next_Video_ID}",'02_VIDEO_PROGRESS'!D1:D${data.master.length+1},0)`:'=0']];
 wb.recalculate();
 const d=wb.worksheets.getItem('00_DASHBOARD');
 for(const [cell,expected] of [['E11',data.totals.titles],['H11',data.totals.thumbnails],['B15',data.totals.packages],['E15',data.totals.qa],['E7',data.totals.channels_complete]]){
  if(d.getRange(cell).values[0][0]!==expected)throw Error(cell+' mismatch '+d.getRange(cell).values[0][0]);
 }
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},maxChars:1500});
 console.log(errors.ndjson);
 const image=await wb.render({sheetName:'00_DASHBOARD',range:'B6:M25',scale:1});
 await fs.writeFile('/tmp/yios-packaging-workbook/after.png',new Uint8Array(await image.arrayBuffer()));
 await(await SpreadsheetFile.exportXlsx(wb)).save(file);
 execFileSync(process.env.YIOS_PYTHON||'python3',[data.research_root+'/preserve_workbook_features.py',file,baseline]);
 console.log(JSON.stringify({reconciled:data.totals,current_channel:data.current_channel}));
}
