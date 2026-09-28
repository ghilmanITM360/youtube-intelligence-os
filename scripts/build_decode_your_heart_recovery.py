#!/usr/bin/env python3
"""Build evidence-backed recovery artifacts for DS-000032 without changing raw sources."""

from __future__ import annotations

import csv
from collections import Counter
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
EXTENDED_STUDIO_ARCHIVE = ROOT / "data/raw/first-party/youtube-studio/DS-000032/2026-09-28/studio-advanced-content-lifetime-extended.zip"
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
LIVE_STUDIO_METRICS_FALLBACK = {
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
    "tf7f4RhQwtc": {
        "duration_seconds": 154,
        "comparison": "Batch 7 obesity explainer with an exported retention curve",
        "timestamps": ["0:03 seated doctor in blue scrubs; NOT JUST WEIGHT/obesity-management framing while the curve falls 18.89 points", "0:05 same clinic shot and kinetic captions; another 7.78-point curve step", "0:12 doctor names obesity as an independent disease", "0:30 400 METABOLIC DISEASES text over the unchanged doctor shot", "1:15 clinician continues a dense cause/risk list", "2:00 exercise/diet advice after most viewers have already left", "2:30 closing summary with heart/brain icons"],
        "opening": "Asks whether belly fat causes tiredness, then moves into obesity importance and disease classification before practical advice.",
        "visuals": "Stable pillarboxed clinic talking head with burned captions, large kinetic phrases and occasional body/organ or patient cutouts.",
        "editing": "Visual changes are overlay-driven; the doctor, desk and background remain nearly fixed across sampled anchors.",
        "closing": "Ends after broad obesity-management advice without a sampled standalone end card.",
        "possible_explanation": "The curve drops from 98.89% at start to 68.89% by 3 seconds, 31.11% at 30 seconds and 7.78% at end while the opening is still framing obesity broadly. The early loss is observable, but the sample does not isolate the wording, topic or feed cohort.",
        "alternative_explanation": "Only 91 views; title promise, traffic source, audience intent and publication context remain uncontrolled.",
    },
    "xI-KdZ96xcI": {
        "duration_seconds": 256,
        "comparison": "Batch 7 heart-failure list with an exported retention curve",
        "timestamps": ["0:03 seated doctor in a book-lined office; opening warning that heart failure does not happen instantly", "0:05 same direct-to-camera frame; curve has already lost 31.25 points by about 0:03", "0:13 doctor explains the body warns weeks or months earlier", "0:30 7 EARLY WARNING SIGNS card before the first sign", "1:30 numbered irregular-heartbeat label over the same shot", "2:30 swollen-ankle cutout and symptom explanation", "3:30 LOOK FOR PATTERN card during multi-symptom synthesis", "4:10 next-video recommendation overlays the doctor"],
        "opening": "Promises seven warning signs and emphasizes that people ignore them, but the first numbered sign arrives only after an extended setup and credential introduction.",
        "visuals": "Stable seated-doctor office shot with large numbered labels, kinetic summary cards and occasional symptom cutouts.",
        "editing": "Single-camera delivery with overlay swaps; no continuous cut or audible-content pass was available.",
        "closing": "Synthesizes symptom combinations, gives a patient example and promotes the next sleeping-habit video.",
        "possible_explanation": "Retention is 65.63% at 3 seconds, 31.25% at 30 seconds and 21.88% at end. The steepest early loss occurs during the warning/setup before the first symptom, but that timing is associative, not causal.",
        "alternative_explanation": "Only 33 views; broad title traffic, medical concern level and viewer cohort can create the same curve.",
    },
    "Nf9pCrPYWyQ": {
        "duration_seconds": 149,
        "comparison": "Batch 7 World Obesity Day explainer with an exported retention curve",
        "timestamps": ["0:03 doctor at a desk under 4 BILLION BY 2035; 3-second retention is 80.77%", "0:12 same desk shot as the date/event setup begins", "0:13 World Obesity Day framing; exported curve has an 11.54-point step", "0:30 WE DON'T CELEBRATE OBESITY card while explaining the event name", "0:55 1 BILLION/current prevalence claim", "1:12 +115% SINCE 1975 card", "2:00 policy and community response", "2:25 end-screen cards overlap the last recommendations"],
        "opening": "Leads with a specific future prevalence statistic, then explains the World Obesity Day occasion and why celebration is a misnomer.",
        "visuals": "Seated doctor at a desk with large statistics, bold white/red/yellow kinetic text and occasional infographic overlays.",
        "editing": "Stable direct-to-camera base with frequent metric cards; retained transcript visibly contains literal timecodes, but captions were not enabled in the sampled player frames.",
        "closing": "Moves from policy to lifestyle recommendations, then suggested-video cards cover the final seconds.",
        "possible_explanation": "Retention holds at 80.77% through 5 seconds, reaches 42.31% at 30 seconds and 19.23% at end. A later 0:12-0:13 step coincides with the calendar/event transition, not proof viewers rejected it.",
        "alternative_explanation": "Only 27 views; World Obesity Day timing and a 7.22% CTR may have selected a narrow, motivated cohort.",
    },
    "qC8BKb8Fh5Q": {
        "duration_seconds": 113,
        "comparison": "Batch 7 banana/blood-pressure explainer with an exported retention curve",
        "timestamps": ["0:02 BLOOD PRESSURE card over seated doctor; 3-second retention is 77.14%", "0:07 doctor gestures while positioning a simple non-medication intervention", "0:18 CORONARY ARTERY DISEASE/heart-failure icons during credential and scope setup", "0:31 bowl-of-fruit cutout before the banana reveal", "1:01 LESS SALT card during sodium/potassium balance", "1:41 3 MORE FRUITS card after the main banana explanation", "1:49 end cards begin and the player loops shortly after"],
        "opening": "Promises a simple fruit for blood pressure, introduces the cardiologist and delays the banana reveal until after broad heart-health framing.",
        "visuals": "Stable office talking head with large kinetic labels, blood-pressure/heart icons and fruit cutouts.",
        "editing": "Overlay-driven variation on one camera angle; the sampled player looped after the end, so the final anchor is documented at the pre-loop end-card transition.",
        "closing": "Expands to berries, oranges and avocados, warns that no food replaces care, then tees up a heart-failure video.",
        "possible_explanation": "Retention falls from 77.14% at 3 seconds to 31.43% at 30 seconds and 8.57% at end while the promised banana is still being delayed by setup. Delay is one plausible explanation, not established cause.",
        "alternative_explanation": "Only 35 views; a food-specific title can attract different intent than the broader narration, and curve steps are coarse.",
    },
    "jxoMnTrVziA": {
        "duration_seconds": 30,
        "comparison": "Batch 7 no-curve 10-second balance-test Short",
        "timestamps": ["0:03 doctor in vertical office frame; TRY THIS prompt", "0:08 orange 10-SECOND BALANCE / TRY THIS NOW card", "0:18 outdoor older-adult one-leg balance demonstration", "0:23 doctor returns with STRUGGLING? warning", "0:29 final doctor frame points viewers to the full video"],
        "opening": "Immediately asks viewers to try a ten-second balance test.",
        "visuals": "Vertical doctor-led Short alternating with a full-frame orange test card and outdoor older-adult balance footage; bold burned captions.",
        "editing": "Multiple scene changes in 29 seconds, but no continuous cut count or audible-content review was available.",
        "closing": "Says balance can improve and points to a full video.",
        "possible_explanation": "Public playback verifies a complete self-test structure, but Studio exported no retention curve, so no visual event can be linked to viewer loss.",
        "alternative_explanation": "Eight basic-export views and six later live-table views are both tiny; metrics may cover different refresh states.",
    },
    "jLEp6jDsN3Q": {
        "duration_seconds": 56,
        "comparison": "Batch 7 no-curve heart-attack warning Short",
        "timestamps": ["0:03 vertical clinic shot with Cardiovascular diseases kinetic words", "0:10 same doctor shot while introducing mortality and heart attack", "0:20 PAIN + SWEAT? style words animate over the doctor", "0:35 immediate-help instruction and symptom sequence", "0:50 red subscribe end card begins", "0:55 subscribe card remains at the player end"],
        "opening": "Begins with global cardiovascular mortality before naming the actionable heart-attack warning signs.",
        "visuals": "Pillarboxed vertical doctor shot with sentence fragments appearing in mixed red, white and yellow type, followed by a red subscribe card.",
        "editing": "Near-single-shot explanation; visual motion comes from kinetic typography and the final card.",
        "closing": "Directs urgent symptoms to a cardiovascular hospital, then asks viewers to watch more and subscribe.",
        "possible_explanation": "Public playback verifies the symptom sequence and long subscribe ending, but no retention curve was disclosed, so their audience effect is unknown.",
        "alternative_explanation": "Nineteen basic-export views versus eight later live-table views show an unstable tiny sample or differing refresh/window state.",
    },
    "Uq3T8YZgyTw": {
        "duration_seconds": 51,
        "comparison": "Batch 7 no-curve three-move Short and black-tail countercheck",
        "timestamps": ["0:04 full-height OVER 50? CAN YOU DO ALL 3? infographic with jumping-jack, side-leg-raise and squat panels", "0:08 same static infographic", "0:21 same infographic while the transcript moves into side leg raises", "0:32 same infographic during squat instructions", "0:41 same infographic during the closing question", "0:47 white Thanks for Watching card with Like/Comment/Share/Subscribe buttons", "0:50 the same white engagement card remains visible less than one second before the 50.82-second end"],
        "opening": "Presents all three exercises immediately on one tall infographic.",
        "visuals": "Static full-height exercise infographic for most of the runtime, then a white engagement card; no demonstrated moving exercise footage was visible at sampled anchors.",
        "editing": "Essentially two visual states: the exercise infographic and the closing engagement card.",
        "closing": "White Thanks for Watching engagement card occupies roughly the last four seconds.",
        "possible_explanation": "The suspected black-tail defect does not recur here: frames at 47.1 and 49.8 seconds show a white engagement card, not black. Studio exported no retention curve, so the static design cannot be tied to loss.",
        "alternative_explanation": "Six basic-export views and three later live-table views are too small for any performance conclusion; audible content was not assessed.",
    },
    "zESWa7FJgHY": {
        "duration_seconds": 197,
        "comparison": "Batch 7 no-curve outdoor back-exercise demonstration",
        "timestamps": ["0:05 outdoor vertical shot; doctor seated on a mat beside 1 IN 3 PATIENTS", "0:16 same location with LET'S FIX IT", "0:32 STEP 1: RELAX NECK beside the demonstration setup", "1:01 upward-facing-dog form cue; STRAIGHT LINE SHOULDER–ELBOW–WRIST", "1:53 leg-raise/bird-dog demonstration", "2:31 child's-pose or floor-mobility sequence", "3:12 suggested-video and subscribe overlays cover the outdoor ending"],
        "opening": "Explains backache prevalence and posture causes before beginning a sequence of five exercises.",
        "visuals": "Vertical outdoor mat demonstration with white side panels, numbered exercise names, form cues and small anatomy/exercise illustrations.",
        "editing": "Exercise-to-exercise progression within one outdoor location; no continuous cut count or audible-content review was available.",
        "closing": "Finishes the last floor exercise and claims the routine will reduce pain while end cards appear.",
        "possible_explanation": "Public playback verifies a concrete multi-exercise demonstration, but Studio exported no curve and only six views, so no retention inference is possible.",
        "alternative_explanation": "Topic, safety suitability, title promise and traffic source are unmeasured confounders; the medical/exercise claims were not clinically validated here.",
    },
    "phSq6PkPtIg": {
        "duration_seconds": 15,
        "comparison": "Batch 8 no-curve Ozempic mechanism Short",
        "timestamps": ["0:02 doctor at a desk asks why weight gain occurs after stopping Ozempic", "0:05 split frame introduces a brain-to-gut illustration", "0:09 hypothalamus diagram identifies the satiety center", "0:13 stimulation stop graphic over a body silhouette", "0:14 brain/gut illustration remains through the 14.86-second end"],
        "opening": "Asks the exact post-Ozempic weight-regain question immediately.",
        "visuals": "Horizontal split layout with doctor on the right and simplified brain, gut and hypothalamus diagrams on the left; captions are burned along the bottom.",
        "editing": "Very short answer-first explainer with rapid medical-illustration substitutions; no continuous cut count or audible-content review was available.",
        "closing": "Ends on the claimed hypothalamic/satiety mechanism without a separate call-to-action card.",
        "possible_explanation": "The retained transcript contains literal 0:21 and 0:27 timecodes even though the public video lasts only 14.86 seconds, showing a caption-source/timecode defect. Studio disclosed no retention curve, so its viewer effect is unknown.",
        "alternative_explanation": "Seven views and 6.25% CTR are too small for performance inference; the clinical mechanism was not independently validated.",
    },
    "sC_0XjL2z_Y": {
        "duration_seconds": 175,
        "comparison": "Batch 8 no-curve kidney-number explainer",
        "timestamps": ["0:06 doctor seated in a clinic room; diabetes/high-blood-pressure laboratory-test setup", "0:16 same shot introduces eGFR", "0:33 BODY WEIGHT/COEFFICIENT/CREATININE labels around the doctor", "1:03 ALBUMIN = PROTEIN card during uACR explanation", "1:44 clinician contrasts individual tests with holistic interpretation", "2:23 KIDNEY FUNCTION MATTERS card", "2:51 suggested-video thumbnails and a large subscribe overlay cover the close"],
        "opening": "Qualifies viewers with diabetes or hypertension, then introduces eGFR and uACR as two kidney measurements.",
        "visuals": "Pillarboxed clinic talking head with large highlighted terms and occasional lab/organ overlays.",
        "editing": "Stable single-camera explanation; typography provides most visual change before an intrusive end-screen overlay.",
        "closing": "Connects kidney status to medication dosing/cardiorenal risk, then asks viewers to subscribe under suggested-video cards.",
        "possible_explanation": "Public playback verifies the two-test explanation, but Studio exported no retention curve and only six views; no timestamp can be linked to audience loss.",
        "alternative_explanation": "The acquisition title differs from the current public title (now Diabetes or High Blood Pressure? Know These 2 Kidney Numbers), so later packaging changed and cannot be separated from content performance.",
    },
    "VlSibJdSZF8": {
        "duration_seconds": 80,
        "comparison": "Batch 8 no-curve Ozempic weight-regain long-form clip",
        "timestamps": ["0:05 doctor at a desk with OZEMPIC (GLP-1 RECEPTOR...) kinetic label", "0:12 same shot asks WHAT HAPPENS WHEN YOU STOP", "0:17 EFFECT LAST LIFELONG label", "0:30 REGAINS WEIGHT during the post-stop outcome", "0:51 WHY DOES THAT HAPPEN transition", "1:10 HUNGRY icon during appetite/hormone explanation", "1:18 suggested-video cards cover the last seconds"],
        "opening": "Introduces GLP-1 use for obesity and asks whether the effect lasts after stopping.",
        "visuals": "Stable desk talking head with yellow kinetic phrases, small medication/appetite icons and burned captions.",
        "editing": "Near-single-shot explanation with overlay substitutions and a suggested-video close; retained transcript includes literal timecodes.",
        "closing": "Attributes regain to hunger hormones and hypothalamic/satiety changes before suggested-video cards appear.",
        "possible_explanation": "Public playback confirms the title/content match, but Studio disclosed no curve and only four views; no production-retention relationship can be tested.",
        "alternative_explanation": "The topic overlaps the 15-second phSq6PkPtIg Short, but runtimes, packages and delivery differ and neither has a curve.",
    },
    "tDZKHR8UjYg": {
        "duration_seconds": 145,
        "comparison": "Batch 8 no-curve Lp(a) explainer",
        "timestamps": ["0:03 doctor in clinic chair under DR. REHAN OMAR credential card", "0:16 same shot introduces the conventional lipid panel", "0:30 crossed-out lipid-panel graphic while explaining what routine tests include", "1:01 clinician identifies Lp(a) as the missing inherited risk", "1:31 heart-warning icon during cardiovascular-risk explanation", "2:00 one-time lifetime testing recommendation", "2:20 suggested-video and subscribe overlays cover the close"],
        "opening": "Starts with a credential introduction and recap of conventional lipid panels before revealing Lp(a) as the omitted marker.",
        "visuals": "Pillarboxed clinic talking head with credential text, lipid-panel graphic, heart warning icon and burned captions.",
        "editing": "Stable single-camera explanation with a few topic overlays; end cards partially obscure the closing advice.",
        "closing": "Recommends at least one lifetime Lp(a) test and ends with a thank-you under suggested-video cards.",
        "possible_explanation": "The title and thumbnail promise the missing risk, but the spoken reveal follows credential and lipid-panel recap. Studio exported no curve, so any cost of that delay cannot be measured.",
        "alternative_explanation": "Twenty-eight basic-export views and a later 24-view live table row are tiny and may reflect different refresh states; topic demand and source mix are unknown.",
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
    "No evidence acquisition remains within authorized scope. Next: run the 30/60/90-day experiments in the forensic report and re-export Studio after 30 days; a heard (audio) continuous review is needed only if a complete audiovisual audit is required."
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
    "tf7f4RhQwtc": "Wide split composition: measured belly and bold NOT JUST WEIGHT beside the doctor; high contrast and title-aligned, though the consequence (heart risk) is left to the title.",
    "xI-KdZ96xcI": "Wide doctor-plus-stairs scene with an older man and STAIRS FEEL HARDER?; the functional symptom is concrete and readable, but heart failure is not disclosed in-image.",
    "Nf9pCrPYWyQ": "Wide alarmed-man/scale/Earth collage with BY 2035? 4 BILLION PEOPLE; strong statistic and event label, but the shocked stock face competes with the data.",
    "qC8BKb8Fh5Q": "Wide blood-pressure monitor, banana and doctor under BANANA + BP?; one-glance food/problem pairing accurately matches the video.",
    "jxoMnTrVziA": "Vertical outdoor older man balancing with tiny GOOD BALANCE / STRONG LEGS text and green checks; demonstration is clear, but text is small and large muted side bars consume space.",
    "jLEp6jDsN3Q": "Vertical older man clutching his chest beside the doctor with PAIN + SWEAT?; symptom urgency is immediate, though the narrow crop leaves large brown side bars.",
    "Uq3T8YZgyTw": "Vertical infographic listing jumping jacks, side leg raises and squats under OVER 50? CAN YOU DO ALL 3?; unusually specific but too text-dense for small mobile display.",
    "zESWa7FJgHY": "Wide outdoor upward-facing-dog pose with doctor and oversized START HERE; strong action cue and clean hierarchy, but back-pain context depends on the title.",
    "phSq6PkPtIg": "Wide medical illustration links an injection, hypothalamus and glowing stomach beside the doctor under THE REAL REASON; mechanism-heavy and title-aligned, though the drug name is absent in-image.",
    "sC_0XjL2z_Y": "Wide doctor holds eGFR 95 beside a urine cup marked uACR HIGH under LOOKS NORMAL?; unusually concrete two-test contrast and accurate to the current public title.",
    "VlSibJdSZF8": "Wide appetite-body illustration, injection pen, food icons and HUNGER RETURNS beside the doctor; one-glance post-Ozempic regain mechanism with strong dark/red contrast.",
    "tDZKHR8UjYg": "Wide doctor points to a lipid panel with a blank highlighted row under MISSING RISK?; clear visualizes an omitted marker without prematurely naming Lp(a).",
    "NznebmgFwXI": "Wide warm-room scene pairs socked feet near a heater with the doctor and ROOM WARM. FEET COLD?; concrete symptom contrast and clean two-part hierarchy.",
    "fAwh2svMARM": "Wide coffee mug, BP-up monitor and doctor under BP SPIKE?; the trigger/outcome relationship is immediate and title-aligned.",
    "YVjbjcVo1is": "Vertical older man clutching his chest beside the doctor under CHEST HEAVY?; urgent symptom cue, but wide muted side bars waste most of the 16:9 canvas.",
    "iltS1TPt4jo": "Vertical older man holding his chest beside the doctor under JUST STRESS?; clear anxiety-versus-heart contradiction, with the same large side-bar limitation as its re-edit sibling.",
    "UeGxF8-hb2s": "Vertical collage combines an older chair-stand demonstration, doctor cutout, 12 GOOD SCORE? and 30-SEC TEST; specific but crowded, and the image cannot warn about the video's black tail.",
    "tD4KOpsJH_c": "Vertical composite stacks a long OVER 60? DON'T DRINK COFFEE BEFORE CHECKING YOUR BLOOD PRESSURE headline, doctor, mug and 156/96 monitor; accurate but far too text-dense at small size.",
    "p_iI0enaFX8": "Vertical pale clinical scene shows a faceless older figure with cane, glowing heart and red 60; it signals age/heart risk but does not visualize the promised calf pain.",
    "qbwCkH_GqhU": "Vertical doctor holds an LDL card and multiple lab sheets under NOT JUST LDL; strong test-number framing, though several small papers compete with the headline.",
    "nRdBvyh7Sy0": "Vertical doctor compares two cup sizes under 2 CUPS? SAME? / NOT ALWAYS; concrete portion-size question, but the narrow crop and stacked text feel cramped.",
    "KPYHy7MDmLM": "Wide montage of three older men walking under STOP SLOW WALKING; readable and movement-specific, but the warning phrase overstates what the image alone can establish medically.",
    "nPqrcrxdrdE": "Vertical desk frame with tiny green doc text and a warning triangle; it does not communicate the promised three walking signs and relies almost entirely on the title.",
    "hUSVbcHVeVw": "Vertical close-up of berries with small 2. BERRIES / INTOXIDANTS text; the food is recognizable, but the word appears misspelled and there is no clinician cue.",
    "FDLU7tX7qNM": "Vertical doctor-at-desk frame dominated by WATCH FULL LONG VIDEO NOW CLICK HERE and a tiny health-warning subtitle; functions as a CTA frame rather than a symptom-led thumbnail.",
    "7MXBh2hjfto": "Dark vertical doctor frame with an injection icon crossed out and a warning triangle but no main hook text; implies medication danger, not the title's Ozempic-versus-appetite-suppressant comparison.",
    "fArHBQo6Ggw": "Vertical doctor, coffee mug, BP-up monitor and heart icons under STOP COFFEE?; direct trigger/question package with strong yellow/white contrast.",
    "j9VqMB6yTXQ": "Vertical reclining-chair frame with small Seniors and Patients who are seniors captions; looks like an arbitrary video frame and neither names potassium nor shows food.",
    "nP9fDHP1jbo": "Vertical stock man with a giant brain and molecule overlay plus only the word IT; no Ozempic, stopping or returning-hunger cue is legible without the title.",
    "TPVOIfcJl-k": "Vertical doctor beside an artery cross-section and a CHOLESTEROL HIGH card under TOO MUCH?; direct topic cue and high contrast, albeit generic to cholesterol quantity.",
    "sUL6SU8LnEg": "Wide cell-like graphic, Ozempic pen and doctor under MYTH?; clearly medication-related but does not disclose the title's cancer-or-blindness question.",
    "8JdBlF-ragM": "Wide Ozempic pens and doctor beside REAL SIDE EFFECT? and an Ozempic vagina? search-style label; specific and provocative, though the sensitive phrase dominates the clinical context.",
    "VrbLuTNi0qE": "Wide before/after balance poses, chair and 10 SEC timer under STEADY OR WOBBLY?; accurately previews the participatory one-leg test.",
    "CZ3gAUzdTAg": "Wide doctor beside salmon, berries, greens, nuts and olive oil under EAT THESE 5; concrete list preview with strong food-first hierarchy.",
    "1bb5M4E1oQs": "Vertical doctor holds a 7 DAY NO SUGAR, NO CARB DIET PLAN chart; materially mismatched with the title's potassium-food hack and blood-pressure promise.",
    "t1j-p9pkw3Y": "Wide older-adult chair-stand action, 00:30 timer and doctor under 30 SEC / HOW MANY?; accurately previews the self-test with a clear measurable challenge.",
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


def duration_seconds(value: str | None) -> int | None:
    if not value:
        return None
    try:
        parts = [int(part) for part in value.split(":")]
    except ValueError:
        return None
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] if len(parts) == 1 else None


def load_extended_studio_metrics() -> tuple[dict[str, tuple], list[dict[str, str]]]:
    if not EXTENDED_STUDIO_ARCHIVE.exists():
        return LIVE_STUDIO_METRICS_FALLBACK, []
    canonical_ids = {record["id"] for record in json.loads(DATASET.read_text())}
    rows = csv_rows_from_zip(EXTENDED_STUDIO_ARCHIVE, "Table data.csv")
    metrics: dict[str, tuple] = {}
    extras: list[dict[str, str]] = []
    for row in rows[1:]:
        video_id = row.get("Content", "").strip()
        if video_id not in canonical_ids:
            extras.append({"video_id": video_id, "title": row.get("Video title", ""), "views": row.get("Views", "")})
            continue
        stayed_raw = row.get("Stayed to watch (%)", "")
        metrics[video_id] = (
            int(fnum(row.get("Engaged views"))),
            duration_seconds(row.get("Average view duration")),
            fnum(row.get("Average percentage viewed (%)")),
            fnum(stayed_raw) if stayed_raw != "" else None,
            int(fnum(row.get("Subscribers gained"))),
        )
    return metrics, extras


LIVE_STUDIO_METRICS, EXTENDED_STUDIO_EXTRA_ROWS = load_extended_studio_metrics()
STUDIO_DIR_0928 = EXTENDED_STUDIO_ARCHIVE.parent


def reconcile_browser_rows() -> dict:
    """Compare 2026-09-28 browser-observed rows with the exported CSV; both are kept as separate evidence."""
    mismatches = []
    for vid, seen in LIVE_STUDIO_METRICS_FALLBACK.items():
        exported = LIVE_STUDIO_METRICS.get(vid)
        if exported is None:
            mismatches.append({"video_id": vid, "reason": "absent from export"})
            continue
        for label, a, b, tol in zip(["engaged_views", "avd_seconds", "apv_percent", "stayed_percent", "subscribers_gained"], seen, exported, [0, 0, 0.0501, 0.0501, 0]):
            if a is None:  # browser cell blank; export may hold 0 or blank
                continue
            if b is None or abs(a - b) > tol:
                mismatches.append({"video_id": vid, "field": label, "browser": a, "export": b})
    return {
        "browser_observed_rows": len(LIVE_STUDIO_METRICS_FALLBACK),
        "exported_canonical_rows": len(LIVE_STUDIO_METRICS),
        "previously_missing_now_exported": sorted(set(LIVE_STUDIO_METRICS) - set(LIVE_STUDIO_METRICS_FALLBACK)),
        "mismatches_beyond_display_rounding": mismatches,
        "rule": "Browser values are rounded to one decimal; differences within 0.05 are display rounding. Blank browser subscriber cells are not treated as zero.",
    }


def load_supplementary_studio() -> dict | None:
    """Channel-level Studio drill-downs exported 2026-09-28 (private; aggregates only, no raw rows copied)."""
    prov_path = STUDIO_DIR_0928 / "studio-export-provenance.json"
    if not prov_path.exists():
        return None
    prov = json.loads(prov_path.read_text())
    canonical_ids = {record["id"] for record in json.loads(DATASET.read_text())}

    def table(name: str, member: str = "Table data.csv") -> list[dict[str, str]]:
        return csv_rows_from_zip(STUDIO_DIR_0928 / name, member)

    search = table("studio-advanced-search-queries-lifetime.zip")
    suggested = table("studio-advanced-suggested-videos-lifetime.zip")
    own = [r for r in suggested[1:] if r["Traffic source"].split(".", 1)[-1] in canonical_ids]
    external = [r for r in suggested[1:] if r not in own]
    geo = table("studio-advanced-geography-lifetime.zip")
    device = table("studio-advanced-device-type-lifetime.zip")
    age_gender = table("studio-advanced-audience-age-gender-lifetime.zip")
    ncr = table("studio-audience-size-growth-last-28-days.zip", "New, casual and regular viewers.csv")
    monthly = table("studio-audience-size-growth-last-28-days.zip", "All.csv")
    subs = table("studio-audience-size-growth-last-28-days.zip", "Subscribers.csv")
    total_views = fnum(geo[0]["Views"])
    ages: dict[str, float] = {}
    for r in age_gender:
        ages[r["Viewer age"]] = round(ages.get(r["Viewer age"], 0) + fnum(r["Views (%)"]), 2)
    last = ncr[-1]
    return {
        "provenance_file": str(prov_path.relative_to(ROOT)),
        "files": {k: {"sha256": v["sha256"], "bytes": v["bytes"], "reporting_period": v["reporting_period"], "report": v["report"]} for k, v in prov["files"].items()},
        "search_terms": {
            "total_search_views": int(fnum(search[0]["Views"])), "total_search_impressions": int(fnum(search[0]["Thumbnail impressions"])), "search_ctr_percent": fnum(search[0]["Thumbnail click-through rate (%)"]),
            "disclosed_terms": len(search) - 1, "views_in_disclosed_terms": int(sum(fnum(r["Views"]) for r in search[1:])),
            "max_views_single_term": int(max(fnum(r["Views"]) for r in search[1:])),
            "top_terms": [{"term": r["Source title"], "views": int(fnum(r["Views"]))} for r in search[1:11]],
        },
        "suggested_sources": {
            "total_suggested_views": int(fnum(suggested[0]["Views"])), "total_suggested_impressions": int(fnum(suggested[0]["Thumbnail impressions"])), "suggested_ctr_percent": fnum(suggested[0]["Thumbnail click-through rate (%)"]),
            "disclosed_source_videos": len(suggested) - 1,
            "own_channel_sources": len(own), "own_channel_views": int(sum(fnum(r["Views"]) for r in own)),
            "external_sources": len(external), "external_views": int(sum(fnum(r["Views"]) for r in external)),
            "top_external_sources": [{"title": r["Source title"], "views": int(fnum(r["Views"]))} for r in sorted(external, key=lambda r: -fnum(r["Views"]))[:8]],
        },
        "geography": {"total_views": int(total_views), "disclosed": [{"country": r["Geography"], "views": int(fnum(r["Views"])), "share_percent": round(100 * fnum(r["Views"]) / total_views, 1)} for r in geo[1:]],
                      "undisclosed_views": int(total_views - sum(fnum(r["Views"]) for r in geo[1:]))},
        "device": [{"device": r["Device type"], "views": int(fnum(r["Views"])), "watch_hours": fnum(r["Watch time (hours)"]), "average_view_duration": r["Average view duration"]} for r in device[1:]],
        "age_views_percent": ages,
        "audience_28_day": {
            "period": f"{ncr[0]['Date']}..{last['Date']}", "monthly_audience_latest": int(fnum(monthly[-1]["Monthly audience"])),
            "new_viewers_latest": int(fnum(last["28-day new viewers"])), "casual_viewers_latest": int(fnum(last["28-day casual viewers"])), "regular_viewers_latest": int(fnum(last["28-day regular viewers"])),
            "regular_viewers_max_in_period": int(max(fnum(r["28-day regular viewers"]) for r in ncr)),
            "subscribers_start": int(fnum(subs[0]["Subscribers"])), "subscribers_latest": int(fnum(subs[-1]["Subscribers"])),
        },
        "limits": [
            "Channel-level drill-downs: they cannot be attributed to individual videos.",
            "Studio discloses only the top rows; undisclosed remainders are recorded, not imputed.",
            "Search-term rows usually show 0 impressions because Studio counts search impressions at source level; per-term CTR is not interpretable.",
            "New/casual/regular counts cover only the last 28 days and are Studio estimates.",
        ],
    }


SUPPLEMENTARY_STUDIO = load_supplementary_studio()


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
        "reporting_period": "2026-02-03 through 2026-09-27 (Studio lifetime view at export)",
        "source": "Authenticated YouTube Studio Advanced Mode CSV export",
        "source_file": str(EXTENDED_STUDIO_ARCHIVE.relative_to(ROOT)) if EXTENDED_STUDIO_ARCHIVE.exists() else None,
        "source_sha256": sha256(EXTENDED_STUDIO_ARCHIVE) if EXTENDED_STUDIO_ARCHIVE.exists() else None,
        "engaged_views": engaged,
        "average_view_duration_seconds_actual": avd,
        "average_percentage_viewed_actual": apv,
        "stayed_to_watch_percent": stayed,
        "swiped_away_percent": round(100 - stayed, 1) if stayed is not None else None,
        "subscribers_gained": gained,
        "browser_observed_2026_09_28": dict(zip(["engaged_views", "average_view_duration_seconds", "average_percentage_viewed", "stayed_to_watch_percent", "subscribers_gained"], LIVE_STUDIO_METRICS_FALLBACK[video_id])) if video_id in LIVE_STUDIO_METRICS_FALLBACK else None,
        "limitation": "Extended row is file-backed. Stayed-to-watch is blank for regular videos and retained as unavailable, not zero. The export also contains one noncanonical Post row, preserved separately and excluded from the 56-video register.",
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
            observation["analysis_basis"] = "revalidation_observation is the image-specific inspection; the remaining descriptor fields are templated from visible text and title and are not independent observations."
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
            "evidence_dimensions": {
                "canonical_video_identity": "VERIFIED",
                "verified_metadata": "VERIFIED",
                "original_transcript": "VERIFIED",
                "actual_thumbnail": "VERIFIED",
                "thumbnail_inspection": "IMAGE_SPECIFIC" if vid in THUMBNAIL_REVALIDATIONS else "TEMPLATED_ONLY",
                "studio_metrics": "BASIC_AND_EXTENDED_EXPORT" if vid in studio_by_id and vid in LIVE_STUDIO_METRICS else ("BASIC_EXPORT_ONLY" if vid in studio_by_id else "NONE"),
                "retention_curve": "AVAILABLE" if retention_record and retention_record.get("curve_status") == "AVAILABLE" else "NOT_DISCLOSED_BY_STUDIO",
                "retention_linked_investigation": "CONTENT_LINKED" if status == "RETENTION_ANALYZED" else "NOT_POSSIBLE_NO_CURVE",
                "seek_sampled_playback": "YES" if vid in SEEK_SAMPLED else ("REPORTED_FULL_TEXT_RECORD_ONLY" if audit else "NO"),
                "audio_cut_signal_measurement": "YES" if vid in SIGNAL_PASS else "NO",
                "actual_spoken_audio_review": "NOT_VERIFIED",
                "verified_full_playback": "NOT_VERIFIED",
                "complete_audiovisual_audit": "NOT_VERIFIED",
                "external_research": "TOPIC_LEVEL_GOOGLE_TRENDS",
                "medical_claim_review": "NOT_PERFORMED",
            },
            "investigation_status": status,
            "google_trends_research": "TOPIC_LEVEL_VERIFIED_COMPLETE",
            "external_competitor_comparison": "REUSED_EXISTING_EVIDENCE",
            "relevant_private_studio_analytics": "LIFETIME_BASIC_ROW_VERIFIED" if vid in studio_by_id else "NO_ROW_IN_EXPORT",
            "studio_metrics": studio_by_id.get(vid),
            "studio_metrics_actual_observation": live_studio_observation(vid),
            "per_video_traffic_source_detail": "NOT_EXPORTED_CHANNEL_LEVEL_SEARCH_AND_SUGGESTED_DRILLDOWNS_ONLY",
            "retention_evidence": retention_record,
            "retention_curve": retention_record.get("curve_status", "NOT_EXPORTED") if retention_record else "NOT_EXPORTED",
            "retention_audience_segments": audience_segments(vid, retention_record),
            "retention_investigation": retention_investigation(vid, retention_record),
            "remaining_gap": "; ".join(remaining) if remaining else "None within recovered evidence",
            "user_action_required": "No; only per-video traffic-source drill-downs and a heard (audio) playback review remain unavailable",
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
        "completeness_matrix": {dim: dict(sorted(Counter(r["evidence_dimensions"][dim] for r in records).items())) for dim in records[0]["evidence_dimensions"]},
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
            {"batch": "Batch 7 final curve-linked and no-curve public-video review", "status": "COMPLETE_WITH_AUDIO_AND_PRIVATE_DATA_LIMITATIONS", "saved_at": "2026-09-28", "result": "tf7f4RhQwtc, xI-KdZ96xcI, Nf9pCrPYWyQ and qC8BKb8Fh5Q were seek-sampled at retained curve events; jxoMnTrVziA, jLEp6jDsN3Q, Uq3T8YZgyTw and zESWa7FJgHY were seek-sampled but remain LIMITED_BY_UNAVAILABLE_EVIDENCE because Studio disclosed no curve. Uq3T8YZgyTw ends on a white engagement card through 49.8 s, not a black tail. Audio was not heard. All eight thumbnails were revalidated."},
            {"batch": "Batch 8 final no-curve public-video review", "status": "COMPLETE_WITH_PRIVATE_RETENTION_UNAVAILABLE", "saved_at": "2026-09-28", "result": "phSq6PkPtIg, sC_0XjL2z_Y, VlSibJdSZF8 and tDZKHR8UjYg were seek-sampled from opening through close. Public content and production characteristics are documented, but all four remain LIMITED_BY_UNAVAILABLE_EVIDENCE because their Studio exports contain no retention curve. phSq6PkPtIg's retained caption text includes impossible 0:21/0:27 timecodes for a 14.86-second video. Audio was not heard. All four thumbnails were revalidated."},
            {"batch": "Batch 9 Studio export recovery and reconciliation", "status": "COMPLETE", "saved_at": "2026-09-28", "result": "Seven Studio CSV exports downloaded 2026-09-28 04:01-04:14 were archived byte-identical (SHA-256 match) under the private 2026-09-28 folder with a provenance manifest: extended lifetime content table, Search-term and Suggested-source drill-downs, geography, device, age/gender and 28-day new/casual/regular audience. Extended table covers all 56 canonical IDs with no duplicates plus one noncanonical Post row; the nine previously missing rows are present; all 47 browser-observed rows agree within display rounding; views equal the 2026-09-27 lifetime export."},
            {"batch": "Batch 3 Research Diagnosis and Deliverables", "status": "COMPLETE_FOR_AVAILABLE_SYNTHESIS", "saved_at": "2026-09-28", "result": "Three Trends comparisons verified; six matched comparisons synthesized; diagnosis and four existing deliverables reconciled."},
        ],
        "execution_matrix": [
            {"task": "Metadata", "previous_result": "56 records", "current_evidence": "56 exact canonical Video IDs; current public catalog still 56 on 2026-09-28", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Transcripts", "previous_result": "56", "current_evidence": "56 original transcript files present", "status": "VERIFIED_COMPLETE", "required_action": "Reuse; do not reread wholesale"},
            {"task": "Thumbnails", "previous_result": "56 identity-verified images with 44 templated analyses", "current_evidence": f"56 images identity-verified and {register['counts']['thumbnail_priority_revalidations']} image-specific observations revalidated", "status": "VERIFIED_COMPLETE", "required_action": "None within the retained thumbnail set"},
            {"task": "Studio reports", "previous_result": "Four reported", "current_evidence": "Lifetime, 90d, 28d and traffic-source ZIP hashes verified", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Individual Analytics", "previous_result": "56 basic rows plus 47 browser-observed extended rows", "current_evidence": f"56 canonical basic rows and {register['counts']['studio_extended_rows_observed']} canonical extended rows in the authenticated CSV export; one noncanonical Post row preserved but excluded", "status": "VERIFIED_COMPLETE_FOR_CONTENT_TABLE", "required_action": "None for the per-video lifetime content table"},
            {"task": "Retention", "previous_result": "Previously missing", "current_evidence": f"56 exports; 46 curves; {register['counts']['retention_content_linked_investigations']} content-linked investigations; 10 no-curve disclosures; {register['counts']['retention_new_vs_returning_split']} exports carry a new-vs-returning split", "status": "COMPLETE_FOR_AVAILABLE_PRIVATE_EVIDENCE", "required_action": "No action possible for the 10 exports with no disclosed curve unless YouTube later exposes data"},
            {"task": "Playback", "previous_result": "Previously missing", "current_evidence": f"{register['counts']['playback_reported_full']} reported full-playback records (text-only completion evidence) and {register['counts']['playback_seek_sampled']} seek-sampled records; zero verified complete audiovisual audits", "status": "PUBLIC_CONTENT_SAMPLED_AUDIOVISUAL_DEPTH_PARTIAL", "required_action": "Audibly review continuous playback only if a complete audiovisual editing audit is required"},
            {"task": "Trends", "previous_result": "Three comparisons", "current_evidence": "Three original official CSVs and configurations verified", "status": "VERIFIED_COMPLETE", "required_action": "No repeat query justified by available source detail"},
            {"task": "Channel-level audience and source reports", "previous_result": "Unavailable", "current_evidence": "Search terms, Suggested sources, geography, device, age/gender and 28-day new/casual/regular exports archived and hash-verified", "status": "VERIFIED_COMPLETE_CHANNEL_LEVEL", "required_action": "Per-video source drill-downs remain unexported"},
            {"task": "Research synthesis", "previous_result": "Partial", "current_evidence": f"{len(MATCHED_COMPARISONS)} matched comparisons and multi-stage diagnosis including audience-development, Search and Suggested evidence", "status": "COMPLETE_FOR_AVAILABLE_EVIDENCE", "required_action": "Run the preregistered experiments; reassess after 30 days of new data"},
        ],
        "phase_status": {
            "repository_recovery": "VERIFIED_COMPLETE",
            "thumbnail_recovery_and_visual_inspection": "VERIFIED_COMPLETE_56_IMAGE_SPECIFIC_REVALIDATIONS",
            "public_catalog_refresh": "VERIFIED_COMPLETE",
            "video_playback_forensics": f"PUBLIC_SAMPLE_COMPLETE_{register['counts']['investigation_status']['RETENTION_ANALYZED']}_RETENTION_ANALYZED_{register['counts']['investigation_status']['LIMITED_BY_UNAVAILABLE_EVIDENCE']}_NO_CURVE_LIMITED_OF_56_AUDIO_NOT_VERIFIED",
            "retention_investigations": f"COMPLETE_FOR_AVAILABLE_EVIDENCE_{register['counts']['retention_content_linked_investigations']}_CONTENT_LINKED_10_NO_CURVE",
            "google_trends": "VERIFIED_COMPLETE",
            "youtube_studio_exports": "VERIFIED_COMPLETE_ORIGINAL_EXPORTS",
            "video_level_studio_metrics": f"VERIFIED_COMPLETE_56_BASIC_{register['counts']['studio_extended_rows_observed']}_EXTENDED",
            "growth_diagnosis": "UPDATED_EVIDENCE_BACKED",
            "four_artifacts": "UPDATED_IN_PLACE",
        },
        "verified_counts": register["counts"],
        "studio": studio,
        "studio_live_observation": {
            "observed_at": "2026-09-28",
            "access": "Authenticated read-only manager session for canonical channel",
            "channel_totals": {"views": 8366, "watch_hours": 45.6, "net_subscribers": 33, "subscribers_gained": 34, "impressions": 36169, "ctr_percent": 2.99, "engaged_views": 3999, "average_view_duration_seconds_actual": 39, "average_percentage_viewed_actual": 37.32, "stayed_to_watch_percent": 36.03},
            "extended_video_rows_observed": len(LIVE_STUDIO_METRICS),
            "extended_video_rows_not_captured": len(records) - len(LIVE_STUDIO_METRICS),
            "source_archive": str(EXTENDED_STUDIO_ARCHIVE.relative_to(ROOT)) if EXTENDED_STUDIO_ARCHIVE.exists() else None,
            "source_sha256": sha256(EXTENDED_STUDIO_ARCHIVE) if EXTENDED_STUDIO_ARCHIVE.exists() else None,
            "noncanonical_rows_preserved_not_counted": EXTENDED_STUDIO_EXTRA_ROWS,
            "missing_short_status": "RESOLVED",
            "missing_short_metrics": {"video_id": "-SjQc2MwaOU", "views": 233, "engaged_views": 54, "average_view_duration_seconds_actual": 23, "average_percentage_viewed_actual": 52.1, "stayed_to_watch_percent": 20.6, "swiped_away_percent": 79.4, "impressions": 338, "ctr_percent": 1.2, "subscribers_gained": 0},
            "unavailable_reports": ["Per-video search queries", "Per-video suggested-video sources", "Viewers across formats", "Per-video new/returning viewer counts (channel-level 28-day new/casual/regular counts are now exported)"],
            "browser_vs_export_reconciliation": reconcile_browser_rows(),
            "availability_note": "New/returning/unique viewer cells displayed em dash in the inspected content table; this is unavailability, not a measured zero.",
        },
        "studio_supplementary_2026_09_28": SUPPLEMENTARY_STUDIO,
        "trends": trends,
        "matched_comparisons": MATCHED_COMPARISONS,
        "knowledge_framework_applications": {
            "status": "REUSED_EXISTING_MAPPINGS",
            "count": 12,
            "source_table": "Forensic report section 9 mapping table",
            "guardrail": "DS-000018 creator claims remain mixed reliability; official YouTube documentation overrides conflicting blanket claims.",
        },
        "diagnosis": [
            {"finding": "Distribution opportunity is limited and uneven", "video_ids": ["CZ3gAUzdTAg", "EB3_A2b4a6o", "BCNWQ3uuSuE"], "metrics": "36,169 lifetime counted impressions across the exported content table; Suggested 19,841, Search 11,245 and Browse 4,028 impressions in the retained source export", "visual_and_transcript_evidence": "No single production pattern explains the source mix", "comparative_evidence": "Some videos still received thousands of impressions", "historical_context": "Lifetime through 2026-09-27", "counterexample": "Low impressions can coexist with high CTR on a narrow loyal audience", "alternative_explanations": "Topic demand, audience size, eligibility and competition", "confidence": "HIGH for limited recorded reach; LOW for one causal mechanism", "practical_experiment": "Run native package tests on mature eligible long-form videos with adequate impressions and preserve the medical promise."},
            {"finding": "Packaging response varies materially by video and source", "video_ids": ["BCNWQ3uuSuE", "SBrMW71O69U", "EB3_A2b4a6o"], "metrics": "Lifetime CTR 3.0%; BCNWQ3uuSuE 4.2%, SBrMW71O69U 2.87%, EB3_A2b4a6o 1.8%", "visual_and_transcript_evidence": "Specific lab-test utility is clearer in BCNWQ3uuSuE than the broad SBrMW71O69U warning", "comparative_evidence": "BCNWQ3uuSuE also retains 60.5% at 30 seconds versus 38.46% for SBrMW71O69U", "historical_context": "Video ages and impression bases differ", "counterexample": "High CTR rows on tiny impression bases are unstable", "alternative_explanations": "Traffic source and audience composition", "confidence": "HIGH for variation; MEDIUM for the specific-package hypothesis", "practical_experiment": "Test exact utility/problem packages against broad warning packages on one unchanged mature video."},
            {"finding": "Early and mid-video retention are inconsistent", "video_ids": ["5oPzZjfNgII", "EB3_A2b4a6o", "BCNWQ3uuSuE", "SBrMW71O69U"], "metrics": "30-second retention 56.15%, 60.0%, 60.5% and 38.46%; midpoint 43.85%, 23.57%, 31.93% and 15.38% respectively", "visual_and_transcript_evidence": "Concrete symptom/test progressions hold more of the audience in selected pairs; long steady explanation sections coincide with faster decline", "comparative_evidence": "Retention and CTR do not always move together", "historical_context": "Actual per-video curves from exports through 2026-09-27", "counterexample": "A dip alone does not identify why viewers left", "alternative_explanations": "Audience intent, source, video length and topic familiarity", "confidence": "HIGH for variation; MEDIUM for production hypotheses", "practical_experiment": "Open with the exact promised decision, demonstrate it early and review the first major dip against the published cut."},
            {"finding": "Shorts feed acceptance and depth are separate", "video_ids": ["QfRaG71ZA_0", "4ByUo2N_C-I", "PTB-6fgaAKk", "gunPgSlxJLA"], "metrics": "QfRaG71ZA_0 stayed 57.3%/APV 83.3%; 4ByUo2N_C-I 43.7%/43.8%; PTB-6fgaAKk 16.9%/126.6%; gunPgSlxJLA 28.7%/84.0%", "visual_and_transcript_evidence": "Concrete symptom frames are easier to parse; very short loops can inflate APV", "comparative_evidence": "kF26QB7xHiE had more views than FVfG_HZV4qg despite much lower stayed-to-watch", "historical_context": "Authenticated lifetime row observations on 2026-09-28", "counterexample": "High APV does not guarantee high stayed-to-watch or distribution", "alternative_explanations": "Feed cohort, loop length and repeat exposure", "confidence": "HIGH", "practical_experiment": "Test first-frame specificity and measure stayed-to-watch separately from APV."},
            {"finding": "The channel is not yet building a returning audience", "video_ids": [], "metrics": "28-day window ending 2026-09-26: monthly audience 505 = 495 new + 10 casual + 0 regular viewers; regular viewers stayed 0 on every day from 2026-08-30; subscribers 29 to 33. Lifetime: Shorts feed 5,355 of 8,366 views; own-channel videos supplied only 70 of 1,031 Suggested views (13 of 472 disclosed source videos).", "visual_and_transcript_evidence": "Catalog alternates cardiology, metabolic/GLP-1, diabetes, mobility and exercise topics without a recurring series frame; end screens mostly point to one next video", "comparative_evidence": "Retention exports show returning viewers holding better where split (FDLU7tX7qNM 46.15% vs 17.78% new at 30 s), but the returning cohort is too small to matter at channel scale", "historical_context": "Only the latest 28 days are covered by the new/casual/regular export", "counterexample": "A young channel with 33 subscribers is expected to be new-viewer dominated; 0 regular viewers is a stage fact as well as a constraint", "alternative_explanations": "Small catalog, irregular cadence, Shorts-feed discovery that YouTube does not convert into long-form sessions, and topic breadth; the export cannot separate these", "confidence": "HIGH that returning-viewer development is a binding constraint; LOW on which cause dominates", "practical_experiment": "Publish one named recurring series (e.g. a weekly 'After 60 heart check') for 8 weeks with end screens and pinned playlists linking series episodes; success = regular viewers above 0 and own-channel Suggested share above 7% (current 70/1,031 = 6.8%)."},
            {"finding": "Discovery comes from other creators' health videos and a long tail of searches, largely South Asian", "video_ids": ["CZ3gAUzdTAg", "EB3_A2b4a6o", "NznebmgFwXI"], "metrics": "Suggested: 1,031 views from 19,844 impressions (CTR 2.9%); 459 external source videos supplied 910 disclosed views, top sources are other doctors' Hindi/Bengali/English general-health videos (thyroid, acid reflux, neuropathy, colonoscopy). Search: 1,175 views from 11,248 impressions (CTR 2.71%); 114 disclosed terms carry only 170 views, maximum 7 views per term. Disclosed geography: IN 16.0%, PK 4.9%, US 3.9%, GB 3.6%; 5,620 views (67%) fall below Studio's disclosure threshold. Device: mobile 6,990 views (AVD 0:34), TV 399 views (AVD 1:17).", "visual_and_transcript_evidence": "Titles use 'After 60' and US-style clinical framing; captions and thumbnails are English", "comparative_evidence": "Search CTR (2.71%) and Suggested CTR (2.9%) are similar; no source outperforms by a margin that survives the small base", "historical_context": "Lifetime through 2026-09-27; channel-level only", "counterexample": "US and GB together still supply 7.5% of views; senior targeting may work there but the base is too small to test", "alternative_explanations": "YouTube may be matching the doctor persona to South Asian general-health viewers regardless of the intended senior/US audience", "confidence": "HIGH for the source mix; MEDIUM for the audience-mismatch hypothesis", "practical_experiment": "Test two topic clusters for 6 weeks each (cardiology decision questions versus general-health adjacent to the top Suggested sources) and compare impressions, CTR and 30-second retention per upload."},
            {"finding": "Format and topic confound most apparent patterns", "video_ids": ["CZ3gAUzdTAg", "HzFdyjyEFTY", "qbwCkH_GqhU", "8JdBlF-ragM"], "metrics": "Extended export medians (impressions >= 100): long-form cardiology CTR 2.83% (14 videos, 1,232 views), long-form broader 3.09% (13, 746), Shorts cardiology 1.48% (18, 2,848), Shorts broader 2.08% (10, 3,305). Lowest CTR among videos with >= 500 impressions: HzFdyjyEFTY 1.35%, qbwCkH_GqhU 1.65%, EB3_A2b4a6o 1.81%; highest: 8JdBlF-ragM 4.89%, 5oPzZjfNgII 4.72%, r9ZyUWyY4Lc 4.64%.", "visual_and_transcript_evidence": "Low-CTR titles open with a population/decision frame ('Daily Aspirin After 60', 'LDL Isn't the Whole Story'); high-CTR titles name a concrete question or body signal", "comparative_evidence": "Cardiology versus broader topic differences are within 0.6 CTR points and reverse between formats", "historical_context": "Lifetime; video ages differ by up to 7 months", "counterexample": "CZ3gAUzdTAg drew the most impressions (5,738) with a mid-range 3.69% CTR", "alternative_explanations": "Impression source mix per video is unexported; Shorts CTR reflects non-feed surfaces only", "confidence": "HIGH that topic label alone does not separate performance; LOW for any single packaging rule", "practical_experiment": "Rewrite the three lowest-CTR mature long-form packages to a concrete question/body-signal form using Test & Compare where eligible; keep the video unchanged."},
            {"finding": "Public demand alone does not explain outcomes", "video_ids": ["sUL6SU8LnEg", "VlSibJdSZF8", "8JdBlF-ragM"], "metrics": "Ozempic mean normalized Trends score 31.45 versus semaglutide 7.71 and GLP-1 2.99 within one US YouTube Search comparison", "visual_and_transcript_evidence": "Existing packages vary between myth, side-effect and rebound-weight angles", "comparative_evidence": "High normalized interest did not yield strong channel results", "historical_context": "Five-year normalized Trends series", "counterexample": "Trends is not absolute volume and does not describe this channel's eligible audience", "alternative_explanations": "Packaging, authority fit, competition, timing and distribution", "confidence": "MEDIUM", "practical_experiment": "Use exact query/source evidence before commissioning another demand study."},
            {"finding": "Caption-track defects are widespread but not associated with a consistent retention pattern", "video_ids": sorted(CAPTION_TIMECODE_IDS | CAPTION_EMOJI_IDS), "metrics": "Raw (m:ss) timecodes appear in 10 of 56 retained caption transcripts (5 Shorts, 5 long-form); emoji and a heading line appear in 2 more (hUSVbcHVeVw, FDLU7tX7qNM). phSq6PkPtIg's retained text includes 0:21 and 0:27 markers although public runtime is 14.86 s. Median compared-to-other-videos value at 30 s: timecode Shorts -27.49 vs other Shorts 7.93; timecode long-form 7.6 vs other long-form -30.81.", "visual_and_transcript_evidence": "Timecodes were seen on screen in iltS1TPt4jo, TPVOIfcJl-k, sUL6SU8LnEg and p_iI0enaFX8 during earlier playback. phSq6PkPtIg's impossible markers are present in retained transcript evidence; player captions were not enabled during its sampled playback.", "comparative_evidence": "Direction flips between formats; Nf9pCrPYWyQ retains 80.77% at 3 s and 42.31% at 30 s despite literal transcript timecodes, while other affected videos perform weakly", "historical_context": "Defect spans February to September 2026 uploads", "counterexample": "FVfG_HZV4qg has the defect and the second-highest Short view count (1,068) with 51.1% stayed-to-watch", "alternative_explanations": "Many viewers may not enable captions; group sizes are 3-19 and title/topic/source differ", "confidence": "HIGH that the retained-text defect exists; LOW for any retention effect", "practical_experiment": "Replace the caption tracks on affected videos (a quality fix that needs no test) and do not attribute retention changes to it."},
            {"finding": "Footage reuse is concentrated in the coffee cluster and one heart-attack re-edit", "video_ids": ["fAwh2svMARM", "QfRaG71ZA_0", "4ByUo2N_C-I", "fArHBQo6Ggw", "nRdBvyh7Sy0", "YVjbjcVo1is", "iltS1TPt4jo"], "metrics": "10-word transcript overlap: YVjbjcVo1is/iltS1TPt4jo 0.75; long-form fAwh2svMARM shares 0.33-0.49 with four coffee Shorts; no other pair exceeds 0.15", "visual_and_transcript_evidence": "Coffee Shorts are excerpts of the long-form coffee video; iltS1TPt4jo adds an illustrated cold open to YVjbjcVo1is footage", "comparative_evidence": "Four coffee Shorts drew 25-341 views each versus 48 for their long-form parent; stayed-to-watch 40.9-57.3%", "historical_context": "Parent published 2026-08-25; Shorts 2026-09-09 to 2026-09-18", "counterexample": "The same source footage produced both the strongest (QfRaG71ZA_0) and a weaker (4ByUo2N_C-I) coffee Short, so the excerpt and package matter more than the footage", "alternative_explanations": "Different excerpts, titles and publication dates", "confidence": "HIGH for reuse; MEDIUM for excerpt choice mattering", "practical_experiment": "When clipping a long-form video, test excerpts that open on a named symptom or viewer qualifier against excerpts that open on a definition."},
            {"finding": "Fast cutting is not a reliable retention lever in this catalog", "video_ids": ["NznebmgFwXI", "KPYHy7MDmLM", "CZ3gAUzdTAg", "8JdBlF-ragM"], "metrics": "Hard cuts per minute: NznebmgFwXI 0.8 (3 s retention 87.1%), KPYHy7MDmLM 16.9 (57.89%), CZ3gAUzdTAg 18.3 (88.72% but 43.92% at 30 s), 8JdBlF-ragM 18.8 (78.69%, 55.74% at 30 s)", "visual_and_transcript_evidence": "The near-single-take video opens on a concrete self-check symptom; the fast-cut weaker video opens on a generic warning with three text layers", "comparative_evidence": "DS-000018 creator advice favours frequent pattern interrupts; this pair contradicts it at the opening", "historical_context": "Continuous 2x signal pass on 8 videos, 2026-09-28", "counterexample": "8JdBlF-ragM is fast-cut and holds well", "alternative_explanations": "Topic, title promise and tiny samples (20-132 views)", "confidence": "MEDIUM that pace alone does not explain opening loss; LOW for any causal claim", "practical_experiment": "Hold pace constant and vary only the first sentence (specific symptom question versus generic warning)."},
            {"finding": "Export and packaging defects remove or misdirect viewers independently of content quality", "video_ids": ["UeGxF8-hb2s", "7MXBh2hjfto", "RD7ugxaBHSQ", "1bb5M4E1oQs", "hUSVbcHVeVw", "Uq3T8YZgyTw"], "metrics": "UeGxF8-hb2s is black and near-silent for its final 39 s (44% of runtime): 69.23% retained at 30 s, 7.69% at end, APV 51.3%. 7MXBh2hjfto's title promises an appetite-suppressant comparison but its content debunks a cancer myth; end retention 6.25%. RD7ugxaBHSQ shifts from calf circulation to modified push-ups. 1bb5M4E1oQs uses a 7-day no-sugar/no-carb thumbnail for a potassium/blood-pressure video.", "visual_and_transcript_evidence": "Frame luminance is 0 from 50 s to 80 s in UeGxF8-hb2s; sampled 7MXBh2hjfto anchors show only cancer-myth content; sampled RD7ugxaBHSQ anchors show modified push-ups; retained 1bb5M4E1oQs thumbnail was re-inspected at full size.", "comparative_evidence": "Uq3T8YZgyTw was the closest word-density candidate for another tail defect, but sampled frames at 47.1 and 49.8 s show a white engagement card through its 50.82 s end, not black.", "historical_context": "Affected uploads span February to September 2026", "counterexample": "Not every low-word-density or static-ending video has a black tail; Uq3T8YZgyTw explicitly refutes that generalization. RD7ugxaBHSQ's largest early loss precedes its title-scope shift, so the mismatch cannot explain the opening drop.", "alternative_explanations": "Tiny samples, later title changes and unknown traffic sources limit performance attribution", "confidence": "HIGH that the listed defects/mismatches exist; MEDIUM that the black tail depresses APV; LOW for distribution effects", "practical_experiment": "Re-export or trim UeGxF8-hb2s; align title, thumbnail and delivered content for 7MXBh2hjfto, RD7ugxaBHSQ and 1bb5M4E1oQs; verify every final render before upload."},
        ],
        "retention_export_summary": {key: retention[key] for key in ("record_count", "available_count", "curve_available_count", "exported_no_curve_count")},
        "remaining_private_requirements": ["Returning-viewer and viewers-across-formats channel reports", "Search query and suggested-video detail", "Geography and device reports"],
        "preservation": {"raw_private_exports_modified": False, "credentials_saved": False, "remote_push_performed": False, "note": "Only derived docs/research artifacts and supporting scripts were updated."},
    }
    (OUT_DIR / "Decode_Your_Heart_Video_Evidence_Register.json").write_text(json.dumps(register, indent=2) + "\n")
    (OUT_DIR / "Decode_Your_Heart_Research_Checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n")


if __name__ == "__main__":
    main()
