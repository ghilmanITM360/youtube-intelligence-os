"""Final forensic validation for Decode Your Heart (DS-000032), 2026-09-28.

Hand-recorded research evidence consumed by build_decode_your_heart_recovery.py.
Every entry cites the private Studio export, retention export, retained transcript
or YouTube storyboard frames it rests on. Nothing here is generated from templates.
"""

AUDIT_DATE = "2026-09-28"

YOUTUBE_DEFINITIONS = {
    "source": "https://support.google.com/youtube/answer/10246996 (retrieved 2026-09-28)",
    "new_viewers": "Watched the channel for the first time in the period (includes people with cleared history or private browsing, or who have not watched in over a year).",
    "casual_viewers": "Watched the channel at least once per month for 1 to 5 months in the past year.",
    "regular_viewers": "Watched the channel at least once per month for more than 6 months in the past year.",
    "returning_viewers": "Umbrella term for casual plus regular viewers; the retention report's new-vs-returning split is a separate segmentation of retention curves, not a viewer count.",
    "monthly_audience": "Unique viewers in the last 28 days.",
}

# Phase 2: every important active conclusion from the 5172bff report, challenged.
CLAIM_AUDIT = [
    {
        "id": "A", "previous_claim": "The channel is not yet building a returning audience; zero regular viewers make returning viewers the binding constraint.",
        "original_evidence": "studio-audience-size-growth-last-28-days.zip: 2026-09-26 row 495 new, 10 casual, 0 regular; monthly audience 505.",
        "period": "28-day windows ending 2026-08-30 through 2026-09-26 (28 daily rows)",
        "sample_size": "505 monthly viewers; casual 3-10 across the 28 rows",
        "confounders": "Channel first published 2026-02-03; lifetime Totals.csv shows only 8 views in April 2026, so almost no viewer can have watched in more than 6 of the past 12 months. Views jumped on 2026-09-09 when the coffee Shorts began (new viewers 339 to 458 in one day).",
        "counterexamples": "Casual (returning) viewers rose from 3 to 10 during the window while new viewers also rose.",
        "evidence_strength": "Regular = 0 is structurally expected for this channel age and gap; it is not evidence of a retention failure. Casual share is 2.0% of monthly audience, which is low but measured over one 28-day window only.",
        "corrected_interpretation": "Audience development is UNPROVEN, not demonstrated as the binding constraint. The measurable fact is that about 98% of the latest 28-day audience was new. Whether the channel converts viewers into casual/regular viewers can only be judged after several further 28-day exports.",
        "status": "CORRECTED",
    },
    {
        "id": "A2", "previous_claim": "Retention exports show returning viewers holding better (FDLU7tX7qNM 46.15% vs 17.78% new at 30 s).",
        "original_evidence": "audience-retention-by-video exports with a new-vs-returning split (11 videos).",
        "period": "Per-video lifetime retention through 2026-09-27",
        "sample_size": "11 videos; returning cohort counts are not disclosed and are very small",
        "confounders": "Returning cohorts can be a handful of viewers; Studio discloses curve shape only.",
        "counterexamples": "Returning viewers retained LESS than new viewers at the 30 s position in 8 of 11 videos (e.g. 8JdBlF-ragM 20.0 vs 62.75, 78JR_U-6HfQ 40.0 vs 60.87, qC8BKb8Fh5Q 18.18 vs 37.5); higher only in FDLU7tX7qNM and xI-KdZ96xcI; equal in BCNWQ3uuSuE.",
        "evidence_strength": "The earlier claim was a single-example selection.",
        "corrected_interpretation": "No consistent returning-viewer retention advantage exists in the available splits; the cohort is too small to interpret.",
        "status": "WITHDRAWN",
    },
    {
        "id": "B", "previous_claim": "Discovery is largely South Asian.",
        "original_evidence": "studio-advanced-geography-lifetime.zip: 8,366 total views; 12 disclosed countries carry 2,746 views.",
        "period": "Lifetime 2026-02-03..2026-09-27",
        "sample_size": "2,746 of 8,366 views (32.8%) have a disclosed country",
        "confounders": "Studio withholds small-country rows; undisclosed views may be concentrated or spread across many countries.",
        "counterexamples": "US 327 and GB 305 views are 11.9% and 11.1% of the disclosed set.",
        "evidence_strength": "Within the disclosed third: IN 48.7%, PK 15.0%, LK/NP/BD 4.2% (South Asia ~68%). Nothing can be said about the other 67%.",
        "corrected_interpretation": "South Asia is the largest DISCLOSED segment. The overall audience composition is unknown; do not extrapolate. The previous percentages (IN 16.0%) were shares of total views, correct arithmetic but presented without the disclosure caveat.",
        "status": "CORRECTED",
    },
    {
        "id": "C", "previous_claim": "Discovery comes from other creators' health videos and a long search tail.",
        "original_evidence": "Traffic-source lifetime table; Search-term and Suggested-source drill-downs (lifetime).",
        "period": "Lifetime 2026-02-03..2026-09-27",
        "sample_size": "Suggested 1,031 views / 19,841 impressions; Search 1,175 views / 11,245 impressions; 114 disclosed search terms carry 170 views; 472 disclosed Suggested source videos",
        "confounders": "Drill-downs disclose only top rows; Suggested impressions in the drill-down (19,844) differ from the source table (19,841) by rounding/refresh.",
        "counterexamples": "Monthly source mix changed: Suggested led May-July (250/340/220 views) but Search led August (317) and September (340); Shorts feed dominated February-March.",
        "evidence_strength": "Facts: Shorts feed is 64% of lifetime views; own-channel videos supplied 70 of 1,031 Suggested views; no search term exceeds 7 views.",
        "corrected_interpretation": "Long-form discovery is fragmented across many external source videos and many low-volume search terms; there is no dominant query or source. This says nothing about whether the recommendation system 'prefers' the channel. Search's rising monthly share since August is the only upward source trend visible.",
        "status": "CONFIRMED_WITH_LIMITS",
    },
    {
        "id": "D", "previous_claim": "Lowest CTR among videos with >=500 impressions: HzFdyjyEFTY 1.35%, qbwCkH_GqhU 1.65%, EB3_A2b4a6o 1.81%; Shorts cardiology median CTR 1.48%.",
        "original_evidence": "studio-advanced-content-lifetime-extended.zip thumbnail impressions and CTR.",
        "period": "Lifetime; each video's own age",
        "sample_size": "15 long-form videos with >=500 impressions",
        "confounders": "qbwCkH_GqhU is a 50-second Short: Shorts-feed views carry no thumbnail impression, so Shorts CTR describes only non-feed surfaces and is not comparable. HzFdyjyEFTY was 10 days old at export. CTR mixes Search (2.71%) and Suggested (2.9%) surfaces with different eligibility.",
        "counterexamples": "EB3_A2b4a6o has the second-highest impressions (3,703) with 1.81% CTR yet 60.0% 30-second retention: low click response did not mean poor content response.",
        "evidence_strength": "Long-form CTR range 1.35-4.89% among mature videos is real variation; Shorts CTR comparisons are invalid.",
        "corrected_interpretation": "Remove qbwCkH_GqhU and all Shorts CTR medians from packaging conclusions. Treat HzFdyjyEFTY as immature. EB3_A2b4a6o is the clearest mature long-form case where packaging under-performs the content.",
        "status": "CORRECTED",
    },
    {
        "id": "E", "previous_claim": "Concrete self-test/symptom openings hold more viewers; slow or generic setup coincides with faster decline; fast cutting is not a reliable lever.",
        "original_evidence": "Retention curves plus storyboard/seek frames.",
        "period": "Lifetime retention through 2026-09-27",
        "sample_size": "Long-form videos with 80-367 views; 30 s retention has roughly +/-10 percentage-point 95% uncertainty at 100 viewers",
        "confounders": "Topic, traffic source mix, length and video age are uncontrolled.",
        "counterexamples": "HzFdyjyEFTY opens on a direct question and holds 66.7% at 30 s but has the lowest CTR; CZ3gAUzdTAg (most views) holds only 43.9% at 30 s.",
        "evidence_strength": "Differences above ~20 points (BCNWQ3uuSuE 60.5% vs SBrMW71O69U 38.5%) exceed sampling noise; smaller ones do not. All are associations.",
        "corrected_interpretation": "Supported as an association: openings that state the specific question and pay it off within 30-50 s (BCNWQ3uuSuE fasting myth at 0:40-0:50; HzFdyjyEFTY aspirin reveal at 0:32) hold better than openings built from generic framing and self-promotion (SBrMW71O69U channel-handle overlay 0:18-0:24). Cutting frequency is unrelated in this catalog. Caption timecode defects show no consistent retention direction.",
        "status": "CONFIRMED_AS_ASSOCIATION",
    },
]

