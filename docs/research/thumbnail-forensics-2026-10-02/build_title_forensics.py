"""Programmatic title forensics for every canonical video (exact Video_ID join; no fuzzy matching).

Everything here is PROGRAMMATIC_RULE_BASED: regex features, rule-based archetypes and heuristic 0-10 proxies.
Proxy scores are NOT analyst judgement, NOT CTR/view predictions. Analyst interpretation is a separate stage
(title-analyst-audit-*.json -> ANALYST_TITLE_DIAGNOSTIC_SCORE) and is never written by this script.
Outputs: title-forensics.csv / title-forensics.json (one row per canonical video).
"""
import csv, json, re, sqlite3
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = sqlite3.connect(ROOT / 'data/catalog/youtube_channel_registry.db')


def rx(p): return re.compile(p, re.I)


NUM = rx(r'\d')
AGE_NUM = rx(r'\b(?:after|over|above|past|at|age[ds]?|from|before|under|turn(?:ing)?|in your|starting at|by)\s+(?:the age of\s+)?(\d{2})\b|\b(\d{2})\s*\+|\b(\d{2})s\b|\b(?:in|at)\s+(?:my|your|their)\s+(\d{2})s\b')
SENIOR_AGE = rx(r'\b(?:after|over|above|past|at|age[ds]?|before|turn(?:ing)?|in your|by)\s+(?:the age of\s+)?(?:5[5-9]|[6-9]\d)\b|\b(?:5[5-9]|[6-9]\d)\s*\+|\b(?:over|after) (?:50|fifty)\b')
LIST_FORM = rx(r'^\s*(?:top\s+)?\d{1,3}\s+(?!years?\b|months?\b|days?\b|hours?\b|minutes?\b|%|percent\b)[\w\'’-]+|\b(?:top|best)\s+\d+\b|\b\d+\s+(?:things|signs|foods|ways|habits|reasons|mistakes|tips|symptoms|warning|secrets|rules|steps|exercises|vitamins|drinks|supplements|myths|facts|lessons|stocks|etfs|investments|dividend|types)\b')
SIGNS = rx(r'\b\d*\s*(?:warning\s+)?signs?\b|\bsymptoms?\b|\bearly warning\b')
QUESTION = rx(r'\?|^\s*(?:how|why|what|when|where|who|which|can|could|should|would|will|do|does|did|is|are|was|were|have|has)\b')
STRICT_Q = rx(r'\?')
POS = rx(r'\b(?:best|boost|improve|better|healthy|healthier|strong(?:er)?|easy|simple|great|secret|benefit|rich|wealth|win|free|safe|good|longer|restore|regain|reverse|heal|cure|protect|thrive|happy|freedom)\b')
NEG = rx(r'\b(?:worst|bad|never|stop|avoid|don\'?t|do not|dont|mistakes?|wrong|danger(?:ous)?|deadly|killing|kill|toxic|ruin|destroy|dying|death|die|fail|lose|losing|poor|broke|warning|risk|harm|scam|trap|myth|lie|nobody|no one|hidden|silent|ignore|regret|damage|unsafe|painful|disaster|terrible|horrible)\b')
WARNING = rx(r'\b(?:warning|warns?|warned|danger(?:ous)?|deadly|never|stop|avoid|don\'?t|do not|dont|before it\'?s too late|too late|red flags?|ignore|careful|beware|risk(?:s|y)?|silent killer|emergency|urgent|alert|harmful|toxic)\b')
CURIOSITY = rx(r'\b(?:nobody|no one|what happens|here\'?s why|the reason|the truth|why\b|secret|hidden|surprising|shocking|unexpected|really|actually|you won\'?t believe|most people|doesn\'?t want|they don\'?t|what (?:they|doctors|most)|didn\'?t (?:know|tell)|never told|reveal|exposed?|mystery|strange|weird|the real)\b|\?')
AUTHORITY = rx(r'\b(?:doctors?|dr\.?|cardiologists?|neurologists?|physicians?|nephrologists?|endocrinologists?|geriatricians?|nurses?|surgeons?|pharmacists?|experts?|specialists?|researchers?|harvard|mayo clinic|stanford|study|studies|research|science|scientists?|clinical|trial|professor|economists?|millionaires?|billionaires?|advisors?|ceo)\b')
DOCTOR = rx(r'\b(?:doctors?|dr\.?|physicians?|surgeons?|nurses?|geriatricians?|pharmacists?|nephrologists?|endocrinologists?|neurologists?)\b')
CARDIO = rx(r'\bcardiologists?\b|\bheart (?:doctor|surgeon|specialist)s?\b')
EXPERT = rx(r'\b(?:experts?|specialists?|advisors?|professors?|economists?|researchers?|scientists?|historians?|nutritionists?|dietitians?|therapists?)\b')
STUDY = rx(r'\b(?:study|studies|research|trial|clinical|harvard|stanford|mayo clinic|journal|data shows|paper)\b')
SCIENCE = rx(r'\b(?:science|scientists?|scientific|biolog\w+|physics|chemistry|evidence)\b')
FEAR = rx(r'\b(?:deadly|killing|kills?|die|dying|death|dead|fatal|stroke|heart attack|cancer|dementia|alzheimer\'?s|silent killer|terrifying|horrifying|scary|nightmare|collapse|crash|bankrupt|broke|disaster|catastrophe|danger(?:ous)?|too late|warning|toxic|painful|suffer\w*|ruin\w*|destroy\w*|doom\w*)\b')
HOPE = rx(r'\b(?:reverse|restore|heal|cure|recover\w*|regain|improve|boost|better|strong(?:er)?|younger|longer|thrive|prevent|protect|lower|fix|repair|rebuild|rich|wealth|freedom|retire(?:d|ment)? (?:early|comfortably)|financial(?:ly)? free|stay independent|naturally|best way|simple way|easy)\b')
URGENCY = rx(r'\b(?:now|today|immediately|right now|before it\'?s too late|too late|urgent|asap|quick(?:ly)?|fast|stop|this year|before|last chance|don\'?t wait|emergency|2026|2025)\b')
SPECIFIC = rx(r'\$\s?\d|\b\d[\d,\.]*\s*(?:%|percent|years?|months?|days?|hours?|minutes?|mg|g|grams?|k|m|million|billion|x)\b|\b\d{2,}\b|\b(?:vitamin\s+\w+|metformin|statins?|aspirin|magnesium|potassium|omega-?3|apoe|lp\(a\)|a1c|egfr|blood pressure|cholesterol|creatine|protein|beta blockers?|calcium channel)\b')
CONTRARIAN = rx(r'\b(?:myths?|wrong|lie|lies|actually|not what you think|isn\'?t|aren\'?t|stop|truth|overrated|misunderstood|backwards|surprising|unpopular|really|everything you know|they (?:don\'?t|won\'?t)|nobody (?:tells|talks|shows)|what (?:they|doctors|most|nobody) )\b')
MISTAKE = rx(r'\b(?:mistakes?|regret\w*|wrong|errors?|oops|blunders?|costly|stop (?:doing|making|eating|taking|using)|don\'?t (?:do|make|eat|take|buy)|never (?:do|eat|take|buy|use))\b')
SECRET = rx(r'\b(?:secrets?|hidden|nobody (?:tells|talks|shows|knows)|no one (?:tells|talks|knows)|what (?:they|doctors) (?:don\'?t|won\'?t)|truth about|they don\'?t want|insider|unknown|rarely|forgotten|overlooked|nobody is talking)\b')
COMPARE = rx(r'\bvs\.?\b|\bversus\b|\bor\b.*\?|\bcompared?\b|\bbetter than\b|\bdifference between\b|\binstead of\b|\bbefore (?:and|&) after\b|\bthen vs\b')
TRANSFORM = rx(r'\b(?:before (?:and|&) after|transform\w*|turned|became|from .{1,30} to\b|how i (?:went|turned|got|lost|made|paid|saved|built|retired)|reverse[ds]?|changed my|\d+ (?:days|weeks|months|years) later|what happens when|after (?:\d+|a|one|two|three|30|60|90) (?:days|weeks|months|years))\b')
PROBSOL = rx(r'\b(?:how to|how do|how can|ways to|fix|solve|solution|cure|remedy|relief|treat\w*|stop\w*|prevent\w*|lower|reduce|get rid|improve|avoid|best way|do this|try this|eat this|drink this|take this|before bed)\b')
HOWTO = rx(r'^\s*how\s+(?:to|do|can|i|you|we)\b|\bhow to\b')
STOPDO = rx(r'\bstop\s+(?:doing|making|eating|taking|using|drinking|buying|wasting|worrying|ignoring|saying|doing)\b|\bstop\b|\bquit\b')
AFTER60 = rx(r'\b(?:after|over|above|past|beyond|at|aged?|in your)\s+(?:the age of\s+)?(?:5[5-9]|[6-9]\d)\b|\b(?:5[5-9]|[6-9]\d)\s*\+|\b(?:over|after)\s+(?:fifty|sixty|seventy|eighty)\b|\b(?:60|65|70|75|80)s\b')
DOCWARN = rx(r'\b(?:doctors?|dr\.?|cardiologists?|physicians?|nurses?|surgeons?)\b.{0,25}\b(?:warns?|warned|says?|reveals?|explains?|urges?|begs?|tells?|recommends?|stops?|admits?)\b|\b(?:warns?|warned)\b')
DOTHIS = rx(r'\b(?:do this|try this|eat this|drink this|take this|add this|use this|start (?:doing|eating|taking)|every (?:day|morning|night)|daily|before bed|first thing in the morning|once you have|if you (?:want|have|are))\b')
MYTH = rx(r'\bmyths?\b|\bwhat you (?:think|know|believe)\b|\beveryone (?:gets|believes)\b|\bwrong about\b|\bnot true\b|\bbusted\b|\bfact or\b|\blies\b')
POV = rx(r'\bpov\b|^\s*you(?:\'re| are| wake| find| were)\b|\byou(?:\'re| are) (?:an?|the|in)\b|\bday in the life\b|\bif you (?:were|lived)\b|\bwhat if you\b|\bimagine\b')
CASE = rx(r'\b(?:how i|my story|i (?:paid|retired|saved|built|made|lost|tried|quit|bought|invested|survived|lived)|we (?:paid|retired|saved)|retired at|net worth|\$\d[\d,\.]*[km]?(?: in| a| per| by| at)?|a (?:retiree|retired|man|woman|patient|doctor|couple)|real (?:story|example))\b')
FOODS = rx(r'\b(?:foods?|eat(?:ing)?|drinks?|drinking|snacks?|breakfast|dinner|lunch|meals?|diet|fruits?|vegetables?|nuts?|oils?|eggs?|bread|rice|coffee|tea|milk|cheese|fish|meat|sugar|salt|supplements?|vitamins?|juice|water|banana|oats?|beans?|yogurt)\b')
AVOID = rx(r'\b(?:avoid|never|don\'?t|do not|stop|worst|bad for|harmful|toxic|danger(?:ous)?|quit|skip|limit|cut out|ban)\b')
EXPL = rx(r'^\s*(?:why|how|what)\b|\bexplained?\b|\bexplains?\b|\bthe (?:economics|science|history|physics|math|truth|reason) (?:of|behind)\b')
SYMPTOM = rx(r'\bsymptoms?\b|\bsigns?\b|\bfeel(?:s|ing)?\b|\bpain\b|\bnumb(?:ness)?\b|\bswollen\b|\bswelling\b|\bdizz(?:y|iness)\b|\bfatigue\b|\bchest\b|\bshortness\b|\bcramps?\b|\bbruis\w*\b|\bitch\w*\b|\bnight sweats?\b|\bblurred\b|\bconfusion\b|\bdoes your\b|\bwhen your\b')
HEALTH = rx(r'\b(?:health\w*|heart|brain|blood|pressure|sugar|diabetes|diabetic|cholesterol|stroke|cancer|dementia|alzheimer\'?s|memory|bones?|joints?|arthritis|kidneys?|liver|lungs?|gut|muscle|sarcopenia|vitamins?|supplements?|medication|medicines?|statins?|metformin|doctors?|symptoms?|pain|sleep|inflammation|aging|longevity|seniors?|elderly|retirees|fall(?:s)?|balance|walking|exercise|eyes?|vision|hearing|skin|neuropathy|dizz\w+|fatigue|hormones?|thyroid|prostate|bladder|colon|a1c|egfr|apoe|lp\(a\))\b')
CLAIM = [('INSTANT_CURE', rx(r'\b(?:cures?|cured|instant(?:ly)?|overnight|in \d+ (?:days|minutes|hours|seconds)|miracle|works right after|within (?:minutes|days|hours))\b')),
         ('REVERSAL', rx(r'\b(?:revers\w+|undo|heal\w*|restor\w+|regrow|repair\w*|rebuild\w*|get rid|clear\w* (?:your )?arter\w*|unclog\w*|clean\w* (?:your )?(?:arteries|vessels))\b')),
         ('PREVENTION', rx(r'\b(?:prevent\w*|protect\w*|lower\w*|reduce\w*|avoid\w*|stop\w* (?:a )?(?:stroke|heart attack|falls?|dementia))\b')),
         ('SYMPTOM_DIAGNOSIS', rx(r'\b(?:signs?|symptoms?|warning signs?|early signs?|means? you have|do you have|could be|looks like|day before)\b')),
         ('MEDICATION', rx(r'\b(?:statins?|metformin|medications?|medicines?|drugs?|pills?|beta blockers?|aspirin|blood thinners?|ozempic|insulin|supplements?|vitamins?|antibiotics?|calcium channel|ace inhibitors?|prescri\w+)\b')),
         ('FOOD_CLAIM', rx(r'\b(?:foods?|eat(?:ing)?|drinks?|breakfast|diet|fruits?|vegetables?|oils?|eggs?|coffee|tea|juice|nuts?|oats?)\b')),
         ('EXERCISE_CLAIM', rx(r'\b(?:exercises?|walk(?:ing)?|workouts?|stretch\w*|yoga|squats?|strength|balance|training|steps)\b')),
         ('RISK_FEAR', rx(r'\b(?:deadly|killing|silent killer|stroke|heart attack|cancer|dementia|too late|danger(?:ous)?|death)\b'))]
