# Captions: wording = supplied script; timing = faster-whisper word starts on the real MP3 (tools/words.json).
# One source feeds both the SRT and the on-screen caption layer (src/captions.json).
# Each chunk = (text, ASR tokens consumed). {r:..} {g:..} {a:..} {b:..} mark the ONE highlighted keyword (colour).
# Script/ASR wording differences are listed in FINAL_QA.md; nothing here alters the recorded voice.
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNKS = [
    ("{r:Calf pain} that starts with walking", 6), ("and {g:eases} with rest", 4),
    ("is a pattern doctors {r:don't ignore.}", 6), ("Let's see what Dr. Rahim says.", 6),
    ("Calf pain or {r:cramping} while walking,", 6), ("this is called {a:claudication}", 4),
    ("or {a:intermittent claudication.}", 3), ("It happens when {r:narrowing arteries}", 5),
    ("reduce {r:blood flow} to the leg muscles", 7), ("during {a:activity.}", 2),
    ("The muscles essentially run {b:low on oxygen.}", 7), ("The pain usually {g:eases} with rest", 6),
    ("and then {r:returns} with walking again.", 6), ("This pattern is a known {a:early signal}", 7),
    ("of {r:peripheral arterial disease,}", 4), ("which is {a:directly connected}", 4),
    ("to the {r:cardiovascular risk.}", 4), ("The signal doctors {a:watch} the most", 7),
    ("is {a:claudication,}", 2), ("that is, {r:calf pain}", 4),
    ("that appears during {r:activity} or walking", 6), ("and {g:disappears with rest.}", 4),
    ("It is considered one of the most", 7), ("{a:clinically significant} early signals.", 4),
    ("But if this {a:intermittent claudication}", 5), ("converts into {r:continuous pain,}", 4),
    ("{r:even at rest,}", 3), ("this occurs in patients who have got", 7),
    ("critical [limb] ischemia,", 2), ("which is a {r:serious} state of affairs", 7),
    ("for {a:peripheral vascular disease.}", 4), ("It suggests that {r:arterial blood flow}", 6),
    ("is {r:already reduced} enough", 4), ("to affect {r:muscle function,}", 4),
    ("and research {a:consistently} shows", 4), ("that people with {a:claudication}", 4),
    ("have {r:elevated cardiovascular risk.}", 4), ("That is why doctors", 4),
    ("{r:don't dismiss} leg pain during walking.", 6), ("They {a:always,}", 2),
    ("{r:always investigate.}", 2),
]
END = 60.58
COL = {"r": "warning", "g": "relief", "a": "caution", "b": "oxygen"}

words = json.load(open(os.path.join(HERE, "words.json")))
assert sum(n for _, n in CHUNKS) == len(words), "token count drifted from words.json"
cues, i = [], 0
for text, n in CHUNKS:
    toks = words[i:i + n]
    i += n
    out = []
    for part in re.split(r"(\{[rgab]:[^}]*\})", text):
        m = re.fullmatch(r"\{([rgab]):([^}]*)\}", part)
        for w in (m.group(2) if m else part).split():
            out.append({"w": w, "hl": COL[m.group(1)] if m else None})
    # highlighted words light up when spoken: map words proportionally onto the ASR tokens
    for j, o in enumerate(out):
        o["s"] = toks[min(len(toks) - 1, round(j * len(toks) / len(out)))]["s"]
    cues.append({"s": toks[0]["s"], "words": out})
for j, c in enumerate(cues):
    c["e"] = cues[j + 1]["s"] if j + 1 < len(cues) else END
    assert c["e"] > c["s"]
plain = lambda c: " ".join(o["w"] for o in c["words"])
ts = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(round(s * 1000)) % 1000:03d}"
open(sys.argv[1], "w").write("\n".join(f"{k + 1}\n{ts(c['s'])} --> {ts(c['e'])}\n{plain(c)}\n" for k, c in enumerate(cues)))
json.dump(cues, open(os.path.join(HERE, "..", "src", "captions.json"), "w"), indent=0)
print(len(cues), "cues; max words", max(len(c["words"]) for c in cues), "; max chars", max(len(plain(c)) for c in cues))
