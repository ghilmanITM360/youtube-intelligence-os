"""Generate the brand SVGs (logo, banner, watermark, sample thumbnail) from one palette.
Run: python3 make_brand_assets.py && sh render.sh   (render.sh rasterises with headless Chrome)
All numbers on the art are verified in ../06_SCIENCE_VERIFICATION.md.
"""
import math

INK, PAPER, SIGNAL = "#10182B", "#F3EEE3", "#FF8A1F"
SIM, DATA, MATH = "#9B8CFF", "#3CC6B3", "#FFC23D"
NAME = "UNREASONABLY EXACT"
TAGLINE = "Absurd questions. Real numbers. Sources on screen."
HEAVY = "font-family=\"Avenir Next, Avenir, Helvetica Neue, sans-serif\" font-weight=\"800\""
MED = "font-family=\"Avenir Next, Avenir, Helvetica Neue, sans-serif\" font-weight=\"500\""
MONO = "font-family=\"Menlo, SF Mono, monospace\" font-weight=\"700\""


def mark(x, y, s, wave=PAPER, line=SIGNAL):
    """The approx-to-exact mark: a rough wave over a dead-straight line (460 x 300 units at s=1)."""
    w = 56
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke-linecap="round" stroke-width="{w}">'
            f'<path d="M0 60 C 75 -20, 150 -20, 230 60 S 385 140, 460 60" stroke="{wave}"/>'
            f'<path d="M0 220 L460 220" stroke="{line}"/>'
            f'<path d="M115 290 L115 300 M230 280 L230 300 M345 290 L345 300" stroke="{wave}" stroke-width="{w*0.45}"/></g>')


def grid(w, h, step, op):
    lines = "".join(f'<path d="M{x} 0V{h}"/>' for x in range(0, w + 1, step))
    lines += "".join(f'<path d="M0 {y}H{w}"/>' for y in range(0, h + 1, step))
    return f'<g stroke="{PAPER}" stroke-opacity="{op}" stroke-width="2">{lines}</g>'


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>\n'


def chip(x, y, text, color, size=26):
    width = len(text) * size * 0.66 + 36
    return (f'<rect x="{x}" y="{y}" width="{width:.0f}" height="{size+22}" rx="8" fill="none" stroke="{color}" stroke-width="3"/>'
            f'<text x="{x+16}" y="{y+size+5}" {MONO} font-size="{size}" fill="{color}" letter-spacing="2">{text}</text>')


# ---- profile picture 800x800 (shown as a 98 px circle) ----
open("logo_profile.svg", "w").write(svg(800, 800, f'<rect width="800" height="800" fill="{INK}"/>' + mark(170, 250, 1)))

# ---- watermark 300x300 (YouTube min 150x150, square, <1 MB) ----
open("watermark.svg", "w").write(svg(300, 300,
    f'<circle cx="150" cy="150" r="146" fill="{INK}"/>' + mark(58, 95, 0.4)))

# ---- banner 2560x1440; safe area 1546x423 centred (x 507-2053, y 508-931) ----
x0, x1, ry = 600, 1960, 862
def lx(metres):  # log ruler, 1 m .. 10^17 m
    return x0 + math.log10(metres) / 17 * (x1 - x0)
rungs = [(1, "1 m", "up"), (38_969, "39 km", "down"), (3_596_400, "3,596 km", "up"),
         (406_771_000, "406,771 km", "down"), (10 * 9.4607e15, "10 ly", "up")]
ticks = "".join(f'<path d="M{lx(10**k):.1f} {ry-12}V{ry+12}"/>' for k in range(0, 18))
rung_svg = ""
for m, label, side in rungs:
    x = lx(m)
    rung_svg += f'<path d="M{x:.1f} {ry-26}V{ry+26}" stroke="{SIGNAL}" stroke-width="6"/>'
    ty = ry - 40 if side == "up" else ry + 62
    rung_svg += f'<text x="{x:.1f}" y="{ty}" text-anchor="middle" {MONO} font-size="28" fill="{SIGNAL}">{label}</text>'