STOP = set('the a an and or of to in on for with at by from is are was were be it its this that these those your you my we our they their i me as but not no do does did how what why when who which can will would should could have has had if than then so just more most very into out up down over about all any each every one two three four five six seven eight nine ten get got make makes made go goes going'.split())


def archetypes(t, fmt_health):
    a = []
    def add(k, c):
        if c and k not in a: a.append(k)
    add('MYTH', MYTH.search(t))
    add('MISTAKE', MISTAKE.search(t))
    add('STOP_DOING', STOPDO.search(t))
    add('DOCTOR_WARNS', DOCWARN.search(t) and DOCTOR.search(t))
    add('WARNING', WARNING.search(t))
    add('SIGNS', SIGNS.search(t))
    add('SYMPTOM', SYMPTOM.search(t) and fmt_health)
    add('AFTER_60', AFTER60.search(t))
    add('AVOID', AVOID.search(t) and FOODS.search(t))
    add('FOODS', FOODS.search(t) and fmt_health)
    add('SECRET', SECRET.search(t))
    add('COMPARISON', COMPARE.search(t))
    add('POV', POV.search(t))
    add('CASE_STUDY', CASE.search(t))
    add('DO_THIS', DOTHIS.search(t))
    add('HOW_TO', HOWTO.search(t))
    add('LIST', LIST_FORM.search(t))
    add('QUESTION', STRICT_Q.search(t) or QUESTION.search(t))
    add('EXPLANATION', EXPL.search(t))
    primary = a[0] if a else 'OTHER'
    return primary, a


