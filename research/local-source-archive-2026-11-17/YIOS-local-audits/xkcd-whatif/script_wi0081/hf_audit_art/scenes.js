// WI-0081 v2: every mark is code. Times are voiceover word times (video/wordlist.json). 1-frame pops, no overshoot, no idle loops.
const NS = "http://www.w3.org/2000/svg", world = document.getElementById("world");
const tl = gsap.timeline({ paused: true });
const E = (p, tag, a = {}, cls = "") => { const e = document.createElementNS(NS, tag); for (const k in a) e.setAttribute(k, a[k]); if (cls) e.setAttribute("class", cls); p.appendChild(e); return e; };
const G = (p, cls = "") => E(p, "g", {}, cls);
const P = (p, d, cls = "l") => E(p, "path", { d }, cls + " h");
const D = (p, d, cls = "l") => E(p, "path", { d, pathLength: 1 }, cls + " d h");
const TX = (p, x, y, s, size = 64, cls = "") => { const t = E(p, "text", { x, y, "font-size": size }, cls + " h"); t.textContent = s; return t; };
const pop = (el, t) => { tl.set(el, { opacity: 1 }, t); return el; };
const off = (el, t) => { tl.set(el, { opacity: 0 }, t); return el; };
const draw = (el, t, d = 0.2) => { tl.set(el, { opacity: 1 }, t); tl.fromTo(el, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: d, ease: "none" }, t); return el; };
const scene = (a, b) => { const g = G(world, "sc"); tl.set(g, { opacity: 1 }, a); tl.set(g, { opacity: 0 }, b); return g; };
const show = (g, t) => { for (const c of g.children) pop(c, t); }; // reveal all children of a group at t
const arrow = (p, x1, y1, x2, y2, cls = "l", hd = 22) => { const a = Math.atan2(y2 - y1, x2 - x1), h = (k) => `${x2 - hd * Math.cos(a + k)} ${y2 - hd * Math.sin(a + k)}`; return P(p, `M${x1} ${y1} L${x2} ${y2} M${h(0.5)} L${x2} ${y2} L${h(-0.5)}`, cls); };
const wave = (x, y, h) => `M${x} ${y} C${x - 22} ${y - h * 0.25} ${x + 22} ${y - h * 0.5} ${x} ${y - h * 0.75} S${x - 18} ${y - h * 0.95} ${x} ${y - h}`;

// ---------- reusable objects ----------
function mug(p, cx, rim, s) {
  const X = (x) => cx + (x - 410) * s, Y = (y) => rim + (y - 900) * s;
  const tp = (d) => d.replace(/(-?\d+\.?\d*)\s+(-?\d+\.?\d*)/g, (m, a, b) => X(+a) + " " + Y(+b));
  const g = G(p);
  const w = P(g, tp("M272 950 L286 1236 Q292 1262 322 1262 L498 1262 Q528 1262 534 1236 L548 950 Z"), "g"); w.setAttribute("stroke", "none");
  const surf = E(g, "ellipse", { cx: X(410), cy: Y(950), rx: 138 * s, ry: 20 * s }, "g h");
  P(g, tp("M270 900 C268 1000 272 1150 286 1238 Q292 1262 322 1262 L498 1262 Q528 1262 534 1238 C548 1150 552 1000 550 900"));
  P(g, tp("M548 960 C650 948 650 1140 536 1150"));
  E(g, "ellipse", { cx: X(410), cy: Y(900), rx: 140 * s, ry: 22 * s }, "l h");
  return { g, X, Y, tp, s, cx, rim, surf, items: [...g.children] };
}
function spoon(p, m, bowl = 1100) {
  const g = G(p);
  P(g, `M${m.X(410)} ${m.Y(730)} L${m.X(410)} ${m.Y(bowl - 34)}`);
  E(g, "ellipse", { cx: m.X(410), cy: m.Y(bowl), rx: 24 * m.s, ry: 36 * m.s }, "f h");
  for (const c of g.children) c.classList.remove("h");
  g.setAttribute("class", "h");
  return g;
}
// Stirred liquid, side view. Real physics: the fluid spins up behind the spoon (lag), the free surface becomes a paraboloid
// h(r)=D*(r^2/R^2-0.5) with D ~ w^2 (dip in the centre, rise at the wall), the spoon pushes a tilted wave that travels round,
// tracer specks (tea leaves) circle on ellipses: front half one way, back half the other. All a pure function of timeline time.
function stir(g, m, t0, t1, amp = 14, o = {}) {
  const rev = o.rev || 1.6, str = o.str ?? 1, s = m.s, cx = m.cx, ys = m.Y(950), R = 136 * s, k = 0.15;
  const W0 = rev * 2 * Math.PI, REF = 1.6 * 2 * Math.PI, TS = 0.25, TF = 1.3, DMAX = 34 * s * str;
  const ox = m.X(410), oy = m.Y(900);
  const wg = G(g.parentNode); g.parentNode.insertBefore(wg, g); wg.setAttribute("class", "h"); pop(wg, t0);
  tl.set(m.surf, { opacity: 0 }, t0);
  const at = { "stroke": "#111", "stroke-linejoin": "round", "stroke-linecap": "round" };
  tl.set(m.items[0], { opacity: 0 }, t0);
  const body = E(wg, "path", { fill: "#C4C4C4", stroke: "none" });
  const side = E(wg, "path", { fill: "none", "stroke-width": 7, ...at });
  const top = E(wg, "path", { fill: "#E4E4E4", "stroke-width": 7, ...at });
  const ring1 = E(wg, "path", { fill: "none", "stroke-width": 4, ...at });
  const ring2 = E(wg, "path", { fill: "#C4C4C4", "stroke-width": 4, ...at });
  const N = 7, fr = [0.3, 0.8, 0.5, 0.72, 0.4, 0.88, 0.62], ph = [0.2, 1.1, 2.3, 3.0, 4.1, 5.0, 5.7];
  const dots = fr.map(() => E(wg, "circle", { r: 7 * Math.max(0.8, s), fill: "#111" }));
  const deep = [[0.7, 70, 0.5], [0.3, 95, 2.0], [0.85, 125, 3.6], [0.5, 150, 5.2], [0.65, 185, 1.2], [0.25, 205, 4.4], [0.8, 235, 2.9], [0.45, 255, 0.1]].map(([f, dy, p0]) => ({ f, dy: dy * s, p0, c: E(wg, "circle", { r: 7 * Math.max(0.8, s), fill: "#111" }) }));
  const wallPath = m.tp("L286 1236 Q292 1262 322 1262 L498 1262 Q528 1262 534 1236");
  const spin = (tt, T) => W0 * (tt - T * (1 - Math.exp(-tt / T))); // angle after spin-up with time constant T
  const ts0 = o.stop != null ? o.stop - t0 : 1e9, TAU = 0.9;
  const upd = (tt0) => {
    const YS = ys + (o.lvl ? o.lvl(tt0 + t0) : 0);
    const tt = tt0 <= ts0 ? tt0 : ts0 + TAU * (1 - Math.exp(-(tt0 - ts0) / TAU)), dk = tt0 <= ts0 ? 1 : Math.exp(-(tt0 - ts0) / 1.2);
    const kk = o.kf ? o.kf(tt0 + t0) : 1;
    const Ts = spin(tt, TS), Tf = spin(tt, TF), wf = W0 * (1 - Math.exp(-tt / TF));
    const D = Math.min(1.5, (wf / REF) ** 2) * DMAX * (1 + 0.5 * (kk - 1)) * dk, A = 0.3 * D * Math.min(1, tt / 0.4);
    const env = amp * kk * Math.min(1, tt / 0.3), ang = env * Math.cos(Ts);
    g.setAttribute("transform", `rotate(${ang} ${ox} ${oy})`);
    if (o.hook) o.hook(ang, env * Math.cos(Ts + 0.45)); // hand leads the spoon
    const ring = (f, close) => { let d = ""; const r = f * R;
      for (let j = 0; j <= 40; j++) { const p = j / 40 * 2 * Math.PI;
        const x = cx + r * Math.cos(p), y = YS - D * (f * f - 0.5) + k * r * Math.sin(p) - A * f * Math.cos(p - Ts + 0.9);
        d += (j ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1); } return d + "Z"; };
    // water body: bottom of the mug, then up to the right wall and back along the front arc of the surface
    let fa = ""; for (let j = 0; j <= 40; j++) { const p = j / 40 * Math.PI, x = cx + R * Math.cos(p), y = YS - 0.5 * D + k * R * Math.sin(p) - A * Math.cos(p - Ts + 0.9); fa += "L" + x.toFixed(1) + " " + y.toFixed(1); }
    const yl = YS - 0.5 * D - A * Math.cos(Math.PI - Ts + 0.9);
    
    body.setAttribute("d", `M${(cx - R).toFixed(1)} ${yl.toFixed(1)} ${wallPath} L${(cx + R).toFixed(1)} ${(YS - 0.5 * D - A * Math.cos(-Ts + 0.9)).toFixed(1)} ${fa.split("L").reverse().filter(Boolean).map((q) => "L" + q).join(" ")} Z`);
    top.setAttribute("d", ring(0.97)); ring1.setAttribute("d", ring(0.6)); ring2.setAttribute("d", ring(0.27));
    deep.forEach((o2) => { const r = o2.f * R, p = o2.p0 + Tf * (1 - 0.35 * o2.dy / (255 * s)), sz = 1 + 0.25 * Math.sin(p);
      o2.c.setAttribute("cx", (cx + r * Math.cos(p)).toFixed(1)); o2.c.setAttribute("cy", (YS + o2.dy + k * r * Math.sin(p)).toFixed(1)); o2.c.setAttribute("r", (7 * Math.max(0.8, s) * sz).toFixed(1)); });
    dots.forEach((c, i) => { const f = fr[i], r = f * R, p = ph[i] + Tf * (1 + 0.4 * (0.6 - f));
      c.setAttribute("cx", (cx + r * Math.cos(p)).toFixed(1));
      c.setAttribute("cy", (YS - D * (f * f - 0.5) + k * r * Math.sin(p) - A * f * Math.cos(p - Ts + 0.9) + 4).toFixed(1)); });
  };
  upd(0); const px = { t: 0 };
  tl.to(px, { t: t1 - t0, duration: t1 - t0, ease: "none", onUpdate: () => upd(px.t) }, t0);
  if (o.restore) { tl.set(wg, { opacity: 0 }, t1); tl.set(m.surf, { opacity: 1 }, t1); tl.set(m.items[0], { opacity: 1 }, t1); }
  return { wg };
}
const TEAL = "#2F9E9E", AMB = "#E09A12", VIO = "#6B5FBF", MINT = "#DDF5E0";
const ink = (el, c, w) => { el.style.stroke = c; if (w) el.style.strokeWidth = w; return el; };
// code-drawn alien arm + hand gripping the spoon top; the hand leads the spoon a little (wrist leads, spoon follows)
function arm(S, m, t0, t1) {
  const hx0 = m.X(410), hy0 = m.Y(730), ox = m.X(410), oy = m.Y(900);
  const ap = P(S, "M0 0", "l"), hand = E(S, "circle", { r: 30, cx: hx0, cy: hy0 }, "l h"); hand.style.fill = MINT;
  const upd = (ang) => { const a = ang * Math.PI / 180, dx = hx0 - ox, dy = hy0 - oy, hx = ox + dx * Math.cos(a) - dy * Math.sin(a), hy = oy + dx * Math.sin(a) + dy * Math.cos(a);
    hand.setAttribute("cx", hx.toFixed(1)); hand.setAttribute("cy", hy.toFixed(1));
    ap.setAttribute("d", `M${hx.toFixed(1)} ${(hy + 28).toFixed(1)} C${(hx - 150).toFixed(1)} ${hy + 90} 60 ${hy + 120} 80 ${hy + 560} S 90 1690 200 1712`); };
  upd(0); pop(ap, t0); pop(hand, t0); off(ap, t1); off(hand, t1);
  return { upd, hand };
}
function stirArm(S, m, sp, t0, t1, amp, o = {}) {
  let A = null; const r = stir(sp, m, t0, t1, amp, { ...o, hook: (a, ah) => A && A.upd(ah) });
  A = arm(S, m, o.armStart ?? t0, o.armEnd ?? t1); return { A, ...r };
}
function thermo(p, x, y100, y0, level, ticks = true) {
  const g = G(p), Yc = (c) => y0 + (y100 - y0) * c / 100, yb = y0 + 42;
  const items = [];
  items.push(P(g, `M${x - 30} ${y100} L${x - 30} ${y0} M${x + 30} ${y100} L${x + 30} ${y0} M${x - 30} ${y100} Q${x} ${y100 - 26} ${x + 30} ${y100}`));
  items.push(P(g, `M${x - 30} ${y0} A52 52 0 1 0 ${x + 30} ${y0}`, "f"));
  if (ticks) for (let c = 10; c < 100; c += 10) items.push(P(g, `M${x + 30} ${Yc(c)} L${x + 54} ${Yc(c)}`, "l")), items[items.length - 1].style.strokeWidth = 5;
  const merc = P(g, `M${x} ${yb} L${x} ${Yc(level)}`, "r"); merc.style.strokeWidth = 14; items.push(merc);
  return { g, Yc, merc, items, x, yb };
}
const mercTo = (th, level, t, d = 0.4) => tl.to(th.merc, { attr: { d: `M${th.x} ${th.yb} L${th.x} ${th.Yc(level)}` }, duration: d, ease: "none" }, t);
function bulb(p, x, yc) { const g = G(p); E(g, "circle", { cx: x, cy: yc - 10, r: 33 }, "f h"); P(g, `M${x - 14} ${yc + 20} L${x + 14} ${yc + 20} M${x - 12} ${yc + 32} L${x + 12} ${yc + 32}`); P(g, `M${x - 12} ${yc + 20} L${x - 12} ${yc + 8} M${x + 12} ${yc + 20} L${x + 12} ${yc + 8}`); return g; }
function cube(p, x, y, sz = 54) { const g = G(p); P(g, `M${x} ${y} L${x + sz} ${y} L${x + sz} ${y + sz} L${x} ${y + sz} Z`, "f"); P(g, `M${x} ${y} L${x + 14} ${y - 14} L${x + sz + 14} ${y - 14} L${x + sz} ${y} M${x + sz} ${y + sz} L${x + sz + 14} ${y + sz - 14} L${x + sz + 14} ${y - 14}`); for (const c of g.children) c.classList.remove("h"); g.setAttribute("class", "h"); return g; }

