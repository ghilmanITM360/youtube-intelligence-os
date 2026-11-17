#!/usr/bin/env python3
"""After UNAVAILABLE_UNIQUE_HASHES.csv reaches this Mac: python3 -I join_missing_list.py <that.csv>. Prints exact overlaps; writes the hash lists here."""
import csv, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
def hashes(name): return {r['sha256'] for r in csv.DictReader(open(HERE / name))}
inventory, local = hashes('inventory_1006_hashes.csv'), hashes('unique_hashes.csv')
missing = set()
for row in csv.reader(open(sys.argv[1])):
    missing |= {c.lower() for c in row if re.fullmatch(r'[0-9a-fA-F]{64}', c)}
assert missing, 'no SHA-256 values found in input'
hit = missing & local
print(f'missing_unique={len(missing)} inventory_unique={len(inventory)} recovered_from_inventory={len(missing & inventory)} '
      f'all_local_unique={len(local)} recovered_all_local={len(hit)} still_missing={len(missing - hit)}')
(HERE / 'JOIN_RECOVERED_HASHES.txt').write_text('\n'.join(sorted(hit)) + '\n')
(HERE / 'JOIN_STILL_MISSING_HASHES.txt').write_text('\n'.join(sorted(missing - hit)) + '\n')
