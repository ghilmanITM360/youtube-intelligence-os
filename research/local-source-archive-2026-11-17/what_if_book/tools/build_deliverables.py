import csv, hashlib, json, re
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'WhatIf_Complete_Extraction'
SOURCE=next(ROOT.glob('Randall-Munroe-What-If*.pdf'))
AUD=OUT/'00_SOURCE_AUDIT'; QDIR=OUT/'01_ALL_QUESTIONS'; FULL=OUT/'02_FULL_QUESTION_DATA'; TRANS=OUT/'03_ORIGINAL_TRANSCRIPTIONS'; QA=OUT/'06_QUALITY_AUDIT'
for p in [QDIR,FULL,TRANS,QA]:p.mkdir(parents=True,exist_ok=True)
data=[json.loads((ROOT/'tools'/name).read_text()) for name in ['questions_early.json','review_middle.json','review_late.json']]

def row_for(raw,group):
 if group==0:
  return dict(section_type=raw['section_type'],chapter_title=raw['chapter_title'],original_question=raw['original_question'],submitted_by=raw.get('submitted_by'),pdf_page_start=raw['pdf_page_start'],pdf_page_end=raw['pdf_page_end'],short_answer_summary='',detailed_scientific_explanation='',initial_assumptions=[],scientific_principles=[],calculations=[],quantitative_facts=[],footnotes=[],references=[],uncertainties_and_limitations=[],verification_status='QUESTION_VISUALLY_VERIFIED; ANSWER_OCR_NEEDS_REVIEW')
 if group==1:
  weird='Weird' in raw['chapter'];return dict(section_type='weird_questions' if weird else 'main_chapter',chapter_title=raw['chapter'],original_question=raw['question'],submitted_by=raw.get('submitter'),pdf_page_start=raw['pdf_start'],pdf_page_end=raw['pdf_end'],short_answer_summary=raw.get('summary',''),detailed_scientific_explanation=raw.get('detailed_explanation',''),initial_assumptions=raw.get('assumptions',[]),scientific_principles=raw.get('principles',[]),calculations=[],quantitative_facts=raw.get('quantitative',[]),footnotes=raw.get('footnotes',[]),references=[],uncertainties_and_limitations=raw.get('limitations',[]),verification_status='VISUALLY_REVIEWED; SOURCE_OCR_NEEDS_PROOFREAD')
 weird=raw['kind']=='weird_inbox_question';return dict(section_type='weird_questions' if weird else 'main_chapter',chapter_title=raw['chapter_title'],original_question=raw['question_text_exact'],submitted_by=raw.get('submitter'),pdf_page_start=raw['pdf_page_start'],pdf_page_end=raw['pdf_page_end'],short_answer_summary=raw.get('summary',''),detailed_scientific_explanation=raw.get('detailed_scientific_explanation',[]),initial_assumptions=raw.get('assumptions',[]),scientific_principles=raw.get('principles',[]),calculations=[],quantitative_facts=raw.get('quantitative_details',[]),footnotes=raw.get('footnotes',[]),references=[],uncertainties_and_limitations=raw.get('limitations',[]),verification_status='VISUALLY_REVIEWED; SOURCE_OCR_NEEDS_PROOFREAD')

rows=[row_for(q,i) for i,d in enumerate(data) for q in d['questions']]
rows.sort(key=lambda r:(r['pdf_page_start'], {'main_chapter':0,'short_answer':1,'weird_questions':2}[r['section_type']]))
for idx,r in enumerate(rows,1):
 r['question_id']=f'WI-{idx:04d}';r['printed_page_start']=r['pdf_page_start']-15 if r['pdf_page_start']>=16 else None;r['printed_page_end']=r['pdf_page_end']-15 if r['pdf_page_end']>=16 else None
 r['source_page_references']=list(range(r['pdf_page_start'],r['pdf_page_end']+1))
 r['extraction_notes']=['Source transcript is machine OCR and requires line-by-line proofreading against page images.']
 if r['section_type']=='weird_questions':r['extraction_notes'].append('The book may offer only a cartoon or no scientific answer for this submitted question.')
 folder={'main_chapter':'chapters','short_answer':'short_answers','weird_questions':'weird_questions'}[r['section_type']]
 target=TRANS/folder/f"{r['question_id']}.md";target.parent.mkdir(exist_ok=True)
 pages=[]
 for n in r['source_page_references']:
  f=AUD/'ocr'/f'page_{n:03d}.txt'
  pages.append(f"\n\n## PDF page {n} / printed page {n-15}\n\n"+(f.read_text(errors='replace') if f.exists() else '[OCR MISSING — NEEDS_REVIEW]'))
 target.write_text(f"# {r['chapter_title']} — {r['question_id']}\n\nMachine OCR source transcription; shared pages may include adjacent questions. Verify against page images before quotation.\n"+''.join(pages))
 r['original_answer_transcription_file']=str(target.relative_to(OUT))
 r['question_topics']=[];r['figures']=[];r['related_question_ids']=[]
 (FULL/f"{r['question_id']}.json").write_text(json.dumps(r,ensure_ascii=False,indent=2))
 (FULL/f"{r['question_id']}.md").write_text(f"# {r['question_id']}: {r['chapter_title']}\n\n**Question:** {r['original_question']}\n\n**Submitted by:** {r['submitted_by'] or 'Not given'}\n\n**PDF pages:** {r['pdf_page_start']}–{r['pdf_page_end']}\n\n**Status:** {r['verification_status']}\n\n## Answer summary\n\n{r['short_answer_summary'] or 'Not yet independently summarized.'}\n\n## Scientific explanation\n\n{r['detailed_scientific_explanation'] or 'See linked OCR transcription; detailed explanation needs review.'}\n\n**OCR source:** {r['original_answer_transcription_file']}\n")

