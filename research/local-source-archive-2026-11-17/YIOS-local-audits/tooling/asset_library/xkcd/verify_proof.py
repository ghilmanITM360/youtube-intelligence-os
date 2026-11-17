#!/usr/bin/env python3
"""Verify the silent proof against the brief (DEEP_VF_ADDENDUM_v1 §9) per layout: pre-encode frames (preencode_<l>.json)
and the exported MP4 (ffprobe + full decode). Native-colour red check: the red-circle pop is measured on HSV red pixels in the
circle ROI, and the greyscale (luma) diff of the same frame is reported alongside, to show why grey detectors miss it.
usage: <venv python> -I verify_proof.py <proof_dir>   -> <proof_dir>/VERIFY.json"""
import json, subprocess, sys
import numpy as np, cv2
P = sys.argv[1]; T = json.load(open(f"{P}/timeline_v1.json")); EV = {e["target"]: e for e in T["events"]}; N = T["frames"]
out = {}
for name, L in T["layouts"].items():
    W, Hh = L["size"]; pre = json.load(open(f"{P}/preencode_{name}.json")); d = pre["changed_px_per_frame"]; red = pre["red_px_per_frame"]
    typ = set(range(EV["card_text"]["f"], EV["card_text"]["f"] + len(T["question"]))) if L["card"] else set()
    pops = [EV[k]["f"] for k in ("moon", "moon_label", "red_circle", "scene_night", "scene_label_1", "scene_label_2")]
    dz = EV["glow_plate"]; dis = set(range(dz["f"], dz["f"] + dz["frames"]))
    holds = [f for f in range(1, N) if f not in typ | dis | set(pops)]
    r = {}
    r["P1_pops_one_frame_PRE"] = all(d[f] > 0 and (f + 1 >= N or f + 1 in typ | dis | set(pops) or d[f + 1] == 0) for f in pops)
    r["P6_holds_dead_still_PRE"] = dict(pass_=all(d[f] == 0 for f in holds), hold_frames=len(holds), nonzero=[f for f in holds if d[f]])
    r["P5_red_only_emphasis_PRE"] = dict(pass_=all(red[f] == 0 for f in range(N) if not (EV["red_circle"]["f"] <= f < EV["scene_night"]["f"])) and min(red[EV["red_circle"]["f"]:EV["scene_night"]["f"]]) > 0,
                                        red_px_before=max(red[:EV["red_circle"]["f"]]), red_px_during=red[EV["red_circle"]["f"]], red_px_after=max(red[EV["scene_night"]["f"]:]))
    r["layout_check_PRE"] = {f: v["defects"] for f, v in pre["layout_check"].items()}
    # exported file
    mp4 = f"{P}/proof_{name}.mp4"
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,avg_frame_rate,nb_read_frames,codec_name,pix_fmt:format=duration", "-of", "json", mp4], capture_output=True, text=True, check=True).stdout)
    st = pr["streams"][0]; dec = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-f", "null", "-"], capture_output=True, text=True)
    r["P7_probe_decode"] = dict(pass_=st["r_frame_rate"] == "24/1" and st["avg_frame_rate"] == "24/1" and int(st["nb_read_frames"]) == N and abs(float(pr["format"]["duration"]) - N / 24) < 0.05 and dec.stderr.strip() == "" and (st["width"], st["height"]) == (W, Hh),
                                **{k: st[k] for k in ("codec_name", "pix_fmt", "width", "height", "r_frame_rate", "avg_frame_rate", "nb_read_frames")}, duration=pr["format"]["duration"], decode_errors=dec.stderr.strip())
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True, check=True).stdout
    F = np.frombuffer(raw, np.uint8).reshape(-1, Hh, W, 3).astype(np.int16)
    mad = [0.0] + [float(np.abs(F[i] - F[i - 1]).mean()) for i in range(1, len(F))]
    r["P6_holds_POST"] = dict(pass_=max(mad[f] for f in holds) < 0.5, max_hold_mad=round(max(mad[f] for f in holds), 4))
    r["P1_pops_POST"] = {f: dict(mad_at=round(mad[f], 3), mad_next=round(mad[f + 1], 4) if f + 1 < N else None) for f in pops}
    r["P1_pops_POST"]["pass_"] = all(mad[f] > 5 * max(mad[f + 1] if f + 1 < N and f + 1 not in typ | dis | set(pops) else 0, 0.02) for f in pops)
    a, b = F[dz["f"] - 1], F[max(dis)]; den = np.abs(b - a).mean()
    prog = [round(float(np.abs(F[f] - a).mean() / den), 3) for f in sorted(dis)]; steps = np.diff([0] + prog)
    r["P2_dissolve_linear_POST"] = dict(pass_=bool(all(abs(s - 1 / 6) <= 0.04 for s in steps)), progress=prog, steps=[round(float(s), 3) for s in steps])
    r["P3_no_overshoot_POST"] = dict(pass_=max(float(np.abs(F[f] - a).mean() / den) for f in range(dz["f"], N)) <= 1.03)
    # P4 canvas + stroke on decoded frame before first pop
    fr = F[EV["moon"]["f"] - 1].astype(np.uint8); vals, cnt = np.unique(fr.reshape(-1, 3), axis=0, return_counts=True); modal = vals[cnt.argmax()][::-1]
    s = min(W, Hh) / 1000; bx0, by0, bx1, by1 = [int(round(v * s)) for v in L["board"]]; row = fr[(by0 + by1) // 2, max(0, bx0 - 20):bx0 + 20].mean(1)
    stroke = int((row < 128).sum())
    r["P4_canvas_stroke_POST"] = dict(pass_=bool(all(abs(int(c) - 0xF8) <= 2 for c in modal) and 7 <= stroke <= 9), modal_rgb="#%02X%02X%02X" % tuple(modal), stroke_px=stroke)
    # native-colour red-circle check vs greyscale
    cx, cy, cr = [v * s for v in L["circle"]]; m = int(cr + 12); y0, y1, x0, x1 = int(cy - m), int(cy + m), int(cx - m), int(cx + m)
    def redcount(f):
        hsv = cv2.cvtColor(F[f, y0:y1, x0:x1].astype(np.uint8), cv2.COLOR_BGR2HSV); h, sat, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
        return int((((h <= 8) | (h >= 172)) & (sat > 90) & (v > 90)).sum())
    fpop = EV["red_circle"]["f"]; grey = lambda f: cv2.cvtColor(F[f].astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(int)
    gdiff = float(np.abs(grey(fpop) - grey(fpop - 1)).mean()); gfrac = float((np.abs(grey(fpop) - grey(fpop - 1)) >= 12).mean())
    rc = [redcount(f) for f in (fpop - 2, fpop - 1, fpop, fpop + 1, fpop + 2)]
    r["RED_CIRCLE_NATIVE_COLOUR_POST"] = dict(pass_=rc[0] == rc[1] == 0 and rc[2] > 200 and abs(rc[3] - rc[2]) <= 0.05 * rc[2], red_px_roi_fm2_to_fp2=rc,
                                             grey_mean_absdiff_at_pop=round(gdiff, 4), grey_changed_frac_ge12=round(gfrac, 5),
                                             note="the pop is 1 frame in native colour; its whole-frame luma change is tiny, which is why grey-only detectors miss it")
    r["P8_human_keyframe_and_playback_review"] = "PENDING_HUMAN (model viewed keyframe sheets of attempt 1 (3 defects) and attempt 2 (none seen); no real-time playback capability in this session)"
    r["P9_humancraft_scorecard"] = "PENDING_HUMAN (not self-scored)"
    r["AUDIO_SYNC_AND_FINAL_AV"] = "BLOCKED/PENDING (silent proof; no narration exists)"
    out[name] = r
json.dump(out, open(f"{P}/VERIFY.json", "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
for n, r in out.items():
    print(n, {k: (v.get("pass_") if isinstance(v, dict) and "pass_" in v else v) for k, v in r.items() if k != "P1_pops_POST"}, "P1_POST", r["P1_pops_POST"]["pass_"])
