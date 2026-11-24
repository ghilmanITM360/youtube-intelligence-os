"""LONG 1 / SHORT 1 - vertical fall from rest, quadratic drag, US-Standard-Atmosphere-1976-like density.
Stdlib only. Run: python3 scripts/fall_model.py  -> output/fall_results.csv + stdout.
MODEL (all labelled): 1-D, zero horizontal speed, no wind, constant CdA/m (posture fixed), no parachute,
g(h)=g0*(R/(R+h))^2, ground at sea level. Density: own implementation of USSA-1976 layers 0-86 km (constants from memory of the
standard, NOT re-read from the document) + log-interpolated table 86-120 km (values RECALLED from memory, not re-sourced) -> results
for release above ~86 km are LOW confidence. Cd held constant: real hypersonic/free-molecular drag differs.
CdA/m parameter sets (provenance matters; see 08 md):
  A  0.00505  calibrated in an earlier project fit to Baumgartner's peak speed (INHERITED; not independent)
  B  Cd 0.60, A 1.19 m2, m 121.2 kg -> 0.005891  Guerster & Walter 2017 PLoS ONE 12(12):e0187798, Sec. III/IV (read 2026-11-24 via PMC5720713 summary); subsonic Cd from flight data
  C  0.55 m2 / 90 kg = 0.006111  (assumed bracket, inherited from earlier review; unsourced)
  D  0.70 m2 / 90 kg = 0.007778  (assumed bracket, unsourced)
  E  0.60*0.525/121.2 = 0.002599 (smallest cross-section A_z of paper's suit axes -> head-down BOUND; stability of that posture NOT established)
"""
import math, csv, os
G0=9.80665; RE=6371000.0; R0=6356766.0
LAY=[(0,288.15,-6.5e-3,101325.0),(11000,216.65,0,22632.06),(20000,216.65,1.0e-3,5474.889),(32000,228.65,2.8e-3,868.0187),
     (47000,270.65,0,110.9063),(51000,270.65,-2.8e-3,66.93887),(71000,214.65,-2.0e-3,3.956420)]
TAB=[(86000,6.958e-6),(90000,3.416e-6),(100000,5.604e-7),(110000,9.708e-8),(120000,2.222e-8)]
RSPEC=287.053
def atm(hg):
    """geometric altitude m -> (rho, T)"""
    hg=max(hg,0.0)
    if hg>=86000:
        for (h1,r1),(h2,r2) in zip(TAB,TAB[1:]):
            if hg<=h2: return (math.exp(math.log(r1)+(math.log(r2)-math.log(r1))*(hg-h1)/(h2-h1)),186.87)
        return (TAB[-1][1]*math.exp(-(hg-120000)/8000.0),300.0)
    H=R0*hg/(R0+hg)
    b=max(i for i,l in enumerate(LAY) if l[0]<=H)
    Hb,Tb,L,Pb=LAY[b]
    if L==0:
        T=Tb; P=Pb*math.exp(-G0*(H-Hb)/(RSPEC*Tb))
    else:
        T=Tb+L*(H-Hb); P=Pb*(T/Tb)**(-G0/(RSPEC*L))
    return (P/(RSPEC*T),T)
def run(h0,cdam,dt=0.02):
    h=h0; v=0.0; t=0.0
    vmax=0; hpk=h0; tpk=0; amin=0; sup0=None; tsup=0; mmax=0; gmax_dec=0; felt=0
    def acc(h,v):
        rho,_=atm(h); g=G0*(RE/(RE+h))**2
        return g-0.5*rho*cdam*v*v
    while h>0:
        a1=acc(h,v)
        k1h,k1v=-v,a1
        k2h,k2v=-(v+0.5*dt*k1v),acc(h+0.5*dt*k1h,v+0.5*dt*k1v)
        k3h,k3v=-(v+0.5*dt*k2v),acc(h+0.5*dt*k2h,v+0.5*dt*k2v)
        k4h,k4v=-(v+dt*k3v),acc(h+dt*k3h,v+dt*k3v)
        hn=h+dt*(k1h+2*k2h+2*k3h+k4h)/6; vn=v+dt*(k1v+2*k2v+2*k3v+k4v)/6
        if hn<=0:
            f=h/(h-hn); v=v+(vn-v)*f; t+=dt*f; h=0; break
        h,v,t=hn,vn,t+dt
        if v>vmax: vmax,hpk,tpk=v,h,t
        rho,T=atm(h); a=math.sqrt(1.4*RSPEC*T)
        felt=max(felt,0.5*rho*cdam*v*v/G0)   # load factor felt by the body = drag accel / g0 (net decel + local g)
        if h<86000:
            m=v/a; mmax=max(mmax,m)
            if m>1: tsup+=dt
        if v<vmax: gmax_dec=max(gmax_dec,-acc(h,v)/G0)
    return dict(h0_m=h0,peak_kmh=vmax*3.6,peak_alt_m=hpk,t_peak_s=tpk,ground_kmh=v*3.6,t_total_s=t,max_mach_below86km=mmax,
                s_above_mach1=tsup,max_decel_g_after_peak=gmax_dec,max_felt_load_g=felt)