assert len(rows)==91
assert Counter(r['section_type'] for r in rows)=={'main_chapter':57,'weird_questions':27,'short_answer':7}
assert all((AUD/'ocr'/f'page_{n:03d}.txt').exists() for n in range(1,322))
hashvalue=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
metadata={'source_pdf':str(SOURCE),'sha256':hashvalue,'physical_pdf_pages':321,'question_count':len(rows),'ocr_caveat':'Transcriptions are machine OCR and are not certified verbatim; page images are authoritative.'}
db={'metadata':metadata,'questions':rows,'chapters':[],'scientific_facts':[],'calculations':[],'figures':[],'references':[],'quality_status':[]}
for r in rows:
 if not any(c['chapter_title']==r['chapter_title'] for c in db['chapters']):db['chapters'].append({'chapter_id':f"CH-{len(db['chapters'])+1:03d}",'chapter_title':r['chapter_title'],'section_type':r['section_type'],'pdf_page_start':r['pdf_page_start'],'pdf_page_end':r['pdf_page_end']})
 for j,f in enumerate(r['quantitative_facts'] if isinstance(r['quantitative_facts'],list) else [],1):db['scientific_facts'].append({'fact_id':f"{r['question_id']}-F{j:02d}",'question_id':r['question_id'],'statement':f,'source_pdf_page_start':r['pdf_page_start'],'verification_status':'REVIEWED_NOTE; SOURCE_OCR_NEEDS_PROOFREAD'})
for group in data[1:]:
 for ref in group.get('references',[]):db['references'].append(ref)
 for fig in group.get('figures',[]):db['figures'].append(fig)
