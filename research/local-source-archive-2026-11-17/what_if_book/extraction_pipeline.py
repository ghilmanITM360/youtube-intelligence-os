from pathlib import Path
import fitz, hashlib, json, csv, subprocess, concurrent.futures, time
from PIL import Image, ImageStat

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'WhatIf_Complete_Extraction'
SRC=next(ROOT.glob('*.pdf'))
def writejson(p,x):
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
def audit():
    for folder in ['00_SOURCE_AUDIT/pages','00_SOURCE_AUDIT/ocr','00_SOURCE_AUDIT/previews','01_ALL_QUESTIONS','02_FULL_QUESTION_DATA','03_ORIGINAL_TRANSCRIPTIONS/chapters','03_ORIGINAL_TRANSCRIPTIONS/short_answers','03_ORIGINAL_TRANSCRIPTIONS/weird_questions','04_FIGURES_AND_DIAGRAMS/figures','05_SCIENTIFIC_DATA','06_QUALITY_AUDIT']:
        (OUT/folder).mkdir(parents=True,exist_ok=True)
    d=fitz.open(SRC); rows=[]
    for i,p in enumerate(d):
        imagepath=OUT/f'00_SOURCE_AUDIT/pages/page_{i+1:03d}.png'
        if not imagepath.exists(): p.get_pixmap(dpi=300,colorspace=fitz.csGRAY).save(imagepath)
        preview=OUT/f'00_SOURCE_AUDIT/previews/page_{i+1:03d}.jpg'
        if not preview.exists():
            im=Image.open(imagepath); im.thumbnail((840,1080)); im.convert('RGB').save(preview,quality=90)
        with Image.open(imagepath) as im:
            hist=im.histogram(); ink=sum(hist[:220])/sum(hist)
        rows.append(dict(pdf_page=i+1,width_pt=p.rect.width,height_pt=p.rect.height,text_characters=len(p.get_text()),image_count=len(p.get_images()),image_dimensions=[list(x[2:4]) for x in p.get_images()],render_sha256=hashlib.sha256(imagepath.read_bytes()).hexdigest(),ink_fraction=ink,blank_candidate=ink<0.0001,render_file=str(imagepath.relative_to(OUT)),category='UNCLASSIFIED',printed_page=None,visual_review='PENDING'))
    writejson(OUT/'00_SOURCE_AUDIT/pdf_metadata.json',dict(source_path=str(SRC),sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(),size_bytes=SRC.stat().st_size,page_count=len(d),metadata=d.metadata,bookmarks=d.get_toc(),page_labels=d.get_page_labels(),text_pages=sum(bool(p.get_text().strip()) for p in d),render_dpi=300,source_unchanged=True))
    writejson(OUT/'00_SOURCE_AUDIT/page_inventory.json',rows)
    print('AUDIT',len(rows),flush=True)
def ocr_page(i):
    base=OUT/f'00_SOURCE_AUDIT/ocr/page_{i:03d}'
    if not base.with_suffix('.tsv').exists():
        import os
        env=os.environ.copy();env['OMP_THREAD_LIMIT']='1'
        r=subprocess.run(['tesseract',str(OUT/f'00_SOURCE_AUDIT/pages/page_{i:03d}.png'),str(base),'-l','eng','--psm','3','txt','tsv'],capture_output=True,text=True,env=env)
        if r.returncode: return dict(page=i,error=r.stderr)
    with base.with_suffix('.tsv').open() as f: words=[r for r in csv.DictReader(f,delimiter='\t') if r.get('text','').strip() and float(r['conf'])>=0]
    conf=[float(w['conf']) for w in words]
    return dict(page=i,status='OCR_COMPLETE_NOT_VISUALLY_VERIFIED',words=len(words),mean_word_confidence=sum(conf)/len(conf) if conf else None,low_confidence_words=sum(c<70 for c in conf))
def ocr():
    n=len(fitz.open(SRC)); results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for r in pool.map(ocr_page,range(1,n+1)):
            results.append(r)
            writejson(OUT/'00_SOURCE_AUDIT/extraction_manifest.json',dict(stage='OCR',pages=results,total_pages=n,completed=len(results)))
            if len(results)%10==0:print('OCR',len(results),'/',n,flush=True)
    (OUT/'00_SOURCE_AUDIT/all_pages_ocr.txt').write_text('\n\n'.join(f'=== PDF PAGE {i} ===\n'+(OUT/f'00_SOURCE_AUDIT/ocr/page_{i:03d}.txt').read_text() for i in range(1,n+1)))
if __name__=='__main__':
    import sys
    if 'audit' in sys.argv:audit()
    if 'ocr' in sys.argv:ocr()
