"""Builds the v1 reference annex (archive register, rule index, claim verification). Run from repo root."""
import csv, hashlib, pathlib, re, sys
R = pathlib.Path('research/finance-economics-intelligence/reference-framework')
ZIP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
cat = {r['SHA256'] if 'SHA256' in r else '': r for r in []}
rows = list(csv.reader(open('knowledge/youtube/SOURCE_CATALOG.csv')))
hdr = rows[0]; hi = [i for i, h in enumerate(hdr) if 'sha' in h.lower()][0]; ti = [i for i, h in enumerate(hdr) if 'location' in h.lower() or 'path' in h.lower()][0]
tracked = {}
for r in rows[1:]:
    if len(r) > hi and r[ti].startswith('data/raw/global-youtube-knowledge/DS-000011'):
        tracked[r[hi]] = r[0]
# (file, pages, dup_group, text_note)
M = [
 ('Hook guide.pdf', 58, 'HOOK_TEXT_IDENTICAL', 'text layer identical to Hook (1).pdf (md5 of pdftotext output equal); bytes differ by 6'),
 ('Hook (1).pdf', 58, 'HOOK_TEXT_IDENTICAL', 'see Hook guide.pdf'),
 ('Intro Analyzer Prompts.docx (1).pdf', 2, '', 'PDF text layer drops f/fi/ff glyphs (e.g. "o" for "of")'),
 ('YouTube Title Analyzer — Natural Language Prompts (2).pdf', 6, '', 'f/fi glyph loss; page 1 holds a social-post title list and a viewer-satisfaction essay'),
 ('Script Analyzer.pdf', 2, '', 'f/fi glyph loss'),
 ('📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf', 6, '', '16 Commandments table is a chat-assistant restatement (pp.3-5), not a primary author source'),
 ('The Magic of ‘BUT’ and ‘THEREFORE’ in Storytelling.docx (1).pdf', 3, '', 'chat-assistant integration transcript; contains an unsourced Fusion Framework v2.0'),
 ('Viral Checklist.pdf', 2, '', 'attributed to Codie Sanchez in the text; 11 items'),
 ('Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf', 12, '', 'AI-persona authoring blueprint'),
 ('Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf', 3, '', 'AI-persona profiles'),
 ('2026 Algorithm Update.docx', None, 'ALGO_COMPILATION', '62 creator-video transcripts; ~1.1M normalized chars; 4 embedded images'),
 ('2026 Algorithm Update.md', None, 'ALGO_COMPILATION', 'same compilation; 8 base64 images; normalized text ~99.6% similar to txt/docx'),
 ('2026 Algorithm Update.txt', None, 'ALGO_COMPILATION', 'same compilation; no images; constituent index by line in algo_update_constituents.json'),
 ('Youtube Algorithm Explained (2026) .xlsx', None, 'ALGO_COMPILATION', 'one sheet, 65 rows (sno/title/transcript), ~1.31M chars; overlapping rendition of the same transcript set, not independent'),
 ('YouTube algorithm guide.docx (2).pdf', 117, '', 'sequencing/creator guide ("Made by NotNotAbu2"); creator opinion'),
 ('new YT algorithms updates.pdf', 45, '', 'creator opinion; page 1 repeats the Tom Brady title list'),
 ('🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf', 13, '', 'tool-oriented SEO checklist incl. tags section'),
 ('VIDEO EDITING.docx', None, '', 'NOT previously registered (hash and name absent from SOURCE_CATALOG/ARCHIVE_MEMBER_INDEX); 128k chars text, 0 images'),
 ('The Ultimate Nano-Banana Prompt Guide.docx', None, '', 'image-generation prompting; NOT_APPLICABLE to financial fact-checking'),
 ('Ultimate Google VEO 3 Prompt Guide for VIRAL Videos.docx', None, '', 'video-generation prompting; NOT_APPLICABLE to audit'),
]
base = ZIP / 'all training data of youtube'
with open(R / 'REFERENCE_ARCHIVE_REGISTER_v1.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Member', 'SHA256', 'Bytes', 'Pages', 'Existing_SRC_ID_DS000011', 'Registration_Status', 'Duplicate_Group', 'Extraction_Note'])
    for n, pg, g, note in M:
        b = (base / n).read_bytes(); h = hashlib.sha256(b).hexdigest()
        src = tracked.get(h, '')
        w.writerow([n, h, len(b), pg or '', src, 'ALREADY_REGISTERED_BY_HASH' if h in {r[hi] for r in rows[1:] if len(r) > hi} else 'NEWLY_REGISTERED_THIS_ANNEX', g, note])