# Phase 3: priority reviews. Visual progression from YouTube storyboard frames
# (public i.ytimg.com/sb sprite sheets; every frame of the level viewed), transcript
# from the retained caption track. Audio was not heard in any case.
AV_METHOD = {
    "visual": "YouTube storyboard level-2 sprite sheets (160x90 per frame for long-form, 45x80 for Shorts) at the frame interval YouTube publishes (1 s for videos under ~100 s, 2 s to 5 s for longer ones), viewed sheet by sheet on 2026-09-28. This is continuous full-length visual progression at storyboard resolution, not full-frame-rate playback.",
    "speech": "Retained uploaded caption track (creator-provided text) read in full. YouTube's auto-generated (ASR) track exists for all 12 videos but could not be retrieved in the signed-out browser (timedtext requests rejected; player exposes only the manual track).",
    "audio": "NOT HEARD. The agent environment has no audio output and no local speech-recognition tool; audible speech quality, music level and mix are therefore not assessed. Automated volume measurements from earlier signal passes are not used as evidence of audible quality.",
    "status_label": "PRIORITY_REVIEW_FULL_LENGTH_VISUAL_AND_TRANSCRIPT_AUDIO_NOT_HEARD",
}

PRIORITY_REVIEWS = {
    "CZ3gAUzdTAg": {
        "why_selected": "Highest impressions (5,737) and views (367) in the catalog; cardiology; long-form",
        "coverage": "Storyboard 2 s x 107 frames, 0:00-3:20 of 3:30 viewed (last 10 s not viewed)",
        "timestamps": ["0:00 seated doctor in maroon chair, bright room", "0:02-0:10 SUDDEN BLOCKAGE, artery animation, BUILDS OVER YEARS, PLAQUE BUILDS UP", "0:18-0:22 TOP 5 HEART FOODS over stock food", "0:26-0:30 stock doctor-patient insert COMMON QUESTION / FOOD FOR ARTERIES?", "0:32 NO INSTANT FIX: no food can magically remove plaque overnight", "0:42 1. FATTY FISH; 0:58 1-2X WEEKLY", "1:00 2. BERRIES; ATHEROSCLEROSIS animation", "1:28 3. LEAFY GREEN VEGETABLES / NITRATES", "1:48 4. NUTS, SMALL PORTION, MODERATION", "2:22 5. EXTRA VIRGIN OLIVE OIL, MEDITERRANEAN DIET", "2:34 NO MIRACLE FOOD; example day", "3:18 NEXT: BALANCE TEST end card"],
        "retention_link": "30 s retention 43.92% sits in the 0:26-0:42 stretch where a generic stock insert and a restated question delay the first food; 3 s retention was 88.72%.",
        "title_promise": "DELIVERED: five foods, hedged as support rather than cure.",
        "pacing_visuals": "Frequent B-roll and animation; numbered cards give clear structure.",
        "medical": "Supported (see claim review).",
        "finding": "Strongest reach is not explained by production polish alone; its early delay to the first item is the most visible retention risk.",
    },
    "EB3_A2b4a6o": {
        "why_selected": "Second-highest impressions (3,703) with low CTR 1.81% but high 30 s retention 60.0%; broader Senior Health (diabetes)",
        "coverage": "Storyboard 5 s x 74 frames, 0:00-6:02 complete",
        "timestamps": ["0:00 seated talking head, dim office", "0:15 WHERE DID IT COME FROM", "0:25 7 REASONS YOUR MORNING SUGAR MAY RISE", "1:00-1:15 BODY STARTS PREPARING / liver / GLUCONEOGENESIS (factor 1)", "1:40 HIGH NUMBER != FAILURE", "~2:35 FACTOR #3 THE SLEEP", "~4:00 FACTOR #4 THE ROUTINE; 4:35 DO NOT STOP THEM / KEEP THEM INFORMED", "~5:05 FACTOR #5 SMALL EVENING HABITS", "5:50 subscribe card; 5:55-6:02 fade"],
        "retention_link": "Holds 60.0% at 30 s but falls to 23.57% at midpoint and 13.57% at end; the steepest loss spans the long single-shot factor 2-3 section.",
        "title_promise": "PARTIAL: the video announces seven reasons at 0:25; the transcript and frames contain five numbered factors, then 'Final thoughts'.",
        "pacing_visuals": "One static seated shot for six minutes; variety comes only from kinetic text and small icons.",
        "medical": "Supported; appropriately tells viewers not to stop medication.",
        "finding": "Packaging and in-video promise both under-deliver a strong opening: low CTR plus a seven-to-five promise gap.",
    },
    "BCNWQ3uuSuE": {
        "why_selected": "Strong long-form (CTR 4.16%, 60.5% at 30 s); cardiology test explainer; matched against SBrMW71O69U",
        "coverage": "Storyboard 2 s, 0:00-1:40 of 3:37 viewed (sheets 0-1); earlier seek samples cover later events",
        "timestamps": ["0:00 seated doctor at desk", "0:04 LIPID PROFILE = CHOLESTEROL TEST", "0:10 CHECK YOUR CHOLESTEROL / SIMPLE BLOOD TEST / FUTURE HEART DISEASE RISK", "0:36 COMMON CONFUSION", "0:40 12-HOUR FAST? MYTH", "0:48 NON-FASTING IS OK", "1:00 only triglycerides are fasting dependent", "1:20 #1 RISK FACTOR OF PLAQUE BUILDUP (LDL)", "1:36 NSTEMI / UNSTABLE ANGINA / HEART ATTACK"],
        "retention_link": "A concrete myth is set up and answered by 0:50, inside the 30 s-60 s window where it keeps 60.5%.",
        "title_promise": "DELIVERED.",
        "pacing_visuals": "Static desk shot with label cards; minimal B-roll.",
        "medical": "Supported (non-fasting lipid testing).",
        "finding": "Clear evidence that specific, useful answers early can hold viewers without heavy editing.",
    },
    "SBrMW71O69U": {
        "why_selected": "Weaker cardiology comparator (38.46% at 30 s, CTR 2.87%)",
        "coverage": "Storyboard 2 s, 0:00-1:40 of 3:51 viewed (sheets 0-1)",
        "timestamps": ["0:00 A VERY COMMON PROBLEM", "0:06 SHOCKED?", "0:08 HYPERCHOLESTEROLEMIA", "0:14 LIPID PROFILE", "0:18-0:24 channel-handle overlay @DrRehanOmar", "0:36 YOUR CHOLESTEROL PANEL; lifestyle icons", "0:44 CHOLESTEROL RISK FACTORS", "0:48 WHAT DO CARDIOLOGISTS LOOK FOR?", "1:04 LET'S BREAK IT DOWN; 1. LDL", "1:30 LDL < 100; LDL < 70; 1:38 coronary artery disease"],
        "retention_link": "The first answer ('what cardiologists look for') arrives at ~0:48 after jargon and a self-promotion overlay; retention is 38.46% at 30 s.",
        "title_promise": "DELIVERED slowly.",
        "pacing_visuals": "Same static single-shot format as BCNWQ3uuSuE; the difference is script order, not production.",
        "medical": "Simplified targets (see claim review).",
        "finding": "Paired with BCNWQ3uuSuE the difference is where the useful answer appears, not visual style.",
    },
    "5oPzZjfNgII": {
        "why_selected": "High CTR 4.72% and 56.15% at 30 s; broader circulation topic",
        "coverage": "Storyboard 2 s, 0:00-1:40 of 3:31 viewed",
        "timestamps": ["0:00 YOUR LEGS ARE SENDING SIGNALS", "0:02 OVER 60? PAY ATTENTION", "0:24 WHICH SYMPTOMS MATTER MOST? / WHAT TO TAKE SERIOUSLY", "0:36 ARE YOU LISTENING TO THE SIGNALS?", "1:06 4 KEY WARNING SYMPTOMS", "1:08 1. CALF PAIN WHILE WALKING / CLAUDICATION", "1:22 EARLY PAD WARNING SIGN", "1:28 2. COLD FEET", "1:38 3. SWELLING IN FEET"],
        "retention_link": "Body-signal framing from frame 1; first symptom arrives at 1:08, later than BCNWQ3uuSuE, yet retention is similar, so early delay alone does not explain all differences.",
        "title_promise": "DELIVERED.",
        "pacing_visuals": "Static seated shot with label cards.",
        "medical": "Supported.",
        "finding": "Counterexample to a strict 'answer by 30 s' rule.",
    },
    "HzFdyjyEFTY": {
        "why_selected": "Lowest long-form CTR (1.35%) with high 30 s retention (66.67%); cardiology medication; published 2026-09-17",
        "coverage": "Storyboard 2 s x 92 frames, 0:00-3:02 complete",
        "timestamps": ["0:00 seated doctor, clinic room", "0:06 ASK YOURSELF / WHY ARE YOU TAKING IT?", "0:22 MISCONCEPTION", "0:32 'Yes, I'm talking about aspirin'", "1:06 CLINICAL DATA / CLINICAL EVIDENCE", "1:14-1:18 'contraindicated or not required' PRIMARY PREVENTION", "1:46 CLINICAL TRIALS ('CAPRIE')", "2:00 BLEEDING RISK: GI, intracranial", "2:34 secondary prevention: 'should always be given as the first priority'", "2:56 AVOID IT: 'avoid taking aspirin'", "3:00 NO KNOWN HEART CONDITION / BLEEDING RISK"],
        "retention_link": "Direct second-person question holds 66.67% at 30 s.",
        "title_promise": "DELIVERED on who should and should not take it, but the close is a blanket instruction.",
        "pacing_visuals": "Single static shot; one icon per sentence.",
        "medical": "SIGNIFICANT ISSUE: no advice to consult a clinician before stopping; cites CAPRIE (a clopidogrel secondary-prevention trial); 'contraindicated' overstates.",
        "finding": "Highest-priority medical correction in the catalog; low CTR is confounded by its 10-day age.",
    },
    "8JdBlF-ragM": {
        "why_selected": "Highest CTR among >=500-impression videos (4.89%), 55.74% at 30 s; GLP-1 topic",
        "coverage": "Storyboard 1 s x 72 frames, 0:00-1:10 complete",
        "timestamps": ["0:00 seated doctor at desk with name plate", "0:02 OZEMPIC / SEMAGLUTIDE", "0:05-0:08 pen-injector stock images", "0:10 NEW ADVERSE EFFECTS", "0:22 search-bar graphic", "0:24 LOSS OF LIBIDO", "0:26 WEIGHT LOSS silhouette", "0:27 FAT LOSS + MUSCLE LOSS", "0:32 GENITAL FAT LOSS; anatomical diagrams", "0:36 FAT PROVIDES STRUCTURAL SUPPORT", "0:48 SAGGY / PETULOUS / DRY", "0:53 RISK gauge: AGGRESSIVELY / RAPIDLY / DAYS INSTEAD OF MONTHS", "0:60 RAPID WEIGHT LOSS = HIGH RISK", "1:05 GRADUAL LOSS / PROPER HYDRATION"],
        "retention_link": "Novel, specific curiosity (named side effect) from 0:10; 45.9% still watching at end.",
        "title_promise": "DELIVERED.",
        "pacing_visuals": "Fastest cutting in the set (1 s storyboard changes every 1-3 frames).",
        "medical": "SIGNIFICANT ISSUE: presents an informal term and a speculative mechanism as an established new adverse effect.",
        "finding": "The best-clicked video is also one of the least evidence-based; strong response must not be copied by adding speculative claims.",
    },
    "QfRaG71ZA_0": {
        "why_selected": "Strongest Short (stayed 57.28%, APV 83.27%)",
        "coverage": "Storyboard 1 s x 47 frames complete at Shorts storyboard resolution",
        "timestamps": ["0:00 VEED-branded AI skeleton character with coffee, 'Seniors watch this' banner", "0:06 cut to doctor in blue scrubs, red chair, yellow caption boxes", "0:14-0:34 doctor with heart/pill icons listing symptoms", "0:36 back to glowing-heart skeleton", "0:45 end"],
        "retention_link": "Unusual non-doctor first frame plus audience call-out.",
        "title_promise": "DELIVERED (symptoms to act on).",
        "pacing_visuals": "Two visual worlds alternating; editor watermark visible at 0:00 and 0:45.",
        "medical": "Supported; repeatedly advises contacting a healthcare provider.",
        "finding": "Best Short uses a distinct first frame and a clear symptom list; third-party editor watermark is a production-quality defect.",
    },
    "hUSVbcHVeVw": {
        "why_selected": "Previously reported title/transcript discrepancy; 414 views Short",
        "coverage": "Storyboard 1 s x 40 frames complete at Shorts storyboard resolution (text on frames not legible at this size)",
        "timestamps": ["0:00-0:04 doctor", "0:06-0:10 anatomical body with highlighted arteries", "0:16-0:18 fish/food", "0:20 berries", "0:26 leafy greens", "0:30 nuts", "0:32 olives/olive oil", "0:34 salad close", "0:36-0:39 doctor with end prompt"],
        "retention_link": "59.87% at 30 s; content is the CZ3gAUzdTAg food list in Short form.",
        "title_promise": "NOT DELIVERED AS STATED: published title says the foods 'Reverse Artery Damage'; retained caption heading says 'Clean Your Arteries'; the script itself says 'No single food can magically fix arteries'.",
        "pacing_visuals": "Food B-roll every 2-4 s.",
        "medical": "MISLEADING TITLE; body copy supported.",
        "finding": "Confirmed: packaging claims what the content explicitly disclaims.",
    },
    "7MXBh2hjfto": {
        "why_selected": "Previously reported title-content mismatch",
        "coverage": "Retained transcript read in full; existing seek-sampled frames reused (no new storyboard pass)",
        "timestamps": ["0:00-0:25 per earlier seek samples: cancer-myth discussion throughout"],
        "retention_link": "End retention 6.25%; 30 s retention not applicable (26 s Short).",
        "title_promise": "NOT DELIVERED: title 'Ozempic vs Appetite Suppressants: Which is Better for Weight Loss'; the entire transcript addresses whether Ozempic causes cancer.",
        "pacing_visuals": "Not re-inspected.",
        "medical": "Overstated reassurance (see claim review).",
        "finding": "Confirmed mismatch.",
    },
    "UeGxF8-hb2s": {
        "why_selected": "Previously verified 39 s black tail; broader mobility topic",
        "coverage": "Retained transcript read; earlier luminance/frame evidence reused",
        "timestamps": ["0:00-0:50 chair-stand explanation", "0:50-1:29 black, near-silent frames (verified earlier)"],
        "retention_link": "69.23% at 30 s collapsing to 7.69% at end over the black section.",
        "title_promise": "PARTIAL: explains the test but defers the answer to 'is 12 a good score' to another video.",
        "pacing_visuals": "Not re-inspected.",
        "medical": "Supported but incomplete (no age-norm answer).",
        "finding": "Confirmed export defect plus an unanswered title question.",
    },
    "FDLU7tX7qNM": {
        "why_selected": "805-view heart-warning Short; only video where returning viewers held better",
        "coverage": "Retained transcript read; earlier seek-sampled frames reused",
        "timestamps": ["0:00 ankle-swelling question", "0:45 end with like/comment/subscribe request"],
        "retention_link": "18.77% at 30 s position; stayed-to-watch 44.01%.",
        "title_promise": "DELIVERED in general terms; content is generic ('health experts warn').",
        "pacing_visuals": "Not re-inspected.",
        "medical": "Supported, generic.",
        "finding": "Generic phrasing and a call-to-action ending; weak evidence either way.",
    },
}

