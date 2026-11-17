"""Crops/grades the v3 stills and VIP overlays into hf/assets/ (sources are never touched).
Run: python3 prep_plates.py   (needs ffmpeg). Grades are VIP-pack LUTs baked in with lut3d."""
import os, subprocess, shutil, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(os.path.dirname(HERE), "02_assets/generated/v3")
VIP = "/Users/ghilmankhan/Downloads/VIP Assets for Video Editor"
OUT = os.path.join(HERE, "hf/assets")
TMP = os.path.join(HERE, ".lut")  # lut3d can't take paths with spaces/parens
DAWN = "eq=brightness=-0.12:saturation=0.55:gamma=0.85,colorbalance=rs=-0.2:gs=-0.05:bs=0.25:rm=-0.12:bm=0.18:rh=-0.1:bh=0.12"  # matches L1b's blue dawn
LUT = {"deep": "luts/LUTS (FREEMIUM 14)/DEEP.cube", "gold": "luts/FRESHLUTS/Golden_Years.cube"}

# name: (source, crop x,y,w,h or None, lut, lut mix 0..1, out width)
PLATES = {
    "dawn_room":   ("L1_bedroom_master_b", None, "deep", 0.55, 1920),
    "dawn_hand":   ("CH1_margaret_identity_a", (556, 503, 559, 438), "dawn", 1, 1120),
    "dawn_window": ("CH1_margaret_identity_a", (840, 0, 412, 495), "dawn", 1, 824),
    "night_hall":  ("L3_hallway_master_a", None, "deep", 0.35, 1920),
    "warm_room":   ("L1_bedroom_master_a", None, "gold", 0.8, 1920),
    "garden":      ("L5_garden_master_a", None, "gold", 0.6, 1920),
    "lily_run":    ("CH3_lily_identity_a", (1183, 0, 489, 941), "gold", 0.6, 978),
    "consult":     ("L4_consult_master_a", None, "gold", 0.35, 1920),
    "cuff":        ("CH4_clinician_hands_a", (838, 472, 834, 469), "gold", 0.35, 1252),
    "coat_door":   ("CH1W_margaret_wardrobe_a", (420, 0, 412, 941), "gold", 0.35, 824),
    "kitchen":     ("L2_kitchen_master_a", None, "gold", 0.5, 1920),
}
SKETCH = {"sk_sit": (30, 370), "sk_rise": (400, 300), "sk_dizzy": (725, 315), "sk_steady": (1060, 280), "sk_walk": (1320, 352)}
# VIP overlays -> 1920x1080 h264 (screen-blended in the edit); start, duration
OVER = {"leak_warm": ("film burns/4k film burn overlays 35mm.  FREE professional light leak overlays!.mp4", 0.0, 6.0),
        "leak_red": ("film burns/Old Film Overlay with Film Burns and Light Leaks.mp4", 9.0, 4.0)}
SFX = {"punch": ("punchole/Punch Hole 15.mp4", 0, 1.33), "glitch": ("glitch/tmp_glitch_05.mp4", 0, 3.6)}

def ff(*a): subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *a], check=True)

os.makedirs(TMP, exist_ok=True); os.makedirs(f"{OUT}/plates", exist_ok=True); os.makedirs(f"{OUT}/fx", exist_ok=True)
for k, p in LUT.items(): shutil.copy(os.path.join(VIP, p), f"{TMP}/{k}.cube")
for name, (src, crop, lut, mix, w) in PLATES.items():
    c = f"crop={crop[2]}:{crop[3]}:{crop[0]}:{crop[1]}," if crop else ""
    g = DAWN if lut == "dawn" else f"lut3d=file={TMP}/{lut}.cube"
    vf = f"{c}split[a][b];[b]{g}[g];[g][a]blend=all_mode=normal:all_opacity={mix},scale={w}:-2:flags=lanczos"
    ff("-i", f"{G}/{src}.png", "-filter_complex", vf, "-q:v", "2", f"{OUT}/plates/{name}.jpg")
for name, (x, w) in SKETCH.items():
    ff("-i", f"{G}/CH1NB_margaret_sketch_a.png", "-vf", f"crop={w}:800:{x}:70", f"{OUT}/plates/{name}.png")
for name, (src, ss, d) in OVER.items():
    ff("-ss", str(ss), "-t", str(d), "-i", os.path.join(VIP, src), "-an", "-vf", "scale=1920:1080,setsar=1,fps=30",
       "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", f"{OUT}/fx/{name}.mp4")
for name, (src, ss, d) in SFX.items():
    ff("-ss", str(ss), "-t", str(d), "-i", os.path.join(VIP, src), "-vn", "-ac", "2", "-ar", "48000", f"{OUT}/sfx/{name}.wav")
shutil.rmtree(TMP)
for f in sorted(os.listdir(G)):  # originals stay untouched: print their hashes for the record
    if f.endswith(".png"): print(hashlib.sha256(open(os.path.join(G, f), "rb").read()).hexdigest()[:16], f)
print("ok:", len(PLATES), "plates,", len(SKETCH), "sketches,", len(OVER), "overlays,", len(SFX), "sfx")
