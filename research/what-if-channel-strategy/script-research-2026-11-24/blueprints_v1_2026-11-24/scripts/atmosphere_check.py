"""Print density/temperature/speed of sound from fall_model.atm at selected altitudes, with the recalled USSA-1976 reference values
(from memory, NOT re-sourced) for a sanity comparison. Run: python3 scripts/atmosphere_check.py"""
import math
from fall_model import atm
REF={0:1.225,1000:1.1117,5000:0.7364,10000:0.4135,20000:0.08891,30000:0.01841,39000:0.004,50000:0.001027,86000:6.958e-6,100000:5.604e-7}
for h in (0,1000,5000,10000,20000,30000,39000,50000,86000,100000):
    rho,T=atm(h); a=math.sqrt(1.4*287.053*T)
    print(f"h={h/1000:6.1f} km rho={rho:.4g} kg/m3 (recalled ref {REF[h]:.4g}) T={T:.1f} K a={a:.0f} m/s  rho0/rho={1.225/rho:,.0f}")