MEDICAL_REFERENCES = {
    "USPSTF_2022_ASPIRIN": "US Preventive Services Task Force, Aspirin Use to Prevent Cardiovascular Disease (2022): Grade D against initiating for primary prevention at >=60; Grade C individual decision at 40-59 with >=10% 10-year risk; current users should not discontinue without consulting their clinician.",
    "ACC_AHA_2019_PRIMARY": "2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease: low-dose aspirin should not be administered routinely for primary prevention in adults >70 or with increased bleeding risk; may be considered selectively at 40-70.",
    "CAPRIE_1996": "CAPRIE (Lancet 1996): clopidogrel versus aspirin in patients with recent stroke, MI or peripheral arterial disease (secondary prevention). It is not a primary-prevention aspirin trial; the relevant primary-prevention trials are ASPREE, ARRIVE and ASCEND (2018).",
    "ESC_EAS_2019_LIPIDS": "2019 ESC/EAS Dyslipidaemia Guidelines: LDL-C goals by risk category, <55 mg/dL very high risk (including established ASCVD), <70 high risk, <100 moderate risk, <116 low risk.",
    "AHA_ACC_2018_CHOLESTEROL": "2018 AHA/ACC Cholesterol Guideline: non-fasting lipid profile acceptable for initial risk assessment; fasting repeat if triglycerides >=400 mg/dL.",
    "FDA_SEMAGLUTIDE_LABEL": "Ozempic/Wegovy US prescribing information: boxed warning for thyroid C-cell tumours in rodents (human relevance not determined); contraindicated with personal or family history of medullary thyroid carcinoma or MEN 2.",
    "AHA_DIET_2021": "2021 AHA Dietary Guidance to Improve Cardiovascular Health: dietary patterns (fish, vegetables, nuts, olive oil) lower risk; no individual food reverses established atherosclerosis.",
    "CDC_STEADI_CHAIR_STAND": "CDC STEADI 30-Second Chair Stand: below-average scores are age- and sex-specific (e.g. <12 for men and <11 for women aged 60-64).",
}

