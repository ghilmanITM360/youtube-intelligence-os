import pickle,re,csv,datetime,json,glob
D='.'
T=datetime.datetime(2026,11,23,20,10,tzinfo=datetime.timezone.utc)
u=pickle.load(open('raw/u.pkl','rb'))
RX={'T1':r'(fall|fell|jump|drop).*(space|every height|edge of space|altitude|terminal|stratos|height)|(space|stratos).*(jump|fall)',
'T2':r'slow(s|ed)? down|decelerat|terminal velocity','T3':r'(tiny|small|little|mini).*(planet|world|asteroid|moon)|jump.*(asteroid|planet|phobos|moon)',
'T4':r'orbit.*(jump|walk|asteroid|tiny|small|run)|jump.*orbit|walk.*orbit','T5':r'voyager','T6':r'moon.*(vanish|disappear|gone|missing)|without the moon|no moon|lost the moon|moon never|vanish.*moon',
'T7':r'tide','T8':r'neutron','T9':r'laser.*moon|retroreflect|lunar (laser|ranging)|moon.*laser|laser.*(echo|reflect)','B1':r'(stop|stood|halt).*(spin|rotat)|spin.*(stop)|rotation.*stop','B2':r'phobos'}
EXACT={'T4':r'jump.*into orbit','T5':r'light.?day','T6':r'moon.*(vanish|disappear|missing)','T8':r'(teaspoon|spoonful).*neutron|neutron.*(teaspoon|spoonful)','B1':r'(1|one|5|five) second','B2':r'phobos'}
TOPICNAME={'T1':'Fall from space (D1 long)','T2':'Slow down before ground (D4 short)','T3':'Jump on tiny planet (D7 short)','T4':'Jump into orbit tiny planet (D10 long)','T5':'Voyager message delay (D13 short)','T6':'Moon vanished (D16 long)','T7':'Tides without Moon (D19 short)','T8':'Neutron-star piece/teaspoon (D22 long, D25 short)','T9':'Laser to Moon and back (D28 short)','B1':'Backup: Earth stops spinning 1 s','B2':'Backup: jump on Phobos'}
ROLE={'Di7mp6KgEDc':'DEMAND SIGNAL + SATURATION: 140-subscriber channel, ~51K views in 8 days on a near-identical premise (1 m to edge of space). Counter-signal to "fall long is unique".',
'XMHPzw7SaLs':'CONTRARY SIGNAL: exact premise exists but only 212 views in ~10 months; lane open but exact-title demand unproven.',
'XVXrDX9zwfM':'SATURATION: 9M-sub What If covered spoonful of neutron star 7 yr ago (2.5M).','jAgBiFWd-yA':'SATURATION: Action Lab neutron drop, 20M.',
'UJwkj82BJjo':'SATURATION: What If, Earth stopped spinning 5 s, 6.7M.','bxTl_cPllZo':'SATURATION: exact "for 1 second" premise, 202K.',
'1EOfJj9ceng':'SATURATION: exact title copy, 416-sub channel, 342 views / 2 wk.','Fp7fT2iabCA':'DEMAND SIGNAL (old): AumSum Moon disappeared 3.6M.',
'6MP920xMC0Q':'DEMAND SIGNAL (old): Insider Tech Moon disappeared 1.7M.','JqFSGkFPipM':'ADJACENT (different question): xkcd official, everyone pointed a laser at the Moon, 6.1M.',
'NiVGpee8M7s':'EVENT SATURATION: Astrum Voyager 1, 2.4M in 5 d.','VRag078yfl0':'EVENT SATURATION: AP, 1.2M.','fakxcJ7Etcc':'CONTRARY SIGNAL for Phobos lane: "Don\'t jump on Phobos" 298K (4 yr) exists.',
'5AnLxpNF1AA':'DEMAND/SATURATION: "What If You Fell From Space?" 18.7K / 26 d.','yYf_xe94aFI':'CLOSE PREMISE: human body falling from every height, 868K / ~1 yr.',
'gp5G1QG6cXc':'xkcd official: What if Earth suddenly stopped spinning? (long) - official channel already made close premise.','x_IgZ3g7uHs':'CLOSE PREMISE short: tides would not fully stop, 42 views.','bMB7blRvtYY':'CLOSE PREMISE: tides drop to one third, 99 views.'}
def cls(t,title):
    if t in EXACT and re.search(EXACT[t],title,re.I): return 'EXACT_PREMISE (title keyword + my title reading)'
    if re.search(RX[t],title,re.I): return 'CLOSE_PREMISE (title keyword + my title reading)'
    return 'BROAD_OR_OFFTOPIC'
