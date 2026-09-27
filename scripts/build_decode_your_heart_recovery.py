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
    "8JdBlF-ragM": {
        "duration_seconds": 71,
        "comparison": "Ozempic long-form: stronger holding versus sUL6SU8LnEg",
        "timestamps": ["0:02 seated doctor at desk with name plate, OZEMPIC / SEMAGLUTIDE lower title; caption: When it comes to weight loss, we always talk about [Ozempic] or semaglutide", "0:04 blurred close-up B-roll of an injector pen (curve -4.9 pts at 2-4% position)", "0:20 doctor on camera, LOSS OF LIBIDO title; caption: is Ozempic vagina or loss of libido because of this drug", "0:44 anatomical cross-section illustration; caption: fat loss occurs from those areas as well (curve -3.3 pts at 61%)", "0:58 animated RISK gauge with DAYS label; caption: lose fat aggressively rapidly over the course of days instead of months (curve -3.3 pts at 81%)", "1:08 doctor with end-screen video cards; caption: if we take care of our hydration status"],
        "opening": "Names the drug and the common weight-loss framing, then turns to the sexual-health side effect by 0:20.",
        "visuals": "Seated desk shot alternating with pen B-roll, anatomy illustration and an animated risk gauge.",
        "editing": "22 hard cuts in 70 s (about 19 per minute) measured in the continuous 2x signal pass.",
        "closing": "Hydration advice over end-screen cards.",
        "possible_explanation": "Short runtime and a specific, rarely discussed side effect; 30-second retention 55.74% and end retention 45.9%. New viewers held far better than returning viewers (62.75% vs 20.0% at the 30-second position), so the topic may have reached a new-audience cohort.",
        "alternative_explanation": "78 views; each curve step is roughly 1.6 viewers. No extended Studio row was captured for this video, so stayed/swiped values are unavailable.",
    },
    "sUL6SU8LnEg": {
        "duration_seconds": 166,
        "comparison": "Ozempic long-form: weaker holding versus 8JdBlF-ragM",
        "timestamps": ["0:03 seated doctor at the same desk, name plate, no title card; caption: There are certain mythologies attributable to ozempic or semaglutide (curve -20 pts at 2% position)", "0:13 illustrated crowd graphic Common Myths About Semaglutide (Ozempic) with Permanent Muscle Loss, Only for Diabetes, It Causes Cancer; caption shows a literal (0:20) timecode (curve -20 pts at 8%)", "0:40 doctor; caption: multi endocrine neoplasia which is known as [medullary] thyroid carcinoma", "1:09 eye-anatomy illustration with magnifier; caption: clinical (1:10) entities like optic", "1:20 doctor gestures to his eye; caption: NAION, non arteritic ischemic anterior optic neuropathy (curve -10 pts at 49%)", "1:55 doctor; caption: US health network comprising of 16000 patients", "2:21 doctor; caption: 0.01% of patients who are taking ozempic (curve -10 pts at 85%)", "2:40 doctor; caption: one should never stop ozempic or semaglutide only because he or she is scared"],
        "opening": "Abstract myth-debunk statement with no question, symptom or viewer qualifier; first graphic arrives around 0:13.",
        "visuals": "Same desk set as 8JdBlF-ragM; two illustrations (myth crowd, eye anatomy) and long single-shot explanation.",
        "editing": "23 hard cuts in 166 s (about 8 per minute); the first hard cut is at 18.6 s.",
        "closing": "Reassurance not to stop the drug out of fear.",
        "possible_explanation": "Abstract myth framing and clinical terminology (medullary thyroid carcinoma, NAION) may raise effort for a lay audience; 30-second retention 40.0% and end 10.0%. The uploaded captions show raw (m:ss) timecodes.",
        "alternative_explanation": "Only 10 views, so each curve step is one viewer; a 2.3x longer runtime also spreads loss over more time.",
    },
    "KPYHy7MDmLM": {
        "duration_seconds": 117,
        "comparison": "Circulation long-form: weaker early holding versus NznebmgFwXI",
        "timestamps": ["0:02 doctor in dim office behind kinetic OVER 50? NOTICING SMALL CHANGES, plus a burned-in all-caps subtitle bar MANY PEOPLE OVER FIFTY NOTICE THIS BUT IGNORE IT and the player caption (three text layers); caption: Many people over 50 notice this but ignore it (curve -15.8 pts at 1% and -10.5 at 2-3%)", "0:05 stock B-roll of a clinician with typewriter-style HEA[RT] text; burned-in HEART SPECIALIST QUIETLY WATCH", "0:30 doctor with cartoon-doctor sticker, OR YOUR HEALTHCARE PROVIDER; caption: It gives small hint and this is up to the doctors", "1:02 stock clinician B-roll; DO YOU KEEP A STEADY PACE OR FADE AFTER A FEW (curve -5.3 pts at 52%)", "1:07 doctor; CAN YOU TELL YOUR NAME IN ONE SENTENCE; caption: Can you talk comfortably or need to pause? (curve -10.5 pts at 57%)", "1:32 stock family on a sofa; IT'S ABOUT INDEPENDENCE IT MEANS VISITING LOVED", "1:49 SUBSCRIBED button animation over doctor; caption: Subscribe for calm, practical advice (curve -5.3 pts at 93%)"],
        "opening": "Generic over-50 warning (notice this but ignore it) with no named symptom; three simultaneous text layers.",
        "visuals": "Dim office, frequent stock B-roll, stickers and kinetic words; burned-in captions duplicate the player captions.",
        "editing": "33 hard cuts in 117 s (about 17 per minute); loudest and most compressed audio in the batch (median RMS 0.18, 10th percentile 0.13).",
        "closing": "Share and subscribe animation.",
        "possible_explanation": "Retention falls to 57.89% by 3 s despite fast cutting: the opener withholds the symptom and the screen is crowded with text. 30-second retention 36.84%.",
        "alternative_explanation": "20 views (each step about 5 pts); only returning viewers appear in the segment export. CTR 6.59% suggests the package attracted clicks the opening did not satisfy, but the sample is tiny.",
    },
    "NznebmgFwXI": {
        "duration_seconds": 151,
        "comparison": "Circulation long-form: stronger early holding versus KPYHy7MDmLM",
        "timestamps": ["0:02 seated doctor, bright office, one white COLD FEET? card; caption: If your feet are often cold, even when the room is warm, your body may be sending an important signal (curve -6.5 pts at 1%, -7.2 at 2%)", "0:06 SOMETIMES NORMAL card; caption: Sometimes cold feet are harmless, but at other times they can reduce blood circulation", "0:14 TODAY ... MEAN lower third; caption: Today, I'll explain what cold feet might mean ... Hello, (introduction; curve -4.8 pts at 15%)", "0:23 O2 icon; caption: oxygen and nutrients throughout the body", "0:45 BLOOD MUST TRAVEL THROUGH LONG ARTERIES TO lower third", "1:30 AGING? card; caption: She often wore thick socks even during warm weather (patient story)", "2:25 NEXT INSIGHT: ONE POWERFUL FRUIT card with two end-screen video cards; caption: there's one everyday fruit that many"],
        "opening": "Viewer-qualifying symptom question in the first sentence, then reassurance (sometimes normal) before the introduction.",
        "visuals": "One continuous seated take with text cards and simple icons; no stock B-roll at sampled anchors.",
        "editing": "Only 2 hard cuts in 151 s; overlays change but the shot does not. Continuous audio floor (no sample below 0.01 RMS).",
        "closing": "Tease of the next video (one powerful fruit) over end-screen cards.",
        "possible_explanation": "A concrete self-check symptom in the first sentence coincides with 87.1% retention at 3 s and 41.13% at 30 s, despite almost no cutting.",
        "alternative_explanation": "Different topic framing (cold feet versus walking ability), 132 versus 20 views and a lower CTR (2.75%) that may have selected a more intent-matched audience.",
    },
    "hUSVbcHVeVw": {
        "duration_seconds": 39,
        "comparison": "Artery-food Short: format contrast with the long-form CZ3gAUzdTAg",
        "timestamps": ["0:02 washed-out, over-exposed near-white frame with a faint figure; caption: 5 Foods That Clean Your Arteries These 5 foods help support healthy arteries (caption track begins with a heading line)", "0:05 3D anatomy figure with glowing arteries, ARTERIES NARROW, CHOLESTEROL, INFLAMMATION warning (curve -5.3 to -5.9 pts at 12-14%)", "0:12 seated doctor, DOCTOR APPROVED TOP 5 FOODS; caption uses emoji numerals: 1 Fatty fish like salmon", "0:27 olive close-up, 5. OLIVE OIL MEDITERRANEAN DIET (curve -4.0 pts at 69%)", "0:37 doctor, SAVE YOUR HEART and FULL VIDEO arrow; caption: Watch it next (curve -11.8 pts at 98%)"],
        "opening": "Title-card style list promise over a pale frame, then an anatomy warning before the doctor appears at about 0:12.",
        "visuals": "Anatomy render, food B-roll and doctor inserts; numbered cards.",
        "editing": "12 hard cuts in 38 s (about 19 per minute).",
        "closing": "Explicit pointer to the full video.",
        "possible_explanation": "A numbered five-item list gives a visible progress path; 30-second retention 59.87% and stayed-to-watch 39.7%.",
        "alternative_explanation": "Short-form retention is not comparable to the long-form partner. The title promises to reverse artery damage while the captions say support healthy arteries, a claim mismatch that metrics cannot evaluate.",
    },
    "CZ3gAUzdTAg": {
        "duration_seconds": 211,
        "comparison": "Artery-food long-form: format contrast with the Short hUSVbcHVeVw",
        "timestamps": ["0:02 doctor in a dim room behind SUDDEN BLOCKAGE?; burned-in subtitle bar plus player caption: Most people think clogged arteries happen suddenly (curve -9.5 pts at 1% and 2%)", "0:05 artery B-roll, BUILDS OVER YEARS", "0:12 doctor in bright office, THE GOOD NEWS (curve -7.7 pts at 6%)", "0:18 food-grid B-roll, TOP 5 HEART FOODS; caption: Today, I'll show you five foods that (curve -3.9 pts at 8%)", "0:45 1. FATTY FISH card; caption: The first food is fatty fish such as salmon, sardines, and mackerel", "1:50 doctor with nuts icon; NUTS CONTAIN A COMBINATION OF HEALTHY FATS", "3:20 NEXT: BALANCE TEST card; caption: reveal important clues about your health"],
        "opening": "Misconception opener (sudden blockage) and promise of five foods; first food named at about 0:43.",
        "visuals": "Two different room setups (dim and bright), food and artery B-roll, burned-in subtitles duplicating player captions.",
        "editing": "64 hard cuts in 210 s (about 18 per minute); continuous audio floor.",
        "closing": "Next-video tease (balance test).",
        "possible_explanation": "The list promise at 0:18 and first item at 0:43 leave a 25 s gap; the curve loses about 34 pts by 10 s. End retention 10.39%.",
        "alternative_explanation": "Highest impressions in the batch (5,737) at 3.7% CTR, so a broader and less intent-matched audience; long-form and Short curves cannot be compared directly.",
    },
    "FDLU7tX7qNM": {
        "duration_seconds": 45,
        "comparison": "Ankle/calf Shorts: high-reach weaker holding versus p_iI0enaFX8",
        "timestamps": ["0:02 illustrated swollen ankles with red highlight circles and DON'T IGNORE, white letterbox; caption: Have you noticed swelling in your ankles? Don't ignore it", "0:05 cut to seated doctor at desk, thumbs-up, no text (curve -9.9 pts at 10% and -7.5 at 11%)", "0:07 SWOLLEN ANKLES? DON'T IGNORE THIS header, burned-in yellow-highlight subtitles duplicate the player caption: Many seniors think it's normal (curve -5.1 pts at 13%)", "0:15 red-blood-cell illustration; caption: fluid can build up in the lower legs and ankles", "0:30 WATCH FULL LONG VIDEO NOW CLICK HERE -> header over the doctor", "0:43 SHARE SHARE SHARE graphic; caption: Like, comment HEALTH, and subscribe (emoji in the caption track)"],
        "opening": "Illustrated symptom question, then a cut to a static doctor at about 0:04 that repeats the question.",
        "visuals": "White letterbox, illustration, doctor at desk, header text and burned-in highlight subtitles.",
        "editing": "11 hard cuts in 45 s; a cluster of cuts in the final 3 s.",
        "closing": "Share/like/comment call and a pointer to the long-form video.",
        "possible_explanation": "The steepest losses (4.5-6 s) coincide with the switch from illustration to a static doctor who repeats the question; 30-second retention 18.77%. New viewers 17.78% versus returning 46.15% at the 30-second position.",
        "alternative_explanation": "805 views and 44.0% stayed-to-watch: feed acceptance was good, so broad feed exposure to less-interested viewers can explain the lower holding.",
    },
    "p_iI0enaFX8": {
        "duration_seconds": 60,
        "comparison": "Ankle/calf Shorts: tiny-sample stronger holding versus FDLU7tX7qNM",
        "timestamps": ["0:02 AI-style figure in a cardigan with glowing heart and ECG line; kinetic word can; caption: (0:00) Over 60, your legs may already be sending you a heart warning. (0:05) 4 leg", "0:10 near-blank white frame at the sampled moment; caption: (0:08) 1. Calf pain while walking (curve -9.1 pts at 16%)", "0:22 two glowing blue feet, 2. COLD WET FEET (curve -9.1 pts at 22%)", "0:38 over-exposed near-white frame at the sampled moment; caption: (0:36) Any one of these alone (curve -9.1 pts at 63%)", "0:48 seated doctor, kinetic word actually; caption: (0:44) The most serious of the four is actually calf cramping (curve -9.1 pts at 80%)", "0:57 doctor; caption: (0:56) Watch my full video for the complete breakdown"],
        "opening": "Age qualifier and numbered promise (4 leg signals) within 5 s, over an illustrated figure.",
        "visuals": "AI-style illustrations, white or over-exposed transition frames, doctor inserts later.",
        "editing": "9 hard cuts in 60 s; numbered progression.",
        "closing": "Ranks the most serious sign, then points to the full video.",
        "possible_explanation": "Numbered promise with a ranked payoff; 30-second retention 81.82%, end 27.27%, stayed 46.2%. Uploaded captions show raw (m:ss) timecodes throughout.",
        "alternative_explanation": "Only 18 views and 144 impressions: each curve step is one viewer (9.1 pts), so the curve cannot support a comparison with FDLU7tX7qNM.",
    },
    "fAwh2svMARM": {
        "duration_seconds": 204,
        "comparison": "Coffee clip family: long-form parent of four coffee Shorts",
        "timestamps": ["0:02 seated doctor in blue shirt, bright office, burned-in BUT HERE'S THE SURPRISING PART; caption: Coffee can raise your blood pressure. But here's the surprising part.", "0:08 50+ card and IN FACT FOR MANY PEOPLE ABOVE THE AGE OF 50; caption: That does not mean that you should stop drinking it (curve -11.1 pts at 8 s, the largest drop)", "0:15 3 THINGS TO KNOW ABOUT COFFEE; caption: But only if you understand these three things. Number one", "1:00 SO THEY DRINK AS MUCH COFFEE AS THEY WANT with coffee icon; caption: Others are not", "1:55 HOME CUP IS NOT EQUIVALENT TO A LARGE OFFICE CUP with cup icons", "2:30 YOU DEVELOP TACHYCARDIA SO ANY OF THESE SYMPTOMS with symptom tiles; caption: please contact your healthcare (curve -7.4 pts at 149 s)", "3:18 YOUR BODY YOUR RESPONSE; caption: your body has the final answer"],
        "opening": "States the worry (coffee raises BP), promises a surprise, then qualifies the audience (above 50) and a three-part list by 0:15.",
        "visuals": "Single seated setup with large burned-in caption lines and occasional icon cards; the player caption duplicates the burned-in text.",
        "editing": "13 hard cuts in 204 s (about 4 per minute); continuous audio floor.",
        "closing": "Individual-tolerance conclusion; end-screen video card.",
        "possible_explanation": "The strongest long-form holding in this batch: 81.48% at 10 s and 70.37% at 30 s, end 22.22%, compared-to-other-videos +2.92 at 30 s. The same permission-plus-numbered-promise structure reappears in the stronger coffee Shorts cut from it.",
        "alternative_explanation": "Only 287 impressions and 48 views; each curve step is about 3.7 pts (one viewer). Its four Shorts drew more views than the parent.",
    },
    "nRdBvyh7Sy0": {
        "duration_seconds": 54,
        "comparison": "Coffee clip family: Short excerpt with no disclosed retention curve",
        "timestamps": ["0:02 close-up of a coffee cup with kinetic I ONLY DRINK 2 CUPS; auto caption: You may say [music] I only drink two cups of coffee a day. But Dr. Rahan said", "0:15 doctor at desk with three cup sizes, THE CUP SIZE MATTERS; caption: Because the cup size matters", "0:30 doctor, MOST GUIDELINES; caption: up to 400 mg of caffeine can be safely taken during 24 hours", "0:52 BP SPIKE? long-form thumbnail over a grid with red down arrow; caption: explained the complete picture in coffee after 50"],
        "opening": "Viewer objection voiced by a third-person narrator (Dr. Rahan said), not the doctor.",
        "visuals": "Stock cup close-up, then the parent video's desk footage with kinetic words.",
        "editing": "6 hard cuts in 53 s; auto captions tag [music].",
        "closing": "Explicit pointer to the long-form parent with its thumbnail.",
        "possible_explanation": "Stayed-to-watch 40.9% and APV 78.6% (browser-observed) are within the range of the other coffee Shorts.",
        "alternative_explanation": "Studio disclosed no retention curve and only 25 views; no timestamp can be tied to viewer loss.",
    },
    "nP9fDHP1jbo": {
        "duration_seconds": 20,
        "comparison": "Ozempic Shorts: higher reach versus 7MXBh2hjfto",
        "timestamps": ["0:02 doctor at desk behind name plate, ??? and HUNGER kinetic text; caption: People also [music] ask me why does hunger reappear after stopping [Ozempic]", "0:05 SIMPLE; caption: The answer is simple (curve -9.7, -7.1 and -6.2 pts across 4.2-5.0 s)", "0:07 hand with injector pen and brain-outline graphic, BRAIN; caption: it talks to the brain through", "0:12 stock man with overlaid brain graphic, THE; caption: through neurons and thereby it reactivates", "0:19 final frame; video ends"],
        "opening": "Question framed as what patients ask, answered as simple within 5 s.",
        "visuals": "Desk shot, injector B-roll, brain overlays.",
        "editing": "9 hard cuts in 19 s (about 28 per minute), the fastest in the catalog so far; loud continuous audio floor.",
        "closing": "Ends on the mechanism with no call to action.",
        "possible_explanation": "Viewers leave as the answer is declared simple (4-5 s); end retention 15.93%, stayed-to-watch 23.9%. The 19 s runtime inflates APV through replays (retention above 100% at 0-3 s).",
        "alternative_explanation": "490 views from 105 impressions means most views came from the Shorts feed, where swipe-away is the dominant exit.",
    },
    "7MXBh2hjfto": {
        "duration_seconds": 26,
        "comparison": "Ozempic Shorts: title-content mismatch versus nP9fDHP1jbo",
        "timestamps": ["0:02 doctor behind name plate, ???, injector icon and tumour graphic; caption: Do you know that there is a myth that Ozempic also causes [cancer]", "0:05 same frame; caption: Well, the myth is absolutely absurd (curve -7.8 pts at 4.4 s)", "0:08 illustrated scientist at a microscope, NO PROVEN LINK TO CANCER; caption: Ozempic has not been caused for any kind of cancer (curve -6.2 pts at 7.8-8.1 s)", "0:15 MEN 2 SYNDROME; caption: history of medullary thyroid carcinoma", "0:24 bell icon; caption: you can watch my video by clicking"],
        "opening": "Cancer-myth question; the title instead promises an Ozempic versus appetite-suppressant comparison that never appears at sampled anchors.",
        "visuals": "Desk shot with icon overlays and one illustration.",
        "editing": "7 hard cuts in 25 s.",
        "closing": "Bell icon and pointer to a longer video.",
        "possible_explanation": "Title-content mismatch plus an early verdict (absurd at 0:05); end retention 6.25%.",
        "alternative_explanation": "216 views from 109 impressions (feed-driven); the mismatch cannot be separated from topic and runtime with this sample.",
    },
    "1bb5M4E1oQs": {
        "duration_seconds": 43,
        "comparison": "Potassium Shorts: same reclining-chair shoot as j9VqMB6yTXQ",
        "timestamps": ["0:02 doctor in a reclining chair with animated elderly-couple sticker and yellow kinetic word simplest; caption: Most seniors ignore that one of the simplest", "0:06 avocado, banana and greens icons, BP-monitor graphic, blood (curve -9.1 pts at 5-7 s)", "0:14 potassium K icon, element; caption: but there's another very important element, potassium (curve -9.1 pts at 13-14 s)", "0:25 Bananas card held in frame; auto caption: causes [music] a reduction in high blood pressure", "0:35 same Bananas card, no caption (speech appears finished; curve -18.2 pts at 35 s)", "0:41 red DON'T FORGET TO SUBSCRIBE end card"],
        "opening": "Mystery framing (simplest food seniors ignore) with the food withheld.",
        "visuals": "One continuous chair shot with stickers and icons; a static card for the last 10 s.",
        "editing": "3 hard cuts in 42 s.",
        "closing": "Several seconds without speech, then a subscribe card.",
        "possible_explanation": "The largest drop (35 s) falls in a stretch with no speech on a static card; 30-second retention 36.36%, stayed 46.2%.",
        "alternative_explanation": "23 views and 53 impressions: each curve step is about 2 viewers, so no single step is reliable.",
    },
    "j9VqMB6yTXQ": {
        "duration_seconds": 47,
        "comparison": "Potassium Shorts: sibling from the same shoot, no disclosed curve",
        "timestamps": ["0:02 doctor in the same reclining chair with a food-colour wheel graphic; auto caption: Potassium is one of the commonest elements [music]", "0:07 same shot, and fights against sodium", "0:18 caption: Patients who are seniors more than the age of 60 if they have high blood pressure", "0:32 rich in potassium; caption: fruits rich in potassium like bananas in my next long video", "0:45 red DON'T FORGET TO SUBSCRIBE end card"],
        "opening": "Definition-first: potassium is one of the commonest elements.",
        "visuals": "Single chair shot with a food wheel and kinetic words.",
        "editing": "1 hard cut in 46 s (near-single take).",
        "closing": "Defers the food list to a future long video, then a subscribe card.",
        "possible_explanation": "Definition-first opener and a deferred payoff, which in curve-bearing videos coincide with early loss.",
        "alternative_explanation": "Studio disclosed no retention curve; 21 views and zero recorded CTR on 90 impressions.",
    },
    "nPqrcrxdrdE": {
        "duration_seconds": 32,
        "comparison": "Walking Shorts: animated avatar versus UeGxF8-hb2s",
        "timestamps": ["0:02 cartoon avatar of the doctor walking on white, kinetic one small; caption (in quotation marks): Do you know one small walking change many seniors ignore... but doctors don't?", "0:06 same avatar (curve -8.9 pts at 6.7 s)", "0:09 but we doctors don't ! card; caption: If you need to slow down sooner than before (curve -6.7 pts at 9 s)", "0:20 If you need to slow down sooner; caption: They often appear long before real symptoms start", "0:29 cut to real doctor at desk, link in; caption: Tap the link in the description and watch it today"],
        "opening": "Question with an insider hook (seniors ignore, doctors don't) over a cartoon avatar.",
        "visuals": "Animated avatar for most of the runtime; real doctor only in the last seconds.",
        "editing": "3 hard cuts in 31 s; natural speech gaps (15% near-silent samples, no bed).",
        "closing": "Link to the long-form video.",
        "possible_explanation": "Retention 62.22% at 10 s and 20.0% at end; compared-to-other-videos +60.2 at 30 s. The captions carry literal quotation marks, suggesting a pasted script.",
        "alternative_explanation": "171 views from 218 impressions; title promises three signs while sampled anchors show one, which is unverified between anchors.",
    },
    "UeGxF8-hb2s": {
        "duration_seconds": 89,
        "comparison": "Walking Shorts: chair-stand test with a 39-second black tail",
        "timestamps": ["0:02 doctor at desk gesturing; caption: If you're over 60, how many times should you be able to stand up", "0:10 same shot; caption: in 30 seconds? 10 times? 20 times?", "0:29 CROSS YOUR ARMS ACROSS YOUR CHEST with chair icon; caption: You sit down properly, put your feet down (curve -7.7 pts at 28-31 s)", "0:48 last content frame; caption: watch my video in the link below (curve -15.4 pts at 50 s)", "0:50 black frame and near silence begin (mean frame luminance 0 from 50 s to 80 s; curve -15.4 pts at 55 s)", "1:28 video ends after about 39 s of black"],
        "opening": "Viewer self-test question with concrete counts in the first 10 s.",
        "visuals": "Seated doctor and one demo card; nothing from 0:50 onward.",
        "editing": "6 hard cuts; 43.8% of audio samples below 0.01 RMS because of the silent tail.",
        "closing": "Content ends at about 0:49; the remaining 44% of the runtime is black.",
        "possible_explanation": "Export defect: a black, silent tail makes up 44% of the runtime. Retention holds (69.23% at 30 s, stayed 50.0%) until the content ends, then falls to 7.69%. APV 51.3% is capped by the dead tail.",
        "alternative_explanation": "34 views (each step about 2 viewers); the defect certainly lowers APV but its effect on distribution is unknown.",
    },
    "qObP1FPrC6Q": {
        "duration_seconds": 61,
        "comparison": "Diabetes Shorts: illustrated morning-glucose explainer versus b-dam2LdHzM",
        "timestamps": ["0:02 illustrated man in bed by a window plus doctor cutout; caption: Most people check their blood sugars the very second", "0:07 dark background with doctor cutout and word-by-word have; curve loses 15.4 points by about 0:07", "0:19 sparse kinetic phrase Therefore, that", "0:28 doctor cutout and text and stress. But there is much", "0:45 traffic-jam-of-glucose metaphor", "0:57 Thanks Watching. end card (missing apostrophe) with Like, Comment, Share and Subscribe"],
        "opening": "Opens on a morning glucose-checking behavior, then moves into an abstract explanation of the morning spike.",
        "visuals": "Illustrated/stock scenes on dark backgrounds with a circular doctor cutout and word-by-word kinetic captions.",
        "editing": "Three hard cuts in the continuous signal pass; much of the change comes from text and illustration swaps.",
        "closing": "A four-action end card begins before the 61-second player runtime ends.",
        "possible_explanation": "Stayed-to-watch is 34.2%, but retention falls from 76.92% at 10 seconds to 15.38% at the end; the abstract mechanism and multi-action closing may not sustain the opening behavior question.",
        "alternative_explanation": "Only 36 views; audience source and the medical topic differ from the paired oatmeal Short.",
    },
    "b-dam2LdHzM": {
        "duration_seconds": 59,
        "comparison": "Diabetes Shorts: concrete oatmeal example versus qObP1FPrC6Q",
        "timestamps": ["0:02 oatmeal bowl with HEALTHY BREAKFAST; caption: Healthy breakfast or blood sugar bomb?", "0:09 oatmeal versus candy bar, HIGHER than a candy bar; curve drops 11.8 points around 0:08-0:10", "0:13 doctor in chair with kinetic oatmeal; caption: You wake up and make a bowl of instant oatmeal", "0:31 doctor and kinetic captions; Your pancreas strains, but your aging cells", "0:50 list of eight with walnuts or eggs to slow digestion", "0:57 red DON'T FORGET TO SUBSCRIBE card; caption directs viewers to the full list after age 70"],
        "opening": "Concrete breakfast-versus-blood-sugar question, followed by an oatmeal-versus-candy comparison.",
        "visuals": "Food imagery and comparison cards hand off to a seated doctor with large kinetic captions.",
        "editing": "Two hard cuts in the continuous signal pass; visual progression comes mainly from overlays and food cards.",
        "closing": "Promises a full list of eight, then displays a subscribe card.",
        "possible_explanation": "Lower feed acceptance (25.8% stayed) but deeper viewing after the swipe decision: APV 65.5%, 64.71% retained at 30 seconds and 35.29% at the end.",
        "alternative_explanation": "64 views and a different title/topic package; no production element is isolated.",
    },
    "78JR_U-6HfQ": {
        "duration_seconds": 184,
        "comparison": "Heart-risk long-form: fast stock/kinetic edit versus 3dRcNqiLHgY",
        "timestamps": ["0:02 doctor in clinic office, MORNING = SAFEST TIME? and burned-in subtitle bar", "0:04 large BUT DOCTORS / CARDIOLOGISTS KNOW SOMETHING SURPRISING text; curve loses 12.1 points by about 0:04", "0:17 heart icon and THAT CAN PROTECT YOUR HEART FOR A LONG; caption: Today I'll show you what the habit is", "0:57 stock elderly man and AND FOR THE OLDER ELDERS THIS SUDDEN CHANGE", "1:50 stock man and STEP 1: SIT 30 SECONDS; caption: here's a simple fix", "2:58 subscribe animation"],
        "opening": "Morning-safety question with a cardiologist-knows-something-surprising open loop.",
        "visuals": "Doctor footage alternates with stock older-adult scenes, icons, large kinetic words and a persistent subtitle treatment.",
        "editing": "Sixty detected hard cuts in 183 seconds (about 19.7 per minute), far faster than the paired talking-head video.",
        "closing": "A practical sit-before-standing step leads into a subscribe animation.",
        "possible_explanation": "Retention is 84.85% at 3 seconds, 72.73% at 10 seconds and 54.55% at 30 seconds; the question and promised habit remain explicit despite the early dip.",
        "alternative_explanation": "37 views, 945 impressions and a 2.54% CTR; topic, packaging, traffic source and edit all differ from 3dRcNqiLHgY.",
    },
    "3dRcNqiLHgY": {
        "duration_seconds": 117,
        "comparison": "Heart-risk long-form: near-single-shot silent-heart-attack explainer versus 78JR_U-6HfQ",
        "timestamps": ["0:03 doctor in blue scrubs in a pillarboxed clinic shot; burned caption repeats very important while introducing the topic", "0:07 same shot with full-width CAUSE OF DEATH WORLDWIDE card; early curve losses occur at 0:01-0:09", "0:10 mortality-chart icon while the narration remains on global cardiovascular deaths", "0:40 same doctor shot; caption: the diagnosis of heart attack becomes", "1:12 doctor plus vertigo/weakness cutouts while atypical symptoms are listed", "1:50 subscribe overlay and next-video cards over the doctor"],
        "opening": "Repeated importance framing and global mortality statistics precede the specific silent-heart-attack symptom value.",
        "visuals": "One pillarboxed clinic talking-head shot with burned captions, occasional full-width keywords, icons and symptom cutouts.",
        "editing": "Sampled anchors show a stable single-camera composition; no continuous cut or audio-level pass was available in this browser session.",
        "closing": "Subscribe overlay and suggested-video cards cover the final explanation.",
        "possible_explanation": "Retention falls to 52.38% at 10 seconds and 38.1% at 30 seconds while the opening is still establishing importance and global mortality rather than naming actionable atypical symptoms.",
        "alternative_explanation": "Only 24 views; small curve steps, topic, title and traffic can explain the difference from 78JR_U-6HfQ.",
    },
    "r9ZyUWyY4Lc": {
        "duration_seconds": 115,
        "comparison": "Medication/food advice long-form: motion-graphic ACV explainer versus HzFdyjyEFTY",
        "timestamps": ["0:00 small circular doctor cutout on a white motion-graphic field", "0:14 large kinetic So what I tell them while the narration says he will tell viewers the same; curve dips at 0:13 and 0:15", "0:16 you guys the same, then the refined-carbohydrate explanation begins", "1:02 acetic-acid molecule points to an enzyme graphic", "1:34 cartoon tooth warning, damages the enamel; transcript advises dilution and a straw", "1:44 sparse kinetic effects text while returning to refined-carbohydrate consequences", "1:54 doctor cutout with suggested-video cards at the end"],
        "opening": "Names organic apple-cider-vinegar benefits, then frames the answer as advice given to patients.",
        "visuals": "White motion-graphic canvas, circular doctor cutout, large kinetic phrases and simple molecule/tooth illustrations.",
        "editing": "Frequent graphic substitutions around a persistent doctor cutout; no continuous cut or audio-level pass was available in this browser session.",
        "closing": "Points to a longer blood-glucose video while suggested-video cards appear.",
        "possible_explanation": "The video holds 89.16% at 10 seconds and 67.47% at 30 seconds; the two early dips coincide with a meta phrase before the refined-carbohydrate mechanism begins, but this is association only.",
        "alternative_explanation": "113 views and a 4.64% CTR; ACV intent, search traffic and package strength may select a more motivated audience.",
    },
    "HzFdyjyEFTY": {
        "duration_seconds": 182,
        "comparison": "Medication/food advice long-form: aspirin decision explainer versus r9ZyUWyY4Lc",
        "timestamps": ["0:03 doctor in an exam room with a large pill illustration; caption asks why the viewer takes this pill", "0:05 same shot; throughout your life", "0:12 oversized WILL IT HELP YOU OUT?", "0:16 older-adult cutout; millions of seniors who are more than 60 years of age", "0:27 heart icon and pill; or this pill is gonna save the heart", "0:42 blood-cell animation while aspirin's blood-thinning/longevity belief is described; curve drops 11.11 points", "1:41 heart and brain icons during primary-prevention explanation", "2:51 large AVOID IT over the doctor; caption: avoid taking aspirin"],
        "opening": "Two direct questions about a daily lifelong pill, with the aspirin name initially withheld even though the title supplies it.",
        "visuals": "Single exam-room doctor shot with pill, heart, blood-cell and brain overlays plus large kinetic phrases and burned captions.",
        "editing": "Stable direct-to-camera setup with overlay-driven variation; no continuous cut or audio-level pass was available in this browser session.",
        "closing": "Ends on an avoid-aspirin warning for primary prevention; transcript separately preserves secondary-prevention use.",
        "possible_explanation": "Retention is 86.11% at 10 seconds and 66.67% at 30 seconds; the largest 11.11-point step at 0:42 occurs around the aspirin reveal/history transition, not proof that the reveal caused exit.",
        "alternative_explanation": "50 views and 1.35% CTR; the current document title was observed as Taking Aspirin Every Day? Why You Need to Reconsider while retained metadata still carries the acquisition title, suggesting packaging variation or a later title change.",
    },
    "PIsyBj58fJA": {
        "duration_seconds": 122,
        "comparison": "Outdoor mobility demonstrations: shoulder routine versus RD7ugxaBHSQ",
        "timestamps": ["0:03 outdoor vertical shot with doctor and two participants; large side text DIABETES", "0:34 all three demonstrate arm raises; side text 15-20 REPETITIONS; curve drops 11.77 points around 0:33", "0:39 side text KEEP ELBOWS STILL; another 11.77-point step occurs around 0:38", "0:44 MOVE THE SHOULDER ONLY while the same movement continues", "1:12 REVERSE DIRECTION during an arm-circle variation", "1:45 REVERSE during the cooldown movement; curve's largest 17.64-point drop is around 1:44", "1:59 end-screen video cards and subscribe overlay cover the outdoor group"],
        "opening": "Identifies diabetes/older age and frozen shoulder before moving into a multi-exercise demonstration.",
        "visuals": "Vertical outdoor group demonstration with large black instructional text on white side panels.",
        "editing": "Exercise progression supplies visual change without leaving the outdoor setup; no continuous cut or audio-level pass was available in this browser session.",
        "closing": "Cooldown/reverse movement, then end-screen cards and subscribe overlay.",
        "possible_explanation": "82.35% remain at 30 seconds, while the largest late drop occurs after most exercise value has been delivered and the routine is reversing/cooling down.",
        "alternative_explanation": "Only 18 views; one viewer can move the curve materially, and the video differs from RD7ugxaBHSQ in exercise, duration and participants.",
    },
    "RD7ugxaBHSQ": {
        "duration_seconds": 92,
        "comparison": "Outdoor mobility demonstrations: calf stretch plus push-ups versus PIsyBj58fJA",
        "timestamps": ["0:02 outdoor vertical shot with doctor and another man before the first step", "0:16 STEP #01 beside the two men; curve drops 14.29 points around 0:15", "0:18 same setup immediately after the first-step label; another 9.52-point step follows", "0:40 NEXT EXERCISE as the video shifts away from calf stretching", "0:52 SENIOR-FRIENDLY while introducing modified push-ups", "1:07 demonstrator on a mat; side text KNEES DOWN / CROSS YOUR FEET", "1:29 suggested-video cards and subscribe overlay over the outdoor group"],
        "opening": "Claims calves are a second heart, then introduces a morning calf stretch.",
        "visuals": "Vertical outdoor two-person instruction, later a mat-based modified push-up demonstration; large side-panel labels.",
        "editing": "Two-part exercise structure: calf stretch, then modified push-ups; no continuous cut or audio-level pass was available in this browser session.",
        "closing": "Returns to the standing group under end-screen cards and a subscribe overlay.",
        "possible_explanation": "The title promises calf movement, but much of the second half demonstrates shoulder/chest/triceps push-ups; 47.62% remain at 30 seconds and 23.81% at the end. The scope shift is observable, not proven causal.",
        "alternative_explanation": "29 views; the 0:15-0:18 loss occurs before the push-up segment, so the later title-scope mismatch cannot explain the early drop.",
    },
}
PRIORITY_PLAYBACK.update(SEEK_SAMPLED)