MEDICAL_CLAIM_REVIEWS = [
    {"video_id": "HzFdyjyEFTY", "priority": "IMMEDIATE", "claim": "'Avoid taking aspirin for the sake of preventing yourself from developing any heart condition' addressed to viewers over 60 already taking it daily.", "verdict": "MISLEADING_FRAMING_SAFETY_RISK", "evidence": "USPSTF_2022_ASPIRIN; ACC_AHA_2019_PRIMARY", "analysis": "Direction (no routine primary-prevention aspirin at >=60) matches guidelines, but the video addresses current users and never advises discussing it with a clinician first. USPSTF explicitly says current users should not discontinue without consulting their clinician; some viewers may have undiagnosed indications (stents, AF history, PAD).", "alternative_wording": "If you are over 60 and take daily aspirin but have never had a heart attack, stroke or stent, ask your doctor whether you still need it. Do not stop it on your own."},
    {"video_id": "HzFdyjyEFTY", "priority": "HIGH", "claim": "'We have data from CAPRIE clinical trial ... harms supersede the benefits' for primary prevention.", "verdict": "UNSUPPORTED_CITATION", "evidence": "CAPRIE_1996", "analysis": "CAPRIE compared clopidogrel and aspirin in secondary prevention; it does not support the primary-prevention statement.", "alternative_wording": "Large trials such as ASPREE, ARRIVE and ASCEND found that for people without heart disease, bleeding risk largely offsets the small benefit."},
    {"video_id": "HzFdyjyEFTY", "priority": "MEDIUM", "claim": "'Aspirin is now regarded to be contraindicated ... for primary prevention.'", "verdict": "OVERSTATED", "evidence": "USPSTF_2022_ASPIRIN", "analysis": "Guidelines say 'not recommended routinely' or 'individual decision' at 40-59; 'contraindicated' is a stronger clinical term.", "alternative_wording": "Aspirin is no longer routinely recommended for people without heart disease."},
    {"video_id": "8JdBlF-ragM", "priority": "HIGH", "claim": "Semaglutide causes 'new adverse effects', 'Ozempic vagina' and loss of libido, via genital fat loss making tissue 'saggy, petulous and dry because of dehydration'.", "verdict": "UNSUPPORTED_SPECULATIVE_MECHANISM", "evidence": "FDA_SEMAGLUTIDE_LABEL", "analysis": "Neither term is a recognised adverse effect in the prescribing information or major trials; the mechanism is presented as fact without cited evidence. Rapid weight loss and hydration advice is reasonable general guidance.", "alternative_wording": "Some people online describe changes they call 'Ozempic vagina'. It is not a recognised side effect and research is limited; if you notice changes in sexual health or dryness while losing weight, discuss them with your doctor."},
    {"video_id": "7MXBh2hjfto", "priority": "HIGH", "claim": "Title promises an Ozempic versus appetite-suppressant comparison.", "verdict": "TITLE_CONTENT_MISMATCH", "evidence": "Retained transcript", "analysis": "Content only addresses a cancer myth.", "alternative_wording": "Does Ozempic Cause Cancer? What the Warning Label Actually Means"},
    {"video_id": "7MXBh2hjfto", "priority": "MEDIUM", "claim": "'Ozempic has not been caused for any kind of cancer ... has not shown in any clinical trial for causing any kind of cancer'; warning described as family history only.", "verdict": "OVERSTATED_REASSURANCE", "evidence": "FDA_SEMAGLUTIDE_LABEL", "analysis": "Trials have not shown a clear human cancer increase, but the boxed warning rests on rodent thyroid C-cell tumours with human relevance undetermined, and the contraindication covers personal as well as family history.", "alternative_wording": "Trials so far have not shown a clear rise in cancer in people. The label warns about thyroid tumours seen in animals, so it is not used if you or a family member has had medullary thyroid cancer or MEN 2."},
    {"video_id": "hUSVbcHVeVw", "priority": "IMMEDIATE", "claim": "Title: '5 Foods That Reverse Artery Damage'.", "verdict": "MISLEADING_TITLE", "evidence": "AHA_DIET_2021; the video's own script", "analysis": "The script says no single food can fix arteries; no food reverses established plaque.", "alternative_wording": "5 Foods That Support Healthy Arteries (Doctor Explains)"},
    {"video_id": "SBrMW71O69U", "priority": "LOW", "claim": "LDL <100 ideal; <70 with diabetes or high blood pressure; <55 with established coronary or cerebrovascular disease.", "verdict": "SUPPORTED_SIMPLIFIED", "evidence": "ESC_EAS_2019_LIPIDS", "analysis": "Matches ESC/EAS goals, but ESC assigns targets by total risk category rather than diabetes/hypertension alone.", "alternative_wording": "Your LDL target depends on your overall risk; your doctor sets it, often below 70 or 55 if you have diabetes or heart disease."},
    {"video_id": "BCNWQ3uuSuE", "priority": "NONE", "claim": "The first lipid profile can be non-fasting; only triglycerides are fasting-dependent.", "verdict": "SUPPORTED", "evidence": "AHA_ACC_2018_CHOLESTEROL", "analysis": "Consistent with guideline.", "alternative_wording": None},
    {"video_id": "CZ3gAUzdTAg", "priority": "NONE", "claim": "Five foods 'may help support healthy arteries'; no food removes plaque overnight.", "verdict": "SUPPORTED", "evidence": "AHA_DIET_2021", "analysis": "Hedged appropriately.", "alternative_wording": None},
    {"video_id": "EB3_A2b4a6o", "priority": "NONE", "claim": "Dawn phenomenon, sleep and medication timing can raise fasting glucose; do not stop medicines.", "verdict": "SUPPORTED", "evidence": "Standard diabetes care guidance", "analysis": "Accurate and safety-conscious; in-video 'seven reasons' promise only partly delivered (five factors).", "alternative_wording": "Five reasons your morning blood sugar may be higher (or add the missing two)."},
    {"video_id": "QfRaG71ZA_0", "priority": "NONE", "claim": "Palpitations, anxiety, sleep problems after coffee warrant contacting a healthcare provider.", "verdict": "SUPPORTED", "evidence": "General clinical guidance", "analysis": "Safety-conscious.", "alternative_wording": None},
    {"video_id": "UeGxF8-hb2s", "priority": "LOW", "claim": "No single passing score for the 30-second chair stand; the number reflects strength and endurance.", "verdict": "SUPPORTED_INCOMPLETE", "evidence": "CDC_STEADI_CHAIR_STAND", "analysis": "True that norms vary, but CDC publishes age/sex thresholds the title question ('Is 12 good?') could answer.", "alternative_wording": "For ages 60-64, fewer than 12 stands (men) or 11 (women) is below average; thresholds fall with age."},
    {"video_id": "5oPzZjfNgII", "priority": "NONE", "claim": "Calf pain on walking (claudication), cold feet and foot swelling can signal circulation problems.", "verdict": "SUPPORTED", "evidence": "General PAD guidance", "analysis": "Presented as signals to check, not diagnoses.", "alternative_wording": None},
    {"video_id": "FDLU7tX7qNM", "priority": "NONE", "claim": "Persistent ankle swelling can be linked to heart function and should be checked.", "verdict": "SUPPORTED_GENERIC", "evidence": "General clinical guidance", "analysis": "Accurate but non-specific.", "alternative_wording": None},
]

