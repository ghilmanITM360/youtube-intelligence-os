"""Merge manual LIVE_WEB_VISUAL thumbnail observations (thumbnail_obs_raw.jsonl,
coded 2026-09-25 from i.ytimg.com images rendered in a browser contact sheet)
with verified video facts; derive title duplication / complement and feature
performance using the within-channel outlier multiple (views / channel median),
so channel size does not masquerade as a thumbnail effect.

Output: forensic-v2/THUMBNAIL-MATRIX.json
"""
import json, re, statistics as st
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SP_ORDER = json.load(open(HERE / "thumbnail_order.json"))
FACTS = {v["video_id"]: v for v in json.load(open(HERE / "VERIFIED-FACTS.json"))["videos"]}
OBS = [json.loads(l) for l in open(HERE / "thumbnail_obs_raw.jsonl")]
STOP = set("the a an to of in on is are you your this that for and or it be at do with my i".split())


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP}


def yes(v):
    return str(v).upper().startswith("Y")


def main():
    order = {o["idx"]: o for o in SP_ORDER}
    rows = []
    for o in OBS:
        meta = order[o["idx"]]
        v = FACTS[meta["video_id"]]
        txt = "" if o["txt"].startswith("(") else o["txt"]
        tw, tt = toks(txt), toks(v["title"])
        overlap = len(tw & tt) / len(tw) if tw else 0
        rows.append({
            "video_id": v["video_id"], "channel": v["channel"], "title": v["title"], "views": v["views"],
            "outlier_multiple": v["outlier_multiple_vs_channel_median"], "upload_date": v["upload_date"],
            "thumbnail_url_observed": meta["thumb"], "thumbnail_url_source": meta["thumb_source"],
            "evidence_label": "LIVE_WEB_VISUAL", "observed_on": "2026-09-25",
            "face": o["f"], "doctor_persona_cues": o["doc"] or "NONE", "senior_shown": o["sr"], "gender": o["g"] or "N/A",
            "expression": o["ex"] or "N/A", "eye_contact": o["eye"], "white_coat_or_scrubs": "Y" if re.search(r"scrubs|coat|surgical", o["doc"]) else "N",
            "body_part": o["bp"] or "NONE", "food": o["food"] or "NONE", "medicine": o["med"] or "NONE",
            "medical_illustration": o["ill"], "exact_thumbnail_text": o["txt"],
            "text_word_count": len(re.findall(r"[A-Za-z0-9%#']+", txt)),
            "large_number": o["n"], "arrow": o["arr"], "circle": o["cir"], "warning_icon": o["warn"],
            "dominant_visual_elements": o["dom"], "contrast": o["con"], "focal_point": o["foc"],
            "background_complexity": o["bg"], "before_after": o["ba"], "fear": o["fear"], "hope": o["hope"],
            "authority": o["auth"], "curiosity": o["cur"], "answer_revealed_or_withheld": o["ans"],
            "title_word_overlap_share": round(overlap, 2),
            "title_relationship": "NO_TEXT" if not tw else "DUPLICATES_TITLE" if overlap >= 0.7 else "PARTIAL_OVERLAP" if overlap >= 0.3 else "COMPLEMENTS_TITLE",
            "analyst_note": o.get("note", ""),
        })

    def perf(pred, label):
        a = [r["outlier_multiple"] for r in rows if pred(r)]
        b = [r["outlier_multiple"] for r in rows if not pred(r)]
        return {"feature": label, "n_with": len(a), "median_multiple_with": round(st.median(a), 3) if a else None,
                "n_without": len(b), "median_multiple_without": round(st.median(b), 3) if b else None,
                "hit_rate_with_ge3x": round(sum(x >= 3 for x in a) / len(a), 3) if a else None,
                "hit_rate_without_ge3x": round(sum(x >= 3 for x in b) / len(b), 3) if b else None}

    feats = [
        (lambda r: r["face"].startswith("Y") and "illustrat" not in r["face"] and "render" not in r["face"] and "partial" not in r["face"], "real/photoreal face prominent"),
        (lambda r: "illustrat" in r["face"] or "sketch" in r["medical_illustration"], "illustrated/sketch human"),
        (lambda r: r["doctor_persona_cues"] != "NONE", "doctor persona cues"),
        (lambda r: r["food"] != "NONE", "food shown"),
        (lambda r: r["medicine"] != "NONE", "medicine shown"),
        (lambda r: r["body_part"] != "NONE", "body part shown"),
        (lambda r: yes(r["medical_illustration"]), "medical illustration / render"),
        (lambda r: yes(r["large_number"]), "large number"),
        (lambda r: yes(r["arrow"]) or "finger" in r["arrow"], "arrow or pointing"),
        (lambda r: yes(r["circle"]), "circle highlight"),
        (lambda r: yes(r["warning_icon"]), "warning icon"),
        (lambda r: yes(r["before_after"]), "before/after"),
        (lambda r: r["background_complexity"] == "H", "high background complexity (clutter)"),
        (lambda r: r["fear"].startswith("Y"), "fear framing"),
        (lambda r: "extreme" in r["fear"], "extreme fear (death/die/killing)"),
        (lambda r: r["hope"].startswith("Y"), "hope framing"),
        (lambda r: r["answer_revealed_or_withheld"].startswith("REVEALED"), "answer revealed in thumbnail"),
        (lambda r: r["answer_revealed_or_withheld"] == "WITHHELD", "answer withheld"),
        (lambda r: r["title_relationship"] == "DUPLICATES_TITLE", "text duplicates title"),
        (lambda r: r["title_relationship"] in ("COMPLEMENTS_TITLE", "NO_TEXT"), "text complements title / no text"),
        (lambda r: 0 < r["text_word_count"] <= 8, "<=8 words of text"),
        (lambda r: r["text_word_count"] > 15, ">15 words of text"),
    ]
    by_channel = {}
    for ch in sorted({r["channel"] for r in rows}):
        sub = [r for r in rows if r["channel"] == ch]
        by_channel[ch] = {"n": len(sub),
                          "dominant_template": max({r["dominant_visual_elements"] for r in sub}, key=lambda d: sum(r["dominant_visual_elements"] == d for r in sub)),
                          "share_doctor_persona": round(sum(r["doctor_persona_cues"] != "NONE" for r in sub) / len(sub), 2),
                          "share_illustrated": round(sum("illustrat" in r["face"] or "sketch" in r["medical_illustration"] for r in sub) / len(sub), 2),
                          "median_text_words": st.median(r["text_word_count"] for r in sub)}
    json.dump({"evidence_label": "LIVE_WEB_VISUAL", "observed_on": "2026-09-25",
               "method": "Each thumbnail rendered from its i.ytimg.com URL in a local contact sheet in the in-app browser and hand-coded; feature performance uses within-channel outlier multiple; cross-channel pooling means features correlated with channel template are confounded (see by_channel).",
               "rows": rows, "feature_performance": [perf(p, l) for p, l in feats], "by_channel": by_channel},
              open(HERE / "THUMBNAIL-MATRIX.json", "w"), indent=1)
    for f in [perf(p, l) for p, l in feats]:
        print(f)
    for k, v in by_channel.items():
        print(k, v)


if __name__ == "__main__":
    main()
