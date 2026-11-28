"""Photos used by the designs. Only public-domain / CC0 pictures from Wikimedia Commons (no credit needed, but credits
are still recorded in assets/credits.json and in the catalog).

`python fetch_assets.py` downloads them once into assets/cache/ (not in Git); designs then call `photo(key)`.
"""

import json
import os

from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
CACHE = os.path.join(ROOT, "cache")
CREDITS = os.path.join(ROOT, "credits.json")

# key -> file name on commons.wikimedia.org
ASSETS = {
    "nebula": "Crab Nebula, as Seen by Herschel and Hubble.jpg",
    "motherboard": "Computer-motherboard-pc-wires (23698613303).jpg",
    "burger": "Hamburger (black bg).jpg",
    "pizza": "Pizza 17.jpg",
    "lake": "Lake Mountain Landscape.jpg",
    "beach": "Ginowan Tropical Beach.JPG",
    "stadium": "Telstra Stadium at Night.jpg",
    "wheat": "Wheat field sunset (Unsplash).jpg",
    "tractor": "Tractor fertilizing a field in Brittany.jpg",
    "satellite": "Crops Kansas AST 20010624.jpg",
    "rose_garden": "White roses, Hochzeitsgarten, Idstein.jpg",
    "dahlia": "Close-up of Pink dahlia flower.jpg",
    "fireworks": "Bratislava New Year Fireworks.jpg",
    "mosque": "Mosque at sunset in Dubai.jpg",
    "cake": "Birthday Cake with Candles (Unsplash M20ylqCzSZw).jpg",
    "greenhouse": "Vegetable garden at Eisenhower National Historic Site with the greenhouse in the background. "
                  "(dcaee63f-c8bc-4b33-9dd2-3a5ce1e05021).jpg",
}


def cache_path(key):
    return os.path.join(CACHE, f"{key}.jpg")


def photo(key):
    """The downloaded picture as an RGB image."""
    path = cache_path(key)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"{key}: run `python fetch_assets.py` first")
    return Image.open(path).convert("RGB")


def credits_for(keys):
    """Short text lines for the catalog: 'title - author, license, page'."""
    with open(CREDITS, encoding="utf-8") as f:
        data = json.load(f)
    return [f"{data[k]['title']} - {data[k]['author']}, {data[k]['license']}, {data[k]['page']}" for k in keys]
