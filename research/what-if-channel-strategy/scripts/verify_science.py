"""Independent recomputation of every quantitative claim in the 30-day calendar (report 06).

Inputs are constants from primary sources cited in 06_SCIENCE_VERIFICATION.md.
Run: uv run python scripts/verify_science.py   (prints all values; asserts are sanity checks)
"""
import math

G = 6.674e-11
AU = 149_597_870.7e3
LY = 9.4607e15
R_E = 6.371e6
M_E = 5.972e24
G0 = 9.80665

# ---------- US Standard Atmosphere 1976 (0-86 km layers, tabulated densities above) ----------
_LAYERS = [(0, 288.15, -6.5e-3), (11e3, 216.65, 0.0), (20e3, 216.65, 1.0e-3), (32e3, 228.65, 2.8e-3),
           (47e3, 270.65, 0.0), (51e3, 270.65, -2.8e-3), (71e3, 214.65, -2.0e-3), (84.852e3, 186.946, 0.0)]
_HIGH = [(86e3, 6.958e-6), (100e3, 5.604e-7), (120e3, 2.222e-8), (150e3, 2.076e-9),
         (200e3, 2.541e-10), (300e3, 1.916e-11), (400e3, 2.803e-12), (500e3, 5.215e-13)]


def atmosphere(h):
    """(density kg/m3, temperature K) at geometric altitude h (m). ponytail: isothermal above 86 km for T."""
    if h >= 86e3:
        for (h1, r1), (h2, r2) in zip(_HIGH, _HIGH[1:]):
            if h <= h2:
                return r1 * (r2 / r1) ** ((h - h1) / (h2 - h1)), 186.87
        return 0.0, 186.87
    hg = R_E * h / (R_E + h)  # geopotential altitude
    p, R, gm = 101325.0, 287.053, 9.80665
    for i, (hb, tb, lr) in enumerate(_LAYERS):
        top = _LAYERS[i + 1][0] if i + 1 < len(_LAYERS) else 1e9
        dh = min(hg, top) - hb
        if lr == 0:
            p_end = p * math.exp(-gm * dh / (R * tb))
        else:
            p_end = p * (1 + lr * dh / tb) ** (-gm / (R * lr))
        t_end = tb + lr * dh
        if hg <= top:
            return p_end / (R * t_end), t_end
        p = p_end


def fall(h0, cda_over_m, v0=0.0, dt=0.01, nose_r=None):
    """1-D vertical drop. Returns dict of peak speed, peak Mach, max decel (g), Sutton-Graves peak heat flux, heat load."""
    h, v, t = h0, v0, 0.0
    out = dict(vmax=0, h_at_vmax=h0, mach_max=0, decel_max=0, q_max=0, q_load=0, t_stag_max=0)
    while h > 0:
        rho, T = atmosphere(h)
        g = G0 * (R_E / (R_E + h)) ** 2
        drag = 0.5 * rho * v * v * cda_over_m
        a = g - drag
        v += a * dt
        h -= v * dt
        t += dt
        a_sound = math.sqrt(1.4 * 287.053 * T)
        if v > out["vmax"]:
            out.update(vmax=v, h_at_vmax=h)
        out["mach_max"] = max(out["mach_max"], v / a_sound)
        out["decel_max"] = max(out["decel_max"], drag / G0)
        out["t_stag_max"] = max(out["t_stag_max"], T * (1 + 0.2 * (v / a_sound) ** 2))
        if nose_r:
            q = 1.7415e-4 * math.sqrt(rho / nose_r) * v ** 3
            out["q_max"] = max(out["q_max"], q)
            out["q_load"] += q * dt
    out["t_total"] = t
    return out


def section(title):
    print(f"\n=== {title} ===")


# ---------- WIB-36 Free fall ----------
section("WIB-36 free fall")
# Calibrate suited-human CdA/m to Baumgartner: exit 38,969 m, FAI max 1,357.6 km/h (377.1 m/s).
lo, hi = 1e-4, 1e-2
for _ in range(40):
    mid = (lo + hi) / 2
    if fall(38_969, mid, dt=0.02)["vmax"] > 377.1:
        lo = mid
    else:
        hi = mid
k_stratos = (lo + hi) / 2
b = fall(38_969, k_stratos, dt=0.02)
print(f"calibrated CdA/m={k_stratos:.5f} m2/kg -> vmax {b['vmax']*3.6:.0f} km/h at {b['h_at_vmax']/1e3:.1f} km, Mach {b['mach_max']:.2f}")
assert abs(b["vmax"] - 377.1) < 1
k_belly = 2 * G0 / (1.225 * 55 ** 2)  # belly-to-earth terminal ~55 m/s at sea level
print(f"sea-level belly terminal 55 m/s -> CdA/m={k_belly:.4f}")
for h0 in [10, 100, 1e3, 10e3, 20e3, 30e3, 38_969, 41_422, 60e3, 100e3, 400e3]:
    r = fall(h0, k_stratos, dt=0.02 if h0 < 1e5 else 0.005, nose_r=0.3)
    print(f"drop {h0/1e3:>8.3f} km: vmax {r['vmax']*3.6:7.0f} km/h at {r['h_at_vmax']/1e3:6.1f} km, Mach {r['mach_max']:.2f}, "
          f"max decel {r['decel_max']:.1f} g, SG peak heat {r['q_max']/1e4:.1f} W/cm2, time {r['t_total']/60:.1f} min")