// ---------- B1-B2 hook 0-7.88: alien hand + spoon + cup already in frame; wrist turn starts on "stirring" ----------
const S1 = scene(0, 7.88);
function hookLayout(g, t0, opts = {}) {
  const m = mug(g, 430, 760, 1.3); const sp = spoon(g, m, 1100);
  const th = thermo(g, 900, 470, 1250, 20);
  show(m.g, t0); pop(sp, t0); for (const i of th.items) pop(i, t0);
  return { m, sp, th };
}
const h1 = hookLayout(S1, 0);
const ST = (T) => 1 + 0.9 * Math.max(0, Math.min(1, (T - 5.82) / 0.3)) * (1 - Math.min(1, Math.max(0, (T - 6.6) / 1.0))); // "does try": one determined, bigger turn
const r1 = stirArm(S1, h1.m, h1.sp, 2.0, 7.88, 12, { kf: ST, armStart: 0 });
const t100 = TX(S1, 842, 490, "100 °C", 54, "red"); t100.style.textAnchor = "end"; pop(t100, 0);
const rm100 = P(S1, "M862 470 L878 470", "r"); pop(rm100, 0);
const t20 = TX(S1, 900, 1400, "20 °C", 60); pop(t20, 0);
const gz = D(S1, "M350 1540 Q600 1420 850 1330", "l"); ink(gz, "#9A9A9A", 5); draw(gz, 0.6, 0.35); off(gz, 1.7); // alien glances at the thermometer on "boil"
const tBoil = TX(S1, 400, 270, "BOIL", 170); pop(tBoil, 0.6);
const tBy = TX(S1, 400, 390, "BY STIRRING?", 80); pop(tBy, 2.1);
const trail = D(S1, "M374 1020 A56 14 0 1 1 486 1020 A56 14 0 1 1 374 1020", "l"); ink(trail, TEAL, 6); draw(trail, 2.08, 1.1); // spoon tip traces a circle under the surface
const clink = P(S1, "M640 745 L668 725 M648 772 L684 772 M640 799 L668 819", "l"); pop(clink, 3.05); off(clink, 3.45); const clTx = TX(S1, 745, 700, "tink", 44); pop(clTx, 3.05); off(clTx, 3.5);
const strike = D(S1, "M205 232 C300 214 410 244 600 208", "r"); draw(strike, 4.3, 0.1);
pop(TX(S1, 880, 330, "NO", 190, "red"), 4.27);
const lblSp = TX(S1, 700, 640, "SPOON", 56); pop(lblSp, 5.6); const arSp = arrow(S1, 640, 665, 480, 760, "l"); pop(arSp, 5.6);
pop(arrow(S1, 1015, 1100, 1015, 540, "r"), 3.4); pop(P(S1, "M985 780 L1045 840 M1045 780 L985 840", "r"), 4.27);
tl.to(r1.A.hand, { attr: { r: 38 }, duration: 0.1, ease: "none" }, 5.82); tl.to(r1.A.hand, { attr: { r: 30 }, duration: 0.15, ease: "none" }, 5.95); // grip adjusts
const tk = [D(S1, "M492 1090 L516 1060", "r"), D(S1, "M504 1138 L530 1110", "r")]; draw(tk[0], 6.2, 0.12); draw(tk[1], 6.3, 0.12);
mercTo(h1.th, 20.7, 6.2, 0.5);

// ---------- B3 "Stirring really does add energy" 7.88-9.33: close on wrist + spoon, amber arrow hand -> spoon -> water ----------
const S2a = scene(7.88, 9.33);
const m2a = mug(S2a, 540, 820, 1.5); const sp2a = spoon(S2a, m2a, 1100); show(m2a.g, 7.88); pop(sp2a, 7.88);
stirArm(S2a, m2a, sp2a, 7.88, 9.33, 14);
pop(TX(S2a, 540, 400, "ENERGY IN", 110), 8.58);
const a1 = D(S2a, "M610 740 L610 1000", "l"); ink(a1, AMB, 12); draw(a1, 8.33, 0.22); const a1h = P(S2a, "M584 972 L610 1012 L636 972", "l"); ink(a1h, AMB, 12); pop(a1h, 8.5);
const a2 = D(S2a, "M630 1090 C720 1050 810 1090 820 1190", "l"); ink(a2, AMB, 12); draw(a2, 8.58, 0.2); const a2h = P(S2a, "M794 1162 L820 1200 L846 1160", "l"); ink(a2h, AMB, 12); pop(a2h, 8.78);
["M690 990 C780 950 890 990 900 1090", "M690 1250 C770 1280 860 1260 880 1330", "M390 1060 C330 1110 330 1190 380 1230"].forEach((d, i) => { const f = D(S2a, d, "l"); ink(f, TEAL, 6); draw(f, 8.7 + i * 0.1, 0.25); });

// ---------- B4-B5 friction -> heat 9.33-18.6: ONE picture (mug -> zoom circle: two water layers slide at different speeds) ----------
const S2 = scene(9.33, 18.6);
const m2 = mug(S2, 540, 330, 0.9); const sp2 = spoon(S2, m2, 1100); show(m2.g, 9.33); pop(sp2, 9.33);
stirArm(S2, m2, sp2, 9.33, 18.6, 12, { kf: (T) => T < 13.6 ? 1 : Math.max(0, 1 - (T - 13.6) / 0.5), stop: 13.6 });
pop(P(S2, "M430 640 L338 836 M650 640 L742 836", "l"), 9.6);
const zcp = E(world, "clipPath", { id: "zc" }); E(zcp, "circle", { cx: 540, cy: 1010, r: 262 });
const zg = G(S2); zg.setAttribute("clip-path", "url(#zc)");
const zr = (y, hh, c) => E(zg, "rect", { x: 270, y, width: 540, height: hh, fill: c }, "h");
pop(zr(748, 262, "#E4E4E4"), 9.6); pop(zr(1010, 262, "#C4C4C4"), 9.6);
pop(P(zg, "M270 1010 L810 1010", "l"), 9.6);
const tg = G(zg); pop(tg, 9.6); tl.to(tg, { opacity: 0, duration: 1.0, ease: "none" }, 14.5); // tracers fade after the spoon stops
const zt = [[0, 800, 1], [130, 850, 1], [250, 905, 1], [370, 955, 1], [60, 1065, 0], [190, 1110, 0], [320, 1160, 0], [450, 1210, 0]].map(([x0, y, up]) => ({ x0, y, v: up ? 150 : 55, len: up ? 40 : 14, c: ink(E(tg, "path", { d: "M0 0" }, "l"), TEAL, 6) }));
const zI = (t) => t <= 4.4 ? t : 4.4 + 0.9 * (1 - Math.exp(-(t - 4.4) / 0.9)); // spoon stops at 14.0 -> tracers slow
const zupd = (t) => zt.forEach((d) => { const x = 270 + ((((d.x0 - d.v * zI(t)) % 540) + 540) % 540); d.c.setAttribute("d", `M${x.toFixed(1)} ${d.y} L${(x + d.len).toFixed(1)} ${d.y}`); });
zupd(0); const zpx = { t: 0 }; tl.to(zpx, { t: 9, duration: 9, ease: "none", onUpdate: () => zupd(zpx.t) }, 9.6);
const za1 = arrow(zg, 380, 830, 700, 830, "l", 26); ink(za1, TEAL, 8); pop(za1, 10.0); const za2 = arrow(zg, 560, 1190, 440, 1190, "l", 22); ink(za2, TEAL, 8); pop(za2, 10.6);
pop(arrow(zg, 640, 985, 565, 985, "r", 16), 12.8); pop(arrow(zg, 440, 1035, 515, 1035, "r", 16), 13.0);
[[420, 14.2], [540, 14.35], [660, 14.5]].forEach(([x, t]) => pop(P(zg, wave(x, 1000, 120), "r"), t));
E(S2, "ellipse", { cx: 540, cy: 1010, rx: 262, ry: 262 }, "l h"); pop(S2.lastChild, 9.6);
{ const hT = TX(S2, 940, 880, "HEAT", 70, "red"), hA = arrow(S2, 900, 905, 730, 950, "r"), ck = P(S2, "M880 1090 L910 1120 L960 1050", "r"); pop(hT, 14.5); pop(hA, 14.6); pop(ck, 16.0); [hT, hA, ck].forEach((e) => off(e, 17.5)); }
const gx = 960, gf = P(S2, `M${gx - 32} 1380 L${gx - 32} 1180 L${gx + 32} 1180 L${gx + 32} 1380`, "l"); pop(gf, 14.4); // tiny THERMAL ENERGY indicator
const ga = E(S2, "rect", { x: gx - 27, y: 1377, width: 54, height: 3, fill: AMB }, "h"); pop(ga, 14.4); tl.to(ga, { attr: { y: 1358, height: 22 }, duration: 0.35, ease: "power2.out" }, 14.51);
const gtx = TX(S2, 860, 1425, "THERMAL ENERGY", 38); pop(gtx, 14.5);
off(gf, 17.66); off(ga, 17.66); off(gtx, 17.66);                       // "the amount": pull back to the whole scale
const bigF = D(S2, `M${gx - 32} 1380 L${gx - 32} 420 L${gx + 32} 420 L${gx + 32} 1380`, "l"); draw(bigF, 17.66, 0.6);
pop(E(S2, "rect", { x: gx - 27, y: 1373, width: 54, height: 6, fill: AMB }, "h"), 17.7);
pop(TX(S2, gx, 380, "NEEDED", 40), 18.2); pop(E(S2, "ellipse", { cx: gx, cy: 1376, rx: 52, ry: 20 }, "r h"), 18.2); pop(TX(S2, 835, 1385, "THIS", 44, "red"), 18.2);

