#!/usr/bin/env python3
"""Build evidence-traceable BHWA breakout, comparison, visual, and review records."""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/research/senior-health-2026-09-25/forensic-v3"
STRUCTURE = BASE / "BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json"
OUTPUT = BASE / "BETTER-HEALTH-WHILE-AGING-DEEP-INVESTIGATIONS.json"
COLLECTED = "2026-09-27"


COMPARISON_FOR = {
    "16n80OQCVSM": "MEqT9LAn-Ek", "Ev-i_E_MlTo": "BzpaQ0F49JE",
    "MpohFGvHZHI": "Hxh7gjyq8Ak", "k-3BY-naQ0M": "MEqT9LAn-Ek",
    "R7uXQBjnTjk": "C9Y4ffXnzHY", "XX5Kw2OotL0": "dAIOQMFCSn8",
    "JUCiIDVTshA": "6y6kJFF7nJs", "8_depH-gT4o": "n2OArU9k-AU",
    "OCWvaUcSPOU": "M2cAj6IppM0", "m8_kM_BQQXc": "dAIOQMFCSn8",
    "jbVT7GSDsEs": "oNDVcr2NOvA", "K_jA1XD09Fs": "BzpaQ0F49JE",
    "w_Ol4q_ze6M": "M2cAj6IppM0", "YIvY8wyjfE4": "BzpaQ0F49JE",
    "cedhUKZ7B_g": "BM21ggH-Z30", "wvFBofvo9vM": "hhAPFWTwAGg",
    "3VlC5wjDYrQ": "K4356-ZoXCY", "0sC4L1ALRGs": "L1G5Zq0KsFs",
    "wO4XgM51tgw": "M2cAj6IppM0", "LbEwYj107pU": "xOf7R-YFWLs",
    "asdCF2RSC44": "39HnOWNmRY4", "Op4UsXgJEQU": "n2OArU9k-AU",
    "8ccVK-Z8s3Y": "MpohFGvHZHI", "hhAPFWTwAGg": "wvFBofvo9vM",
    "xOf7R-YFWLs": "LbEwYj107pU",
}