rows=[];n=0
def add(**k):
    global n;n+=1;k['evidence_id']='BE-%03d'%n;rows.append(k)
# A) browser channel + trends + watch pages
add(topic_id='ALL',access_method='BROWSER channel Videos tab',observed_utc='2026-11-23T19:55:23Z',source_url='https://www.youtube.com/channel/UC6IxnFzHofFJ5X2PycSMsww/videos',video_id='',publisher="xkcd's What If?",title='(channel page) 1.38M subscribers, 92 videos; latest: What if we tried to eat the sun? 942K / 5 d; nuke in Mariana Trench 2.9M / 3 wk; toaster vs freezer 1.5M / 2 mo',publish_date_or_age='see title',views_at_obs='',premise_class='n/a',inspected='Channel header and first 30 Latest-tab cards (title, views text, age text, duration) via DOM read; no video watched',not_inspected='Thumbnails not visually reviewed; Shorts tab not opened visually (listed with yt-dlp, raw/xkcd_shorts.txt)',role='Baseline: xkcd made Moon-black-hole, Moon-electrons, pool-on-Moon, laser-at-Moon, Earth-stopped-spinning and rotated-90 videos; none is Moon-vanishes, tiny-planet orbit, neutron teaspoon, Voyager, falling-from-space.',window='')
add(topic_id='ALL',access_method='BROWSER channel tabs via yt-dlp flat list',observed_utc=open('raw/xkcd_tabs_observed_utc.txt').read().strip(),source_url='https://www.youtube.com/channel/UC6IxnFzHofFJ5X2PycSMsww/shorts',video_id='',publisher="xkcd's What If?",title='46 long + 46 Shorts listed (raw/xkcd_videos.txt, raw/xkcd_shorts.txt). Earth-stopped-spinning: long gp5G1QG6cXc + Shorts ERieN5pee7A (257K) and 19gun1mffWs (2.2M). Moon-black-hole: long UQgw50GQu1A + Short n2XRulD_IVs (1.0M). Several Shorts per long exist.',publish_date_or_age='',views_at_obs='',premise_class='n/a',inspected='Titles and Short view counts from tab listing (tool, not browser DOM)',not_inspected='Long view counts not returned by flat list',role='xkcd pairs one long with several Shorts (rotation: 4 Shorts; Earth-stopped: 3): supports parent-Short pattern but those Shorts are clips of the parent.',window='')
add(topic_id='ALL',access_method='BROWSER Google Trends (classic Explore)',observed_utc='2026-11-23T20:00:00Z',source_url='https://trends.google.com/trends/explore?date=today%203-m&gprop=youtube&q=voyager%201,neutron%20star,terminal%20velocity,moon%20tides,lunar%20laser&hl=en',video_id='',publisher='Google Trends',title='Worldwide, Past 90 days, All categories, YouTube Search; 5 terms. Period averages (relative index, same chart): voyager 1 = 11, neutron star = 4, terminal velocity = 2, moon tides = 0, lunar laser = 0. voyager 1 daily: ~6-9 in Sep-Oct, 19 (Nov 15), 44 (Nov 17), 100 (Nov 18), 66 (Nov 19), 42 (Nov 20), 30 (Nov 21), 27 (Nov 22).',publish_date_or_age='',views_at_obs='',premise_class='n/a',inspected='Chart data table text read from page',not_inspected='0-100 is relative to the largest term in this chart; small terms show 0-4 only because Voyager dominates. Not search volume. No per-question data. Prior audit has separate single-term pulls (raw/trends_summary.md in earlier audit).',role='Voyager interest is event-driven and decaying within 4 days of the peak; other terms not interpretable in this chart.',window='')
for vid,pub,title,age,views,subs,note in [
('Di7mp6KgEDc','Quiet World','POV: You Fall From Every Height (Real Physics)','8 days ago (2026-11-15)','51K-52K','140 subscribers; 4:19; description: from 1 metre to the edge of space, real atmosphere','watch page opened in pane'),
('XMHPzw7SaLs','Sky Bug','Could you JUMP INTO ORBIT around a small asteroid ?','9 mo ago','212','description: astronaut on small asteroid gets into orbit by jumping','watch page opened in pane'),
('XVXrDX9zwfM','What If','What If a 6 BILLION Ton Spoonful of Neutron Star Appeared on Earth?','7 yr ago','2.5M','9M subscribers; 3:59','watch page opened in pane'),
('1EOfJj9ceng','The Curious Hour','What If the Moon Disappeared Tonight?','2 wk ago','342','416 subscribers; 7:53','watch page opened in pane')]:
    add(topic_id={'Di7mp6KgEDc':'T1','XMHPzw7SaLs':'T4','XVXrDX9zwfM':'T8','1EOfJj9ceng':'T6'}[vid],access_method='BROWSER watch page (opened, not played)',observed_utc='2026-11-23T19:59:00Z',source_url='https://www.youtube.com/watch?v='+vid,video_id=vid,publisher=pub,title=title,publish_date_or_age=age,views_at_obs=views,premise_class='CLOSE_PREMISE' if vid!='XVXrDX9zwfM' else 'CLOSE_PREMISE',inspected='Page opened; title, owner, subscriber text, views/age text and first lines of description read from DOM. Video NOT played or watched; thumbnail not reviewed',not_inspected='Content, accuracy, retention, thumbnail',role=ROLE[vid],window='')
