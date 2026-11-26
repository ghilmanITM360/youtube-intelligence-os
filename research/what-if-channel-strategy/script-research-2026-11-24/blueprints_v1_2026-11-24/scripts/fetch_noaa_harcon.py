"""Fetch NOAA CO-OPS harmonic constituents (M2, S2, K1, O1, N2) for a few stations.
Source: https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/<id>/harcon.json
Output: data/noaa_harcon_<id>.json (raw) + data/noaa_harcon_summary.csv
Run: python3 scripts/fetch_noaa_harcon.py   (needs network; stdlib only)
"""
import json, urllib.request, csv, os, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "data"); os.makedirs(OUT, exist_ok=True)
ST = {"8518750":"The Battery, NY","9414290":"San Francisco, CA","9447130":"Seattle, WA","9455920":"Anchorage, AK",
      "1612340":"Honolulu, HI","8443970":"Boston, MA","8761724":"Grand Isle, LA (Gulf of Mexico)","9751639":"Charlotte Amalie, USVI"}
rows=[]
for sid,name in ST.items():
    url=f"https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{sid}/harcon.json"
    try:
        d=json.load(urllib.request.urlopen(url,timeout=30))
    except Exception as e:
        rows.append([sid,name,"ERROR",str(e),"","","",""]); continue
    json.dump(d,open(os.path.join(OUT,f"noaa_harcon_{sid}.json"),"w"),indent=1)
    unit=d.get("units"); amp={c["name"]:c["amplitude"] for c in d["HarmonicConstituents"]}
    m2,s2=amp.get("M2"),amp.get("S2")
    rows.append([sid,name,unit,m2,s2,round(s2/m2,3) if m2 else "",amp.get("K1"),amp.get("O1")])
w=csv.writer(open(os.path.join(OUT,"noaa_harcon_summary.csv"),"w",newline=""))
w.writerow(["station_id","name","units","M2_amp","S2_amp","S2_over_M2","K1_amp","O1_amp"]); w.writerows(rows)
print("fetched",datetime.date.today()); [print(r) for r in rows]
