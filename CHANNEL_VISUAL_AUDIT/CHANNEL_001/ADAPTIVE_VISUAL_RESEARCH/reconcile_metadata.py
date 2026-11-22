"""Join local corpus names to the archived channel snapshot, without changing byte identities."""
import argparse
import csv
import re
import unicodedata

def normalize(value):
    return "".join(c for c in unicodedata.normalize("NFKC", value).casefold() if c.isalnum())

def reconcile(rows, metadata):
    occupied = {row["reconciled_video_id"] for row in rows}
    for row in rows:
        title = row["title"]
        if row["reconciled_video_id"] != "-xtqbRt94TTw" and row["reconciled_video_id"]:
            continue
        stem = re.sub(r"(?:-SnapYT\.App| - Casual Finance \(.+?\))?\.mp4$", "", title)
        key = normalize(stem)
        candidates = []
        for entry in metadata:
            if entry["channel_id"] != "UCrNfRFWnLC3tCy1TnyhVQ7g":
                continue
            if entry["format_class"] != {"short": "SHORT", "long": "LONG_FORM"}[row["format"]]:
                continue
            if abs(float(entry["duration_sec"] or 0) - float(row["duration_s"])) > 2:
                continue
            archived = normalize(entry["title"])
            if key == archived or ("-SnapYT.App" in title and len(key) >= 7 and archived.startswith(key)):
                candidates.append(entry)
        if len(candidates) != 1 or candidates[0]["video_id"] in occupied:
            continue
        entry = candidates[0]
        occupied.add(entry["video_id"])
        row.update(
            reconciled_video_id=entry["video_id"],
            identity_basis="unique archived channel title or SnapYT prefix + format + duration within 2s (metadata linkage)",
            published_at=entry["published_at"],
            publication_year=entry["published_at"][:4],
        )

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus")
    parser.add_argument("metadata")
    args = parser.parse_args()
    with open(args.corpus, newline="") as file:
        reader = csv.DictReader(file)
        rows, columns = list(reader), reader.fieldnames
    with open(args.metadata, newline="") as file:
        reconcile(rows, list(csv.DictReader(file)))
    with open(args.corpus, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