TOPIC_NOTES = {
    "16n80OQCVSM": ("Medication-risk list with a concrete, reversible threat: common drugs may slow an aging brain.", "Credential, prevalence problem, acetylcholine mechanism, seven drug groups, three high-risk audiences, medication-review steps.", "Anticholinergic is unfamiliar jargon, but Benadryl and seven categories convert it into recognizable choices.", "Strongest case combines fear with agency and named examples; later Beers-criteria explainer shows medication-avoidance topic alone is not sufficient."),
    "Ev-i_E_MlTo": ("Broad B12 deficiency explainer promises causes, symptoms, testing, and treatment.", "Role of B12, absorption/intrinsic factor, symptoms, serum and methylmalonic-acid testing, oral/injection treatment, recap.", "Treatable deficiency creates hope; low-normal testing gap creates diagnostic curiosity.", "Depth and practical testing pathway distinguish it; adjacent nutrition videos and later B12-form follow-up show topic demand, not proof of a single packaging cause."),
    "MpohFGvHZHI": ("Challenges normalization of memory loss and promises ten causes doctors should check.", "Myth correction, multifactorial model, ten causes, functional/cognitive/physical evaluation, labs and imaging, primary-care action plan.", "Open debt: memory loss may not mean Alzheimer’s; viewer waits for reversible causes and exact evaluation.", "Early-channel breakout delivers unusually comprehensive advocacy; shorter remake retained topic and list but achieved far less, weakening formula-only explanations."),
    "k-3BY-naQ0M": ("Four brain-slowing medication groups framed as avoidable barriers to memory improvement.", "Risk framing, medication classes and mechanisms, examples, safer alternatives, review-with-clinician plan.", "Promises improvement through subtraction, while withholding four categories until after credential and setup.", "Revisits channel’s peak theme with fewer categories and newer packaging; success supports durable audience concern, while generic Beers framing underperformed."),
    "R7uXQBjnTjk": ("Direct comparison resolves a common OTC choice for older adults.", "Defines three drugs, separates pain from cardiovascular use, organ-specific risks, scenario-based selection, dose and clinician cautions.", "Question title creates decision debt: no universally safest drug; answer depends on liver, kidney, bleeding, and cardiovascular context.", "High utility and familiar brand names matter; chronic-pain follow-up was useful but less decision-specific and much lower."),
    "XX5Kw2OotL0": ("Ten observable warning signs target adult children worried about a parent.", "Normal-vs-abnormal distinction, ten behavioral/functional signs, context and duration cautions, evaluation next steps.", "Recognition loop lets viewers score lived behaviors; diagnosis is deliberately withheld and cautioned against.", "Specific signs outperform adjacent ADL process content, but identical presenter/series/visual system means authority and design cannot explain gap."),
    "JUCiIDVTshA": ("Twenty-one behaviors, including paranoia, translate vague worry into an observation checklist.", "Safety disclaimer, checklist instructions, escalating cognitive/behavioral signs, acute-vs-chronic distinction, evaluation and workshop CTA.", "Emotionally salient paranoia is one entry, not sensational diagnosis; each next sign sustains enumeration debt.", "Large list and alarming title widen appeal, but careful transcript repeatedly limits self-diagnosis; memory topic’s early cluster is major confounder."),
    "8_depH-gT4o": ("Answers whether a number is too low by making symptoms and context central.", "Thresholds, acute and chronic causes, orthostatic/postprandial forms, measurement protocol, medication review, home-monitor plan.", "Question cannot be answered by one cutoff, producing useful diagnostic tension rather than a simplistic reveal.", "Same-series high-BP treatment videos are longer and similarly authoritative but less novel; reverse framing may explain appeal, not prove it."),
    "OCWvaUcSPOU": ("Seasonally relevant geriatric problem promises definition, symptoms, treatment, prevention, and heat safety.", "Age physiology, medication/mobility causes, unreliable symptoms, lab diagnosis, severity-based treatment, daily prevention, heat stroke.", "Counterintuitive point that thirst and visible signs can be unreliable sustains attention.", "Topic had seasonal demand and broad caregiver utility; thumbnail omits face yet performed strongly, countering a doctor-face requirement."),
    "m8_kM_BQQXc": ("Terminology-confusion hook distinguishes cognitive impairment, MCI, dementia, and Alzheimer’s.", "Defines cognition and syndromes, MCI criteria, dementia/independence threshold, Alzheimer pathology, diagnostic uncertainty, recap.", "Viewer seeks a clean taxonomy; progressive narrowing from symptom to syndrome to disease repays that debt.", "Direct semantic question and early cold open outperform process-led memory videos; topic cluster timing and series distribution remain confounds."),
    "jbVT7GSDsEs": ("Big question ‘reverse aging’ is narrowed into four exercise domains and realistic slowing/reversal of decline.", "Definitions, age-related decline, aerobic/strength/balance/flexibility, starting safely, frailty/cognitive barriers, protein support, recap.", "Contrarian ‘walking is not enough’ and conditional reverse-aging claim create repeated corrections.", "Broad promise plus exhaustive practical depth worked; later falls-prevention upload covers overlapping exercise/fall advice but had weaker aspirational framing."),
    "K_jA1XD09Fs": ("Follow-up resolves methylcobalamin-versus-cyanocobalamin dispute raised by comments.", "Form chemistry, conversion in body, comparative evidence, cyanide concern, stability/cost, diminishing-returns conclusion.", "Audience arrives expecting a winner; nuanced answer delays and then partially rejects strong online claims.", "Strong follow-up shows responsive exploitation of B12 demand; result may inherit topic momentum and cannot isolate title or script effects."),
    "w_Ol4q_ze6M": ("Common quality-of-life problem promises causes, red flags, and safe treatment sequence.", "Definition, bowel physiology, causes/medications, evaluation/red flags, routine/fiber/fluids, laxative classes, frailty cautions, recap.", "Safety questions around indefinite laxative use and fiber provide practical uncertainty.", "Large evergreen problem plus explicit age marker worked despite no face in thumbnail; no close same-topic internal failure exists, limiting causal comparison."),
    "YIvY8wyjfE4": ("Contrarian vitamin D frame challenges ‘more is better’ for seniors.", "Vitamin D biology and units, deficiency history, official intake, trial evidence on falls/fractures, guideline change, dosing advice.", "Narrative debt asks whether common high-dose practice survived randomized trials; answer unfolds through evidence.", "Accurate contrarianism and harm avoidance fit audience concern; adjacent nutrition content is not a close control."),
    "cedhUKZ7B_g": ("Eighty-second Medicare call-to-action targets people turning 65 and one immediate task.", "Eligibility prompt, automatic-enrollment caveat, missed-window penalty, medicare.gov and phone actions.", "Deadline and penalty create urgency; ‘isn’t it automatic?’ is answered conditionally.", "Radically shorter and more focused than two long Medicare explainers; likely public-service distribution/context confound means creative superiority is not established."),
    "wvFBofvo9vM": ("Specialist interview maps AFib symptoms, rhythm control, stroke prevention, blood thinners, Watchman, and lifestyle.", "Electrical-system analogy, diagnosis, symptom/rhythm treatments, anticoagulation, Watchman tradeoffs, lifestyle, recap.", "Treatment-choice debt persists across multiple branches rather than one reveal.", "Guest expertise and comprehensive decision map outperform AFib Shorts; slow-heart-rate interview is closest long-form control but covers different need."),
    "3VlC5wjDYrQ": ("Gender-specific treatment guide promises options beyond pads or medication.", "Bladder mechanics, five incontinence types, diary/evaluation, general measures, pelvic therapy/pessary/drugs, frailty and cognition, action plan.", "Type identification delays treatment choice; overlooked pelvic-floor and pessary options create discovery.", "Women-specific audience and treatment intent beat men’s broader symptom explainer by ~7x; publication age and sex-specific demand confound."),
    "0sC4L1ALRGs": ("UTI explainer directly addresses overdiagnosis in older adults while covering real danger signs.", "Anatomy and severity, local/systemic symptoms, diagnosis, sex and retention risks, asymptomatic bacteriuria, prevention, antibiotic stewardship.", "Contrarian debt: positive urine test does not always mean treatable UTI.", "High-stakes myth correction and specialist dialogue worked; narrower UTI-and-memory-loss episode was much lower despite same guests and visual style."),
    "wO4XgM51tgw": ("Symptom-to-cause explainer separates anemia from iron deficiency.", "Blood/hemoglobin basics, symptoms, production/loss causes, CBC and workup, questions for clinicians, iron pitfalls, recap.", "Viewer expects iron solution; script withholds it until cause classification and warns against assumption.", "Broad lab literacy and common symptom appeal outperform generic blood-test content, but no exact anemia control exists."),
    "LbEwYj107pU": ("Medication decision guide follows osteoporosis diagnosis and asks what to know before starting.", "DEXA/T-score context, fracture risk, bisphosphonates, administration/adverse effects/drug holidays, denosumab/anabolic agents, sequencing, questions.", "Risk-benefit and drug-sequence decisions sustain debt; rare adverse effects are contextualized.", "Medication-stage specificity outperformed prevention companion modestly; both share design and presenter, supporting intent-stage rather than thumbnail explanation."),
    "asdCF2RSC44": ("Timely 2026 update answers which COVID and flu vaccines older adults should get.", "Current burden data, updated products, eligibility and dose timing, flu formulations, coadministration, non-vaccine prevention, recap.", "Annual uncertainty and timing decisions supply urgency, but value decays rapidly.", "Unlike 2021–22 updates, this snapshot remained fresh at capture; age—not proven creative improvement—is dominant confound."),
    "Op4UsXgJEQU": ("Foundational hypertension explainer asks when treatment matters and how goals change with frailty.", "Blood-pressure mechanics, definitions/measurement, causes, harm, benefit evidence, age/frailty targets, home monitoring.", "Threshold disagreement and individualized target create decision debt.", "High-BP topic performs above median but far below low-BP reverse-angle video; same presenter/design makes novelty and problem framing plausible differences."),
    "8ccVK-Z8s3Y": ("Condensed ten-cause memory-loss episode gives differential diagnosis without full workup detail.", "Cold question, normal-aging correction, ten causes, MCI/dementia distinction, evaluation and series CTA.", "Reversible-cause list counters Alzheimer’s assumption.", "Near-duplicate topic/title of 2021 breakout drew ~11% of its views; shorter runtime and series packaging did not reproduce original outcome."),
    "hhAPFWTwAGg": ("Cardiology interview explains slow rates and pacemaker decisions.", "Threshold/context, ECG and conduction sites, device types/procedure, follow-up/battery, end-of-life issues, newer placement.", "Pacemaker necessity and procedure fear create sequential questions.", "Useful but specialist and technical; AFib interview reached roughly twice views, suggesting broader disease concern rather than interview format alone."),
    "xOf7R-YFWLs": ("Prevention-focused bone guide promises stronger bones and fewer fractures.", "Bone remodeling, DEXA scores, primary/secondary causes, exercise/calcium/vitamin D, hormones/drugs, protein evidence, monitoring.", "Viewer waits for actions that actually change density; script separates association from trial evidence.", "Broad prevention appeal slightly trails medication companion despite similar visual system; both qualify, showing cluster strength without one dominant angle."),
}