# browser search cards
B={
'T6|what if the moon vanished tonight|19:57:37':"""What If the Moon Disappeared Tonight?|1EOfJj9ceng|The Curious Hour|342 / 2 wk ago
What if the Moon went Missing?|Fp7fT2iabCA|AumSum's Science|3.6m / 4 yr ago
What If the Moon Vanished Tonight?|MXfHZNBCEjs|Orbium|41 / 7 days ago
What If the Moon Disappeared Tonight?|llW-0vrxNvg|What If Unfolded|36 / 2 wk ago
If the Moon Vanished Tonight, the Tides Wouldn't Fully Stop|x_IgZ3g7uHs|HowLumen|42 / 2 wk ago
What If the Moon Vanished Tonight?|DVPVF0F7VVg|Whatif|33 / 13 days ago
What Would Happen If The Moon Disappeared|6MP920xMC0Q|Insider Tech|1.7m / 8 yr ago
What if the Moon disappeared tonight?|zCWrPs2vU80|WhatIf|3 / 7 days ago
What if the Moon Disappeared?|FVrdyIW4C1I|It's AumSum Time|1.1m / 7 yr ago
What If the Moon Vanished Tonight?|nYVqMPKILH8|UNASKED|10 / 4 days ago
What If the Moon Disappeared?|r1uYsSdia3E|The Sky Rewritten|5.2k / 4 wk ago
What If the Moon Vanished Tonight?|PBUrubikV5s|WHAT IF UNIVERSE|1 / 7 days ago""",
'T8|teaspoon of neutron star|19:57:50':"""What If a 6 BILLION Ton Spoonful of Neutron Star Appeared on Earth?|XVXrDX9zwfM|What If|2.5m / 7 yr ago
How Can a Teaspoon of a Neutron Star Weigh a Billion Tons?|-3t0O0u5WT0|Casual Science|341 / 4 mo ago
Warning: DO NOT TRY - Seeing How Close I Can Get To a Drop of Neutrons|jAgBiFWd-yA|The Action Lab|20m / 8 yr ago
How Can a Teaspoon of Neutron Star Matter Weigh a Billion Tonnes?|xlyLVDhh8cA|The Snoozy Scientist and The Sleepy Scientist|26k / 2 mo ago
What If a Teaspoon of Neutron Star Landed on Your Kitchen Table?|zhk0SoQURaM|What If anything|6.2k / 5 mo ago
What if you brought a TEASPOON of NEUTRON STAR to earth?|v_cuVU43eLs|TyroScience|14k / 7 yr ago
Neutron Stars - The Most Extreme Things that are not Black Holes|udFxKZRyQt4|Kurzgesagt|23m / 7 yr ago
What If You Held a Teaspoon of Neutron Star?|WCFE06uIvGo|Newts Theorys|49 / 5 days ago
A Teaspoon of a Neutron Star Is a Planet Killer|-U96b7ZRjIc|The Global Lab|34 / 2 mo ago""",
'T5|voyager 1 one light day message|19:57:56':"""Shine Bright for Voyager's Light-Day: How to Participate in NASA's Global Activation|aCYFpH3wtAU|NASA Jet Propulsion Laboratory|172k / 13 days ago
What Voyager 1 Is Still Telling Us From One Light-Day Away|oihhXuvchvQ|Slow Sky with Dale Brennan|304k / 2 wk ago
WATCH: The moment NASA confirmed Voyager 1 reached one-light day from Earth|0W5Jmd3hAGM|Associated Press|22k / 3 days ago
What Voyager 1 Found Beyond the Edge of Our Solar System|NiVGpee8M7s|Astrum|2.4m / 5 days ago
How is NASA Still in Contact With Voyager 1 One Light Day Away|OVOpU7qx81I|The Secrets of the Universe|135k / 5 days ago
Voyager 1 is Now 1 Light-Day From Home - And It's Terrifying|GLpny4lTmvg|Today in the Space World|627k / 8 days ago
Voyager 1 Is Now ONE LIGHT-DAY Away! What Is It Still Sending Us?|uxaR3RwKGqM|1Dot|5k / 5 days ago""",
'T4|could you jump into orbit on a tiny planet|19:58:01':"""What If The Earth Shrank and Couldn't Stop?|h5vpQSMAV_k|Beyond If|52k / 2 wk ago
Could you JUMP INTO ORBIT around a small asteroid ?|XMHPzw7SaLs|Sky Bug|212 / 9 mo ago
How High Could You Jump on EVERY World? 20 Worlds|G_OhcWEcLks|Orbitimbre|5.8k / 4 days ago
How High You Could Jump on Different Planets in 3D|D8H1RNtka6s|BRIGHT SIDE|25m / 6 yr ago
Could You Live on a Tiny Planet Like the Little Prince?|c5IgvJ3rgY4|IQ Tuber|15 / 1 mo ago
How High Can You Jump? From a Tiny Asteroid to a Neutron Star|MDrTY4ttQkI|Pop Orbit|21 / 5 days ago
We Shrank Earth Until You Could Jump Off|L8CECfPhtu4|Toggle Lab|90 / 4 days ago""",
'T1|would falling from space make you hit the ground faster|19:58:13':"""How Can Something Fall Faster Than Gravity?|dosAbCCKXLs|The Action Lab|694k / 9 mo ago
POV: You Fall From Every Height (Real Physics)|Di7mp6KgEDc|Quiet World|52k / 8 days ago
Misconceptions About Falling Objects|_mCC-68LyZM|Veritasium|2.2m / 15 yr ago
What If You Kept Falling and Couldn't Stop?|IdMCrP0Tbxc|WhyVerse|142 / 3 wk ago
I Jumped From Space (World Record Supersonic Freefall)|Hz2F_S3Tl0Y|Red Bull|89m / 4 yr ago
What If You Fell From the International Space Station?|30j6WfQMlCw|What If|238k / 5 yr ago""",
'T9|how long does a laser take to reach the moon and back|19:58:18':"""Mythbusters Moon Hoax Retroreflectors|VmVxSFnjYCA|LunarTuner|806k / 18 yr ago
NASA launches lasers at the moon|-k5QNCsYU9M|KTNV Channel 13 Las Vegas|169k / 6 yr ago
Shining The World's Most Powerful Laser At The Moon!|9srfJNPzK_Q|The Action Lab|2.1m / 6 yr ago
The Moon Has Been Answering Our Lasers Since 1969|-gvx0l2ugFw|Cosmic Hours|48 / 9 days ago
We Time a Laser Echo From the Moon to a Millimeter|-80XMlElXWE|Sure So Far|7 / 2 wk ago""",
'T7|would we still have tides without the moon|19:58:23':"""What Would Happen If The Moon Disappeared|6MP920xMC0Q|Insider Tech|1.7m / 8 yr ago
What If We Lost The Moon?|EFmPZv7LIdo|What If|1.2m / 8 yr ago
What If Earth Had No Moon? 6-Hour Days, Mega Tides, and Theia's Impact|32HSFEX5Obs|Learn Physics|291 / 3 days ago
One Night Without the Moon: The Real Changes, Hour by Hour|UybUcqja2dw|Visualized in 3D|208 / 5 days ago
If Earth Had No Moon: 6-Hour Days, 10,000-Foot Tides, and Chaos|kkmFGF6elLQ|Pure Physics|534 / 1 mo ago
Earth's Tides Collapse Without the Moon|Cf3rWnXSWLU|if|10 / 10 mo ago""",
'B2|what if you jumped on phobos|19:58:28':"""Do NOT jump on Mars' moon Phobos (OLD)|_t_csXuUi-Y|IanRuizsSongs|358 / 10 mo ago
Don't jump on Phobos|fakxcJ7Etcc|Philip Unekwu|298k / 4 yr ago
What Happens If You Jump on Phobos The Martian Moon?|UTi7Jd_218A|Andy the Martian|232 / 3 wk ago
How High Could You Jump on EVERY World? 20 Worlds|G_OhcWEcLks|Orbitimbre|5.8k / 4 days ago""",
'B1|what if earth stopped spinning for one second|19:58:42':"""What If the Earth Stopped Spinning for 5 Seconds and Winds Hit 1,670 km/h?|UJwkj82BJjo|What If|6.7m / 4 yr ago
Timeline: What If Earth Stopped Rotating For 1 Second|bxTl_cPllZo|vidData Comparisons|202k / 4 yr ago
What If Earth Stopped Spinning for Just 1 Second?|121DNeINE3k|UniverseEquation|776 / 1 mo ago
What if Earth Stopped Spinning for just 1 Second|m7wr_X_LHBs|Kaushik Bhattacharjee|47k / 7 mo ago
What If Earth Stopped Spinning for Just 1 Second?|MUUCFEidOSU|Hichverse|140 / 1 mo ago""",
'T2|why do you slow down before hitting the ground skydiving from space|19:58:47':"""I Jumped From Space (World Record Supersonic Freefall)|Hz2F_S3Tl0Y|Red Bull|89m / 4 yr ago
POV: You Fall From Every Height (Real Physics)|Di7mp6KgEDc|Quiet World|52k / 8 days ago
Jump From Space: What Happens If You Do A Space Jump?|XYXCJ-VD3l8|Science ABC|68k / 7 yr ago""",
'T7|farthest from any other human Al Worden 3596 km (WIB-52 check)|20:05:49':"""Al Worden the Most Isolated Man in History Claimed He Wasn't Lonely|14qTE3bNdwM|The Vitus Logs|1.6k / 2 mo ago
NASA Remembers Apollo Astronaut Al Worden|8UhnO53XoHM|NASA|75k / 6 yr ago
How Far Can a Human Actually Go Before Space Kills You?|TS5nGHw9VzM|Astrowise|4k / 1 mo ago""",
}
for key,block in B.items():
    t,q,hm=key.split('|')
    for line in block.split('\n'):
        title,vid,ch,vv=line.split('|')
        tt='WIB52' if 'WIB-52' in q else t
        add(topic_id=tt,access_method='BROWSER YouTube search results card (query: %s)'%q,observed_utc='2026-11-23T%s:00Z'%hm,source_url='https://www.youtube.com/watch?v='+vid,video_id=vid,publisher=ch,title=title,publish_date_or_age=vv.split(' / ')[1],views_at_obs=vv.split(' / ')[0],premise_class=cls(t,title) if tt!='WIB52' else 'ADJACENT (WIB-52 lane)',inspected='Search-result card only (title, channel, views text, age text); not opened, not watched',not_inspected='Everything else',role=ROLE.get(vid,''),window='')
