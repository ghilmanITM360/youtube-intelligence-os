#!/usr/bin/env python3
"""Build reference-only index of the 2014 What If? book extraction. Run: python3 -I build_book_index.py"""
import csv, json, os, re, sqlite3, hashlib, collections
B="/Users/ghilmankhan/workprojects/what if book"; X=B+"/WhatIf_Complete_Extraction"
OUT=os.path.dirname(os.path.abspath(__file__))
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
q=list(csv.DictReader(open(X+"/01_ALL_QUESTIONS/all_questions.csv")))
m=list(csv.DictReader(open(X+"/07_CHANNEL_BOOK_COMPARISON/all_91_video_matches.csv")))
vids=collections.defaultdict(list)
for v in m:
    for bid in filter(None,[s.strip() for s in v['book_question_ids'].replace(';',',').split(',')]):
        vids[bid].append((v['video_id'],v['format'],v['classification'],v['match_evidence']))
# INFERRED mechanism tags (keyword heuristic, ours, not from the book)
TAGS={'impact_fall':r'drop|fall|jump|land|terminal|re-?entry','heat_energy':r'heat|hot|fire|burn|cook|temperature|energy|nuclear|boil','fluid_pressure':r'water|ocean|rain|pressure|dive|drain|pool|air|wind','orbit_space':r'orbit|space|moon|mars|sun|planet|earth|satellite|rocket','light_speed_rel':r'light|laser|relativ|speed of','scale_count':r'everyone|all the|every|million|billion|population|human','electric_magnet':r'lightning|electric|magnet|battery|volt','bio_body':r'body|human|blood|eat|food|sleep|dna|cell'}
rows=[];ftsrows=[]
for x in q:
    i=x['question_id']; j=json.load(open(f"{X}/02_FULL_QUESTION_DATA/{i}.json"))
    det=x['detailed_scientific_explanation'].strip()
    tier='A_STRUCTURED' if len(det)>=350 and (j['scientific_principles'] or j['initial_assumptions'] or j['quantitative_facts']) else ('B_PROSE_ONLY' if len(det)>=350 else ('C_SHORT_NOTE' if len(det)>5 else 'D_NO_EXPLANATION'))
    txt=(x['chapter_title']+' '+x['original_question']+' '+x['short_answer_summary']).lower()
    tags=[t for t,rx in TAGS.items() if re.search(rx,txt)]
    vm=vids.get(i,[])
    rows.append(dict(question_id=i,section=x['section_type'],chapter_title=x['chapter_title'],question=x['original_question'],
      pdf_p=f"{x['pdf_page_start']}-{x['pdf_page_end']}",printed_p=f"{x['printed_page_start']}-{x['printed_page_end']}",
      transcription=f"{X}/{x['original_answer_transcription_file']}",record_json=f"{X}/02_FULL_QUESTION_DATA/{i}.json",
      source_status=x['verification_status'],detail_tier=tier,n_principles=len(j['scientific_principles']),n_assumptions=len(j['initial_assumptions']),
      n_quant_facts=len(j['quantitative_facts']),n_footnotes=len(j['footnotes']),mechanism_tags_INFERRED='|'.join(tags),
      channel_videos='|'.join(a for a,*_ in vm),channel_evidence='|'.join(f"{c}/{e}" for _,_,c,e in vm),
      originality=('COVERED_BY_CHANNEL' if any(c in('BOOK_2014_QUESTION_ANSWER',) for _,_,c,_e in vm) else 'PARTIAL_EXCERPT_OR_COMPILATION' if vm else 'NOT_ON_CHANNEL')))
    ftsrows.append((i,x['chapter_title'],x['original_question'],x['short_answer_summary'],'; '.join(j['scientific_principles']),'; '.join(j['initial_assumptions']),' '.join(tags)))
w=csv.DictWriter(open(OUT+"/BOOK_INDEX.csv","w",newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
db=OUT+"/book_index.sqlite"
if os.path.exists(db): os.remove(db)
c=sqlite3.connect(db);c.execute("create virtual table q using fts5(id,title,question,summary,principles,assumptions,tags)");c.executemany("insert into q values(?,?,?,?,?,?,?)",ftsrows);c.commit()
pdf=[f for f in os.listdir(B) if f.lower().endswith('.pdf')][0]
reg=dict(edition="Randall Munroe, What If? Serious Scientific Answers to Absurd Hypothetical Questions, Houghton Mifflin Harcourt, 2014 (per filename; PDF metadata title/author only)",
 pdf=dict(path=f"{B}/{pdf}",sha256=sha(f"{B}/{pdf}"),pages=321,producer="Google Books PDF Converter (scanned images, no text layer)",pdf_to_printed_offset=15),
 titles_workbook=dict(path=B+"/XKCD_What_If_Titles_and_Full_Scripts.xlsx",sha256=sha(B+"/XKCD_What_If_Titles_and_Full_Scripts.xlsx")),
 extraction_files={p:sha(f"{X}/{p}") for p in ["01_ALL_QUESTIONS/all_questions.csv","07_CHANNEL_BOOK_COMPARISON/all_91_video_matches.csv","04_FIGURES_AND_DIAGRAMS/figure_index.csv","what_if_complete_database.json"]},
 counts=dict(questions=len(rows),unique_ids=len({r['question_id'] for r in rows}),unique_question_text=len({r['question'].strip().lower() for r in rows}),by_section=dict(collections.Counter(r['section'] for r in rows)),by_detail_tier=dict(collections.Counter(r['detail_tier'] for r in rows)),by_originality=dict(collections.Counter(r['originality'] for r in rows))))
json.dump(reg,open(OUT+"/BOOK_SOURCE_REGISTRY.json","w"),indent=1)
print(json.dumps(reg['counts'],indent=1))