SETS={"A_inherited_0.00505":0.00505,"B_StratosPaper_0.60x1.19/121.2":0.60*1.19/121.2,"C_0.55/90":0.55/90,"D_0.70/90":0.70/90,"E_headdown_bound":0.60*0.525/121.2}
HEIGHTS=[300,1000,3000,5000,10000,20000,39000,100000]
if __name__=="__main__":
    out=[]
    for name,c in SETS.items():
        for h0 in HEIGHTS:
            r=run(h0,c); r["set"]=name; r["cdam"]=round(c,6); out.append(r)
    # vacuum reference
    for r in out:
        r["no_air_kmh_flat_g"]=round(math.sqrt(2*G0*r["h0_m"])*3.6,1) if r["h0_m"]<=10000 else ""
    keys=["set","cdam","h0_m","peak_kmh","peak_alt_m","t_peak_s","ground_kmh","t_total_s","max_mach_below86km","s_above_mach1","max_decel_g_after_peak","max_felt_load_g","no_air_kmh_flat_g"]
    with open(os.path.join(os.path.dirname(__file__),"output","fall_results.csv"),"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=keys); w.writeheader()
        for r in out: w.writerow({k:(round(r[k],2) if isinstance(r[k],float) else r[k]) for k in keys})
    print("terminal speed at sea level, CdA/m sets (km/h):",{n:round(math.sqrt(2*G0/(1.225*c))*3.6,1) for n,c in SETS.items()})
    for r in out:
        print(f'{r["set"][:26]:26s} h0={r["h0_m"]:>6} peak={r["peak_kmh"]:7.0f} km/h @{r["peak_alt_m"]/1000:5.1f} km t={r["t_peak_s"]:5.0f}s ground={r["ground_kmh"]:6.1f} T={r["t_total_s"]/60:5.1f}min M={r["max_mach_below86km"]:.2f} netdecel={r["max_decel_g_after_peak"]:.2f}g felt={r["max_felt_load_g"]:.2f}g supersonic={r["s_above_mach1"]:.0f}s')
    # Stratos reconstruction check
    print("\nStratos check (release 38,969.4 m; paper: peak 377.1 m/s=1357.6 km/h at 28,833 m, t=50.0 s; paper Cd 0.60 +-0.05, A 1.19 m2, m 121.2 kg):")
    for n in ("A_inherited_0.00505","B_StratosPaper_0.60x1.19/121.2"):
        r=run(38969.4,SETS[n]); print(n,f'peak {r["peak_kmh"]/3.6:.1f} m/s @ {r["peak_alt_m"]:.0f} m t={r["t_peak_s"]:.1f}s')
    # threshold release height where peak exceeds landing speed by >=5% (set B and A)
    print("\nslow-down threshold: smallest release height with peak >= 1.05 x ground speed")
    for n in ("A_inherited_0.00505","B_StratosPaper_0.60x1.19/121.2","D_0.70/90"):
        for h0 in range(200,6000,50):
            r=run(h0,SETS[n],dt=0.05)
            if r["peak_kmh"]>=1.05*r["ground_kmh"]: print(n,h0,"m  peak",round(r["peak_kmh"],1),"ground",round(r["ground_kmh"],1)); break