# Phase 5: root-cause investigation matrix (no overall score).
ROOT_CAUSE_MATRIX = [
    {"constraint": "Discovery volume", "observation": "36,159 lifetime thumbnail impressions for 56 videos over ~8 months; 4,360 in the last 28 days.", "scope": "Channel", "supporting_evidence": "Traffic-source lifetime table; content last-28-days export.", "counterexamples": "CZ3gAUzdTAg alone received 5,737 impressions.", "confounders": "Channel age, niche competition, upload gap in April 2026.", "interpretation": "Reach is small in absolute terms. The data cannot say why; there is no evidence of suppression.", "confidence": "HIGH for the observation; NONE for any mechanism", "practical_response": "Do not chase 'algorithm' fixes. Measure impressions per new long-form video in its first 28 days as the baseline for experiments."},
    {"constraint": "Viewer appeal (click response) on long-form", "observation": "Mature long-form CTR ranges 2.5-4.9%; EB3_A2b4a6o 1.81% on 3,703 impressions despite 60.0% 30 s retention.", "scope": "Some long-form videos, not systematic", "supporting_evidence": "Extended content export CTR/impressions; EB3_A2b4a6o retention export.", "counterexamples": "BCNWQ3uuSuE 4.16%, 5oPzZjfNgII 4.72% with the same doctor-portrait thumbnail style.", "confounders": "Source mix per video not exported; video age; topic.", "interpretation": "Packaging is a video-level issue for specific videos (EB3_A2b4a6o clearest), not a channel-wide failure.", "confidence": "MEDIUM", "practical_response": "Experiment E1 (Test & Compare) on EB3_A2b4a6o and HzFdyjyEFTY."},
    {"constraint": "Opening retention (first 30-60 s)", "observation": "Mature long-form 30 s retention ranges 31-67%.", "scope": "Long-form", "supporting_evidence": "BCNWQ3uuSuE 60.5% (myth answered by 0:50) vs SBrMW71O69U 38.46% (answer at ~0:48 after jargon and handle overlay); CZ3gAUzdTAg 43.92% with a stock insert before the first food at 0:42.", "counterexamples": "5oPzZjfNgII 56.15% with first symptom at 1:08.", "confounders": "Topic, audience source, small cohorts (80-367 views).", "interpretation": "Association only: early, specific payoff and absence of self-promotion coincide with better holds.", "confidence": "MEDIUM", "practical_response": "Experiment E2 (opening structure) on the next 6 long-form uploads."},
    {"constraint": "Ongoing engagement (mid-video)", "observation": "EB3_A2b4a6o falls 60.0% to 23.57% by midpoint; CZ3gAUzdTAg ends 10.39%.", "scope": "Longer (>3.5 min) long-form", "supporting_evidence": "Retention curves; EB3_A2b4a6o storyboard shows six minutes of one static shot and a seven-reason promise with five delivered.", "counterexamples": "BCNWQ3uuSuE is also a static shot and ends 10.92%, similar to CZ3gAUzdTAg which has heavy B-roll.", "confounders": "Length; topic depth.", "interpretation": "No production style explains mid-video loss; unkept promises (EB3_A2b4a6o) are a concrete, fixable contributor in one video.", "confidence": "LOW-MEDIUM", "practical_response": "Keep count promises exact; review mid-video curve after E2."},
    {"constraint": "Topic strategy", "observation": "Cardiology and broader senior-health videos show overlapping CTR and retention ranges.", "scope": "Channel", "supporting_evidence": "Long-form cardiology vs broader CTR medians 2.83% vs 3.09% (within noise).", "counterexamples": "Top five by views mix arteries, walking tests, ankles and lipid tests.", "confounders": "Format and age.", "interpretation": "No evidence that narrowing to cardiology or widening to senior health would help by itself.", "confidence": "LOW", "practical_response": "Experiment E4 (topic series) rather than a channel pivot."},
    {"constraint": "Audience alignment", "observation": "Titles target 'After 60'; age export shows most views from viewers aged 25-54; disclosed geography is mostly South Asian but covers 32.8% of views.", "scope": "Channel", "supporting_evidence": "Age/gender and geography exports.", "counterexamples": "Signed-in age data exclude many older viewers and shared devices; undisclosed geography is 67%.", "confounders": "Studio demographics are signed-in estimates.", "interpretation": "Possible mismatch between intended and actual audience; not demonstrated.", "confidence": "LOW", "practical_response": "Future research R2; do not re-target content on current data."},
    {"constraint": "Audience development", "observation": "Latest 28 days: 495 new, 10 casual, 0 regular.", "scope": "Channel", "supporting_evidence": "New/casual/regular export; YouTube definitions.", "counterexamples": "Regular = 0 is structurally expected for an 8-month channel with a dormant April.", "confounders": "Channel age; Shorts spike from 2026-09-09.", "interpretation": "Hypothesis, not a demonstrated constraint.", "confidence": "LOW", "practical_response": "Future research R1: re-export monthly and track casual share."},
    {"constraint": "Content and medical quality", "observation": "Two misleading titles, one unsafe instruction, one speculative medical claim, one 39 s black tail, one editor watermark, caption defects on 10 tracks.", "scope": "Specific videos (local, not channel-wide)", "supporting_evidence": "Medical claim reviews; priority reviews; caption scan.", "counterexamples": "8JdBlF-ragM (speculative claim) is among the best performers, so quality defects are not what limits growth.", "confounders": "Not applicable (these are quality issues regardless of metrics).", "interpretation": "Fix for accuracy and trust, not as a growth lever.", "confidence": "HIGH for the defects", "practical_response": "Immediate corrections Q1-Q6."},
]