// ---------- B6 "Take a quarter liter of water at twenty degrees" 18.6-21.87: pour into the jug, level rises to 250 mL, probe goes in ----------
const S3 = scene(18.6, 27.77);
const JX = 120;
const jug = G(S3); jug.setAttribute("transform", `translate(${JX} 0)`);
const jw = P(jug, "M0 0", "g"); jw.style.stroke = "none";
P(jug, "M330 660 L335 1110 Q338 1140 368 1140 L480 1140 Q510 1140 513 1110 L518 660"); P(jug, "M330 660 L300 640"); P(jug, "M518 760 C590 750 590 920 513 930");
const jsurf = E(jug, "ellipse", { cx: 424, cy: 1138, rx: 94, ry: 14 }, "g h"); [880, 980, 1060].forEach((y) => P(jug, `M335 ${y} L365 ${y}`));
show(jug, 18.6); tl.set(jw, { opacity: 0 }, 18.6); tl.set(jsurf, { opacity: 0 }, 18.6); pop(jw, 18.9); pop(jsurf, 18.9);
const strm = E(S3, "rect", { x: 553, y: 428, width: 14, height: 0 }, "g h"); pop(strm, 18.85); off(strm, 19.98);
const jx = (y) => 330 + (y - 780) * 5 / 330, jxr = (y) => 518 - (y - 780) * 5 / 330;
const setLv = (y, r) => { const yy = y + 3 * r; jw.setAttribute("d", `M${jx(yy)} ${yy} L335 1110 Q338 1140 368 1140 L480 1140 Q510 1140 513 1110 L${jxr(yy)} ${yy} Z`); jsurf.setAttribute("cy", yy); jsurf.setAttribute("ry", 14 + 5 * r); strm.setAttribute("height", Math.max(0, yy - 428)); };
const lvY = (t) => t < 1.15 ? 1138 - 358 * (1 - (1 - t / 1.15) ** 2) : 780, lvR = (t) => t > 1.15 ? Math.exp(-(t - 1.15) * 5) * Math.sin((t - 1.15) * 22) : 0; // meniscus settles
setLv(1138, 0); const lp = { t: 0 }; tl.to(lp, { t: 1.9, duration: 1.9, ease: "none", onUpdate: () => setLv(lvY(lp.t), lvR(lp.t)) }, 18.85);
const pit = G(S3); const pp = (d) => d.replace(/(-?\d+\.?\d*) (-?\d+\.?\d*)/g, (m, a, b) => `${+a + 560} ${+b + 420}`);
P(pit, pp("M0 0 L8 150 Q10 165 28 165 L170 165 Q188 165 190 150 L196 -6 Z"), "f"); P(pit, pp("M0 0 L-26 -12"), "l"); P(pit, pp("M193 20 C262 20 262 125 188 132"), "l");
show(pit, 18.6); tl.set(pit, { rotation: 0, svgOrigin: "560 420" }, 0); tl.to(pit, { rotation: -48, duration: 0.3, ease: "power1.out" }, 18.62); tl.to(pit, { rotation: 0, duration: 0.2, ease: "power1.in" }, 19.95); off(pit, 20.2);
pop(TX(S3, 290, 760, "250 mL", 64), 20.1); pop(P(S3, "M390 780 L450 780", "l"), 20.1);
const TC = 544, th3 = thermo(S3, TC, 480, 1020, 20); for (const i of th3.items) pop(i, 20.2);
tl.set(th3.g, { y: -430 }, 0); tl.to(th3.g, { y: 0, duration: 0.55, ease: "power1.out" }, 20.25); // probe lowered into the water
const y20 = th3.Yc(20), y100b = th3.Yc(100);
const rd = TX(S3, TC, 380, "20 °C", 110); pop(rd, 20.86);
const cl = { v: 20 };
const setT = (v) => { rd.textContent = Math.round(v) + " °C"; rd.style.fill = v >= 95 ? "#D7263D" : "#111"; th3.merc.setAttribute("d", `M${th3.x} ${th3.yb} L${th3.x} ${th3.Yc(v)}`); };
tl.to(cl, { v: 100, duration: 1.15, ease: "power1.in", onUpdate: () => setT(cl.v) }, 24.16);   // "eighty degrees" -> reading climbs 20 -> 100
const l100 = TX(S3, 496, y100b + 16, "100 °C", 50, "red"); l100.style.textAnchor = "end"; pop(l100, 23.2);
const tStart = TX(S3, 860, 380, "START", 56, "red"); pop(tStart, 23.2); off(tStart, 24.1);
pop(P(S3, `M745 ${y20} L765 ${y20} L765 ${y100b} L745 ${y100b}`, "r"), 24.16);
pop(TX(S3, 905, (y20 + y100b) / 2 + 24, "+80 °C", 72, "red"), 24.16);
const ff = TX(S3, 880, 1010, "FAST-FORWARD", 40); pop(ff, 24.16); off(ff, 25.9);
const pulse = E(world, "rect", { x: 10, y: 10, width: 1060, height: 1900, fill: "none", stroke: "#D7263D", "stroke-width": 20 }, "h"); // red edge pulse (overlay only)
[0, 1, 2].forEach((k) => { const t = 24.85 + k * 0.27; tl.set(pulse, { opacity: 0.5 }, t); tl.to(pulse, { opacity: 0.1, duration: 0.2, ease: "none" }, t); }); tl.set(pulse, { opacity: 0 }, 25.75);
pop(TX(S3, 540, 1300, "≈ 84,000 J", 104), 25.52); pop(P(S3, "M230 1322 L850 1322", "r"), 26.6);
[480, 544, 608].forEach((x, i) => pop(P(S3, wave(x, 1215, 55), "r"), 26.9 + i * 0.15));

// cutaway 21.87-23.15 (approved)
// boiling pot (approved shot): bubbles are born at the hot bottom, rise, break at the surface; the surface rolls. Reused for the B22 split screen.
function boilPot(S, t0, dur, o = {}) {
  const gp = G(S); if (o.tf) gp.setAttribute("transform", o.tf);
  const at = (dt) => t0 + dt;
  if (o.full) pop(E(gp, "rect", { x: 0, y: 0, width: 1080, height: 1330, fill: "#fff" }, "h"), t0);
  const potBody = P(gp, "M312 870 L768 870 L764 1150 Q761 1180 730 1180 L350 1180 Q319 1180 316 1150 Z", "g"); potBody.style.stroke = "none"; pop(potBody, t0);
  const surfL = P(gp, "M312 870 L768 870", "l"); pop(surfL, t0);
  pop(P(gp, "M300 780 L305 1150 Q308 1180 340 1180 L740 1180 Q772 1180 775 1150 L780 780 M300 830 L240 830 M780 830 L840 830", "l"), t0);
  [430, 540, 650].forEach((fx, i) => pop(P(gp, `M${fx} 1290 C${fx - 34} 1250 ${fx - 22} 1225 ${fx - 8} 1205 C${fx - 4} 1228 ${fx + 10} 1228 ${fx + 14} 1200 C${fx + 42} 1235 ${fx + 44} 1262 ${fx} 1290 Z`, "r"), at(i * 0.05)));
  pop(P(gp, "M330 1300 L750 1300", "l"), t0);
  const bubs = [[380, 0.62, 0.0], [450, 0.78, 0.25], [530, 0.66, 0.1], [600, 0.84, 0.4], [660, 0.7, 0.5], [720, 0.6, 0.3], [490, 0.9, 0.55], [570, 0.74, 0.15]].map(([x, Pd, ph]) => {
    const c = E(gp, "circle", { cx: x, cy: 1150, r: 6 }, "f"); c.style.strokeWidth = 5; c.style.opacity = 0;
    const pp = P(gp, `M${x - 14} 870 L${x - 22} 856 M${x + 14} 870 L${x + 22} 856 M${x} 866 L${x} 848`, "l"); pp.style.strokeWidth = 4; pp.style.opacity = 0; pp.classList.remove("h");
    return { x, Pd, ph, c, pp }; });
  const SBy = (x, tau) => 870 + 13 * Math.min(1, tau / 0.7) * Math.sin(x / 38 - tau * 9);
  const bupd = (tau) => {
    let d = "M312 " + SBy(312, tau).toFixed(1); for (let x = 331; x <= 768; x += 19) d += " L" + x + " " + SBy(x, tau).toFixed(1);
    surfL.setAttribute("d", d);
    potBody.setAttribute("d", d + " L764 1150 Q761 1180 730 1180 L350 1180 Q319 1180 316 1150 Z");
    bubs.forEach((b) => { const lt = tau - b.ph; if (lt < 0) { b.c.style.opacity = 0; b.pp.style.opacity = 0; return; }
      const u = (lt % b.Pd) / b.Pd, sy = SBy(b.x, tau);
      if (u < 0.9) { b.c.style.opacity = 1; b.c.setAttribute("cy", (1150 - u / 0.9 * (1150 - sy - 14)).toFixed(1)); b.c.setAttribute("r", (6 + 10 * u / 0.9).toFixed(1)); b.pp.style.opacity = 0; }
      else { b.c.style.opacity = 0; b.pp.style.opacity = 1; b.pp.setAttribute("transform", `translate(0 ${(sy - 870).toFixed(1)})`); } });
  };
  bupd(0); const bpx = { t: 0 }; tl.to(bpx, { t: dur, duration: dur, ease: "none", onUpdate: () => bupd(bpx.t) }, t0);
  pop(arrow(gp, 540, 1110, 540, 960, "l"), at(0.43)); pop(arrow(gp, 370, 920, 370, 1060, "l"), at(0.43)); pop(arrow(gp, 710, 920, 710, 1060, "l"), at(0.43));
  if (o.full) { pop(TX(gp, 540, 500, "BOILING", 130), t0); pop(TX(gp, 540, 690, "100 °C", 150, "red"), at(0.63)); pop(TX(gp, 540, 765, "at 1 atm", 48), at(0.88)); }
  else pop(TX(gp, 540, 670, "100 °C", 150, "red"), o.t100);
}
const SB = scene(21.87, 23.15); boilPot(SB, 21.87, 1.28, { full: true }); // cutaway: approved, unchanged