def person_address(t):
    f = []
    if re.search(r'\byou(?:rs|r|\'re|\'ll|\'ve|\'d)?\b|\byourself\b', t, re.I): f.append('YOU' if re.search(r'\byou(?!r)', t, re.I) else 'YOUR')
    if re.search(r'\byour\b', t, re.I) and 'YOUR' not in f: f.append('YOUR')
    if re.search(r'\b(?:seniors?|elderly|retirees?|retired|over (?:50|60|65|70)|older adults?|aging|grandparents?|boomers?)\b', t, re.I): f.append('SENIORS')
    if re.search(r'\b(?:men|man|guys?|husbands?|fathers?)\b', t, re.I): f.append('MEN')
    if re.search(r'\b(?:women|woman|ladies|wives|mothers?)\b', t, re.I): f.append('WOMEN')
    if re.search(r'\bpatients?\b', t, re.I): f.append('PATIENTS')
    return f or ['OTHER']


def authority(t):
    if CARDIO.search(t): return 'CARDIOLOGIST'
    if DOCTOR.search(t): return 'DOCTOR'
    if STUDY.search(t): return 'STUDY'
    if SCIENCE.search(t): return 'SCIENCE'
    if EXPERT.search(t): return 'EXPERT'
    return 'NONE'


def claim_types(t, health):
    if not health: return []
    return [k for k, r in CLAIM if r.search(t)]


