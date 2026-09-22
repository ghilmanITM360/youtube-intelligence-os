from __future__ import annotations

import re
from pathlib import Path


REPORT = Path(__file__).resolve().parents[2] / "outputs" / "How_long_could_you_drive_towards_the_sunset_forensic_blueprint.md"
text = REPORT.read_text()

cards = re.split(r"(?=^## V\d{2} — )", text, flags=re.M)[1:]
errors: list[str] = []
if len(cards) != 34:
    errors.append(f"expected 34 cards, found {len(cards)}")

prompt_counts: dict[str, int] = {}
for card in cards:
    card_id = re.match(r"## (V\d{2})", card).group(1)
    headings = [int(n) for n in re.findall(r"^### C(\d+)\.", card, flags=re.M)]
    expected = list(range(1, 27))
    if headings != expected:
        errors.append(f"{card_id}: C headings {headings}")
    prompt_match = re.search(r'^\*\*ANIMATION PROMPT:\*\* “([^”]*)”', card, flags=re.M)
    if not prompt_match:
        errors.append(f"{card_id}: missing animation prompt")
        continue
    count = len(prompt_match.group(1))
    prompt_counts[card_id] = count
    if count > 500:
        errors.append(f"{card_id}: animation prompt {count} chars")

def replace_count(match: re.Match[str]) -> str:
    prompt = match.group(1)
    count = len(prompt)
    return f'**ANIMATION PROMPT:** “{prompt}”  \n**CHARACTER COUNT:** {count} / 500'

text = re.sub(
    r'\*\*ANIMATION PROMPT:\*\* “([^”]*)”  \n\*\*CHARACTER COUNT:\*\* (?:AUTO|\d+) / 500',
    replace_count,
    text,
)
REPORT.write_text(text)

if "AUTO / 500" in text:
    errors.append("unreplaced AUTO character count")

print(f"cards={len(cards)}")
print(f"animation_prompts={len(prompt_counts)}")
print(f"max_prompt_chars={max(prompt_counts.values()) if prompt_counts else 0}")
print(f"words={len(text.split())}")
print(f"characters={len(text)}")
for card_id, count in prompt_counts.items():
    print(f"{card_id}\t{count}")
if errors:
    print("ERRORS")
    print("\n".join(errors))
    raise SystemExit(1)
print("VALIDATION PASS")
