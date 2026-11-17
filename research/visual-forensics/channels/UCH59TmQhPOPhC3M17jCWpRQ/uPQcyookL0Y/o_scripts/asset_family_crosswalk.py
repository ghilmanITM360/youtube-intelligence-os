# Extend asset crosswalk (raw reviewer IDs/descriptions untouched): keyword rules over o_art_consolidated text -> candidate family links.
# ponytail: keyword matching, not visual identity; every link is INFERRED_FROM_AUDIT_TEXT and needs visual confirmation before production use.
import csv,re
F={'reviewer_13:CHAR_TEACHER':r'glasses.{0,40}(teacher|lecturer|professor)|(teacher|lecturer|professor).{0,40}glasses|GLASSES_TEACHER',
 'reviewer_13:SET_CLASSROOM_BG':r'classroom|CLASSROOM','reviewer_13:PROP_CHALKBOARD':r'chalkboard|blackboard|green board|SMART_BOARD|board insert',
 'reviewer_13:PROP_POINTER_STICK':r'pointer','reviewer_14:ASSET_GLOBE':r'\bglobe\b|GLOBE','PRIMARY:PROP_PROJECTOR':r'projector',
 'reviewer_13:TEXT_TITLE_CARD':r'Survival chance|chapter heading|TITLE','PRIMARY:SET_WHITE_CARD':r'white (field|void|canvas|background)|off-white',
 'PRIMARY:CHAR_BEARDED_HAIRY_STICKARM_MAN':r'(beard|bearded).{0,80}(stick|thin black).{0,20}arm|BROWN_BEARD_A|BALD_BEARD_B','PRIMARY:PROP_TOMBSTONE':r'tombstone|R\.I\.P',
 'PRIMARY:ASSET_MAMMOTH':r'mammoth','PRIMARY:ASSET_MAP_EUROPE':r'Europe map|map of Europe|\bmap\b','PRIMARY:FX_FADE_BLACK':r'black (frame|screen|field)|fade to black|pure black'}
rows=list(csv.DictReader(open('tables/o_art_consolidated.csv')));out=[]
for fam,pat in F.items():
    hits=[r for r in rows if re.search(pat,' '.join(str(v) for v in r.values()),re.I)]
    for r in hits:out.append({'family':fam,'state':r['state'],'reviewer':r.get('reviewer','') or 'n_art_consolidated','frames_viewed':r['frames_viewed'][:300],'link_basis':'INFERRED_FROM_AUDIT_TEXT keyword /'+pat+'/','decision':'CANDIDATE_SAME_FAMILY_UNCONFIRMED'})
w=csv.DictWriter(open('tables/o_asset_family_crosswalk_ext.csv','w',newline=''),list(out[0]));w.writeheader();w.writerows(out)
import collections;c=collections.Counter(o['family'] for o in out)
for k,v in c.most_common():print(v,k,sorted({o['state'] for o in out if o['family']==k})[:12])
