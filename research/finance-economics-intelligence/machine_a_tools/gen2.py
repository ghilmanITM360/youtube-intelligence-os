"""Generic NICK packet generator; bespoke analyst content comes from a spec file (argv[1])."""
import csv,json,re,hashlib,statistics as st,zipfile,sys,sqlite3,runpy
W='/Users/ghilmankhan/workprojects/yios-finance-machine-a'
B=W+'/research/finance-economics-intelligence/'
sp=runpy.run_path(sys.argv[1]); S=sp['DIR']; VID=sp['VID']; NICK=sp['NICK']; DATE=__import__('datetime').date.today().isoformat()
text=open(S+'text.txt').read(); norm=' '.join(text.split())
m={r['Video_ID']:r for r in csv.DictReader(open(B+'VIDEO_MASTER.csv'))}
tc={r['Video_ID']:r for r in csv.DictReader(open(B+'TRANSCRIPT_COVERAGE.csv'))}[VID]
r=m[VID]; peers=r['Peer_Video_IDs'].split('|'); PUB=r['Published_at_raw'][:10]
con=sqlite3.connect(f'file:{W}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
likes,comments=con.execute('select likes,comments from videos where youtube_video_id=?',(VID,)).fetchone()
def loc(anchor):
    mt=re.search(r'\s+'.join(map(re.escape,anchor.split())),text); assert mt,anchor
    s=mt.start(); return s,s+160,text[s:s+160]
REFS=[f'VIDEO_MASTER.csv:{VID}',f'TRANSCRIPT_COVERAGE.csv:{VID}',f'audit-batches/{NICK}_READ_RECEIPTS.json']
DS=f'Video publication context {PUB}; source dates and access limitations in companion receipts'
ca=[]
for i,(c,a,ass,sids) in enumerate(sp['CLAIMS'],1):
    s,e,w=loc(a); ca.append({'claim_id':f'C{i:02d}','claim':c,'start_char':s,'end_char':e,'stored_text_witness':w,'assessment':ass,'source_ids':sids,'evidence_kind':'ANALYST_FACT_CHECK_OR_EXPLICIT_UNVERIFIED_CREATOR_ASSERTION','date_scope':DS})
rate=lambda p:int(m[p]['Views'])/float(m[p]['Age_days'])
vpd=int(r['Views'])/float(r['Age_days']); med10=st.median(map(rate,peers)); med5=st.median(map(rate,peers[:5]))
tier=lambda x:'STRONG' if x>=2 else 'WEAK' if x<=0.5 else 'TYPICAL'
low=sorted(peers,key=lambda p:float(m[p]['Lifetime_rate_ratio']))[:3]
words=norm.split(); opening=' '.join(words[:80]); ending=' '.join(words[-70:])
first=norm[:norm.index(sp['FIRST_END'])+len(sp['FIRST_END'])]
kind=sp.get('IMAGE','maxresdefault'); img=open(S+f'dl/{kind}.jpg','rb').read(); ish=hashlib.sha256(img).hexdigest(); dims=sp['DIMS']
n=len(text); rg=[list(x) for x in sp['RANGES']]; rg[-1][1]=n
per1k=lambda x:x/int(r['Views'])*1000
review={'Video_ID':VID,'review_date':DATE,'statuses':{k:'COMPLETE_LIMITED_EVIDENCE' for k in ['PERFORMANCE_REVIEW','SCRIPT_REVIEW','THUMBNAIL_REVIEW','TITLE_REVIEW','TOPIC_REVIEW','VIRALITY_REVIEW']},
'title':{'review_scope':'ACTUAL_TITLE','source_refs':REFS,'analysis':sp['TITLE'],'peer_comparison_ids':peers[:5],'search_demand':'UNKNOWN;no query-volume,Trends or impressions evidence',
 'peer_titles':[{'Video_ID':p,'Title':m[p]['Title'],'Performance_tier':m[p]['Performance_tier']} for p in peers[:5]]},
'thumbnail':{'review_scope':'ACTUAL_IMAGE','source_refs':REFS,'analysis':sp['THUMB'],
 'image_path':f'research/finance-economics-intelligence/audit-batches/NICK_{VID}.jpg','image_source':f'https://i.ytimg.com/vi/{VID}/{kind}.jpg','image_sha256':ish,'dimensions':dims,'mobile_review_width':320,
 'historical_design':'UNKNOWN;current capture cannot prove upload-era art','performance_effect':'UNKNOWN;no CTR/impressions/experiment'},
'script':{'review_scope':'FULL_STORED_TEXT','source_refs':REFS,'source':tc,
 'stored_text_completeness':f'All {n} canonical characters read sequentially in full in {len(rg)} bounded ranges; auto-generated untimed text{sp.get("COMPLETENESS_EXTRA","")}; audio, timed delivery and editing unverified.',
 'audio_verified':False,'timing':'OPENING_WORDS_ONLY','opening_words':opening,'ending_words':ending,
 'analysis':f'Full {n} canonical characters read. '+sp['SCRIPT'],'beat_map':sp['BEATS'],'claim_audit':ca},
'topic':{'review_scope':'FULL_TRANSCRIPT_TOPIC','source_refs':REFS,**sp['TOPIC'],'novelty_and_corpus_angle':sp['LESSON'],'competition':'Same-channel nearest-age peers in K01; not an independent niche or causal test'},
'virality':{'review_scope':'INDIVIDUAL_PUBLIC_EVIDENCE','source_refs':REFS,'causal_status':'DESCRIPTIVE_ASSOCIATION_NOT_CAUSAL',
 'analysis':f'Frozen {r["Views"]} views / {r["Age_days"]} days = {vpd:.5f} views/day. Against 10 peers {vpd/med10:.5f}x ({tier(vpd/med10)}); against 5 peers {vpd/med5:.5f}x ({tier(vpd/med5)}). '+sp['VIRAL'],
 'observed_result':f'Snapshot {r["Metric_snapshot_date"]}; {r["Duration_seconds"]} seconds; {likes} likes, {comments} comments ({per1k(likes):.2f} and {per1k(comments):.2f} per 1,000 views); not live or private analytics',
 'topic_demand':'UNKNOWN;interest hypothesis only','trend_timing':sp['TREND'],
 'competition':'Exact same-channel/format/snapshot peer cohorts and thresholds in K01','format_fit':sp['FORMAT'],
 'channel_context':f'Peer medians {med10:.5f}/{med5:.5f} views/day; exposure-confounded, not current velocity',
 'alternative_explanations':sp['ALTS'],
 'weak_performance_counterexamples':[{'Video_ID':p,'Title':m[p]['Title'],'Lifetime_rate_ratio':m[p]['Lifetime_rate_ratio'],'Performance_tier':m[p]['Performance_tier']} for p in low],
 'original_content_lesson':{'test':sp['LESSON'],'boundary':'Editorial hypothesis; use comprehension tests and real first-party data for causal claims'}},
'event':{'status':'LIMITED_PRIMARY_SOURCE_VERIFICATION','source_refs':REFS,'analysis':sp['EVENT']}}
json.dump({'batch_id':NICK,'status':'COMPLETE_LIMITED_EVIDENCE','reviews':[review]},open(S+f'{NICK}.json','w'),indent=1,ensure_ascii=False)
a,_,mem=tc['Evidence_locator'].partition('::'); zb=zipfile.ZipFile(W+'/'+a).read(mem)
rec={'batch_id':f'{NICK}_READ_RECEIPTS','reviews':[],'receipts':[{'Video_ID':VID,'scope':'FULL_STORED_TEXT','Text_SHA256':hashlib.sha256(text.encode()).hexdigest(),'character_count':n,'canonical_utf8_bytes':len(text.encode()),'canonical_whitespace_word_count':len(text.split()),'coverage_token_count':int(tc['Words']),'read_character_ranges':rg,
 'read_provenance':'Sequential full text read in bounded character ranges;read-only SQLite hash and normalized archive containment verified',
 'first_text_witness':first,'last_text_witness':ending,
 'range_boundary_witnesses':[{'start':s,'end':e,'first80':text[s:s+80],'last80':text[e-80:e]} for s,e in rg],
 'archive':a,'archive_sha256':hashlib.sha256(open(W+'/'+a,'rb').read()).hexdigest(),'archive_member':mem,'archive_member_sha256':hashlib.sha256(zb).hexdigest(),'archive_member_bytes':len(zb),'archive_member_lines':len(zb.splitlines()),
 'audio_verified':False,'image_sha256':ish,'image_bytes':len(img),'image_media_type':'image/jpeg','image_inspected_sizes':[dims,[320,180]],
 'registered_image_url':f'https://i.ytimg.com/vi/{VID}/{sp.get("REG","maxresdefault")}.jpg','fetched_image_url':f'https://i.ytimg.com/vi/{VID}/{kind}.jpg',
 'image_acquisition':sp['IMAGE_ACQ'],'acquired_date':DATE}],
'primary_source_receipts':[{**s,'accessed':DATE} for s in sp['SOURCES']],
'calculation_receipts':[
 {'calculation_id':'K01','method':'Frozen lifetime-view-rate: views / four-decimal age; nearest eligible same-channel/format/snapshot peers,0.5–2age; median10andfirst5;2.0strong/0.5weak',
  'results':{'views':int(r['Views']),'age_days':float(r['Age_days']),'views_per_day':vpd,'peer_median_10':med10,'peer_median_5':med5,'peer_ratio_10':vpd/med10,'peer_ratio_5':vpd/med5,'tier_10':tier(vpd/med10),'tier_5':tier(vpd/med5),'peer_ids_10':peers,'peer_ids_5':peers[:5],
   'peer_rows':[{'Video_ID':p,**{k:m[p][k] for k in ['Title','Views','Age_days','Format','Metric_snapshot_date','Performance_tier']}} for p in peers]},
  'limitations':'Lifetime public exposure-confounded snapshot,not current velocity; no private metrics,causal packaging or sales inference.'},
 {'calculation_id':'K02',**sp['K02']}],
'limits':sp['LIMITS']}
json.dump(rec,open(S+f'{NICK}_READ_RECEIPTS.json','w'),indent=1,ensure_ascii=False)
assert norm.startswith(first) and norm.endswith(ending)
assert abs(vpd/med10-float(r['Lifetime_rate_ratio']))<1e-5 and tier(vpd/med10)==r['Performance_tier']
print('ok',NICK,len(ca),round(vpd/med10,5),tier(vpd/med10),round(vpd/med5,5),ish)
