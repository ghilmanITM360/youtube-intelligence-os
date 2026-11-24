import math
G0=9.80665;R=6371000.0
# US Standard Atmosphere 1976, 0-86 km layers (geopotential), 86-100 km: log-linear on published table values
L=[(0,-0.0065,288.15,101325.0),(11000,0,216.65,None),(20000,0.001,216.65,None),(32000,0.0028,228.65,None),(47000,0,270.65,None),(51000,-0.0028,270.65,None),(71000,-0.002,214.65,None),(84852,0,186.946,None)]
Rg=287.053;P=[L[0][3]]
for i in range(1,len(L)):
    h0,b,T0,_=L[i-1];h1=L[i][0];T1=T0+b*(h1-h0)
    P.append(P[-1]*(T1/T0)**(-G0/(b*Rg)) if b else P[-1]*math.exp(-G0*(h1-h0)/(Rg*T0)))
tab=[(86000,6.958e-6),(90000,3.416e-6),(95000,1.393e-6),(100000,5.604e-7)]
def rho(h):
    h=max(h,0.0)
    if h>86000:
        for (a,ra),(b_,rb) in zip(tab,tab[1:]):
            if a<=h<=b_: return math.exp(math.log(ra)+(h-a)/(b_-a)*(math.log(rb)-math.log(ra)))
        return tab[-1][1]*math.exp(-(h-100000)/6000)
    hg=h*R/(R+h)
    i=max(j for j in range(len(L)) if L[j][0]<=hg);h0,b,T0,_=L[i];T=T0+b*(hg-h0)
    p=P[i]*((T/T0)**(-G0/(b*Rg)) if b else math.exp(-G0*(hg-h0)/(Rg*T0)))
    return p/(Rg*T)
def fall(h0,k,dt=0.05):
    h,v=h0,0.0;vmax=0;t=0
    def a(h,v): return G0*(R/(R+h))**2-rho(h)*k*v*v/2
    while h>0:
        k1v=a(h,v);k1h=-v
        k2v=a(h+k1h*dt/2,v+k1v*dt/2);k2h=-(v+k1v*dt/2)
        k3v=a(h+k2h*dt/2,v+k2v*dt/2);k3h=-(v+k2v*dt/2)
        k4v=a(h+k3h*dt,v+k3v*dt);k4h=-(v+k3v*dt)
        hn=h+dt/6*(k1h+2*k2h+2*k3h+k4h);vn=v+dt/6*(k1v+2*k2v+2*k3v+k4v)
        if hn<=0: f=h/(h-hn);v=v+(vn-v)*f;t+=dt*f;h=0;break
        h,v=hn,vn;t+=dt;vmax=max(vmax,v)
    return v*3.6,vmax*3.6,t
print('FALL (CdA/m multipliers; k0=0.00505 m2/kg, same as prior audit input -> checks integrator/atmosphere, NOT the drag value)')
for mult in(0.8,1,1.2):
    for h0 in(1000,100000,400000):
        v,vm,t=fall(h0,0.00505*mult);print(f' x{mult} from {h0/1000:g} km: ground {v:.1f} km/h, peak {vm:.0f} km/h, {t:.0f} s')
# 400 km: rho above 100 km extrapolated crudely (exp scale 6 km) -> low confidence
print('NEUTRON 0.7 cm3:',[f'{0.7e-6*d/1e3/1e6:.0f} Mt at {d:.1e} kg/m3' for d in(2.7e17,4e17,1e18)])
print(' rock cube side (2700 kg/m3) for those:',[f'{(0.7e-6*d/2700)**(1/3):.0f} m' for d in(2.7e17,1e18)])
Ms,Mm=1.989e30,7.342e22;rs,rm=1.496e11,3.844e8
print('TIDE solar/lunar force ratio:',round((Ms/Mm)*(rm/rs)**3,3))
Gc=6.674e-11
for rho_ in(2000,5514,3000):
    k=math.sqrt(4*math.pi*Gc*rho_/3);print(f'ORBIT rho={rho_}: R for v=3.0..3.6 m/s: {3.0/k/1e3:.2f}-{3.6/k/1e3:.2f} km; period {2*math.pi/k/60:.1f} min')
ld=299792458*86400;print('LIGHT-DAY km',ld/1e3,'AU',ld/1.495978707e11,'round-trip days 2')