// ---------- S4 "Do that in two minutes": timer 0:00 -> 2:00 27.77-29.15 ----------
const S4 = scene(27.77, 29.15);
const rcx = 540, rcy = 800, rr = 300, ringPath = `M${rcx} ${rcy - rr} A${rr} ${rr} 0 1 1 ${rcx} ${rcy + rr} A${rr} ${rr} 0 1 1 ${rcx} ${rcy - rr}`;
const ringBg = P(S4, ringPath, "l"); ringBg.style.stroke = "#E4E4E4"; pop(ringBg, 27.77);
pop(P(S4, `M${rcx - 26} ${rcy - rr - 36} L${rcx + 26} ${rcy - rr - 36} M${rcx} ${rcy - rr - 36} L${rcx} ${rcy - rr}`), 27.77);
[27.93, 28.07, 28.21, 28.34].forEach((t, q) => { const a0 = q * Math.PI / 2, a1 = (q + 1) * Math.PI / 2, pt = (a) => `${rcx + rr * Math.sin(a)} ${rcy - rr * Math.cos(a)}`; const seg = P(S4, `M${pt(a0)} A${rr} ${rr} 0 0 1 ${pt(a1)}`, "r"); seg.style.strokeWidth = 16; pop(seg, t); }); // quarter arcs land with 0:30/1:00/1:30/2:00
const tm = [["0:00", 27.77], ["0:30", 27.93], ["1:00", 28.07], ["1:30", 28.21], ["2:00", 28.34]];
tm.forEach(([s, t], i) => { const e = TX(S4, rcx, rcy + 75, s, 190, i === 4 ? "red" : ""); pop(e, t); if (i < 4) off(e, tm[i + 1][1]); });

// ---------- S4b "700 watts going in" 29.15-31.5 ----------
const S4b = scene(29.15, 31.5);
const m4 = mug(S4b, 540, 960, 0.8); show(m4.g, 29.15);
pop(TX(S4b, 540, 560, "700 W", 250, "red"), 29.72);
pop(TX(S4b, 540, 705, "84,000 J ÷ 120 s ≈ 700 W", 50), 30.24);
pop(arrow(S4b, 540, 770, 540, 985, "r", 28), 30.54); pop(TX(S4b, 850, 860, "INTO THE", 46), 30.54); pop(TX(S4b, 850, 915, "WATER", 46), 30.6);

// ---------- S5 "seven old 100-watt bulbs" 31.5-34.8 : exactly 7, eased timing (slow-fast-slow) ----------
const S5 = scene(31.5, 34.8);
const bt = [31.55, 32.05, 32.39, 32.63, 32.85, 33.19, 33.69];
bt.forEach((t, i) => {
  const x = i < 4 ? 170 + i * 247 : 293 + (i - 4) * 247, yc = i < 4 ? 560 : 900, g = G(S5);
  const glass = E(g, "circle", { cx: x, cy: yc, r: 46 }, "f h");
  P(g, `M${x - 17} ${yc + 43} L${x - 17} ${yc + 62} M${x + 17} ${yc + 43} L${x + 17} ${yc + 62} M${x - 20} ${yc + 62} L${x + 20} ${yc + 62} M${x - 18} ${yc + 78} L${x + 18} ${yc + 78} M${x - 8} ${yc + 90} L${x + 8} ${yc + 90}`);
  const fil = `M${x - 14} ${yc + 40} L${x - 14} ${yc + 8} L${x - 7} ${yc + 20} L${x} ${yc + 8} L${x + 7} ${yc + 20} L${x + 14} ${yc + 8} L${x + 14} ${yc + 40}`;
  const fo = P(g, fil); fo.style.strokeWidth = 4; show(g, 31.5);
  const fr = P(S5, fil, "r"); fr.style.strokeWidth = 5; pop(fr, t);
  tl.set(glass, { fill: "#FFE27A" }, t);
  [-150, -120, -90, -60, -30].forEach((a) => { const ar = a * Math.PI / 180; const rr2 = P(S5, `M${x + 60 * Math.cos(ar)} ${yc + 60 * Math.sin(ar)} L${x + 82 * Math.cos(ar)} ${yc + 82 * Math.sin(ar)}`); rr2.style.stroke = "#E8A800"; pop(rr2, t); });
  const ring = E(S5, "circle", { cx: x, cy: yc, r: 48, fill: "none", stroke: "#F2B705", "stroke-width": 8 }, "h"); pop(ring, t); tl.to(ring, { opacity: 0, attr: { r: 100 }, duration: 0.3, ease: "power1.out" }, t);
  pop(TX(S5, x, yc + 140, "100 W", 44), t);
});
pop(TX(S5, 540, 1210, "7 × 100 W = 700 W", 78), 33.69);

// ---------- S6 "microwave draws to heat a mug" 34.8-36.95 ----------
const S6 = scene(34.8, 36.95);
const mwg = G(S6);
P(mwg, "M140 560 L930 560 L930 1100 L140 1100 Z", "f"); P(mwg, "M170 590 L710 590 L710 1070 L170 1070 Z", "f"); P(mwg, "M730 590 L900 590 L900 1070 L730 1070 Z");
P(mwg, "M765 900 L865 900 M765 960 L865 960"); E(mwg, "circle", { cx: 815, cy: 1015, r: 20 }, "f h"); E(mwg, "rect", { x: 755, y: 630, width: 120, height: 70 }, "f h");
show(mwg, 34.8);
const lightR = E(S6, "rect", { x: 172, y: 592, width: 536, height: 476, fill: "#FFF4B8" }, "h"); pop(lightR, 35.3);
const plate = E(S6, "ellipse", { cx: 440, cy: 1012, rx: 205, ry: 24 }, "f h"); pop(plate, 34.8);
const m6 = mug(S6, 440, 800, 0.55); show(m6.g, 34.8);
const tdots = [0, 2.094, 4.189].map(() => E(S6, "circle", { cx: 440, cy: 1012, r: 7, fill: "#111" }, "h"));
const tdupd = (t) => tdots.forEach((c, i) => { const a = i * 2.094 + t * 7; c.setAttribute("cx", (440 + 185 * Math.cos(a)).toFixed(1)); c.setAttribute("cy", (1012 + 17 * Math.sin(a)).toFixed(1)); });
tdots.forEach((c) => pop(c, 35.5)); tdupd(0); const tdx = { t: 0 }; tl.to(tdx, { t: 1.45, duration: 1.45, ease: "none", onUpdate: () => tdupd(tdx.t) }, 35.5);
pop(P(S6, "M240 1058 C330 1092 550 1092 640 1058 M614 1046 L640 1058 L610 1073", "r"), 35.5);
const doorFr = (pts, t0, t1) => { const d = P(S6, pts, "f"); pop(d, t0); if (t1) off(d, t1); return d; };
doorFr("M170 590 L60 560 L60 1100 L170 1070 Z", 34.8, 34.95); doorFr("M170 590 L110 575 L110 1085 L170 1070 Z", 34.95, 35.08); doorFr("M170 590 L145 584 L145 1076 L170 1070 Z", 35.08, 35.2);
pop(P(S6, "M170 590 L710 590 L710 1070 L170 1070 Z M200 620 L680 620 L680 1040 L200 1040 Z", "l"), 35.2);
P(S6, "M700 1175 L850 1175"); const spB = E(S6, "ellipse", { cx: 880, cy: 1175, rx: 34, ry: 22 }, "f h"); pop(S6.children[S6.children.length - 2], 34.8); pop(spB, 34.8);
const tm6 = TX(S6, 540, 470, "20 °C", 110); pop(tm6, 35.4);
const c6 = { v: 20 }; tl.to(c6, { v: 80, duration: 0.75, ease: "power1.in", onUpdate: () => { tm6.textContent = Math.round(c6.v) + " °C"; } }, 35.8);
const ff6 = TX(S6, 540, 525, "FAST-FORWARD", 38); pop(ff6, 35.8);
[[410, 36.0], [440, 36.12], [470, 36.24]].forEach(([x, t]) => pop(P(S6, wave(x, 770, 80), "r"), t));
pop(TX(S6, 390, 1232, "WALL ≈ 1,000 W", 50), 36.1); pop(TX(S6, 390, 1302, "INTO FOOD ≈ 700 W", 50, "red"), 36.4);

// ---------- B13 "In horse terms, about one horsepower" 36.95-39.3: 700 W goes into a gauge, needle stops just shy of 1 hp, horse takes one step ----------
const S7 = scene(36.95, 39.33);
const HX = (x) => 30 + 1.2 * x, HY = (y) => 1000 + 1.2 * (y - 250);
const hp = (d) => d.replace(/(-?\d+\.?\d*)\s+(-?\d+\.?\d*)/g, (m, a, b) => `${HX(+a)} ${HY(+b)}`);
const hz = G(S7);
P(hz, hp("M40 70 C40 40 120 36 170 44 C205 48 224 58 232 78 C240 102 226 122 204 124 L72 124 C50 120 38 100 40 70 Z"), "f");
P(hz, hp("M205 48 C226 32 238 14 246 0 M232 78 C248 58 258 44 264 38"));
P(hz, hp("M246 0 L290 22 L284 40 L262 36 M242 2 L240 -16 L252 0"));
P(hz, hp("M176 122 L176 168 L170 200 L174 244 M168 244 L186 244"));
P(hz, hp("M70 118 C80 150 94 164 86 190 L72 204 L78 244 M72 244 L90 244 M96 122 C100 150 114 164 108 190 L98 204 L102 244 M96 244 L114 244"));
P(hz, hp("M42 64 C18 72 10 112 20 152"));
P(hz, hp("M0 250 L300 250")); show(hz, 36.95);
const legA = (d, a, b) => { const e = P(S7, hp(d)); pop(e, a); if (b) off(e, b); };
legA("M198 122 L204 168 L198 200 L202 244 M196 244 L214 244", 36.95, 38.3); legA("M198 122 L206 160 L186 186 L190 210 M184 210 L200 212", 38.3, 38.56); legA("M198 122 L214 168 L212 204 L220 244 M214 244 L232 244", 38.56); // one natural step on "horsepower"
const gcx = 740, gcy = 960, GR = 230, gp2 = (w, r) => { const a = Math.PI * (1 - w / 1000); return [gcx + r * Math.cos(a), gcy - r * Math.sin(a)]; };
pop(P(S7, `M${gcx - GR} ${gcy} A${GR} ${GR} 0 0 1 ${gcx + GR} ${gcy} Z`, "l"), 36.95);
for (let w = 0; w <= 1000; w += 100) { const [x1, y1] = gp2(w, GR - (w % 500 === 0 ? 34 : 20)), [x2, y2] = gp2(w, GR); pop(P(S7, `M${x1} ${y1} L${x2} ${y2}`, "l"), 36.95); }
{ const [x1, y1] = gp2(746, GR - 44), [x2, y2] = gp2(746, GR + 16), [x3, y3] = gp2(746, GR + 62); pop(P(S7, `M${x1} ${y1} L${x2} ${y2}`, "r"), 37.0); pop(TX(S7, x3, y3 + 14, "1 hp", 50, "red"), 37.0); }
pop(TX(S7, gcx - GR, gcy + 50, "0", 36), 36.95); pop(TX(S7, gcx + GR, gcy + 50, "1000", 36), 36.95);
const ndl = P(S7, `M${gcx} ${gcy} L${gcx} ${gcy - 200}`, "l"); ndl.style.strokeWidth = 9; pop(ndl, 36.95); pop(E(S7, "circle", { cx: gcx, cy: gcy, r: 14 }, "f h"), 36.95);
const nw = { v: 0 }; tl.to(nw, { v: 700, duration: 0.95, ease: "power2.out", onUpdate: () => { const [x, y] = gp2(nw.v, 200); ndl.setAttribute("d", `M${gcx} ${gcy} L${x.toFixed(1)} ${y.toFixed(1)}`); } }, 37.0); // needle rises to 700 W and stops just short of the 1 hp tick
pop(TX(S7, gcx, gcy + 130, "700 W", 100, "red"), 36.95);
pop(TX(S7, 290, 1110, "1 HORSEPOWER", 56), 38.14); pop(TX(S7, 540, 1270, "≈ 746 W", 90, "red"), 38.7);

