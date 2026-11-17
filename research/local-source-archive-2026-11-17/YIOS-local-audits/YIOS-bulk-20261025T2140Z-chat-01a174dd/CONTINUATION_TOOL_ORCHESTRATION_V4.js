
const q=s=>"'"+s.replaceAll("'","'\\''")+"'";
async function helper(cmd,arg){
 let e=await tools.exec_command({cmd:"python3 "+q(load("bulkRoot")+"/continue_backup.py")+" "+q(cmd)+" "+q(JSON.stringify(arg)),max_output_tokens:7000,yield_time_ms:1000});
 while(e.session_id)e=await tools.write_stdin({session_id:e.session_id,chars:"",yield_time_ms:5000,max_output_tokens:7000});
 if(e.exit_code!==0)throw Error(e.output);return e.output.trim();
}


async function captureUiListing(){
 let b=load("activeBatch");
 const originalFolder=b.destination_folder_id||load("uiBatchFolderCreation")?.structuredContent?.id;
 b=JSON.parse(await helper("resume",{batch_dir:b.batch_dir}));b.destination_folder_id=originalFolder;
 const mm=(await tools.mcp__codex_apps__google_drive_get_file_metadata({fileId:originalFolder,fields:"*"})).structuredContent;
 if(mm.shared!==false||mm.permissions?.length!==1||mm.permissions[0].emailAddress!=="kgk2930@gmail.com")throw Error("FOLDER_PRIVACY");
 const lr=await tools.mcp__codex_apps__google_drive_fetch({url:mm.url});if(lr.isError)throw Error("DIRECT_CHILD_LIST_FAILED");
 const files=JSON.parse(lr.structuredContent.content).files;if(files.length>20)throw Error("UNEXPECTED_NAMESPACE_OBJECTS");
 const seen=new Set();
 for(const f of files){
  const x=b.files.find(x=>x.source_absolute.split("/").pop()===f.title);
  if(!x||seen.has(x.sequence))throw Error("UNEXPECTED_OR_DUPLICATE_REMOTE_NAME");seen.add(x.sequence);
  if(x.remote_id){if(x.remote_id!==f.id)throw Error("DUPLICATE_REMOTE_OBJECT");continue;}
  const m=(await tools.mcp__codex_apps__google_drive_get_file_metadata({fileId:f.id,fields:"*"})).structuredContent;
  if(m.shared!==false||m.permissions?.length!==1||m.permissions[0].role!=="owner"||m.permissions[0].emailAddress!=="kgk2930@gmail.com"||Number(m.size)!==x.bytes||!m.parent_ids.includes(originalFolder))throw Error("OBJECT_PRIVACY_OR_SIZE");
  await helper("upload",{batch_dir:b.batch_dir,sequence:x.sequence,remote_id:f.id,remote_url:m.url,upload_response:{method:"Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",metadata:m}});
  x.remote_id=f.id;x.remote_url=m.url;
 }
 store("activeBatch",b);store("lastUiNamespaceListingCount",files.length);text({batch:b.batch,namespace_objects:files.length,upload_ids_recorded:b.files.filter(x=>x.remote_id).length,pending_source_uploads:b.files.filter(x=>!x.remote_id).map(x=>x.sequence)});
 return b;
}


async function transferBatch(){
 const b=load("activeBatch");
 for(const x of b.files){
  if(x.duplicate_of_verified||x.duplicate_of_sequence||x.remote_id)continue;
  if(x.bytes>104857600){store("browserUploadRequired",x);throw Error("QUALIFIED_BROWSER_UPLOAD_REQUIRED_"+x.sequence);}
  await helper("check",{batch_dir:b.batch_dir,sequence:x.sequence});
  const result=await tools.mcp__codex_apps__google_drive_upload_file({file_uri:x.source_absolute,file_name:x.proposed_destination_name,mime_type:null,parent_folder_id:(b.destination_folder_id||"12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf")});
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
  const start=x.next_attempt||1;
  for(let attempt=start;attempt<start+2;attempt++){
   const mr=await tools.mcp__codex_apps__google_drive_get_file_metadata({fileId:x.remote_id,fields:"*"});const m=mr.structuredContent;
   if(mr.isError||!m||m.shared!==false||m.permissions?.length!==1||m.permissions[0].role!=="owner"||m.permissions[0].emailAddress!=="kgk2930@gmail.com"||!m.parent_ids?.includes(b.destination_folder_id||"12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf")||Number(m.size)!==x.bytes)throw Error("REMOTE_METADATA_GATE_"+x.sequence);
   if(x.verified_before&&x.verified_modified_time&&m.modified_time===x.verified_modified_time){pass=true;text({sequence:x.sequence,status:"EXISTING_FULL_VERIFICATION_REUSED_METADATA_UNCHANGED"});break;}
   const fr=await tools.mcp__codex_apps__google_drive_fetch({url:m.url,download_raw_file:true,include_base64:false});
   const f=fr.structuredContent?.file_uri;if(fr.isError||!f?.download_url)throw Error("FETCH_BLOCKED_"+x.sequence);
   const v=JSON.parse(await helper("verify",{batch_dir:b.batch_dir,sequence:x.sequence,attempt,remote_id:x.remote_id,metadata:m,file_id:f.file_id,download_url:f.download_url}));
   text(v);if(v.status==="VERIFIED"){pass=true;break;}await new Promise(r=>setTimeout(r,2000));
  }
  if(!pass)throw Error("UPLOADED_UNVERIFIED_STOP_"+x.sequence);
 }
 text({batch:b.batch,phase:"ALL_FILES_VERIFIED_PENDING_POSTFLIGHT"});
}


