# V12 shot code. Executed inside tools/v13.py's namespace (palette, camera, arrows, text, PHYS, I, R).
# V12 = motion-design re-edit of V11 (owner review 2026-11-25): text cut to essentials, no persistent brand,
# no MODEL banner, no floating speed inset, forces and magnification built inside the scene, a single
# descending equal-time trail on one common scale, layered 2.5D opening, side rig with arm lift / glance / blink.
# Visual rhythm (research/VISUAL_REFERENCE_NOTES.md): mostly calm holds, one new visual event every ~2 s.

SPEED_MAX = I.SPEED_MAX
ZOOM = 30                     # in-scene magnifier for the arrow tips (disclosed on the lens rim)
CAPTIONS = False              # burned captions are a separate overlay pass (tools/v13.py --captions)

def chip(c, s, x, y, h=MUTED, a=1.0, size=8.5, align='l'):
    """Small, quiet label (no box)."""
    if a > .01: text(c, s, x, y, size, h, True, align, a)

# ---------------------------------------------------------------- character
BODIES = {   # whole-pose drawings (three-quarter / back): file, canvas width, centre of mass (px), body length (px)
    'side':          ('assets/v11reg/side_body.png', 1920, (960, 500), 1900),
    'three_quarter': ('assets/v13reg/tq_body.png',   1774, (880, 470), 1700),
    'back':          ('assets/v13reg/back_body.png', 1586, (790, 560), 1500),
}
RIG = json.loads((ROOT / 'assets/v12rig/RIG.json').read_text())
NLIFT = RIG['lift_frames']
NECK = RIG['neck_pivot']
EYE = (1472, 291)

def body(c, view, x, y, width, t=0.0, amt=1.0, seed=0, rot=0.0, alpha=1.0):
    """Whole-pose drawing; calm roll/bob scaled by amt (used for three-quarter, back, tiny figures)."""
    f, cw, (px, py), L = BODIES[view]
    s = width / L
    roll = rot + wobble(t, .11, seed + 1, 1.0 * amt)
    bob = wobble(t, .17, seed + 2, 1.2 * amt)
    c.save(); c.translate(x, y + bob); c.rotate(math.radians(roll)); c.scale(s, s); c.translate(-px, -py)
    R.draw(c, f, alpha, cw); c.restore()
    return x, y + bob

def side_rig(c, x, y, width, t=0.0, lift=0.0, glance=0.0, nod=0.0, blink=False, amt=.6, seed=0, rot=0.0, alpha=1.0):
    """V12 side rig (tools/build_rig.py): lift 0..1 plays the forearm-raise sequence, glance 0..1 cross-fades
    the head to the registered glance drawing, nod (deg, |nod|<=1) tilts the head about the neck."""
    cw, (px, py), L = 1920, (960, 500), 1900
    s = width / L
    roll = rot + wobble(t, .11, seed + 1, .8 * amt)
    bob = wobble(t, .17, seed + 2, 1.2 * amt)
    k = int(round(clamp(lift) * (NLIFT - 1)))
    c.save(); c.translate(x, y + bob); c.rotate(math.radians(roll)); c.scale(s, s); c.translate(-px, -py)
    c.push_group()
    R.draw(c, f'assets/v12rig/side_lift_{k:02}.png', 1, cw)
    R.draw(c, 'assets/v12rig/side_neck_underlay.png', 1, cw)
    c.save(); c.translate(*NECK); c.rotate(math.radians(clamp(nod, -1, 1))); c.translate(-NECK[0], -NECK[1])
    g = clamp(glance)
    if g < 1: R.draw(c, 'assets/v12rig/side_head.png', 1, cw)
    if blink and g < .5:
        col(c, (233 / 255, 203 / 255, 176 / 255)); c.save(); c.translate(*EYE); c.scale(17, 14); c.arc(0, 0, 1, 0, 6.283); c.restore(); c.fill()
        col(c, INK); c.set_line_width(3.2); c.set_line_cap(C.LINE_CAP_ROUND)
        c.move_to(EYE[0] - 13, EYE[1] - 1); c.curve_to(EYE[0] - 4, EYE[1] + 6, EYE[0] + 6, EYE[1] + 6, EYE[0] + 13, EYE[1] - 1); c.stroke()
    if g > 0: R.draw(c, 'assets/v12rig/side_head_glance.png', g, cw)
    c.restore()
    c.pop_group_to_source(); c.paint_with_alpha(alpha)
    c.restore()
    return x, y + bob

def lift_curve(t, t_up, t_down=None, up=.42, down=.36):
    """Purposeful lift: ease up over `up` s, hold, ease down. Drives the sprite index (no bounce)."""
    a = ease_io((t - t_up) / up)
    if t_down is not None: a *= 1 - ease_io((t - t_down) / down)
    return a

def blinking(t, times):
    return any(0 <= t - b < .11 for b in times)

# ---------------------------------------------------------------- airflow (V12: trim-path reveal + flow markers)
def stream_paths(cx, cy, a, b, n=12, span=160, top=-230, bot=230):
    """Potential flow past an ellipse, relative to the body (air arrives from below, leaves above). Schematic."""
    R0 = b; sx = a / b; out = []
    for i in range(n):
        x0 = (i - (n - 1) / 2) / ((n - 1) / 2) * span; X0 = x0 / sx
        if abs(X0) < R0 * .5: continue
        pts = []
        for k in range(0, 91):
            Y = bot - k * (bot - top) / 90.0; X = X0
            for _ in range(14):
                r2 = X * X + Y * Y
                if r2 < 1e-6: break
                f = X * (1 - R0 * R0 / r2) - X0; df = (1 - R0 * R0 / r2) + 2 * X * X * R0 * R0 / (r2 * r2)
                if abs(df) < 1e-6: break
                X -= f / df
            pts.append((cx + X * sx, cy + Y))
        out.append((x0, pts))
    return out

def airflow(c, paths, t, speed, grow, alpha, layer, span=160, cy=300, half=230):
    """layer 'back': all lines (drawn behind the body); 'front': only the outer lines, faint, in front.
    grow: trim-path reveal 0..1 (staggered per line). Markers: short dashes travelling along each path."""
    if alpha <= 0: return
    c.save(); c.set_line_cap(C.LINE_CAP_ROUND)
    for j, (x0, pts) in enumerate(paths):
        outer = abs(x0) > span * .62
        if layer == 'front' and not outer: continue
        g = clamp(grow * 1.6 - j * .05)
        m = int(len(pts) * g)
        if m < 2: continue
        near = 1 - min(1, abs(x0) / (span * 1.05))
        k_layer = .55 if layer == 'front' else 1.0
        for q in range(1, m):
            yv = (pts[q][1] - cy) / half
            aa = alpha * k_layer * (.32 + .45 * near) * max(0, 1 - abs(yv) ** 2.2)
            col(c, AIR, aa); c.set_line_width(1.1 if layer == 'back' else 1.5)
            c.move_to(*pts[q - 1]); c.line_to(*pts[q]); c.stroke()
        for q in range(4):   # flow markers
            u = ((t * speed / 420.0) + q / 4 + j * .17) % 1.0
            p = int(u * (m - 3)) + 1
            if p + 2 >= m: continue
            yv = (pts[p][1] - cy) / half; aa = alpha * k_layer * max(0, 1 - abs(yv) ** 2.2)
            col(c, '#FFFFFF', .95 * aa); c.set_line_width(2.6); c.move_to(*pts[p]); c.line_to(*pts[p + 2]); c.stroke()
            col(c, AIR, aa); c.set_line_width(1.4); c.move_to(*pts[p]); c.line_to(*pts[p + 2]); c.stroke()
    c.restore()

