"""Programmatic transcript forensics over the ACTUAL stored transcript text
(registry DB `transcripts.transcript_text`) for all Senior Health cohort videos.

Stored transcripts are plaintext with no timestamps. Every time-based field is
derived from word position x (duration_seconds / word_count) and labelled
APPROXIMATED_FROM_WORD_POSITION. All lexical feature flags are
TRANSCRIPT_LEXICAL_HEURISTIC: they detect wording, not intent.

Also runs cross-channel duplicate detection (title similarity + transcript
5-gram shingle Jaccard).

Outputs (forensic-v2/):
  TRANSCRIPT-FORENSICS.json      one record per video (deep-sample flag set)
  DUPLICATE-NETWORK.json         candidate duplicate pairs with performance
"""
import json, re, sqlite3, difflib, statistics
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[5]
DB = ROOT / "data/catalog/youtube_channel_registry.db"
FACTS = json.load(open(HERE / "VERIFIED-FACTS.json"))
SAMPLE = {v["video_id"] for v in json.load(open(HERE.parent / "DEEP-ANALYSIS-SAMPLE.json"))}
TIME_LABEL = "APPROXIMATED_FROM_WORD_POSITION"

LEX = {
    "audience_id": r"\b(after|over|past) (5|6|7|8)0\b|\bseniors?\b|\belderly\b|\bolder adults?\b|\byou or someone you love\b|\bif you('re| are) (over|in your) ",
    "authority": r"\bas a (doctor|physician|cardiologist|surgeon|neurologist|nurse)\b|\bin my (practice|clinic|years|career)\b|\bmy patients?\b|\bi've (treated|seen|worked)\b|\b\d+ years (of|in) (practice|medicine)\b",
    "credibility": r"\bstud(y|ies)\b|\bresearch(ers)?\b|\bjournal\b|\bpublished\b|\buniversity\b|\baccording to\b|\bclinical trial\b|\bharvard\b|\bmayo\b|\bamerican (heart|diabetes)\b",
    "fear": r"\bdanger(ous)?\b|\bdeadly\b|\bkill(s|ing)?\b|\bdie\b|\bdeath\b|\bstroke\b|\bheart attack\b|\bsilent(ly)?\b|\bwarning\b|\bdamag(e|ing)\b|\bserious\b|\bemergency\b|\bamputation\b|\bfatal\b",
    "hope": r"\bgood news\b|\bimprove\b|\bheal(ing)?\b|\brestore\b|\bprotect\b|\bstrong(er)?\b|\byou can\b|\bnot too late\b|\bfeel better\b|\bindependen(t|ce)\b|\bbenefit\b",
    "curiosity": r"\bsecret\b|\bno one (tells|talks)\b|\bhidden\b|\bsurpris(e|ing)\b|\bwhat happens\b|\bmost people (don't|never)\b|\bthe truth\b|\bshock(ing|ed)\b|\bmistake\b",
    "open_loop": r"\blater in (this|the) video\b|\bstay (with me )?(until|to) the end\b|\bby the end of this video\b|\bi'll (show|reveal|explain|tell) you\b|\bin a moment\b|\bbut first\b|\bkeep watching\b|\bnumber one\b.{0,80}\b(surprise|most important)\b|\bwe'll get to\b",
    "story": r"\bi remember\b|\bmy patient\b|\ba patient\b|\b\d{2}[- ]year[- ]old\b|\bher (husband|daughter|son)\b|\bhis (wife|daughter|son)\b|\bshe (told|said)\b|\bhe (told|said)\b|\bone day\b|\blast (week|year|month)\b|\bnamed [A-Z]",
    "pattern_interrupt": r"\bbut here'?s\b|\bhere'?s the thing\b|\bnow here'?s\b|\bwait\b|\bpause\b|\bthink about (that|this)\b|\bstop (and|right)\b|\blet that sink in\b",
    "cta": r"\bsubscribe\b|\bhit the (like|bell)\b|\blike (this|the) video\b|\bcomment (below|down)\b|\bin the comments\b|\bshare this (video|with)\b|\bnotification\b",
    "bridge": r"\bnext video\b|\bwatch this video\b|\bthe video on (your )?screen\b|\bcheck out (this|my|our)\b|\bi'll see you in\b|\bclick (on )?(the|this) video\b",
    "enumeration": r"\bnumber (one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b|\b(sign|step|food|tip|mistake|exercise|habit|reason|drink|pill|vegetable) (number )?(one|two|three|four|five|six|seven|eight|nine|ten|#?\d)\b|\b(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth)(ly)?,",
    "medical_claim": r"\b(lower|lowers|reduce|reduces|increase|increases|raise|raises|prevent|prevents|cure|cures|reverse|reverses|protect|protects|damage|damages|cause|causes|boost|boosts|flush|flushes|dissolve|dissolves|unclog|clears?)\b[^.?!]{0,60}\b(blood|sugar|pressure|cholesterol|arter|heart|kidney|liver|stroke|inflammation|risk|nerve|brain|memory|circulation|colon|toxin|plaque|insulin|bone)",
    "disclaimer": r"\b(talk|speak|check) (to|with) your (doctor|physician|pharmacist)\b|\bnot (medical|a substitute)\b|\bconsult\b|\bthis video is for (educational|informational)\b",
    "ai_disclosure": r"\bAI[- ]assisted\b|\bartificial intelligence\b[^.]{0,40}\b(tools?|voice|narrat)|\bsynthetic (voice|media)\b|\bcomposites?\b|\bnot real (names|patients)\b",
    "specific_study_claim": r"\b(a|one) (19|20)\d\d study\b|\bstudy (from|at|by|in|published in) (the )?[A-Z][a-z]+|\b(Harvard|Stanford|Johns Hopkins|Mayo|Cleveland Clinic|Yale|Oxford|Cambridge)\b[^.]{0,60}\b(study|trial|found|research)|\b\d+(\.\d+)? ?(%|percent) (less|more|lower|higher|reduction|increase|greater|fewer)\b",
    "cure_language": r"\bcure[sd]?\b|\breverse[sd]?\b|\bmiracle\b|\bflush(es)? out\b|\bdetox\b|\bdissolve[sd]?\b|\bunclog\b|\bmelt(s)? away\b|\binstead of (your )?medication\b|\bstop taking\b",
}
LEX = {k: re.compile(v, re.I) for k, v in LEX.items()}
HOOK_RULES = [  # checked on first ~30s text, first match wins -> primary hook archetype
    ("DIRECT_COMMAND", r"^\W*(look|right now|put|grab|stop|take|try|check|go to|press|touch|imagine)\b"),
    ("WHAT_IF_QUESTION", r"\bwhat if (i|you)\b"),
    ("STORY_OPEN", LEX["story"].pattern),
    ("QUESTION", r"\?"),
    ("STATISTIC", r"\b\d+ ?(%|percent)\b|\b(million|billion|thousand)s?\b|\b\d+ (out|in) (of )?\d+\b"),
    ("WARNING", r"\b(warning|danger|deadly|silent(ly)?|kill)\b"),
    ("PROMISE", r"\b(in this video|today|i'm going to|i will|you'll (learn|discover))\b"),
]


