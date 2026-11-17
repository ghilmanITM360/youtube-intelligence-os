"""Bounded integration in an isolated checkout; publication belongs to the coordinator.

The original 966-video builder is the authority. Expansion audits require a separately
validated expansion adapter; they are deliberately rejected here.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from xml.etree import ElementTree as ET
from zipfile import ZipFile

FINANCE = Path("research/finance-economics-intelligence")
LEDGER = "VIDEO_AUDIT_966.jsonl"
WORKBOOK = "FINANCE_1612_COMBINED_INTELLIGENCE.xlsx"
CSVS = ("VIDEO_AUDIT_966.csv", "VIDEO_COMPLETION_MATRIX.csv", "TITLE_ANALYSIS_966.csv",
        "THUMBNAIL_ANALYSIS_966.csv", "SCRIPT_ANALYSIS_966.csv", "TOPIC_ANALYSIS_966.csv",
        "VIRALITY_INTELLIGENCE_966.csv")
DIMS = ("TITLE", "THUMBNAIL", "SCRIPT", "TOPIC", "PERFORMANCE", "VIRALITY")
COMPLETE = {"COMPLETE_EVIDENCE_BACKED", "COMPLETE_LIMITED_EVIDENCE"}
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
ET.register_namespace("", NS)
ET.register_namespace("r", REL)
Q = lambda name: "{" + NS + "}" + name


class IntegrationError(ValueError):
    pass


def check_expected_head(expected: str, live: str) -> None:
    if expected != live:
        raise IntegrationError(f"stale canonical head: expected {expected}, live {live}")


def _rows(data: bytes):
    lines = data.splitlines(keepends=True)
    rows = [json.loads(line) for line in lines]
    ids = [r["Video_ID"] for r in rows]
    if len(ids) != len(set(ids)):
        raise IntegrationError("duplicate ledger identity")
    return rows, lines, ids


def _complete(row):
    return set(row.get("statuses", {})) == {d + "_REVIEW" for d in DIMS} and all(
        value in COMPLETE for value in row["statuses"].values())


def guard_target_changes(before: bytes, after: bytes, target_ids: set[str]) -> list[str]:
    old, old_lines, ids = _rows(before)
    new, new_lines, new_ids = _rows(after)
    if not target_ids or target_ids - set(ids):
        raise IntegrationError("empty or unknown target IDs; expansion adapter not implemented")
    if ids != new_ids:
        raise IntegrationError("ledger identities or ordering changed")
    changed = []
    for a, b, raw_a, raw_b in zip(old, new, old_lines, new_lines):
        vid = a["Video_ID"]
        if vid not in target_ids:
            if raw_a != raw_b:
                raise IntegrationError("non-target ledger bytes changed: " + vid)
            continue
        if _complete(a):
            raise IntegrationError("already accepted: " + vid)
        if any(a.get(k) != b.get(k) for k in ("Video_ID", "Channel_ID", "identity")):
            raise IntegrationError("target identity changed: " + vid)
        if not _complete(b) or raw_a == raw_b:
            raise IntegrationError("target did not become six-dimension complete: " + vid)
        changed.append(vid)
    return changed


def _csv_records(data: bytes):
    lines = data.decode("utf-8").splitlines(keepends=True)
    reader = csv.reader(lines)
    header = next(reader)
    if len(header) != len(set(header)) or "Video_ID" not in header:
        raise IntegrationError("invalid CSV header")
    end = reader.line_num
    raw_header = "".join(lines[:end])
    result = []
    for fields in reader:
        if len(fields) != len(header):
            raise IntegrationError("invalid CSV record width")
        raw = "".join(lines[end:reader.line_num])
        end = reader.line_num
        result.append((dict(zip(header, fields)), raw))
    ids = [r[0]["Video_ID"] for r in result]
    if len(ids) != len(set(ids)):
        raise IntegrationError("duplicate CSV identity")
    return header, raw_header, result, ids


def verify_csv_targets(before: bytes, after: bytes, target_ids: set[str]) -> list[str]:
    h1, rh1, old, ids1 = _csv_records(before)
    h2, rh2, new, ids2 = _csv_records(after)
    if h1 != h2 or rh1 != rh2:
        raise IntegrationError("CSV header changed")
    if ids1 != ids2:
        raise IntegrationError("CSV identities or ordering changed")
    changed = []
    for (a, ra), (b, rb) in zip(old, new):
        if ra != rb:
            if a["Video_ID"] not in target_ids:
                raise IntegrationError("non-target CSV bytes changed: " + a["Video_ID"])
            changed.append(a["Video_ID"])
    return changed


def verify_csv_projections(rows: list[dict], csvs: dict[str, bytes]) -> None:
    """Independently reconcile every field under each published existing header."""
    for name, data in csvs.items():
        header, _, actual, ids = _csv_records(data)
        if ids != [r["Video_ID"] for r in rows]:
            raise IntegrationError("CSV projection identity mismatch: " + name)
        for row, (observed, _) in zip(rows, actual):
            if name == "VIDEO_AUDIT_966.csv":
                expected = {**row["identity"], **row["statuses"], "Batch": row["batch_id"],
                            **{k: row[k] for k in ("title", "thumbnail", "script", "topic", "performance",
                                                   "virality", "event", "private_metrics")}}
            elif name == "VIDEO_COMPLETION_MATRIX.csv":
                expected = {"Video_ID": row["Video_ID"], "Channel_ID": row["Channel_ID"],
                            **row["statuses"], "Batch": row["batch_id"]}
            else:
                section = name.split("_")[0].lower()
                expected = {"Video_ID": row["Video_ID"], "Channel_ID": row["Channel_ID"],
                            "Channel": row["identity"]["Channel"], "Title": row["identity"]["Title"],
                            "Views": row["identity"]["Views"], "Performance_tier": row["performance"]["Performance_tier"],
                            "Metric_snapshot_date": row["performance"]["Metric_snapshot_date"],
                            "Status": row["statuses"][section.upper() + "_REVIEW"], **row[section]}
            for key in header:
                value = expected.get(key, "")
                if isinstance(value, (dict, list)) or isinstance(value, str) and ("\n" in value or "\r" in value):
                    value = json.dumps(value, ensure_ascii=False, sort_keys=True)
                rendered = "" if value is None else str(value)
                if observed[key] != rendered:
                    raise IntegrationError(f"CSV projection mismatch: {name}:{row['Video_ID']}:{key}")


def _sheet_parts(z):
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    return {s.attrib["name"]: (targets[s.attrib["{" + REL + "}id"]].lstrip("/")
                              if targets[s.attrib["{" + REL + "}id"]].startswith("/")
                              else "xl/" + targets[s.attrib["{" + REL + "}id"]])
            for s in wb.find(Q("sheets"))}


def _strings(z):
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    return ["".join(e.itertext()) for e in ET.fromstring(z.read("xl/sharedStrings.xml"))]


def _value(cell, strings):
    if cell.attrib.get("t") == "inlineStr":
        return "".join(cell.find(Q("is")).itertext())
    v = cell.find(Q("v"))
    value = v.text if v is not None else None
    return strings[int(value)] if cell.attrib.get("t") == "s" and value is not None else value


def _identities(root, strings):
    return [(c.attrib["r"][1:], _value(c, strings)) for c in root.iter(Q("c"))
            if c.attrib["r"].startswith("A") and c.attrib["r"][1:].isdigit()
            and int(c.attrib["r"][1:]) >= 5]


def _allowed(z, targets):
    parts = _sheet_parts(z)
    required = ["Combined Dashboard", "All Finance Videos", "Channel Directory", "Detailed Research"]
    if list(parts) != required:
        raise IntegrationError("four original workbook sheets not preserved")
    strings = _strings(z)
    ids = {}
    allowed = {}
    for name in ["All Finance Videos", "Detailed Research"]:
        ids[name] = _identities(ET.fromstring(z.read(parts[name])), strings)
        values = [vid for _, vid in ids[name]]
        if len(values) != len(set(values)) or not targets <= set(values):
            raise IntegrationError("workbook target identities absent or duplicated")
        rows = {vid: n for n, vid in ids[name]}
        cols = (["U", "V", "W", "X", "Y", "Z", "AA", "AC", "AD", "AF"]
                if name == "All Finance Videos" else [_column(n) for n in range(4, 25)])
        allowed[parts[name]] = {col + rows[vid] for vid in targets for col in cols}
    allowed[parts["Combined Dashboard"]] = {
        "B6", "B7", "C13", "D13", "C17", "D17", "G14", "G15", "G16",
        *[col + str(n) for n in range(5, 11) for col in ("G", "H")]}
    return parts, allowed, ids


def _column(n):
    name = ""
    while n:
        n, r = divmod(n - 1, 26)
        name = chr(65 + r) + name
    return name


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _readable(value):
    if value is None or value == "":
        return ""
    if isinstance(value, list):
        return ", ".join(filter(None, map(_readable, value)))
    if isinstance(value, dict):
        return "; ".join(k.replace("_", " ") + ": " + _readable(v)
                         for k, v in value.items() if _readable(v))
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def _beat_map(script):
    beats = script.get("beat_map")
    legacy = script.get("legacy_beat_map", {}).get("Narrative_chain")
    if beats in (None, ""):
        return legacy or "PENDING"
    result = []
    for beat in beats if isinstance(beats, list) else [beats]:
        if isinstance(beat, dict):
            label = _readable(next((beat[k] for k in ("beat", "title", "label", "description") if k in beat), None))
            span = beat.get("character_range")
            prefix = f"{span[0]:,}–{span[1]:,} chars: " if isinstance(span, list) and len(span) == 2 else ""
            text = prefix + label if label else _readable(beat)
        else:
            text = _readable(beat)
        if text:
            result.append(text)
    return " → ".join(result) or legacy or "PENDING"


def _detail_values(row):
    script, title, thumb, topic, viral = (row[s + "_research"] for s in ("script", "title", "thumbnail", "topic", "virality"))
    refs = viral.get("source_refs") or title.get("source_refs") or [title.get("legacy_review", {}).get("Source")]
    return [row["batch_id"], row["deep_audit_status"], script.get("review_scope"),
            topic.get("analysis") or topic.get("legacy_review", {}).get("Audience_problem") or "PENDING",
            title.get("analysis") or _json(title.get("legacy_review", {})), _beat_map(script),
            script.get("analysis") or "PENDING", _readable(script.get("claim_audit")) or "PENDING",
            thumb.get("analysis") or "PENDING", viral.get("analysis") or "PENDING",
            viral.get("original_content_lesson", {}).get("test") or "PENDING",
            "\n".join(str(x) for x in refs if x), _json(row["statuses"]),
            *[_json(row[d.lower() + "_research"]) for d in DIMS],
            _json(row.get("event_research", {})), _json(row.get("private_metrics", {}))]


def _write_cell(root, address, value, strings):
    row_num = "".join(filter(str.isdigit, address))
    sheet_data = root.find(Q("sheetData"))
    row = next((r for r in sheet_data if r.attrib["r"] == row_num), None)
    if row is None:
        return  # Some minimal fixture dashboards omit optional counters.
    cell = next((c for c in row if c.attrib.get("r") == address), None)
    if cell is not None and (_value(cell, strings) or "") == ("" if value is None else str(value)):
        return
    if cell is None and value in (None, ""):
        return
    if cell is None:
        cell = ET.SubElement(row, Q("c"), {"r": address})
        row[:] = sorted(row, key=lambda c: (len(c.attrib.get("r", "")), c.attrib.get("r", "")))
    formula = cell.find(Q("f"))
    for child in list(cell):
        if child.tag != Q("f"):
            cell.remove(child)
    if formula is not None or isinstance(value, (int, float)):
        cell.attrib.pop("t", None)
        ET.SubElement(cell, Q("v")).text = "" if value is None else str(value)
    else:
        cell.attrib["t"] = "inlineStr"
        text = ET.SubElement(ET.SubElement(cell, Q("is")), Q("t"))
        text.attrib["{http://www.w3.org/XML/1998/namespace}space"] = "preserve"
        text.text = "" if value is None else str(value)


def patch_workbook(path: Path, payload: dict, target_ids: set[str]) -> dict:
    if path.with_suffix(path.suffix + ".pre-integration").exists() or path.with_suffix(path.suffix + ".failed-integration").exists():
        raise IntegrationError("prior workbook checkpoint exists; preserve and inspect before retry")
    with ZipFile(path) as z:
        parts, allowed, ids = _allowed(z, target_ids)
        strings = _strings(z)
        roots = {part: ET.fromstring(z.read(part)) for part in allowed}
        by_id = {r["video_id"]: r for r in payload["all_videos"]}
        details = {r["video_id"]: r for r in payload["details"]}
        for name in ("All Finance Videos", "Detailed Research"):
            row_numbers = {vid: n for n, vid in ids[name]}
            for vid in target_ids:
                if name == "All Finance Videos":
                    r = by_id[vid]
                    values = {**{_column(21 + i): r[d.lower() + "_review_status"] for i, d in enumerate(DIMS)},
                              "AA": r["audit_status"], "AC": r.get("thumbnail_status"),
                              "AD": r.get("local_media_status"), "AF": r.get("blocker")}
                else:
                    values = {_column(4 + i): v for i, v in enumerate(_detail_values(details[vid]))}
                for col, value in values.items():
                    _write_cell(roots[parts[name]], col + row_numbers[vid], value, strings)
        summary, all_rows = payload["summary"], payload["all_videos"]
        dashboard = {"B6": summary["deep_audited"], "B7": summary["pending"],
                     "C13": summary["deep_audited"], "D13": len(payload["details"]) - summary["deep_audited"],
                     "C17": summary["deep_audited"], "D17": summary["pending"],
                     "G15": sum(r.get("thumbnail_status") not in {"AVAILABLE", "REFERENCE_AVAILABLE"} for r in all_rows)}
        for i, dimension in enumerate(DIMS):
            count = sum(r[dimension.lower() + "_review_status"] in COMPLETE for r in all_rows)
            dashboard["G" + str(i + 5)] = count
            dashboard["H" + str(i + 5)] = summary["total"] - count
        for address, value in dashboard.items():
            _write_cell(roots[parts["Combined Dashboard"]], address, value, strings)
        replacements = {part: ET.tostring(root, encoding="utf-8", xml_declaration=True) for part, root in roots.items()}
        with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".xlsx", delete=False) as tmp:
            temporary = Path(tmp.name)
        try:
            with ZipFile(temporary, "w") as out:
                for entry in z.infolist():
                    out.writestr(entry, replacements.get(entry.filename, z.read(entry.filename)))
            path.replace(path.with_suffix(path.suffix + ".pre-integration"))
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)
    backup = path.with_suffix(path.suffix + ".pre-integration")
    try:
        report = verify_workbook(backup, path, target_ids)
    except Exception:
        # Preserve failed output for inspection and restore the original workbook.
        path.replace(path.with_suffix(path.suffix + ".failed-integration"))
        backup.replace(path)
        raise
    backup.unlink()
    return report


def verify_workbook(before: Path, after: Path, target_ids: set[str]) -> dict:
    changed = []
    with ZipFile(before) as old, ZipFile(after) as new:
        parts, allowed, identities = _allowed(old, target_ids)
        new_parts, _, new_ids = _allowed(new, target_ids)
        if parts != new_parts or identities != new_ids or old.namelist() != new.namelist():
            raise IntegrationError("workbook sheet/package/identity drift")
        for name in old.namelist():
            a, b = old.read(name), new.read(name)
            if a == b:
                continue
            if name not in allowed:
                raise IntegrationError("workbook non-target package part changed: " + name)
            ar, br = ET.fromstring(a), ET.fromstring(b)
            ac = {c.attrib["r"]: c for c in ar.iter(Q("c"))}
            bc = {c.attrib["r"]: c for c in br.iter(Q("c"))}
            for address in set(ac) | set(bc):
                ca, cb = ac.get(address), bc.get(address)
                sa = ET.tostring(ca) if ca is not None else None
                sb = ET.tostring(cb) if cb is not None else None
                if sa == sb:
                    continue
                if address not in allowed[name]:
                    raise IntegrationError("workbook non-target cell changed: " + name + ":" + address)
                if ca is not None and cb is None:
                    raise IntegrationError("workbook existing target cell/formula removed: " + address)
                if ca is None and cb is not None and (set(cb.attrib) - {"r", "t"} or cb.find(Q("f")) is not None):
                    raise IntegrationError("workbook new target style/formula introduced: " + address)
                if ca is not None and cb is not None:
                    if {k: v for k, v in ca.attrib.items() if k != "t"} != {k: v for k, v in cb.attrib.items() if k != "t"}:
                        raise IntegrationError("workbook target style changed: " + address)
                    fa, fb = ca.find(Q("f")), cb.find(Q("f"))
                    if (ET.tostring(fa) if fa is not None else None) != (ET.tostring(fb) if fb is not None else None):
                        raise IntegrationError("workbook formula changed: " + address)
                changed.append(name + ":" + address)
            for root in (ar, br):
                for row in root.find(Q("sheetData")):
                    for cell in list(row):
                        if cell.attrib.get("r") in allowed[name]:
                            row.remove(cell)
            if ET.tostring(ar) != ET.tostring(br):
                raise IntegrationError("workbook dimensions/panes/filter/format drift: " + name)
    return {"structural_validation": "PASS", "native_excel_recalculation": "NOT_TESTED",
            "changed_cells": sorted(changed), "identity_count": len(identities["All Finance Videos"]),
            "preserved_sheets": list(parts),
            "generation_metadata": "PRESERVED_FROM_SOURCE; integration receipt supplies current provenance"}


def _fingerprints(repo):
    manifest = json.loads((repo / FINANCE / "audit-baseline/MANIFEST.json").read_text())
    for relative, expected in manifest["source_hashes"].items():
        data = (repo / relative).read_bytes()
        if data.startswith(b"version https://git-lfs.github.com/spec/"):
            raise IntegrationError("required source is an LFS pointer, restore original bytes: " + relative)
        if hashlib.sha256(data).hexdigest() != expected:
            raise IntegrationError("immutable source drift: " + relative)
    return len(manifest["source_hashes"])


def prepare_finance(repo: Path, baseline: Path, target_ids: set[str], python: str = sys.executable,
                    node: str = "node") -> dict:
    """Run only in a disposable checkout at an already-checked canonical base.

    Caller imports new packets first, holds both task and coordinator claims, and
    verifies remote heads again before publication. Failure leaves the checkout
    intact; this function never changes claims, commits, pushes or source files.
    """
    base = repo / FINANCE
    before = (baseline / LEDGER).read_bytes()
    rows, _, ids = _rows(before)
    if not target_ids or target_ids - set(ids):
        raise IntegrationError("unknown/expansion target; original-966 adapter only")
    if any(_complete(r) for r in rows if r["Video_ID"] in target_ids):
        raise IntegrationError("already accepted target")
    for name in (LEDGER, *CSVS, WORKBOOK, "audit-baseline/MANIFEST.json"):
        if (base / name).read_bytes() != (baseline / name).read_bytes():
            raise IntegrationError("staged canonical output differs from the accepted baseline before build: " + name)
    checked = _fingerprints(repo)
    logs = []

    def run(args, cwd=base):
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                                env={**os.environ, "GIT_NO_LAZY_FETCH": "1"}, timeout=120)
        logs.append({"command": args, "exit_code": result.returncode,
                     "stdout_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
                     "stderr_sha256": hashlib.sha256(result.stderr.encode()).hexdigest()})
        if result.returncode:
            raise IntegrationError(f"validation failed: {args}: {result.stderr[-4000:]} {result.stdout[-4000:]}")
        return result.stdout

    run([python, "build_audit_966.py"])
    guard_target_changes(before, (base / LEDGER).read_bytes(), target_ids)
    after_rows, _, _ = _rows((base / LEDGER).read_bytes())
    projections = {name: verify_csv_targets((baseline / name).read_bytes(), (base / name).read_bytes(), target_ids)
                   for name in CSVS}
    verify_csv_projections(after_rows, {name: (base / name).read_bytes() for name in CSVS})
    payload = json.loads(run([python, "build_combined_workbook_data.py"]))
    wb = patch_workbook(base / WORKBOOK, payload, target_ids)
    verify_workbook(baseline / WORKBOOK, base / WORKBOOK, target_ids)
    run([python, "-m", "unittest", "discover", "-p", "test_*.py", "-v"])
    run([node, "--test", "test_workbook_formatting.mjs"])
    run([python, "validate_audit_966.py"])
    run([python, "validate_research.py"])
    _fingerprints(repo)
    return {"validation": "PASS", "target_ids": sorted(target_ids), "source_hashes_checked": checked,
            "summary": payload["summary"], "csv_changed_ids": projections, "workbook": wb,
            "checks": logs, "canonical_outputs": [str(FINANCE / p) for p in (LEDGER, *CSVS, WORKBOOK,
                                     "VALIDATION_966.json", "VALIDATION.json")],
            "hosted_ci": "NOT_TESTED", "expansion_adapter": "NOT_IMPLEMENTED"}


def integrate_finance(repo: Path, baseline: Path, target_ids: set[str], python: str = sys.executable,
                      node: str = "node") -> dict:
    return prepare_finance(repo, baseline, target_ids, python, node)


def prepare_visual(repo: Path, files: dict[str, bytes], video_id: str, channel_id: str) -> list[str]:
    """Copy reviewed new files only; no replacement of an existing visual record."""
    if video_id == "5umJ63d3rzQ":
        raise IntegrationError("Video003 protected: explicit legacy migration required")
    if not files or any(not component or "/" in component or component in {".", ".."}
                        for component in (video_id, channel_id)):
        raise IntegrationError("empty visual packet or invalid channel/video identity")
    prefix = Path("research/visual-forensics/channels") / channel_id / video_id
    destinations = []
    for relative, data in files.items():
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts or not path.is_relative_to(prefix):
            raise IntegrationError("visual destination outside exact channel/video")
        destination = repo / path
        if not destination.resolve().is_relative_to(repo.resolve()):
            raise IntegrationError("visual destination escapes repository through a symlink")
        if destination.exists() or destination.is_symlink():
            raise IntegrationError("visual existing record collision: " + relative)
        if len(data) > 5 * 1024 * 1024 or path.suffix.lower() not in {".json", ".csv", ".md", ".txt"}:
            raise IntegrationError("visual binary/large media requires external recovery manifest")
        destinations.append((relative, destination, data))
    for relative, destination, data in destinations:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    return [r for r, _, _ in destinations]
