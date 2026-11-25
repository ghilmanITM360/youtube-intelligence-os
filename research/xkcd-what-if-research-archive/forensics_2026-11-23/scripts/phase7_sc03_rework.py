"""SC03 rework (2026-11-23 continuation): which QUANTITY does the lightning line mean, and do the video's own three lines agree with each other and with the sources?
Inputs are all stated below; nothing is read from the video except the quoted wording. Run: python3 -I scripts/phase7_sc03_rework.py"""
import json
HIRO = 15 * 4.184e12                  # J; 15 kt TNT (Wikipedia Little Boy ~15 kt = 63 TJ; OSTI best estimate 15 kt, range 6-23 kt quoted there)
US_KWH_YR = 3861e9                    # EIA MER/STEO 2023 sales to ultimate customers, 3,861 billion kWh (3,874 in EIA-861)
HOUSE_KWH_MO = 899                    # EIA FAQ id=97 (fetched this session): 2022 average US residential customer 10,791 kWh/yr
house_d = HOUSE_KWH_MO * 12 / 365 * 3.6e6          # J per day
us_5min = US_KWH_YR * 3.6e6 / (365 * 24 * 12)      # J
bolts = 1e6                                         # video: 'about a million separate bolts'
out = {}
out['house_J_per_day'] = house_d; out['house_kWh_per_day'] = house_d / 3.6e6
out['two_bombs_J'] = 2 * HIRO; out['us_5min_J'] = us_5min; out['two_bombs_over_us5min'] = 2 * HIRO / us_5min
# per-bolt energy implied by the video's own lines
out['per_bolt_from_two_bombs_MJ'] = 2 * HIRO / bolts / 1e6
out['per_bolt_from_us5min_MJ'] = us_5min / bolts / 1e6
out['house_days_from_two_bombs'] = 2 * HIRO / bolts / house_d
out['per_bolt_for_two_house_days_MJ'] = 2 * house_d / 1e6
# source ranges (all per FLASH / 'discharge'; none states a ground-delivered share)
for nm, mj in (('NatGeo_low_100MJ', 100), ('NatGeo_typical_low_1000MJ', 1000), ('NatGeo_typical_high_5000MJ', 5000), ('NatGeo_max_30000MJ', 30000), ('Cooray97_ground_flash_950MJ', 950)):
    out[f'house_days_{nm}'] = mj * 1e6 / house_d
out['natgeo_own_equivalence_1000MJ_kWh'] = 1000e6 / 3.6e6     # NatGeo says about 280 kWh
out['natgeo_implied_household_kWh_per_day_(9 days)'] = 280 / 9
# console + TV line (world day): 'several million years'
yr = 365.25 * 86400
for P in (100, 300, 500):
    out[f'console_TV_{P}W_years_for_two_bombs'] = 2 * HIRO / P / yr
out['power_W_needed_for_3e6_years_on_two_bombs'] = 2 * HIRO / (3e6 * yr)
# Catatumbo line: one flash per 2 s, ~10 h night
fl = 10 * 3600 / 2; out['catatumbo_flashes_10h'] = fl
for e in (126e6, 1e9):
    out[f'catatumbo_energy_J_at_{e/1e6:.0f}MJ'] = fl * e
    for P in (300,): out[f'catatumbo_years_at_{e/1e6:.0f}MJ_{P}W'] = fl * e / P / yr
out['world_day_to_catatumbo_night_ratio'] = bolts / fl
out['flashes_per_day_45_per_s'] = 45 * 86400
print(json.dumps({k: float(f'{v:.4g}') for k, v in out.items()}, indent=1))
json.dump(out, open('07_SC03_LIGHTNING_REWORK.json', 'w'), indent=1)