# ---------------------------------------------------------------- forces
L_W = 118   # weight arrow length on the common scale (units); drag = L_W * D/W
def grow_arrow(c, x, y, L, h, g, w=5, head=12, alpha=1.0, **kw):
    """Arrow drawn on like a pen stroke (trim path): g 0..1 of its length."""
    if g <= 0: return
    arrow(c, x, y, 0, L * ease_out(g), h, w, head, alpha=alpha, **kw)

def forces(c, cx, cy, dw, gw=1.0, gd=1.0, a=1.0, lab=0.0):
    grow_arrow(c, cx, cy + 3, L_W, WEIGHT, gw, alpha=a)
    grow_arrow(c, cx, cy - 3, -L_W * dw, DRAG, gd, alpha=a)
    if lab > 0:
        chip(c, 'weight', cx + 9, cy + L_W - 6, WEIGHT, a * lab, 10)
        chip(c, 'drag', cx + 9, cy - 3 - L_W * max(dw, .2) + 12, DRAG, a * lab, 10)

def vel_arrow(c, x, y, v, a=1.0, t=0.0, k=.75):
    """Downward velocity: dashed blue, separate lane, length proportional to model speed (schematic scale)."""
    arrow(c, x, y, 0, 8 + k * v, VEL, 3.2, 10, dashed=True, alpha=a, dash_off=-t * 18)

def magnifier(c, t, cx, cy, dw, open_, lx, ly, r=86, ring_y=None):
    """In-scene lens on the arrow tips, x ZOOM. Inside the lens everything is the SAME drawing scaled ZOOM x about
    the weight-length mark: the dashed rust line = where an arrow as long as the weight ends; the teal tip sits
    (dw-1)*L_W*ZOOM above it. Violet = the difference = net force. Lens joined to the tips by a leader."""
    if open_ <= 0: return
    rr = r * ease_out(open_)
    ty = cy - 3 - L_W if ring_y is None else ring_y   # weight-length mark on the body diagram (screen)
    col(c, NET, .7 * open_); c.set_line_width(1.2)
    c.move_to(cx + 10, ty); c.line_to(lx - rr * .7, ly + rr * .7); c.stroke()
    col(c, NET, open_); c.arc(cx, ty, 9, 0, 6.283); c.stroke()
    c.save(); c.arc(lx, ly, rr, 0, 6.283); c.clip()
    col(c, '#F7F8F5', .97); c.paint()
    gap = (dw - 1) * L_W * ZOOM
    base = ly + 18
    # drag: magnified arrow head + shaft rising to its tip
    tip = base - gap
    col(c, DRAG); c.rectangle(lx - 12, tip + 30, 24, 400); c.fill()
    c.move_to(lx - 30, tip + 34); c.line_to(lx, tip); c.line_to(lx + 30, tip + 34); c.close_path(); c.fill()
    # weight-length mark
    col(c, WEIGHT); c.set_line_width(2.4); c.set_dash([7, 5]); c.move_to(lx - rr, base); c.line_to(lx + rr, base); c.stroke(); c.set_dash([])
    if gap > 5:
        arrow(c, lx + 44, base, 0, -gap, NET, 5, 11, double=True)
    elif gap < -5:
        arrow(c, lx + 44, base, 0, -gap, WEIGHT, 2.4, 8, alpha=.8)
    c.restore()
    col(c, NET, open_); c.set_line_width(2); c.arc(lx, ly, rr, 0, 6.283); c.stroke()
    # rim badge (scale disclosure)
    c.save(); col(c, NET, open_); rrect(c, lx + rr * .45, ly + rr * .78, 34, 15, 7); c.fill(); c.restore()
    chip(c, f'×{ZOOM}', lx + rr * .45 + 17, ly + rr * .78 + 11, '#FFFFFF', open_, 9, 'c')
    if gap > 5: chip(c, 'net force', lx + 52, base - gap / 2 + 3, NET, open_ * clamp(gap / 30), 9)

# ---------------------------------------------------------------- in-scene instruments
def alt_ruler(c, h, a=1.0, x=340, y0=118, y1=560, ghosts=()):
    """Altitude ruler on the right edge: top = 10 km, bottom = ground. Marker = model altitude."""
    if a <= 0: return
    col(c, INK, .45 * a); c.set_line_width(1); c.move_to(x, y0); c.line_to(x, y1); c.stroke()
    for km in range(0, 11):
        yy = y1 - (y1 - y0) * km / 10; c.move_to(x - (5 if km % 5 == 0 else 3), yy); c.line_to(x, yy); c.stroke()
    chip(c, '10 km', x - 7, y0 + 3, MUTED, a, 8, 'r'); chip(c, 'ground', x - 7, y1 + 3, MUTED, a, 8, 'r')
    yy = y1 - (y1 - y0) * h / 10000
    col(c, VEL, a); c.move_to(x + 1, yy); c.line_to(x + 8, yy - 5); c.line_to(x + 8, yy + 5); c.close_path(); c.fill()
    return yy

def air_lens(c, t, x, y, r, rho, v, a=1.0, seed=4):
    """Equal-size air sample: dot count proportional to model density (marks, not molecules); dots drift up past
    the falling body at a rate following the model speed (relative air)."""
    if a <= 0: return
    c.save(); c.arc(x, y, r, 0, 6.283); c.clip()
    col(c, '#FFFFFF', .9 * a); c.paint()
    rr = random.Random(seed); n = int(round(rho / 1.226 * 70))
    col(c, '#35658A', .9 * a)
    for i in range(70):
        px, py = rr.uniform(-r, r), rr.uniform(-r, r) * 1.0
        py = (py + r - t * (6 + v * .35)) % (2 * r) - r
        if i < n: c.arc(x + px, y + py, 1.7, 0, 6.283); c.fill()
    c.restore()
    col(c, AIR, a); c.set_line_width(1.4); c.arc(x, y, r, 0, 6.283); c.stroke()

