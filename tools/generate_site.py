from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.message import render_message
DATA = ROOT / "data" / "name.txt"
OUT = ROOT / "dist" / "index.html"


def main():
    name = DATA.read_text(encoding="utf-8").strip()
    rendered = render_message(name)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Day4 Artifact Demo</title>
  <style>
    body {{ font-family: Arial, Helvetica, sans-serif; padding: 24px; }}
    .box {{ max-width: 720px; border: 1px solid #ddd; border-radius: 8px; padding: 16px; }}
  </style>
</head>
<body>
  <div class="box">
    <h1>CI + Artifact CD Demo</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Message:</strong> {rendered}</p>
    <p><strong>Generated at (UTC):</strong> {now}</p>
  </div>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
