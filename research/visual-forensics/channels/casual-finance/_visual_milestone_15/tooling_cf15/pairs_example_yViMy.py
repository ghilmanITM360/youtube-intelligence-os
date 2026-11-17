import json, sys
ws = sys.argv[1]
a = json.load(open(f'{ws}/audio/yViMyIVOHkQ_small_en.json'))
W = [(x['start'], x['end'], x['word'].strip()) for s in a['segments'] for x in s['words']]
norm = lambda w: w.lower().strip('.,?!')
C = [(74,'Unemployment',3.2),(122,'growth',5.6),(184,'GDP',7.8),(339,'recession',14.0),(554,'National',22.8),(855,'started',36.5),(900,'December',37.5),(985,'2008',40.2),(1017,'full',42.6),(1045,'Lehman',43.4),(1096,'world',46.0),(1148,'2001',47.8),(1188,'bubble',49.5),(1226,'March',51.0),(1291,'months',54.0),(1368,'methodology',56.4),(1482,'confirmation',61.2),(1699,'unemployment',71.0),(1831,'number',77.4),(1882,'looking',79.0),(1969,'applied',82.0),(2013,'weeks',84.5),(2071,'pandemic',87.2),(2142,'Americans',89.5),(2180,'stopped',91.0),(2272,'unemployed',95.2),(2396,'labor',99.0),(2492,'pre-pandemic',104.2),(2646,'story',111.0),(2678,'headlines',111.9),(2764,'giving',115.0),(2840,'quality',120.0),(3034,'Full-time',127.0),(3314,'part-time',140.0),(3367,'counts',141.0),(3501,'2025',146.0),(3745,'financially',158.0),(3984,'benefits',165.0),(4066,'security',170.2),(4175,'housing',174.5),(4284,'apartments',179.5),(4347,'inflation',182.0),(4467,'scary',187.5),(4686,'plastic',196.0),(4836,'basics',201.5),(4876,'problem',203.8),(4914,'debt',206.0),(5039,'interest',211.5),(5154,'media',215.0),(5364,'savings',224.0),(5413,'historically',226.0),(5641,'households',236.0),(5846,'movie',244.2),(5869,'2007',245.5),(5908,'cheered',248.0),(5994,'crashing',250.5),(6180,'leading',257.8),(6287,'declined',262.5),(6562,'spreading',274.0),(6619,'bankruptcies',275.9),(7011,'coincidence',291.5),(7065,'wolf',293.5),(7102,'labor',296.5),(7157,'quality',299.0),(7205,'purchasing',300.5),(7279,'savings',304.0),(7394,'constellation',308.8),(7507,'check',313.0),(7531,'engine',314.5),(7553,'oil',315.5),(7581,'brake',316.5),(8032,'1940s',335.0),(8199,'hour',342.5),(8259,'DoorDash',345.5),(8426,'GDP',352.0),(8625,'blind',361.0),(8742,'Law',364.5),(8984,'target',374.5),(9239,'measure',386.5),(9591,'GDP',400.5),(9703,'inflation',405.5),(9786,'cost',409.5),(9911,'effects',413.0),(10193,'hide',425.0),(10346,'NBER',432.0),(10440,'news',436.0),(10509,'confirmation',438.5),(10668,'media',445.0),(10782,'wage',449.5),(10857,'spending',452.5),(10916,'Because',455.0),(10988,'deeper',458.0),(11241,'constellation',469.5),(11431,'preceded',477.0),(11551,'official',482.0),(11681,'subscribe',487.0),(11705,'light',489.8),(11827,'comment',493.5),(12117,'bigger',504.2)]
out = []; amb = []
for f, w, h in C:
    c = [x for x in W if norm(x[2]) == norm(w)]
    c = sorted(c, key=lambda x: abs(x[0] - h))
    if not c or abs(c[0][0] - h) > 2.5: print('DROP', f, w, h, [round(x[0], 1) for x in c[:3]]); continue
    near = [x for x in c if abs(x[0] - h) <= 2.5]
    if len(near) > 1: amb.append((f, w, [round(x[0], 1) for x in near]))
    out.append([f, c[0][2], round(c[0][0], 2)])
json.dump(out, open(f'{ws}/build/phrase_pairs.json', 'w'))
lags = sorted(round(f / 24 - t, 3) for f, w, t in out)
print(len(out), 'pairs; ambiguous', amb)
print('lag min/median/max', lags[0], lags[len(lags) // 2], lags[-1])