def keywords(t):
    w = [x.lower() for x in re.findall(r"[A-Za-z][A-Za-z'’-]+", t)]
    return [x for x in w if x not in STOP and len(x) > 2][:8]


def clamp(x, lo=0, hi=10): return max(lo, min(hi, round(x, 1)))


def proxies(t, f):
    n = f['Word_Count']; ch = f['Character_Count']
    spec = 3 + 2 * f['Number_Present'] + 2 * bool(SPECIFIC.search(t)) + (1 if f['Age_Number_Present'] else 0) + (1 if f['Topic_Keywords'] else 0)
    clarity = 6 + (1 if 5 <= n <= 12 else -1 if n > 16 else 0) + (1 if f['Specificity_Frame'] else 0) - (1 if re.search(r'\b(?:this|these|it|that)\b', t, re.I) and n < 6 else 0) - (1 if ch > 85 else 0)
    cur = 2 + 2 * bool(f['Curiosity_Frame']) + 2 * bool(f['Secret_Frame']) + (1 if f['Question_Form'] else 0) + (1 if f['Contrarian_Frame'] else 0) + (1 if f['Warning_Frame'] else 0)
    cred = 5 + (1 if f['Authority_Cue'] != 'NONE' else 0) + (1 if f['Specificity_Frame'] else 0) - (2 if re.search(r'\b(?:miracle|instant|overnight|guaranteed|cure[sd]?|destroy\w*|never (?:get|have)|forever|100%)\b', t, re.I) else 0) - (1 if re.search(r'[A-Z]{4,}.*[A-Z]{4,}', t) else 0)
    prom = 3 + 2 * bool(f['Problem_Solution_Frame']) + 2 * bool(f['Hope_Frame']) + 1 * bool(f['Transformation_Frame']) + (1 if f['Specificity_Frame'] else 0) + (1 if f['Fear_Frame'] else 0)
    over = 1 + 2 * bool(re.search(r'\b(?:cure[sd]?|miracle|instant(?:ly)?|overnight|guaranteed|destroy\w*|reverse[sd]?|clear\w* (?:your )?arter\w*|forever|never (?:get|have)|100%|works right after)\b', t, re.I)) + (1 if f['Fear_Frame'] and f['Urgency_Frame'] else 0) + (1 if re.search(r'\b(?:stroke|heart attack|cancer|dementia)\b', t, re.I) and f['Warning_Frame'] else 0) + (1 if re.search(r'\b(?:everyone|nobody|always|never|all)\b', t, re.I) else 0)
    search = 3 + 2 * bool(f['Topic_Keywords']) + (2 if HOWTO.search(t) else 0) + (1 if f['Specificity_Frame'] else 0) + (1 if 4 <= n <= 11 else 0) - (1 if f['Curiosity_Frame'] and not f['Specificity_Frame'] else 0) - (1 if re.search(r'\b(?:pov|nobody|this)\b', t, re.I) else 0)
    browse = 2 + 2 * bool(f['Curiosity_Frame']) + (1 if f['Fear_Frame'] else 0) + (1 if f['Secret_Frame'] else 0) + (1 if f['Warning_Frame'] else 0) + (1 if f['Contrarian_Frame'] else 0) + (1 if f['Question_Form'] else 0) + (1 if f['Hope_Frame'] else 0)
    novelty = 4 + (1 if f['Secret_Frame'] else 0) + (1 if f['Contrarian_Frame'] else 0) + (1 if re.search(r'\b(?:nobody|weird|strange|bizarre|unexpected|surprising)\b', t, re.I) else 0) - (1 if f['Title_Archetype'] in ('LIST', 'HOW_TO') else 0)
    return dict(Clarity_Proxy=clamp(clarity), Specificity_Proxy=clamp(spec), Novelty_Proxy=clamp(novelty), Curiosity_Proxy=clamp(cur), Credibility_Proxy=clamp(cred),
                Promise_Strength_Proxy=clamp(prom), Overpromise_Risk_Proxy=clamp(over), Searchable_Title_Score_Proxy=clamp(search), Browse_Curiosity_Score_Proxy=clamp(browse))


