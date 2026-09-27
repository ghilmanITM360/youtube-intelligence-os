#!/usr/bin/env python3
"""Build evidence-backed recovery artifacts for DS-000032 without changing raw sources."""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/raw/competitors/DS-000032/dataset.json"
THUMB_MANIFEST = ROOT / "data/raw/competitors/DS-000032/public-browser-2026-09-27/thumbnail-recovery-manifest.json"
TRENDS_DIR = ROOT / "data/raw/competitors/DS-000032/public-browser-2026-09-27/google-trends"
STUDIO_DIR = ROOT / "data/raw/first-party/youtube-studio/DS-000032/2026-09-27"
RETENTION_ANALYSIS = STUDIO_DIR / "audience-retention-analysis.json"
OUT_DIR = ROOT / "docs/research/decode-your-heart-2026-09-27"
OUT_DIR.mkdir(parents=True, exist_ok=True)

VISIBLE_TEXT = {
    "-SjQc2MwaOU": "happen when the heart isn't pumping blood efficiently.", "1bb5M4E1oQs": "7 DAY NO SUGAR, NO CARB DIET PLAN",
    "3dRcNqiLHgY": "NO SEVERE PAIN?", "4ByUo2N_C-I": "WRONG QUESTION!", "5oPzZjfNgII": "WORSE BY EVENING? / AM to PM",
    "78JR_U-6HfQ": "CARDIOLOGIST WARNS / THIS MORNING HABIT DAMAGES YOUR HEART / See How to Fix It In The Video Below",
    "7MXBh2hjfto": "No main text; warning/no-smoking-style injection icon", "8JdBlF-ragM": "REAL SIDE EFFECT? / Ozempic vagina?",
    "BCNWQ3uuSuE": "WHICH NUMBER MATTERS? / LIPID PROFILE / LDL / HDL / TRIGLYCERIDES", "CZ3gAUzdTAg": "EAT THESE 5",
    "EB3_A2b4a6o": "NO FOOD? / 168", "FDLU7tX7qNM": "WATCH FULL LONG VIDEO NOW CLICK HERE / Health experts warn that persistent or worsening swelling should",
    "FVfG_HZV4qg": "START", "HEJoPEEndG8": "This leads to persistent fatigue even at rest.", "HzFdyjyEFTY": "SAME PILL? DIFFERENT STORY.",
    "KPYHy7MDmLM": "STOP SLOW WALKING", "Nf9pCrPYWyQ": "BY 2035? 4 BILLION PEOPLE / World Obesity Day", "NznebmgFwXI": "ROOM WARM. FEET COLD?",
    "PIsyBj58fJA": "AFTER 60 / FROZEN SHOULDER?", "PTB-6fgaAKk": "SLOW BLOOD FLOW", "QfRaG71ZA_0": "PALPITATIONS? ANXIETY? / COFFEE?",
    "RD7ugxaBHSQ": "KEEP BLOOD MOVING / AFTER 60", "SBrMW71O69U": "READ THIS FIRST / lipid profile", "TPVOIfcJl-k": "TOO MUCH? / CHOLESTEROL HIGH",
    "UeGxF8-hb2s": "OVER 60? 12 GOOD SCORE? / 30-SEC TEST", "Uq3T8YZgyTw": "OVER 50? CAN YOU DO ALL 3?",
    "VlSibJdSZF8": "APPETITE / HUNGER RETURNS", "VrbLuTNi0qE": "STEADY OR WOBBLY? / 10 SEC", "YVjbjcVo1is": "CHEST HEAVY?",
    "b-dam2LdHzM": "HEALTHY? SPIKE? / INSTANT OATS", "fArHBQo6Ggw": "STOP COFFEE?", "fAwh2svMARM": "BP SPIKE?",
    "gunPgSlxJLA": "FEET FEEL IT FIRST", "hUSVbcHVeVw": "2. BERRIES / INTIOXIDANTS", "iltS1TPt4jo": "JUST STRESS?",
    "j9VqMB6yTXQ": "Seniors / Patients who are seniors", "jLEp6jDsN3Q": "PAIN + SWEAT?", "jxoMnTrVziA": "GOOD BALANCE / STRONG LEGS",
    "kF26QB7xHiE": "IT PREDICTS / HEART", "nP9fDHP1jbo": "IT", "nPqrcrxdrdE": "doc", "nRdBvyh7Sy0": "2 CUPS? SAME? / NOT ALWAYS",
    "p_iI0enaFX8": "60", "phSq6PkPtIg": "THE REAL REASON", "qC8BKb8Fh5Q": "BANANA + BP?", "qObP1FPrC6Q": "7 AM SPIKE?",
    "qbwCkH_GqhU": "NOT JUST LDL", "r9ZyUWyY4Lc": "DOES THIS WORK? / ACV / GLUCOSE", "sC_0XjL2z_Y": "LOOKS NORMAL? / eGFR 95 / uACR HIGH",
    "sUL6SU8LnEg": "MYTH? / Ozempic", "t1j-p9pkw3Y": "30 SEC / HOW MANY?", "tD4KOpsJH_c": "OVER 60? DON'T DRINK COFFEE BEFORE CHECKING YOUR BLOOD PRESSURE! / HIGH READING RISK!",
    "tDZKHR8UjYg": "MISSING RISK? / lipid panel missing row", "tf7f4RhQwtc": "NOT JUST WEIGHT", "xI-KdZ96xcI": "STAIRS FEEL HARDER?", "zESWa7FJgHY": "START HERE",
}


# Authenticated, read-only Studio table observations made on 2026-09-28.
# These are derived research records, not replacements for the retained 2026-09-27 exports.
# Rows not visible in the paged table remain explicitly unavailable below.
LIVE_STUDIO_METRICS = {
    "FVfG_HZV4qg": (522, 18, 53.7, 51.1, 3),
    "FDLU7tX7qNM": (373, 16, 35.9, 44.0, 4),
    "CZ3gAUzdTAg": (343, 59, 28.3, None, None),
    "kF26QB7xHiE": (328, 13, 59.8, 27.0, None),
    "fArHBQo6Ggw": (157, 29, 60.5, 46.7, 1),
    "hUSVbcHVeVw": (152, 31, 79.8, 39.7, 1),
    "EB3_A2b4a6o": (147, 105, 29.0, None, 0),
    "5oPzZjfNgII": (132, 92, 44.1, None, 0),
    "NznebmgFwXI": (124, 46, 31.0, None, 1),
    "BCNWQ3uuSuE": (120, 82, 38.2, None, 2),
    "nP9fDHP1jbo": (113, 10, 53.2, 23.9, 1),
    "VrbLuTNi0qE": (108, 70, 29.5, None, 2),
    "r9ZyUWyY4Lc": (83, 66, 58.2, None, 1),
    "qbwCkH_GqhU": (77, 23, 47.7, 38.6, None),
    "t1j-p9pkw3Y": (77, 79, 44.6, None, 1),
    "QfRaG71ZA_0": (60, 38, 83.3, 57.3, None),
    "-SjQc2MwaOU": (54, 23, 52.1, 20.6, 0),
    "4ByUo2N_C-I": (53, 25, 43.8, 43.7, None),
    "tD4KOpsJH_c": (39, 20, 44.1, 48.7, None),
    "78JR_U-6HfQ": (37, 75, 41.1, None, 1),
    "HzFdyjyEFTY": (37, 68, 37.6, None, None),
    "qC8BKb8Fh5Q": (35, 28, 25.0, None, None),
    "iltS1TPt4jo": (34, 20, 33.8, 37.7, None),
    "xI-KdZ96xcI": (33, 67, 26.5, None, None),
    "YVjbjcVo1is": (31, 27, 52.8, 33.7, None),
    "gunPgSlxJLA": (30, 10, 84.0, 28.7, None),
    "Nf9pCrPYWyQ": (27, 51, 34.4, None, None),
    "fAwh2svMARM": (27, 103, 50.7, None, None),
    "TPVOIfcJl-k": (27, 14, 33.4, 31.4, None),
    "PTB-6fgaAKk": (27, 15, 126.6, 16.9, None),
    "HEJoPEEndG8": (25, 15, 28.0, 13.3, 1),
    "tDZKHR8UjYg": (24, 77, 53.6, None, 2),
    "3dRcNqiLHgY": (23, 36, 31.2, None, None),
    "RD7ugxaBHSQ": (21, 39, 43.5, None, None),
    "KPYHy7MDmLM": (20, 40, 35.0, None, None),
    "b-dam2LdHzM": (17, 38, 65.5, 25.8, None),
    "PIsyBj58fJA": (17, 57, 47.3, None, None),
    "qObP1FPrC6Q": (13, 33, 55.3, 34.2, None),
    "UeGxF8-hb2s": (13, 45, 51.3, 50.0, None),
    "1bb5M4E1oQs": (12, 16, 38.0, 46.2, None),
    "p_iI0enaFX8": (11, 43, 72.0, 46.2, None),
    "sUL6SU8LnEg": (10, 46, 28.3, None, None),
    "nRdBvyh7Sy0": (9, 42, 78.6, 40.9, None),
    "jLEp6jDsN3Q": (8, 23, 42.1, 31.6, None),
    "phSq6PkPtIg": (7, 6, 42.1, None, None),
    "jxoMnTrVziA": (6, 10, 33.9, 57.1, None),
    "Uq3T8YZgyTw": (3, 15, 31.2, 50.0, None),
}


