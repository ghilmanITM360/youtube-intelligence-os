"""Last-80-words of transcript vs tier (S/W/M within channel). Flags (regex, INFERRED): CTA (subscribe/like/comment/channel), NEXT (next video/watch this/another video/video on screen), SPONSOR."""
import csv,re,sqlite3,collections
rows=list(csv.DictReader(open("../_analysis/openings_tiered_2026-11-13.csv")))
con=sqlite3.connect("file:../../../data/catalog/finance_economics_complete.db?mode=ro",uri=True)
CTA=re.compile(r"subscribe|like (the|this) video|hit the|comment|leave a|bell",re.I)
NEXT=re.compile(r"next video|watch (this|that|next)|another video|on screen|check out|up next|click",re.I)
out=[];cnt=collections.defaultdict(lambda:collections.Counter())
for r in rows:
    t=con.execute("select text from transcripts where video_id=? order by status limit 1",(r["video_id"],)).fetchone()
    w=re.sub(r"\s+"," ",t[0]).split(" ")[-80:] if t and t[0] else []
    e=" ".join(w); f=("CTA" if CTA.search(e) else "")+("NEXT" if NEXT.search(e) else "")
    cnt[r["tier"]]["n"]+=1; cnt[r["tier"]]["CTA"]+=bool(CTA.search(e)); cnt[r["tier"]]["NEXT"]+=bool(NEXT.search(e))
    out.append({"channel":r["channel"],"video_id":r["video_id"],"tier":r["tier"],"views":r["views"],"flags":f,"last_80w":e})
for k in "SMW": print(k,dict(cnt[k]))
w=csv.DictWriter(open("../_analysis/endings_2026-11-13.csv","w",newline=""),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