banner = (f'<rect width="2560" height="1440" fill="{INK}"/>' + grid(2560, 1440, 64, 0.05)
          + f'<path d="M0 {ry}H2560" stroke="{PAPER}" stroke-opacity="0.18" stroke-width="3"/>'
          + mark(600, 560, 0.30)
          + f'<text x="770" y="652" {HEAVY} font-size="92" fill="{PAPER}" letter-spacing="3">{NAME}</text>'
          + f'<text x="774" y="722" {MED} font-size="40" fill="{PAPER}" fill-opacity="0.82">{TAGLINE}</text>'
          + f'<path d="M{x0} {ry}H{x1}" stroke="{PAPER}" stroke-width="4"/>'
          + f'<g stroke="{PAPER}" stroke-width="3">{ticks}</g>' + rung_svg
          + chip(880, 1010, "SIMULATION", SIM) + chip(1130, 1010, "REAL DATA", DATA) + chip(1355, 1010, "THE MATH", MATH))
open("banner.svg", "w").write(svg(2560, 1440, banner))
open("banner_safe_area_check.svg", "w").write(svg(2560, 1440, banner
    + '<rect x="507" y="508" width="1546" height="423" fill="none" stroke="red" stroke-width="4" stroke-dasharray="20 12"/>'
    + '<rect x="0" y="508" width="2560" height="423" fill="none" stroke="#00E5FF" stroke-width="3" stroke-dasharray="6 10"/>'))

# ---- sample thumbnail 1280x720: Day 25 "Who Was the Loneliest Human Ever?" (orbit ~110 km drawn to scale: 12 px at r=190 px = 1,737 km) ----
cx, cy, r = 320, 380, 190
thumb = (f'<rect width="1280" height="720" fill="{INK}"/>' + grid(1280, 720, 48, 0.05)
         + f'<circle cx="{cx}" cy="{cy}" r="{r+12}" fill="none" stroke="{PAPER}" stroke-opacity="0.45" stroke-width="4" stroke-dasharray="14 12"/>'
         + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#1C2742" stroke="{PAPER}" stroke-width="8"/>'
         + f'<path d="M{cx-r} {cy}L{cx+r+12} {cy}" stroke="{SIGNAL}" stroke-width="6" stroke-dasharray="18 10"/>'
         + f'<circle cx="{cx-r}" cy="{cy}" r="16" fill="{PAPER}"/><circle cx="{cx+r+12}" cy="{cy}" r="16" fill="{SIGNAL}"/>'
         + f'<text x="620" y="372" {HEAVY} font-size="112" fill="{SIGNAL}">3,596 km</text>'
         + f'<text x="626" y="446" {HEAVY} font-size="54" fill="{PAPER}">FROM ANY HUMAN</text>'
         + chip(36, 34, "REAL DATA", DATA, 24))
open("thumbnail_sample_day25.svg", "w").write(svg(1280, 720, thumb))
print("svgs written")

# ---- Day 1 thumbnail: "Does a Higher Fall Always Hit Harder?" (written into the production folder) ----
import os
PROD = "../../../productions/unreasonably-exact-01-free-fall"
os.makedirs(PROD, exist_ok=True)
top, bot, rx = 80, 650, 150
def ry(metres):  # vertical log ruler, 1 m at bottom .. 400 km at top
    return bot - math.log10(metres) / math.log10(400e3) * (bot - top)
marks = [(1, "1 m"), (100, "100 m"), (10e3, "10 km"), (100e3, "100 km"), (400e3, "400 km")]  # no 39 km highlight: v2 thumbnail is about landing speed
ruler = f'<path d="M{rx} {top}V{bot}" stroke="{PAPER}" stroke-width="5"/>'
for m, label in marks:
    y, hot = ry(m), label == "39 km"
    col = SIGNAL if hot else PAPER
    ruler += (f'<path d="M{rx-18} {y:.0f}H{rx+(40 if hot else 18)}" stroke="{col}" stroke-width="{8 if hot else 5}" stroke-linecap="round"/>'
              f'<text x="{rx-30}" y="{y+9:.0f}" text-anchor="end" {MONO} font-size="{28 if hot else 22}" fill="{col}">{label}</text>')
