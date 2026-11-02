"""Validate the installed YIOS Visual Forensics standard (read-only).

Usage: python3 -I research/visual-forensics/validate_install.py <repo_root>
Exit 0 = PASS. Checks byte-identical source prompts, skill frontmatter,
reference/template integrity, link resolution, routing phrases and index links.
"""
import csv, hashlib, json, re, sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
vf = root / "research/visual-forensics"
skill = root / ".claude/skills/visual-ct-scan"
errors = []
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

# 1. Four original prompts, byte-identical.
man = json.loads((vf / "SOURCE_PROMPT_MANIFEST.json").read_text())
assert man["source_count"] == len(man["sources"]) == 4
for s in man["sources"]:
    p = vf / s["bundled_path"]
    if not p.is_file() or p.stat().st_size != s["bytes"] or sha(p) != s["sha256"]:
        errors.append(f"source prompt mismatch: {p}")

# 2. Every installed file matches the recorded install hash list.
for line in (vf / "INSTALLED_FILES.sha256").read_text().splitlines():
    h, rel = line.split("  ", 1)
    p = root / rel
    if not p.is_file() or sha(p) != h:
        errors.append(f"installed file changed or missing: {rel}")

# 3. Skill frontmatter.
raw = (skill / "SKILL.md").read_text()
m = re.match(r'---\nname: (\S+)\ndescription: "([^"\n]+)"\n---\n', raw)
if not m or m.group(1) != "visual-ct-scan" or len(m.group(2)) > 1024:
    errors.append("invalid SKILL.md frontmatter")

# 4. References 01-14 present; all relative links in SKILL.md resolve.
for i in range(1, 15):
    if len(list((skill / "references").glob(f"{i:02d}_*.md"))) != 1:
        errors.append(f"reference {i:02d} missing")
for link in re.findall(r"\]\(([^)#:]+)\)", raw):
    if not (skill / link).exists():
        errors.append(f"broken SKILL.md link: {link}")

# 5. Templates parse.
for f in (skill / "templates").iterdir():
    if f.stat().st_size == 0:
        errors.append(f"empty template {f.name}")
    if f.suffix == ".json":
        json.loads(f.read_text())
    if f.suffix == ".csv" and len(next(csv.reader(f.open()))) < 5:
        errors.append(f"bad csv header {f.name}")

# 6. Mode names and owner trigger phrases are routable.
desc = m.group(2).lower() if m else ""
for mode in ["INVENTORY", "STRUCTURAL", "DEEP", "CT_SCAN", "RECONSTRUCTION", "CHANNEL_DNA"]:
    if f"`{mode}`" not in raw:
        errors.append(f"mode {mode} missing")
for phrase in ["visual forensics", "ct scan", "deeper visual analysis", "motion reconstruction",
               "frame-by-frame investigation", "channel visual dna"]:
    if phrase not in desc:
        errors.append(f"trigger phrase not in description: {phrase}")

# 7. Discoverability from project instructions and research index.
if "visual-ct-scan" not in (root / "AGENTS.md").read_text():
    errors.append("AGENTS.md lacks visual-ct-scan reference")
if "visual-forensics/README.md" not in (root / "research/README.md").read_text():
    errors.append("research/README.md lacks visual-forensics link")

print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors}, indent=1))
sys.exit(1 if errors else 0)