# ---------------------------------------------------------------- graph (progressive, no card)
def speed_graph(c, t, t0, upto, alpha=1.0, alt=None, x=48, y=150, w=270, h=280, axes=1.0, marks=1.0):
    if alpha <= 0: return
    c.save()
    col(c, INK, .85 * alpha); c.set_line_width(1.5); c.set_line_cap(C.LINE_CAP_ROUND)
    ay = ease_out(axes); c.move_to(x, y + h); c.line_to(x, y + h - (h + 8) * ay); c.stroke()
    c.move_to(x, y + h); c.line_to(x + (w + 8) * ay, y + h); c.stroke()
    chip(c, 'downward speed', x - 2, y - 14, INK, alpha * ay, 10.5)
    chip(c, 'time', x + w + 6, y + h + 18, INK, alpha * ay, 10.5, 'r')
    chip(c, 'zero', x - 5, y + h + 3, MUTED, alpha * ay, 8.5, 'r')
    tmax = PHYS.END_T
    def P(row): return x + w * row[0] / tmax, y + h - h * row[2] / SPEED_MAX
    def curve(tr, up):
        c.new_path(); first = True
        for row in tr[::25]:
            if row[0] > up: break
            (c.move_to if first else c.line_to)(*P(row)); first = False
    if alt:
        for lab, k, a, dy in alt:
            if a <= 0: continue
            col(c, MUTED, a * alpha); c.set_line_width(1.6); c.set_dash([5, 4]); curve(PHYS_ALT[k], tmax * ease_out(a)); c.stroke(); c.set_dash([])
            mx, my = P(PHYS_ALT[k][-1]); chip(c, lab, x + w, my + dy, MUTED, a * alpha, 8.5, 'r')
    if upto > 0:
        col(c, VEL, alpha); c.set_line_width(3.2); curve(PHYS.TRACE, upto); c.stroke()
        row = PHYS.at_time(min(upto, tmax - .05)); px, py = P(row)
        col(c, '#FFFFFF', alpha); c.arc(px, py, 6.5, 0, 6.283); c.fill(); col(c, VEL, alpha); c.arc(px, py, 4.5, 0, 6.283); c.fill()
        pk = P(PHYS.PEAK)
        if upto > PHYS.PEAK[0] + 4:
            m = alpha * marks * ramp(upto, PHYS.PEAK[0] + 4, PHYS.PEAK[0] + 12)
            col(c, INK, .6 * m); c.set_line_width(1); c.set_dash([2, 3]); c.move_to(pk[0], pk[1] - 4); c.line_to(pk[0], y - 2); c.stroke(); c.set_dash([])
            chip(c, 'top speed', pk[0] + 5, y + 6, INK, m, 9)
        if upto > 100:   # bracket: still above zero
            m = alpha * marks * ramp(upto, 100, 140)
            col(c, VEL, .8 * m); c.set_line_width(1.4)
            c.move_to(px + 8, py); c.line_to(px + 12, py); c.line_to(px + 12, y + h); c.line_to(px + 8, y + h); c.stroke()
            chip(c, 'not zero', px + 4, py + (y + h - py) / 2 + 4, VEL, m, 9, 'r')
    c.restore()

def sim_alt(k):
    old = PHYS.CDA; PHYS.CDA = old * k
    try: return PHYS.simulate()
    finally: PHYS.CDA = old
PHYS_ALT = {}

# ---------------------------------------------------------------- environment helpers
def aircraft(c, x, y, w, t, alpha=1.0):
    s = w / 640.0
    c.save(); c.translate(x - w / 2, y - 200 * s); c.scale(s, s); c.push_group()
    R.draw(c, 'assets/codex/aircraft_side.png', 1, 640)
    c.translate(602, 220); c.scale(1, .55 + .45 * abs(math.sin(t * 40))); c.translate(-602, -220)
    R.draw(c, 'assets/codex/aircraft_propeller.png', .8, 640)
    c.pop_group_to_source(); c.paint_with_alpha(alpha); c.restore()

def near_clouds(c, t, x0, rate, alpha=1.0, y=300, size=520, kinds=(0, 3, 5)):
    """Foreground cloud layer passing the lens (depth reveal / wipe)."""
    for i, k in enumerate(kinds):
        cloud_sprite(c, x0 + i * 260 - t * rate, y + 60 * math.sin(i * 2.1), size * (1 + .2 * i), CLOUD_KINDS[k], alpha)

def tracking_bg(c, t, h, v, pitch=-14.0, F=430, streak_alpha=.5, wisps=True, cy=330):
    cam = Cam(h, pitch, F, cy=cy)
    environment(c, cam)
    if wisps: passing_wisps(c, t, 2.2 * v, alpha=.42)
    air_streaks(c, t, 4.8 * v + 20, streak_alpha)
    return cam

def push(c, fx, fy, z):
    c.translate(fx, fy); c.scale(z, z); c.translate(-fx, -fy)

def pov_shot(c, t, t0, dur, tm0, tm1, mode):
    u = clamp((t - t0) / dur)
    tm = lerp(tm0, tm1, u); h, v, dw, rho = state(tm)
    if mode == 'dial':
        pitch = 64; z = lerp(1.15, 2.3, ease_io(u)); ax, ay = 200, 300
    else:
        pitch = lerp(64, 86, ease_io(u)); z = lerp(2.3, 1.0, ease_io(u * 1.4)); ax, ay = lerp(200, 20, ease_io(u / .55)), lerp(300, 1150, ease_io(u / .55))
    cam = Cam(h, pitch, 360, cy=300); environment(c, cam)
    air_streaks(c, t, 4.5 * v, .5, count=34)
    c.save(); push(c, ax, ay, z)
    I.wrist(c, 'pov', ax, ay, 700, v, 1, rot=-6 + 1.5 * math.sin(t * 1.1), detail=clamp((z - 1.2) / .5))
    c.restore()
    return h, v


# ---------------------------------------------------------------- V13 opening (restores the V10/V11 composition, adds parallax)
LAND = 'CODEX_V11_ART_REPAIR_PACKAGE/environment/landscape_reference.png'
LAND_HORIZON = .555          # horizon row of the painted study (fraction of image height)
@lru_cache(maxsize=4)
def painted(f):
    from PIL import Image
    import io
    im = Image.open(ROOT / f).convert('RGBA'); b = io.BytesIO(); im.save(b, 'PNG'); b.seek(0)
    return C.ImageSurface.create_from_png(b)

def land_layer(c, horizon_y, zoom, dx, part):
    """Painted V11 landscape split at its horizon: part 'far' (sky + distant hills) or 'near' (fields).
    horizon_y = screen y of the horizon; the two parts get different offsets/zooms for parallax."""
    s = painted(LAND); iw, ih = s.get_width(), s.get_height()
    k = 640 / ih * 1.02 * zoom
    c.save(); c.translate(180 + dx - iw * k / 2, horizon_y - LAND_HORIZON * ih * k); c.scale(k, k)
    if part == 'far': c.rectangle(0, -2000, iw, LAND_HORIZON * ih + 2000 + 2)
    else: c.rectangle(0, LAND_HORIZON * ih - 1, iw, ih + 2000)
    c.clip()
    if part == 'near':    # continue the foreground field colour below the painting
        col(c, (165 / 255, 190 / 255, 135 / 255)); c.rectangle(0, ih - 2, iw, 2002); c.fill()
    if part == 'far':     # extend the sky above the painting with its own top colour
        g = C.LinearGradient(0, -1400, 0, 2); g.add_color_stop_rgb(0, *rgb('#9CC4E4')); g.add_color_stop_rgb(1, 185 / 255, 217 / 255, 239 / 255)
        c.set_source(g); c.rectangle(0, -2000, iw, 2002); c.fill()
    c.set_source_surface(s, 0, 0); c.get_source().set_filter(C.FILTER_GOOD); c.paint(); c.restore()