THUMB_TEXT = {
    "16n80OQCVSM":"7 Common Brain-slowing Drugs to Avoid in Aging", "Ev-i_E_MlTo":"VITAMIN B12 AND AGING", "MpohFGvHZHI":"MEMORY LOSS IN AGING? WHAT DOCTORS SHOULD CHECK",
    "k-3BY-naQ0M":"4 TYPES OF MEDICATIONS TO AVOID TO IMPROVE MEMORY", "R7uXQBjnTjk":"WHICH PAINKILLER IS SAFEST IN AGING?", "XX5Kw2OotL0":"10 WARNING SIGNS OF ALZHEIMER'S",
    "JUCiIDVTshA":"21 Signs & Behaviors that are NOT Normal in Aging", "8_depH-gT4o":"HOW TO KNOW IF BLOOD PRESSURE IS TOO LOW?", "OCWvaUcSPOU":"DEHYDRATION IN AGING",
    "m8_kM_BQQXc":"ALZHEIMER'S VS. DEMENTIA WHAT'S THE DIFFERENCE?", "jbVT7GSDsEs":"HOW TO EXERCISE TO AGE WELL", "K_jA1XD09Fs":"WHICH TYPE OF B12 IS BETTER?",
    "w_Ol4q_ze6M":"CONSTIPATION IN AGING", "YIvY8wyjfE4":"VITAMIN D: WHY LESS IS MORE IN AGING", "cedhUKZ7B_g":"HOW TO GET STARTED WITH MEDICARE",
    "wvFBofvo9vM":"ATRIAL FIBRILLATION IN OLDER ADULTS", "3VlC5wjDYrQ":"URINARY INCONTINENCE IN OLDER WOMEN", "0sC4L1ALRGs":"URINARY TRACT INFECTIONS IN AGING",
    "wO4XgM51tgw":"ANEMIA IN AGING", "LbEwYj107pU":"OSTEOPOROSIS DRUGS EXPLAINED", "asdCF2RSC44":"COVID & Aging Adults / Fall 2026 Update: COVID & Flu Vaccines / Leslie Kernisan, MD MPH / BetterHealthWhileAging.net",
    "Op4UsXgJEQU":"HIGH BLOOD PRESSURE IN AGING", "8ccVK-Z8s3Y":"CAUSES OF MEMORY LOSS IN OLD AGE", "hhAPFWTwAGg":"SLOW HEART RATES IN AGING", "xOf7R-YFWLs":"BOOSTING BONE DENSITY IN AGING",
    "dAIOQMFCSn8":"HOW ADLS & IADLS CHANGE IN EARLY ALZHEIMER'S", "Hxh7gjyq8Ak":"DOES GETTING A MEMORY LOSS EVALUATION MATTER?", "6y6kJFF7nJs":"IS MEMORY LOSS NORMAL WITH AGING?",
    "oNDVcr2NOvA":"BEST WAYS TO PREVENT FALLS IN AGING", "BM21ggH-Z30":"ESSENTIAL PARTS OF MEDICARE", "XEweB2GK9Ls":"THE EASIEST WAY TO PICK THE BEST MEDICARE PLAN",
    "K4356-ZoXCY":"URINARY INCONTINENCE IN AGING MEN", "L1G5Zq0KsFs":"UTIS IN MEMORY LOSS & NURSING HOMES", "n2OArU9k-AU":"HOW TO LOWER BLOOD PRESSURE",
    "C9Y4ffXnzHY":"TREATING CHRONIC PAIN IN AGING", "M2cAj6IppM0":"TOP 4 BLOOD TESTS IN AGING", "Ppjoa2fmhCY":"COVID & Vaccination for Aging Adults / Updates & Recommendations / (10.28.21 Edition)",
    "JcCfj0iqliY":"COVID & Aging Adults / Updates on Omicron & More / (2.24.22 Edition)", "39HnOWNmRY4":"What's NEW for 2022 with Flu Vaccines for Aging Adults / September 2022",
}

