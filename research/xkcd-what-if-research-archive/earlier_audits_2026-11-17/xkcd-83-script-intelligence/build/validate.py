"""Check every audit: JSON parses, required keys exist, every *quote is an exact substring of its transcript."""
import csv, glob, json, os, sys

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ["A_identity", "B_hook", "C_opening_beats", "D_spine", "E_loops", "F_mechanics", "G_emotion", "H_pacing",
        "I_payoffs", "J_ending", "K_assessment", "L_formula", "lenses", "framework_rules", "matrix_row", "tags"]
RULES = {"FR-HOOK-01", "FR-INTRO-03", "FR-SCR-01", "FR-SCR-06", "FR-BT-01", "FR-16C-07", "FR-16C-13", "FR-16C-16"}


def quotes(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}"
            if isinstance(v, str) and k.endswith("quote"):
                yield p, v
            elif isinstance(v, list) and k.endswith("quotes"):
                for i, q in enumerate(v):
                    if isinstance(q, str):
                        yield f"{p}[{i}]", q
            else:
                yield from quotes(v, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from quotes(v, f"{path}[{i}]")


def main():
    inv = list(csv.DictReader(open(f"{O}/D1_dataset_inventory.csv")))
    bad, nq, done = [], 0, 0
    for r in inv:
        f = f"{O}/audits/{r['vid']}.json"
        if not os.path.exists(f):
            bad.append((r["vid"], "MISSING", "")); continue
        try:
            a = json.load(open(f))
        except Exception as e:
            bad.append((r["vid"], "BAD_JSON", str(e)[:80])); continue
        done += 1
        t = open(f"{O}/transcripts/{r['file']}").read().split("TRANSCRIPT:\n", 1)[1]
        for k in KEYS:
            if k not in a:
                bad.append((r["vid"], "NO_KEY", k))
        got = {x.get("rule_id") for x in a.get("framework_rules", []) if isinstance(x, dict)}
        if got != RULES:
            bad.append((r["vid"], "RULES", str(sorted(RULES ^ got))))
        if bool(r["overlaps_longer_video"]) != bool(a.get("excerpt_delta")):
            bad.append((r["vid"], "EXCERPT_DELTA", "expected " + ("set" if r["overlaps_longer_video"] else "null")))
        for p, q in quotes(a):
            nq += 1
            if q not in t:
                bad.append((r["vid"], "QUOTE", f"{p}: {q[:70]}"))
    print(f"audits present {done}/{len(inv)}; quotes checked {nq}; problems {len(bad)}")
    for b in bad:
        print(" ", *b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
