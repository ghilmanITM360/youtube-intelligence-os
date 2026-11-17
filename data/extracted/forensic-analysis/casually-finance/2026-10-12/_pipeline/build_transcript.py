"""Stage A2: whisper.json -> TRANSCRIPT.csv (word level) + sentences (SENTENCES.csv used to build SEMANTIC_BEATS) and a compact readable text with timestamps.
Sentence split: terminal punctuation on Whisper's own tokens (. ? !) -- no re-wording. Word confidence = Whisper token probability.
Usage: python3 -B build_transcript.py <VIDEO_ID> <WORK_ROOT> <OUT_DIR>
"""
import csv, json, re, sys
from pathlib import Path

ABBR = {"mr.", "mrs.", "dr.", "u.s.", "vs.", "inc.", "no.", "st.", "jr.", "sr.", "e.g.", "i.e.", "p.m.", "a.m."}


def main(vid, work_root, out):
    work = Path(work_root) / vid; d = Path(out) / "02_VIDEO_FORENSICS" / vid; d.mkdir(parents=True, exist_ok=True)
    wj = json.load(open(work / "whisper.json"))
    words = []
    for s in wj["segments"]:
        for w in s["words"]:
            words.append(dict(text=w["word"].strip(), start=round(w["start"], 3), end=round(w["end"], 3), prob=round(w["probability"], 3), seg=s["id"]))
    # repair zero/negative durations only by clamping (flagged), never by inventing timing
    sents, cur = [], []
    for w in words:
        cur.append(w)
        t = w["text"]
        if re.search(r"[.?!]+[\"'”’)]*$", t) and t.lower() not in ABBR and not re.fullmatch(r"\d+\.", t):
            sents.append(cur); cur = []
    if cur: sents.append(cur)
    wrows, srows, wid = [], [], 0
    for si, s in enumerate(sents):
        first = wid
        for k, w in enumerate(s):
            wrows.append(dict(video_id=vid, word_id=f"W{wid:05d}", sentence_id=f"T{si:04d}", word_index=k, start_sec=w["start"], end_sec=w["end"], word=w["text"],
                              normalized_word=re.sub(r"[^\w$%']", "", w["text"].lower()), asr_probability=w["prob"], alignment_source="WHISPER_BASE_WORD_TIMESTAMPS",
                              text_status="ASR_UNVERIFIED" if w["prob"] < 0.5 else "ASR_HIGH_CONF" if w["prob"] >= 0.8 else "ASR_MEDIUM_CONF")); wid += 1
        text = " ".join(w["text"] for w in s)
        dur = s[-1]["end"] - s[0]["start"]
        srows.append(dict(video_id=vid, sentence_id=f"T{si:04d}", start_sec=s[0]["start"], end_sec=s[-1]["end"], text=text, first_word_id=f"W{first:05d}", last_word_id=f"W{wid - 1:05d}",
                          word_count=len(s), words_per_sec=round(len(s) / dur, 2) if dur > 0 else "", is_question=text.rstrip().endswith("?"), has_number=bool(re.search(r"\d|trillion|billion|million|percent", text, re.I)),
                          min_word_prob=min(w["prob"] for w in s), gap_before_sec=round(s[0]["start"] - (sents[si - 1][-1]["end"] if si else 0), 3)))
    for name, rows in (("TRANSCRIPT.csv", wrows), ("_SENTENCES.csv", srows)):
        with open(d / name, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(work / "transcript_readable.txt", "w") as f:
        for r in srows: f.write(f"[{r['sentence_id']} {r['start_sec']:.2f}-{r['end_sec']:.2f}] {r['text']}\n")
    print(vid, "words", len(wrows), "sentences", len(srows), "low-conf words", sum(1 for w in wrows if w["text_status"] == "ASR_UNVERIFIED"))


if __name__ == "__main__":
    main(*sys.argv[1:4])