NOT_SUPPORTED = [
    "Zero regular viewers proves a returning-audience failure (structurally expected for channel age).",
    "Returning viewers retain better (8 of 11 splits show the opposite).",
    "The audience is predominantly South Asian (only 32.8% of views have a disclosed country).",
    "Shorts CTR differences reflect packaging quality (Shorts-feed views carry no impressions).",
    "Faster cutting improves retention (NznebmgFwXI 0.8 cuts/min held better than KPYHy7MDmLM 16.9).",
    "Caption timecode defects reduce retention (no consistent direction).",
    "Cardiology topics under-perform broader health topics (within 0.6 CTR points, direction reverses by format).",
    "The recommendation system prefers or penalises the channel (no data can show this).",
    "Posting Shorts and long-form on one channel harms growth (DS-000018 creator claim; cross-format data not exported).",
]

KNOWLEDGE_APPLICATIONS = [
    {"source": "DS-000011 Hook guide (creator reference)", "passage": "3-step hook: Context Lean (clearly state what the video is about) then Scroll-Stop Interjection then Contrarian Snapback.", "applied_to": "BCNWQ3uuSuE: 'lipid profile' context, 'common confusion', '12-hour fast is a myth' by 0:50 (60.5% at 30 s). HzFdyjyEFTY: question, misconception, aspirin reveal at 0:32 (66.67%).", "verdict": "SUPPORTED by in-video retention", "contradiction": "HzFdyjyEFTY's hook holds viewers but its package gets the lowest CTR: the framework speaks to retention, not clicks."},
    {"source": "DS-000031 strategy corpus (creator)", "passage": "Demand -> Click -> Watch -> Want More; Hit -> Follow-up -> Cluster -> Series; check which video brought returning viewers.", "applied_to": "Coffee cluster (fArHBQo6Ggw, QfRaG71ZA_0, 4ByUo2N_C-I, nRdBvyh7Sy0) coincides with new-viewer rise from 2026-09-09; casual viewers 3 to 10 in the same window.", "verdict": "PARTIALLY SUPPORTED; cluster timing aligns but causation unshown", "contradiction": "The parent coffee long-form (fAwh2svMARM) drew only 48 views; the cluster did not carry viewers to long-form measurably."},
    {"source": "DS-000031 (creator, Urdu lecture)", "passage": "YouTube judges satisfaction: click, stay, binge session, return; 'views are vanity metrics'.", "applied_to": "Use retention and casual-viewer share as experiment metrics, not raw views.", "verdict": "CONSISTENT WITH OFFICIAL GUIDANCE (YouTube describes appeal, engagement and satisfaction)", "contradiction": None},
    {"source": "DS-000018 algorithm-watch creator video", "passage": "Shorts and long-form are 'two completely different algorithms' and audiences; posting both on one channel is a mistake.", "applied_to": "64% of lifetime views are Shorts feed; long-form gets few views.", "verdict": "UNVALIDATED CREATOR CLAIM; viewers-across-formats report not exported, so the channel cannot test it", "contradiction": "YouTube's official Studio offers a viewers-across-formats report precisely because overlap exists; no recommendation to split channels."},
    {"source": "YouTube Help (official)", "passage": "Casual = 1-5 of past 12 months; regular = more than 6 of past 12 months.", "applied_to": "Claim A correction.", "verdict": "OFFICIAL, OVERRIDES CREATOR CLAIMS", "contradiction": None},
]

