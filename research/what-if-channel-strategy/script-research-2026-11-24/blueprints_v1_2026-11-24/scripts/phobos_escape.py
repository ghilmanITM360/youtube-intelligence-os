"""SHORT 3 - Phobos. Stdlib only. Run: python3 scripts/phobos_escape.py
INPUTS (sourced): Phobos mass 10.6e15 kg, semi-axes 13.0/11.4/9.1 km, a=9378 km, T=0.31891 d, Mars mass 0.64169e24 kg  [NASA NSSDC Mars fact sheet, read 2026-11-24];
 NASA KSC/JSC 2012 conference slides (Muscatello et al., NTRS 20120013420, slide 'Basic Properties'): escape velocity 11.3 m/s (40 km/h), surface-gravity entry garbled in text extraction (not used), rotation synchronous, mass 1.072e16 kg.
 G=6.67430e-11 (CODATA 2018, recalled).
MODEL (labelled, crude): point-mass Phobos inside a sphere of chosen radius, Mars as a distant point mass, Hill's equations (circular, planar-ish, r<<a).
 This IGNORES Phobos's irregular shape, its non-uniform gravity field, Mars's oblateness, eccentricity (0.015) and Mars's J2. It is an order-of-magnitude test, NOT a flight-grade result.
"""
import math, csv, os
G=6.67430e-11
mP=10.6e15; mP_alt=1.072e16; mM=0.64169e24
a=9378e3; T=0.31891*86400; n=2*math.pi/T
semi=(13.0e3,11.4e3,9.1e3); Rv=(semi[0]*semi[1]*semi[2])**(1/3)
mu=G*mP; muM=G*mM
def hill(mu_,a_,mM_): return a_*(mu_/(3*G*mM_))**(1/3)
rH=hill(mu,a,mM)
print(f"Rv (volume-equivalent radius) = {Rv/1000:.2f} km   mu_Phobos = {mu:.4g} m3/s2 (alt mass 1.072e16 -> {G*mP_alt:.4g})")
print(f"mean surface g = mu/Rv^2 = {mu/Rv**2*1e3:.2f} mm/s2   NASA 2012 slide text is garbled ('86Q-190 ~g') and its gravity range is inconsistent with its own mass and size -> NOT used")
for lab,R in (("polar semi-axis 9.1 km",semi[2]),("volume-equivalent",Rv),("sub-Mars semi-axis 13.0 km",semi[0])):
    print(f"  point-mass sphere R={R/1000:5.2f} km ({lab}): v_circ={math.sqrt(mu/R):5.2f} m/s  v_esc={math.sqrt(2*mu/R):5.2f} m/s = {math.sqrt(2*mu/R)*3.6:4.1f} km/h")
print(f"  mass 1.072e16 variant at Rv: v_esc={math.sqrt(2*G*mP_alt/Rv):.2f} m/s (NASA slides: 11.3 m/s)")
print("\nMars side:")
print(f"  mean motion n = {n:.4e} rad/s; Mars GM from NSSDC mass = {muM:.5g} m3/s2 ; consistency n^2 a^3 = {n*n*a**3:.5g} m3/s2 (ratio {n*n*a**3/muM:.4f})")
vorb=a*n; vesc_M=math.sqrt(2*muM/a)
print(f"  Phobos orbital speed about Mars = {vorb/1000:.3f} km/s ; Mars escape speed at that radius = {vesc_M/1000:.3f} km/s ; extra needed to leave Mars from Phobos's orbit = {(vesc_M-vorb):.0f} m/s")
print(f"  Hill radius of Phobos w.r.t. Mars = {rH/1000:.2f} km = {rH/Rv:.2f} x Rv ; = {rH/semi[0]:.2f} x the 13.0 km sub-Mars semi-axis (L1/L2 distance)")
# energy-based minimum speed to reach L1/L2 from surface points (Hill potential, sphere)
print("\nEnergy test (Hill potential Phi=-mu/r-1.5 n^2 x^2+0.5 n^2 z^2; L1/L2 at |x|=rH, Phi=-1.5 mu/rH). Minimum speed relative to Phobos's surface to REACH the pass:")
for lab,R in (("sphere 9.1 km",semi[2]),("sphere Rv",Rv),("sphere 13.0 km",semi[0])):
    PhiL=-1.5*mu/rH
    for d,(x,z) in {"Mars-ward/anti-Mars (x)":(R,0),"along orbit (y)":(0,0),"pole (z)":(0,R)}.items():
        Phi=-mu/R-1.5*n*n*x*x+0.5*n*n*z*z
        dE=PhiL-Phi
        print(f"  {lab:15s} {d:26s}: min speed to reach pass = {math.sqrt(2*dE):.3f} m/s" if dE>0 else f"  {lab:15s} {d:26s}: surface is already beyond the pass energy (dE={dE:.3g}) -> loose material escapes at rest in this model")
