"""Read-only: dump first ~150 words of transcript for long videos of 7 DB channels -> CSV (analysis input)."""
import sqlite3, csv, sys, re
DB="file:../../../data/catalog/finance_economics_complete.db?mode=ro"
CH={"UCP9RPj_BG0vit2TNM7LuRxA":"039 Crayon","UCiBGqUxeTe4AYQyRseSZaKw":"024 Monkey","UCZXShYiBJlahi8mCNiU3XBg":"059 CapitalCase",
"UC_DdIoJzHZXlEKTVy41_KQw":"066 Nutshell","UC14Fb2zWTEZklONPXFbLrTQ":"055 Primate","UCrNfRFWnLC3tCy1TnyhVQ7g":"037 CasualFin","UCZ4AMrDcNrfy3X6nsU8-rPg":"040 EconExplained"}
con=sqlite3.connect(DB,uri=True)
rows=con.execute(f"""select v.channel_id,v.video_id,v.title,v.published,v.duration_seconds,v.views,t.text,t.source,t.status
 from videos v join transcripts t on t.video_id=v.video_id
 where v.channel_id in ({','.join('?'*len(CH))}) and v.duration_seconds>=180
 order by v.channel_id, t.status, t.source""",list(CH)).fetchall()
seen={}
for r in rows:  # first transcript per video; ORDER prefers COMPLETE
    if r[1] not in seen and r[6]: seen[r[1]]=r
out=csv.writer(open(sys.argv[1],"w",newline=""))
out.writerow(["channel","video_id","title","published","dur_s","views","t_source","t_status","opening_150w"])
for r in seen.values():
    w=re.sub(r"\s+"," ",r[6]).split(" ")
    out.writerow([CH[r[0]],r[1],r[2],r[3],r[4],r[5],r[7],r[8]," ".join(w[:150])])
print(len(seen))
