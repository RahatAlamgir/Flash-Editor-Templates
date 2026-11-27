"""YouTube thumbnail: Match Day Live (stadium at night, LIVE tag, VS score board)."""

from fe import assets
from fe.page import Page

META = {
    "id": "match-day-live", "type": "youtube-thumbnail", "name": "Match Day Live",
    "keywords": ["sports", "dark", "red", "modern"], "photos": ["stadium"],
}
OUTLINE = dict(outline=7, outline_color="#000000", shadow=(8, 10, 14, 0.7))


def build():
    page = Page(1280, 720)
    page.photo(assets.photo("stadium"), focus=(0.5, 0.45), saturation=1.3, contrast=1.2, brightness=0.9,
               name="Stadium photo")
    page.overlay([("#0a1030c8", 0), ("#0a103040", 0.5), ("#000000e0", 1)], angle=90, name="Dark blue")
    page.vignette(0.6)
    page.shape("rectangle", 60, 50, 190, 70, "#e11d48", radius=10, name="Live tag")
    page.shape("ellipse", 80, 73, 24, 24, "#ffffff", name="Live dot")
    page.text("LIVE", 112, 56, 46, "#ffffff", family="Impact", bold=False)
    page.text("MATCH DAY", 0, 120, 215, "#ffffff", family="Impact", bold=False, width=1280, align="center", **OUTLINE)
    page.shape("rectangle", 110, 470, 410, 130, "#e11d48", radius=14, rotation=-2, name="Home box")
    page.text("HOME", 110, 497, 84, "#ffffff", family="Impact", bold=False, width=410, align="center", rotation=-2)
    page.shape("rectangle", 760, 470, 410, 130, "#2563eb", radius=14, rotation=2, name="Away box")
    page.text("AWAY", 760, 497, 84, "#ffffff", family="Impact", bold=False, width=410, align="center", rotation=2)
    page.shape("burst", 520, 440, 240, 240, "#facc15", name="VS burst")
    page.text("VS", 520, 502, 100, "#111111", family="Impact", bold=False, width=240, align="center")
    return [page]