OPEN_CLOUDS = [(-150, 405, 64, 1), (60, 418, 48, 4), (250, 398, 80, 2), (440, 412, 56, 0)]
def opening(c, t):
    """A ESTABLISH 0-1.2 s: aircraft upper-middle, figure just below it, both readable at phone size.
       B FOLLOW 1.2-2.3 s: camera tilts down with the falling figure; the aircraft rises to the top of frame.
       C APPROACH 2.3-3.3 s: dolly in on the figure; far hills, mid clouds and figure move at different rates.
       (D REVEAL is the next shot: behind the faller, closed pack.)  Illustrative framing, not jump procedure."""
    b = ease_io(clamp((t - 1.1) / 1.3))          # follow (tilt)
    z = ease_io(clamp((t - 2.15) / 1.15))        # approach (dolly)
    Z = lerp(1.0, 4.2, z)
    # figure: falls in the world; the camera tracks it with a little lag
    fx, fy = 172 + 4 * t, lerp(262, 292, b) + 3 * math.sin(t * 2.1)
    tilt = 95 * b                               # screen shift of distant layers caused by the tilt
    hz = 430 - tilt * .55 + 0                    # horizon y (far layer moves least)
    def zoom_about(k):                           # parallax in depth: far layers zoom less than the subject
        c.translate(fx, fy); c.scale(k, k); c.translate(-fx, -fy)
    c.save(); zoom_about(1 + (Z - 1) * .06); land_layer(c, hz, 1.0, 150 - 8 * t, 'far'); c.restore()
    c.save(); zoom_about(1 + (Z - 1) * .12); land_layer(c, hz - tilt * .25, 1.0, 150 - 14 * t, 'near'); c.restore()
    # atmospheric haze band on the horizon
    g = C.LinearGradient(0, hz - 70, 0, hz + 60)
    g.add_color_stop_rgba(0, *HAZE, 0); g.add_color_stop_rgba(.55, *HAZE, .55); g.add_color_stop_rgba(1, *HAZE, 0)
    c.set_source(g); c.paint()
    # mid clouds (between the ground and the figure): medium scale, never covering the subjects
    c.save(); zoom_about(1 + (Z - 1) * .45)
    for x, y, w, kd in OPEN_CLOUDS:
        cloud_sprite(c, (x - 22 * t) % 640 - 140, y - tilt * .8, w, CLOUD_KINDS[kd], .95)
    c.restore()
    # subjects (full zoom)
    c.save(); zoom_about(Z)
    ax, ay = 178 + 30 * t, 176 - tilt * 1.05
    aircraft(c, ax, ay, 124, t)
    body(c, 'side', fx, fy, 50, t, 1.4, 3, rot=6)
    c.restore()
    ra = ramp(t, .45, .8) * (1 - ramp(t, 1.7, 2.1))      # one attention ring on the faller, no label
    col(c, INK, .75 * ra); c.set_line_width(1.1); c.arc(fx, fy, 34 + 6 * (1 - ra), 0, 6.283); c.stroke()


# ---------------------------------------------------------------- V13 science scenes
def sky_plain(c, alpha=1.0):
    g = C.LinearGradient(0, 0, 0, 640); g.add_color_stop_rgb(0, *rgb('#A9CDE6')); g.add_color_stop_rgb(1, *rgb('#E2EEF5'))
    c.set_source(g); c.paint_with_alpha(alpha)

AIR_DOTS = [(random.Random(91 + i).uniform(-175, 175), random.Random(191 + i).uniform(0, 720)) for i in range(120)]
def deflect(X0, Y, a, b):
    """Potential flow past an ellipse (cylinder of radius b, x scaled by a/b): x-position of the streamline that
    starts at x0 far upstream, at height Y relative to the body. Schematic, not a validated simulation."""
    sx = a / b; Xs = X0 / sx; X = Xs if abs(Xs) > 1 else math.copysign(1, Xs or 1)
    for _ in range(10):
        r2 = X * X + Y * Y
        if r2 < 1e-6: break
        f = X * (1 - b * b / r2) - Xs; df = (1 - b * b / r2) + 2 * X * X * b * b / (r2 * r2)
        if abs(df) < 1e-6: break
        X -= f / df
    return X * sx

def air_cause(c, t):
    """E1 16.80-20.92. A: you move DOWN through still air (world frame). B: the camera catches up and holds you:
    now the air streams UP past you (relative airflow, dots). C: the air meeting your front pushes back: the drag
    force arrow (solid teal) grows up from the centre of mass. Airflow (dots) and force (arrow) stay distinct."""
    V = 115.0                                            # screen units / s of the body before the camera locks
    t0, l0, l1 = 16.80, 17.75, 18.45
    def lock(q): return smooth((q - l0) / (l1 - l0))
    n = 40; tt = max(0.0, t - t0); cam = sum(lock(t0 + tt * (i + .5) / n) for i in range(n)) * tt / n * V
    yb = 150 + V * tt - cam                              # body on screen
    bx, A_, B_ = 180, 112, 30
    sky_plain(c)
    # air dots (behind the body)
    dot_a = ramp(t, 16.82, 17.1)
    for X0, Yw in AIR_DOTS:
        def pos(q_cam):
            ys = (Yw - q_cam) % 720 - 40
            Y = ys - yb
            return bx + deflect(X0, Y, A_, B_), ys
        x, y = pos(cam)
        if ((x - bx) / (A_ + 2)) ** 2 + ((y - yb) / (B_ + 2)) ** 2 < 1: continue
        px, py = pos(cam - V * .07 * lock(t))            # where it was 0.07 s ago (relative motion trail)
        k = dot_a * (.55 + .45 * min(1, abs(X0) / 80))
        if math.hypot(px - x, py - y) < 22 and lock(t) > .05:
            col(c, AIR, .55 * k); c.set_line_width(1.2); c.move_to(px, py); c.line_to(x, y); c.stroke()
        col(c, '#35658A', .85 * k); c.arc(x, y, 1.9, 0, 6.283); c.fill()
    cx, cy = side_rig(c, bx, yb, 280, t, amt=.25, seed=33, blink=blinking(t, (19.9,)))
    # A: you move down (velocity, dashed blue) -- shown while the air is still
    a1 = ramp(t, 16.9, 17.2) * (1 - ramp(t, 18.3, 18.6))
    vel_arrow(c, 40, yb - 30, 60, a1, t, 1.0); chip(c, 'you: down', 40, yb - 40, VEL, a1, 10, 'c')
    chip(c, 'still air', 300, 120, MUTED, a1, 10, 'c')
    # B: relative airflow
    a2 = ramp(t, 18.3, 18.7)
    chip(c, 'air, relative to you', 180, 96, AIR, a2, 12, 'c')
    chip(c, 'schematic', 180, 110, MUTED, .8 * a2, 8.5, 'c')
    # C: the push -> drag force
    g = clamp((t - 19.35) / .7)
    if g > 0:
        grow_arrow(c, cx, cy - 4, -96, DRAG, g, 6, 14)
        chip(c, 'drag: the air pushes back', cx + 12, cy - 96 + 10, DRAG, ramp(t, 19.6, 19.9), 11)
    return cx, cy

def density_box(c, t, x, y, w, h, rho, a=1.0, fill=1.0, seed=5, drift=12.0):
    """Same-size sample of air; dot count proportional to model density (schematic marks, not molecules)."""
    if a <= 0: return
    c.save(); rrect(c, x, y, w, h, 10); c.clip()
    col(c, '#FFFFFF', .92 * a); c.paint()
    rr = random.Random(seed); nmax = 170; n = int(round(rho / 1.226 * nmax * fill))
    for i in range(nmax):
        px, py = rr.uniform(4, w - 4), rr.uniform(0, h)
        if i >= n: continue
        py = (py - t * drift) % h
        col(c, '#35658A', .9 * a); c.arc(x + px, y + py, 2.0, 0, 6.283); c.fill()
    c.restore()
    col(c, AIR, a); c.set_line_width(1.5); rrect(c, x, y, w, h, 10); c.stroke()

