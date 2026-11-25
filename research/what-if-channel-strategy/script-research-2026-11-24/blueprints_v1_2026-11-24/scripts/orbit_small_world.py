"""LONG 2 - uniform spherical, non-rotating, airless toy world. Stdlib only. Run: python3 scripts/orbit_small_world.py
MODEL: sphere radius R, uniform density rho (so g = 4/3*pi*G*rho*R), point-mass external gravity (exact for a uniform sphere),
no rotation, no air, no terrain, no other bodies. G = 6.67430e-11 (CODATA 2018, recalled). Human launch speeds are ASSUMPTIONS.
Outputs: output/orbit_small_world.csv + stdout, including an RK4 cross-check of the analytic orbit.
"""
import math, csv, os
G=6.67430e-11
def world(R,rho):
    mu=G*rho*4/3*math.pi*R**3; g=mu/R**2; vc=math.sqrt(mu/R); ve=math.sqrt(2)*vc; T=2*math.pi*math.sqrt(R**3/mu)
    return mu,g,vc,ve,T
def horizontal_launch(R,mu,v):
    """horizontal launch at surface radius R with speed v. returns kind, periapsis, apoapsis, period(min) or flight time"""
    vc2=mu/R
    if v>=math.sqrt(2*vc2): return "escape",None,None,None
    # vis-viva + angular momentum: other apsis rho = R*v^2/(2*vc2 - v^2)
    r_other=R*v*v/(2*vc2-v*v)
    if v<math.sqrt(vc2): return "suborbital_hits_ground",r_other,R,None
    a=(R+r_other)/2; return "orbit_bound",R,r_other,2*math.pi*math.sqrt(a**3/mu)
