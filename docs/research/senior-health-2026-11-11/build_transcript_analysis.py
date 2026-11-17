"""Report 2 Phase 2.5: dataset-wide transcript structure features (read-only on sources).
Run from repo root: python3 -I docs/research/senior-health-2026-11-11/build_transcript_analysis.py
Needs 02-benchmark-video-table.csv (build_benchmark.py). Heuristic regex counts = OBSERVED text features; they say nothing about retention.
"""
import csv, json, re, sqlite3, statistics as st, collections
csv.field_size_limit(10**9)
D = "docs/research/senior-health-2026-11-11"
E = "data/extracted/channel-data/senior-health-16-acquisition"
bm = {r["video_id"]: r for r in csv.DictReader(open(f"{D}/02-benchmark-video-table.csv"))}
tx = {}
for l in open(f"{E}/TRANSCRIPTS_ALL.jsonl"):
    r = json.loads(l); tx[r["video_id"]] = r["text"]
db = sqlite3.connect("file:data/catalog/youtube_channel_registry.db?mode=ro", uri=True)
for vid, t in db.execute("select youtube_video_id, transcript_text from transcripts where is_placeholder=0"):
    if vid in bm and vid not in tx and t: tx[vid] = t
clean = lambda t: re.sub(r"\[[^\]]*\]", " ", t)
W = lambda t: re.findall(r"[A-Za-z0-9'’%.-]+", t.lower())

F = {
 "q_open": r"^[^.!]{0,140}\?", "you_open": r"^(if you|when you|do you|have you|are you|did you|you |your |imagine)", "story_open": r"^(on a|one |last |it was|[A-Z][a-z]+,? \d{2}\b)|\b(he|she) (was|had|said)\b",
 "warn_open": r"(warn|danger|deadly|mistake|never|stop |risk|kill|silent|hidden)", "stat_open": r"\d+ ?(%|percent|million|out of|in \d)|one in (four|three|five|two)",
 "doctor_claim": r"(i'?m a|i am a|as a|as an|in my \d+ years|my patients|in my practice|i'?ve (seen|treated))", "no_clickbait_promise": r"(by the end|stay (till|until|to) the end|watch (till|until) the end|before we (start|begin|continue)|but first|number \d.{0,20}(surprise|shock))",
}
OPEN_N = 90  # first ~90 words ≈ first 30-40 s at ~150-170 wpm (timestamps unavailable)
REHOOK = r"(stay with me|but wait|here'?s the (twist|catch|part)|the (surprising|shocking|scary|crazy) part|but here'?s|now here'?s|and this is where|coming up|in a moment|later in this video|before i tell you|you won'?t believe|number \d+ will|the last one|the most important one)"
CTA = r"(subscribe|like (this|the) video|hit the (like|bell)|comment below|leave a comment|drop a comment|let me know in the comments|share this|notification|bell icon|link (below|in the description)|free (guide|pdf|ebook)|join (our|my))"
SRC = r"(study|studies|research(ers)?|journal|trial|published in|according to|harvard|mayo clinic|cdc|nih|who |american heart|meta-analysis|randomized|peer[- ]reviewed|\bjama\b|\bnejm\b|lancet|cochrane|guidelines?)"
HEDGE = r"(consult (your|a) (doctor|physician|healthcare)|talk to your (doctor|physician)|not (a substitute|medical advice)|educational (purposes|only)|check with your (doctor|pharmacist)|disclaimer|speak (to|with) your (doctor|physician))"
ABS = r"(guarantee|100%|cure[sd]? |reverse[sd]? (your|diabetes|aging|dementia)|miracle|instantly|never fails|detox|flush(es|ing)? (out|your)|toxins?)"
PERSONAL = r"\b(i|my|me)\b"
rows = []
for vid, t in tx.items():
    if vid not in bm: continue
    b = bm[vid]
    if b["is_short"] == "1" or b["mult"] == "": continue
    ct = clean(t); words = W(ct)
    if len(words) < 300: continue
    head = " ".join(ct.split()[:OPEN_N]); hl = head.lower(); tl = ct.lower()
    n = len(words)
    tri = collections.Counter(zip(words, words[1:], words[2:]))
    rep = sum(c for c in tri.values() if c > 1) / max(sum(tri.values()), 1)
    kw = {k: int(bool(re.search(p, head if k != "story_open" else head.strip(), re.I if k != "story_open" else 0))) for k, p in F.items()}
    segs = [tl[int(n_ * len(tl) / 10):int((n_ + 1) * len(tl) / 10)] for n_ in range(10)]
    rows.append(dict(
        video_id=vid, channel=b["channel"], mult=float(b["mult"]), tier=b["tier"], immature=int(b["immature"]), views=int(b["views"]), words=n, **kw,
        head_but=int(bool(re.search(r"\b(but|however|yet|except)\b", hl))), head_words_to_topic=None,
        rehooks_per1k=round(1000 * len(re.findall(REHOOK, tl)) / n, 2), cta_n=len(re.findall(CTA, tl)), cta_in_first10pct=int(bool(re.search(CTA, segs[0]))),
        cta_in_last10pct=int(bool(re.search(CTA, segs[9]))), src_per1k=round(1000 * len(re.findall(SRC, tl)) / n, 2), hedge=int(bool(re.search(HEDGE, tl))),
        abs_n=len(re.findall(ABS, tl)), first_person_pct=round(100 * len(re.findall(PERSONAL, tl)) / n, 2),
        you_pct=round(100 * len(re.findall(r"\byou(r|rs)?\b", tl)) / n, 2), rep=round(rep, 3), wpm_proxy=None,
        numbered_items=len(set(re.findall(r"\b(?:number|tip|habit|mistake|sign|food|reason|fact|step)? ?(?:#|number )?([1-9]|10)[.:]? ", tl[:0]))),
        list_markers=len(re.findall(r"\b(number (one|two|three|four|five|six|seven|eight|nine|ten)|first,|second,|third,|fourth,|fifth,|next,|finally,|last,)", tl)),
        head=head[:260]))