fy = ry(38_969)
diver = (f'<g transform="translate(330,{fy:.0f})" stroke-linecap="round">'
         f'<path d="M0 -150V-40 M-40 -160V-70 M40 -160V-70" stroke="{PAPER}" stroke-opacity="0.35" stroke-width="5"/>'
         f'<path d="M-70 -30 L-30 0 M70 -30 L30 0 M-20 40 L-55 85 M20 40 L55 85" stroke="{PAPER}" stroke-width="22"/>'
         f'<ellipse cx="0" cy="15" rx="34" ry="46" fill="{PAPER}"/>'
         f'<circle cx="0" cy="-40" r="30" fill="{PAPER}"/><path d="M-18 -44 H18" stroke="{INK}" stroke-width="10"/></g>')
day1 = (f'<rect width="1280" height="720" fill="{INK}"/>' + grid(1280, 720, 48, 0.05) + ruler + diver
        + f'<text x="500" y="330" {HEAVY} font-size="76" fill="{SIGNAL}">1 KM: 204 km/h</text>'
        + f'<text x="500" y="430" {HEAVY} font-size="76" fill="{PAPER}">100 KM: 204 km/h</text>'
        + f'<text x="506" y="530" {HEAVY} font-size="60" fill="{PAPER}">SAME LANDING?</text>'
        + chip(1000, 34, "SIMULATION", DATA, 24))  # v2 (2026-11-19): landing-speed contrast, model values D1-07/D1-19
open(f"{PROD}/thumbnail_day01.svg", "w").write(svg(1280, 720, day1))

# ---- Day 3 thumbnail: "What If a Bullet Were Made of Neutron Star?" (level balance, equal arms of 210 px: 0.7 cm3 pellet = 412 m rock cube) ----
PROD3 = "../../../productions/unreasonably-exact-03-neutron-bullet"
os.makedirs(PROD3, exist_ok=True)
by = 380
day3 = (f'<rect width="1280" height="720" fill="{INK}"/>' + grid(1280, 720, 48, 0.05)
        + '<defs><radialGradient id="glow"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.25" stop-color="#9FD8FF"/>'
          '<stop offset="1" stop-color="#9FD8FF" stop-opacity="0"/></radialGradient></defs>'
        + f'<path d="M80 {by}H680" stroke="{PAPER}" stroke-width="10" stroke-linecap="round"/>'
        + f'<path d="M360 {by} L310 {by+170} H410 Z" fill="none" stroke="{PAPER}" stroke-width="8" stroke-linejoin="round"/>'
        + f'<circle cx="150" cy="{by-14}" r="60" fill="url(#glow)"/><circle cx="150" cy="{by-14}" r="9" fill="#FFFFFF"/>'
        + f'<rect x="470" y="{by-200}" width="200" height="200" fill="#1C2742" stroke="{PAPER}" stroke-width="6"/>'
        + f'<text x="150" y="{by+50}" text-anchor="middle" {MONO} font-size="24" fill="{PAPER}">0.7 cm³</text>'
        + f'<text x="570" y="{by+50}" text-anchor="middle" {MONO} font-size="24" fill="{PAPER}">412 m rock cube</text>'
        + f'<text x="740" y="190" {HEAVY} font-size="44" fill="{PAPER}">AT LEAST</text>'
        + f'<text x="730" y="360" {HEAVY} font-size="200" fill="{SIGNAL}">190</text>'
        + f'<text x="736" y="440" {HEAVY} font-size="52" fill="{PAPER}">MILLION TONNES</text>'
        + chip(1050, 34, "THE MATH", MATH, 24))
open(f"{PROD3}/thumbnail_day03.svg", "w").write(svg(1280, 720, day3))
