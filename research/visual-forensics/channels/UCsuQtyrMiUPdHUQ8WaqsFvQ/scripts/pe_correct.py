"""Apply primary corrections to a reviewer's annotations without touching the raw file.
review/primary_corrections.csv: seg,field,old,new,reason,evidence  -> review/<rv>/annotations_corrected.csv
Usage: python3 -I pe_correct.py <video_dir> <reviewer_id>"""
import csv, sys, pathlib
V = pathlib.Path(sys.argv[1]).resolve(); R = V / "review" / sys.argv[2]
rows = list(csv.DictReader(open(R / "annotations.csv"))); fix = list(csv.DictReader(open(V / "review/primary_corrections.csv")))
by = {r["seg"]: r for r in rows}
for c in fix:
    assert by[c["seg"]][c["field"]] == c["old"], c
    by[c["seg"]][c["field"]] = c["new"]
with open(R / "annotations_corrected.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("applied", len(fix))