def density_scene(c, t):
    """I1 28.63-31.42: one comparison, nothing else on screen. Two equal boxes: high/thin vs low/denser. Then the
    density effect alone: SAME speed under each box -> the drag arrow is longer in the denser air (x rho ratio)."""
    sky_plain(c)
    r_hi, r_lo = PHYS.rho(10000), PHYS.rho(600)
    a1 = ramp(t, 28.7, 29.0); a2 = ramp(t, 29.2, 29.5)
    density_box(c, t, 22, 150, 150, 150, r_hi, a1, 1)
    density_box(c, t, 188, 150, 150, 150, r_lo, a2, ease_out(clamp((t - 29.2) / .9)))
    chip(c, 'high up: thin air', 97, 138, INK, a1, 11, 'c')
    chip(c, 'lower: denser air', 263, 138, INK, a2, 11, 'c')
    a3 = ramp(t, 30.0, 30.3)
    for bx, rho in ((97, r_hi), (263, r_lo)):
        cx, cy = side_rig(c, bx, 400, 120, t, amt=.2, seed=40 + bx, alpha=a3)
        vel_arrow(c, bx - 62, 372, 46, a3, t, 1.0)
        grow_arrow(c, cx, cy - 4, -38 * rho / r_hi * .75, DRAG, clamp((t - 30.25) / .6), 5, 11)
    chip(c, 'same speed', 180, 478, VEL, a3, 10.5, 'c')
    chip(c, 'denser air: more drag', 180, 494, DRAG, ramp(t, 30.7, 31.0), 10.5, 'c')
    chip(c, 'dots are schematic, not molecules', 180, 318, MUTED, .85 * a2, 8.5, 'c')

BAR_BASE, BAR_LEN, BAR_X = 532, 280, 300
def force_bars(c, t, dw, a=1.0, gw=1.0, gd=1.0, gap_a=0.0, eq_a=0.0):
    """Option B (chosen over the V12 x30 lens): the two force sizes side by side from one baseline, one scale.
    Bars = magnitudes (no arrowheads). The bit of drag above the weight line is the net force (violet)."""
    if a <= 0: return
    lw = BAR_LEN * ease_out(gw); ld = BAR_LEN * dw * ease_out(gd)
    col(c, '#FFFFFF', .75 * a); rrect(c, BAR_X - 30, BAR_BASE - BAR_LEN - 40, 82, BAR_LEN + 70, 10); c.fill()
    col(c, INK, .6 * a); c.set_line_width(1.2); c.move_to(BAR_X - 24, BAR_BASE); c.line_to(BAR_X + 44, BAR_BASE); c.stroke()
    col(c, WEIGHT, a); c.rectangle(BAR_X - 16, BAR_BASE - lw, 14, lw); c.fill()
    col(c, DRAG, a); c.rectangle(BAR_X + 20, BAR_BASE - ld, 14, ld); c.fill()
    chip(c, 'weight', BAR_X - 9, BAR_BASE + 13, WEIGHT, a * ramp(gw, .5, 1), 8.5, 'c')
    chip(c, 'drag', BAR_X + 27, BAR_BASE + 13, DRAG, a * ramp(gd, .5, 1), 8.5, 'c')
    if gw >= 1:   # weight line carried across
        col(c, WEIGHT, .9 * a); c.set_line_width(1.2); c.set_dash([3, 2])
        c.move_to(BAR_X - 22, BAR_BASE - lw); c.line_to(BAR_X + 40, BAR_BASE - lw); c.stroke(); c.set_dash([])
    if gap_a > 0 and ld > lw + .3:
        col(c, NET, gap_a * a); c.rectangle(BAR_X + 20, BAR_BASE - ld, 14, ld - lw); c.fill()
    if eq_a > 0: chip(c, 'equal', BAR_X + 10, BAR_BASE - lw - 9, INK, eq_a * a, 9.5, 'c')

# ---------------------------------------------------------------- model time map (film -> model seconds)
MODEL_MAP = [(20.92, 0), (24.89, 0.6), (28.63, 12), (33.67, 14), (38.72, 14), (42.0, 17.5), (43.6, 20), (46.6, 27),
             (47.71, 30), (55.57, 60), (57.16, 90), (59.35, 130), (61.93, 142), (70.53, 148), (78.2, 150)]
def model_t(t):
    if t < MODEL_MAP[0][0]: return None
    for (a, ma), (b, mb) in zip(MODEL_MAP, MODEL_MAP[1:]):
        if t <= b: return lerp(ma, mb, (t - a) / (b - a))
    return MODEL_MAP[-1][1]
def state(tm):
    t, h, v, dw, rho = PHYS.at_time(tm or 0.0); return h, v, dw, rho

# ---------------------------------------------------------------- shots (narration timing unchanged)
SHOTS = [
 ('A1', 0.00, 3.30, 'establish', 'V13 opening on the V11 composition: A establish (aircraft upper-middle, figure below), B follow (tilt with the figure), C approach (layered dolly-in)'),
 ('A2', 3.30, 5.22, 'rear', 'D reveal: direct cut behind the faller (bare hands), slow push, closed pack circled once'),
 ('B1', 5.22, 8.33, 'gravity', 'Side tracking; weight arrow draws on from the centre of mass'),
 ('B2', 8.33, 9.70, 'lift', 'Purposeful action: forearm lifts, head turns to the wrist; camera pushes toward the wrist'),
 ('B3', 9.70, 11.15, 'wrist', 'Motivated close-up of the attached device; needle eases down'),
 ('C1', 11.15, 12.52, 'reaction', '"Wait, what?": head snaps up from the wrist, blink, arm returns; quick push on the face'),
 ('D1', 12.52, 16.80, 'questions', 'Gravity unchanged (arrow re-measured against a tick); air rushes past'),
 ('E1', 16.80, 20.92, 'air', 'Cause and effect: you move down through still air -> camera holds you, air streams up past you -> drag arrow grows'),
 ('F1', 20.92, 23.14, 'reset', 'MODEL intro: world freezes, frame draws in; altitude ruler; at rest'),
 ('G1', 23.14, 24.89, 'thin', 'Thin-air box beside the body (same box as I1), no force diagram'),
 ('H1', 24.89, 28.63, 'accelerate', 'Weight long, drag short and growing; speed arrow grows; world speeds up'),
 ('I1', 28.63, 31.42, 'denser', 'Two equal boxes: thin vs denser air; then same speed under each -> longer drag in denser air'),
 ('I2', 31.42, 33.67, 'drag_grows', 'Camera eases in; drag arrow closes on weight; relative airflow'),
 ('J1', 33.67, 38.72, 'compare', 'Same air, same posture (fixed box): speed x2 -> drag x4, ghost of the x1 arrow'),
 ('K1', 38.72, 46.60, 'cross', 'Arrows grow to equal (balanced: still falling); bars side by side on one scale; drag bar passes weight line; push in; net force up'),
 ('K2', 46.60, 47.71, 'think', 'Lens closes; dashed DOWN still there'),
 ('L1', 47.71, 52.19, 'positions', 'One descending trail, a mark every 10 s, one scale: gaps grow then shrink; net UP, moving DOWN'),
 ('M1', 52.19, 55.35, 'slowing', 'Context; speed arrow shortening; the wrist lifts again'),
 ('N1', 55.35, 57.16, 'pov_dial', 'Own forearm (first person), push-in, needle falling'),
 ('O1', 57.16, 59.35, 'pov_ground', 'Tilt from the wrist to the approaching ground'),
 ('P1', 59.35, 61.93, 'pack', 'Behind: pack still closed (held beat)'),
 ('Q1', 61.93, 66.03, 'graph', 'Graph builds: axes, zero, rise, top speed, fall that stays above zero'),
 ('Q2', 66.03, 70.53, 'recap_forces', 'Bars again: drag slightly larger than weight (push in), then still moving down'),
 ('R1', 70.53, 74.52, 'pullback', 'Pull back; model frame + assumptions line'),
 ('S1', 74.52, 78.20, 'conditions', 'Graph returns; other inputs drawn on as the narration names them'),
]
SHOT_OBJS = [dict(id=i, start=a, end=b, kind=k, purpose=p, start_frame=round(a * FPS), end_frame=round(b * FPS))
             for i, a, b, k, p in SHOTS]
