#!/usr/bin/env python3
"""Usage: python3 -I search_book.py 'fall OR heat'  -> id, pdf pages, title, originality"""
import sqlite3,sys,csv,os
d=os.path.dirname(os.path.abspath(__file__));idx={r['question_id']:r for r in csv.DictReader(open(d+'/BOOK_INDEX.csv'))}
for (i,) in sqlite3.connect(d+'/book_index.sqlite').execute("select id from q where q match ? order by rank",(sys.argv[1],)):
    r=idx[i];print(i,'pdf p.'+r['pdf_p'],'(printed '+r['printed_p']+')',r['chapter_title'],'|',r['originality'],'|',r['detail_tier'])