const RY = (w) => 1300 - w; // 1 px per watt
// ---------- B14 Niagara Falls 39.33-45.67: three-quarter aerial of the Horseshoe curve (Niagara Parks aerial, simplified like xkcd pfbzrrcQZjs 21-35 s / 116-138 s) ----------
// order of motion: river currents (39.33) -> falling sheet (40.2) -> base spray (40.95) -> mist (41.4); marker follows one parcel 40.54-42.3; cliffs and brink never move
const S8 = scene(39.33, 45.67), N0 = 39.33;
const bz = (s) => { const u = 1 - s; return [u * u * u * 150 + 3 * u * u * s * 260 + 3 * u * s * s * 840 + s * s * s * 1010, u * u * u * 870 + 3 * u * u * s * 590 + 3 * u * s * s * 560 + s * s * s * 800]; };
const Hd = (s) => 360 - 130 * s, gb = (s) => { const [x, y] = bz(s); return [x, y + Hd(s)]; };
const samp = (f, n = 30) => Array.from({ length: n + 1 }, (_, i) => f(i / n));
const poly = (pts) => pts.map(([x, y], i) => (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1)).join(" ");
const rlanes = Array.from({ length: 9 }, (_, i) => { const s = 0.06 + i * 0.11, [xe, ye] = bz(s); return { i, s, x0: 180 + i * 92, xe, ye, c: ink(E(S8, "path", { d: "M0 0" }, "l"), TEAL, 7) }; });
const qb = (l, u) => { const cx = l.x0 * 0.7 + l.xe * 0.3, cy = 400 + (l.ye - 400) * 0.55, a = (1 - u) * (1 - u), b = 2 * u * (1 - u), c = u * u; return [a * l.x0 + b * cx + c * l.xe, a * 400 + b * cy + c * l.ye]; };
const isl = P(S8, "M700 480 C700 440 760 425 810 440 C850 455 845 500 800 510 C760 520 700 520 700 480 Z", "f"); pop(isl, N0);
const cur = P(S8, poly(samp(bz)) + " " + samp(gb).reverse().map(([x, y]) => `L${x.toFixed(1)} ${y.toFixed(1)}`).join(" ") + " Z", "g"); cur.style.stroke = "none"; cur.style.fill = "#E4E4E4"; pop(cur, N0);
const streaks = Array.from({ length: 30 }, (_, i) => { const s = (i + 0.5) / 30, [x, y0] = bz(s); const c = E(S8, "path", { d: "M0 0" }, "l"); c.style.strokeWidth = 3.5; return { i, x, y0, H: Hd(s), v: 400 + (i * 37 % 160), c }; });
pop(P(S8, "M150 870 L144 960 L156 1050 L146 1140 L150 1230 M1010 800 L1016 880 L1006 960 L1010 1030", "l"), N0);
pop(P(S8, poly(samp(bz)), "l"), N0); S8.lastChild.style.strokeWidth = 9;
const pool = Array.from({ length: 6 }, (_, r) => ({ r, c: ink(E(S8, "path", { d: "M0 0" }, "l"), TEAL, 6) })); // plunge pool / gorge river below the base
const foam = Array.from({ length: 14 }, (_, i) => { const g = G(S8), s = 0.02 + 0.07 * i; const cs = [0, 1].map(() => { const c = E(g, "circle", { cx: 0, cy: 0, r: 10 }, "f"); c.style.stroke = "#9A9A9A"; c.style.strokeWidth = 3; return c; }); return { i, s, g, cs, r: 40 + 9 * Math.sin(i * 1.7) }; });
const sprays = Array.from({ length: 22 }, (_, i) => { const c = E(S8, "circle", { cx: 0, cy: 0, r: 6 }, "f"); c.style.strokeWidth = 3; c.style.opacity = 0; return { i, s: 0.04 + 0.92 * ((i * 7) % 22) / 22, c }; });
const puffs = Array.from({ length: 12 }, (_, i) => { const g = G(S8); g.style.opacity = 0; const cs = [0, 1, 2].map(() => { const c = E(g, "circle", { cx: 0, cy: 0, r: 10 }, "f"); c.style.stroke = "#9A9A9A"; c.style.strokeWidth = 3; return c; }); return { i, s: 0.08 + 0.07 * i, g, cs }; });
const parc = E(S8, "ellipse", { cx: 0, cy: 0, rx: 20, ry: 20 }, "h"); parc.style.fill = TEAL; parc.style.stroke = "#111"; parc.style.strokeWidth = 5;
const pl = rlanes[4], [pbx, pby] = bz(pl.s), pgy = gb(pl.s)[1];
const nupd = (T) => {
  const t = T - N0;
  rlanes.forEach((l) => l.c.setAttribute("d", [0, 1, 2].map((k) => { const u0 = (t * 0.33 + l.i * 0.17 + k / 3) % 1, a = u0 ** 1.25, b = Math.min(1, Math.min(1, u0 + 0.06) ** 1.25), p = qb(l, a), q = qb(l, b); return `M${p[0].toFixed(1)} ${p[1].toFixed(1)} L${q[0].toFixed(1)} ${q[1].toFixed(1)}`; }).join(" ")));
  pool.forEach((d) => { const pts = []; for (let k = 0; k < 4; k++) { const sc = ((t * 0.22 + d.r * 0.11 + k / 4) % 1) * 0.94; const sa = Math.min(1, sc + 0.05), [x1, y1] = [bz(sc)[0], gb(sc)[1] + 45 + d.r * 42], [x2, y2] = [bz(sa)[0], gb(sa)[1] + 45 + d.r * 42]; if (y1 < 1300 && y2 < 1300) pts.push(`M${x1.toFixed(1)} ${y1.toFixed(1)} L${x2.toFixed(1)} ${y2.toFixed(1)}`); } d.c.setAttribute("d", pts.join(" ") || "M0 0"); });
  foam.forEach((d) => { const [x, y] = gb(d.s); d.g.style.opacity = T >= 40.95 ? 1 : 0; d.cs[0].setAttribute("cx", (x - d.r * 0.45).toFixed(1)); d.cs[0].setAttribute("cy", (y + 4 + 5 * Math.sin(T * 3 + d.i)).toFixed(1)); d.cs[0].setAttribute("r", (d.r * 0.85).toFixed(1)); d.cs[1].setAttribute("cx", (x + d.r * 0.4).toFixed(1)); d.cs[1].setAttribute("cy", (y - 12 + 5 * Math.sin(T * 3.4 + d.i * 2)).toFixed(1)); d.cs[1].setAttribute("r", d.r.toFixed(1)); });
  const tf = Math.max(0, T - 40.2);
  streaks.forEach((l) => l.c.setAttribute("d", [0, 1, 2].map((k) => { const ys = l.y0 + ((tf * l.v + l.i * 47 + k * l.H / 3) % l.H), ye = Math.min(ys + 34, l.y0 + l.H); return `M${l.x.toFixed(1)} ${ys.toFixed(1)} L${l.x.toFixed(1)} ${ye.toFixed(1)}`; }).join(" ")));
  sprays.forEach((d) => { const a = T - 40.95 - d.i * 0.037; if (a < 0) { d.c.style.opacity = 0; return; } const u = (a % 0.8) / 0.8, [x, y] = gb(d.s), sg = d.i % 2 ? 1 : -1; d.c.style.opacity = 1; d.c.setAttribute("cx", (x + sg * (8 + 34 * u)).toFixed(1)); d.c.setAttribute("cy", (y - 4 * 90 * u * (1 - u)).toFixed(1)); d.c.setAttribute("r", (8 - 4 * u).toFixed(1)); });
  puffs.forEach((d) => { const a = T - 41.4 - d.i * 0.22; if (a < 0) { d.g.style.opacity = 0; return; } const u = (a % 2.6) / 2.6, [x, y] = gb(d.s), r = 24 + 32 * u, cx = x + 90 * u + 14 * Math.sin(d.i * 2 + u * 4), cy = y - 20 - 170 * u;
    d.g.style.opacity = (Math.min(1, u * 5) * (1 - u) ** 0.8).toFixed(2); [[-0.8, 0, 0.8], [0, -0.45, 1], [0.8, 0, 0.8]].forEach(([dx, dy, k], j) => { d.cs[j].setAttribute("cx", (cx + dx * r).toFixed(1)); d.cs[j].setAttribute("cy", (cy + dy * r).toFixed(1)); d.cs[j].setAttribute("r", (r * k).toFixed(1)); }); });
  if (T < 40.54 || T >= 42.3) parc.style.opacity = 0;
  else { parc.style.opacity = 1; if (T < 41.55) { const [x, y] = qb(pl, 0.1 + 0.9 * ((T - 40.54) / 1.01)); parc.setAttribute("cx", x.toFixed(1)); parc.setAttribute("cy", y.toFixed(1)); parc.setAttribute("ry", 20); }
    else { const q = (T - 41.55) / 0.75; parc.setAttribute("cx", pbx.toFixed(1)); parc.setAttribute("cy", (pby + (pgy - pby) * q * q).toFixed(1)); parc.setAttribute("ry", (20 + 14 * q).toFixed(1)); } }
};
nupd(N0); const npx = { t: N0 }; tl.to(npx, { t: 45.67, duration: 45.67 - N0, ease: "none", onUpdate: () => nupd(npx.t) }, N0);
const tN = TX(S8, 540, 250, "NIAGARA FALLS", 100); pop(tN, 42.0); pop(TX(S8, 540, 322, "HORSESHOE FALLS", 38), 42.0);
pop(P(S8, "M120 870 L105 870 L105 1230 L120 1230", "l"), 42.8); { const t51 = TX(S8, 66, 1050, "≈ 51 m DROP", 40); t51.setAttribute("transform", "rotate(-90 66 1050)"); pop(t51, 42.8); }
pop(P(S8, "M640 1380 L1060 1380 L1060 1700 L640 1700 Z", "f"), 44.0); pop(TX(S8, 850, 1470, "≈ +0.1 °C", 66, "red"), 44.15); pop(TX(S8, 850, 1525, "idealized estimate", 38), 44.76);
pop(P(S8, "M700 1650 L760 1650 M700 1590 L760 1590", "l"), 44.0); [["20.0 °C", 1662], ["20.1 °C", 1602]].forEach(([s, y]) => { const t = TX(S8, 775, y, s, 34); t.style.textAnchor = "start"; pop(t, 44.0); }); pop(TX(S8, 985, 1636, "zoomed", 32), 44.0);
const mk = E(S8, "path", { d: "M672 1650 L696 1638 L696 1662 Z", fill: "#D7263D" }, "h"); pop(mk, 44.0); tl.to(mk, { y: -60, duration: 0.18, ease: "power1.out" }, 44.4);

