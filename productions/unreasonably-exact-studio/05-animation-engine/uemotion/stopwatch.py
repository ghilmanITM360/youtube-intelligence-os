"""Stopwatch: analog dial + digital readout, driven ONLY by a model-clock value (model_t) so it can never drift from the pulse."""
import math
from . import tokens as T
from .camera import T3, S3

def hand_angle(value, full): return value / full * 2 * math.pi - math.pi / 2

def format_reading(value): return '%.2f' % value

def draw_stopwatch(cv, c, r=170, value=0.0, full=3.0, alpha=1.0, pop=0.0, tint=T.WARM, digits=True, frozen=False):
    """value = seconds shown (model_t). full = seconds per dial revolution. pop = 0..~1.2 'stop' kick (scale overshoot).
    Returns the digital string actually drawn (so tests can assert the displayed reading)."""
    x, y = c; s = 1.0 + 0.07 * pop; reading = format_reading(value)
    with cv.xf(T3(x, y) @ S3(s) @ T3(-x, -y)), cv.group(alpha):
        cv.rect((x - 16, y - r - 34, x + 16, y - r + 4), fill=T.GREY, radius=6)                      # crown
        cv.rect((x - 26, y - r - 44, x + 26, y - r - 28), fill=T.mix(T.GREY, T.WHITE, 0.3), radius=8)
        cv.circle(c, r + 12, fill=T.mix(T.PANEL, T.GREY, 0.35))                                       # case
        cv.circle(c, r, fill=T.PANEL, outline=T.WHITE if not frozen else tint, width=5)
        for i in range(30):                                                                           # 30 ticks per revolution = 0.1 s each at full=3
            a = i / 30 * 2 * math.pi - math.pi / 2; major = i % 5 == 0; l = 0.17 if major else 0.08
            cv.line((x + math.cos(a) * r * (0.93 - l), y + math.sin(a) * r * (0.93 - l)), (x + math.cos(a) * r * 0.93, y + math.sin(a) * r * 0.93),
                    T.GREY if not major else T.WHITE, 3 if major else 2)
        for k in range(int(full)):                                                                    # whole-second numerals
            a = hand_angle(k, full); cv.text((x + math.cos(a) * r * 0.62, y + math.sin(a) * r * 0.62), str(k), 30, T.GREY, bold=True, mono=True)
        a0 = -math.pi / 2; a1 = hand_angle(value, full)
        if value > 1e-3: cv.arc(c, r * 0.80, a0, a1, tint, 6, alpha=0.55)                            # swept arc = elapsed
        a = hand_angle(value, full)
        cv.line((x - math.cos(a) * r * 0.16, y - math.sin(a) * r * 0.16), (x + math.cos(a) * r * 0.74, y + math.sin(a) * r * 0.74), tint, 7)
        cv.circle(c, 11, fill=T.WHITE); cv.circle(c, 5, fill=T.PANEL)
        if digits:                                           # digital readout in its own pill UNDER the dial (never covers the numerals)
            pw, ph = r * 1.45, r * 0.52; y0 = y + r + 30
            cv.rect((x - pw / 2, y0, x + pw / 2, y0 + ph), fill=(10, 14, 30), outline=tint if frozen else T.GREY, width=3, radius=14)
            cv.text((x - 12, y0 + ph / 2 + 2), reading, int(r * 0.40), tint if frozen else T.WHITE, mono=True, bold=True)
            cv.text((x + pw / 2 - 24, y0 + ph / 2 + 8), 's', 32, T.GREY, mono=True, anchor='rm')
    return reading
