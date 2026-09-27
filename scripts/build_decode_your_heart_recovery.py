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
        "timestamps": ["0:00 promise to identify serious leg signals; doctor introduction", "mid-video intermittent claudication and pain-at-rest explanation", "3:31 target ended before post-roll"],
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
        "timestamps": ["0:00 chapter The morning sugar mystery", "2:20 evening-meal impact on next-morning glucose", "6:02 target ended before post-roll"],
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
        "timestamps": ["0:00 lipid-profile question and doctor introduction", "mid-video explanation of why LDL alone is insufficient", "3:36 end"],
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
        "timestamps": ["0:00 broad high-cholesterol framing", "1:40 HDL reverse-transport explanation", "3:50 end"],
        "opening": "Broad warning asks viewers to read the lipid result first without the paired video's exact-number promise.",
        "visuals": "Doctor and lipid report dominate the package; playback remains a steady explanatory presentation.",
        "editing": "Linear explanation with limited visual reset before the midpoint.",
        "closing": "Target video reached its natural end at 3:50.",
        "possible_explanation": "The broader promise and weaker first-30-second retention may reduce momentum.",
        "alternative_explanation": "Its smaller impression base and different audience exposure prevent a causal claim.",
    },
}


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
        "content_linkage": "ACTUAL_FULL_PLAYBACK" if priority else "NOT_PLAYBACK_VERIFIED",
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
            "Curve timestamps were linked to actual full playback; dips remain associative, not causal."
            if priority else
            "Numeric curve profile complete, but individual dip/spike meaning remains open until content at those timestamps is playback-verified."
        ),
    }