NO_FACE = {"OCWvaUcSPOU", "w_Ol4q_ze6M", "C9Y4ffXnzHY"}
INTERVIEW = {"wvFBofvo9vM", "0sC4L1ALRGs", "hhAPFWTwAGg", "BM21ggH-Z30", "XEweB2GK9Ls", "L1G5Zq0KsFs"}
WHITE_UPDATE = {"asdCF2RSC44", "Ppjoa2fmhCY", "JcCfj0iqliY", "39HnOWNmRY4"}


def locator_for(row: dict) -> str:
    return row["caption_provenance"]["evidence_locator"]


def age_days(published_at: str) -> int:
    return (date.fromisoformat(COLLECTED) - date.fromisoformat(published_at[:10])).days


def comparison_rationale(bid: str, cid: str) -> tuple[str, str]:
    high = {"XX5Kw2OotL0", "m8_kM_BQQXc", "cedhUKZ7B_g", "3VlC5wjDYrQ", "0sC4L1ALRGs", "Op4UsXgJEQU", "8ccVK-Z8s3Y", "asdCF2RSC44"}
    quality = "HIGH" if bid in high else "MEDIUM"
    rationales = {
        "dAIOQMFCSn8":"same HOP-ML series, host, period, memory/Alzheimer’s audience, regular format",
        "Hxh7gjyq8Ak":"same memory-care series and family audience; process/evaluation intent versus causes",
        "6y6kJFF7nJs":"same early memory series and normal-versus-abnormal question framing",
        "MEqT9LAn-Ek":"same medication-safety audience; broader Beers-criteria packaging",
        "C9Y4ffXnzHY":"same pain-management cluster and older-adult audience; broader chronic-pain intent",
        "n2OArU9k-AU":"same blood-pressure series, presenter, format, and close publication period",
        "M2cAj6IppM0":"same practical geriatric explainer format; adjacent diagnostic/self-management intent",
        "oNDVcr2NOvA":"same exercise/fall-independence audience and long-form educational format",
        "BzpaQ0F49JE":"same nutrition/supplement audience and long-form evidence-led format; topic not exact",
        "BM21ggH-Z30":"same Medicare audience; comprehensive interview versus focused enrollment CTA",
        "hhAPFWTwAGg":"same cardiology guest/interview format and treatment-decision audience",
        "K4356-ZoXCY":"same incontinence topic, presenter, format; audience sex differs",
        "L1G5Zq0KsFs":"same UTI guests and interview format; narrower memory/nursing-home angle",
        "39HnOWNmRY4":"same seasonal vaccine-update family; older snapshot provides durability control",
        "Ppjoa2fmhCY":"same COVID/vaccine update family; 2021 dated edition provides durability control",
        "JcCfj0iqliY":"same COVID update family; 2022 dated edition provides durability control",
        "MpohFGvHZHI":"same ten-causes memory title/topic; earlier full-length version",
        "wvFBofvo9vM":"same cardiology guest/interview format; AFib topic differs",
        "xOf7R-YFWLs":"same bone-health cluster and close publication period; prevention versus medication intent",
        "LbEwYj107pU":"same bone-health cluster and close publication period; medication versus prevention intent",
    }
    return rationales[cid], quality