def shot_at(t):
    f = round(t * FPS)
    for s in SHOT_OBJS:
        if s['start_frame'] <= f < s['end_frame']: return s
    return SHOT_OBJS[-1]

def model_frame(c, a, t):
    """Model framing: thin rounded frame + small 'MODEL' tab; drawn in (trim) when introduced."""
    if a <= 0: return
    c.save(); col(c, VEL, .55 * a); c.set_line_width(1.2)
    rrect(c, 10, 14, 340, 612, 12); c.stroke()
    col(c, VEL, .9 * a); rrect(c, 22, 8, 52, 14, 5); c.fill()
    chip(c, 'MODEL', 48, 18.5, '#FFFFFF', a, 8.5, 'c'); c.restore()

# ---------------------------------------------------------------- per-shot drawing
def draw(c, t):
    s = shot_at(t); k = s['kind']; u = clamp((t - s['start']) / (s['end'] - s['start'])); lt = t - s['start']
    tm = model_t(t)
    if k == 'establish':
        opening(c, t)
    elif k == 'rear':
        # D REVEAL: direct cut behind the faller (no cloud wipe); slow push; the closed pack is circled once
        cam = Cam(9990 - 20 * lt, 62, 520, cy=300)
        environment(c, cam); air_streaks(c, t, 120, .4, count=26)
        zz = lerp(1.0, 1.1, ease_io(u))
        c.save(); push(c, 180, 290, zz)
        x, y = 180 + 3 * math.sin(t * .9), 300 + 3 * math.sin(t * 1.3)
        body(c, 'back', x, y, 300, t, .8, 5)
        a = ramp(t, 3.75, 4.05) * (1 - ramp(t, 4.95, 5.2))
        col(c, '#FFFFFF', .95 * a); c.set_line_width(2); c.set_dash([5, 4]); c.arc(x, y - 8, 46 + 8 * (1 - a), 0, 6.283); c.stroke(); c.set_dash([])
        c.restore()
        chip(c, 'parachute: closed', 180, 430, INK, a, 12, 'c')
    elif k in ('gravity', 'questions'):
        tracking_bg(c, t, 9300, 60, streak_alpha=.5)
        cx, cy = side_rig(c, 172, 290, 330, t, nod=wobble(t, .2, 4, 1), blink=blinking(t, (6.9, 14.0, 15.9)), seed=9)
        g = clamp((t - 5.5) / .5)
        forces(c, cx, cy, 0, gw=g, gd=0)
        chip(c, 'gravity', cx + 10, cy + 70, WEIGHT, ramp(t, 5.9, 6.2) * (1 - ramp(t, 8.0, 8.3)), 11)
        if k == 'questions':   # "did gravity change?": re-measure against a fixed tick, same length
            a = ramp(t, 12.9, 13.2) * (1 - ramp(t, 14.4, 14.7))
            col(c, INK, .8 * a); c.set_line_width(1.2)
            for yy in (cy + 3, cy + 3 + L_W): c.move_to(cx - 30, yy); c.line_to(cx - 18, yy); c.stroke()
            q = ease_io(clamp((t - 13.1) / .6)); c.move_to(cx - 24, cy + 3); c.line_to(cx - 24, cy + 3 + L_W * q); c.stroke()
            chip(c, 'same', cx - 32, cy + 64, INK, a * ramp(t, 13.6, 13.8), 9.5, 'r')
            # "air grow brakes?": a quick gust of streaks past the body
            air_streaks(c, t, 520, .7 * ramp(t, 14.4, 14.8) * (1 - ramp(t, 16.2, 16.6)), seed=21, count=26)
    elif k == 'lift':
        tracking_bg(c, t, 9200, 62, streak_alpha=.45)
        z = lerp(1.0, 1.7, ease_io((t - 8.55) / 1.1)); c.save(); push(c, 258, 316, z)
        side_rig(c, 172, 290, 330, t, lift=lift_curve(t, 8.4), glance=ramp(t, 8.62, 8.78), seed=9)
        c.restore()
        col(c, '#FFFFFF', ramp(t, 9.5, 9.7)); c.paint()          # quick white flash into the close-up (match on the dial)
    elif k == 'wrist':
        uu = clamp(lt / 1.45)
        cam = Cam(9000, 8, 430, cy=330); environment(c, cam); air_streaks(c, t, 260, .4)
        z = lerp(1.25, 2.3, ease_io(uu)); v = lerp(74, 66, ease_io((uu - .2) / .7))
        fx, fy = 196, 318
        c.save(); push(c, fx, fy, z)
        I.wrist(c, 'mounted', fx + 2 * math.sin(t * 1.3), fy + 1.5 * math.sin(t * 1.7), 640, v, 1, rot=-4, detail=clamp((z - 1.3) / .6))
        c.restore()
        col(c, '#FFFFFF', 1 - ramp(t, 9.7, 9.9)); c.paint()
    elif k == 'reaction':
        tracking_bg(c, t, 9100, 62, streak_alpha=.5)
        q = lt
        z = lerp(1.7, 2.2, ease_out(clamp(q / .35))); fx, fy = 196, 262      # face centred (head at canvas ~1400,300)
        c.save(); push(c, fx, fy, z)
        side_rig(c, 120, 297, 330, t, lift=1 - ease_io((q - .25) / .45), glance=1 - ramp(t, 11.25, 11.33),
                 nod=-1 * ease_out(clamp((q - .1) / .2)), blink=blinking(t, (11.62, 11.95)), seed=9)
        c.restore()
    elif k == 'air':
        air_cause(c, t)
    elif k == 'denser':
        density_scene(c, t)
    elif k in ('reset', 'thin', 'accelerate', 'drag_grows', 'cross', 'think', 'slowing', 'recap_forces'):
        model_scene(c, t, k, tm, u, s)
    elif k == 'compare':
        compare_scene(c, t, s)
    elif k == 'positions':
        positions_demo(c, t, s['start'], tm)
    elif k == 'pov_dial':
        pov_shot(c, t, s['start'], s['end'] - s['start'], model_t(s['start']), model_t(s['end']), 'dial')
    elif k == 'pov_ground':
        pov_shot(c, t, s['start'], s['end'] - s['start'], model_t(s['start']), model_t(s['end']), 'ground')
    elif k == 'pack':
        h, v, dw, rho = state(tm)
        cam = Cam(h, 70, 380, cy=300); environment(c, cam); air_streaks(c, t, 4.5 * v, .45, count=30)
        zz = lerp(1.0, 1.18, ease_io((t - 60.4) / 1.3))
        c.save(); push(c, 180, 270, zz); body(c, 'back', 180, 300, 330, t, .7, 31); c.restore()
    elif k == 'graph':
        h, v, dw, rho = state(tm)
        tracking_bg(c, t, h, v, streak_alpha=.2)
        col(c, '#F3F6F8', .82 * ramp(t, 61.95, 62.3)); c.paint()
        speed_graph(c, t, 62.1, PHYS.END_T * ease_io(clamp((t - 62.4) / 3.0)) ** 1.0, 1, axes=clamp((t - 61.95) / .45))
    elif k == 'pullback':
        h, v, dw, rho = state(tm)
        z = ease_io(u)
        cam = Cam(h + lerp(0, 700, z), lerp(0, 8, z), lerp(700, 380, z), cy=lerp(300, 260, z), z=-lerp(870, 7000, z))
        environment(c, cam)
        p = cam.proj(0, h, 0)
        if p: side_rig(c, p[0], p[1], cam.F * 1.8 / p[2] / 2.9 * 440, t, amt=.3, seed=51)
        a = ramp(t, 70.8, 71.3)
        model_frame(c, a, t)
        chip(c, 'fixed posture · standard air · no wind', 180, 600, VEL, ramp(t, 71.6, 72.0), 10, 'c')
    elif k == 'conditions':
        cam = Cam(1200 - 160 * u, 6, 380, cy=250, z=420 * u); environment(c, cam); air_streaks(c, t, 120, .3)
        col(c, '#F3F6F8', .82); c.paint()
        if not PHYS_ALT:
            PHYS_ALT[1.6] = sim_alt(1.6); PHYS_ALT[.7] = sim_alt(.7)
        a1 = clamp((t - 75.2) / 1.0); a2 = clamp((t - 76.0) / 1.0)
        speed_graph(c, t, 74.5, PHYS.END_T, 1, marks=0, alt=[('smaller drag area', .7, a1, -12), ('larger drag area', 1.6, a2, 20)])
        chip(c, 'UNREASONABLY EXACT', 180, 610, MUTED, ramp(t, 77.0, 77.5) * .8, 8, 'c')
    if CAPTIONS: caption(c, t)

