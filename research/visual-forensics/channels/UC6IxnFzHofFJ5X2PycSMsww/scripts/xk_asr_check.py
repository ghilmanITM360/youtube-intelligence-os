"""Word agreement between provisional ASR and catalog plaintext captions (DS-000017). Text agreement only; no timing, not listening.
Usage: python3 -I xk_asr_check.py <video_dir>"""
import json, re, sys, pathlib, difflib
V = pathlib.Path(sys.argv[1]).resolve(); vid = V.name
T = pathlib.Path("/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/raw/competitors/DS-000017/apify/mzl5dCHF81LbcBamS/transcripts") / f"{vid}.txt"
norm = lambda s: re.findall(r"[a-z0-9]+", s.lower().replace("’", "'"))
a = norm(" ".join(s["text"] for s in json.load(open(V / "asr/asr_small_en.json"))["segments"]))
out = dict(video_id=vid, catalog_caption=str(T), catalog_available=T.exists(), asr_words=len(a))
if T.exists():
    c = norm(T.read_text()); sm = difflib.SequenceMatcher(None, a, c, autojunk=False)
    out.update(caption_words=len(c), matched_words=sum(b.size for b in sm.get_matching_blocks()), ratio=round(sm.ratio(), 4),
               note="SequenceMatcher on normalised word lists; numerals vs spelled numbers count as mismatches")
(V / "asr/asr_vs_catalog_caption.json").write_text(json.dumps(out, indent=1)); print(out)
