"""Makes the template files from the designs in designs/.

    python build.py                  make every design
    python build.py gaming-channel   make only these ids
    python build.py --no-pictures    only write template.fe (skip thumb.jpg / page-N.jpg / catalog sizes)

For each design it writes templates/<type>/<id>/template.fe and makes sure catalog.json has an entry. Unless
--no-pictures is given it then runs the app's own `build_templates` tool (from the Flash Editor Rust project,
unchanged) which opens every template with the app's code, so a file the app can't read fails here, and writes the
pictures plus the size / sha256 in the catalog.
"""

import datetime
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from designs import all_designs  # noqa: E402
from fe import assets, writer  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
RUST = os.environ.get("FE_RUST_DIR", r"D:\AiBuild\Flash Editor Rust")


def ensure_catalog_entry(catalog, meta, page):
    for entry in catalog["templates"]:
        if entry["id"] == meta["id"] and entry["type"] == meta["type"]:
            entry["name"], entry["keywords"] = meta["name"], meta["keywords"]
            if meta.get("photos"):
                entry["credits"] = assets.credits_for(meta["photos"])
            return
    credits = assets.credits_for(meta["photos"]) if meta.get("photos") else []
    catalog["templates"].append({
        "id": meta["id"], "type": meta["type"], "name": meta["name"], "keywords": meta["keywords"], "pages": 1,
        "width": page.width, "height": page.height, "bytes": 0, "sha256": "",
        "added": datetime.date.today().isoformat(),
        **({"credits": credits} if credits else {}),
    })


def main(argv):
    pictures = "--no-pictures" not in argv
    wanted = [a for a in argv if not a.startswith("--")]
    catalog_path = os.path.join(REPO, "catalog.json")
    with open(catalog_path, encoding="utf-8") as f:
        catalog = json.load(f)
    made = 0
    for module in all_designs():
        meta = module.META
        if wanted and meta["id"] not in wanted:
            continue
        pages = module.build()
        folder = os.path.join(REPO, "templates", meta["type"], meta["id"])
        os.makedirs(folder, exist_ok=True)
        size = writer.write(os.path.join(folder, "template.fe"), pages, presentation=meta["type"] == "presentation")
        ensure_catalog_entry(catalog, meta, pages[0])
        print(f"{meta['type']}/{meta['id']}: {len(pages)} page(s), {size // 1000} KB")
        made += 1
    if not made:
        sys.exit("nothing to make (check the ids)")
    with open(catalog_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
    if pictures:
        subprocess.run(["cargo", "run", "-p", "fe-app", "--release", "--example", "build_templates", "--", REPO],
                       cwd=RUST, check=True)


if __name__ == "__main__":
    main(sys.argv[1:])