def rk4_orbit(R,mu,v,dt):
    """integrate planar motion from (R,0) with velocity (0,v); return (min r, time to first return to angle 0 after 180deg)"""
    x,y,vx,vy=R,0.0,0.0,v; t=0; rmin=R; passed=False
    def f(x,y,vx,vy):
        r3=(x*x+y*y)**1.5; return vx,vy,-mu*x/r3,-mu*y/r3
    while t<5*2*math.pi*math.sqrt(R**3/mu):
        k1=f(x,y,vx,vy); k2=f(x+dt/2*k1[0],y+dt/2*k1[1],vx+dt/2*k1[2],vy+dt/2*k1[3])
        k3=f(x+dt/2*k2[0],y+dt/2*k2[1],vx+dt/2*k2[2],vy+dt/2*k2[3]); k4=f(x+dt*k3[0],y+dt*k3[1],vx+dt*k3[2],vy+dt*k3[3])
        px=y
        x+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; y+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        vx+=dt*(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6; vy+=dt*(k1[3]+2*k2[3]+2*k3[3]+k4[3])/6; t+=dt
        r=math.hypot(x,y); rmin=min(rmin,r)
        if y>=0 and px<0 and x>0: return rmin,t   # crossed back through the +x launch axis, moving counter-clockwise
    return rmin,None
if __name__=="__main__":
    rows=[]
    print("Period of a surface-skimming circular orbit T=sqrt(3*pi/(G*rho)) - independent of radius:")
    for rho in (1000,1900,2000,2700,5514):
        print(f"  rho={rho:5d} kg/m3  T={math.sqrt(3*math.pi/(G*rho))/60:6.1f} min")
    print("\nRadius at which circular speed equals a chosen human speed (rho=2000):")
    for vc in (1,2,3,5,8,10):
        k=math.sqrt(4*math.pi*G*2000/3); R=vc/k
        mu,g,vcc,ve,T=world(R,2000); rows.append(dict(rho=2000,R_m=round(R,1),g_ms2=g,vc_ms=vcc,vesc_ms=ve,T_min=T/60))
        print(f"  v_c={vc:4.1f} m/s -> R={R/1000:6.2f} km  g={g*1e3:6.2f} mm/s2 (={g/9.80665*100:5.3f}% of Earth)  v_esc={ve:5.2f} m/s  T={T/60:5.1f} min")
    print("\nWorked world: rho=2000, R=3000 m")
    R=3000.0; rho=2000; mu,g,vc,ve,T=world(R,rho)
    print(f"  g={g*1e3:.2f} mm/s2  v_c={vc:.3f} m/s  v_esc={ve:.3f} m/s  T={T/60:.1f} min  (jump of 3 m/s vertical: height v^2/2g={3**2/2/g:.0f} m (flat-g approx; exceeds R? {3**2/2/g>R}); true: v>v_esc? {3>ve})")
    for v in (0.5*vc,0.9*vc,0.99*vc,1.0*vc,1.01*vc,1.1*vc,1.3*vc,0.99*ve,1.0001*ve):
        kind,a,b,per=horizontal_launch(R,mu,v)
        s=f"  launch {v:5.3f} m/s ({v/vc:5.3f} v_c): {kind}"
        if kind=="suborbital_hits_ground": s+=f"; periapsis would be {a:7.1f} m from centre = {R-a:6.1f} m BELOW the surface"
        if kind=="orbit_bound": s+=f"; periapsis {a:.0f} m (launch point), apoapsis {b:.0f} m = {b-R:6.1f} m above surface, period {per/60:.1f} min"
        print(s)
    print("\nWhere is the periapsis (closest approach) of the conic through the launch point if the launch has an upward angle gamma? (R=3000 m world, rho=2000)")
    print("  Periapsis below the surface = the orbit would plough through the ground on the way round. Only a (near-)horizontal launch keeps periapsis >= R.")
    for u in (1.1,1.3):
        for gd in (0,0.5,1,2,5,10,45):
            c2=math.cos(math.radians(gd))**2; disc=1-2*u*u*c2*(1-u*u/2); xmax=(1+math.sqrt(disc))/(u*u*c2)
            print(f"    speed {u*vc:5.3f} m/s ({u} v_c), elevation {gd:4.1f} deg: periapsis {R/xmax:8.1f} m from centre ({R/xmax-R:+8.1f} m vs surface)")
    print("  Clearance: a jumper's centre of mass starts ~1 m above the ground; a horizontal launch there at the local circular speed keeps periapsis at ~R+1 m: any rock/bump taller than ~1 m on the path blocks it.")
    print("\nBallistic hop (RK4) for sub-orbital launches, R=3000 m, rho=2000, launch at 45 deg elevation:")
    for u in (0.2,0.5,0.9):
        v=u*vc; x,y=R,0.0; vx,vy=v*math.sin(math.radians(45)),v*math.cos(math.radians(45)); t=0; dt=0.5
        # local frame: x radial, y tangential
        def f(x,y,vx,vy):
            r3=(x*x+y*y)**1.5; return vx,vy,-mu*x/r3,-mu*y/r3
        while True:
            k1=f(x,y,vx,vy); k2=f(x+dt/2*k1[0],y+dt/2*k1[1],vx+dt/2*k1[2],vy+dt/2*k1[3])
            k3=f(x+dt/2*k2[0],y+dt/2*k2[1],vx+dt/2*k2[2],vy+dt/2*k2[3]); k4=f(x+dt*k3[0],y+dt*k3[1],vx+dt*k3[2],vy+dt*k3[3])
            x+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; y+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
            vx+=dt*(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6; vy+=dt*(k1[3]+2*k2[3]+2*k3[3]+k4[3])/6; t+=dt
            if math.hypot(x,y)<=R and t>dt: break
        print(f"    {v:5.3f} m/s ({u} v_c): lands after {t/60:6.1f} min, {math.atan2(y,x)*R/1000:6.3f} km along the surface")
    print("\nRK4 cross-check, 1.1 v_c launch, R=3000 m, rho=2000:")
    v=1.1*vc; kind,a,b,per=horizontal_launch(R,mu,v); rmin,t=rk4_orbit(R,mu,v,0.5)
    print(f"  analytic period {per:.1f} s, apo {b:.1f} m ; RK4: min r {rmin:.1f} m (>=R means no ground contact), return-through-launch-axis time {t}")
    print("\nRotation: equatorial speed that equals v_c means period T_spin = T_orbit (loose-surface limit): rho=2000 ->",round(math.sqrt(3*math.pi/(G*2000))/3600,2),"h")
    with open(os.path.join(os.path.dirname(__file__),"output","orbit_small_world.csv"),"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(r) for r in rows]