# Continuous 2x playback of the whole video through a Web Audio analyser that was not connected to the speakers,
# measured 2026-09-28. Numbers are RMS amplitude (0-1) and hard cuts (mean 32x18 frame change > 40/255).
# This measures levels and cuts only: speech, music and fades were not perceived or classified.
SIGNAL_PASS = {
    "8JdBlF-ragM": {"reached_s": 70.1, "duration_s": 70.3, "hard_cuts": 22, "rms_p10": 0.038, "rms_median": 0.0624, "rms_p90": 0.0905, "share_below_0_01": 0.005},
    "sUL6SU8LnEg": {"reached_s": 165.2, "duration_s": 165.5, "hard_cuts": 23, "rms_p10": 0.0083, "rms_median": 0.1115, "rms_p90": 0.1854, "share_below_0_01": 0.108},
    "KPYHy7MDmLM": {"reached_s": 116.8, "duration_s": 116.9, "hard_cuts": 33, "rms_p10": 0.1323, "rms_median": 0.1837, "rms_p90": 0.255, "share_below_0_01": 0.008},
    "NznebmgFwXI": {"reached_s": 150.4, "duration_s": 150.6, "hard_cuts": 2, "rms_p10": 0.0549, "rms_median": 0.1111, "rms_p90": 0.1774, "share_below_0_01": 0.0},
    "hUSVbcHVeVw": {"reached_s": 38.1, "duration_s": 38.2, "hard_cuts": 12, "rms_p10": 0.0234, "rms_median": 0.0921, "rms_p90": 0.1622, "share_below_0_01": 0.027},
    "CZ3gAUzdTAg": {"reached_s": 210.1, "duration_s": 210.2, "hard_cuts": 64, "rms_p10": 0.0861, "rms_median": 0.1334, "rms_p90": 0.1902, "share_below_0_01": 0.001},
    "FDLU7tX7qNM": {"reached_s": 44.7, "duration_s": 45.0, "hard_cuts": 11, "rms_p10": 0.0343, "rms_median": 0.1259, "rms_p90": 0.2242, "share_below_0_01": 0.004},
    "p_iI0enaFX8": {"reached_s": 59.4, "duration_s": 59.6, "hard_cuts": 9, "rms_p10": 0.0366, "rms_median": 0.1107, "rms_p90": 0.1889, "share_below_0_01": 0.014},
    "fAwh2svMARM": {"reached_s": 203.7, "duration_s": 203.9, "hard_cuts": 13, "rms_p10": 0.0461, "rms_median": 0.1162, "rms_p90": 0.1999, "share_below_0_01": 0.0},
    "nRdBvyh7Sy0": {"reached_s": 53.0, "duration_s": 53.3, "hard_cuts": 6, "rms_p10": 0.0355, "rms_median": 0.1209, "rms_p90": 0.2094, "share_below_0_01": 0.0},
    "nP9fDHP1jbo": {"reached_s": 18.9, "duration_s": 19.1, "hard_cuts": 9, "rms_p10": 0.0985, "rms_median": 0.1354, "rms_p90": 0.2006, "share_below_0_01": 0.0},
    "7MXBh2hjfto": {"reached_s": 24.8, "duration_s": 25.1, "hard_cuts": 7, "rms_p10": 0.0657, "rms_median": 0.1364, "rms_p90": 0.1953, "share_below_0_01": 0.0},
    "1bb5M4E1oQs": {"reached_s": 41.8, "duration_s": 42.0, "hard_cuts": 3, "rms_p10": 0.0493, "rms_median": 0.0903, "rms_p90": 0.1664, "share_below_0_01": 0.021},
    "j9VqMB6yTXQ": {"reached_s": 46.0, "duration_s": 46.1, "hard_cuts": 1, "rms_p10": 0.0331, "rms_median": 0.0888, "rms_p90": 0.1723, "share_below_0_01": 0.0},
    "nPqrcrxdrdE": {"reached_s": 31.1, "duration_s": 31.3, "hard_cuts": 3, "rms_p10": 0.007, "rms_median": 0.1157, "rms_p90": 0.227, "share_below_0_01": 0.152},
    "UeGxF8-hb2s": {"reached_s": 88.7, "duration_s": 88.8, "hard_cuts": 6, "rms_p10": 0.0, "rms_median": 0.0333, "rms_p90": 0.1688, "share_below_0_01": 0.438},
    "qObP1FPrC6Q": {"reached_s": 59.8, "duration_s": 60.0, "hard_cuts": 3, "rms_p10": 0.0152, "rms_median": 0.1273, "rms_p90": 0.199, "share_below_0_01": 0.074, "dark_share": 0.0},
    "b-dam2LdHzM": {"reached_s": 58.4, "duration_s": 58.7, "hard_cuts": 2, "rms_p10": 0.0113, "rms_median": 0.0594, "rms_p90": 0.1748, "share_below_0_01": 0.054, "dark_share": 0.0},
    "78JR_U-6HfQ": {"reached_s": 183.1, "duration_s": 183.1, "hard_cuts": 60, "rms_p10": 0.0824, "rms_median": 0.1511, "rms_p90": 0.2233, "share_below_0_01": 0.0, "dark_share": 0.0},
}


