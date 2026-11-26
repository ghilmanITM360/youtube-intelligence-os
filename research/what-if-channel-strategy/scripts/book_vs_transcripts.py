# Map book chapters (OCR) to What If transcripts by word 5-gram containment + key-term check.
# usage: python3 book_vs_transcripts.py <dir containing book/book_ocr.txt (OCR text of the 15 HTML parts)> <research/what-if-scripts>
import re,sys,json,glob
S=sys.argv[1]; R=sys.argv[2]
t=open(S+'/book/book_ocr.txt').read()
parts=re.split(r'Original PDF page (\d+) of 321',t)
pp={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
# chapter start pages (PDF) and names, from TOC + heading detection
CH=[(16,'Global Windstorm'),(22,'Relativistic Baseball'),(25,'Spent Fuel Pool'),(29,'W&W #1'),(30,'New York-Style Time Machine'),(38,'Soul Mates'),(42,'Laser Pointer'),(50,'Periodic Wall of the Elements'),(58,'Everybody Jump'),(62,'A Mole of Moles'),(67,'Hair Dryer'),(75,'W&W #2'),(76,'The Last Human Light'),(83,'Machine-Gun Jetpack'),(88,'Rising Steadily'),(92,'W&W #3'),(93,'Orbital Submarine'),(98,'Short-Answer Section'),(104,'Lightning'),(110,'W&W #4'),(111,'Human Computer'),(117,'Little Planet'),(122,'Steak Drop'),(127,'Hockey Puck'),(129,'Common Cold'),(134,'Glass Half Empty'),(140,'W&W #5'),(141,'Alien Astronomers'),(146,'No More DNA'),(152,'Interplanetary Cessna'),(157,'W&W #6'),(158,'Yoda'),(161,'Flyover States'),(165,'Falling with Helium'),(168,'Everybody Out'),(172,'W&W #7'),(173,'Self-Fertilization'),(183,'High Throw'),(189,'Lethal Neutrinos'),(193,'W&W #8'),(194,'Speed Bump'),(198,'Lost Immortals'),(202,'Orbital Speed'),(207,'FedEx Bandwidth'),(210,'Free Fall'),(214,'W&W #9'),(215,'Sparta'),(219,'Drain the Oceans'),(225,'Drain the Oceans: Part II'),(232,'Twitter'),(237,'Lego Bridge'),(243,'Longest Sunset'),(248,'Random Sneeze Call'),(251,'W&W #10'),(252,'Expanding Earth'),(259,'Weightless Arrow'),(263,'Sunless Earth'),(267,'Updating a Printed Wikipedia'),(270,'Facebook of the Dead'),(274,'Sunset on the British Empire'),(277,'Stirring Tea'),(281,'All the Lightning'),(285,'Loneliest Human'),(288,'W&W #11'),(289,'Raindrop'),(293,'SAT Guessing'),(295,'Neutron Bullet'),(304,'W&W #12'),(305,'Richter 15'),(310,'END')]
def toks(s): return re.findall(r"[a-z0-9]+",s.lower().replace('’',"'"))
def grams(w,n=5): return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}
book=[]
for (p,name),(q,_) in zip(CH,CH[1:]):
  txt=' '.join(pp.get(k,'') for k in range(p,q))
  book.append((name,p,q-1,grams(toks(txt))))
vids=[]
for f in sorted(glob.glob(R+'/long/*.md')+glob.glob(R+'/shorts/*.md')):
  s=open(f).read(); title=s.split('\n')[0][2:]; vid=re.search(r'Video ID \| `([^`]+)`',s).group(1)
  body=s.split('## Script',1)[1]; g=grams(toks(body))
  vids.append((vid,title,f.split('/')[-2],g))
res=[]
for name,p,q,bg in book:
  hits=[]
  for vid,title,fmt,vg in vids:
    if not vg: continue
    c=len(bg&vg)/len(vg)   # share of transcript 5-grams found in this chapter
    if c>=0.08: hits.append((round(c,3),vid,fmt,title))
  hits.sort(reverse=True)
  res.append(dict(chapter=name,pdf_pages=f'{p}-{q}',matches=[dict(containment=h[0],video_id=h[1],format=h[2],title=h[3]) for h in hits]))
json.dump(res,open(S+'/book_map.json','w'),indent=1)
for r in res: print(f"{r['chapter']:32} p{r['pdf_pages']:8} ", '; '.join(f"{m['video_id']}({m['format'][0]}) {m['containment']}" for m in r['matches']) or '-')
# transcripts not matched to any chapter
used={m['video_id'] for r in res for m in r['matches']}
print('\nTranscripts with no book chapter >=0.08:')
for vid,title,fmt,vg in vids:
  if vid not in used:
    best=max(((len(bg&vg)/max(len(vg),1)),name) for name,p,q,bg in book)
    print(f"  {vid} ({fmt}) best={best[0]:.3f} [{best[1]}] {title}")