json.dump(rows, open(f"{D}/02-transcript-structure-rows.json", "w"))
med = lambda xs: round(st.median(xs), 2) if xs else 0
mean = lambda xs: round(st.mean(xs), 2) if xs else 0
mature = [r for r in rows if not r["immature"]]
groups = {"OUTLIER_5X+ (mult>=5)": [r for r in mature if r["mult"] >= 5], "ABOVE_2X": [r for r in mature if 2 <= r["mult"] < 5],
          "BASELINE": [r for r in mature if 0.5 <= r["mult"] < 2], "BELOW_HALF": [r for r in mature if r["mult"] < 0.5]}
P = print
P("n transcripts analysed (long-form, >=300 words, mature):", len(mature), "| all:", len(rows))
cols = ["q_open", "you_open", "story_open", "warn_open", "stat_open", "doctor_claim", "no_clickbait_promise", "head_but", "hedge", "cta_in_first10pct", "cta_in_last10pct"]
P("\n== binary opening/structure features: % of videos in group ==")
P("feature | " + " | ".join(f"{g} (n={len(v)})" for g, v in groups.items()) + " | ALL")
for c in cols: P(c, "|", " | ".join(str(round(100 * mean([r[c] for r in v]))) if v else "-" for v in groups.values()), "|", round(100 * mean([r[c] for r in mature])))
nums = ["words", "rehooks_per1k", "cta_n", "src_per1k", "abs_n", "first_person_pct", "you_pct", "rep", "list_markers"]
P("\n== numeric features: group median ==")
P("feature | " + " | ".join(groups) + " | ALL")
for c in nums: P(c, "|", " | ".join(str(med([r[c] for r in v])) for v in groups.values()), "|", med([r[c] for r in mature]))
# by channel-tier (view level) rather than within-channel multiple
P("\n== top-quartile-channels vs bottom: structure ==")
chmed = collections.defaultdict(list)
for r in mature: chmed[r["channel"]].append(r["views"])
cm = {c: st.median(v) for c, v in chmed.items()}
hi = [r for r in mature if cm[r["channel"]] >= 10000]; lo = [r for r in mature if cm[r["channel"]] < 500]
for nm, v in (("channel_median>=10k", hi), ("channel_median<500", lo)):
    P(nm, "n", len(v), "|", {c: round(100 * mean([r[c] for r in v])) for c in cols[:8]}, "| med words", med([r["words"] for r in v]), "| rehooks", med([r["rehooks_per1k"] for r in v]), "| src", med([r["src_per1k"] for r in v]), "| cta", med([r["cta_n"] for r in v]))
P("\n== per-channel structure ==")
P("channel | n | q_open% | you_open% | story_open% | stat_open% | doctor_claim% | hedge% | src/1k | rehook/1k | cta | rep | abs_n")
by = collections.defaultdict(list)
for r in rows: by[r["channel"]].append(r)
for c, v in sorted(by.items(), key=lambda x: -cm.get(x[0], 0)):
    P(c, "|", len(v), "|", " | ".join(str(round(100 * mean([r[k] for r in v]))) for k in ("q_open", "you_open", "story_open", "stat_open", "doctor_claim", "hedge")), "|", med([r["src_per1k"] for r in v]), "|", med([r["rehooks_per1k"] for r in v]), "|", med([r["cta_n"] for r in v]), "|", med([r["rep"] for r in v]), "|", med([r["abs_n"] for r in v]))
P("\n== sample openings of top outliers (first ~40 words) ==")
for r in sorted([r for r in mature if r["mult"] >= 5 and r["views"] >= 100000], key=lambda r: -r["views"])[:14]:
    P(f'{r["views"]} x{r["mult"]:.0f} {r["channel"]} {r["video_id"]}: {" ".join(r["head"].split()[:42])}')