TRACK_TAG = re.compile(r"\[([a-zA-Z-]+) \| ([a-z_]+)\]")


def first_track(text):
    """Some stored transcripts concatenate several caption tracks, each prefixed
    '[lang | type]'. Keep only the first track (English in all cohort cases)."""
    tags = list(TRACK_TAG.finditer(text))
    if not tags:
        return text, 1
    end = tags[1].start() if len(tags) > 1 else len(text)
    return text[tags[0].end():end], len(tags)


def words(text):
    return re.findall(r"\S+", text)


def seg(ws, n):
    return " ".join(ws[:max(1, n)])


def hits(key, text):
    return len(LEX[key].findall(text))


def first_pos(key, ws, wps):
    t = " ".join(ws)
    m = LEX[key].search(t)
    if not m:
        return None
    idx = len(t[: m.start()].split())
    return {"word_index": idx, "approx_seconds": round(idx / wps) if wps else None,
            "approx_share_of_video": round(idx / len(ws), 3), "time_label": TIME_LABEL,
            "matched_text": m.group(0)[:80]}


def hook_type(txt):
    for name, pat in HOOK_RULES:
        if re.search(pat, txt, re.I):
            return name
    return "PLAIN_STATEMENT"


def shingles(ws, k=5):
    ws = [w.lower().strip(".,!?;:\"'()") for w in ws]
    return {" ".join(ws[i:i + k]) for i in range(0, max(0, len(ws) - k + 1))}


