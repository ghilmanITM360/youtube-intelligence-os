"""Arithmetic behind slot 04 (uniform airless sphere) and slot 05 (ball escape speed). Stdlib only. Run: python3 orbit_checks.py"""
import math
G=6.6743e-11
rho=2000.0; R=3000.0
g=4/3*math.pi*G*rho*R
vc=R*math.sqrt(4*math.pi*G*rho/3)
T=math.sqrt(3*math.pi/(G*rho))
Te=math.sqrt(3*math.pi/(G*5514.0))
print(f"toy world: g={g:.3e} m/s2 = {g/9.80665:.2e} g; v_circ={vc:.3f} m/s = {vc*3.6:.2f} km/h; escape={vc*math.sqrt(2):.3f} m/s; lap={T:.0f}s={T/60:.1f} min; Earth-density lap={Te:.0f}s={Te/60:.1f} min")
for f in (0.99,1.0,1.1):
    a=R/(2-f*f); apo=2*a-R
    print(f"launch level at {f:.2f} v_c: apoapsis radius {apo:.0f} m ({apo-R:+.0f} m relative to launch radius)")
for deg in (0.5,5):
    print(f"tilt {deg} deg at v_c: periapsis {R*math.sin(math.radians(deg)):.1f} m below launch radius; hop ~{T/2*(1-deg/90)/60:.0f} min")
print(f"friction-limited sprint (mu=1): {vc/g/60:.1f} min")
print(f"orbit radius for take-off speeds 2.0/3.0 m/s: {2.0/(vc/R)/1000:.2f}/{3.0/(vc/R)/1000:.2f} km")
# Phobos ball model
M=1.0637e16; Rp=11080.0
ve=math.sqrt(2*G*M/Rp); gp=G*M/Rp**2
print(f"Phobos ball: escape {ve:.2f} m/s = {ve*3.6:.1f} km/h; g={gp:.4f} m/s2; flight time for 2/3 m/s up: {2*2/gp/60:.1f}/{2*3/gp/60:.1f} min")
GMm=4.2828e13; rp=9.376e6
print(f"Mars at Phobos orbit: circular {math.sqrt(GMm/rp):.0f} m/s, escape {math.sqrt(2*GMm/rp):.0f} m/s, extra {math.sqrt(2*GMm/rp)-math.sqrt(GMm/rp):.0f} m/s")
print(f"light-day: {299792.458*86400/1e9:.3f} billion km = {299792.458*86400/149597870.7:.2f} au; Moon {384400/299792.458:.2f} s; Sun {149597870.7/299792.458/60:.2f} min")
