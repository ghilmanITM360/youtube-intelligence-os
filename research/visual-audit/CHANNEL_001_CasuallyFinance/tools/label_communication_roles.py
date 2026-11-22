import csv,os,re,collections,random,json
H=os.path.expanduser('~/YIOS-local-audits/')
VID=['yViMyIVOHkQ','eePIUX0Sd6c','turJ6VMfUjI','CFrVTZBYa3Q']
def role(r):
    L=r['label'].lower();a=r['asset_ids'].upper();ec=r['entering_class'];vt=r['visible_text']
    t=(L+' '+vt.lower())
    chart=re.search(r'GFX_[A-Z0-9_]*(CHART|FRED|STATISTA|GRAPH|LABEL_\d|PRICE)',a) or re.search(r'\b(chart|graph|dashboard|candlestick|bar chart|line chart|plot|table)\b',L)
    al=[x for x in a.split(';') if x and x!='-']
    if al and all(re.match(r'GFX_.*(ARROW|ELLIPSE|CIRCLE|HIGHLIGHT|ANNOT|UNDERLINE|CROSS|TICK)',x) for x in al): return 'ANNOTATION'
    if re.search(r'DOC_|SCREEN_WEB|NEWS_|NEWSPAPER|SNIPPET|IMG_MEME',a) and not re.search(r'GFX_[A-Z0-9_]*(CHART|FRED|STATISTA|GRAPH)',a): return 'EVIDENCE'
    if 'CH_BARS' in a or re.search(r'bar-chart character|chart character',L): return 'METAPHOR_CHARACTER'
    if re.search(r'GOLD_BAR|ICEBERG|TURTLE|BUNKER',a+L.upper()) and not chart: return 'PROP_OBJECT'
    if chart or re.search(r'\b\d+(\.\d+)?\s?(%|percent)|price tag|\$[\d,.]+|\brate\b|\bindex\b',t): return 'DATA_VISUAL'
    if re.search(r'document|article|headline|newspaper|news |photo|logo|wordmark|report|screenshot|tweet|website|meme',L) or re.search(r'DOC_|NEWS|IMG_',a): return 'EVIDENCE'
    if re.search(r'calendar|\b(19|20)\d\d\b|year|month|decade|numerals',L) or 'CALENDAR' in a: return 'TIME_NUMBER'
    if re.search(r'replaces|becomes|text|caption|bubble|speech|says|"|held',L) or (a.startswith('TXT_') and 'CH_' not in a): return 'TEXT_POINT'
    if ec.startswith('POSE') and 'OBJ_' not in a and 'ICON_' not in a or re.search(r'angry|worried|sceptical|skeptical|smiling|panic|shock|sad|laugh|frown|expression',L): return 'REACTION'
    if 'CH_STICKMAN' in a and not re.search(r'OBJ_(?!CHALKBOARD)',a): return 'HOST'
    if re.search(r'CH_(USA|EARTH|CALENDAR|OIL|GOLD|DOLLAR|MONEY)',a): return 'METAPHOR_CHARACTER'
    if a.startswith('CH_'): return 'CAST_SCENE'
    if re.search(r'^(OBJ|BG|ICON)_',a): return 'PROP_OBJECT'
    return 'OTHER'
rows=[]
for v in VID:
    for r in csv.DictReader(open(H+f'2026-11-08-{v}-deep-ct-scan/visual_states.csv')):
        r['role']=role(r);rows.append(r)
print(len(rows),collections.Counter(r['role'] for r in rows))
random.seed(53);S=random.sample(rows,60)
for i,r in enumerate(S):print(i,r['video_id'],r['visual_state_id'],r['role'],'|',r['entering_class'],'|',r['label'][:70],'|',r['visible_text'][:40],'|',r['asset_ids'][:50])
json.dump(rows,open('lab.json','w'))
json.dump([[r['video_id'],r['visual_state_id']] for r in S],open('sample.json','w'))
