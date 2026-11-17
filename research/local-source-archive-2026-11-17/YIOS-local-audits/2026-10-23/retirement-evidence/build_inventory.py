from pathlib import Path
import json,re
r=Path(__file__).parent;t=(r/'registered-transcript.txt').read_text();tokens=list(re.finditer(r'\S+',t));norm='';mapping=[]
for m in tokens:
 if norm:norm+=' ';mapping.append(m.start()-1)
 norm+=m[0];mapping.extend(range(m.start(),m.end()))
anchors=[('T01',"Uh what you don't know","Let's rewind",'CONDITIONALLY_SUPPORTED'),('T02','If instead of buying that truck','One truck decision.','CONDITIONALLY_SUPPORTED'),('T03','The difference between retiring','Meanwhile, your college roommate','UNSUPPORTED_OR_UNVERIFIED'),('T04','Meanwhile, your college roommate',"You look like you're winning.",'CONDITIONALLY_SUPPORTED'),('T05',"Most people don't just buy",'And now we arrive','CONDITIONALLY_SUPPORTED'),('T06','Meanwhile, the average American','The person who looks wealthy','DENOMINATOR_MISMATCH'),('T07','That $14,900 invested','Strategy two','MATHEMATICALLY_REPRODUCED'),('T08','That $35,650 invested','Strategy three','CONFIRMED_ERROR'),('T09','That $23,000 becomes','Strategy four','CONFIRMED_ERROR'),('T10','The 42,000 dollar difference','Strategy five','CONFIRMED_ERROR'),('T11','The 11,800 dollars annual difference',"The goal isn't",'MATHEMATICALLY_REPRODUCED'),('T12','The goal is to recognize',"Here's what nobody tells",'CONDITIONALLY_SUPPORTED'),('T13',"You're about to destroy",'Researchers call','UNSUPPORTED_OR_UNVERIFIED'),('T14','The median American','You cannot spend','DENOMINATOR_MISMATCH'),('T15','until you wake up at 65',"The system isn't broken",'UNSUPPORTED_OR_UNVERIFIED'),('T16','Let me tell you what $500,000','Um that truck','MISINTERPRETED_WITHDRAWAL_RULE'),('T17','Um that truck you bought',"That's your grocery budget",'MISINTERPRETED_WITHDRAWAL_RULE'),('T18','Every time you make that $1,076',"And here's the part",'UNSUPPORTED_OR_UNVERIFIED'),('T19','Every $1,000 you spend','Um, every car payment','CONDITIONALLY_SUPPORTED'),('T20','Think about it this way',"That's the real cost",'CONDITIONALLY_SUPPORTED'),('T21',"You're not buying a $70,000 truck",'And the dealership','CONDITIONALLY_SUPPORTED'),('T22','The average American will own 13 cars',"And here's what makes",'UNSUPPORTED_OR_UNVERIFIED'),('T23','Understand that the $1,076','Uh the choice','UNSUPPORTED_OR_UNVERIFIED'),('T24','And 30 years later',"That's the real flex",'UNSUPPORTED_OR_UNVERIFIED')]
a=[]
for id,s,e,k in anchors:
 start=norm.index(s);end=norm.index(e,start);os=mapping[start];oe=mapping[end]
 a.append({'id':id,'source':'SQLite transcripts youtube_video_id=SsHQ-TtXhRQ / transcript_text','start_char_inclusive':os,'end_char_exclusive':oe,'wording':t[os:oe],'display_wording':re.sub(r'\s+',' ',t[os:oe]).strip(),'classification':k})
(r/'transcript-claim-inventory.json').write_text(json.dumps(a,indent=2))
aud=json.loads((r/'NICK_165.json').read_text());out=[]
def walk(x,p=''):
 if isinstance(x,dict):
  for k,v in x.items():walk(v,p+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,p+'/'+str(i))
 elif isinstance(x,str) and any(v in x.lower() for v in ['retir','withdraw','compoun','nominal','principal','7%','10%','future value']):out.append({'source':'NICK_165.json','json_pointer':p,'origin':'ANALYST_COMMENTARY_UNLESS_EXPLICIT_CLAIM_FIELD_QUOTING_TRANSCRIPT','wording':x})
walk(aud);(r/'audit-retirement-language-inventory.json').write_text(json.dumps(out,indent=2))
for x in a:print(x['id'],x['start_char_inclusive'],x['end_char_exclusive'],x['display_wording'][:65])
print('SOCIAL SECURITY OCCURRENCES',norm.lower().count('social security'),'4%',norm.count('4%'))