PRIORITY_PLAYBACK = {
    "QfRaG71ZA_0": {
        "duration_seconds": 45,
        "comparison": "Coffee Shorts: stronger acceptance versus 4ByUo2N_C-I",
        "timestamps": ["0:00 AI/staged skeleton holding coffee; PALPITATIONS? ANXIETY? COFFEE?", "0:18 doctor in blue scrubs; red Seniors watch this header and yellow captions", "0:45 end/autoplay transition"],
        "opening": "Immediate symptom-plus-trigger question with a visually extreme coffee/heart cue.",
        "visuals": "Doctor-led medium shot follows the staged opener; static office framing and karaoke-style captions.",
        "editing": "One major visual handoff from staged opener to direct explanation; limited later variation.",
        "closing": "No distinct recap or next step was visible before the autoplay transition.",
        "possible_explanation": "The concrete symptom and trigger may make the first frame easier to classify than the paired generic coffee question.",
        "alternative_explanation": "Audience mix, feed distribution and topic timing may explain part or all of the metric gap.",
    },
    "4ByUo2N_C-I": {
        "duration_seconds": 57,
        "comparison": "Coffee Shorts: weaker retention versus QfRaG71ZA_0",
        "timestamps": ["0:00 doctor, coffee cup and WRONG QUESTION", "0:24 split frame with doctor above generic/cartoon B-roll", "0:57 end screen"],
        "opening": "Contrarian phrase creates curiosity but initially withholds the actual heart-health answer.",
        "visuals": "Doctor in a white coat and a large coffee cup; later split-screen/cartoon support; white captions.",
        "editing": "Moderate visual change, but doctor eye-line often points downward and the frame stays busy.",
        "closing": "Video reaches an end screen after the explanation.",
        "possible_explanation": "The opener's withheld meaning and busier composition may increase early uncertainty.",
        "alternative_explanation": "Its audience and feed cohort may differ from QfRaG71ZA_0.",
    },
    "FVfG_HZV4qg": {
        "duration_seconds": 34,
        "comparison": "Walking Shorts: higher stayed-to-watch versus kF26QB7xHiE",
        "timestamps": ["0:00 direct doctor frame with START", "0:14 fatigued-walker B-roll and LOW STAMINA", "0:34 end screen"],
        "opening": "Direct instruction and recognizable walking-test context.",
        "visuals": "Doctor in black scrubs changes to illustrative walking footage with large labels and captions.",
        "editing": "Fast visual handoff and repeated kinetic words create more motion than the paired walking Short.",
        "closing": "Ends after the test explanation without a long outro.",
        "possible_explanation": "A clear test framing plus early visual change may support feed acceptance.",
        "alternative_explanation": "Higher acceptance did not produce the highest views; distribution scale differed.",
    },
    "kF26QB7xHiE": {
        "duration_seconds": 23,
        "comparison": "Walking Shorts: lower stayed-to-watch versus FVfG_HZV4qg",
        "timestamps": ["0:00 tinted doctor desk frame with IT PREDICTS and cartoon heart", "0:09 generic walking B-roll and DOCTOR OBSERVES", "0:23 end screen"],
        "opening": "The pronoun in IT PREDICTS delays the subject while the cartoon heart competes with the doctor.",
        "visuals": "Warm tint, doctor at desk, cartoon overlay, then generic walking footage and kinetic text.",
        "editing": "Rapid word changes but limited narrative progression beyond claim then explanation.",
        "closing": "Ends immediately after the explanatory line.",
        "possible_explanation": "Vague first-frame language may reduce swipe-stop clarity even though viewers who stayed watched much of the short video.",
        "alternative_explanation": "Its 1,212 views show broad distribution can coexist with low stayed-to-watch.",
    },
    "PTB-6fgaAKk": {
        "duration_seconds": 11,
        "comparison": "Cold-feet Shorts: replay loop versus gunPgSlxJLA",
        "timestamps": ["0:00 circulation anatomy and SLOW BLOOD FLOW", "0:09 caption says movement and walking help circulation", "0:11 end"],
        "opening": "Anatomical circulation image states the mechanism immediately.",
        "visuals": "Full-body vascular illustration with one centered warning label.",
        "editing": "Very short loop; little room for development or variation.",
        "closing": "Explicit prompt to watch the full video.",
        "possible_explanation": "The 126.6% APV is consistent with looping or replay, not necessarily strong feed acceptance.",
        "alternative_explanation": "Low stayed-to-watch may reflect the first frame or the feed cohort rather than the 11-second edit itself.",
    },
    "gunPgSlxJLA": {
        "duration_seconds": 11,
        "comparison": "Cold-feet Shorts: better feed acceptance versus PTB-6fgaAKk",
        "timestamps": ["0:00 seated doctor with FEET FEEL IT FIRST", "0:03 caption explains slow circulation", "0:11 end"],
        "opening": "Concrete body-part statement with the doctor visible immediately.",
        "visuals": "Single office shot, centered doctor, restrained caption treatment.",
        "editing": "Minimal cuts; clarity comes from the concise statement rather than motion.",
        "closing": "Ends after the circulation explanation.",
        "possible_explanation": "The direct symptom phrase may be easier to parse than an anatomy-only opener.",
        "alternative_explanation": "The difference is small-sample and distribution-sensitive.",
    },
    "-SjQc2MwaOU": {
        "duration_seconds": 45,
        "comparison": "Heart-failure Shorts: stronger retention versus HEJoPEEndG8",
        "timestamps": ["0:00 doctor in scrubs with heart warning icon", "0:08 seated doctor under red SENIORS MUST WATCH banner (curve dip -7.4 pts at 0:08)", "0:15 animated heart and warning-triangle overlay while caption says the heart is not pumping efficiently", "0:24 full-frame yellow tint flash over doctor; caption: breathlessness is a commonly missed early sign", "0:33 cartoon patient cutout over doctor; red WATCH FULL VIDEO, LINK IN DESCRIPTION banner", "0:42 full-frame SHARE SHARE SHARE end card with like/comment HEALTH/subscribe caption", "0:45 end (curve dip -11.1 pts at 0:45 follows the CTA card)"],
        "opening": "Shortness of breath is presented as a specific heart signal.",
        "visuals": "Doctor-led vertical office frame, heart/warning overlay and sentence captions.",
        "editing": "Mostly direct-to-camera with explanatory overlays; limited scene change.",
        "closing": "Reaches the player end at 0:45.",
        "possible_explanation": "A concrete symptom may retain more viewers than generic fatigue.",
        "alternative_explanation": "Both Shorts have weak stayed-to-watch; feed cohort and topic familiarity remain plausible.",
    },
    "HEJoPEEndG8": {
        "duration_seconds": 54,
        "comparison": "Heart-failure Shorts: weaker retention versus -SjQc2MwaOU",
        "timestamps": ["0:00 doctor-led office frame", "0:01 static seated doctor, hands clasped, no banner or overlay; caption: tired all the time even without doing much", "0:06 same static frame; caption: could be an early warning sign from the heart (curve dips -12 pts at 0:05 and -16 pts at 0:07)", "0:20 tired-man cutout over doctor; caption: persistent fatigue even after rest", "0:38 full-frame white card: older man holding chest, red arrow, NEVER BE IGNORED", "0:51 back to static doctor frame; caption: subscribe the channel", "0:54 end"],
        "opening": "A broad fatigue warning is introduced before a more specific mechanism is established.",
        "visuals": "Doctor shot with a generic fatigued-person cutout and highlighted captions.",
        "editing": "Overlay changes add movement but the visual idea remains general.",
        "closing": "Reaches the player end at 0:54.",
        "possible_explanation": "Generic fatigue may feel less diagnostic or urgent than shortness of breath.",
        "alternative_explanation": "Low exposure and different viewer cohorts limit causal interpretation.",
    },
    "5oPzZjfNgII": {
        "duration_seconds": 211,
        "comparison": "Long-form symptom explainer versus EB3_A2b4a6o",
        "timestamps": ["0:00 promise to identify serious leg signals; doctor introduction", "0:21 seated doctor in book-lined study; white WHICH SYMPTOMS MATTER MOST? card; caption: as a cardiologist I see this pattern constantly (curve -3.1 pts)", "0:27 same frame; caption: I'm Dr. Rehan, cardiologist, over 20 years of practice (credential intro coincides with -5.4 pt dip, largest after 0:04)", "1:10 white CLAUDICATION card over doctor; caption names intermittent claudication (curve +1.5 pt spike)", "2:21 inset leg-image B-roll over doctor; caption: continuous pain even at rest (curve -3.9 pts)", "3:00 LEGS ARE EARLY INDICATORS summary card; caption: legs are one of the most honest indicators of cardiovascular health", "3:25 red SUBSCRIBE button card; caption teases what we'll cover next", "3:31 target ended before post-roll (end dip -8.5 pts)"],
        "opening": "Specific symptom and seriousness promise arrives before the full doctor introduction.",
        "visuals": "Doctor explanation with symptom-focused examples; thumbnail uses AM/PM ankle comparison.",
        "editing": "Steady explanatory rhythm with topic-specific progression through leg signals.",
        "closing": "Target video ended cleanly; post-roll started afterward.",
        "possible_explanation": "The concrete symptom, shorter duration and clear consequence ladder may support both CTR and retention.",
        "alternative_explanation": "Topic demand, traffic source and publication context also differ from EB3_A2b4a6o.",
    },
    "EB3_A2b4a6o": {
        "duration_seconds": 362,
        "comparison": "Long-form metabolic explainer versus 5oPzZjfNgII",
        "timestamps": ["0:00 chapter The morning sugar mystery", "0:21 seated doctor in plain white clinic room; blood-drop icon; burned-in WHILE YOU WERE ASLEEP WITHOUT YOU; caption previews today's walkthrough (curve -4.3 pts)", "0:32 THE EVENING MISTAKE? burned-in text; caption still previewing: one mistake many people make every evening (curve -3.6 pts)", "0:39 caption: one of the questions I hear most often, doc I didn't eat anything (curve -3.6 pts; still setup, explanation not yet begun)", "0:58 first mechanism line: your body has its own alarm clock around 3 or 4 am (curve -2.9 pts)", "2:00 split food graphics beside doctor: balanced dinner at 6:30 pm versus large refined-carb plate", "3:23 caption: hormones like cortisol, glucagon and adrenaline (curve +2.1 pt spike)", "4:29 check-mark icon over doctor; caption: small changes become habits and patterns (curve +2.1 pt spike)", "5:30 crackers/television illustration; caption narrates an evening snacking scene", "5:55 caption: click the bell icon and subscribe", "6:02 target ended before post-roll (end dip -12.1 pts)"],
        "opening": "Opens with the morning-sugar mystery and a numeric glucose cue.",
        "visuals": "Doctor-led explanation organized by chapters; thumbnail uses meter 168 and NO FOOD.",
        "editing": "Longer, chaptered explanation; mid-video remains visually and narratively steady.",
        "closing": "Target video ended and changed to a post-roll element.",
        "possible_explanation": "Longer duration and a slower middle may contribute to the lower APV and midpoint retention.",
        "alternative_explanation": "The 1.8% CTR and differing distribution mean packaging may also constrain performance.",
    },
    "BCNWQ3uuSuE": {
        "duration_seconds": 216,
        "comparison": "Cholesterol long-form: stronger package/retention versus SBrMW71O69U",
        "timestamps": ["0:00 lipid-profile question and doctor introduction", "0:28 seated doctor in book-lined study, no overlay; caption lists HDL, TGs and triglycerides (curve -3.4 pts)", "1:05 white REPEAT TEST WHILE FASTING card; caption: repeat lipid profile fasting at least 12 hours (curve -3.4 pts)", "1:35 doctor holds a small white item toward camera; caption uses clinical terms non-STEMI and unstable angina with auto-caption errors (curve -3.4 pts)", "2:17 no overlay; caption: South Asian females have heart disease risk (curve +2.5 pt spike)", "2:36 INFLAMMATION SIGNAL card; caption: triglycerides act as an acute inflammatory marker (curve -2.5 pts)", "3:17 START TESTING AT AGE 9 card; caption: first lipid panel advised at 9 years old (curve -2.5 pts)", "3:36 end (end dip -5.0 pts)"],
        "opening": "Asks which lab number matters and names the exact test.",
        "visuals": "Doctor-led explanation supported by the lipid-panel hierarchy shown in the thumbnail.",
        "editing": "Sequential lab-marker explanation provides clear progression with modest visual variety.",
        "closing": "Target video reached its natural end at 3:36.",
        "possible_explanation": "Specific lab-test utility may create a clearer promise than a broad high-cholesterol warning.",
        "alternative_explanation": "Audience source, publication timing and impression volume differ.",
    },
    "SBrMW71O69U": {
        "duration_seconds": 230,
        "comparison": "Cholesterol long-form: weaker early retention versus BCNWQ3uuSuE",
        "timestamps": ["0:00 broad high-cholesterol framing", "0:05 doctor standing in plain white clinic room with stethoscope; white SHOCKED? card; caption: whenever a doctor tells you that you have high cholesterol (curve -16.7 pts at 0:02 and -11.5 at 0:05, steepest opening loss of the pair)", "0:25 caption: doctor gives you a blood test known as lipid profile; burned-in THAT MEANS THAT HE WANTS TO CHECK TOTAL (curve -5.1 pts)", "0:38 lifestyle photo insets (sofa, fast food) around doctor; caption: poor lifestyle, bad dietary habits, abdominal obesity (curve -3.8 pts)", "1:13 LOWER LDL = BETTER card; caption contrasts good and bad cholesterol (curve -2.6 pts)", "2:12 INFLAMMATION MARKER card; caption: third component is triglycerides (curve +1.3 pt spike)", "3:21 150-180 MIN/WEEK card; caption: at least 150 to 180 minutes per week of physical activity", "3:46 SUBSCRIBE button with two end-screen video tiles; caption asks viewers to click", "3:50 end (end dip -16.7 pts)"],
        "opening": "Broad warning asks viewers to read the lipid result first without the paired video's exact-number promise.",
        "visuals": "Doctor and lipid report dominate the package; playback remains a steady explanatory presentation.",
        "editing": "Linear explanation with limited visual reset before the midpoint.",
        "closing": "Target video reached its natural end at 3:50.",
        "possible_explanation": "The broader promise and weaker first-30-second retention may reduce momentum.",
        "alternative_explanation": "Its smaller impression base and different audience exposure prevent a causal claim.",
    },
}