db['figures']+=json.loads((ROOT/'tools/figures_early.json').read_text()).get('figures',[])
db['quality_status']=[{'check':'All source PDF pages OCR processed','status':'PASS','details':'321/321 text files'}, {'check':'All answer transcripts proofread visually','status':'INCOMPLETE','details':'Machine OCR requires visual proofreading'}, {'check':'Early chapter explanation records','status':'INCOMPLETE','details':'32 question records lack detailed answer notes'}, {'check':'Question discovery','status':'PROVISIONAL','details':'91 source questions identified; duplicate and page-boundary audit pending'}]
(OUT/'what_if_complete_database.json').write_text(json.dumps(db,ensure_ascii=False,indent=2))
(QDIR/'all_questions.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (QDIR/'all_questions.jsonl').open('w') as f:
 for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
cols=['question_id','section_type','chapter_title','original_question','submitted_by','pdf_page_start','pdf_page_end','printed_page_start','printed_page_end','short_answer_summary','detailed_scientific_explanation','original_answer_transcription_file','verification_status']
with (QDIR/'all_questions.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(cols)
 for r in rows:w.writerow([json.dumps(r.get(k),ensure_ascii=False) if isinstance(r.get(k),(list,dict)) else r.get(k) for k in cols])
(QDIR/'all_questions.md').write_text('# All identified original questions\n\n'+''.join(f"## {r['question_id']} — {r['chapter_title']}\n\n{r['original_question']}\n\nPDF pp. {r['pdf_page_start']}–{r['pdf_page_end']} · {r['section_type']}\n\n**Answer:** {r['short_answer_summary'] or 'Detailed answer pending review.'}\n\n" for r in rows))

wb=Workbook();ws=wb.active;ws.title='Questions'
for title in ['Chapters','Scientific facts','Calculations','Figures','References','Quality status']:wb.create_sheet(title)
for sheet,key in [('Questions','questions'),('Chapters','chapters'),('Scientific facts','scientific_facts'),('Calculations','calculations'),('Figures','figures'),('References','references'),('Quality status','quality_status')]:
 sh=wb[sheet];records=db[key];keys=list(dict.fromkeys(k for x in records for k in x))
 if not keys:keys=['status'];records=[{'status':'No independently verified records yet'}]
 sh.append(keys)
 for x in records:sh.append([json.dumps(x.get(k),ensure_ascii=False) if isinstance(x.get(k),(list,dict)) else x.get(k) for k in keys])
 sh.freeze_panes='A2';sh.auto_filter.ref=sh.dimensions
 for cell in sh[1]:cell.fill=PatternFill('solid',fgColor='263B53');cell.font=Font(color='FFFFFF',bold=True)
 for col in sh.columns:
  letter=col[0].column_letter;sh.column_dimensions[letter].width=65 if col[0].value in ('original_question','short_answer_summary','detailed_scientific_explanation') else 25
 for row in sh.iter_rows(min_row=2):
  for cell in row:cell.alignment=Alignment(wrap_text=True,vertical='top')
wb.save(OUT/'what_if_complete_database.xlsx')
qwb=Workbook();qws=qwb.active;qws.title='Questions'
for row in wb['Questions'].values:qws.append(row)
qws.freeze_panes='A2';qws.auto_filter.ref=qws.dimensions
qwb.save(QDIR/'all_questions.xlsx')

styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='Question',parent=styles['Heading2'],fontSize=11,leading=14,spaceAfter=8));styles.add(ParagraphStyle(name='SmallBody',parent=styles['BodyText'],fontSize=8.5,leading=12,spaceAfter=6))
story=[Paragraph('What If? — 91 Question Research Index',styles['Title']),Paragraph('AI-readable research report generated from the supplied 321-page PDF. Source answer transcriptions are machine OCR and require proofreading against the original page images. Answer summaries are available for 59 records; detailed scientific explanations for 52. The 32 early-section records retain question metadata and OCR source pending explanation review.',styles['BodyText']),Spacer(1,10)]
for r in rows:
 story.append(Paragraph(escape(f"{r['question_id']} — {r['chapter_title']}"),styles['Question']))
 for label,value in [('Question',r['original_question']),('Submitted by',r['submitted_by'] or 'Not stated'),('Section',r['section_type']),('PDF pages',f"{r['pdf_page_start']}–{r['pdf_page_end']}"),('Answer summary',r['short_answer_summary'] or 'Pending source-grounded explanation'),('Scientific explanation',r['detailed_scientific_explanation'] or 'See OCR source file; explanation pending review.'),('Source transcript',r['original_answer_transcription_file']),('Verification',r['verification_status'])]:
  if isinstance(value,list):value='; '.join(map(str,value))
  story.append(Paragraph(f'<b>{escape(label)}:</b> {escape(str(value))}',styles['SmallBody']))
 story.append(Spacer(1,8))
SimpleDocTemplate(str(OUT/'what_if_91_questions_research.pdf'),pagesize=(595,842),rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=42).build(story)

(QA/'coverage_report.md').write_text(f"# Coverage\n\nSource pages OCR processed: 321/321. Identified original questions: 91 (57 main, 27 Weird, 7 Short-Answer). Answer summaries: 59/91. Detailed scientific explanations: 52/91. Early records pending: 32. Seven Weird questions have short notes but no detailed scientific explanation. Source transcriptions are machine OCR, not fully proofread.\n")
(QA/'unresolved_items.md').write_text('# Unresolved\n\n- All machine OCR transcriptions require visual proofreading.\n- 32 early-section questions lack independent answer explanation notes.\n- Weird questions may intentionally have no scientific answer in the book.\n- Figure crops and question-to-figure mapping are incomplete.\n- Some source numerical claims were flagged by reviewers and need page-level checking.\n')
(QA/'verification_report.json').write_text(json.dumps({'source_sha256':hashvalue,'ocr_pages':321,'questions':91,'counts':dict(Counter(r['section_type'] for r in rows)),'answer_summaries':sum(bool(r['short_answer_summary']) for r in rows),'detailed_explanations':sum(bool(r['detailed_scientific_explanation']) for r in rows),'source_transcripts':len(rows),'final_source_verification':'INCOMPLETE'},indent=2))
(OUT/'README.md').write_text('# What If? research database\n\nThe Excel workbook and searchable PDF contain 91 source questions. The JSON file preserves structured data and links to page-level OCR transcriptions. The original scanned PDF remains unchanged. Treat machine OCR as unverified; compare quotations, equations, units, footnotes, and figures with page images before publication. See 06_QUALITY_AUDIT for unresolved work.\n')
print(json.dumps({'questions':len(rows),'counts':dict(Counter(r['section_type'] for r in rows)),'explanation_notes':sum(bool(r['detailed_scientific_explanation']) for r in rows),'sha256':hashvalue,'workbook':str(OUT/'what_if_complete_database.xlsx'),'pdf':str(OUT/'what_if_91_questions_research.pdf')},indent=2))
