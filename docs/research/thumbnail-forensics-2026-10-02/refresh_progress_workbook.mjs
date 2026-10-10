import fs from 'node:fs/promises';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';
const file=process.argv[2], mode=process.argv[3], payload=process.argv[4] || '/tmp/yios-packaging-workbook/payload.json';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
if(mode==='before'){
 const image=await wb.render({sheetName:'00_DASHBOARD',range:'B6:M25',scale:1});
 await fs.writeFile('/tmp/yios-packaging-workbook/before.png',new Uint8Array(await image.arrayBuffer()));
}else{
 const data=JSON.parse(await fs.readFile(payload,'utf8'));
 await fs.mkdir('/tmp/yios-packaging-workbook',{recursive:true});
 const channel=wb.worksheets.getItem('01_CHANNEL_PROGRESS');
 const cids=channel.getRange('B2:B76').values;
 for(const q of data.queue){
  const n=cids.findIndex(row=>row[0]===q.Channel_ID)+2;if(n<2)throw Error('Missing channel '+q.Channel_ID);
  for(const [col,key] of [['L','Existing_Verified_Thumbnail_Audits'],['O','Existing_Package_Audits'],['P','Existing_Package_QA']]){const cell=channel.getRange(`${col}${n}`);if(cell.values[0][0]!==Number(q[key]))cell.values=[[Number(q[key])]];}
  if(q.Channel_Status==='COMPLETE')channel.getRange(`W${n}`).values=[['NONE']];
 }
 const video=wb.worksheets.getItem('02_VIDEO_PROGRESS');
 const ids=video.getRange('D2:D2304').values;
 for(const m of data.master){
  const n=ids.findIndex(row=>row[0]===m.Video_ID)+2;if(n<2)throw Error('Missing video '+m.Video_ID);
  if(m.Thumbnail_Audit_Status.startsWith('AUDITED')){
   {const cell=video.getRange(`K${n}`);if(cell.values[0][0]!=='THUMBNAIL_VERIFIED')cell.values=[['THUMBNAIL_VERIFIED']];}
   {const cell=video.getRange(`R${n}`);if(cell.values[0][0]!==Number(m.Thumbnail_Diagnostic_Score))cell.values=[[Number(m.Thumbnail_Diagnostic_Score)]];}
  }
  if(m.Packaging_Audit_Status.startsWith('AUDITED')){
   {const cell=video.getRange(`N${n}`);if(cell.values[0][0]!=='PACKAGE_AUDITED')cell.values=[['PACKAGE_AUDITED']];}
   {const cell=video.getRange(`S${n}`);if(cell.values[0][0]!==Number(m.EXPERT_PACKAGING_DIAGNOSTIC_SCORE))cell.values=[[Number(m.EXPERT_PACKAGING_DIAGNOSTIC_SCORE)]];}
  }
 }
 wb.recalculate();
 const d=wb.worksheets.getItem('00_DASHBOARD');
 for(const [cell,expected] of [['E11',2303],['H11',518],['B15',518],['E15',121]]){
  if(d.getRange(cell).values[0][0]!==expected)throw Error(cell+' mismatch '+d.getRange(cell).values[0][0]);
 }
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},maxChars:1500});
 console.log(errors.ndjson);
 const image=await wb.render({sheetName:'00_DASHBOARD',range:'B6:M25',scale:1});
 await fs.writeFile('/tmp/yios-packaging-workbook/after.png',new Uint8Array(await image.arrayBuffer()));
 await(await SpreadsheetFile.exportXlsx(wb)).save(file);
 console.log('Workbook reconciled: 2303 / 518 / 518 / 121');
}
