"""Compact authoring helpers (import from a per-video author_review.py).
Usage in author_review.py:
  import sys; sys.path.insert(0,'scripts'); from author_lib import *
  A=Author('VIDEO_ID', frames_total, evidence_root)
  A.scenes([(f0,"label","layers","asset,ids","purpose"), ...], start_nocut=True)   # f1 of each scene = next f0; last ends at frames_total
  A.event("S03",f0,f1,"OP","target","description",conf="MEDIUM")
  A.write(headline=None)   # also snaps scene starts (+-15 frames) to large stage changes, clamps events, writes assets from scene asset lists
"""
import json, os
import numpy as np

FAM = {"CH": "CHARACTER_STICK_FIGURE", "PR": "PROP_FINANCIAL", "SS": "SOURCE_SCREENSHOT", "TY": "TYPOGRAPHY_EMPHASIS", "OV": "OVERLAY_ANNOTATION", "LOGO": "SOURCE_LOGO", "PHOTO": "SOURCE_PHOTO", "FX": "FX_OVERLAY_CLIP"}
OVER = {"CH_USMAP": "CHARACTER_COUNTRY_MAP", "CH_UKMAP": "CHARACTER_COUNTRY_MAP", "CH_NLMAP": "CHARACTER_COUNTRY_MAP", "CH_MAPS": "CHARACTER_COUNTRY_MAP", "CH_JAPAN": "CHARACTER_COUNTRY_MAP", "CH_EARTH": "CHARACTER_PLANET", "PR_DEBTDOC": "PROP_FINANCIAL_PAPER", "PR_BOND": "PROP_FINANCIAL_PAPER",
        "PR_MORTGAGE": "PROP_FINANCIAL_PAPER", "PR_DOC": "PROP_FINANCIAL_PAPER", "PR_PAPER": "PROP_FINANCIAL_PAPER", "PR_CHECK": "PROP_FINANCIAL_PAPER", "PR_BILLS": "PROP_MONEY", "PR_BAG": "PROP_MONEY", "PR_BAGS": "PROP_MONEY",
        "PR_CASH": "PROP_MONEY", "PR_DOLLAR": "PROP_MONEY", "PR_HOUSE": "PROP_HOUSING", "PR_BLDG": "PROP_HOUSING", "PR_SERVER": "PROP_DEVICE", "PR_CLOCK": "PROP_DEVICE", "PR_CALENDAR": "PROP_DEVICE", "PR_CHIP": "PROP_DEVICE",
        "PR_QCIRCLE": "PROP_OBJECT", "PR_DESK": "PROP_FURNITURE", "PR_NOTES": "PROP_OBJECT", "CH_DEBTMAN": "CHARACTER_PROP_WITH_LIMBS", "PR_BLACKBOARD": "PROP_OBJECT", "PR_BUBBLE": "PROP_OBJECT", "TY_HEADER": "TYPOGRAPHY_PERSISTENT", "TY_TITLE": "TYPOGRAPHY_PERSISTENT", "TY_CAPTION": "TYPOGRAPHY_CAPTION"}


class Author:
    def __init__(self, vid, n, ev_root="/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence"):
        self.v, self.n, self.ev = vid, n, ev_root
        self.S, self.E = [], []
        self.rd = "videos/%s/" % vid
        os.makedirs(self.rd + "review", exist_ok=True)
        g = np.load("%s/%s/gray.npy" % (ev_root, vid)).astype(np.int16)
        b = json.load(open(self.rd + "auto/bands.json"))
        h = g.shape[1]
        a0, a1 = int(b["stage"][0] * h), int(b["stage"][1] * h)
        self._px = lambda i: int((np.abs(g[i, a0:a1] - g[i - 1, a0:a1]) > 16).sum()) if 0 < i < len(g) else 0

    def scenes(self, rows, start_nocut=True):
        B = [r[0] for r in rows] + [self.n]
        for k in range(1, len(rows)):
            if self._px(B[k]) < 1000:
                lo, hi = B[k - 1] + 1, B[k + 1] - 1
                c = max(range(max(B[k] - 15, lo), min(B[k] + 16, hi)), key=self._px)
                if self._px(c) >= 1000:
                    B[k] = c
        for k, (f0, lab, lay, ass, pur) in enumerate(rows):
            d = dict(id="S%02d" % (k + 1), f0=B[k], f1=B[k + 1], label=lab, layers=lay, assets=ass, transition_in="START" if k == 0 else "HARD_CUT",
                     purpose=pur + " [ART_DIRECTION_INFERENCE]", notes="")
            if (k == 0 and start_nocut) or (k > 0 and self._px(B[k]) < 1000):
                d["no_auto_cut"] = True
            self.S.append(d)

    def event(self, scene, f0, f1, op, target, desc, ref="", conf="MEDIUM", label="DIRECTLY_OBSERVED", mclass="CONV", geo="", amb=""):
        self.E.append(dict(id="x", scene=scene, f0=f0, f1=f1, op=op, target=target, desc=desc, mclass=mclass, geometry=geo, easing="not measured", measure="",
                           evidence=ref, label=label, confidence=conf, ambiguity=amb, trigger="", after=""))

    def write(self, headline=None):
        sc = {s["id"]: s for s in self.S}
        for e in self.E:
            s = sc[e["scene"]]
            e["f0"] = max(e["f0"], s["f0"])
            e["f1"] = min(e["f1"], s["f1"] - 1)
            if e["f1"] < e["f0"]:
                e["f1"] = e["f0"]
        A = []
        for s in self.S:
            for aid in [a for a in s["assets"].split(",") if a]:
                A.append(dict(asset_id=aid, family=OVER.get(aid, FAM.get(aid.split("_")[0], "PROP_OBJECT")), variant=s["label"][:60], scene=s["id"], f0=s["f0"], f1=s["f1"], role="", desc=""))
        if headline:
            A.append(dict(asset_id="TY_HEADER", family="TYPOGRAPHY_PERSISTENT", variant=headline, scene="S01", f0=0, f1=self.n, role="headline", desc=""))
        A.append(dict(asset_id="TY_CAPTION", family="TYPOGRAPHY_CAPTION", variant="hand-lettered/small caption", scene="S01", f0=0, f1=self.n, role="captions", desc=""))
        json.dump(self.S, open(self.rd + "review/scenes.json", "w"), indent=1)
        self.E.sort(key=lambda e: e["f0"])
        json.dump(self.E, open(self.rd + "review/events.json", "w"), indent=1)
        json.dump(A, open(self.rd + "review/assets.json", "w"), indent=1)
        print(len(self.S), "scenes", len(self.E), "events", len(A), "assets; ends", self.S[-1]["f1"])
