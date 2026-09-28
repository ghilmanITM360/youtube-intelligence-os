"""Stage-E paid acquisition plan from a dated master inventory (no network, no spend).

Usage: python3 plan_paid_acquisition.py SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json <credit_usd> <campaign_remaining_usd>
Writes PAID-ACQUISITION-PLAN-<date>.md next to the inventory. Every figure is recomputed from inventory rows.
"""
import json, math, sys
from pathlib import Path

PRICE = 0.004  # Free-plan $/video, verified live on the Actor pricing page 2026-09-28
CAP_HEADROOM = 1.25  # server-side maxTotalChargeUsd = ceil(expected * 1.25, to the cent)
# 2026-09-25 report priority order for the 14 Group-C channels
ORDER = ["UCslmaJaMSw8F8BId4CxByJw", "UCC4TRhL4BiA7--jpxVVXcpQ", "UC2BaKQ5vqal9yaC-VbpD5ZQ", "UClzqmRzoC-7r8GiB_XQUn_A",
         "UCLxLjL1XVaKqZg-wZ2EBspA", "UCRxZVn1cDGyo_p7ZbxhkeUQ", "UCX_cW2SeHF1iBxbjx41vfrA", "UCPjG4ZRBkiO1y_vHlnj8jIg",
         "UCUUKjcYdqOHk2j-pbUnWDNw", "UC4oT7W2VOi-TJI3WWU51DHA", "UCHOrUqhgZmEwhmXqvLwghpg", "UCj-4CkWt2waFCjt5h7fZSiA",
         "UCxD2fste1dR0EUhj0gB8aOw", "UC6VFFdBkvTxy8VUO0d2h1Xg"]


def cap(expected):
    return math.ceil(expected * CAP_HEADROOM * 100) / 100


def main(inv_path, credit, campaign):
    inv_path, credit, campaign = Path(inv_path), float(credit), float(campaign)
    rows = {r["canonical_channel_id"]: r for r in json.loads(inv_path.read_text())["channels"] if r["canonical_channel_id"]}
    runs = []
    refresh = [r for r in rows.values() if r["inventory_category"] == "ACQUIRED_WITH_NEW_PUBLIC_UPLOADS"]
    ids = [(r["verified_name"], v) for r in refresh for v in
           (r["missing_regular_ids"] or []) + (r["missing_shorts_ids"] or []) + (r["missing_stream_ids"] or [])]
    if ids:
        runs.append({"run": "R-REFRESH", "channel": ", ".join(sorted({n for n, _ in ids})), "cid": "multiple",
                     "have": sum(r["repo_videos"] for r in refresh), "r": len(ids), "s": 0, "l": 0,
                     "target": "startUrls = exact watch URLs of the new-upload Video IDs listed below",
                     "gain": "complete acquired competitors to 2026-09-28 (titles/descriptions/captions)"})
    for i, cid in enumerate(ORDER, 1):
        r = rows.get(cid)
        if not r or r["inventory_category"] != "QUALIFIED_PENDING":
            continue
        runs.append({"run": f"R-Q{i:02d}", "channel": r["verified_name"], "cid": cid, "have": 0,
                     "r": r["live_regular"] or 0, "s": r["live_shorts"] or 0, "l": r["live_streams"] or 0,
                     "target": f"channel URL; maxResults={r['live_regular'] or 0}, maxResultsShorts={r['live_shorts'] or 0}, "
                               f"maxResultStreams={r['live_streams'] or 0}",
                     "gain": "first video-level evidence incl. real captions where YouTube has them"})
    cum, fit_sum, lines = 0.0, 0.0, []
    for x in runs:  # priority order; a run that would break a ceiling is skipped, cheaper later runs may still fit
        x["n"] = x["r"] + x["s"] + x["l"]
        x["cost"] = round(x["n"] * PRICE, 3)
        x["cap"] = cap(x["cost"])
        cum = round(cum + x["cost"], 3)
        x["cum"] = cum
        ok = x["n"] and fit_sum + x["cap"] <= min(campaign, credit * 0.8)
        x["fits"] = "yes" if ok else "no"
        fit_sum = round(fit_sum + x["cap"], 2) if ok else fit_sum
    lines += [f"# Paid acquisition plan — {inv_path.stem.split('-')[-3]}-{inv_path.stem.split('-')[-2]}-{inv_path.stem.split('-')[-1]}", "",
              "**Not authorized.** Nothing here has been run. Each run needs explicit owner approval in chat.", "",
              f"- Actor `streamers/youtube-scraper` build `0.0.303`; Free plan `${PRICE * 1000:.2f}/1,000` videos (verified live 2026-09-28).",
              "- Input: `transcriptionAndSubtitle=ALWAYS_SUBTITLES` (existing YouTube captions only), `subtitlesFormat=plaintext`, "
              "`aiVideoDescription=false`, `aiVideoSummary=false`, no date-range add-on.",
              f"- Live Apify free credit: `${credit:.2f}`. Residual of the historical `$4.50` campaign cap: `${campaign:.3f}` "
              "(a historical ceiling, not a current authorization).",
              f"- `fits` = in priority order, the run's hard cap still fits (with every earlier fitting run's cap) inside both the campaign residual and 80% of live credit — never the whole balance.",
              f"- Per-run server-side hard cap (`maxTotalChargeUsd`) = expected × {CAP_HEADROOM}, rounded up to the cent.", "",
              "| Run | Channel | Channel ID | Already acquired | Regular | Shorts | Streams | Results | Expected $ | Hard cap $ | Cumulative $ | Fits | Target / config | Capability gained |",
              "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|"]
    for x in runs:
        lines.append(f"| {x['run']} | {x['channel'].replace('|', '/').strip()} | `{x['cid']}` | {x['have']} | {x['r']} | {x['s']} | {x['l']} | {x['n']} | "
                     f"{x['cost']:.3f} | {x['cap']:.2f} | {x['cum']:.3f} | {x['fits']} | {x['target']} | {x['gain']} |")
    fit = [x for x in runs if x["fits"] == "yes"]
    lines += ["", f"Total for all {len(runs)} runs: {sum(x['n'] for x in runs)} results, ${sum(x['cost'] for x in runs):.3f} expected.",
              f"Runs that fit the current ceilings: {len(fit)} ({', '.join(x['run'] for x in fit)}), "
              f"${sum(x['cost'] for x in fit):.3f} expected, ${sum(x['cap'] for x in fit):.2f} aggregate hard caps.", ""]
    if ids:
        lines += ["## R-REFRESH exact Video IDs", ""] + [f"- {n}: `https://www.youtube.com/watch?v={v}`" for n, v in ids] + [""]
    out = inv_path.with_name("PAID-ACQUISITION-PLAN-" + inv_path.stem.removeprefix("SENIOR-HEALTH-MASTER-INVENTORY-") + ".md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out.name, len(runs), "runs;", len(fit), "fit")


if __name__ == "__main__":
    main(*sys.argv[1:4])