# --- rule index. Fields: id, source member, locator, meaning, dimension, kind, evidence, applicability
H = 'Hook guide.pdf'; IA = 'Intro Analyzer Prompts.docx (1).pdf'; TA = 'YouTube Title Analyzer — Natural Language Prompts (2).pdf'
SA = 'Script Analyzer.pdf'; SE = '📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf'
BT = 'The Magic of ‘BUT’ and ‘THEREFORE’ in Storytelling.docx (1).pdf'; VC = 'Viral Checklist.pdf'; SEO = '🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf'
CH, CAUSE, LIM = 'CREATIVE_GUIDANCE', 'DESCRIPTIVE_LENS', 'creator/AI heuristic; not a platform fact; conformity is not causation'
RU = [
 ('FR-HOOK-01', H, 'p.1 "3-Step Hook Formula"; p.2', 'Hook = context lean (state topic, relatable frame) -> scroll-stop beat -> contrarian snapback.', 'SCRIPT', CH, 'opening transcript passage', 'Applies to explainers only where a stop/snapback beat exists; do not penalise absence.'),
 ('FR-INTRO-01', IA, 'p.1 s.1 ChatGPT', 'Judge intro (first ~30s) on clarity, curiosity, emotional tone, narrative setup.', 'SCRIPT', CAUSE, 'opening transcript passage; timestamps only if supported', 'Use first ~30s of text as proxy only; no audio/timing evidence.'),
 ('FR-INTRO-02', IA, 'p.2 s.7 Google AI Studio', 'Does the title/thumbnail expectation match the opening lines?', 'SCRIPT', CAUSE, 'title + thumbnail observation + opening passage', 'Retention graph is NOT available; report as expectation match only.'),
 ('FR-INTRO-03', IA, 'p.2 s.6 Perplexity', 'Identify where the intro over-explains vs under-explains.', 'SCRIPT', CAUSE, 'opening passage', LIM),
 ('FR-INTRO-04', IA, 'p.1 s.3 Gemini', 'Flag early anticlimax and missed opportunities in the intro.', 'SCRIPT', CAUSE, 'opening passage', LIM),
 ('FR-TITLE-01', TA, 'p.3 s.1 ChatGPT', 'Key information should sit in the first ~55 characters.', 'TITLE', CH, 'actual title text', 'Truncation varies by surface; not an official limit.'),
 ('FR-TITLE-02', TA, 'p.4 s.3 Gemini', 'Title should match the video concept and balance curiosity with promise of payoff.', 'TITLE', CAUSE, 'title + transcript payoff passage', LIM),
 ('FR-TITLE-03', TA, 'p.5 s.6 Google AI Studio', 'Does the title overpromise or underdeliver (clickbait / audience-betrayal risk)?', 'TITLE', CAUSE, 'title + payoff passage', 'Aligns with official guidance against misleading titles (support.google.com/youtube/answer/141805).'),
 ('FR-TITLE-04', TA, 'p.5 s.7 Claude', 'Title opens a loop that the video must pay off.', 'TITLE', CAUSE, 'title + payoff passage', LIM),
 ('FR-VC-01', VC, 'p.1 item 1', 'Audience pain point: a specific pain/desire the audience already has.', 'TOPIC', CH, 'opening passage', LIM),
 ('FR-VC-02', VC, 'p.1 item 2', 'Promise of transformation: tangible outcome addressing the pain.', 'TITLE', CH, 'title + passage', LIM),
 ('FR-VC-04', VC, 'p.1 item 4', 'Contrarian thinking: idea challenging conventional wisdom.', 'VIRALITY', CH, 'passage', 'Checklist states it is not about ticking every box.'),
 ('FR-VC-05', VC, 'p.1 item 5', 'Specificity & numbers make hooks actionable.', 'SCRIPT', CH, 'numeric claim passage', 'Specific numbers must still be verified; specificity is not accuracy.'),
 ('FR-VC-06', VC, 'p.1 item 6', 'Urgency or timeliness.', 'VIRALITY', CH, 'passage + publication date', 'Finance timeliness needs dated evidence.'),
 ('FR-VC-09', VC, 'p.2 item 9', 'Concise: no filler words.', 'SCRIPT', CH, 'passage', LIM),
 ('FR-SCR-01', SA, 'p.1 s.1 ChatGPT', 'Narrative spine: coherent setup -> tension -> resolution.', 'SCRIPT', CAUSE, 'beat map of full transcript', 'Educational explainers may use argument structure, not narrative arc.'),
 ('FR-SCR-02', SA, 'p.1 s.1 ChatGPT', 'Retention mechanics: mini-hooks, open loops, pacing, cliffhangers.', 'SCRIPT', CAUSE, 'passages opening/closing loops', 'Inferred retention risk only; measured retention is NOT_AVAILABLE.'),
 ('FR-SCR-03', SA, 'p.1 s.1 ChatGPT; s.6 Google AI Studio', 'Script must deliver what title and thumbnail promise.', 'SCRIPT', CAUSE, 'title, thumbnail, payoff passage', LIM),
 ('FR-SCR-04', SA, 'p.1 s.4 DeepSeek', 'Cause-and-effect links clear; flag momentum collapse/anticlimax; payoffs satisfying.', 'SCRIPT', CAUSE, 'transition passages', LIM),
 ('FR-SCR-05', SA, 'p.1 s.1; p.1 s.7 Claude', 'CTA and monetization placement: where the script guides to next action.', 'SCRIPT', CAUSE, 'closing passage', 'Sponsor/CTA presence is descriptive, not quality.'),
 ('FR-SCR-06', SA, 'p.2 s.5 Perplexity', 'Curiosity gaps planted, delayed, layered; pacing between complexity and accessibility.', 'SCRIPT', CAUSE, 'passages', LIM),
 ('FR-BT-01', BT, 'p.1 rows 4 and 7', 'BUT = complication, THEREFORE = consequence; avoid flat "and then" sequencing.', 'SCRIPT', CH, 'transition passages', 'Source is an assistant transcript; "alternate every 8-12 seconds" (p.1 row 7) is unverified and conflicts with FR-16C-06 (resets every 20-30 s) and with p.3 (micro-arc every 2-3 min).'),
 ('FR-16C-03', SE, 'p.4 #3', 'Cause & Effect: every beat connects by BUT/THEREFORE; no AND THEN.', 'SCRIPT', CH, 'transition passages', 'Chat-assistant restatement; equals FR-BT-01 in substance (one rule, two sources).'),
 ('FR-16C-04', SE, 'p.4 #4', 'Promise delivery: video delivers emotionally and conceptually on title/thumbnail.', 'SCRIPT', CH, 'title + payoff', 'Same substance as FR-SCR-03.'),
 ('FR-16C-05', SE, 'p.4 #5', 'Throughline: one central question or pursuit.', 'SCRIPT', CH, 'beat map', LIM),
 ('FR-16C-06', SE, 'p.4 #6', 'Inject a new visual, emotional or conceptual reset every 20-30 seconds.', 'SCRIPT', CH, 'timed transcript or video', 'NOT_EVALUABLE from stored text alone (no timing/visuals); conflicts with FR-BT-01 cadence claims.'),
 ('FR-16C-07', SE, 'p.4 #7', 'Open new loops before closing old ones.', 'SCRIPT', CH, 'passages', 'Creator heuristic; not validated.'),
 ('FR-16C-13', SE, 'p.5 #13', 'Universal simplicity: complex ideas in plain language.', 'SCRIPT', CH, 'jargon passages', 'Finance jargon vs defined terms can be judged from text.'),
 ('FR-16C-16', SE, 'p.5 #16', 'Echo: end by looping back to the opening question/theme.', 'SCRIPT', CH, 'opening and closing passage', 'Not every explainer needs a callback.'),
 ('FR-SEO-01', SEO, 'p.5 s.7 Title Checklist; p.3 script optimization', 'Main keyword in title (early) and spoken naturally in first 30s.', 'TITLE', CH, 'title + opening passage', 'Keyword stuffing warned against p.12; no search-volume data in packets.'),
]
NA = [('FR-NA-01', '16C #9/#10/#12', 'Cinematic energy, visual metaphor, texture', 'NOT_APPLICABLE_WITHOUT_AUDIOVISUAL_EVIDENCE'),
      ('FR-NA-02', 'Nano-Banana and VEO 3 guides', 'Image/video generation prompting', 'NOT_APPLICABLE_TO_FINANCE_FACT_CHECKING_OR_K01'),
      ('FR-NA-03', 'Seven Engine/Intro/Script persona prompts', 'Scores 1-10, hero journey overlay, named-director comparisons, multi-model personas', 'NOT_EXECUTED; lenses applied by one analyst, no seven services invoked')]