browser_ids={r['video_id'] for r in rows if r['video_id']}
# B) script watch-page rows: all keyword-near + top-3 views per topic
by={}
for e in u.values(): by.setdefault(e['topic'],[]).append(e)
for t,L in sorted(by.items()):
    pick={e['id'] for e in L if re.search(RX[t],e['title'],re.I)}|{e['id'] for e in sorted(L,key=lambda e:-e['views'])[:3]}
    for e in sorted([e for e in L if e['id'] in pick],key=lambda e:-e['views']):
        age=(T-e['pub']).total_seconds()
        fl=','.join(f for f,s in (('90d',90*86400),('30d',30*86400),('7d',7*86400),('24h',86400),('4h',4*3600)) if age<=s) or '>90d'
        add(topic_id=t,access_method='SCRIPT: yt-dlp search (filters none/month/week/today/hour) + watch-page microformat',observed_utc='2026-11-23T19:55-20:10Z (search/fetch window)',source_url='https://www.youtube.com/watch?v='+e['id'],video_id=e['id'],publisher=e['ch'],title=e['title'],publish_date_or_age=e['pub'].isoformat(),views_at_obs=str(e['views']),premise_class=cls(t,e['title']),inspected='Watch-page metadata (publishDate with offset, viewCount, length %ds) read by script; title keyword classification; not opened in browser unless listed above, not watched'%e['len'],not_inspected='Content, thumbnail, quality',role=ROLE.get(e['id'],''),window=fl+' (age %.1f d)'%(age/86400))