INVESTIGATION_STATUS_DEFINITIONS = {
    "NOT_STARTED": "No canonical metadata or transcript joined.",
    "TRANSCRIPT_ONLY": "Metadata, transcript and thumbnail joined; no saved playback record.",
    "PARTIAL_PLAYBACK": "Saved playback record exists but lacks numeric m:ss anchors, or long-form has fewer than one anchor per 60 seconds.",
    "PLAYBACK_COMPLETE": "Saved playback record with numeric anchors from 0:00 to end and adequate coverage.",
    "EDITING_AUDIT_COMPLETE": "PLAYBACK_COMPLETE plus specific opening, visuals, editing and closing observations.",
    "RETENTION_ANALYZED": "EDITING_AUDIT_COMPLETE plus an exported retention curve read against the observed timestamps.",
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
    return {
        "status": "COMPLETE_FULL_PLAYBACK",
        "full_editing_audit_status": "COMPLETE_WITH_AUDIO_LIMITATION",
        "observed_at": "2026-09-28",
        "source": f"https://www.youtube.com/watch?v={video_id}",
        "playback_speed": "2x for long-form; normal/player speed for Shorts",
        "completion_evidence": f"HTML5 player reached target duration/end at {item['duration_seconds']} seconds" + (" ; 2026-09-28 gap-fill: muted seek-and-inspect frames at listed anchors, captions read on screen" if video_id in {"-SjQc2MwaOU", "HEJoPEEndG8"} else ""),
        "comparison": item["comparison"],
        "timestamps": item["timestamps"],
        "opening_presentation": item["opening"],
        "doctor_delivery": "Direct clinician explanation with visible gestures; delivery content was reviewed with captions/transcript.",
        "speech_clarity_and_pacing": "Speech sequence was intelligible through player captions; precise vocal prosody was not independently scored.",
        "camera_framing": item["visuals"],
        "audio": "Playback completed, but no isolated headphone/loudness/noise measurement was made.",
        "b_roll_and_medical_visuals": item["visuals"],
        "on_screen_typography": THUMBNAIL_REVALIDATIONS[video_id],
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
            "playback_full": sum(r["playback_inspected"] == "COMPLETE_FULL_PLAYBACK" for r in records),
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
        "exact_next_unfinished_task": "Add numeric m:ss anchors at each exported retention dip for the four PARTIAL_PLAYBACK long-form videos (5oPzZjfNgII, EB3_A2b4a6o, BCNWQ3uuSuE, SBrMW71O69U); then audit the 44 TRANSCRIPT_ONLY videos in matched strong-versus-weak pairs.",
        "batch_history": [
            {"batch": "Batch 1 Recovery and Analytics", "status": "COMPLETE_WITH_LIMITATIONS", "saved_at": "2026-09-28", "result": "Four original Studio ZIPs verified; 56 basic per-video rows joined; 47 extended rows observed; missing Short resolved."},
            {"batch": "Batch 2 Retention and Actual Playback", "status": "PARTIAL", "saved_at": "2026-09-28", "result": "56 retention exports, 46 curves; 12 saved playback records, of which 8 meet RETENTION_ANALYZED and 4 long-form records are PARTIAL_PLAYBACK (too few numeric anchors); 44 TRANSCRIPT_ONLY. -SjQc2MwaOU and HEJoPEEndG8 anchors gap-filled 2026-09-28."},
            {"batch": "Batch 3 Research Diagnosis and Deliverables", "status": "COMPLETE_FOR_AVAILABLE_SYNTHESIS", "saved_at": "2026-09-28", "result": "Three Trends comparisons verified; six matched comparisons synthesized; diagnosis and four existing deliverables reconciled."},
        ],
        "execution_matrix": [
            {"task": "Metadata", "previous_result": "56 records", "current_evidence": "56 exact canonical Video IDs; current public catalog still 56 on 2026-09-28", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Transcripts", "previous_result": "56", "current_evidence": "56 original transcript files present", "status": "VERIFIED_COMPLETE", "required_action": "Reuse; do not reread wholesale"},
            {"task": "Thumbnails", "previous_result": "56", "current_evidence": "56 images identity-verified; 12 priority observations revalidated; 44 contain templated commentary", "status": "COMPLETE_NEEDS_CORRECTION", "required_action": "Revalidate remaining 44 only when they enter a priority comparison"},
            {"task": "Studio reports", "previous_result": "Four reported", "current_evidence": "Lifetime, 90d, 28d and traffic-source ZIP hashes verified", "status": "VERIFIED_COMPLETE", "required_action": "None"},
            {"task": "Individual Analytics", "previous_result": "55 references reported", "current_evidence": "56 file-backed basic rows; 47 authenticated extended rows; 9 extended rows not captured", "status": "PARTIAL", "required_action": "Capture remaining extended rows only if Studio table/export becomes reliable"},
            {"task": "Retention", "previous_result": "Previously missing", "current_evidence": "56 exports; 46 curves; 12 content-linked investigations; 34 curve-only profiles; 10 no-curve disclosures", "status": "PARTIAL", "required_action": "Link remaining 34 curves during playback; no action possible for 10 blank curves"},
            {"task": "Playback", "previous_result": "Previously missing", "current_evidence": "12 complete end-to-end player audits", "status": "PARTIAL", "required_action": "Audit remaining 44"},
            {"task": "Trends", "previous_result": "Three comparisons", "current_evidence": "Three original official CSVs and configurations verified", "status": "VERIFIED_COMPLETE", "required_action": "No repeat query justified by available source detail"},
            {"task": "Research synthesis", "previous_result": "Partial", "current_evidence": "Six matched comparisons and multi-stage diagnosis complete; audience/query/device/geography gaps remain", "status": "PARTIAL", "required_action": "Revisit only if unavailable Studio reports become accessible"},
        ],
        "phase_status": {
            "repository_recovery": "VERIFIED_COMPLETE",
            "thumbnail_recovery_and_visual_inspection": "COMPLETE_NEEDS_CORRECTION",
            "public_catalog_refresh": "VERIFIED_COMPLETE",
            "video_playback_forensics": "PARTIAL_8_ANALYZED_4_PARTIAL_OF_56",
            "retention_investigations": "PARTIAL_12_CONTENT_LINKED_34_CURVE_ONLY_10_NO_CURVE",
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
            "unavailable_reports": ["Per-video search queries", "Per-video suggested-video sources", "Geography", "Device", "Viewers across formats", "Structured new/returning viewer values"],
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