IMMEDIATE_CORRECTIONS = [
    {"id": "Q1", "video_id": "HzFdyjyEFTY", "action": "Pin a comment and add to description (and, if re-editing, a closing card): 'Do not stop aspirin without talking to your doctor.' Replace the CAPRIE reference with ASPREE/ARRIVE/ASCEND in future cuts.", "evidence": "USPSTF 2022; storyboard 2:56-3:00; transcript"},
    {"id": "Q2", "video_id": "hUSVbcHVeVw", "action": "Retitle to 'Foods That Support Healthy Arteries'; remove 'Reverse'.", "evidence": "Title vs own script"},
    {"id": "Q3", "video_id": "7MXBh2hjfto", "action": "Retitle to match the cancer-myth content; correct the 'family history only' wording in a pinned comment.", "evidence": "Transcript; FDA label"},
    {"id": "Q4", "video_id": "8JdBlF-ragM", "action": "Add a pinned clarification that 'Ozempic vagina' is not a recognised side effect and the mechanism is unproven; keep the title (it is not false) but avoid 'new adverse effects' framing in any follow-up.", "evidence": "FDA label; transcript"},
    {"id": "Q5", "video_id": "UeGxF8-hb2s", "action": "Trim the 39 s black tail with YouTube Studio's Trim tool (keeps the URL and metrics).", "evidence": "Earlier luminance verification"},
    {"id": "Q6", "video_id": "10 caption tracks listed in CAPTION_TIMECODE_IDS; 2 with emoji", "action": "Re-upload clean caption files without '(m:ss)' markers or emoji.", "evidence": "Caption scan of retained transcripts"},
    {"id": "Q7", "video_id": "QfRaG71ZA_0 and any VEED-watermarked Shorts", "action": "Export future Shorts without the third-party editor watermark.", "evidence": "Storyboard 0:00 and 0:45"},
    {"id": "Q8", "video_id": "EB3_A2b4a6o", "action": "Either change the spoken '7 reasons' reference in future re-uses or make follow-ups state the exact count delivered.", "evidence": "Transcript factors 1-5; storyboard 0:25"},
]