with open(R / 'REFERENCE_RULE_INDEX_v1.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Rule_ID', 'Source_Member', 'Source_SHA256', 'Locator', 'Meaning', 'Audit_Dimension', 'Rule_Kind', 'Evidence_Required', 'Applicability_Limits', 'Version'])
    reg = {r['Member']: r['SHA256'] for r in csv.DictReader(open(R / 'REFERENCE_ARCHIVE_REGISTER_v1.csv'))}
    for rid, m, loc, mean, dim, kind, ev, lim in RU: w.writerow([rid, m, reg[m], loc, mean, dim, kind, ev, lim, 'v1'])
    for rid, loc, mean, st in NA: w.writerow([rid, '', '', loc, mean, 'NONE', 'NOT_APPLICABLE', '', st, 'v1'])
CL = [
 ('AL-01', 'Title Analyzer p.1', 'Algorithm "prioritizes Satisfaction" via end-of-watch signals and 1-5 star surveys; 1 star "suffocates" reach.', 'support.google.com/youtube/answer/16089387; 11914225', 'PARTLY_SUPPORTED', 'Official pages confirm satisfaction surveys and likes/dislikes/not-interested as inputs; star-scale reach suppression and the "good abandonment" taxonomy are not stated.', 'Treat satisfaction as a real but unmeasured signal; never infer it for a video.'),
 ('AL-02', '2026 Algorithm Update.txt l.52-58 (video 01)', 'Channels with <100k-impression-style "dead" status should be abandoned for a fresh email; YouTube treats every email differently.', 'support.google.com/youtube/answer/16089387', 'UNVERIFIED_NOT_ON_OFFICIAL_PAGES', 'Neither page mentions dead channels or account/email treatment; recommendations are described as personalised to viewers.', 'Do not use; creator theory only.'),
 ('AL-03', '2026 Algorithm Update.txt video 01 (l.20-60)', 'Mixing Shorts and long-form on one channel harms performance.', 'support.google.com/youtube/answer/11914225', 'CONTRADICTED_IN_PART', 'Official page says the system favors no particular format or video type; no channel-mixing penalty is stated.', 'Do not penalise formats for mixing.'),
 ('AL-04', 'SEO checklist p.7 s.10', 'Tags checklist (main keyword first tag etc.).', 'support.google.com/youtube/answer/141805', 'CONTRADICTED_IN_PART', 'Official page calls tags minimally important (spelling variants).', 'Never score tag use; titles/descriptions matter more.'),
 ('AL-05', 'new YT algorithms updates.pdf p.1', 'Algorithm ranks viewer curiosity gap, not how good the video is.', 'support.google.com/youtube/answer/11914225', 'CONTRADICTED_IN_PART', 'Official page lists clicks, skips, view duration, percentage viewed, surveys and likes as performance signals.', 'Curiosity is a creative lens, not a ranking law.'),
 ('AL-06', 'YouTube algorithm guide pp.1-', 'Upload sequencing / content chaining drives binge loops.', 'support.google.com/youtube/answer/11914225', 'PARTLY_SUPPORTED', 'Official page says recommendations use videos commonly watched together and how much of a channel the viewer already watches; no required upload order.', 'Not relevant to single-video audits.'),
 ('AL-07', '2026 Algorithm Update.txt l.1620; l.3322; video 19', 'Views die after 24-48 hours; fixed reset windows.', 'support.google.com/youtube/answer/11914225', 'UNVERIFIED_NOT_ON_OFFICIAL_PAGES', 'Page states no reset intervals; reach shifts with topic popularity, competition and seasonality.', 'Do not interpret age-based tiers as reset effects; K01 uses lifetime rate only.'),
 ('AL-08', 'Viral Checklist p.1', 'More boxes hit raises odds of going viral.', 'support.google.com/youtube/answer/16089387', 'UNVERIFIED_NOT_ON_OFFICIAL_PAGES', 'Page makes no guarantees; checklist itself says it is not about checking every box.', 'Report conformity, never causation.'),
 ('AL-09', '2026 Algorithm Update.txt l.136-197', 'AEO/AI-citation optimization and "net information gain".', 'support.google.com/youtube/answer/11914225', 'UNVERIFIED_NOT_ON_OFFICIAL_PAGES', 'Not covered by the three starting pages.', 'Creator hypothesis; not applied.'),
]
with open(R / 'REFERENCE_ALGORITHM_CLAIM_VERIFICATION_v1.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Claim_ID', 'Locator', 'Assertion', 'Official_Evidence_URL', 'Verdict', 'Evidence_Note', 'Audit_Use', 'Accessed'])
    for r in CL: w.writerow([*r, '2026-11-02'])
print('ok', len(RU), len(CL))