async function publish(info){
 const q=s=>"'"+s.replaceAll("'","'\\''")+"'";
 const stamp=info.checkpoint_dir.split("checkpoint-").pop();
 const ur=await tools.mcp__codex_apps__google_drive_upload_file({file_uri:info.handoff_path,file_name:info.handoff_path.split("/").pop(),mime_type:"text/markdown",parent_folder_id:"1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr"});
 store("lastHandoffUploadResponse",ur);
 const u=ur.structuredContent;if(ur.isError||!u?.success||!u.id)throw Error("CONTROL_UPLOAD_UNCERTAIN_"+stamp);
 let e=await tools.exec_command({cmd:"python3 - "+q(JSON.stringify({root:load("bulkRoot"),info,stamp,upload:u}))+" <<'PY'\nimport json,sys,datetime\nfrom pathlib import Path\na=json.loads(sys.argv[1]);r={'remote_id':a['upload']['id'],'remote_url':a['upload']['url'],'source_path':a['info']['handoff_path'],'sha256':a['info']['handoff_sha256'],'uploaded_bytes':a['info']['handoff_bytes'],'upload_response':a['upload'],'upload_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'UPLOADED_RETRIEVAL_PENDING'}\np=Path(a['root'])/('CONTROL-UPLOAD-'+a['stamp']+'.json')\nwith p.open('x') as f:json.dump(r,f,indent=2)\np.chmod(0o400)\nPY",max_output_tokens:200});if(e.exit_code!==0)throw Error(e.output);
 const m=(await tools.mcp__codex_apps__google_drive_get_file_metadata({fileId:u.id,fields:"*"})).structuredContent;
 if(m.shared!==false||m.permissions?.length!==1||m.permissions[0].role!=="owner"||m.permissions[0].emailAddress!=="kgk2930@gmail.com"||!m.parent_ids.includes("1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr"))throw Error("CONTROL_PRIVACY_GATE");
 const f=(await tools.mcp__codex_apps__google_drive_fetch({url:m.url,download_raw_file:true,include_base64:false})).structuredContent.file_uri;
 e=await tools.exec_command({cmd:"python3 - "+q(JSON.stringify({root:load("bulkRoot"),stamp,metadata:m,file_id:f.file_id,url:f.download_url}))+" <<'PY'\nimport json,sys,hashlib,urllib.request,datetime\nfrom pathlib import Path\na=json.loads(sys.argv[1]);r=Path(a['root']);u=json.loads((r/('CONTROL-UPLOAD-'+a['stamp']+'.json')).read_text());h=hashlib.sha256();n=0\nwith urllib.request.urlopen(a['url'],timeout=90) as f:\n for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)\nassert n==u['uploaded_bytes']==int(a['metadata']['size']) and h.hexdigest()==u['sha256']\nv={'status':'VERIFIED','remote_id':u['remote_id'],'retrieved_bytes':n,'sha256':h.hexdigest(),'metadata':a['metadata'],'retrieval_file_id':a['file_id'],'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Fresh authenticated complete remote raw read after upload ended; streamed SHA-256, no local substitution'}\np=r/('CONTROL-VERIFY-'+a['stamp']+'.json')\nwith p.open('x') as f:json.dump(v,f,indent=2)\np.chmod(0o400)\nprint(json.dumps({'status':'VERIFIED','remote_id':u['remote_id'],'remote_url':u['remote_url'],'bytes':n,'sha256':h.hexdigest()}))\nPY",max_output_tokens:600,yield_time_ms:1000});
 while(e.session_id)e=await tools.write_stdin({session_id:e.session_id,chars:"",yield_time_ms:5000,max_output_tokens:600});
 if(e.exit_code!==0)throw Error(e.output);text(e.output);store("lastPublishedHandoff",{...info,remote_id:u.id,remote_url:u.url});
}