# Batch 3 (2026-09-28): muted seek-and-inspect at each exported retention event plus coverage anchors.
# Frames were viewed and captions read on screen; the video was not watched continuously and audio was not heard.
SEEK_SAMPLED = {
    "YVjbjcVo1is": {
        "duration_seconds": 53,
        "comparison": "Heart-attack Shorts: same doctor footage as iltS1TPt4jo without the cartoon cold open",
        "timestamps": ["0:02 seated doctor in blue scrubs, stethoscope, hands steepled, plain white clinic wall; no title card; caption: Heart attack, or cardiovascular", "0:07 kinetic word Cardiovascular diseases over doctor; caption: cause of mortality across the globe (curve -6.5, -16.1 and -9.7 pts across 0:05-0:08)", "0:25 same frame; caption: relieved on taking rest or after a sublingual nitrate tablet", "0:46 red vertical wipe transition; caption: click the bell icon (curve -9.7 pts at 0:45)"],
        "opening": "Definition-first opener: heart attack and cardiovascular-mortality statistics before any symptom is named.",
        "visuals": "Single seated clinic shot with occasional kinetic words; no B-roll at sampled anchors.",
        "editing": "Minimal cuts; a red wipe introduces the closing CTA.",
        "closing": "Bell-icon CTA over a red wipe.",
        "possible_explanation": "Without a cold open, viewers who stayed past the statistics line reached the symptom content; 30-second retention 45.16% versus 20.59% for the re-edit.",
        "alternative_explanation": "85 versus 87 views: each curve step is roughly one viewer, so the difference may be noise or a different feed cohort.",
    },
    "iltS1TPt4jo": {
        "duration_seconds": 59,
        "comparison": "Heart-attack Shorts: re-edit of YVjbjcVo1is footage with AI-illustrated cold open",
        "timestamps": ["0:02 AI-style illustration STRESS VS HEART ATTACK? (anxious man versus man clutching chest); caption shows literal (0:00) and (0:09) timecodes", "0:06 full-frame illustration of man clutching chest with ECG speech bubble; no doctor yet (curve loses about 5.9 pts per second 0:01-0:08)", "0:13 doctor footage begins under red DONT MISS THIS VIDEO banner, artery-plaque graphic; caption: cause of mortality (0:14) across the globe (curve -8.8 pts at 0:12)", "0:35 same banner; caption: relieved on taking rest or after a sublingual nitrate", "0:55 caption: shortness of breath, weakness, fatigue, in order to find out more (CTA)"],
        "opening": "Illustrated stress-versus-heart-attack question for about 12 seconds, then the same definition-first doctor footage.",
        "visuals": "AI illustrations, then seated doctor under a persistent red DONT MISS THIS VIDEO banner.",
        "editing": "Cold open adds a question but delays the doctor; banner stays on screen for the remainder.",
        "closing": "Verbal CTA at 0:55.",
        "possible_explanation": "Stayed-to-watch was slightly higher (37.7% vs 33.7%) but 30-second retention was far lower (20.59% vs 45.16%): the illustrated question may stop the swipe yet mismatch the statistics-led footage that follows. Uploaded captions display raw (0:00)-style timecodes to viewers.",
        "alternative_explanation": "Tiny samples (87 views) and different publication dates; the caption-timecode defect and banner cannot be separated from the cold open.",
    },
    "fArHBQo6Ggw": {
        "duration_seconds": 49,
        "comparison": "Coffee Shorts: stronger 30-second retention versus tD4KOpsJH_c",
        "timestamps": ["0:02 dark stock-style shot, coffee-drinker illustration in a cup, DRINK COFFEE; caption: If you are 50 and drink coffee", "0:07 stock footage of a man writing, DOCTOR REHAN title; third-person narrator: Listen to what Dr. Rehan says (curve -5.7 and -5.1 pts at 0:05-0:07)", "0:24 doctor on camera, 1. BLOOD PRESSURE card with BP-monitor icon; caption: understand these three things, number one", "0:44 BP SPIKE? long-form thumbnail inset; caption points to the full video Coffee After 50"],
        "opening": "Narrated audience-qualifier question (if you are 50 and drink coffee) before the doctor appears.",
        "visuals": "Stock and illustrated cold open, then doctor with numbered list cards.",
        "editing": "Three-part numbered structure; ends by cross-promoting the long-form video.",
        "closing": "Explicit pointer to the long-form coffee video with its thumbnail.",
        "possible_explanation": "Audience-qualified permission framing plus a numbered promise (three things) may give viewers a reason to stay; 30-second retention 52.23% versus 23.08%.",
        "alternative_explanation": "341 versus 87 views and a permission-versus-warning title difference; distribution scale differs.",
    },
    "tD4KOpsJH_c": {
        "duration_seconds": 46,
        "comparison": "Coffee Shorts: weaker 30-second retention versus fArHBQo6Ggw",
        "timestamps": ["0:02 seated doctor holding a mug, kinetic RAISE YOUR, rising-arrow and heart icons; caption: coffee can temporarily raise your blood pressure", "0:06 AND CHECK YOUR with BP-monitor icon; caption: might not be getting your actual reading (curve -7.7 and -10.3 pts at 0:05-0:06)", "0:10 YOU MIGHT BE GETTING FALSELY with heart/ECG graphic (curve -7.7 pts)", "0:24 COFFEE IS; caption: but here's the important part", "0:42 I HAVE EXPLAINED ALL THESE THINGS with red down-arrow; caption: in my subsequent video"],
        "opening": "Mechanism stated in the first sentence; no audience qualifier or question.",
        "visuals": "Seated doctor with dense kinetic words and icons every few seconds.",
        "editing": "High text density; payoff (measurement advice) delivered by 0:10, leaving little open loop.",
        "closing": "Points to a subsequent video.",
        "possible_explanation": "Delivering the answer immediately may remove the reason to keep watching; the curve loses about 5 pts every 1-3 seconds after 0:05.",
        "alternative_explanation": "Stayed-to-watch was similar (48.7% vs 46.7%), so feed acceptance was not the gap; small sample (87 views).",
    },
    "qbwCkH_GqhU": {
        "duration_seconds": 50,
        "comparison": "Cholesterol Shorts: stronger versus TPVOIfcJl-k",
        "timestamps": ["0:02 doctor standing outdoors on a paved courtyard, THE LIPID PROFILE STORY title and lab-report prop; caption: let me tell you the lipid profile story", "0:05 large LDL text; caption: patients become anxious looking at their LDL number (curve -11.8 pts at 0:04)", "0:25 body and blood-drop icons; caption: they tell you different stories like metabolic syndrome or diabetes", "0:46 checklist LDL, HDL, Triglycerides, Lp(a), HbA1c; caption: look at all these tests to find your future cardiovascular risk"],
        "opening": "Story framing and a named patient emotion (anxiety over LDL) in the first five seconds.",
        "visuals": "Outdoor standing shot, different from the channel's usual seated clinic frame; icons and a closing checklist.",
        "editing": "Builds to a five-item checklist payoff at the end.",
        "closing": "Checklist summary rather than a subscribe card.",
        "possible_explanation": "Patient-problem framing plus a checklist payoff may hold viewers; 30-second retention 39.47% versus 18.52%, end 19.74% versus 3.7%.",
        "alternative_explanation": "199 versus 77 views; the outdoor setting, title and topic specificity all differ at once.",
    },
    "TPVOIfcJl-k": {
        "duration_seconds": 42,
        "comparison": "Cholesterol Shorts: weaker versus qbwCkH_GqhU",
        "timestamps": ["0:02 seated doctor in blue scrubs, plain clinic wall, no title card; caption: (0:01) Hi! Cholesterol is a chemical produced in the body (raw timecode visible)", "0:06 same frame; caption: achieve different metabolic functions, part of hormones and enzymes (curve -7.4, -11.1 and -11.1 pts at 0:04-0:07)", "0:14 kinetic order to cause; caption: but in excess, excessive cholesterol (curve -11.1 pts)", "0:38 full-frame red DON'T FORGET TO SUBSCRIBED card"],
        "opening": "Textbook definition with a greeting; no problem, stakes or audience qualifier.",
        "visuals": "Same seated clinic session as YVjbjcVo1is; sparse kinetic words.",
        "editing": "Single shot; ends on a red subscribe card.",
        "closing": "Subscribe card, no recap.",
        "possible_explanation": "Definition-first openers (also seen in YVjbjcVo1is) coincide with the steepest 0:04-0:08 losses; retention fell to 3.7% by the end.",
        "alternative_explanation": "77 views; the raw caption timecodes and the definition opener cannot be separated.",
    },
    "t1j-p9pkw3Y": {
        "duration_seconds": 178,
        "comparison": "Mobility-test long-form: stronger versus VrbLuTNi0qE",
        "timestamps": ["0:02 seated doctor in teal scrubs, study with red leather chair and framed art, wrist-watch inset; HOW MANY TIMES; caption: If you are over 60, how many times", "0:20 IT MATTERS; caption: what people over 60 can do in 30 seconds, it's a variable (curve -7.8 pts at 0:20)", "0:50 1. FIRM CHAIR, 2. NO ARMRESTS list; caption: use a firm chair without armrest (curve +2.6 pt spike at 0:48)", "1:40 YOUR AGE + SEX GROUP; caption: reference for somebody who is 80 is different", "2:30 THE GOAL is not HIGHEST SCORE; caption: maintain strength and endurance for activities of daily living", "2:54 10-SECOND BALANCE teaser; caption: watch my next video"],
        "opening": "Direct second-person test question in the first two seconds.",
        "visuals": "Seated study shot with numbered setup cards and kinetic keywords.",
        "editing": "Instruction-led: setup, how to score, interpretation, then next-video teaser.",
        "closing": "Teases the balance-test video (VrbLuTNi0qE).",
        "possible_explanation": "A participatory test the viewer can perform gives a concrete reason to stay; 30-second retention 59.74% versus 41.12%, end 22.08% versus 14.95%.",
        "alternative_explanation": "Derived APV is lower (22.2% vs 29.2%), so the advantage is concentrated early; audience and traffic mix differ.",
    },
    "VrbLuTNi0qE": {
        "duration_seconds": 238,
        "comparison": "Mobility-test long-form: weaker versus t1j-p9pkw3Y",
        "timestamps": ["0:02 seated doctor, same study set, circular 10 icon; caption: The 10 second balance test that every senior should (curve -11.2 pts at 0:02)", "0:07 inset of a person standing on one leg; caption: one leg for 10 seconds without losing your balance? (curve -10.3 pts at 0:07)", "0:12 BALANCE = HEALTH SIGNAL card; caption: doctors and researchers discovered balance can reveal important clues (curve -6.5 pts)", "0:31 no overlay; caption: [Dr. Rehan] Omar, consultant cardiologist (credential intro coincides with -4.7 pt dip)", "0:50 caption: how multiple systems in your body work together (curve -4.7 pts)", "2:00 caption: comfortably hold position for about 10 seconds", "3:00 MOVE CONFIDENTLY card; caption: these habits can improve stability", "3:52 SUBSCRIBE button with like icon"],
        "opening": "Names the test and shows it by 0:07, but then shifts to research framing and a credential introduction before the how-to.",
        "visuals": "Same set as t1j-p9pkw3Y; demo inset and summary cards.",
        "editing": "Explanation-led; how-to arrives near 2:00.",
        "closing": "Subscribe card.",
        "possible_explanation": "Heavy early losses at 0:02 and 0:07 happen despite a demo inset; the credential intro at 0:31 again coincides with a dip, as in 5oPzZjfNgII at 0:27.",
        "alternative_explanation": "Views are small (109), and a longer runtime spreads the same audience thinner.",
    },
}
PRIORITY_PLAYBACK.update(SEEK_SAMPLED)


