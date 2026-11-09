import json, sys
ws = sys.argv[1]; FPS = 24
a = json.load(open(f'{ws}/audio/dPoDyl9Ys38_small_en.json'))
W = [(x['start'], x['end'], x['word'].strip()) for s in a['segments'] for x in s['words']]
norm = lambda w: w.lower().strip('.,?!')
C = [(193,'microstrategy',8.4),(254,'leveraged',10.7),(298,'bitcoin',12.8),(359,'saylor',14.9),(388,'microstrategy',15.7),(465,'bomb',19.8),(995,'stock',41.8),(1022,'down',42.8),(1058,'fast',44.2),(1357,'popular',57.1),(1595,'total',66.7),(1632,'down',67.7),(1729,'victory',72.3),(1764,'bullied',74.0),(1784,'comments',74.7),(2111,'underneath',88.3),(2163,'issues',90.4),(2216,'leads',92.4),(2276,'bitcoin',95.6),(2308,'bitcoin',96.9),(2359,'project',98.7),(2381,'foundation',99.8),(2449,'bottom',102.8),(2745,'future',115.0),(2803,'inflation',117.0),(2822,'corruption',117.8),(3006,'testing',125.6),(3124,'data',130.1),(3190,'pattern',134.0),(3365,'value',141.3),(3526,'satoshi',147.5),(3583,'2008',150.2),(3637,'idea',151.6),(3781,'bitcoin',158.2),(3842,'money',160.6),(3904,'banks',162.9),(3938,'people',164.6),(3998,'intermediaries',167.5),(4030,'if',168.3),(4083,'revolutionary',170.4),(4163,'close',173.7),(4259,'three',177.5),(4347,'medium',181.0),(4512,'store',188.4),(4571,'today',190.3),(4685,'third',193.3),(5058,'slow',211.1),(5132,'processes',214.4),(5333,'visa',222.6),(5389,'65',224.7),(5446,'second',227.1),(5509,'entire',229.6),(5658,'carbon',237.4),(5751,'million',240.5),(5813,'energy',242.4),(6033,'widely',252.3),(6387,'gold',265.6),(6514,'reasons',271.6),(6542,'first',272.2),(6558,'stability',272.9),(6664,'historically',278.1),(6758,'exactly',281.8),(6896,'20',287.2),(7017,'businesses',292.3),(7035,'households',293.0),(7055,'individuals',294.2),(7106,'speculative',296.6),(7190,'second',300.1),(7274,'ownership',302.6),(7481,'roughly',312.0),(7580,'supply',315.5),(7750,'jane',323.8),(7930,'wiping',330.6),(8161,'third',340.4),(8196,'requirement',341.3),(8330,'businesses',347.6),(8364,'accept',348.6),(8460,'everything',352.9),(8653,'passing',361.2),(8778,'three',366.6),(8934,'um',372.6),(9265,'back',386.5),(9308,'salvador',388.3),(9459,'chivo',394.5),(9558,'$30',398.0),(9611,'free',399.9),(10207,'98',425.0),(10735,'chivo',448.1),(10832,'national',451.3),(11162,'reports',465.2),(11688,'left',487.4),(11745,'where',489.3),(11811,'answer',492.5),(11893,'once',495.8),(11973,'memes',499.3),(12125,'greater',505.2),(12663,'stock',528.4),(12686,'goods',529.3),(12868,'belief',536.0),(13089,'cycle',545.8),(13341,'inflation',556.3),(13437,'moment',560.4),(13499,'machine',563.3),(13759,'truth',574.0),(14150,'fools',588.6)]
out = []; amb = []; dropped = []
for f, w, h in C:
    c = sorted([x for x in W if norm(x[2]) == norm(w)], key=lambda x: abs(x[0] - h))
    if not c or abs(c[0][0] - h) > 2.5: dropped.append((f, w, h, 'noword')); continue
    near = [x for x in c if abs(x[0] - h) <= 2.5]
    if len(near) > 1: amb.append((f, w, [round(x[0], 1) for x in near]))
    out.append([f, c[0][2], round(c[0][0], 2)])
keep = [o for o in out if abs(o[0] / FPS - o[2]) <= 1.5]; far = [o for o in out if abs(o[0] / FPS - o[2]) > 1.5]
json.dump(keep, open(f'{ws}/build/phrase_pairs.json', 'w'))
lags = sorted(round(f / FPS - t, 3) for f, w, t in keep)
print('candidates', len(C), 'kept', len(keep), 'dropped-noword', dropped, 'dropped-lag>1.5', [(o[0], o[1], round(o[0] / FPS - o[2], 2)) for o in far])
print('lag min/median/max', lags[0], lags[len(lags) // 2], lags[-1], 'early', sum(l < 0 for l in lags), 'late', sum(l > 0 for l in lags), 'within0.1', sum(abs(l) <= 0.1 for l in lags), 'within0.3', sum(abs(l) <= 0.3 for l in lags))
print('p10', lags[int(.1 * len(lags))], 'p90', lags[int(.9 * len(lags))]); print('ambiguous', len(amb))