def model_scene(c, t, k, tm, u, s):
    h, v, dw, rho = state(tm)
    still = k == 'reset'
    Zb = 1.0     # motivated push toward the bar tops (cross / recap): a real camera move, both bars scale together
    if k == 'cross': Zb = 1 + 1.25 * ease_io((t - 44.1) / 1.0) * (1 - ease_io((t - 46.05) / .5))
    if k == 'recap_forces': Zb = 1 + 1.6 * ease_io((t - 67.2) / 1.0) * (1 - ease_io((t - 68.95) / .6))
    # push toward the bar tops; as it zooms the tops travel to (200, 230) so the labels stay inside the frame
    zq = (Zb - 1) / max(.01, (2.25 if k == 'cross' else 2.6) - 1)
    P = (BAR_X + 9, BAR_BASE - BAR_LEN); Q = (lerp(P[0], 205, zq), lerp(P[1], 250, zq))
    c.save(); c.translate(*Q); c.scale(Zb, Zb); c.translate(-P[0], -P[1])
    tracking_bg(c, t, h, 0 if still else v, streak_alpha=.42 if not still else 0, wisps=not still)
    x, y, w = 160, 330, 300
    zz = 1.0
    if k in ('reset', 'thin'): zz = 1 + .05 * ease_io((t - 20.92) / 3.97)      # slow creep: a held frame never fully stops
    if k == 'drag_grows': zz = lerp(1.0, 1.12, ease_io(u))
    if k == 'cross': zz = lerp(1.12, 1.0, ease_io((t - 38.72) / .8))
    fx, fy = x, y - 3 - L_W
    c.save(); push(c, fx, fy, zz)
    if k == 'drag_grows':
        paths = stream_paths(x, y, 120, 32, n=10, span=150)
        airflow(c, paths, t, 4 * v, 1, .5, 'back')
    lift = lift_curve(t, 54.35) if k == 'slowing' else 0
    cx, cy = side_rig(c, x, y, w, t, amt=.15 if still else .35, seed=61, lift=lift, glance=ramp(t, 54.55, 54.7) if k == 'slowing' else 0,
                      blink=blinking(t, (22.2, 30.1, 37.0, 44.9, 50.6, 53.1, 68.3)))
    gw = 1.0; gd = 1.0
    if k == 'reset': gw = gd = 0
    if k == 'thin': gw = gd = 0                      # density only: no force diagram yet
    if k == 'accelerate': gw = clamp((t - 24.95) / .45); gd = clamp((t - 25.6) / .5)
    lab = 0
    if k == 'accelerate': lab = ramp(t, 25.1, 25.4) * (1 - ramp(t, 27.6, 28.0))
    if k == 'recap_forces': gw = gd = clamp((t - 66.1) / .5)
    if k in ('think', 'slowing'): gw = gd = 1 - ramp(t, s['start'], s['start'] + .3)
    forces(c, cx, cy, dw if gd > 0 else 0, gw, gd, 1, lab)
    if k in ('accelerate', 'drag_grows', 'think', 'slowing', 'recap_forces', 'cross'):
        va = 1.0
        if k == 'accelerate': va = ramp(t, 26.7, 27.0)
        if k == 'recap_forces': va = ramp(t, 69.7, 70.0)
        if k == 'cross': va = 1.0
        vel_arrow(c, cx - 70 if k != 'think' else cx, cy + 34, v, va, t)
        if k in ('think', 'recap_forces'): chip(c, 'still moving down', cx + 12, cy + 100, VEL, va * ramp(t, s['start'] + .2, s['start'] + .5) if k == 'think' else va, 10.5)
    c.restore()
    if k == 'cross':
        ba = ramp(t, 40.3, 40.6)
        force_bars(c, t, dw, ba, clamp((t - 40.35) / .5), clamp((t - 40.75) / .5),
                   gap_a=ramp(t, 43.75, 44.1), eq_a=ramp(t, 43.3, 43.5) * (1 - ramp(t, 43.9, 44.1)))
        chip(c, 'side by side, one scale', BAR_X + 10, BAR_BASE - BAR_LEN - 22, MUTED, ba * (1 - ramp(t, 43.0, 43.3)), 8.5, 'c')
        chip(c, 'net force: up', BAR_X - 24, BAR_BASE - BAR_LEN * (dw + 1) / 2 + 3, NET, ramp(t, 44.6, 44.9) * (1 - ramp(t, 46.1, 46.4)), 5, 'r')
        chip(c, 'balanced: still falling', cx - 70, cy + 132, VEL, ramp(t, 43.3, 43.6) * (1 - ramp(t, 43.95, 44.2)), 9.5, 'c')
    if k == 'recap_forces':
        ga = clamp((t - 66.3) / .5)
        force_bars(c, t, dw, ramp(t, 66.2, 66.5), ga, ga, gap_a=ramp(t, 67.0, 67.3))
        chip(c, 'net force: up', BAR_X - 24, BAR_BASE - BAR_LEN * (dw + 1) / 2 + 2, NET, ramp(t, 67.6, 67.9) * (1 - ramp(t, 68.6, 68.9)), 4.5, 'r')
    if k == 'slowing':
        chip(c, 'slower', cx - 70, cy + 34 + 8 + .75 * v + 16, VEL, ramp(t, 52.6, 52.9) * (1 - ramp(t, 54.2, 54.4)), 10, 'c')
        col(c, '#FFFFFF', ramp(t, 55.15, 55.35)); c.paint()      # flash cut into first person
    # model chrome: frame introduced once, then just the small tab; altitude ruler
    fa = ramp(t, 21.0, 21.5)
    intro = ramp(t, 21.0, 21.4) * (1 - ramp(t, 22.6, 23.0))
    if k == 'reset':
        col(c, VEL, .55 * fa); c.set_line_width(1.2); c.save(); rrect(c, 10, 14, 340, 612, 12); c.restore()
        c.save(); c.rectangle(0, 0, 360 * ease_io((t - 21.0) / .7), 640); c.clip(); rrect(c, 10, 14, 340, 612, 12); c.stroke(); c.restore()
        chip(c, 'starts at rest · fixed posture', 180, 96, VEL, intro, 11, 'c')
    if k == 'reset' or True:
        col(c, VEL, .9 * fa); rrect(c, 22, 8, 52, 14, 5); c.fill(); chip(c, 'MODEL', 48, 18.5, '#FFFFFF', fa, 8.5, 'c')
    if k in ('reset', 'accelerate', 'drag_grows', 'slowing'):
        ry = alt_ruler(c, h, ramp(t, 21.3, 21.8))
    if k == 'thin':      # the same box used for the thin/denser comparison (I1), alone on screen with the body
        a = ramp(t, 23.2, 23.5)
        density_box(c, t, 22, 110, 150, 150, rho, a, 1)
        chip(c, 'up here: thin air', 97, 98, INK, a, 11, 'c')
    if k == 'denser':
        for i, hh in enumerate((10000, 5000, 600)):
            a = ramp(t, 28.8 + i * .5, 29.1 + i * .5)
            yy = 560 - 442 * hh / 10000
            r = 30 * ease_out(clamp((t - 28.8 - i * .5) / .3))
            col(c, AIR, .6 * a); c.set_line_width(.8); c.move_to(334, yy); c.line_to(300, yy); c.stroke()
            air_lens(c, t, 266, min(yy, 520), r + .1, PHYS.rho(hh), v, a, seed=4)
        chip(c, 'denser lower down', 266, 600, AIR, ramp(t, 30.2, 30.5), 9.5, 'c')
    c.restore()