def signal_summary(video_id: str) -> dict | None:
    sp = SIGNAL_PASS.get(video_id)
    if not sp:
        return None
    gaps = "natural speech gaps present" if sp["share_below_0_01"] >= 0.05 else "almost no near-silent samples (consistent with a background bed or heavy compression; not heard)"
    return {
        **sp,
        "method": "Continuous 2x playback to the end, audio routed to an analyser only; hard-cut detector on downscaled frames. Fades and overlay changes are not counted as cuts.",
        "cuts_per_minute": round(60 * sp["hard_cuts"] / sp["duration_s"], 1),
        "audio_level_reading": gaps,
    }


# Caption-track defects found by scanning the 56 retained caption transcripts (2026-09-28).
CAPTION_TIMECODE_IDS = {"r9ZyUWyY4Lc", "iltS1TPt4jo", "p_iI0enaFX8", "4ByUo2N_C-I", "TPVOIfcJl-k", "sUL6SU8LnEg", "phSq6PkPtIg", "VlSibJdSZF8", "Nf9pCrPYWyQ", "FVfG_HZV4qg"}
CAPTION_EMOJI_IDS = {"hUSVbcHVeVw", "FDLU7tX7qNM"}

NEXT_TASK = (
    "Batch 7 (tf7f4RhQwtc, xI-KdZ96xcI, Nf9pCrPYWyQ, qC8BKb8Fh5Q plus no-curve jxoMnTrVziA, jLEp6jDsN3Q, Uq3T8YZgyTw, zESWa7FJgHY), "
    "and Batch 8 (no-curve phSq6PkPtIg, sC_0XjL2z_Y, VlSibJdSZF8, tDZKHR8UjYg)."
)


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
    "qObP1FPrC6Q": "Dark vertical design: 7:01/7:00 clock and rising glucose line dominate above 7 AM SPIKE?; doctor cutout and hands support the hook, but two clock readings create avoidable ambiguity.",
    "b-dam2LdHzM": "Warm vertical breakfast scene with oats, a red rising glucose line and HEALTHY? SPIKE?; concrete food prop makes the metabolic question legible at small size.",
    "78JR_U-6HfQ": "Wide composite: older man on stairs, white-coat doctor and glowing heart under a long CARDIOLOGIST WARNS headline; high urgency but too much text for a small thumbnail.",
    "3dRcNqiLHgY": "Wide two-person composition: older man clutching chest beside Dr. Rehan, with NO SEVERE PAIN? in large red/white type; symptom contradiction is immediate and title-aligned.",
    "r9ZyUWyY4Lc": "Wide doctor-and-props layout: DOES THIS WORK?, ACV bottle and glucose meter reading 160; clear test question, though three focal objects compete.",
    "HzFdyjyEFTY": "Wide clinical montage with older couple taking pills, Dr. Rehan and SAME PILL? DIFFERENT STORY.; primary-versus-secondary distinction is implied but not disclosed.",
    "PIsyBj58fJA": "Wide doctor clutching shoulder beside an older woman and exercise ghost image; AFTER 60 FROZEN SHOULDER? is large, direct and accurately matched to the demonstration.",
    "RD7ugxaBHSQ": "Wide calf/vein illustration beside walking doctor and KEEP BLOOD MOVING; strong circulation cue, but thumbnail does not disclose the later modified-push-up segment.",
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
    {"pair": "Ozempic long-form", "stronger_id": "8JdBlF-ragM", "comparison_id": "sUL6SU8LnEg", "evidence": "30-second retention 55.74% vs 40.0%; end 45.9% vs 10.0%; derived APV 46.0% vs 28.3%; views 78 vs 10; duration 71 vs 166 s.", "interpretation": "Specific side-effect question with frequent visual change versus abstract myth-debunk with clinical terms and raw caption timecodes; duration and a 10-view sample dominate the uncertainty."},
    {"pair": "Circulation long-form", "stronger_id": "NznebmgFwXI", "comparison_id": "KPYHy7MDmLM", "evidence": "Retention at 3 s 87.1% vs 57.89%; 30 s 41.13% vs 36.84%; views 132 vs 20; hard cuts 2 vs 33.", "interpretation": "Counterexample to pace-driven advice: the near-single-take video with a concrete symptom question held more early viewers than the fast-cut, text-heavy generic warning."},
    {"pair": "Artery foods (Short vs long-form)", "stronger_id": "hUSVbcHVeVw", "comparison_id": "CZ3gAUzdTAg", "evidence": "Short: 30 s 59.87%, stayed 39.7%, 414 views, CTR 0.63%. Long-form: 30 s 43.92%, end 10.39%, 367 views from 5,737 impressions at 3.7% CTR.", "interpretation": "Same list topic in two formats; not a like-for-like retention comparison. The long-form delays the first item to about 0:43; the Short title over-claims (reverse) relative to its captions (support)."},
    {"pair": "Ankle/calf Shorts", "stronger_id": "p_iI0enaFX8", "comparison_id": "FDLU7tX7qNM", "evidence": "30 s 81.82% vs 18.77%; stayed 46.2% vs 44.0%; views 18 vs 805.", "interpretation": "Not interpretable as a production effect: 18 views means one viewer per 9.1-pt step. FDLU7tX7qNM reached a broad feed audience and new viewers held far worse than returning viewers (17.78% vs 46.15%)."},
    {"pair": "Coffee clip family", "stronger_id": "fAwh2svMARM", "comparison_id": "nRdBvyh7Sy0", "evidence": "Parent long-form: 30 s 70.37%, end 22.22%, 48 views from 287 impressions. Short excerpt: stayed 40.9%, APV 78.6%, 25 views; no retention curve disclosed.", "interpretation": "The parent holds unusually well but reached few viewers; its Shorts, including this one, redistribute the same footage. The Short's curve is unavailable, so no timestamp comparison is possible."},
    {"pair": "Ozempic Shorts", "stronger_id": "nP9fDHP1jbo", "comparison_id": "7MXBh2hjfto", "evidence": "End retention 15.93% vs 6.25%; retention at 10 s 35.4% vs 46.88%; views 490 vs 216.", "interpretation": "Both lose most viewers at 4-8 s as the answer is declared; 7MXBh2hjfto's title promises a comparison with appetite suppressants that its content does not deliver at sampled anchors."},
    {"pair": "Potassium Shorts (same shoot)", "stronger_id": "1bb5M4E1oQs", "comparison_id": "j9VqMB6yTXQ", "evidence": "1bb5M4E1oQs: 30 s 36.36%, stayed 46.2%, 23 views; j9VqMB6yTXQ: no curve, 21 views, 0% recorded CTR.", "interpretation": "Mystery opener versus definition-first opener from the same chair shoot; curve missing for one side, so this is descriptive only."},
    {"pair": "Walking Shorts", "stronger_id": "nPqrcrxdrdE", "comparison_id": "UeGxF8-hb2s", "evidence": "End retention 20.0% vs 7.69%; views 171 vs 34; UeGxF8-hb2s is black and near-silent from 0:50 to 1:28.", "interpretation": "The weaker video's end retention is an export defect, not a content judgement: it held 69.23% at 30 s, better than nPqrcrxdrdE's 26.67% at its 30 s end."},
    {"pair": "Diabetes Shorts", "stronger_id": "b-dam2LdHzM", "comparison_id": "qObP1FPrC6Q", "evidence": "b-dam2LdHzM: stayed 25.8%, APV 65.5%, 30 s 64.71%, end 35.29%, 64 views. qObP1FPrC6Q: stayed 34.2%, APV 55.3%, 30 s 46.15%, end 15.38%, 36 views.", "interpretation": "Feed acceptance and post-swipe depth diverge: the illustrated morning-spike Short stopped more swipes, while the concrete oatmeal/candy comparison retained more of those who stayed. Samples, titles and topics differ; no success formula follows."},
    {"pair": "Heart-risk long-form", "stronger_id": "78JR_U-6HfQ", "comparison_id": "3dRcNqiLHgY", "evidence": "78JR_U-6HfQ: 3 s 84.85%, 10 s 72.73%, 30 s 54.55%, end 15.15%, 37 views, 60 detected cuts. 3dRcNqiLHgY: 3 s 76.19%, 10 s 52.38%, 30 s 38.1%, end 19.05%, 24 views; no comparable signal pass.", "interpretation": "The faster edit also opens with a specific morning-safety question and promised habit; the weaker video spends its opening on repeated importance/mortality setup. Topic, packaging, view count and missing matched signal data prevent attributing the difference to pace."},
    {"pair": "Medication/food advice long-form", "stronger_id": "r9ZyUWyY4Lc", "comparison_id": "HzFdyjyEFTY", "evidence": "At 10 s: 89.16% vs 86.11%; 30 s: 67.47% vs 66.67%; end: 25.3% vs 19.44%; views 113 vs 50; CTR 4.64% vs 1.35%.", "interpretation": "Early curves are effectively similar despite white motion graphics versus a clinic talking head. The small end difference can reflect topic intent, title/traffic selection, runtime or audience; it is not evidence that one visual style wins."},
    {"pair": "Outdoor mobility demonstrations", "stronger_id": "PIsyBj58fJA", "comparison_id": "RD7ugxaBHSQ", "evidence": "PIsyBj58fJA: 30 s 82.35%, end 17.65%, 18 views. RD7ugxaBHSQ: 10 s 76.19%, 30 s 47.62%, end 23.81%, 29 views.", "interpretation": "Both use vertical outdoor demonstrations and side-panel instructions. The shoulder video stays on its promised routine; the calf video switches to modified push-ups. The 18- and 29-view curves are too coarse to isolate title alignment, exercise type or production."},
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
    "LIMITED_BY_UNAVAILABLE_EVIDENCE": "Numeric playback anchors meet the coverage rule but Studio disclosed no retention curve, so no anchor can be tied to viewer loss; playback_audit.status gives the playback method.",
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
        "continuous_signal_pass": signal_summary(video_id),
        "audio": (f"Not heard. Level-only measurement over continuous 2x playback: {signal_summary(video_id)['audio_level_reading']}. Speech content is taken from on-screen captions." if video_id in SIGNAL_PASS else "Muted; audio not heard. Speech content is taken from on-screen captions at each anchor.") if sampled else "Playback completed, but no isolated headphone/loudness/noise measurement was made.",
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
        elif vid in SIGNAL_PASS:
            remaining.append("Seek-sampled frames plus a continuous level/cut pass; speech and music were not heard and no complete audiovisual editing review exists")
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
            "completion_states": {
                "transcript_analysis": "STRUCTURAL_ANALYSIS_REUSED",
                "thumbnail_inspection": observation["quality_status"],
                "retention_analysis": "CONTENT_LINKED" if status == "RETENTION_ANALYZED" else ("NO_CURVE_DISCLOSED" if not retention_record or retention_record.get("curve_status") != "AVAILABLE" else "CURVE_NOT_YET_LINKED"),
                "sampled_playback": "COMPLETE" if vid in SEEK_SAMPLED else ("REPORTED_FULL_PLAYBACK" if audit else "NOT_STARTED"),
                "continuous_signal_pass": "COMPLETE_LEVELS_AND_CUTS_ONLY" if vid in SIGNAL_PASS else "NOT_STARTED",
                "complete_audiovisual_editing_review": "NOT_VERIFIED",
            },
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
            "continuous_signal_passes": sum(r["video_id"] in SIGNAL_PASS for r in records),
            "complete_audiovisual_audits_verified": sum(r["completion_states"]["complete_audiovisual_editing_review"] == "COMPLETE" for r in records),
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
        "exact_next_unfinished_task": NEXT_TASK,
        "batch_history": [
            {"batch": "Batch 1 Recovery and Analytics", "status": "COMPLETE_WITH_LIMITATIONS", "saved_at": "2026-09-28", "result": "Four original Studio ZIPs verified; 56 basic per-video rows joined; 47 extended rows observed; missing Short resolved."},
            {"batch": "Batch 2 Retention and Actual Playback", "status": "PARTIAL", "saved_at": "2026-09-28", "result": "56 retention exports, 46 curves; 12 saved playback records, of which 8 meet RETENTION_ANALYZED and 4 long-form records are PARTIAL_PLAYBACK (too few numeric anchors); 44 TRANSCRIPT_ONLY. -SjQc2MwaOU and HEJoPEEndG8 anchors gap-filled 2026-09-28."},
            {"batch": "Batch 2b Partial playback gap-fill", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "5oPzZjfNgII, EB3_A2b4a6o, BCNWQ3uuSuE and SBrMW71O69U given numeric anchors at every exported retention event (7-11 anchors each) by muted seek-and-inspect; all four now RETENTION_ANALYZED."},
            {"batch": "Batch 3b Matched pairs (seek-sampled)", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "8 TRANSCRIPT_ONLY videos in 4 matched pairs seek-sampled at retention events: YVjbjcVo1is/iltS1TPt4jo (same footage, re-edited), fArHBQo6Ggw/tD4KOpsJH_c, qbwCkH_GqhU/TPVOIfcJl-k, t1j-p9pkw3Y/VrbLuTNi0qE. Audience-segment curves summarized from retained exports for all 56."},
            {"batch": "Batch 4 Matched pairs (seek-sampled plus continuous signal pass)", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "8JdBlF-ragM/sUL6SU8LnEg, NznebmgFwXI/KPYHy7MDmLM, hUSVbcHVeVw/CZ3gAUzdTAg and p_iI0enaFX8/FDLU7tX7qNM seek-sampled at retention events and played continuously at 2x through a level-and-cut analyser. Caption-track defects scanned across all 56 transcripts; reused-footage scan across all 56."},
            {"batch": "Batch 5 Coffee clips, Ozempic, potassium and walking Shorts", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "fAwh2svMARM/nRdBvyh7Sy0, nP9fDHP1jbo/7MXBh2hjfto, 1bb5M4E1oQs/j9VqMB6yTXQ and nPqrcrxdrdE/UeGxF8-hb2s seek-sampled plus continuous signal pass; two no-curve videos recorded as LIMITED_BY_UNAVAILABLE_EVIDENCE. Found a 39 s black tail in UeGxF8-hb2s and a title-content mismatch in 7MXBh2hjfto."},
            {"batch": "Batch 6 Diabetes, heart-risk, medication and outdoor-mobility pairs", "status": "COMPLETE_WITH_AUDIO_LIMITATIONS", "saved_at": "2026-09-28", "result": "qObP1FPrC6Q/b-dam2LdHzM, 78JR_U-6HfQ/3dRcNqiLHgY, r9ZyUWyY4Lc/HzFdyjyEFTY and PIsyBj58fJA/RD7ugxaBHSQ seek-sampled at retained curve events. Three preserved signal passes were registered; current read-only browser did not expose audio/canvas instrumentation for the other five. Audio was not heard. All eight thumbnails were revalidated."},
            {"batch": "Batch 3 Research Diagnosis and Deliverables", "status": "COMPLETE_FOR_AVAILABLE_SYNTHESIS", "saved_at": "2026-09-28", "result": "Three Trends comparisons verified; six matched comparisons synthesized; diagnosis and four existing deliverables reconciled."},
        ],
        "execution_matrix": [
            {"task": "Metadata", "previous_result": "56 records", "current_evidence": "56 exact canonical Video IDs; current public catalog still 56 on 2026-09-28", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Transcripts", "previous_result": "56", "current_evidence": "56 original transcript files present", "status": "VERIFIED_COMPLETE", "required_action": "Reuse; do not reread wholesale"},
            {"task": "Thumbnails", "previous_result": "56", "current_evidence": "56 images identity-verified; 12 priority observations revalidated; 44 contain templated commentary", "status": "COMPLETE_NEEDS_CORRECTION", "required_action": "Revalidate remaining 44 only when they enter a priority comparison"},
            {"task": "Studio reports", "previous_result": "Four reported", "current_evidence": "Lifetime, 90d, 28d and traffic-source ZIP hashes verified", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Individual Analytics", "previous_result": "55 references reported", "current_evidence": "56 file-backed basic rows; 47 authenticated extended rows; 9 extended rows not captured", "status": "PARTIAL", "required_action": "Capture remaining extended rows only if Studio table/export becomes reliable"},
            {"task": "Retention", "previous_result": "Previously missing", "current_evidence": f"56 exports; 46 curves; {register['counts']['retention_content_linked_investigations']} content-linked investigations; 10 no-curve disclosures; {register['counts']['retention_new_vs_returning_split']} exports carry a new-vs-returning split", "status": "PARTIAL", "required_action": f"Link remaining {46 - register['counts']['retention_content_linked_investigations']} curves during playback; no action possible for 10 blank curves"},
            {"task": "Playback", "previous_result": "Previously missing", "current_evidence": f"{register['counts']['playback_reported_full']} reported full-playback records (text-only completion evidence) and {register['counts']['playback_seek_sampled']} seek-sampled records", "status": "PARTIAL", "required_action": f"Audit remaining {register['counts']['investigation_status']['TRANSCRIPT_ONLY']} TRANSCRIPT_ONLY videos"},
            {"task": "Trends", "previous_result": "Three comparisons", "current_evidence": "Three original official CSVs and configurations verified", "status": "VERIFIED_COMPLETE", "required_action": "No repeat query justified by available source detail"},
            {"task": "Research synthesis", "previous_result": "Partial", "current_evidence": f"{len(MATCHED_COMPARISONS)} matched comparisons and multi-stage diagnosis; audience/query/device/geography gaps remain", "status": "PARTIAL", "required_action": "Revisit only if unavailable Studio reports become accessible"},
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
            {"finding": "Caption-track defects are widespread but not associated with a consistent retention pattern", "video_ids": sorted(CAPTION_TIMECODE_IDS | CAPTION_EMOJI_IDS), "metrics": "Raw (m:ss) timecodes appear in 10 of 56 caption transcripts (5 Shorts, 5 long-form); emoji and a heading line appear in 2 more (hUSVbcHVeVw, FDLU7tX7qNM). Median compared-to-other-videos value at 30 s: timecode Shorts -27.49 vs other Shorts 7.93; timecode long-form 7.6 vs other long-form -30.81.", "visual_and_transcript_evidence": "Timecodes were seen on screen in iltS1TPt4jo, TPVOIfcJl-k, sUL6SU8LnEg and p_iI0enaFX8 during playback; the pattern suggests pasted script or chapter text uploaded as captions", "comparative_evidence": "Direction flips between formats", "historical_context": "Defect spans February to September 2026 uploads", "counterexample": "FVfG_HZV4qg has the defect and the second-highest Short view count (1,068) with 51.1% stayed-to-watch", "alternative_explanations": "Most viewers watch without captions; group sizes are 3-19", "confidence": "HIGH that the defect exists; LOW for any retention effect", "practical_experiment": "Replace the caption tracks on affected videos (a quality fix that needs no test) and do not attribute retention changes to it."},
            {"finding": "Footage reuse is concentrated in the coffee cluster and one heart-attack re-edit", "video_ids": ["fAwh2svMARM", "QfRaG71ZA_0", "4ByUo2N_C-I", "fArHBQo6Ggw", "nRdBvyh7Sy0", "YVjbjcVo1is", "iltS1TPt4jo"], "metrics": "10-word transcript overlap: YVjbjcVo1is/iltS1TPt4jo 0.75; long-form fAwh2svMARM shares 0.33-0.49 with four coffee Shorts; no other pair exceeds 0.15", "visual_and_transcript_evidence": "Coffee Shorts are excerpts of the long-form coffee video; iltS1TPt4jo adds an illustrated cold open to YVjbjcVo1is footage", "comparative_evidence": "Four coffee Shorts drew 25-341 views each versus 48 for their long-form parent; stayed-to-watch 40.9-57.3%", "historical_context": "Parent published 2026-08-25; Shorts 2026-09-09 to 2026-09-18", "counterexample": "The same source footage produced both the strongest (QfRaG71ZA_0) and a weaker (4ByUo2N_C-I) coffee Short, so the excerpt and package matter more than the footage", "alternative_explanations": "Different excerpts, titles and publication dates", "confidence": "HIGH for reuse; MEDIUM for excerpt choice mattering", "practical_experiment": "When clipping a long-form video, test excerpts that open on a named symptom or viewer qualifier against excerpts that open on a definition."},
            {"finding": "Fast cutting is not a reliable retention lever in this catalog", "video_ids": ["NznebmgFwXI", "KPYHy7MDmLM", "CZ3gAUzdTAg", "8JdBlF-ragM"], "metrics": "Hard cuts per minute: NznebmgFwXI 0.8 (3 s retention 87.1%), KPYHy7MDmLM 16.9 (57.89%), CZ3gAUzdTAg 18.3 (88.72% but 43.92% at 30 s), 8JdBlF-ragM 18.8 (78.69%, 55.74% at 30 s)", "visual_and_transcript_evidence": "The near-single-take video opens on a concrete self-check symptom; the fast-cut weaker video opens on a generic warning with three text layers", "comparative_evidence": "DS-000018 creator advice favours frequent pattern interrupts; this pair contradicts it at the opening", "historical_context": "Continuous 2x signal pass on 8 videos, 2026-09-28", "counterexample": "8JdBlF-ragM is fast-cut and holds well", "alternative_explanations": "Topic, title promise and tiny samples (20-132 views)", "confidence": "MEDIUM that pace alone does not explain opening loss; LOW for any causal claim", "practical_experiment": "Hold pace constant and vary only the first sentence (specific symptom question versus generic warning)."},
            {"finding": "Export and packaging defects remove viewers independently of content quality", "video_ids": ["UeGxF8-hb2s", "7MXBh2hjfto", "hUSVbcHVeVw"], "metrics": "UeGxF8-hb2s is black and near-silent for its final 39 s (44% of runtime): 69.23% retained at 30 s, 7.69% at end, APV 51.3%. 7MXBh2hjfto's title promises an appetite-suppressant comparison but its content debunks a cancer myth; end retention 6.25%.", "visual_and_transcript_evidence": "Frame luminance 0 from 50 s to 80 s in UeGxF8-hb2s; sampled 7MXBh2hjfto anchors show only cancer-myth content", "comparative_evidence": "Transcript word density flags Uq3T8YZgyTw (1.8 words/s against a catalog median of 2.86) as the next candidate for the same tail defect", "historical_context": "UeGxF8-hb2s published 2026-09-01; 7MXBh2hjfto 2026-02-25", "counterexample": "UeGxF8-hb2s held well while content lasted, so the defect affects APV and end retention rather than the opening", "alternative_explanations": "Tiny samples (34 and 216 views)", "confidence": "HIGH that the defects exist; MEDIUM that they depress APV; LOW for distribution effects", "practical_experiment": "Re-export or trim UeGxF8-hb2s and check uploads for trailing black; align 7MXBh2hjfto's title with its content."},
        ],
        "retention_export_summary": {key: retention[key] for key in ("record_count", "available_count", "curve_available_count", "exported_no_curve_count")},
        "remaining_private_requirements": ["Returning-viewer and viewers-across-formats channel reports", "Search query and suggested-video detail", "Geography and device reports", "Nine uncaptured extended per-video rows if a reliable export becomes available"],
        "preservation": {"raw_private_exports_modified": False, "credentials_saved": False, "remote_push_performed": False, "note": "Only derived docs/research artifacts and supporting scripts were updated."},
    }
    (OUT_DIR / "Decode_Your_Heart_Video_Evidence_Register.json").write_text(json.dumps(register, indent=2) + "\n")
    (OUT_DIR / "Decode_Your_Heart_Research_Checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n")


if __name__ == "__main__":
    main()