# Records whose anchors were added on 2026-09-28 by muted seek-and-inspect (frames viewed, captions read on screen; audio not heard).
GAP_FILLED = {"-SjQc2MwaOU", "HEJoPEEndG8", "5oPzZjfNgII", "EB3_A2b4a6o", "BCNWQ3uuSuE", "SBrMW71O69U"}


THUMBNAIL_REVALIDATIONS = {
    "QfRaG71ZA_0": "Vertical staged skeleton with coffee, large PALPITATIONS/ANXIETY/COFFEE text and wide brown side bars; dramatic but not a doctor frame.",
    "4ByUo2N_C-I": "Vertical composite: Dr. Rehan in white coat, oversized coffee cup, WRONG QUESTION, and three small BP/heart/cups icons.",
    "FVfG_HZV4qg": "Vertical direct-to-camera office frame with only START; doctor and gesture dominate, with muted red side bars.",
    "kF26QB7xHiE": "Warm orange vertical frame; IT PREDICTS and HEART are separated by the doctor and a cartoon heart, weakening one-pass readability.",
    "PTB-6fgaAKk": "Vertical vascular anatomy figure with one compact SLOW BLOOD FLOW warning; no doctor face and wide gray side bars.",
    "gunPgSlxJLA": "Vertical seated doctor frame with FEET FEEL IT FIRST and snowflake; simple but visually dark with wide side bars.",
    "-SjQc2MwaOU": "Vertical doctor frame with heart and warning icons; a sentence-length subtitle sits at the bottom and is small at mobile scale.",
    "HEJoPEEndG8": "Vertical doctor frame with a generic fatigued-man cutout and sentence caption; the cutout competes with the doctor.",
    "5oPzZjfNgII": "16:9 AM-versus-PM ankle comparison, large WORSE BY EVENING text and doctor in scrubs; symptom difference is immediately visible.",
    "EB3_A2b4a6o": "16:9 glucose meter reading 168, empty plate, NO FOOD text and doctor; the numeric contradiction is explicit.",
    "BCNWQ3uuSuE": "16:9 lipid-profile card with LDL/HDL/triglycerides, WHICH NUMBER MATTERS and doctor; strongest topic specificity in the pair.",
    "SBrMW71O69U": "16:9 doctor holding a lipid profile marked HIGH with READ THIS FIRST; legible but broader than the paired exact-number question.",
}