EXPERIMENTS = [
    {"id": "E1", "name": "Long-form title/thumbnail Test & Compare", "purpose": "Test whether a specific question/answer package lifts click response on videos whose content already holds viewers.", "eligible_videos": ["EB3_A2b4a6o", "HzFdyjyEFTY (after it passes 28 days old)", "CZ3gAUzdTAg"], "evidence_basis": "EB3_A2b4a6o CTR 1.81% vs 60.0% 30 s retention; HzFdyjyEFTY CTR 1.35% vs 66.67%.", "window": "Days 1-30; YouTube Studio Test & Compare runs up to 2 weeks per test", "metrics": "Test & Compare watch-time share (YouTube's winner criterion); secondary impressions CTR from the same period", "interpretation": "Count a lift only if Studio declares a winner; 'inconclusive' is a valid result and means packaging is not the limiting factor for that video. Never compare against lifetime CTR."},
    {"id": "E2", "name": "Opening structure on new long-form", "purpose": "Test early specific payoff: state the question in the first sentence and deliver the first concrete answer by 0:30, with no channel-handle or subscribe overlay before 1:00.", "eligible_videos": ["Next 6 long-form uploads, alternating with 3 in the current style if cadence allows"], "evidence_basis": "BCNWQ3uuSuE vs SBrMW71O69U; CZ3gAUzdTAg stock insert before the first item.", "window": "Days 1-60; evaluate each video at 28 days", "metrics": "Retention at 30 s and 60 s (Studio key moments), average percentage viewed; views only as context", "interpretation": "Require a difference above ~15 points in 30 s retention between groups before acting; with ~100 viewers per video smaller differences are noise. Report as association unless randomised."},
    {"id": "E3", "name": "Shorts first-frame specificity", "purpose": "Test whether a distinct first frame plus a named symptom or number improves stayed-to-watch.", "eligible_videos": ["Next 8 Shorts: 4 with a distinct visual first frame and named symptom, 4 in the current talking-head style"], "evidence_basis": "QfRaG71ZA_0 (57.28% stayed) vs 4ByUo2N_C-I (43.7%) from the same footage.", "window": "Days 1-30 per Short", "metrics": "Stayed to watch (%) and engaged views; ignore Shorts CTR", "interpretation": "Shorts feed cohorts vary; judge on the median of each group of 4, not the single best Short."},
    {"id": "E4", "name": "Topic cluster/series pilot", "purpose": "Test whether a connected 3-part long-form series with explicit end-screen links raises own-channel Suggested views and casual viewers.", "eligible_videos": ["New 3-part series on one topic that already showed interest (lipid tests: BCNWQ3uuSuE; leg/circulation signals: 5oPzZjfNgII, NznebmgFwXI)"], "evidence_basis": "Own-channel videos supplied only 70 of 1,031 Suggested views; DS-000031 cluster/series framework (creator claim).", "window": "Days 31-90", "metrics": "Own-channel Suggested views per series video (Suggested drill-down), end-screen click rate, 28-day casual viewers", "interpretation": "Useful evidence = own-channel Suggested share of series videos above the channel's 6.8% lifetime baseline; casual viewer count is secondary because it is channel-wide."},
    {"id": "E5", "name": "Medical-accuracy guardrail (process, not growth test)", "purpose": "Every new script checked against a named guideline before recording; titles may not claim reversal/cure.", "eligible_videos": ["All new uploads"], "evidence_basis": "Five significant claim issues in the priority set.", "window": "Continuous", "metrics": "Count of claims with named source; zero unsupported treatment claims", "interpretation": "Not measured by views."},
]

FUTURE_RESEARCH = [
    {"id": "R1", "question": "Is audience development a real constraint?", "requires": "Monthly new/casual/regular export for at least 3 further 28-day windows (2026-10-26, 2026-11-23, 2026-12-21); regular viewers cannot appear until viewers accumulate >6 active months."},
    {"id": "R2", "question": "Who is the actual audience?", "requires": "Viewers-across-formats report; per-video geography and age for the top 10 videos; comments review."},
    {"id": "R3", "question": "Which surfaces drive each video?", "requires": "Per-video traffic-source and Suggested/Search drill-downs for the E1/E2 videos."},
    {"id": "R4", "question": "Audible speech quality and mix", "requires": "Heard review by a person, or explicit approval to install a local speech-recognition tool and download audio; not attempted without approval."},
]

PLAN_30_60_90 = [
    {"window": "Days 1-30 (from 2026-09-28)", "actions": "Q1-Q8 corrections; start E1 on EB3_A2b4a6o then CZ3gAUzdTAg; publish first E2 and E3 videos; export new/casual/regular on 2026-10-26.", "success_evidence": "Corrections live; E1 Studio verdict recorded (winner or inconclusive)."},
    {"window": "Days 31-60", "actions": "Continue E2/E3; E1 on HzFdyjyEFTY; plan and publish E4 series part 1-2; export per-video traffic sources for E2 videos.", "success_evidence": "At least 4 E2 videos with 28-day retention; E3 group medians compared."},
    {"window": "Days 61-90", "actions": "Finish E4 series; compare own-channel Suggested share; third audience export; decide which formats to keep.", "success_evidence": "Decisions based on pre-set thresholds; no view-count targets."},
]


def validate() -> None:
    reviewed = set(PRIORITY_REVIEWS)
    assert 8 <= len(reviewed) <= 12
    assert {c["video_id"] for c in MEDICAL_CLAIM_REVIEWS} <= reviewed


if __name__ == "__main__":
    validate()
    print(len(PRIORITY_REVIEWS), "priority reviews;", len(MEDICAL_CLAIM_REVIEWS), "claim reviews")