def compare_scene(c, t, s):
    """Same air (density fixed), same body: speed sweeps x1 -> x2 and the drag arrow follows speed squared."""
    tracking_bg(c, t, 7000, 70, streak_alpha=0, wisps=False)
    q = ease_io(clamp((t - 34.3) / 2.6)); k = 1 + q            # speed factor 1 -> 2
    air_streaks(c, t, 140 * k, .65, count=26, seed=8)
    cx, cy = side_rig(c, 180, 330, 270, t, amt=.3, seed=70)
    vel_arrow(c, 60, cy - 30, 40 * k, ramp(t, 33.8, 34.1), t, 1)
    dl = 24 * k * k
    arrow(c, cx, cy - 4, 0, -dl, DRAG, 5, 12, alpha=ramp(t, 33.8, 34.1))
    chip(c, 'speed ×%.1f' % k if k < 1.995 else 'speed ×2', 72, cy - 30 + 40 * k + 26, VEL, ramp(t, 34.3, 34.6), 10.5, 'c')
    chip(c, 'drag ×%.1f' % (k * k) if k < 1.995 else 'drag ×4', cx + 12, cy - dl + 8, DRAG, ramp(t, 34.3, 34.6), 10.5)
    # the fixed condition, stated once and shown: one air sample that never changes + same posture
    fa = ramp(t, 33.75, 34.1)
    density_box(c, t, 262, 44, 76, 76, PHYS.rho(7000), fa, 1, seed=9, drift=6 * k)
    chip(c, 'same air', 300, 134, AIR, fa, 10, 'c'); chip(c, 'same posture', 300, 148, MUTED, fa, 9, 'c')
    if q > .02:   # ghost of the x1 drag arrow for comparison
        col(c, DRAG, .35); c.set_line_width(1.2); c.set_dash([3, 3]); c.move_to(cx + 14, cy - 4); c.line_to(cx + 14, cy - 28); c.stroke(); c.set_dash([])
    col(c, VEL, .9); rrect(c, 22, 8, 52, 14, 5); c.fill(); chip(c, 'MODEL', 48, 18.5, '#FFFFFF', 1, 8.5, 'c')

TRAIL_T = [10 * i for i in range(16)]          # model seconds, one mark every 10 s
TRAIL_SCALE = .085                             # units per metre (one common scale for every gap)
def positions_demo(c, t, t0, tm):
    """One descending trail from the model, a mark every 10 s on ONE scale. The camera follows the newest mark.
    Gaps grow (speeding up, 0-20 s) then shrink (slowing, after ~20 s). Every mark is lower: moving DOWN."""
    h, v, dw, rho = state(tm)
    tracking_bg(c, t, h, 0, streak_alpha=0, wisps=False); col(c, '#EEF3F7', .78); c.paint()
    hs = [PHYS.at_time(q)[1] for q in TRAIL_T]
    ys = [80 + (10000 - hh) * TRAIL_SCALE for hh in hs]          # world-y in units
    # reveal: first 4 marks (0..30 s) appear quickly, the rest one per ~0.3 s
    n = 1 + int(clamp((t - t0 - .15) / .6) * 3) + int(clamp((t - t0 - .9) / 3.2) * 12)
    n = min(n, len(ys))
    yc = ys[n - 1]
    camy = lerp(0, max(0, yc - 470), ease_io(clamp((t - t0 - .5) / 3.6)))
    c.save(); c.translate(0, -camy)
    x = 190
    col(c, INK, .35); c.set_line_width(1); c.move_to(x - 70, ys[0]); c.line_to(x - 70, ys[n - 1]); c.stroke()
    for i in range(n):
        yy = ys[i]; last = i == n - 1
        c.save(); c.push_group(); side_rig(c, x, yy, 92, t if last else 0, amt=.2, seed=80); c.pop_group_to_source()
        c.paint_with_alpha(1 if last else .38); c.restore()
        col(c, INK, .8); c.arc(x - 70, yy, 2.6, 0, 6.283); c.fill()
        if i:
            g = ys[i] - ys[i - 1]
            hue = WEIGHT if TRAIL_T[i] <= 20 else DRAG
            col(c, hue, .9); c.set_line_width(3); c.move_to(x - 82, ys[i - 1] + 4); c.line_to(x - 82, yy - 4); c.stroke()
    if n > 2: chip(c, 'gaps grow', x - 90, (ys[1] + ys[2]) / 2 + 4, WEIGHT, ramp(t, t0 + .5, t0 + .8), 10, 'r')
    if n > 8: chip(c, 'gaps shrink', x - 90, (ys[n - 2] + ys[n - 1]) / 2 + 4, DRAG, ramp(t, t0 + 2.6, t0 + 2.9), 10, 'r')
    last_y = ys[n - 1]
    if TRAIL_T[n - 1] > 20:
        arrow(c, x + 92, last_y + 24, 0, -50, NET, 5, 11, alpha=ramp(t, 49.5, 49.9), double=True)
        chip(c, 'net force', x + 100, last_y - 6, NET, ramp(t, 49.6, 50.0), 9.5)
        vel_arrow(c, x + 70, last_y + 14, 40, ramp(t, 47.9, 48.2), t, 1)
    c.restore()
    # fixed legend (one line) + small clock pulse on every new mark
    chip(c, 'a mark every 10 s · one scale', 180, 600, MUTED, ramp(t, t0, t0 + .3), 9.5, 'c')
    col(c, VEL, .9); rrect(c, 22, 8, 52, 14, 5); c.fill(); chip(c, 'MODEL', 48, 18.5, '#FFFFFF', 1, 8.5, 'c')