def main():
    con = sqlite3.connect(DB)
    txt = dict(con.execute("select youtube_video_id, transcript_text from transcripts where is_placeholder=0 and word_count>0"))
    out, shing = [], {}
    for v in FACTS["videos"]:
        vid = v["video_id"]
        rec = {k: v[k] for k in ("video_id", "channel", "title", "upload_date", "views", "channel_median_views",
                                  "outlier_multiple_vs_channel_median", "duration_seconds", "transcript_path")}
        rec["in_deep_sample_149"] = vid in SAMPLE
        t = txt.get(vid)
        if not t:
            rec["transcript_status"] = "ABSENT: " + str(v["transcript_unavailable_reason"])
            out.append(rec)
            continue
        t, n_tracks = first_track(t)
        rec["caption_tracks_in_stored_text"] = n_tracks
        ws = words(t)
        n = len(ws)
        dur = v["duration_seconds"] if isinstance(v["duration_seconds"], int) and v["duration_seconds"] > 0 else None
        wps = n / dur if dur else None
        full = " ".join(ws)
        shing[vid] = shingles(ws)
        per_k = lambda c: round(1000 * c / n, 2)
        o15, o30, o60 = (seg(ws, round(wps * s)) if wps else "UNKNOWN" for s in (15, 30, 60))
        half = n // 2
        rec.update({
            "transcript_status": "PRESENT",
            "word_count": n, "words_per_minute": round(60 * wps, 1) if wps else "UNKNOWN",
            "time_label": TIME_LABEL,
            "opening_first_15s": o15, "opening_first_30s": o30, "opening_first_60s": o60,
            "hook_archetype": hook_type(o30 if wps else seg(ws, 75)),
            "opening_30s_flags": {k: hits(k, o30) > 0 for k in ("audience_id", "authority", "credibility", "fear",
                                                                  "hope", "curiosity", "open_loop", "story")} if wps else "UNKNOWN",
            "first_authority_cue": first_pos("authority", ws, wps),
            "first_credibility_cue": first_pos("credibility", ws, wps),
            "first_open_loop": first_pos("open_loop", ws, wps),
            "first_enumerated_payoff": first_pos("enumeration", ws, wps),
            "first_cta": first_pos("cta", ws, wps),
            "first_bridge": first_pos("bridge", ws, wps),
            "counts": {k: hits(k, full) for k in LEX},
            "per_1000_words": {k: per_k(hits(k, full)) for k in ("fear", "hope", "story", "credibility", "medical_claim",
                                                                 "enumeration", "pattern_interrupt", "cure_language", "specific_study_claim")},
            "fear_escalation_ratio_2nd_half_vs_1st": round((hits("fear", " ".join(ws[half:])) + 1) / (hits("fear", " ".join(ws[:half])) + 1), 2),
            "transcript_ai_disclosure_present": hits("ai_disclosure", full) > 0,
            "information_density_numbers_per_100w": round(100 * len(re.findall(r"\b\d+(\.\d+)?\b|\b(one|two|three|four|five|six|seven|eight|nine|ten)\b", full, re.I)) / n, 2),
            "ending_last_60_words": " ".join(ws[-60:]),
            "feature_label": "TRANSCRIPT_LEXICAL_HEURISTIC",
        })
        out.append(rec)
    json.dump(out, open(HERE / "TRANSCRIPT-FORENSICS.json", "w"), indent=1)

    # --- duplicate network: every cross-video pair; keep strong signals only
    vids = [v for v in FACTS["videos"]]
    pairs = []
    for i, a in enumerate(vids):
        for b in vids[i + 1:]:
            tr = difflib.SequenceMatcher(None, a["title"].lower(), b["title"].lower()).ratio()
            sa, sb = shing.get(a["video_id"]), shing.get(b["video_id"])
            jac = len(sa & sb) / len(sa | sb) if sa and sb else None
            if tr >= 0.72 or (jac is not None and jac >= 0.08):
                hi, lo = (a, b) if a["views"] >= b["views"] else (b, a)
                pairs.append({
                    "video_a": a["video_id"], "channel_a": a["channel"], "title_a": a["title"], "date_a": a["upload_date"], "views_a": a["views"], "multiple_a": a["outlier_multiple_vs_channel_median"],
                    "video_b": b["video_id"], "channel_b": b["channel"], "title_b": b["title"], "date_b": b["upload_date"], "views_b": b["views"], "multiple_b": b["outlier_multiple_vs_channel_median"],
                    "same_channel": a["channel"] == b["channel"],
                    "title_similarity": round(tr, 3), "transcript_5gram_jaccard": round(jac, 4) if jac is not None else "UNKNOWN",
                    "days_apart": abs((__import__("datetime").date.fromisoformat(a["upload_date"]) - __import__("datetime").date.fromisoformat(b["upload_date"])).days),
                    "view_ratio_high_over_low": round(hi["views"] / max(lo["views"], 1), 1),
                    "classification": ("NEAR_IDENTICAL_SCRIPT" if (jac or 0) >= 0.5 else "SHARED_SCRIPT_MATERIAL" if (jac or 0) >= 0.08 else "TITLE_TEMPLATE_ONLY"),
                })
    pairs.sort(key=lambda p: (-(p["transcript_5gram_jaccard"] if isinstance(p["transcript_5gram_jaccard"], float) else 0), -p["title_similarity"]))
    json.dump({"method": "difflib title ratio >=0.72 OR transcript word-5-gram Jaccard >=0.08; all 306 cohort videos",
               "pairs": pairs}, open(HERE / "DUPLICATE-NETWORK.json", "w"), indent=1)
    print(len(out), "transcript records;", sum(r.get("transcript_status") == "PRESENT" for r in out), "present;",
          len(pairs), "duplicate candidates;", sum(not p["same_channel"] for p in pairs), "cross-channel")


if __name__ == "__main__":
    main()