print("ISS orbital speed for comparison: 7.66 km/s horizontal (orbit = falling sideways fast enough to miss)")

# ---------- WIB-18 Steak drop ----------
section("WIB-18 steak drop")
steak_k = 1.1 * 0.02 / 0.3  # Cd 1.1, 0.02 m2 face, 0.3 kg
for h0 in [10e3, 30e3, 39e3, 50e3, 70e3, 100e3, 200e3, 400e3]:
    r = fall(h0, steak_k, dt=0.002, nose_r=0.07)
    print(f"steak from {h0/1e3:>5.0f} km: vmax {r['vmax']:6.0f} m/s, Mach {r['mach_max']:.2f}, stagnation T max {r['t_stag_max']-273.15:6.0f} C, "
          f"SG heat load {r['q_load']/1e4:8.1f} J/cm2")
cook = 0.01 * 1050 * 3500 * 40  # 1 cm layer, +40 K
print(f"energy to heat 1 cm surface layer by 40 K: {cook/1e4:.0f} J/cm2 (order-of-magnitude benchmark)")

# ---------- WIB-55 Neutron bullet ----------
section("WIB-55 neutron bullet")
m_sun = 1.989e30
for M, R in [(1.4, 11e3), (1.4, 12e3), (1.4, 13e3), (2.0, 12e3)]:
    print(f"mean density {M} Msun, R={R/1e3:.0f} km: {M*m_sun/(4/3*math.pi*R**3):.2e} kg/m3")
rho_sat = 0.16e45 * 1.6749e-27  # 0.16 fm^-3
print(f"nuclear saturation density: {rho_sat:.2e} kg/m3")
for rho in (rho_sat, 4e17, 1e18):
    tsp = 4.93e-6 * rho
    bullet = (8.0e-3 / 11340) * rho  # 8 g lead 9 mm bullet volume
    n = bullet / 1.6749e-27
    e_decomp = n * 16e6 * 1.602e-19  # ~16 MeV/neutron (pure-neutron-matter energy at saturation)
    e_beta = n * 0.782e6 * 1.602e-19
    print(f"rho={rho:.1e}: teaspoon {tsp/1e12:.1f} billion t (= {tsp/2.7e12:.1f} km3 of rock); bullet {bullet:.2e} kg; "
          f"g at 1 m {G*bullet:.0f} m/s2; decompression ~{e_decomp:.1e} J = {e_decomp/4.184e15:.1e} Mt; beta decay {e_beta:.1e} J")

# ---------- NEW-06 Moon vanishes ----------
section("NEW-06 Moon vanishes")
m_moon, d_moon, d_sun = 0.07346e24, 384_400e3, 149.6e9
ratio = (m_sun / m_moon) * (d_moon / d_sun) ** 3
print(f"solar/lunar tide-generating force = {ratio:.3f}")
print(f"tide range: sun-only vs spring = {ratio/(1+ratio):.0%}, vs neap = {ratio/(1-ratio):.0%}")
bary = d_moon * m_moon / (M_E + m_moon)
print(f"barycentre offset {bary/1e3:.0f} km from Earth centre; Earth wobble speed {2*math.pi*bary/(27.32*86400):.1f} m/s")

# ---------- WIB-22 Alien astronomers ----------
section("WIB-22 alien astronomers")
for d in (4.2465, 10, 100, 1000, 10000):
    theta = 2 * R_E / (d * LY)
    print(f"{d:>8} ly: sees Earth of {2026-d:.0f}; aperture to make Earth 1 resolved pixel at 550 nm: {1.22*550e-9/theta/1e3:,.1f} km")
print(f"Earth transit depth: {(6371/695700)**2*1e6:.0f} ppm")

# ---------- NEW-08 Light at 100 km/h ----------
section("NEW-08 slow light (c = 100 km/h)")
c = 100 / 3.6
for name, v in [("walk 5", 5), ("run 15", 15), ("cycle 25", 25), ("car 50", 50), ("car 90", 90), ("99 km/h", 99)]:
    beta = v / 100
    print(f"{name:>9} km/h: gamma {1/math.sqrt(1-beta**2):.3f}, approaching Doppler x{math.sqrt((1+beta)/(1-beta)):.2f}")
print(f"see someone 100 m away: {100/c:.1f} s late; Moon light {d_moon/c/86400:.0f} days; Sunlight {d_sun/c/3.156e7:.0f} years")
print(f"fine-structure constant would scale by {299792458/c:.2e} -> alpha ~ {299792458/c/137.036:.1e} (atoms impossible)")