def thumb_record(video_id: str, row: dict) -> dict:
    if video_id in WHITE_UPDATE:
        composition = "White update card on black field; clinician portrait at left; large dated text; credentials/site footer."
        authority = "White coat/stethoscope plus printed MD/MPH attribution."
        complexity = "MEDIUM_HIGH"
    elif video_id in INTERVIEW:
        composition = "Teal field; large left-aligned text; two stacked webcam portraits with name/credential labels at right."
        authority = "Named clinician/guest credentials in image; interview format visible."
        complexity = "MEDIUM"
    elif video_id in NO_FACE:
        composition = "Teal field with oversized black/white text only; no person, object, icon, or medical diagram."
        authority = "No visual authority cue beyond channel-consistent design."
        complexity = "LOW"
    else:
        composition = "Teal field; oversized left-aligned black/white text; smiling clinician in white coat with stethoscope at right."
        authority = "Doctor portrait, white coat, and stethoscope; no credential text."
        complexity = "LOW"
    return {
        "video_id": video_id, "title": row["title"], "thumbnail_url": f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
        "collection_date": COLLECTED, "inspection_state": "VISUALLY_INSPECTED", "evidence_temporality": "CURRENT_PUBLIC_THUMBNAIL_NOT_VERIFIED_AS_ORIGINAL_PUBLICATION_ASSET",
        "visible_text": THUMB_TEXT[video_id], "composition": composition, "focal_point": "text only" if video_id in NO_FACE else "clinician face plus headline",
        "imagery": "No illustrative medical imagery; photographic subject only where present.", "clinical_authority_cues": authority,
        "contrast": "High black/white text contrast on teal" if video_id not in WHITE_UPDATE else "High black text on white with black outer field",
        "visual_complexity": complexity, "curiosity_mechanism": "Question/contrast/list specificity in text; answer usually withheld." if "?" in THUMB_TEXT[video_id] or any(k in THUMB_TEXT[video_id] for k in ("7 ", "10 ", "21 ", "4 ", "WHY", "VS.")) else "Topic label; little independent mystery beyond title.",
        "title_relationship": "Mostly restates or compresses title; adds no separate visual mechanism or medical object.",
        "inspection_method": "Direct browser render of registered maxresdefault URL; analyst visual observation.",
    }


