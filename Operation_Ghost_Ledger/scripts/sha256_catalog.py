#!/usr/bin/env python3
from pathlib import Path
import hashlib
import csv
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
out = Path("sha256_catalog_generated.csv")

with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Filename", "SHA-256", "Size"])
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name != out.name:
            h = hashlib.sha256()
            with p.open("rb") as fh:
                for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                    h.update(chunk)
            w.writerow([str(p), h.hexdigest(), p.stat().st_size])

print(f"Wrote {out}")