# ---------- WIB-17 Little planet ----------
section("WIB-17 little planet")
for rho in (2000, 5514):
    k = math.sqrt(4 / 3 * math.pi * G * rho)
    for vj in (2.8, 3.4):
        r = vj / k
        g = 4 / 3 * math.pi * G * rho * r
        print(f"rho {rho}: orbit by {vj} m/s jump -> radius {r/1e3:.1f} km, g {g*1e3:.1f} mm/s2, period {2*math.pi*r/vj/60:.0f} min, "
              f"escape {vj*math.sqrt(2):.1f} m/s, max walk speed (Froude 0.5, leg 0.9 m) {math.sqrt(0.5*g*0.9)*100:.1f} cm/s")
print(f"vertical jump 0.4-0.6 m on Earth -> take-off {math.sqrt(2*G0*0.4):.1f}-{math.sqrt(2*G0*0.6):.1f} m/s")
print("Deimos (NASA): mean radius 6.2 km, escape 5.6 m/s; you cannot jump off it with ~3 m/s")

# ---------- WIB-11 Last light ----------
section("WIB-11 last light")
for years in (12.32, 25, 50):
    print(f"tritium sign after {years} y: {0.5**(years/12.32):.0%} of new brightness (decay only)")
print(f"Pm-147 (2.62 y) after 10 y: {0.5**(10/2.62):.0%}")
print(f"PV panel at 0.5%/y median degradation after 50 y: {(1-0.005)**50:.0%}")

# ---------- WIB-53 Raindrop ----------
section("WIB-53 storm as one drop")
for diam_km, depth_mm in [(5, 10), (10, 25), (20, 50)]:
    V = math.pi * (diam_km * 1e3 / 2) ** 2 * depth_mm / 1e3
    r = (3 * V / (4 * math.pi)) ** (1 / 3)
    for h in (2e3, 5e3):
        E = V * 1000 * G0 * h
        print(f"cell {diam_km} km x {depth_mm} mm: {V*1000/1e9:.2f} Mt water, drop diameter {2*r:.0f} m; from {h/1e3:.0f} km: "
              f"<= {math.sqrt(2*G0*h):.0f} m/s, {E:.1e} J = {E/4.184e12:.1f} kt TNT")

# ---------- WIB-24 Plane on every planet ----------
section("WIB-24 Cessna on every planet")
v_s_earth = 53 * 0.5144  # C172S stall, flaps up, max weight, KCAS -> m/s
titan_rho = 146_700 * 0.0280 / (8.314 * 93.65)  # Huygens HASI; N2-dominated M ~ 28 g/mol
for name, g, rho, a in [("Earth", 9.81, 1.225, 340), ("Venus surface", 8.87, 65, 410), ("Mars", 3.73, 0.016, 240),
                        ("Titan", 1.352, titan_rho, 194)]:
    vs = v_s_earth * math.sqrt((g / 9.81) * (1.225 / rho))
    print(f"{name:>14}: rho {rho:.3f} kg/m3 -> C172 stall {vs:6.1f} m/s ({vs*3.6:.0f} km/h, Mach {vs/a:.2f})")

# ---------- WIB-52 Loneliest human ----------
section("WIB-52 loneliest human")
r_moon = 1737.4
for alt in (110, 120):
    print(f"CSM at {alt} km, crew on surface at antipode: max separation {r_moon*2+alt:.0f} km")
print(f"Artemis II record 252,756 mi = {252756*1.609344:,.0f} km; Apollo 13 248,655 mi = {248655*1.609344:,.0f} km")

# ---------- T-01 Apophis ----------
section("T-01 Apophis")
d = 0.000254090910419299 * AU
print(f"JPL CAD: {d/1e3:,.0f} km from Earth centre = {(d-R_E)/1e3:,.0f} km above surface; GEO altitude 35,786 km; "
      f"Moon is {d_moon/d:.1f}x farther")

# ---------- NEW-07 Jupiter ----------
section("NEW-07 fall into Jupiter")
print("escape velocity 59.5 km/s (NASA): a fall from far away arrives at >= this speed")
print(f"Galileo probe 47.4 km/s, peak 228 g = {228/46.2:.1f}x the highest voluntary human sled exposure (Stapp, 46.2 g)")

# ---------- Day-29 defaults ----------
section("Day-29 defaults")
sigma = 3000 * G0 * R_E / 2  # thin self-gravitating shell membrane stress, rock density
print(f"Hollow Earth thin rock shell stress ~{sigma/1e9:.0f} GPa vs granite compressive strength ~0.2 GPa")
print(f"Gravity doubles (Earth mass x2, Moon speed unchanged): new perigee {d_moon/3/1e3:,.0f} km")
print("Time machine on one spot: Earth orbital speed 29.78 km/s -> 1 s jump = ~30 km displacement (frame must be stated)")