// ---------- B15 "Now the spoon. A hard stir adds well under one watt" 45.67-48.9 ----------
const S9a = scene(45.67, 48.9);
const h9 = hookLayout(S9a, 45.67);
const r9 = stirArm(S9a, h9.m, h9.sp, 45.67, 48.9, 16, { rev: 2.4, str: 1.5, kf: (T) => 1 + 0.5 * Math.min(1, Math.max(0, (T - 46.4) / 0.4)) });
tl.to(r9.A.hand, { attr: { r: 40 }, duration: 0.12, ease: "none" }, 46.58); tl.to(r9.A.hand, { attr: { r: 32 }, duration: 0.15, ease: "none" }, 46.72); // tighter grip
const g700 = TX(S9a, 540, 330, "700 W", 150); g700.style.fill = "#C4C4C4"; pop(g700, 45.67);
const lt1 = TX(S9a, 735, 575, "< 1 W", 84); lt1.style.fill = AMB; pop(lt1, 47.98);
pop(TX(S9a, 900, 1400, "20 °C", 60), 45.67);

// ---------- B16 "Less than a hundredth of one of those bulbs" 48.9-51.4: ONE bulb, its 100 W bar, zoom inset on the 1 W boundary ----------
const S9b = scene(48.9, 51.4);
{ const x = 230, yc = 760, g = G(S9b); E(g, "circle", { cx: x, cy: yc, r: 46 }, "f h").style.fill = "#FFE27A";
  P(g, `M${x - 17} ${yc + 43} L${x - 17} ${yc + 62} M${x + 17} ${yc + 43} L${x + 17} ${yc + 62} M${x - 20} ${yc + 62} L${x + 20} ${yc + 62} M${x - 18} ${yc + 78} L${x + 18} ${yc + 78} M${x - 8} ${yc + 90} L${x + 8} ${yc + 90}`);
  const fo = P(g, `M${x - 14} ${yc + 40} L${x - 14} ${yc + 8} L${x - 7} ${yc + 20} L${x} ${yc + 8} L${x + 7} ${yc + 20} L${x + 14} ${yc + 8} L${x + 14} ${yc + 40}`, "r"); fo.style.strokeWidth = 5; show(g, 48.9);
  [-150, -120, -90, -60, -30].forEach((a) => { const ar = a * Math.PI / 180; const r2 = P(S9b, `M${x + 60 * Math.cos(ar)} ${yc + 60 * Math.sin(ar)} L${x + 82 * Math.cos(ar)} ${yc + 82 * Math.sin(ar)}`); ink(r2, "#E8A800"); pop(r2, 48.9); });
  pop(TX(S9b, x, yc + 160, "100 W", 50), 48.9); }
const bar = E(S9b, "rect", { x: 420, y: 1250, width: 100, height: 0, fill: "#FFE27A", stroke: "#111", "stroke-width": 7 }, "h"); pop(bar, 49.2);
tl.to(bar, { attr: { y: 550, height: 700 }, duration: 0.55, ease: "power2.out" }, 49.2);
pop(TX(S9b, 470, 500, "100 W", 64), 49.75);
pop(P(S9b, "M395 1243 L545 1243", "r"), 49.8); pop(TX(S9b, 600, 1236, "1 W", 44, "red"), 49.8);
const izc = E(world, "clipPath", { id: "iz" }); E(izc, "circle", { cx: 800, cy: 1010, r: 200 });
const izg = G(S9b); izg.setAttribute("clip-path", "url(#iz)");
pop(E(izg, "rect", { x: 600, y: 810, width: 400, height: 400, fill: "#fff" }, "h"), 50.2);
pop(E(izg, "rect", { x: 700, y: 760, width: 120, height: 370, fill: "#FFE27A", stroke: "#111", "stroke-width": 7 }, "h"), 50.2);
pop(P(izg, "M600 1130 L1000 1130", "l"), 50.2); pop(P(izg, "M600 1060 L1000 1060", "r"), 50.2);
E(S9b, "circle", { cx: 800, cy: 1010, r: 200 }, "l h"); pop(S9b.lastChild, 50.2);
pop(E(S9b, "circle", { cx: 470, cy: 1246, r: 30 }, "l h"), 50.2); pop(P(S9b, "M498 1236 L630 1150", "l"), 50.2);
pop(TX(S9b, 800, 790, "ZOOM ×10", 40), 50.2); pop(TX(S9b, 905, 1050, "1 W", 40, "red"), 50.2);
const dm = E(izg, "circle", { cx: 760, cy: 1100, r: 14 }, "h"); dm.style.fill = AMB; dm.style.stroke = "#111"; dm.style.strokeWidth = 5; pop(dm, 50.55);
const lt2 = TX(S9b, 800, 1180, "< 1 W", 50); lt2.style.fill = AMB; pop(lt2, 50.55);

// ---------- B17 "700 needed, under one delivered" 51.4-54.5: same linear scale, amber mark from the friction scene ----------
const S9c = scene(51.4, 54.44);
const rul2 = G(S9c); P(rul2, `M220 ${RY(0)} L220 ${RY(1000)}`); for (let w = 0; w <= 1000; w += 100) P(rul2, `M220 ${RY(w)} L${w % 500 === 0 ? 256 : 240} ${RY(w)}`).style.strokeWidth = 5;
[[0, "0"], [500, "500"], [1000, "1000 W"]].forEach(([w, s]) => { const t = TX(rul2, 204, RY(w) + 14, s, 36); t.style.textAnchor = "end"; }); show(rul2, 51.4);
const nb = E(S9c, "rect", { x: 330, y: 1300, width: 140, height: 0, stroke: "#111", "stroke-width": 7 }, "g h"); pop(nb, 51.46); tl.to(nb, { attr: { y: RY(700), height: 700 }, duration: 0.5, ease: "power2.out" }, 51.46);
pop(TX(S9c, 440, 480, "700 W", 80), 51.46); pop(TX(S9c, 440, 540, "NEEDED", 48), 51.5);
const sl = E(S9c, "rect", { x: 750, y: 1297, width: 100, height: 3, fill: AMB }, "h"); pop(sl, 52.52);
const dl = TX(S9c, 800, 1245, "< 1 W", 80); dl.style.fill = AMB; pop(dl, 52.52); pop(TX(S9c, 800, 1360, "DELIVERED", 50), 53.32);
const izc2 = E(world, "clipPath", { id: "iz2" }); E(izc2, "circle", { cx: 800, cy: 800, r: 190 });
const izg2 = G(S9c); izg2.setAttribute("clip-path", "url(#iz2)");
pop(E(izg2, "rect", { x: 610, y: 610, width: 380, height: 380, fill: "#fff" }, "h"), 52.84);
pop(P(izg2, "M610 900 L990 900", "l"), 52.84); pop(P(izg2, "M610 830 L990 830", "r"), 52.84);
const im = E(izg2, "rect", { x: 750, y: 868, width: 100, height: 32, fill: AMB, stroke: "#111", "stroke-width": 5 }, "h"); pop(im, 52.84);
E(S9c, "circle", { cx: 800, cy: 800, r: 190 }, "l h"); pop(S9c.lastChild, 52.84); pop(P(S9c, "M800 1285 L800 992", "l"), 52.84);
pop(TX(S9c, 800, 590, "ZOOM ×70", 40), 52.84); pop(TX(S9c, 935, 812, "1 W", 40, "red"), 52.84);

// ---------- B18 heat in = heat out 54.44-60.4 ----------
const S10 = scene(54.44, 60.4);
const m10 = mug(S10, 540, 800, 1.3); const sp10 = spoon(S10, m10, 1100); show(m10.g, 54.44); pop(sp10, 54.44);
stirArm(S10, m10, sp10, 54.44, 60.4, 10, { str: 0.35 });
const th10 = thermo(S10, 920, 520, 1220, 20); for (const i of th10.items) pop(i, 54.44); mercTo(th10, 21.4, 55.04, 2.3);
const ain = D(S10, "M610 640 L610 960", "l"); ink(ain, AMB, 14); draw(ain, 55.04, 0.25); const ainh = P(S10, "M582 930 L610 972 L638 930", "l"); ink(ainh, AMB, 14); pop(ainh, 55.25);
pop(TX(S10, 690, 690, "IN", 64, "red"), 55.04);
const outs = [[420, 975, "u"], [540, 975, "u"], [660, 975, "u"], [352, 1100, "l"], [352, 1190, "l"], [728, 1100, "r"], [728, 1190, "r"]];
outs.forEach(([x, y, k], i) => { const g = G(S10); const d = k === "u" ? wave(x, y, 150) : k === "l" ? `M${x} ${y} L${x - 110} ${y}` : `M${x} ${y} L${x + 110} ${y}`;
  const pth = P(g, d, "l"); ink(pth, AMB, 9); if (k === "l") P(g, `M${x - 82} ${y - 22} L${x - 112} ${y} L${x - 82} ${y + 22}`, "l"), ink(g.lastChild, AMB, 9); if (k === "r") P(g, `M${x + 82} ${y - 22} L${x + 112} ${y} L${x + 82} ${y + 22}`, "l"), ink(g.lastChild, AMB, 9);
  tl.set(g, { scale: 0.3, svgOrigin: `${x} ${y}` }, 0); show(g, 56.52 + i * 0.1); tl.to(g, { scale: 1, duration: 1.7, ease: "power1.out" }, 56.52 + i * 0.1); }); // the cup's losses grow until out = in
pop(TX(S10, 540, 380, "HEAT OUT", 70), 56.9); pop(TX(S10, 540, 500, "IN = OUT", 80, "red"), 58.46);

