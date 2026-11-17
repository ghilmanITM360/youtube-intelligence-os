
const q=s=>"'"+s.replaceAll("'","'\\''")+"'";
async function helper(cmd,arg){
 let e=await tools.exec_command({cmd:"python3 "+q(load("bulkRoot")+"/continue_backup.py")+" "+q(cmd)+" "+q(JSON.stringify(arg)),max_output_tokens:7000,yield_time_ms:1000});
 while(e.session_id)e=await tools.write_stdin({session_id:e.session_id,chars:"",yield_time_ms:1000,max_output_tokens:7000});
 if(e.exit_code!==0)throw Error(e.output);return e.output.trim();
}


async function transferBatch(){
 const b=load("activeBatch");
 for(const x of b.files){
  if(x.duplicate_of_verified||x.duplicate_of_sequence)continue;
  if(x.bytes>104857600){store("browserUploadRequired",x);throw Error("QUALIFIED_BROWSER_UPLOAD_REQUIRED_"+x.sequence);}
  await helper("check",{batch_dir:b.batch_dir,sequence:x.sequence});
  const result=await tools.mcp__codex_apps__google_drive_upload_file({file_uri:x.source_absolute,file_name:x.proposed_destination_name,mime_type:null,parent_folder_id:"12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf"});
  const u=result.structuredContent;if(result.isError||!u?.success||!u.id){store("lastUploadUncertainResponse",result);await helper("event",{batch_dir:b.batch_dir,name:"upload-error-"+x.sequence+"-"+Date.now()+".json",data:{sequence:x.sequence,response:result,status:"UPLOAD_UNCERTAIN_NO_RETRY_UNTIL_REMOTE_RECONCILIATION"}});throw Error("UPLOAD_UNCERTAIN_"+x.sequence);}
  x.remote_id=u.id;x.remote_url=u.url;
  await helper("upload",{batch_dir:b.batch_dir,sequence:x.sequence,remote_id:u.id,remote_url:u.url,upload_response:u});
  text({phase:"uploaded",sequence:x.sequence,bytes:x.bytes});
 }
 store("activeBatch",b);
 await helper("end",{batch_dir:b.batch_dir});
 for(const x of b.files){
  if(x.duplicate_of_verified||x.duplicate_of_sequence)continue;
  let pass=false;
  for(let attempt=1;attempt<=2;attempt++){
   const mr=await tools.mcp__codex_apps__google_drive_get_file_metadata({fileId:x.remote_id,fields:"*"});const m=mr.structuredContent;
   if(mr.isError||!m||m.shared!==false||m.permissions?.length!==1||m.permissions[0].role!=="owner"||m.permissions[0].emailAddress!=="kgk2930@gmail.com"||!m.parent_ids?.includes("12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf")||Number(m.size)!==x.bytes)throw Error("REMOTE_METADATA_GATE_"+x.sequence);
   const fr=await tools.mcp__codex_apps__google_drive_fetch({url:m.url,download_raw_file:true,include_base64:false});
   const f=fr.structuredContent?.file_uri;if(fr.isError||!f?.download_url)throw Error("FETCH_BLOCKED_"+x.sequence);
   const v=JSON.parse(await helper("verify",{batch_dir:b.batch_dir,sequence:x.sequence,attempt,remote_id:x.remote_id,metadata:m,file_id:f.file_id,download_url:f.download_url}));
   text(v);if(v.status==="VERIFIED"){pass=true;break;}await new Promise(r=>setTimeout(r,2000));
  }
  if(!pass)throw Error("UPLOADED_UNVERIFIED_STOP_"+x.sequence);
 }
 text({batch:b.batch,phase:"ALL_FILES_VERIFIED_PENDING_POSTFLIGHT"});
}

