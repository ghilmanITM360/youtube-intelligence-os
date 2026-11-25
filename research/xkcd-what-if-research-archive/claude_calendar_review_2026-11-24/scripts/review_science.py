import math
G=6.674e-11; c=299792458.0
# 1 FALL: independent simple model: isothermal-exp atmosphere piecewise (scale heights) vs the prior's 1976 layers. Terminal v at sea level from CdA/m
def rho(h):
    # coarse US-1976-like: troposphere 11km lapse, strat exp; adequate for a cross-check (not the same code as prior audit)
    if h<11000:
        T=288.15-0.0065*h; return 1.225*(T/288.15)**4.2559
    if h<20000: return 0.3639*math.exp(-(h-11000)/6340)
    if h<32000: return 0.0880*(1+0.001*(h-20000)/216.65)**(-35.16)
    if h<47000: return 0.0132*(1+0.0028*(h-32000)/228.65)**(-13.2)
    if h<51000: return 0.00143*math.exp(-(h-47000)/7922)
    if h<71000: return 0.00086*(1-0.0028*(h-51000)/270.65)**(11.2)
    if h<100000: return max(0.000064*math.exp(-(h-71000)/5500),5e-7)
    return 5.6e-7*math.exp(-(h-100000)/6000)
def fall(h0,k,dt=0.02):
    h,v,t,pk,hp=h0,0.0,0.0,0.0,h0
    while h>0:
        g=9.80665*(6371e3/(6371e3+h))**2
        a=g-rho(h)*k*v*v/2
        v+=a*dt;h-=v*dt;t+=dt
        if v>pk:pk,hp=v,h
    return v*3.6,pk*3.6,hp/1000,t
print('FALL independent check, k=CdA/m (m2/kg)')
for k,lab in((0.00505,'prior-audit k'),(0.55/90,'CdA 0.55 m2, 90 kg belly'),(0.7/90,'CdA 0.7')):
    print(lab,'k=%.5f sea-level terminal %.0f km/h'%(k,math.sqrt(2/(1.225*k))*3.6))
    for h0 in(1000,5000,10000,15000,20000,39000,100000):
        v,pk,hp,t=fall(h0,k); print('  from %6.0f m: ground %.0f km/h, peak %.0f km/h at %.1f km, %.0f s'%(h0,v,pk,hp,t))
print('Baumgartner Wikipedia-cited peak ~380 m/s =',380*3.6,'km/h; belly terminal 55 m/s =',55*3.6)
# 2 TINY PLANET
print('\nTINY PLANET circular speed v=R*sqrt(4piG rho/3); escape=sqrt2*v')
for rho_ in(1900,2700,5514):
    k=math.sqrt(4*math.pi*G*rho_/3)
    print(' rho',rho_,'R for v=2,3,4 m/s: %s km; period %.0f min'%([round(v/k/1e3,2) for v in(2,3,4)],2*math.pi/k/60))
# Phobos from NSSDC mass 10.6e15, semi-axes 13.0/11.4/9.1 km
M=10.6e15;Rm=(13.0*11.4*9.1)**(1/3)*1e3
print('PHOBOS mean radius(geo mean) %.2f km, density %.0f, g(mean) %.4f m/s2, v_circ %.2f m/s, v_esc %.2f m/s = %.0f km/h'%(Rm/1e3,M/(4/3*math.pi*Rm**3),G*M/Rm**2,math.sqrt(G*M/Rm),math.sqrt(2*G*M/Rm),math.sqrt(2*G*M/Rm)*3.6))
g=G*M/Rm**2; v=3.0; print(' vertical 3 m/s jump: height %.0f m, hang time %.0f s (%.1f min) -- ignores Mars tide, rotation, shape'%(v*v/2/g,2*v/g,2*v/g/60))
print(' Phobos rotation (tidally locked, 7.65 h) equatorial speed at 13 km: %.2f m/s'%(2*math.pi*13e3/(0.31891*86400)))
# 3 VOYAGER
ld=c*86400;print('\nLIGHT-DAY %.4e km = %.2f AU; one-way 24 h; round trip 48 h (no processing)'%(ld/1e3,ld/1.495978707e11))
# 4 MOON TIDES
Ms,Mm=1.989e30,7.342e22;rs,rm=1.496e11,3.844e8
r=(Ms/Mm)*(rm/rs)**3;print('TIDE solar/lunar generating force ratio %.3f; solar share of total (no phase) %.2f; lunar %.2f'%(r,r/(1+r),1/(1+r)))
print(' moon mass / earth mass %.4f; EM barycenter %.0f km from Earth centre'%(Mm/5.972e24,rm/1e3*Mm/(Mm+5.972e24)))
# 5 NEUTRON
for d in(2.7e17,4e17,1e18):
    print('NEUTRON density %.1e: teaspoon 5 mL -> %.2f billion t; 4.93 mL -> %.2f; 0.7 cm3 -> %.0f Mt; 1 cm3 -> %.2f billion t'%(d,5e-6*d/1e3/1e9,4.93e-6*d/1e3/1e9,0.7e-6*d/1e3/1e6,1e-6*d/1e3/1e9))
print(' Everest mass ~1.6e14 kg (assumption, order only) ; teaspoon at 4e17 =',5e-6*4e17,'kg')
# 6 LASER
for d,l in((384400,'mean centre-centre'),(356400,'perigee'),(406700,'apogee')):print('LASER',l,d,'km round trip %.4f s'%(2*d/299792.458))
print(' surface-to-surface mean approx (384400-6371-1737)=%.0f km -> %.4f s'%(384400-6371-1737,2*(384400-6371-1737)/299792.458))
# 7 EARTH SPIN
w=2*math.pi/86164.0905
for lat in(0,40,60):print('SPIN surface speed lat %d: %.1f m/s'%(lat,w*6378137*math.cos(math.radians(lat))))
print(' stopping that uniformly in 1 s at equator: %.1f g'%(w*6378137/9.80665))
