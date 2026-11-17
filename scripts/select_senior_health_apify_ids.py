# usage: python3 scripts/select_senior_health_apify_ids.py [max_ids]
# Picks videos still missing a transcript for the 25-channel set, in priority order (CSV order = avg views desc), using the 60-video plan:
# 30 newest + 20 most viewed + 10 least viewed (>=90 days old); channels with <=60 videos take all. Prints JSON {"videoUrls":[...]}.
import csv, datetime, json, sqlite3, sys
R = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
d = sqlite3.connect(f'{R}/data/catalog/senior_health_complete.db'); cap = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
out = []
for r in csv.DictReader(open(f'{R}/research/senior-health-master/REMAINING_CHANNELS_NEW_GOOD_VIEWS.csv')):
    ch = r['url'].rsplit('/', 1)[1]
    vs = d.execute('select video_id, coalesce(published,\'\'), coalesce(views,0), has_transcript from videos where channel_id=?', (ch,)).fetchall()
    vs.sort(key=lambda v: v[1], reverse=True)  # newest first
    if len(vs) <= 60: pick = vs
    else:
        new, rest = vs[:30], vs[30:]
        top = sorted(rest, key=lambda v: -v[2])[:20]; left = [v for v in rest if v not in top]
        cutoff = (datetime.date.today() - datetime.timedelta(days=90)).isoformat()
        low = [v for v in sorted(left, key=lambda v: v[2]) if v[1] and v[1] <= cutoff][:10]
        pick = new + top + low
        for v in vs:
            if len(pick) >= 60: break
            if v not in pick: pick.append(v)
    out += [v[0] for v in pick if not v[3]]
print(json.dumps({'videoUrls': out[:cap]}))
