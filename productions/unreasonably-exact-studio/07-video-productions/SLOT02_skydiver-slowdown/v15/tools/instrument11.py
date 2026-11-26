"""V11 wearable speed indicator.

Artwork: Codex V11 *candidate* wrist compositions (sleeve + hand + device with a BLANK face).
The face itself (scale, labels, needle, cap) is authored here so it stays editable and identical in every view:
  mounted  - wrist/mounted_reference.png  (third-person forearm, device face toward camera)
  pov      - wrist/pov_reference.png      (first-person: your own forearm reaching out)
Face ellipses were measured on the gridded sheets qa/G_mounted.png and qa/G_pov.png (source pixels).
It is an illustrative DOWNWARD-SPEED indicator with a qualitative SLOW..FAST scale and no numerals,
not an altimeter (the real wrist devices in the owner's references measure altitude)."""
import math
import rig_renderer as R
C = R.C
PKG = 'CODEX_V11_ART_REPAIR_PACKAGE/wrist/'
# name: (file, canvas width, face centre, rx, ry, face rotation deg [12 o'clock direction])
WRISTS = {
    'mounted': (PKG + 'mounted_reference.png', 1774, (853, 409), 84, 81, -4),
    'pov':     (PKG + 'pov_reference.png',     1774, (829, 497), 76, 85, -18),
}
SPEED_MAX = 90.0
SWEEP = 120.0
INK = (0.17, 0.17, 0.16); BLUE = (0.18, 0.36, 0.55)

def needle_angle(v):
    """0 speed = -120 deg (lower left, SLOW), full scale = +120 deg (lower right, FAST). Clockwise from 12."""
    return -SWEEP + 2 * SWEEP * max(0.0, min(1.0, v / SPEED_MAX))

def _pol(a_deg, r):
    a = math.radians(a_deg)
    return r * math.sin(a), -r * math.cos(a)

def face(c, v, alpha=1.0, detail=1.0):
    """Dial face in unit-circle coordinates (radius 1 = inner edge of the bezel). detail<1 drops small text."""
    c.save()
    # graduated band: light at SLOW, deep blue at FAST (no numbers)
    n = 24
    for i in range(n):
        a0 = -SWEEP + 2 * SWEEP * i / n; a1 = -SWEEP + 2 * SWEEP * (i + 1) / n
        k = (i + .5) / n
        c.set_source_rgba(*[0.80 + (b - 0.80) * k for b in BLUE], alpha)
        c.set_line_width(.13); c.new_path()
        c.arc(0, 0, .74, math.radians(a0 - 90), math.radians(a1 - 90 + .4)); c.stroke()
    # ticks
    for i in range(9):
        a = -SWEEP + 2 * SWEEP * i / 8
        r0 = .60 if i % 4 == 0 else .65
        x0, y0 = _pol(a, r0); x1, y1 = _pol(a, .86)
        c.set_source_rgba(*INK, alpha); c.set_line_width(.045 if i % 4 == 0 else .028)
        c.move_to(x0, y0); c.line_to(x1, y1); c.stroke()
    if detail > .3:
        c.select_font_face('Helvetica Neue', 0, C.FONT_WEIGHT_BOLD); c.set_font_size(.17)
        for s, a in (('SLOW', -122), ('FAST', 122)):
            x, y = _pol(a, .42); e = c.text_extents(s)
            c.set_source_rgba(*INK, alpha * min(1, detail)); c.move_to(x - e[2] / 2 - e[0], y + .05); c.show_text(s)
        c.set_font_size(.12); s = 'DOWN SPEED'; e = c.text_extents(s)
        c.set_source_rgba(*BLUE, alpha * min(1, detail)); c.move_to(-e[2] / 2 - e[0] + .05, .58); c.show_text(s)
        # small down-arrow glyph before the words: this dial is about downward motion
        gx = -e[2] / 2 - .04
        c.set_line_width(.03); c.move_to(gx, .46); c.line_to(gx, .57); c.stroke()
        c.move_to(gx - .04, .53); c.line_to(gx, .58); c.line_to(gx + .04, .53); c.stroke()
    # needle (charcoal, tapered, with tail) + cap
    c.save(); c.rotate(math.radians(needle_angle(v)))
    c.set_source_rgba(*INK, alpha)
    c.move_to(-.045, .14); c.line_to(-.022, -.66); c.line_to(0, -.80); c.line_to(.022, -.66); c.line_to(.045, .14); c.close_path(); c.fill()
    c.restore()
    c.arc(0, 0, .085, 0, 6.283); c.set_source_rgba(.35, .35, .33, alpha); c.fill()
    c.arc(0, 0, .085, 0, 6.283); c.set_source_rgba(*INK, alpha); c.set_line_width(.025); c.stroke()
    c.restore()

def wrist(c, name, x, y, width, v, alpha=1.0, rot=0.0, detail=1.0):
    """Draw a whole wrist composition so the DIAL CENTRE lands at (x, y) and the artwork is `width` units wide."""
    f, cw, (fx, fy), rx, ry, frot = WRISTS[name]
    s = width / cw
    c.save(); c.translate(x, y); c.rotate(math.radians(rot)); c.scale(s, s); c.translate(-fx, -fy)
    R.draw(c, f, alpha, cw)
    c.translate(fx, fy); c.rotate(math.radians(frot)); c.scale(rx, ry)
    face(c, v, alpha, detail)
    c.restore()

def face_radius(name, width):
    f, cw, _, rx, ry, _ = WRISTS[name]; return width / cw * (rx + ry) / 2