MATCHED_COMPARISONS = [
    {"pair": "Coffee Shorts", "stronger_id": "QfRaG71ZA_0", "comparison_id": "4ByUo2N_C-I", "evidence": "Stayed 57.3% vs 43.7%; APV 83.3% vs 43.8%; 30-second retention 67.8% vs 39.62%.", "interpretation": "Specific symptom-plus-trigger framing is a plausible contributor, not a proven cause."},
    {"pair": "Walking Shorts", "stronger_id": "FVfG_HZV4qg", "comparison_id": "kF26QB7xHiE", "evidence": "Stayed 51.1% vs 27.0%; APV 53.7% vs 59.8%; views 1,068 vs 1,212.", "interpretation": "Clearer feed acceptance did not equal more views; distribution and completion are separate stages."},
    {"pair": "Cold-feet Shorts", "stronger_id": "gunPgSlxJLA", "comparison_id": "PTB-6fgaAKk", "evidence": "Stayed 28.7% vs 16.9%; APV 84.0% vs 126.6%.", "interpretation": "Replay above 100% can coexist with weak swipe acceptance."},
    {"pair": "Heart-failure Shorts", "stronger_id": "-SjQc2MwaOU", "comparison_id": "HEJoPEEndG8", "evidence": "Stayed 20.6% vs 13.3%; APV 52.1% vs 28.0%; 30-second retention 35.19% vs 16.0%.", "interpretation": "Both openings are weak in feed terms; concrete shortness-of-breath framing retains more of those who stay."},
    {"pair": "Symptom vs metabolic long-form", "stronger_id": "5oPzZjfNgII", "comparison_id": "EB3_A2b4a6o", "evidence": "CTR 4.7% vs 1.8%; actual APV 44.1% vs 29.0%; end retention 20.0% vs 13.57%.", "interpretation": "Shorter duration and concrete symptom progression are plausible contributors; topic and source mix remain confounded."},
    {"pair": "Heart-attack Shorts (same footage)", "stronger_id": "YVjbjcVo1is", "comparison_id": "iltS1TPt4jo", "evidence": "30-second retention 45.16% vs 20.59%; APV 21.2% vs 14.2%; stayed 33.7% vs 37.7%; views 85 vs 87.", "interpretation": "Closest natural experiment in the set: same doctor footage, re-edited with an illustrated cold open, banner and raw caption timecodes. Better swipe acceptance but worse holding; tiny samples."},
    {"pair": "Coffee Shorts II", "stronger_id": "fArHBQo6Ggw", "comparison_id": "tD4KOpsJH_c", "evidence": "30-second retention 52.23% vs 23.08%; APV 29.2% vs 21.9%; stayed 46.7% vs 48.7%; views 341 vs 87.", "interpretation": "Similar feed acceptance; audience-qualifier plus numbered open loop held viewers better than an answer-first opener."},
    {"pair": "Cholesterol Shorts", "stronger_id": "qbwCkH_GqhU", "comparison_id": "TPVOIfcJl-k", "evidence": "30-second retention 39.47% vs 18.52%; end 19.74% vs 3.7%; stayed 38.6% vs 31.4%; views 199 vs 77.", "interpretation": "Patient-problem story with checklist payoff versus a textbook definition opener; setting and title also differ."},
    {"pair": "Mobility-test long-form", "stronger_id": "t1j-p9pkw3Y", "comparison_id": "VrbLuTNi0qE", "evidence": "30-second retention 59.74% vs 41.12%; end 22.08% vs 14.95%; derived APV 22.2% vs 29.2%; views 160 vs 109.", "interpretation": "Participatory how-to opener held more early viewers than a research-framed opener with credential intro; later APV favours the weaker video, so the effect is early-only."},
    {"pair": "Cholesterol long-form", "stronger_id": "BCNWQ3uuSuE", "comparison_id": "SBrMW71O69U", "evidence": "CTR 4.2% vs 2.87%; 30-second retention 60.5% vs 38.46%; subscribers +2 vs 0.", "interpretation": "Specific lab-test utility is the leading package hypothesis, not causal proof."},
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def csv_rows_from_zip(path: Path, member: str) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as zf:
        text = zf.read(member).decode("utf-8-sig")
    return list(csv.DictReader(text.splitlines()))


def fnum(v: str | None) -> float:
    try:
        return float(v or 0)
    except ValueError:
        return 0.0


def build_studio() -> tuple[dict, dict[str, dict]]:
    periods = {}
    lifetime_by_id = {}
    for slug in ["last-28-days", "last-90-days", "lifetime"]:
        path = STUDIO_DIR / f"studio-advanced-content-{slug}.zip"
        rows = csv_rows_from_zip(path, "Table data.csv")
        total, videos = rows[0], rows[1:]
        periods[slug] = {
            "archive": str(path.relative_to(ROOT)), "sha256": sha256(path),
            "views": int(fnum(total.get("Views"))), "watch_hours": fnum(total.get("Watch time (hours)")),
            "subscribers": int(fnum(total.get("Subscribers"))), "thumbnail_impressions": int(fnum(total.get("Thumbnail impressions"))),
            "thumbnail_ctr_percent": fnum(total.get("Thumbnail click-through rate (%)")), "video_rows": len(videos),
        }
        if slug == "lifetime":
            for row in videos:
                views, hours, duration = int(fnum(row.get("Views"))), fnum(row.get("Watch time (hours)")), int(fnum(row.get("Duration")))
                avd = hours * 3600 / views if views else 0
                lifetime_by_id[row["Content"].strip()] = {
                    "views": views, "watch_hours": hours, "subscribers": int(fnum(row.get("Subscribers"))),
                    "impressions": int(fnum(row.get("Thumbnail impressions"))), "ctr_percent": fnum(row.get("Thumbnail click-through rate (%)")),
                    "duration_seconds": duration, "average_view_duration_seconds_derived": round(avd, 1),
                    "average_percentage_viewed_derived": round(100 * avd / duration, 1) if duration else None,
                }
    traffic_path = STUDIO_DIR / "studio-advanced-traffic-source-lifetime.zip"
    traffic_rows = csv_rows_from_zip(traffic_path, "Table data.csv")
    periods["traffic-source-lifetime"] = {"archive": str(traffic_path.relative_to(ROOT)), "sha256": sha256(traffic_path), "rows": traffic_rows[1:]}
    studio = {
        "dataset_id": "DS-000032", "channel_id": "UCQIzqH7QZ9viBYpOFqgSXMg", "obtained_at": "2026-09-27",
        "source": "YouTube Studio Advanced Mode authenticated read-only manager session", "account_role_observed": "Manager",
        "periods": periods, "limits": ["Per-video retention exports are stored separately; some curves may be blank when Studio does not disclose rows", "Derived average view duration and percentage use exported views, watch hours and duration; YouTube rounding may cause small error"],
    }
    return studio, lifetime_by_id


def build_trends() -> dict:
    files = {}
    for path in sorted(TRENDS_DIR.glob("*.csv")):
        lines = path.read_text().splitlines()
        rows = list(csv.DictReader(lines[2:]))
        series = {}
        for col in rows[0].keys():
            if col == "Week":
                continue
            vals = [int(r[col]) for r in rows if r[col] and r[col] != "<1"]
            series[col] = {"mean": round(statistics.mean(vals), 2), "median": round(statistics.median(vals), 2), "max": max(vals), "weeks": len(rows)}
        files[path.name] = {"configuration": {"geography": "United States", "property": "YouTube Search", "range": "Past 5 years", "category": "All categories"}, "series": series}
    out = {"obtained_at": "2026-09-27", "source": "Official Google Trends CSV downloads", "files": files,
           "interpretation_limits": ["Scores normalized 0-100 within each comparison; not absolute volume", "Do not infer view causation without traffic-source and query evidence", "Lp a broad query is ambiguous; lipoprotein a series is preferred"]}
    return out


def thumbnail_observation(rec: dict) -> dict:
    vid, typ, title = rec["id"], rec["type"], rec["title"]
    text = VISIBLE_TEXT[vid]
    short_frame = typ == "shorts" and vid in {"-SjQc2MwaOU", "FDLU7tX7qNM", "FVfG_HZV4qg", "HEJoPEEndG8", "gunPgSlxJLA", "hUSVbcHVeVw", "j9VqMB6yTXQ", "kF26QB7xHiE", "nP9fDHP1jbo", "nPqrcrxdrdE"}
    return {
        "visible_text": text,
        "text_readability": "Low: sentence-length in-frame caption" if len(text) > 62 else ("Medium: small UI/secondary text" if len(text) > 35 else "High: short, bold question/claim"),
        "composition": (f"{vid}: vertical source frame centered with side bars; '{text}' occupies the narrow mobile-safe column" if typ == "shorts" else f"{vid}: headline '{text}' shares 16:9 frame with doctor and topic-specific object/scene"),
        "subject_and_imagery": (f"Frame for '{title}' shows in-video doctor/illustration rather than a separately staged thumbnail" if short_frame else f"Staged doctor-led illustration visualizes the promise in '{title}'"),
        "medical_authority_cues": f"{vid} uses Dr. Rehan, clinical clothing/stethoscope or a diagnostic visual tied to '{text}'.",
        "color_and_contrast": f"{vid} uses high-contrast white/yellow/red hook text against dark or muted field; legibility varies with '{text}' length.",
        "focal_point": (f"'{text}' and central vertical subject" if typ == "shorts" else f"'{text}', then doctor face and topic prop"),
        "visual_hierarchy": (f"{vid}: vertical frame and side bars reduce hierarchy; caption competes with subject" if short_frame else f"{vid}: hook text leads, doctor/prop supports, secondary labels explain"),
        "title_relationship": f"Thumbnail phrase '{text}' compresses '{title}' but does not itself establish the medical outcome.",
        "intended_audience": f"Audience signaled by '{title}': older adults, caregivers, or viewers managing the named heart/metabolic concern.",
        "curiosity_and_disclosure": f"'{text}' creates the open loop; title supplies the specific context. Disclosure is {'thin' if len(text) < 8 else 'topic-specific'}.",
        "competitor_comparison": f"{vid} uses clinician authority and explicit problem imagery; within this channel it competes with many similar doctor-plus-hook layouts, so '{text}' carries most differentiation.",
    }


def live_studio_observation(video_id: str) -> dict | None:
    values = LIVE_STUDIO_METRICS.get(video_id)
    if not values:
        return None
    engaged, avd, apv, stayed, gained = values
    return {
        "observed_at": "2026-09-28",
        "reporting_period": "Lifetime since upload through authenticated observation date",
        "source": "Authenticated YouTube Studio Advanced Mode read-only table observation",
        "source_file": None,
        "engaged_views": engaged,
        "average_view_duration_seconds_actual": avd,
        "average_percentage_viewed_actual": apv,
        "stayed_to_watch_percent": stayed,
        "swiped_away_percent": round(100 - stayed, 1) if stayed is not None else None,
        "subscribers_gained": gained,
        "limitation": "Browser-observed row; CSV export did not complete. Retained 2026-09-27 ZIP remains the file-backed source for views, watch time, impressions and CTR.",
    }


def retention_investigation(video_id: str, retention_record: dict | None) -> dict:
    if not retention_record or retention_record.get("curve_status") != "AVAILABLE":
        return {
            "status": "UNAVAILABLE_EXPORTED_NO_CURVE",
            "content_linkage": "NOT_AVAILABLE",
            "limitation": "Studio export contained no disclosed retention rows; no curve interpretation was manufactured.",
        }
    priority = video_id in PRIORITY_PLAYBACK
    return {
        "status": "CONTENT_LINKED_COMPLETE" if priority else "CURVE_PROFILE_COMPLETE_CONTENT_LINK_PENDING",
        "content_linkage": ("SEEK_SAMPLED_PLAYBACK" if video_id in SEEK_SAMPLED else "REPORTED_FULL_PLAYBACK") if priority else "NOT_PLAYBACK_VERIFIED",
        "retention_at_3_seconds_percent": retention_record.get("retention_at_3_seconds_percent"),
        "retention_at_5_seconds_percent": retention_record.get("retention_at_5_seconds_percent"),
        "retention_at_30_seconds_percent": retention_record.get("retention_at_30_seconds_percent"),
        "retention_at_midpoint_percent": retention_record.get("retention_at_midpoint_percent"),
        "retention_at_end_percent": retention_record.get("retention_at_end_percent"),
        "major_dips": retention_record.get("largest_step_dips", []),
        "major_spikes": retention_record.get("largest_step_spikes", []),
        "possible_explanation": PRIORITY_PLAYBACK.get(video_id, {}).get("possible_explanation"),
        "alternative_explanation": PRIORITY_PLAYBACK.get(video_id, {}).get("alternative_explanation"),
        "limitation": (
            "Curve events were linked to observed frames and captions at those timestamps; dips remain associative, not causal."
            if priority else
            "Numeric curve profile complete, but individual dip/spike meaning remains open until content at those timestamps is playback-verified."
        ),
    }


def audience_segments(video_id: str, retention_record: dict | None) -> dict | None:
    """Segment curves already inside the retained per-video retention export (no new Studio access)."""
    path = STUDIO_DIR / "audience-retention-by-video" / f"{video_id}.zip"
    if not path.exists():
        return None
    with zipfile.ZipFile(path) as zf:
        def rows(member):
            return [r for r in csv.reader(zf.read(member).decode("utf-8-sig").splitlines())][1:] if member in zf.namelist() else []
        new_ret, organic, paid, subscribed = rows("New and returning viewers.csv"), rows("Organic.csv"), rows("Organic and paid traffic.csv"), rows("Subscribers and non-subscribers.csv")
    p30 = (retention_record or {}).get("retention_30_seconds_source_position_percent")
    def at(segment, pos):
        vals = [fnum(r[2]) for r in new_ret if r[1] == segment and int(fnum(r[0])) == pos]
        return vals[0] if vals else None
    rel = {int(fnum(r[0])): fnum(r[2]) for r in organic if len(r) == 3 and r[2] != ""}
    return {
        "source_export": str(path.relative_to(ROOT)),
        "provenance": "Retained Studio audience-retention export (2026-09-27); segment curves, not viewer counts.",
        "traffic_types_present": sorted({r[1] for r in paid if len(r) == 3}),
        "subscription_segments_present": sorted({r[1] for r in subscribed if len(r) == 3}),
        "new_vs_returning_available": bool({r[1] for r in new_ret} >= {"New viewers", "Returning viewers"}),
        "new_viewers_retention_at_30s_position": at("New viewers", p30) if p30 is not None else None,
        "returning_viewers_retention_at_30s_position": at("Returning viewers", p30) if p30 is not None else None,
        "new_viewers_retention_at_end": at("New viewers", 99),
        "returning_viewers_retention_at_end": at("Returning viewers", 99),
        "compared_to_other_videos_at_30s_position_as_exported": rel.get(p30) if p30 is not None else None,
        "compared_to_other_videos_at_end_as_exported": rel.get(99),
    }


INVESTIGATION_STATUS_DEFINITIONS = {
    "NOT_STARTED": "No canonical metadata or transcript joined.",
    "TRANSCRIPT_ONLY": "Metadata, transcript and thumbnail joined; no saved playback record.",
    "PARTIAL_PLAYBACK": "Saved playback record exists but lacks numeric m:ss anchors, or long-form has fewer than one anchor per 60 seconds.",
    "PLAYBACK_COMPLETE": "Saved playback record with numeric anchors from 0:00 to end and adequate coverage.",
    "EDITING_AUDIT_COMPLETE": "PLAYBACK_COMPLETE plus specific opening, visuals, editing and closing observations.",
    "RETENTION_ANALYZED": "Numeric anchors meeting the coverage rule, read against an exported retention curve. Does not by itself prove continuous playback: playback_audit.status says whether anchors came from reported full playback or seek-sampling at curve events.",
    "LIMITED_BY_UNAVAILABLE_EVIDENCE": "EDITING_AUDIT_COMPLETE but Studio disclosed no retention curve; cannot advance further.",
}


def investigation_status(video_id: str, retention_record: dict | None) -> tuple[str, str | None]:
    item = PRIORITY_PLAYBACK.get(video_id)
    if not item:
        return "TRANSCRIPT_ONLY", None
    stamps = item["timestamps"]
    numeric = all(s.split(" ", 1)[0].count(":") == 1 and s.split(" ", 1)[0].replace(":", "").isdigit() for s in stamps)
    enough = len(stamps) >= max(3, -(-item["duration_seconds"] // 60))
    if not numeric:
        return "PARTIAL_PLAYBACK", "Saved timestamps are descriptive, not numeric m:ss anchors; re-inspect only the unanchored segments."
    if not enough:
        return "PARTIAL_PLAYBACK", f"{len(stamps)} anchors for {item['duration_seconds']}s long-form; add mid-video anchors at each retention dip."
    if not retention_record or retention_record.get("curve_status") != "AVAILABLE":
        return "LIMITED_BY_UNAVAILABLE_EVIDENCE", "No exported retention curve."
    return "RETENTION_ANALYZED", None


def playback_audit(video_id: str) -> dict | None:
    item = PRIORITY_PLAYBACK.get(video_id)
    if not item:
        return None
    sampled = video_id in SEEK_SAMPLED
    return {
        "status": "SEEK_SAMPLED_AT_RETENTION_EVENTS" if sampled else "REPORTED_FULL_PLAYBACK",
        "full_editing_audit_status": "SAMPLED_FRAMES_ONLY" if sampled else "COMPLETE_WITH_AUDIO_LIMITATION",
        "observed_at": "2026-09-28",
        "source": f"https://www.youtube.com/watch?v={video_id}",
        "playback_speed": "muted seeks; about 1.8 s of playback at each anchor" if sampled else "2x for long-form; normal/player speed for Shorts",
        "completion_evidence": (
            "Not watched continuously. Frames viewed and on-screen captions read at each listed anchor, chosen from exported retention events plus coverage points to the end."
            if sampled else
            f"Previous session reported the HTML5 player reached {item['duration_seconds']} seconds (text record only, no saved player capture)"
            + (" ; 2026-09-28 gap-fill: muted seek-and-inspect frames at listed anchors, captions read on screen" if video_id in GAP_FILLED else "")
        ),
        "comparison": item["comparison"],
        "timestamps": item["timestamps"],
        "opening_presentation": item["opening"],
        "doctor_delivery": "Direct clinician explanation with visible gestures; delivery content was reviewed with captions/transcript.",
        "speech_clarity_and_pacing": "Speech sequence was intelligible through player captions; precise vocal prosody was not independently scored.",
        "camera_framing": item["visuals"],
        "audio": "Muted; audio not heard. Speech content is taken from on-screen captions at each anchor." if sampled else "Playback completed, but no isolated headphone/loudness/noise measurement was made.",
        "b_roll_and_medical_visuals": item["visuals"],
        "on_screen_typography": THUMBNAIL_REVALIDATIONS.get(video_id, "Thumbnail not revalidated in this batch; see thumbnail_observation."),
        "editing_rhythm": item["editing"],
        "visual_variety": item["editing"],
        "narrative_progression": item["opening"] + " " + item["closing"],
        "repetition": "No repeated segment was counted as a causal retention factor; loop behavior is noted where APV exceeded 100%.",
        "medical_claims": "Claims were recorded as presented; this playback audit does not independently validate clinical correctness.",
        "closing_structure": item["closing"],
        "possible_explanation": item["possible_explanation"],
        "alternative_explanation": item["alternative_explanation"],
        "limitations": "Association only. Traffic source, audience cohort and publication context remain uncontrolled; audio was not instrument-tested.",
    }


def main() -> None:
    data = json.loads(DATASET.read_text())
    thumbs = json.loads(THUMB_MANIFEST.read_text())
    thumb_by_id = {r["video_id"]: r for r in thumbs["records"]}
    studio, studio_by_id = build_studio()
    retention = json.loads(RETENTION_ANALYSIS.read_text())
    retention_by_id = {record["video_id"]: record for record in retention["records"]}
    trends = build_trends()
    records = []
    for rec in data:
        vid = rec["id"]
        image = thumb_by_id[vid]
        retention_record = retention_by_id.get(vid)
        audit = playback_audit(vid)
        observation = thumbnail_observation(rec)
        if vid in THUMBNAIL_REVALIDATIONS:
            observation["revalidation_observation"] = THUMBNAIL_REVALIDATIONS[vid]
            observation["quality_status"] = "REVALIDATED_PRIORITY_2026-09-28"
        else:
            observation["quality_status"] = "COMPLETE_NEEDS_CORRECTION_TEMPLATED_COMMENTARY"
            observation["quality_limitation"] = "Image identity is verified, but several analytical fields were generated from a repeated template and were not re-certified in this pass."
        status, status_gap = investigation_status(vid, retention_record)
        remaining = [status_gap] if status_gap else []
        if not audit:
            remaining.append("Full playback and detailed editing audit")
        elif vid in SEEK_SAMPLED:
            remaining.append("Seek-sampled only: continuous playback and audio not verified")
        if not retention_record or retention_record.get("curve_status") != "AVAILABLE":
            remaining.append("Retention curve unavailable because Studio disclosed no rows")
        elif not audit:
            remaining.append("Retention timestamps not yet linked to actual playback")
        if vid not in LIVE_STUDIO_METRICS:
            remaining.append("Extended Studio row metrics not captured in the authenticated visible table")
        if vid not in THUMBNAIL_REVALIDATIONS:
            remaining.append("Thumbnail commentary quality revalidation")
        records.append({
            "video_id": vid,
            "title_at_acquisition": rec["title"],
            "type": rec["type"],
            "published_at": rec["date"],
            "public_url": rec["url"],
            "canonical_metadata": "VERIFIED_COMPLETE",
            "actual_description": "VERIFIED_COMPLETE",
            "original_transcript": "VERIFIED_COMPLETE",
            "transcript_analyzed": "STRUCTURAL_ANALYSIS_REUSED",
            "transcript_path": f"data/raw/competitors/DS-000032/apify/KgQRSlx1CGL0OKq7Q/transcripts/{vid}.txt",
            "thumbnail_url": "VERIFIED_COMPLETE",
            "actual_thumbnail_image": "VERIFIED_COMPLETE",
            "thumbnail_image_path": image["local_path"],
            "thumbnail_visually_inspected": "COMPLETE",
            "thumbnail_inspection_status": observation["quality_status"],
            "thumbnail_observation": observation,
            "public_watch_page_accessible": "VERIFIED_PUBLIC_2026-09-28" if audit else "PUBLIC_URL_REGISTERED_NOT_REPLAYED_THIS_PASS",
            "playback_inspected": audit["status"] if audit else "NOT_STARTED",
            "video_actually_reviewed": audit["status"] if audit else "NOT_COMPLETE",
            "full_editing_audit_complete": audit["full_editing_audit_status"] if audit else "NOT_STARTED",
            "editing_observations_recorded": audit["full_editing_audit_status"] if audit else "NOT_COMPLETE",
            "playback_audit": audit,
            "investigation_status": status,
            "google_trends_research": "TOPIC_LEVEL_VERIFIED_COMPLETE",
            "external_competitor_comparison": "REUSED_EXISTING_EVIDENCE",
            "relevant_private_studio_analytics": "LIFETIME_BASIC_ROW_VERIFIED" if vid in studio_by_id else "NO_ROW_IN_EXPORT",
            "studio_metrics": studio_by_id.get(vid),
            "studio_metrics_actual_observation": live_studio_observation(vid),
            "per_video_traffic_source_detail": "NOT_EXPORTED",
            "retention_evidence": retention_record,
            "retention_curve": retention_record.get("curve_status", "NOT_EXPORTED") if retention_record else "NOT_EXPORTED",
            "retention_audience_segments": audience_segments(vid, retention_record),
            "retention_investigation": retention_investigation(vid, retention_record),
            "remaining_gap": "; ".join(remaining) if remaining else "None within recovered evidence",
            "user_action_required": "No for public playback; authenticated Studio source table would be required for uncaptured extended rows and audience reports",
        })
    register = {
        "schema_version": "2.0", "generated_at": datetime.now(timezone.utc).isoformat(), "dataset_id": "DS-000032", "channel_id": "UCQIzqH7QZ9viBYpOFqgSXMg",
        "retained_acquisition_observed_at": "2026-09-25T10:45:45.525Z", "public_catalog_observed_at": "2026-09-28",
        "counts": {
            "videos": len(records),
            "regular": sum(r["type"] == "video" for r in records),
            "shorts": sum(r["type"] == "shorts" for r in records),
            "descriptions": sum(bool(r.get("text")) for r in data),
            "transcripts": sum((ROOT / f"data/raw/competitors/DS-000032/apify/KgQRSlx1CGL0OKq7Q/transcripts/{r['id']}.txt").exists() for r in data),
            "thumbnail_urls": sum(bool(r.get("thumbnailUrl")) for r in data),
            "thumbnail_images": len(thumb_by_id),
            "thumbnail_visual_inspections": len(thumb_by_id),
            "thumbnail_priority_revalidations": len(THUMBNAIL_REVALIDATIONS),
            "studio_basic_rows": sum(r["video_id"] in studio_by_id for r in records),
            "studio_extended_rows_observed": sum(r["video_id"] in LIVE_STUDIO_METRICS for r in records),
            "retention_exports": retention["available_count"],
            "retention_curves": retention["curve_available_count"],
            "retention_content_linked_investigations": sum(r["retention_investigation"]["status"] == "CONTENT_LINKED_COMPLETE" for r in records),
            "playback_reported_full": sum(r["playback_inspected"] == "REPORTED_FULL_PLAYBACK" for r in records),
            "playback_seek_sampled": sum(r["playback_inspected"] == "SEEK_SAMPLED_AT_RETENTION_EVENTS" for r in records),
            "retention_new_vs_returning_split": sum(bool((r["retention_audience_segments"] or {}).get("new_vs_returning_available")) for r in records),
            "editing_audits_detailed": sum(r["full_editing_audit_complete"] == "COMPLETE_WITH_AUDIO_LIMITATION" for r in records),
            "matched_comparisons": len(MATCHED_COMPARISONS),
            "new_public_videos": 0,
            "investigation_status": {k: sum(r["investigation_status"] == k for r in records) for k in INVESTIGATION_STATUS_DEFINITIONS},
        },
        "investigation_status_definitions": INVESTIGATION_STATUS_DEFINITIONS,
        "matched_comparisons": MATCHED_COMPARISONS,
        "records": records,
    }
    checkpoint = {
        "schema_version": "2.0",
        "project": "Decode Your Heart forensic audit",
        "as_of": "2026-09-28",
        "branch": "research/senior-health-acquisition-phase-2",
        "starting_head": "31ea9a53a6b4c9a1b74a3478ce16e510fdf06e10",
        "overall_status": "PARTIALLY_COMPLETE",
        "exact_next_unfinished_task": "Batch 4: seek-sample the next matched pairs among the 36 TRANSCRIPT_ONLY videos, starting with Ozempic long-form (8JdBlF-ragM vs sUL6SU8LnEg), circulation long-form (KPYHy7MDmLM vs NznebmgFwXI), artery-food Short vs long-form (hUSVbcHVeVw vs CZ3gAUzdTAg) and ankle/calf Shorts (FDLU7tX7qNM vs p_iI0enaFX8); then the remaining no-curve videos as LIMITED_BY_UNAVAILABLE_EVIDENCE.",
        "batch_history": [
            {"batch": "Batch 1 Recovery and Analytics", "status": "COMPLETE_WITH_LIMITATIONS", "saved_at": "2026-09-28", "result": "Four original Studio ZIPs verified; 56 basic per-video rows joined; 47 extended rows observed; missing Short resolved."},
            {"batch": "Batch 2 Retention and Actual Playback", "status": "PARTIAL", "saved_at": "2026-09-28", "result": "56 retention exports, 46 curves; 12 saved playback records, of which 8 meet RETENTION_ANALYZED and 4 long-form records are PARTIAL_PLAYBACK (too few numeric anchors); 44 TRANSCRIPT_ONLY. -SjQc2MwaOU and HEJoPEEndG8 anchors gap-filled 2026-09-28."},
            {"batch": "Batch 2b Partial playback gap-fill", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "5oPzZjfNgII, EB3_A2b4a6o, BCNWQ3uuSuE and SBrMW71O69U given numeric anchors at every exported retention event (7-11 anchors each) by muted seek-and-inspect; all four now RETENTION_ANALYZED."},
            {"batch": "Batch 3b Matched pairs (seek-sampled)", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "8 TRANSCRIPT_ONLY videos in 4 matched pairs seek-sampled at retention events: YVjbjcVo1is/iltS1TPt4jo (same footage, re-edited), fArHBQo6Ggw/tD4KOpsJH_c, qbwCkH_GqhU/TPVOIfcJl-k, t1j-p9pkw3Y/VrbLuTNi0qE. Audience-segment curves summarized from retained exports for all 56."},
            {"batch": "Batch 3 Research Diagnosis and Deliverables", "status": "COMPLETE_FOR_AVAILABLE_SYNTHESIS", "saved_at": "2026-09-28", "result": "Three Trends comparisons verified; six matched comparisons synthesized; diagnosis and four existing deliverables reconciled."},
        ],
        "execution_matrix": [
            {"task": "Metadata", "previous_result": "56 records", "current_evidence": "56 exact canonical Video IDs; current public catalog still 56 on 2026-09-28", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Transcripts", "previous_result": "56", "current_evidence": "56 original transcript files present", "status": "VERIFIED_COMPLETE", "required_action": "Reuse; do not reread wholesale"},
            {"task": "Thumbnails", "previous_result": "56", "current_evidence": "56 images identity-verified; 12 priority observations revalidated; 44 contain templated commentary", "status": "COMPLETE_NEEDS_CORRECTION", "required_action": "Revalidate remaining 44 only when they enter a priority comparison"},
            {"task": "Studio reports", "previous_result": "Four reported", "current_evidence": "Lifetime, 90d, 28d and traffic-source ZIP hashes verified", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Individual Analytics", "previous_result": "55 references reported", "current_evidence": "56 file-backed basic rows; 47 authenticated extended rows; 9 extended rows not captured", "status": "PARTIAL", "required_action": "Capture remaining extended rows only if Studio table/export becomes reliable"},
            {"task": "Retention", "previous_result": "Previously missing", "current_evidence": f"56 exports; 46 curves; {register['counts']['retention_content_linked_investigations']} content-linked investigations; 10 no-curve disclosures; {register['counts']['retention_new_vs_returning_split']} exports carry a new-vs-returning split", "status": "PARTIAL", "required_action": "Link remaining 34 curves during playback; no action possible for 10 blank curves"},
            {"task": "Playback", "previous_result": "Previously missing", "current_evidence": f"{register['counts']['playback_reported_full']} reported full-playback records (text-only completion evidence) and {register['counts']['playback_seek_sampled']} seek-sampled records", "status": "PARTIAL", "required_action": f"Audit remaining {register['counts']['investigation_status']['TRANSCRIPT_ONLY']} TRANSCRIPT_ONLY videos"},
            {"task": "Trends", "previous_result": "Three comparisons", "current_evidence": "Three original official CSVs and configurations verified", "status": "VERIFIED_COMPLETE", "required_action": "No repeat query justified by available source detail"},
            {"task": "Research synthesis", "previous_result": "Partial", "current_evidence": "Six matched comparisons and multi-stage diagnosis complete; audience/query/device/geography gaps remain", "status": "PARTIAL", "required_action": "Revisit only if unavailable Studio reports become accessible"},
        ],
        "phase_status": {
            "repository_recovery": "VERIFIED_COMPLETE",
            "thumbnail_recovery_and_visual_inspection": "COMPLETE_NEEDS_CORRECTION",
            "public_catalog_refresh": "VERIFIED_COMPLETE",
            "video_playback_forensics": f"PARTIAL_{register['counts']['investigation_status']['RETENTION_ANALYZED']}_ANALYZED_{register['counts']['investigation_status']['PARTIAL_PLAYBACK']}_PARTIAL_OF_56",
            "retention_investigations": f"PARTIAL_{register['counts']['retention_content_linked_investigations']}_CONTENT_LINKED_10_NO_CURVE",
            "google_trends": "VERIFIED_COMPLETE",
            "youtube_studio_exports": "VERIFIED_COMPLETE_ORIGINAL_EXPORTS",
            "video_level_studio_metrics": "PARTIAL_56_BASIC_47_EXTENDED",
            "growth_diagnosis": "UPDATED_EVIDENCE_BACKED",
            "four_artifacts": "UPDATED_IN_PLACE",
        },
        "verified_counts": register["counts"],
        "studio": studio,
        "studio_live_observation": {
            "observed_at": "2026-09-28",
            "access": "Authenticated read-only manager session for canonical channel",
            "channel_totals": {"views": 8366, "watch_hours": 45.6, "net_subscribers": 33, "subscribers_gained": 34, "impressions": 36159, "ctr_percent": 3.0, "engaged_views": 3999, "average_view_duration_seconds_actual": 39, "average_percentage_viewed_actual": 37.3, "stayed_to_watch_percent": 36.0},
            "extended_video_rows_observed": len(LIVE_STUDIO_METRICS),
            "extended_video_rows_not_captured": len(records) - len(LIVE_STUDIO_METRICS),
            "missing_short_status": "RESOLVED",
            "missing_short_metrics": {"video_id": "-SjQc2MwaOU", "views": 233, "engaged_views": 54, "average_view_duration_seconds_actual": 23, "average_percentage_viewed_actual": 52.1, "stayed_to_watch_percent": 20.6, "swiped_away_percent": 79.4, "impressions": 338, "ctr_percent": 1.2, "subscribers_gained": 0},
            "unavailable_reports": ["Per-video search queries", "Per-video suggested-video sources", "Geography", "Device", "Viewers across formats", "New/returning viewer counts (retention-by-segment curves are available in the retained exports; counts are not)"],
            "availability_note": "New/returning/unique viewer cells displayed em dash in the inspected content table; this is unavailability, not a measured zero.",
        },
        "trends": trends,
        "matched_comparisons": MATCHED_COMPARISONS,
        "knowledge_framework_applications": {
            "status": "REUSED_EXISTING_MAPPINGS",
            "count": 12,
            "source_table": "Forensic report section 9 mapping table",
            "guardrail": "DS-000018 creator claims remain mixed reliability; official YouTube documentation overrides conflicting blanket claims.",
        },
        "diagnosis": [
            {"finding": "Distribution opportunity is limited and uneven", "video_ids": ["CZ3gAUzdTAg", "EB3_A2b4a6o", "BCNWQ3uuSuE"], "metrics": "36,159 lifetime counted impressions across 56 videos; Suggested 19,841, Search 11,245 and Browse 4,028 impressions", "visual_and_transcript_evidence": "No single production pattern explains the source mix", "comparative_evidence": "Some videos still received thousands of impressions", "historical_context": "Lifetime through 2026-09-27", "counterexample": "Low impressions can coexist with high CTR on a narrow loyal audience", "alternative_explanations": "Topic demand, audience size, eligibility and competition", "confidence": "HIGH for limited recorded reach; LOW for one causal mechanism", "practical_experiment": "Run native package tests on mature eligible long-form videos with adequate impressions and preserve the medical promise."},
            {"finding": "Packaging response varies materially by video and source", "video_ids": ["BCNWQ3uuSuE", "SBrMW71O69U", "EB3_A2b4a6o"], "metrics": "Lifetime CTR 3.0%; BCNWQ3uuSuE 4.2%, SBrMW71O69U 2.87%, EB3_A2b4a6o 1.8%", "visual_and_transcript_evidence": "Specific lab-test utility is clearer in BCNWQ3uuSuE than the broad SBrMW71O69U warning", "comparative_evidence": "BCNWQ3uuSuE also retains 60.5% at 30 seconds versus 38.46% for SBrMW71O69U", "historical_context": "Video ages and impression bases differ", "counterexample": "High CTR rows on tiny impression bases are unstable", "alternative_explanations": "Traffic source and audience composition", "confidence": "HIGH for variation; MEDIUM for the specific-package hypothesis", "practical_experiment": "Test exact utility/problem packages against broad warning packages on one unchanged mature video."},
            {"finding": "Early and mid-video retention are inconsistent", "video_ids": ["5oPzZjfNgII", "EB3_A2b4a6o", "BCNWQ3uuSuE", "SBrMW71O69U"], "metrics": "30-second retention 56.15%, 60.0%, 60.5% and 38.46%; midpoint 43.85%, 23.57%, 31.93% and 15.38% respectively", "visual_and_transcript_evidence": "Concrete symptom/test progressions hold more of the audience in selected pairs; long steady explanation sections coincide with faster decline", "comparative_evidence": "Retention and CTR do not always move together", "historical_context": "Actual per-video curves from exports through 2026-09-27", "counterexample": "A dip alone does not identify why viewers left", "alternative_explanations": "Audience intent, source, video length and topic familiarity", "confidence": "HIGH for variation; MEDIUM for production hypotheses", "practical_experiment": "Open with the exact promised decision, demonstrate it early and review the first major dip against the published cut."},
            {"finding": "Shorts feed acceptance and depth are separate", "video_ids": ["QfRaG71ZA_0", "4ByUo2N_C-I", "PTB-6fgaAKk", "gunPgSlxJLA"], "metrics": "QfRaG71ZA_0 stayed 57.3%/APV 83.3%; 4ByUo2N_C-I 43.7%/43.8%; PTB-6fgaAKk 16.9%/126.6%; gunPgSlxJLA 28.7%/84.0%", "visual_and_transcript_evidence": "Concrete symptom frames are easier to parse; very short loops can inflate APV", "comparative_evidence": "kF26QB7xHiE had more views than FVfG_HZV4qg despite much lower stayed-to-watch", "historical_context": "Authenticated lifetime row observations on 2026-09-28", "counterexample": "High APV does not guarantee high stayed-to-watch or distribution", "alternative_explanations": "Feed cohort, loop length and repeat exposure", "confidence": "HIGH", "practical_experiment": "Test first-frame specificity and measure stayed-to-watch separately from APV."},
            {"finding": "Cross-format loyalty and audience-positioning effects remain unresolved", "video_ids": [], "metrics": "Shorts feed produced 5,355 of 8,366 views and 11.23 of 45.62 watch hours; viewers-across-formats and returning-viewer values were unavailable", "visual_and_transcript_evidence": "Catalog spans cardiology, metabolic health and mobility", "comparative_evidence": "YouTube documentation does not support a blanket mixed-format algorithm penalty", "historical_context": "Lifetime source totals", "counterexample": "Mixed formats can serve the same viewer needs", "alternative_explanations": "Small audience and limited returning-viewer history", "confidence": "HIGH that evidence is insufficient; LOW on audience-fragmentation hypothesis", "practical_experiment": "Use recurring series and compare audience reports when YouTube discloses enough data."},
            {"finding": "Public demand alone does not explain outcomes", "video_ids": ["sUL6SU8LnEg", "VlSibJdSZF8", "8JdBlF-ragM"], "metrics": "Ozempic mean normalized Trends score 31.45 versus semaglutide 7.71 and GLP-1 2.99 within one US YouTube Search comparison", "visual_and_transcript_evidence": "Existing packages vary between myth, side-effect and rebound-weight angles", "comparative_evidence": "High normalized interest did not yield strong channel results", "historical_context": "Five-year normalized Trends series", "counterexample": "Trends is not absolute volume and does not describe this channel's eligible audience", "alternative_explanations": "Packaging, authority fit, competition, timing and distribution", "confidence": "MEDIUM", "practical_experiment": "Use exact query/source evidence before commissioning another demand study."},
        ],
        "retention_export_summary": {key: retention[key] for key in ("record_count", "available_count", "curve_available_count", "exported_no_curve_count")},
        "remaining_private_requirements": ["Returning-viewer and viewers-across-formats channel reports", "Search query and suggested-video detail", "Geography and device reports", "Nine uncaptured extended per-video rows if a reliable export becomes available"],
        "preservation": {"raw_private_exports_modified": False, "credentials_saved": False, "remote_push_performed": False, "note": "Only derived docs/research artifacts and supporting scripts were updated."},
    }
    (OUT_DIR / "Decode_Your_Heart_Video_Evidence_Register.json").write_text(json.dumps(register, indent=2) + "\n")
    (OUT_DIR / "Decode_Your_Heart_Research_Checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n")


if __name__ == "__main__":
    main()