def main() -> None:
    source = json.loads(STRUCTURE.read_text(encoding="utf-8"))
    rows = {row["video_id"]: row for row in source["videos"]}
    ordered = sorted(rows.values(), key=lambda r: r["published_at"])
    all_median = median(r["views"] for r in ordered)
    regular_median = median(r["views"] for r in ordered if r["video_type"] == "video")
    shorts_median = median(r["views"] for r in ordered if r["video_type"] == "shorts")
    breakouts = []
    for inv in source["breakout_inventory"]:
        row = rows[inv["video_id"]]
        idx = ordered.index(row)
        local = [x["views"] for x in ordered[max(0, idx-10):idx] + ordered[idx+1:idx+11] if x["video_type"] == row["video_type"]]
        local_median = median(local) if local else None
        note = TOPIC_NOTES[row["video_id"]]
        comp_id = COMPARISON_FOR[row["video_id"]]
        comp = rows[comp_id]
        rationale, quality = comparison_rationale(row["video_id"], comp_id)
        breakouts.append({
            "video_id": row["video_id"], "cohort": inv["cohort"], "transcript_review_state": "COMPLETE_TRANSCRIPT_REVIEWED",
            "identity_and_metrics": {"title": row["title"], "published_at": row["published_at"], "views_at_snapshot": row["views"], "format": row["video_type"], "duration_seconds": row["duration_seconds"], "age_days_at_2026_09_27": age_days(row["published_at"]), "multiple_vs_all_video_median": round(row["views"]/all_median, 2), "multiple_vs_regular_median": round(row["views"]/regular_median, 2), "multiple_vs_local_20_video_median": round(row["views"]/local_median, 2) if local_median else None, "views_per_age_day_snapshot": round(row["views"]/max(1, age_days(row["published_at"])), 2), "evidence_locator": locator_for(row)},
            "title_analysis": note[0],
            "opening_and_audience": {"actual_opening_excerpt": row["actual_opening_and_audience_promise"], "intended_audience": "Adults over 60 and/or family caregivers managing the named aging-health decision.", "analysis": "Opening names clinician role, channel scope, target problem, and promised coverage; later-era episodes often add a cold question before standard introduction."},
            "timed_opening": {"timing_method": row["timing_method"], "first_15_seconds": row["opening_first_15_seconds"], "first_30_seconds": row["opening_first_30_seconds"], "first_60_seconds": row["opening_first_60_seconds"]},
            "hook_and_psychology": note[0], "title_script_alignment": "DELIVERED: transcript substantively covers title promise; caveats narrow absolute wording where medically required.",
            "script_progression": note[1], "authority_and_evidence": f"Board-certified geriatrician identity plus mechanisms, clinical practice examples, guidelines/studies or specialist guest where relevant. Machine counts: {row['authority_and_supporting_evidence']['counts']}.",
            "curiosity_and_narrative_debt": note[2], "major_revelations": [{"observation": s["opening_excerpt"], "word_range": [s["start_word"], s["end_word"]], "timing": row["timing_method"]} for s in row["script_structure"][1:4]],
            "practical_advice": {"analysis": "Ends with condition-specific monitoring, clinician questions, safer alternatives, or stepwise self-management; does not tell viewers to stop prescription treatment independently.", "first_recommendation_locator": row["practical_recommendations"]["first"]},
            "closing_and_cta": row["conclusion_and_cta"],
            "matched_comparison": {"comparison_video_id": comp_id, "comparison_title": comp["title"], "comparison_views": comp["views"], "matching_rationale": rationale, "comparison_quality": quality, "observable_difference": f"Breakout {row['views']:,} views versus comparison {comp['views']:,}; public snapshot only."},
            "supporting_evidence": note[3].split(";", 1)[0] + ".",
            "contradictory_evidence": note[3].split(";", 1)[1].strip() if ";" in note[3] else "Same surface format also appears in weaker videos.",
            "conclusion": note[3],
            "limitations": ["No impressions, CTR, retention, traffic-source, or historical thumbnail data.", "View counts are unequal-age public snapshots, not velocity curves.", "Plaintext captions lack cue timestamps; 15/30/60-second windows are estimated from word position.", "Association does not establish why recommendation systems distributed the video."],
        })

    comparison_ids = sorted((set(COMPARISON_FOR.values()) | {"Ppjoa2fmhCY", "JcCfj0iqliY"}) - {x["video_id"] for x in source["breakout_inventory"]})
    comparisons = []
    for cid in comparison_ids:
        row = rows[cid]
        paired = [bid for bid, value in COMPARISON_FOR.items() if value == cid] or ["asdCF2RSC44"]
        rationale, quality = comparison_rationale(paired[0], cid)
        comparisons.append({
            "comparison_video_id": cid, "title": row["title"], "views_at_snapshot": row["views"], "published_at": row["published_at"], "video_age_days": age_days(row["published_at"]), "format": row["video_type"],
            "paired_breakout_ids": paired, "matching_rationale": rationale, "important_similarities": "Same channel, presenter/authority system, regular format, and a related audience problem; thumbnail style is controlled more tightly than across-channel comparisons.",
            "important_differences": "Intent, specificity, novelty, publication timing, and topic differ; these variables prevent a clean causal winner/loser claim.",
            "public_performance": f"{row['views']:,} views at retained snapshot; {round(row['views']/regular_median,2)}x regular-video median.",
            "publication_timing": row["published_at"], "transcript_observations": {"opening": row["actual_opening_and_audience_promise"], "progression": [s["opening_excerpt"] for s in row["script_structure"]], "ending": row["conclusion_and_cta"]["ending_excerpt"]},
            "thumbnail_observations": THUMB_TEXT.get(cid, "Visually inspected current thumbnail; see thumbnail_inspections when registered."),
            "competing_explanations": ["Topic demand", "problem/decision specificity", "unequal video age", "distribution history", "audience fit", "unobserved packaging changes"],
            "confounding_variables": ["No first-party analytics", "single public snapshot", "publication dates differ", "topic match is imperfect for some pairs"], "comparison_quality": quality,
            "transcript_review_state": "COMPLETE_TRANSCRIPT_REVIEWED", "evidence_locator": locator_for(row),
        })

    visual_ids = list(THUMB_TEXT)
    thumbnails = [thumb_record(vid, rows[vid]) for vid in visual_ids]
    payload = {
        "artifact_type": "BHWA_DEEP_FORENSIC_INVESTIGATION_REGISTER", "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": {"breakout_cases": 25, "comparison_transcripts": len(comparisons), "thumbnail_inspections": len(thumbnails), "collection_date": COLLECTED},
        "population_baselines": {"all_video_median": all_median, "regular_video_median": regular_median, "shorts_median": shorts_median, "candidate_rule_preserved": "views >= 5 * all-video median", "format_specific_sensitivity": "All 25 candidates are regular videos. Using 5x regular-video median retains 21/25; Op4UsXgJEQU, 8ccVK-Z8s3Y, hhAPFWTwAGg, and xOf7R-YFWLs fall below that stricter screen.", "age_sensitivity": "Per-day and local-20-video multiples are descriptive controls only; snapshots do not reconstruct early velocity."},
        "first_party_analytics": {"status": "NOT_AVAILABLE", "missing": ["impressions", "CTR", "retention", "traffic sources", "historical view curves"]}, "causal_claims_authorized": False,
        "breakout_investigations": breakouts, "comparison_investigations": comparisons, "thumbnail_inspections": thumbnails,
        "historical_demand_investigations": [
            {"id":"GT-BHWA-01","terms":["memory loss","vitamin B12 deficiency","dementia"],"geo":"US","property":"YouTube Search","range":"2021-01-01 to 2026-09-27","collected":COLLECTED,"observation":"Dementia has materially higher normalized interest than the other two across the displayed period; B12 is volatile and lower. No publication-specific traffic inference is supported.","url":"https://trends.google.com/trends/explore?date=2021-01-01%202026-09-27&geo=US&gprop=youtube&q=memory%20loss,vitamin%20B12%20deficiency,dementia"},
            {"id":"GT-BHWA-02","terms":["anticholinergic","medications to avoid","low blood pressure","dehydration"],"geo":"US","property":"YouTube Search","range":"2021-01-01 to 2026-09-27","collected":COLLECTED,"observation":"Dehydration dominates and shows a pronounced seasonal spike; anticholinergic is comparatively tiny. This supports broad seasonal demand, not a claim that search caused views.","url":"https://trends.google.com/trends/explore?date=2021-01-01%202026-09-27&geo=US&gprop=youtube&q=anticholinergic,medications%20to%20avoid,low%20blood%20pressure,dehydration"},
            {"id":"GT-BHWA-03","terms":["vitamin B12 deficiency"],"geo":"US","property":"YouTube Search","range":"2021-01-01 to 2026-09-27","collected":COLLECTED,"observation":"Normalized interest is volatile with intermittent peaks; no clear unique spike at the February 2025 BHWA publication is visible at this resolution.","url":"https://trends.google.com/trends/explore?date=2021-01-01%202026-09-27&geo=US&gprop=youtube&q=vitamin%20B12%20deficiency"},
            {"id":"GT-BHWA-04","terms":["Medicare","osteoporosis","urinary incontinence","constipation"],"geo":"US","property":"YouTube Search","range":"2021-01-01 to 2026-09-27","collected":COLLECTED,"observation":"Medicare shows recurring sharp seasonal peaks; constipation is steadier and substantial; osteoporosis rises gradually; urinary incontinence is lower. Normalized comparison cannot supply absolute searches.","url":"https://trends.google.com/trends/explore?date=2021-01-01%202026-09-27&geo=US&gprop=youtube&q=Medicare,osteoporosis,urinary%20incontinence,constipation"},
        ],
        "external_comparable_video_research": [
            {"topic":"Dehydration","url":"https://www.youtube.com/watch?v=HwwkLIirmAo","title":"Signs and Symptoms of Dehydration in Seniors","channel":"mmlearn.org","published":"2015-07-30","public_views_observed":31255,"observation":"Older, shorter caregiver explainer existed a decade before BHWA and had meaningful but much lower public reach. Age/channel/length differ; count does not prove creative inferiority."},
            {"topic":"Vitamin B12 deficiency","url":"https://www.doctorodonovan.com/videos/doctor-explains-vitamin-b12-deficiency-causes-symptoms-foods-treatment-and-more","title":"Doctor explains Vitamin B12 Deficiency | Causes, Symptoms, Foods, Treatment and more!","channel":"Dr. James O'Donovan","published":"2025-01-19","observation":"Closely related clinician explainer appeared about one month before BHWA, confirming active competition. Comparable public view count was not verified, so no winner claim."},
            {"topic":"Anticholinergic medication risk","url":"https://www.youtube.com/watch?v=HE4mJJKPHuE","title":"Doctor Explains: 9 Common Medications That May Increase Dementia Risk","channel":"William Health Insights","published":"2026-07-23","public_views_observed":460066,"observation":"Later, smaller medical channel achieved substantial public reach with nearly same medication-memory promise. Supports durable topic demand; later date and channel context block causal comparison."},
            {"topic":"MCI/dementia distinction","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9807411/","title":"The physician's Alzheimer's disease management guide","published":"2022","observation":"External clinical literature supports distinction and multiple-cause framing. Not a YouTube performance comparator; used only for topic/evidence context."},
        ],
        "medical_claim_reviews": [
            {"videos":["16n80OQCVSM","k-3BY-naQ0M"],"claim":"Anticholinergic drugs can impair cognition in older adults; medication changes require clinician review.","assessment":"SUPPORTED_WITH_CAUTION","source":"https://www.nia.nih.gov/sites/default/files/d7/MedAgeBrain-Brochure.pdf","note":"NIA supports confusion/memory effects and professional review. Observational dementia associations do not prove that any individual drug caused dementia."},
            {"videos":["Ev-i_E_MlTo","K_jA1XD09Fs"],"claim":"Older adults are at risk of B12 deficiency; MMA can clarify borderline status; high-dose oral therapy can be effective.","assessment":"SUPPORTED_WITH_EVIDENCE_LIMITS","source":"https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/","note":"NIH supports risk, symptoms and oral treatment evidence but notes low-quality RCT evidence; B12 does not generally improve cognition absent deficiency."},
            {"videos":["YIvY8wyjfE4"],"claim":"Routine high-dose vitamin D and routine testing are not justified for healthy 50–74-year-olds; lower daily doses preferred when indicated.","assessment":"SUPPORTED_AND_AGE_DEPENDENT","source":"https://www.endocrine.org/clinical-practice-guidelines/vitamin-d-for-prevention-of-disease","note":"Guideline separately suggests empiric supplementation for adults 75+; ‘less is more’ needs this age distinction."},
            {"videos":["R7uXQBjnTjk"],"claim":"Long-term NSAIDs can cause bleeding or kidney harm and may be unsafe for many older adults.","assessment":"SUPPORTED","source":"https://www.nia.nih.gov/health/pain/pain-you-can-get-help","note":"No single OTC analgesic is safest for every person; liver disease, kidney disease, bleeding, cardiovascular use and dose matter."},
            {"videos":["0sC4L1ALRGs","L1G5Zq0KsFs"],"claim":"Do not screen for or treat asymptomatic bacteriuria in most older adults; delirium/falls alone require other-cause assessment.","assessment":"SUPPORTED","source":"https://www.idsociety.org/practice-guideline/asymptomatic-bacteriuria/","note":"Exceptions and systemic instability require clinical judgment; transcript appropriately avoids absolute no-treatment advice."},
            {"videos":["8_depH-gT4o","Op4UsXgJEQU"],"claim":"Orthostatic hypotension is a sustained >=20/10 mmHg fall within 3 minutes standing and is common with age.","assessment":"SUPPORTED","source":"https://professional.heart.org/en/science-news/orthostatic-hypotension-in-adults-with-hypertension/top-things-to-know","note":"Individual BP targets remain contextual; video’s symptom/medication emphasis is defensible."},
            {"videos":["OCWvaUcSPOU"],"claim":"Adults 65+ are more heat-vulnerable, may not adjust well, and should not wait for thirst in hot weather.","assessment":"SUPPORTED_WITH_FLUID_RESTRICTION_CAVEAT","source":"https://www.cdc.gov/heat-health/risk-factors/heat-and-older-adults-aged-65.html","note":"CDC explicitly says people on fluid limits/diuretics should ask clinicians how much to drink."},
            {"videos":["xOf7R-YFWLs","LbEwYj107pU"],"claim":"Approved osteoporosis medicines can reduce fracture risk; drug choice and sequencing depend on risk.","assessment":"SUPPORTED","source":"https://www.bonehealthandosteoporosis.org/patients/treatment/medicationadherence/","note":"Rare harms and drug holidays require individualized management; lifestyle alone is not equivalent after high-risk fracture."},
        ],
        "knowledge_framework_applications": [
            {"source":"DS-000011 TR-011-004","framework":"one big idea / bold readable packaging","support":["16n80OQCVSM","Ev-i_E_MlTo","R7uXQBjnTjk"],"counterexamples":["dAIOQMFCSn8","n2OArU9k-AU"],"result":"Fits nearly all channel thumbnails, including failures; channel constant, not sufficient explanation."},
            {"source":"DS-000011 TR-011-003","framework":"first 0–30 seconds clarity/curiosity/emotion","support":["m8_kM_BQQXc","LbEwYj107pU","asdCF2RSC44"],"counterexamples":["6y6kJFF7nJs","Hxh7gjyq8Ak"],"result":"Cold questions help some later videos, but equally clear memory openings fail; partial creative hypothesis."},
            {"source":"DS-000011 TR-011-014","framework":"title/script promise alignment","support":["MpohFGvHZHI","w_Ol4q_ze6M","3VlC5wjDYrQ"],"counterexamples":["jbVT7GSDsEs"],"result":"Promises are generally delivered; ‘reverse aging’ is responsibly narrowed, so alignment cannot explain performance variance."},
            {"source":"DS-000018 ALG26-CLM-003","framework":"evergreen videos can accumulate late views","support":["16n80OQCVSM","MpohFGvHZHI","Ev-i_E_MlTo"],"counterexamples":["Ppjoa2fmhCY","JcCfj0iqliY","39HnOWNmRY4"],"result":"Evergreen explainers dominate old updates; snapshots cannot identify when views accrued."},
            {"source":"DS-000018 ALG26-CLM-008","framework":"each upload earns own audience; hit does not raise floor","support":["16n80OQCVSM","k-3BY-naQ0M","Ev-i_E_MlTo"],"counterexamples":["K_jA1XD09Fs"],"result":"Most immediate neighbors revert, while B12 follow-up stayed high; topic clusters can recur without durable floor lift."},
            {"source":"DS-000018 ALG26-CLM-005","framework":"format preferences remain distinct","support":["all 25 breakouts are regular videos"],"counterexamples":["2DsxuIYUvcY"],"result":"18 Shorts median 3,153 versus regular median 28,688; one B12 Short reached 30,899. Format baseline matters, absolute separation does not."},
            {"source":"DS-000031 CS-013/015/020","framework":"Outlier to Demand Signal","support":["memory cluster","B12 cluster","bone-health pair"],"counterexamples":["8ccVK-Z8s3Y","MEqT9LAn-Ek"],"result":"Repeated topic success supports demand signal; remakes and broad variants show it does not transfer automatically."},
            {"source":"DS-000031 CS-028..032","framework":"Narrative Debt","support":["8_depH-gT4o","YIvY8wyjfE4","m8_kM_BQQXc"],"counterexamples":["Hxh7gjyq8Ak","6y6kJFF7nJs"],"result":"Unresolved diagnostic/contrarian questions fit wins and failures. Useful script lens, not causal explanation."},
            {"source":"DS-000031 CS-059/060","framework":"Doubling Down / Hit-Follow-up-Cluster-Series","support":["Ev-i_E_MlTo","K_jA1XD09Fs","xOf7R-YFWLs","LbEwYj107pU"],"counterexamples":["MpohFGvHZHI","8ccVK-Z8s3Y"],"result":"Fresh follow-ups sometimes preserve demand; condensed repeat of memory-causes did not. Double down on unresolved audience question, not title surface."},
        ],
        "limitations": ["External comparable-video search is a disclosed sample, not an exhaustive YouTube census.", "Google Trends values are normalized relative interest, not absolute searches or YouTube traffic attribution.", "Current thumbnails may differ from publication thumbnails.", "Four comparisons are adjacent-topic rather than exact-topic because no valid internal control exists."],
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