// ---------- B19 "So stir faster. Far faster than any hand." 60.4-62.5 hand limit, then HYPOTHETICAL motor rig ----------
const ghost = (S, m, a, t) => { const gs = G(S), x = m.X(410); P(gs, `M${x} ${m.Y(730)} L${x} ${m.Y(1066)}`).classList.remove("h"); E(gs, "ellipse", { cx: x, cy: m.Y(1100), rx: 24 * m.s, ry: 36 * m.s }, "l").classList.remove("h"); for (const c of gs.children) { c.style.strokeOpacity = 0.35; c.style.strokeWidth = 4; } gs.setAttribute("class", "h"); gs.setAttribute("transform", `rotate(${a} ${x} ${m.Y(900)})`); pop(gs, t); return gs; };
const S11a = scene(60.4, 62.5);
const m11 = mug(S11a, 540, 800, 1.3); const sp11 = spoon(S11a, m11, 1100); show(m11.g, 60.4); pop(sp11, 60.4);
stirArm(S11a, m11, sp11, 60.4, 62.5, 18, { rev: 2.6, str: 0.9, kf: (T) => 1 + 0.5 * Math.min(1, (T - 60.4) / 1.5) });
[[-22, 60.6], [22, 60.6], [-11, 60.7], [11, 60.7]].forEach(([a, t]) => ghost(S11a, m11, a, t));
pop(TX(S11a, 540, 330, "HAND LIMIT", 110, "red"), 61.18); pop(P(S11a, "M375 480 L345 450 M485 480 L515 450 M330 560 L290 560", "r"), 61.6);
const S11b = scene(62.5, 67.2);
const m11b = mug(S11b, 540, 900, 1.3); const sp11b = spoon(S11b, m11b, 1100); show(m11b.g, 62.5); pop(sp11b, 62.5);
pop(P(S11b, "M300 1371 L780 1371 L780 1400 L300 1400 Z", "f"), 62.5); [330, 750].forEach((x) => pop(E(S11b, "circle", { cx: x, cy: 1386, r: 8 }, "f h"), 62.5));
pop(P(S11b, "M290 1371 L290 560 L410 560", "l"), 62.5); pop(P(S11b, "M410 520 L670 520 L670 640 L410 640 Z", "f"), 62.5); pop(TX(S11b, 540, 598, "MOTOR", 54), 62.5);
stir(sp11b, m11b, 62.5, 67.2, 14, { rev: 3.4, str: 1.3 });
pop(TX(S11b, 540, 400, "HYPOTHETICAL", 100, "red"), 62.5);
[[-22, 62.7], [22, 62.7], [-14, 63.2], [14, 63.2], [-7, 63.9], [7, 63.9]].forEach(([a, t]) => ghost(S11b, m11b, a, t));
pop(TX(S11b, 540, 480, "TENS OF THOUSANDS OF STROKES / s", 40), 63.02);
pop(P(S11b, "M300 880 L370 880 M710 880 L780 880 M300 930 L370 930", "r"), 64.4);

// ---------- B20-B21 cavitation close-up 67.2-71.2: submerged spoon, low-pressure wake, bubbles appear in the patch, then collapse as pressure recovers ----------
const S12 = scene(67.2, 71.23);
pop(E(S12, "rect", { x: 60, y: 560, width: 730, height: 700, fill: "#E4E4E4", stroke: "#111", "stroke-width": 7 }, "h"), 67.2);
const vpt = E(S12, "ellipse", { cx: 320, cy: 910, rx: 105, ry: 135, fill: VIO, "fill-opacity": 0.28, stroke: VIO, "stroke-width": 6, "stroke-dasharray": "12 12" }, "h"); pop(vpt, 68.55); // low-pressure patch on the trailing side
pop(P(S12, "M470 440 L470 790", "l"), 67.2); const bw = E(S12, "ellipse", { cx: 470, cy: 910, rx: 48, ry: 125 }, "f h"); pop(bw, 67.2);
const sarr = arrow(S12, 520, 500, 740, 500, "l"); pop(sarr, 68.0); pop(TX(S12, 640, 450, "SPOON", 44), 68.0);
const lanes = [650, 725, 1050, 1125, 1200]; const tr12 = lanes.flatMap((y0, i) => [0, 1, 2].map((k) => ({ y0, x0: 90 + ((i * 97 + k * 260) % 700), c: ink(E(S12, "path", { d: "M0 0" }, "l"), TEAL, 6) })));
const trg = G(S12); pop(trg, 67.2); tr12.forEach((d) => { trg.appendChild(d.c); d.c.classList.remove("h"); });
const tu = (t) => tr12.forEach((d) => { const x = 90 + ((((d.x0 - 90) - 260 * t) % 700) + 700) % 700, sg = d.y0 < 910 ? -1 : 1, dy = sg * 34 * Math.exp(-(((x - 470) / 130) ** 2)); d.c.setAttribute("d", `M${x.toFixed(1)} ${(d.y0 + dy).toFixed(1)} L${(x + 30).toFixed(1)} ${(d.y0 + dy).toFixed(1)}`); });
tu(0); const tpx = { t: 0 }; tl.to(tpx, { t: 4, duration: 4, ease: "none", onUpdate: () => tu(tpx.t) }, 67.2);
const bubs12 = [{ t0: 67.6, P: 9, y0: 905, ph: 0, once: 1 }, ...[69.5, 69.7, 69.9].map((t0, i) => ({ t0, P: 1.5, y0: 860 + i * 55, ph: i })), ...[70.3, 70.42, 70.54, 70.66, 70.78].map((t0, i) => ({ t0, P: 1.4, y0: 840 + i * 38, ph: i * 2 }))].map((b) => ({ ...b, c: (() => { const c = E(S12, "circle", { cx: 440, cy: 900, r: 1 }, "f"); c.style.opacity = 0; c.style.strokeWidth = 5; return c; })() }));
const bu = (T) => bubs12.forEach((b) => { const a = T - b.t0; if (a < 0 || (b.once && a > 1.1)) { b.c.style.opacity = 0; return; } const u = ((a % b.P) / b.P) * (b.once ? 9 : 1); if (u > 1) { b.c.style.opacity = 0; return; }
  b.c.style.opacity = 1; b.c.setAttribute("cx", (430 - u * 300).toFixed(1)); b.c.setAttribute("cy", (b.y0 + 14 * Math.sin(b.ph + u * 6)).toFixed(1)); b.c.setAttribute("r", Math.max(0.5, 17 * Math.sin(Math.PI * Math.min(1, u)) ** 0.8).toFixed(1)); });
bu(0); const bx12 = { t: 67.2 }; tl.to(bx12, { t: 71.2, duration: 4, ease: "none", onUpdate: () => bu(bx12.t) }, 67.2);
pop(TX(S12, 450, 1385, "CAVITATION", 100), 67.2); const lp12 = TX(S12, 270, 530, "LOW PRESSURE", 40); lp12.style.fill = VIO; pop(lp12, 68.55);
pop(P(S12, "M850 640 L850 860 L880 860 L880 640 Z", "l"), 68.0); pop(TX(S12, 885, 600, "PRESSURE", 32), 68.0);
const pm = E(S12, "rect", { x: 853, y: 650, width: 24, height: 10, fill: VIO }, "h"); pop(pm, 68.0); tl.to(pm, { attr: { y: 840 }, duration: 0.45, ease: "power2.in" }, 68.55); tl.to(pm, { attr: { y: 720 }, duration: 0.8, ease: "power1.out" }, 70.7);
const th12 = thermo(S12, 990, 640, 1100, 20, false); for (const i of th12.items) pop(i, 67.2); pop(TX(S12, 990, 1230, "20 °C", 44), 67.2);

// ---------- B22 split screen 71.23-74.6: HEATING (approved boiling shot) vs LOW PRESSURE ----------
const S13 = scene(71.23, 74.6);
boilPot(S13, 71.23, 3.4, { tf: "translate(0 330) scale(0.5)", t100: 72.11 });
pop(P(S13, "M540 470 L540 1330", "l"), 71.23); S13.lastChild.style.stroke = "#9A9A9A";
pop(TX(S13, 270, 520, "HEATING", 80), 72.11);
const m13 = mug(S13, 810, 745, 0.8); const sp13 = spoon(S13, m13, 1100); show(m13.g, 71.23); pop(sp13, 71.23); stir(sp13, m13, 71.23, 74.6, 14, { rev: 3, str: 1.2 });
[[790, 880, 6], [842, 900, 8], [800, 940, 7], [836, 952, 9], [774, 920, 5], [852, 860, 5]].forEach(([x, y, r], i) => pop(E(S13, "circle", { cx: x, cy: y, r }, "f h"), 73.32 + i * 0.1));
const vp13 = E(S13, "ellipse", { cx: 810, cy: 910, rx: 80, ry: 80, fill: VIO, "fill-opacity": 0.2, stroke: VIO, "stroke-width": 5, "stroke-dasharray": "10 10" }, "h"); pop(vp13, 73.32);
const lp13 = TX(S13, 810, 520, "LOW PRESSURE", 50); lp13.style.fill = VIO; pop(lp13, 73.32);
const th13 = thermo(S13, 1010, 700, 1100, 20, false); for (const i of th13.items) pop(i, 71.23); pop(TX(S13, 1000, 1235, "20 °C", 44), 71.23);
pop(TX(S13, 785, 1330, "NOT HEAT", 68, "red"), 74.18);

// ---------- B23 splashing 74.6-79.1 ----------
const S14 = scene(74.6, 79.1);
const m14 = mug(S14, 540, 900, 1.3); const sp14 = spoon(S14, m14, 1100); show(m14.g, 74.6); pop(sp14, 74.6);
pop(P(S14, "M300 1371 L780 1371 L780 1400 L300 1400 Z", "f"), 74.6); [330, 750].forEach((x) => pop(E(S14, "circle", { cx: x, cy: 1386, r: 8 }, "f h"), 74.6));
pop(P(S14, "M290 1371 L290 560 L410 560", "l"), 74.6); pop(P(S14, "M410 520 L670 520 L670 640 L410 640 Z", "f"), 74.6); pop(TX(S14, 540, 598, "MOTOR", 54), 74.6);
pop(P(S14, "M60 1400 L1040 1400", "l"), 74.6);
stir(sp14, m14, 74.6, 79.1, 14, { rev: 3.4, str: 1.3, lvl: (T) => 130 * Math.min(1, Math.max(0, (T - 75.3) / 3.4)) ** 1.3 });
pop(TX(S14, 540, 400, "SPLASH", 100), 75.5);
const drops = Array.from({ length: 14 }, (_, i) => ({ ti: 75.2 + i * 0.22, vx: 140 + (i * 53 % 280), vy: -(620 + (i * 71 % 300)), e: (() => { const c = E(S14, "circle", { cx: 0, cy: 0, r: 8 + (i % 3) * 3 }, "f"); c.style.opacity = 0; return c; })(), fl: (() => { const f = E(S14, "ellipse", { cx: 0, cy: 1394, rx: 3, ry: 5 }, "g"); f.style.opacity = 0; return f; })() }));
const du = (T) => drops.forEach((d) => { const a = T - d.ti; if (a < 0) { d.e.style.opacity = 0; d.fl.style.opacity = 0; return; } const x = 640 + d.vx * Math.min(a, 1.4), y0 = 800 + d.vy * a + 0.5 * 1800 * a * a;
  if (y0 < 1390) { d.e.style.opacity = 1; d.e.setAttribute("cx", x.toFixed(1)); d.e.setAttribute("cy", y0.toFixed(1)); d.fl.style.opacity = 0; }
  else { d.e.style.opacity = 0; const tl2 = a - Math.sqrt(2 * 0) ; d.fl.style.opacity = 1; d.fl.setAttribute("cx", x.toFixed(1)); d.fl.setAttribute("rx", Math.min(48, 6 + 40 * Math.min(1, (T - (d.ti + 1.0)) * 1.5 + 0.2)).toFixed(1)); } });
