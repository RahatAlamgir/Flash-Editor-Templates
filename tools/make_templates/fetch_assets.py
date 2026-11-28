"""Downloads the photos listed in fe/assets.py from Wikimedia Commons and writes assets/credits.json.

    python fetch_assets.py          download what is missing
    python fetch_assets.py --force  download everything again

Each picture is fetched as a copy no wider than 2400 px (plenty for a 1280 px thumbnail). The licence is read from
Commons and anything that is not public domain / CC0 is refused.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from fe import assets  # noqa: E402

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "flash-editor-templates-asset-fetch/1.0"}
WIDTH = 2400


def fetch(url, tries=6):
    """Download a URL. Wikimedia answers "429 Too Many Requests" when asked too fast: wait and try again."""
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=120).read()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == tries - 1:
                raise
            wait = int(error.headers.get("Retry-After", 0) or 0) or 8 * (attempt + 1)
            print(f"  (asked too fast, waiting {wait} s)")
            time.sleep(wait)


def info(title):
    query = {"action": "query", "titles": "File:" + title, "prop": "imageinfo", "iiprop": "extmetadata|url|size",
             "format": "json"}
    data = json.loads(fetch(API + "?" + urllib.parse.urlencode(query)))
    page = next(iter(data["query"]["pages"].values()))
    return page["imageinfo"][0]


def plain(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()


def main(force):
    os.makedirs(assets.CACHE, exist_ok=True)
    known = {}
    if os.path.isfile(assets.CREDITS) and not force:
        with open(assets.CREDITS, encoding="utf-8") as f:
            known = json.load(f)
    credits = {}
    for key, title in assets.ASSETS.items():
        path = assets.cache_path(key)
        if not force and os.path.isfile(path) and known.get(key, {}).get("title") == title:
            credits[key] = known[key]      # already downloaded and its licence was checked: no need to ask again
            print(f"{key}: already there")
            continue
        meta = info(title)
        extra = meta["extmetadata"]
        license_name = extra.get("LicenseShortName", {}).get("value", "?")
        if not any(word in license_name.lower() for word in ("cc0", "public domain")):
            sys.exit(f"{key}: licence '{license_name}' is not public domain / CC0, refusing")
        credits[key] = {"title": title, "author": plain(extra.get("Artist", {}).get("value", "unknown")) or "unknown",
                        "license": license_name, "page": meta["descriptionurl"]}
        path = assets.cache_path(key)
        if force or not os.path.isfile(path):
            url = "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(title) + f"?width={WIDTH}"
            data = fetch(url)
            with open(path, "wb") as f:
                f.write(data)
            print(f"{key}: {len(data) // 1000} KB  ({license_name})")
        else:
            print(f"{key}: already there")
    with open(assets.CREDITS, "w", encoding="utf-8", newline="\n") as f:
        json.dump(credits, f, indent=2, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main("--force" in sys.argv)
