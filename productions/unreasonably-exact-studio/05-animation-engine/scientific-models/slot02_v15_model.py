"""Fixed-posture vertical fall from rest at 10 km through the NASA Glenn troposphere fit.
Illustrative parameters (m, CdA) are assumptions, not a prediction for any real person."""
import math
M, G, CDA = 80.0, 9.8, 0.50          # kg, m/s^2, m^2  (assumed fixed belly-down posture)
def rho(h):
    T = 15.04 - 0.00649*h
    p = 101.29*((T+273.1)/288.08)**5.256
    return p/(0.2869*(T+273.1))
def simulate(h0=10000.0, dt=0.01):
    t, h, v, out = 0.0, h0, 0.0, []
    while h > 0:
        d = 0.5*rho(h)*v*v*CDA
        out.append((t, h, v, d/(M*G), rho(h)))
        a = G - d/M                   # downward positive
        v += a*dt; h -= v*dt; t += dt
    return out
TRACE = simulate()
def at_time(t):
    i = min(int(t/0.01), len(TRACE)-1); return TRACE[i]
PEAK = max(TRACE, key=lambda r: r[2])
END_T = TRACE[-1][0]
if __name__ == '__main__':
    t, h, v, ratio, r = PEAK
    print(f'peak speed {v:.1f} m/s at t={t:.1f}s h={h:.0f} m; drag/weight there {ratio:.3f}')
    for tt in [0,5,10,15,20,30,45,60,90,120,END_T-0.05]:
        t,h,v,ratio,r=at_time(tt); print(f't={t:6.1f}s h={h:7.0f} v={v:5.1f} D/W={ratio:5.3f} rho={r:.3f}')
    # checks: velocity never reverses; after peak D/W >= 1 (slowdown); speed at ground < peak
    assert all(row[2] >= 0 for row in TRACE)
    k = TRACE.index(PEAK)
    assert all(row[3] >= 0.999 for row in TRACE[k+10:])
    assert TRACE[-1][2] < PEAK[2]
    print('model checks pass; ground reached at', round(END_T,1), 's')