du(75); const dx = { t: 75 }; tl.to(dx, { t: 79.1, duration: 4.1, ease: "none", onUpdate: () => du(dx.t) }, 75);
const area = E(S14, "ellipse", { cx: 870, cy: 1394, rx: 190, ry: 26, fill: "none", stroke: AMB, "stroke-width": 6, "stroke-dasharray": "14 12" }, "h"); pop(area, 76.4); pop(TX(S14, 870, 1455, "MORE AREA", 44), 76.4);
[800, 880, 960].forEach((x, i) => pop(ink(P(S14, wave(x, 1370, 190), "l"), AMB, 8), 76.99 + i * 0.12)); pop(TX(S14, 870, 1520, "WARMTH OUT", 44), 77.3); pop(TX(S14, 870, 1575, "(qualitative)", 34), 77.8);

// ---------- B24-B25 tea experiment 79.1-83.97 ----------
const S15 = scene(79.1, 83.97);
const cxs = [170, 520, 870], labs = ["STIR", "DIP", "NOTHING"], mugs15 = [], sps15 = [];
cxs.forEach((cx, i) => {
  const mg = mug(S15, cx, 800, 0.75); const sp = spoon(S15, mg, 1100); show(mg.g, 79.1); pop(sp, 79.1); mugs15.push(mg); sps15.push(sp);
  pop(P(S15, `M${cx + 60} 610 L${cx + 60} 990`, "l"), 79.1); pop(E(S15, "rect", { x: cx - 80, y: 520, width: 160, height: 90 }, "f h"), 79.1);
  pop(TX(S15, cx, 590, "80 °C", 50), 80.09 + i * 0.1); pop(TX(S15, cx, 1130, labs[i], 52), 79.5 + i * 0.1);
});
pop(E(S15, "rect", { x: 380, y: 330, width: 320, height: 120 }, "f h"), 79.1); const clk = TX(S15, 540, 420, "0:00", 90); pop(clk, 79.1);
const kc = { s: 0 }; tl.to(kc, { s: 600, duration: 5.9, ease: "none", onUpdate: () => { const s = Math.floor(kc.s); clk.textContent = Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); } }, 80.09); // shared clock
stir(sps15[0], mugs15[0], 81.18, 83.97, 12, { rev: 1.6, str: 0.8 });
[0, 1].forEach((k) => { tl.to(sps15[1], { y: -70, duration: 0.3, ease: "power1.out" }, 81.8 + k * 0.7); tl.to(sps15[1], { y: 0, duration: 0.3, ease: "power1.in" }, 82.1 + k * 0.7); });
const dp = E(S15, "circle", { cx: 520, cy: 960, r: 9 }, "f h"); pop(dp, 82.1); tl.to(dp, { y: 60, duration: 0.22, ease: "power2.in" }, 82.1); off(dp, 82.35); const dp2 = E(S15, "circle", { cx: 520, cy: 960, r: 9 }, "f h"); pop(dp2, 82.8); tl.to(dp2, { y: 60, duration: 0.22, ease: "power2.in" }, 82.8); off(dp2, 83.03);
tl.to(sps15[2], { y: -260, duration: 0.3, ease: "power1.in" }, 82.92); off(sps15[2], 83.25);
{ const rs = G(S15); P(rs, "M740 1060 L650 1060"); E(rs, "ellipse", { cx: 625, cy: 1060, rx: 26, ry: 14 }, "f h"); show(rs, 83.25); }

// ---------- B26 chart: three cooling traces drawn together 83.97-86.02 ----------
const S15c = scene(83.97, 86.02);
pop(P(S15c, "M170 1150 L930 1150 M170 1150 L170 560", "l"), 83.97); pop(TX(S15c, 115, 540, "°C", 44), 83.97); pop(TX(S15c, 550, 1225, "TIME", 48), 83.97);
pop(TX(S15c, 540, 470, "ILLUSTRATIVE", 60, "red"), 83.97);
const ser = [[TEAL, 1.65, "STIR"], [AMB, 1.85, "DIP"], ["#444", 1.45, "NOTHING"]];
const crv = ser.map(([c, k]) => ({ k, c: ink(P(S15c, "M0 0", "l"), c, 9) })); crv.forEach((s) => pop(s.c, 83.97));
const cd = (k, p) => { let d = ""; for (let j = 0; j <= 40; j++) { const u = j / 40 * p; d += (j ? "L" : "M") + (190 + 720 * u).toFixed(1) + " " + (600 + 330 * (1 - Math.exp(-u * k)) / (1 - Math.exp(-k))).toFixed(1); } return d; };
const cu = (p) => crv.forEach((s) => s.c.setAttribute("d", cd(s.k, p))); cu(0); const cpx = { p: 0 }; tl.to(cpx, { p: 1, duration: 1.4, ease: "none", onUpdate: () => cu(cpx.p) }, 84.1);
ser.forEach(([c, k, lab], i) => { const x = [150, 450, 740][i]; pop(ink(P(S15c, `M${x} 1300 L${x + 55} 1300`, "l"), c, 9), 84.1); const t = TX(S15c, x + 68, 1315, lab, 40); t.style.textAnchor = "start"; pop(t, 84.1); });

// ---------- B27-B28 answer 86.02-93.1: open-cup question, the swirl settles, the needle stays ----------
const S16 = scene(86.02, 93.08);
const h16 = hookLayout(S16, 86.02); tl.set(h16.sp, { opacity: 0 }, 86.02); pop(h16.sp, 86.32);
const r16a = stirArm(S16, h16.m, h16.sp, 86.32, 88.71, 12, { stop: 88.33, kf: (T) => T < 88.33 ? 1 : Math.max(0, 1 - (T - 88.33) / 0.35), restore: true, armEnd: 90.95 });
const r16b = stirArm(S16, h16.m, h16.sp, 91.0, 93.1, 16, { kf: (T) => 1 + 0.9 * Math.min(1, (T - 91.0) / 0.4), armStart: 90.95 });
pop(TX(S16, 900, 1400, "20 °C", 60), 86.02);
const olab = TX(S16, 650, 612, "ORDINARY SPOON", 38); pop(olab, 86.32); off(olab, 88.2);
tl.to(h16.m.items[4], { attr: { ry: 50 }, duration: 0.3, ease: "power1.out" }, 87.56); const clab = TX(S16, 700, 710, "OPEN CUP", 46); pop(clab, 87.56); off(clab, 89.4); const car = arrow(S16, 640, 725, 615, 750, "l"); pop(car, 87.56); off(car, 89.4);
const n16 = TX(S16, 430, 330, "NO.", 200, "red"); pop(n16, 88.33); off(n16, 89.5);
pop(TX(S16, 430, 440, "STILL ROOM TEMP", 60), 89.63); pop(P(S16, "M835 1094 L965 1094", "r"), 89.79);
pop(P(S16, "M375 500 L345 470 M485 500 L515 470", "r"), 91.6); off(S16.lastChild, 92.9);

// ---------- B29 sugar + job description 93.08-98.33 ----------
const S17 = scene(93.08, 98.33);
const m17 = mug(S17, 360, 900, 1.0); const sp17 = spoon(S17, m17, 1100); show(m17.g, 93.08); pop(sp17, 93.08);
stirArm(S17, m17, sp17, 93.3, 96.8, 10, { kf: (T) => T < 96.4 ? 1 : Math.max(0, 1 - (T - 96.4) / 0.3), stop: 96.4, armEnd: 96.8 }); off(sp17, 96.8);
const grains = Array.from({ length: 16 }, (_, i) => ({ ti: 93.3 + i * 0.12, x: 360 - 90 + (i * 37 % 180), r: 6 + (i % 3), e: (() => { const c = E(S17, "rect", { x: 0, y: 0, width: 12, height: 12 }, "f"); c.style.opacity = 0; c.style.strokeWidth = 3; return c; })() }));
const gu = (T) => grains.forEach((g) => { const a = T - g.ti; if (a < 0 || a > 1.9) { g.e.style.opacity = 0; return; } let x = g.x, y, s = 1, o = 1; if (a < 0.4) y = 600 + 350 * (a / 0.4) ** 2; else { const b = a - 0.4; y = 950 + 120 * (b / 1.5) ** 0.7; x = 360 + (g.x - 360) * Math.cos(2.5 * b); s = Math.max(0.1, 1 - b / 1.5); o = Math.max(0, 1 - b / 1.5); }
  g.e.style.opacity = o; g.e.setAttribute("x", (x - 6 * s).toFixed(1)); g.e.setAttribute("y", (y - 6 * s).toFixed(1)); g.e.setAttribute("width", (12 * s).toFixed(1)); g.e.setAttribute("height", (12 * s).toFixed(1)); });
gu(0); const gx17 = { t: 93.08 }; tl.to(gx17, { t: 96, duration: 2.92, ease: "none", onUpdate: () => gu(gx17.t) }, 93.08);
pop(TX(S17, 360, 1330, "SUGAR", 80), 94.66);
const card = G(S17); P(card, "M560 700 L1060 700 L1060 960 L560 960 Z", "f");
TX(card, 830, 780, "JOB: DISSOLVE SUGAR", 34); TX(card, 810, 900, "BOIL WATER", 40); P(card, "M578 772 L594 796 L624 740", "r");
tl.set(card, { y: 180 }, 0); show(card, 96.4); tl.to(card, { y: 0, duration: 0.25, ease: "power2.out" }, 96.4);
draw(D(S17, "M640 892 L980 892", "r"), 96.9, 0.2);
const rsp = G(S17); P(rsp, "M560 1255 L700 1255"); E(rsp, "ellipse", { cx: 725, cy: 1255, rx: 28, ry: 14 }, "f h"); show(rsp, 96.8);
const cl2 = P(S17, "M690 1215 L704 1195 M722 1212 L726 1190 M750 1222 L770 1206", "l"); pop(cl2, 96.8); off(cl2, 97.15);

// ---------- narrator: Codex alien poses, 1-frame swaps on the spoken beat ----------
const PI = {};
function poses(list, end = 98.33) {
  list.forEach(([t, n], i) => {
    if (!PI[n]) { PI[n] = E(world, "image", { href: `assets/chr/p${String(n).padStart(2, "0")}.png`, x: -134, y: 1335, width: 768, height: 768 }); PI[n].style.opacity = 0; }
    tl.set(PI[n], { opacity: 1 }, t); tl.set(PI[n], { opacity: 0 }, i + 1 < list.length ? list[i + 1][0] : end);
  });
}
poses([[0, 1], [0.6, 3], [1.7, 1], [4.3, 12], [5.6, 11], [5.9, 5], [7.9, 1], [8.6, 4], [12.8, 5], [15.8, 10], [17.9, 2], [18.6, 4], [20.9, 6], [24.2, 11], [25.5, 8], [27.8, 1], [29.7, 4], [34.8, 6], [36.9, 10], [38.3, 8],
  [39.3, 2], [42.0, 11], [44.8, 9], [45.7, 5], [51.5, 11], [52.8, 12], [54.6, 1], [57.0, 7], [60.4, 8], [63.0, 10], [66.1, 5], [67.2, 11], [70.3, 2], [71.2, 12], [72.1, 6], [74.2, 11],
  [75.0, 1], [77.0, 4], [79.3, 5], [80.6, 11], [83.0, 7], [86.0, 1], [88.3, 12], [90.0, 9], [93.1, 10], [95.0, 13], [96.7, 2]]);

window.__timelines["main"] = tl;
tl.seek(0);
