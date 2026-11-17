# lookup.py VIDEO_DIR frame... : print containing state + its art-audit / prompt rows
import csv,sys
d=sys.argv[1];fr=[int(x) for x in sys.argv[2:]]
v1='uPQcyookL0Y' in d
st=list(csv.DictReader(open(d+('/tables/states_v6_draft.csv' if v1 else '/tables/states_v1.csv'))))
sk='state_v4' if v1 else 'state'
art=list(csv.DictReader(open(d+('/tables/o_art_consolidated.csv' if v1 else '/tables/consolidated_art_audit.csv'))))
for f in fr:
    s=next(r for r in st if int(r['start'])<=f<=int(r['end']))
    print(f'f{f} -> {s[sk]} [{s["start"]}-{s["end"]}]')
    for a in art:
        if s[sk] in a.values(): print('   ART:', {k:v[:300] for k,v in a.items() if v and k not in('batch',)})