cols=['evidence_id','topic_id','access_method','observed_utc','source_url','video_id','publisher','title','publish_date_or_age','views_at_obs','premise_class','window','inspected','not_inspected','role']
with open('BROWSER_COMPETITOR_EVIDENCE.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(rows)
print(len(rows),'evidence rows')
# window summary
out=[]
for t in sorted(by):
    L=by[t];near=[e for e in L if re.search(RX[t],e['title'],re.I)]
    def n_(S,d): return sum(1 for e in S if (T-e['pub']).total_seconds()<=d)
    out.append(dict(topic_id=t,topic=TOPICNAME[t],unique_hits_all=len(L),all_90d=n_(L,90*86400),all_30d=n_(L,30*86400),all_7d=n_(L,7*86400),all_24h=n_(L,86400),all_4h=n_(L,4*3600),
     near_premise_keyword=len(near),near_90d=n_(near,90*86400),near_30d=n_(near,30*86400),near_7d=n_(near,7*86400),near_24h=n_(near,86400),near_4h=n_(near,4*3600),
     near_with_100k_views=sum(1 for e in near if e['views']>=100000),near_under_1k_views=sum(1 for e in near if e['views']<1000),
     max_views_near=max([e['views'] for e in near] or [0]),note='Search-hit sample (top 3-6 per query x filter x query), not a census; unpersonalised US-server yt-dlp search; keyword rule; the 4h/24h window hits are mostly recency-filter filler, so counts there are not demand.'))
with open('SEARCH_WINDOW_SUMMARY.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys()));w.writeheader();w.writerows(out)
for o in out: print(o['topic_id'],o['unique_hits_all'],'near',o['near_premise_keyword'],'30d',o['near_30d'],'7d',o['near_7d'],'24h',o['near_24h'],'4h',o['near_4h'],'>=100k',o['near_with_100k_views'],'<1k',o['near_under_1k_views'])
