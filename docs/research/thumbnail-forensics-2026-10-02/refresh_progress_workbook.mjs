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
  for(const [col,key] of [['J','Existing_Title_Audits'],['L','Existing_Verified_Thumbnail_Audits'],['M','Existing_Thumbnail_Drafts'],['O','Existing_Package_Audits'],['P','Existing_Package_QA']]){const cell=channel.getRange(`${col}${n}`);if(cell.values[0][0]!==Number(q[key]))cell.values=[[Number(q[key])]];}
  if(channel.getRange(`V${n}`).values[0][0]!==q.Channel_Status)channel.getRange(`V${n}`).values=[[q.Channel_Status]];
  if(q.Channel_Status==='COMPLETE')channel.getRange(`W${n}`).values=[['NONE']];
 }
 const video=wb.worksheets.getItem('02_VIDEO_PROGRESS');
 const ids=video.getRange(`D2:D${data.master.length+1}`).values;
 const qa=new Set(data.qa_ids);
 const channelReviews=JSON.parse(await fs.readFile(data.research_root+'/channels/'+data.current_channel.Channel_ID+'/qa.json','utf8')).reviews;
 const qaSheet=wb.worksheets.getItem('08_QA_PROGRESS');
 const checkpoints=wb.worksheets.getItem('09_GIT_CHECKPOINTS');
 for(const review of channelReviews){
  const micro=qaSheet.getRange('C2:C80').values;
  if(!micro.some(row=>row[0]===review.microbatch)){
   const index=qaSheet.getRange('A2:A80').values.findIndex(row=>!row[0])+2;
   if(index<2)throw Error('QA sheet capacity exhausted');
   qaSheet.getRange(`A${index}:P${index}`).values=[[data.current_channel.name,review.legacy_package_source,review.microbatch,1,1,review.material,review.minor_factual,review.classification,review.subjective,review.style_only,0,0,0,review.result,'COMMIT_CONTAINING_THIS_RECORD','channels/'+data.current_channel.Channel_ID+'/qa.json']];
  }
  const work='QA '+review.Video_ID;
  if(!checkpoints.getRange('C2:C80').values.some(row=>row[0]===work)){
   const index=checkpoints.getRange('A2:A80').values.findIndex(row=>!row[0])+2;
   if(index<2)throw Error('Checkpoint sheet capacity exhausted');
   checkpoints.getRange(`A${index}:I${index}`).values=[[review.review_timestamp,data.current_channel.name,work,1,'COMMIT_CONTAINING_THIS_RECORD','PUSH_VERIFIED_EXTERNALLY','SEE_GIT_REMOTE','Exact source hash, visual QA, dynamic workbook validation','Containing commit and remote sync recorded by Git; no self-referential commit SHA.']];
  }
 }
 for(const m of data.master){
  const n=ids.findIndex(row=>row[0]===m.Video_ID)+2;if(n<2)throw Error('Missing video '+m.Video_ID);
  const set=(col,value)=>{const cell=video.getRange(`${col}${n}`);if(cell.values[0][0]!==value)cell.values=[[value]];};
  set('H',m.Title_Status);
  if(qa.has(m.Video_ID))set('O',channelReviews.find(row=>row.Video_ID===m.Video_ID)?.result || (['PASS','PASS_WITH_CORRECTIONS'].includes(video.getRange(`O${n}`).values[0][0])?video.getRange(`O${n}`).values[0][0]:'PASS'));
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