def build():
    chan = {c: (n, h) for c, n, h in REG.execute('select canonical_channel_id,channel_name,current_handle from channels')}
    vm = {r['Video_ID']: r for r in csv.DictReader((HERE / 'video-metrics.csv').open())}
    niche = {}
    for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()):
        if r['Channel_ID'] and r['Niche_Label']: niche.setdefault(r['Channel_ID'], Counter())[r['Niche_Label'].split(' (')[0]] += 1
    niche = {c: k.most_common(1)[0][0] for c, k in niche.items()}
    rows = []
    for vid, ch, title, pub, dur, vt in REG.execute('select youtube_video_id,canonical_channel_id,title,published_at,duration_seconds,video_type from videos order by canonical_channel_id, published_at, youtube_video_id'):
        t = (title or '').strip()
        fmt_raw = (vm.get(vid) or {}).get('Format', '')
        fmt = 'SHORT' if (vt or '').lower() in ('short', 'shorts') or fmt_raw == 'SHORTS' else 'LONG_FORM' if (fmt_raw.startswith('LONG') or vt) else 'UNKNOWN'
        nic = niche.get(ch, 'UNKNOWN')
        health = nic in ('SENIOR_HEALTH', 'FITNESS_HEALTH') or bool(HEALTH.search(t))
        words = re.findall(r"[A-Za-z0-9$%'’+.,-]*[A-Za-z0-9$%]", t)
        f = dict(Video_ID=vid, Channel_ID=ch, Channel_Name=chan[ch][0], Niche=nic, Format=fmt, Published_At=pub or '', Exact_Title=t,
                 Character_Count=len(t), Word_Count=len(re.findall(r"\S+", t)), Number_Present=int(bool(NUM.search(t))), Age_Number_Present=int(bool(SENIOR_AGE.search(t))),
                 Question_Form=int(bool(STRICT_Q.search(t) or re.match(r'\s*(?:how|why|what|when|where|who|which|can|could|should|would|will|do|does|did|is|are|was|were|have|has)\b', t, re.I))),
                 List_Form=int(bool(LIST_FORM.search(t))), All_Caps_Words=len([w for w in re.findall(r'\b[A-Z]{3,}\b', t)]), Emoji_Or_Symbol=int(bool(re.search(r'[^\w\s\.,!?\'"’“”:;()\-–—$%&|/+#@*\[\]]', t))),
                 Positive_Frame=int(bool(POS.search(t))), Negative_Frame=int(bool(NEG.search(t))), Warning_Frame=int(bool(WARNING.search(t))), Curiosity_Frame=int(bool(CURIOSITY.search(t))),
                 Authority_Frame=int(bool(AUTHORITY.search(t))), Fear_Frame=int(bool(FEAR.search(t))), Hope_Frame=int(bool(HOPE.search(t))), Urgency_Frame=int(bool(URGENCY.search(t))),
                 Specificity_Frame=int(bool(SPECIFIC.search(t))), Contrarian_Frame=int(bool(CONTRARIAN.search(t))), Mistake_Frame=int(bool(MISTAKE.search(t))), Secret_Frame=int(bool(SECRET.search(t))),
                 Comparison_Frame=int(bool(COMPARE.search(t))), Transformation_Frame=int(bool(TRANSFORM.search(t))), Problem_Solution_Frame=int(bool(PROBSOL.search(t))),
                 Person_Address='|'.join(person_address(t)), Authority_Cue=authority(t), Health_Topic=int(bool(health and HEALTH.search(t))),
                 Health_Claim_Type='|'.join(claim_types(t, health and bool(HEALTH.search(t)))), Topic_Keywords='|'.join(keywords(t)))
        f['Title_Archetype'], allarch = archetypes(t, bool(f['Health_Topic']))
        f['Title_Archetypes_All'] = '|'.join(allarch)
        f.update(proxies(t, f))
        f['Title_Observation'] = 'CURRENT_REGISTRY_TITLE'
        f['Title_Observed_At'] = (vm.get(vid) or {}).get('Metric_Observation_Date', '')
        f['Classification_Method'] = 'PROGRAMMATIC_RULE_BASED'
        rows.append(f)
    return rows


if __name__ == '__main__':
    rows = build()
    with (HERE / 'title-forensics.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(rows[0])); w.writeheader(); w.writerows(rows)
    (HERE / 'title-forensics.json').write_text(json.dumps(dict(method='PROGRAMMATIC_RULE_BASED; *_Proxy columns are heuristic 0-10 proxies, not analyst scores, not CTR predictions', rows=rows), ensure_ascii=False))
    print(len(rows), len({r['Video_ID'] for r in rows}), Counter(r['Title_Archetype'] for r in rows).most_common(),
          'empty', sum(1 for r in rows if not r['Exact_Title']))