# numerical test
def sim(R,dirv,v,orbits=30,rcap=6):
    x,y,z=[R*c for c in dirv]; vx,vy,vz=[v*c for c in dirv]; t=0; tmax=orbits*T; left=False
    def f(s):
        x,y,z,vx,vy,vz=s; r3=(x*x+y*y+z*z)**1.5
        return (vx,vy,vz,2*n*vy+3*n*n*x-mu*x/r3,-2*n*vx-mu*y/r3,-n*n*z-mu*z/r3)
    s=(x,y,z,vx,vy,vz); rmax=R
    while t<tmax:
        r=math.sqrt(s[0]**2+s[1]**2+s[2]**2); dt=min(150.0,0.02*math.sqrt(r**3/mu))
        k1=f(s); k2=f(tuple(si+dt/2*ki for si,ki in zip(s,k1))); k3=f(tuple(si+dt/2*ki for si,ki in zip(s,k2))); k4=f(tuple(si+dt*ki for si,ki in zip(s,k3)))
        s=tuple(si+dt*(a1+2*a2+2*a3+a4)/6 for si,a1,a2,a3,a4 in zip(s,k1,k2,k3,k4)); t+=dt
        r=math.sqrt(s[0]**2+s[1]**2+s[2]**2); rmax=max(rmax,r)
        rdot=(s[0]*s[3]+s[1]*s[4]+s[2]*s[5])/r
        if r<=R and rdot<0: return "impact",t,rmax   # came back down to the surface
        if r>rcap*rH: return "far(>%gxrH)"%rcap,t,rmax
    return "still_near_after_%d_orbits"%orbits,t,rmax
DIRS={"toward Mars (-x)":(-1,0,0),"away from Mars (+x)":(1,0,0),"forward along orbit (+y)":(0,1,0),"backward (-y)":(0,-1,0),"up out of orbit plane (+z)":(0,0,1)}
rows=[]
print("\nNumerical test (radial launches from a surface point at rest in Phobos's rotating frame; 30 Phobos orbits ~ 9.6 days):")
for lab,R in (("sphere 9.1 km",semi[2]),("sphere Rv",Rv),("sphere 13.0 km",semi[0])):
    for dn,dv in DIRS.items():
        out=[]
        for v in (0.5,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.4):
            res,t,rmax=sim(R,dv,v); out.append(f"{v:g}:{res.split('_')[0][:5]}"); rows.append(dict(sphere=lab,R_km=round(R/1000,2),direction=dn,v_ms=v,outcome=res,t_s=round(t),rmax_km=round(rmax/1000,1)))
        print(f"  {lab:14s} {dn:28s} "+"  ".join(out))
w=csv.DictWriter(open(os.path.join(os.path.dirname(__file__),"output","phobos_hill_sim.csv"),"w",newline=""),fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(r) for r in rows]
print("\nJump speed ASSUMPTIONS: a ~0.45 m jump on Earth is v=sqrt(2*9.80665*0.45)=%.2f m/s (assumption, unsourced); suited/loaded jumps lower."%math.sqrt(2*9.80665*0.45))
print("Uniform-gravity hang time for 3 m/s vertical on mean g=%.5f m/s2: %.1f min (NOT reliable here; see Hill sim)"%(mu/Rv**2,2*3/(mu/Rv**2)/60))
