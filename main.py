"""Catalogue photo of an impossible gadget.

Writes the pre-rendered catalogue image to /output/entry.png.
Stdlib only; no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Preferred asset first; fall back to any gadget.* image in this dir.
CANDIDATES = ("gadget.jpg", "gadget.png", "gadget.jpeg")


def find_asset():
    for name in CANDIDATES:
        path = os.path.join(HERE, name)
        if os.path.isfile(path):
            return path
    for name in sorted(os.listdir(HERE)):
        if name.lower().startswith("gadget.") and name.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):
            return os.path.join(HERE, name)
    return None


def main():
    asset = find_asset()
    if asset is None:
        print("error: no gadget image found next to main.py", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(asset, "/output/entry.png")
    size = os.path.getsize("/output/entry.png")
    print(f"wrote /output/entry.png ({size} bytes) from {os.path.basename(asset)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
