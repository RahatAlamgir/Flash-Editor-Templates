"""YouTube thumbnail: Hidden Lake Vlog (mountain lake photo, bottom title band, tags)."""

from fe import assets
from fe.page import Page

META = {
    "id": "hidden-lake-vlog", "type": "youtube-thumbnail", "name": "Hidden Lake Vlog",
    "keywords": ["travel", "holiday", "simple", "modern"], "photos": ["lake"],
}
OUTLINE = dict(outline=7, outline_color="#000000", shadow=(8, 10, 14, 0.7))


def build():
    page = Page(1280, 720)
    page.photo(assets.photo("lake"), focus=(0.5, 0.5), saturation=1.3, contrast=1.15, name="Lake photo")
    page.overlay([("#00000000", 0.35), ("#000000d0", 1)], angle=90, name="Dark bottom")
    page.overlay([("#00000090", 0), ("#00000000", 1)], angle=90, name="Dark top", box=(0, 0, 1280, 200))
    page.vignette(0.45)
    page.shape("rectangle", 60, 50, 230, 64, "#ef4444", radius=10, rotation=-3, name="Tag")
    page.text("TRAVEL VLOG", 60, 61, 32, "#ffffff", width=230, align="center", rotation=-3)
    page.shape("rectangle", 960, 50, 260, 64, "#ffffff", radius=32, name="Episode pill")
    page.text("EP. 04", 960, 62, 36, "#111111", width=260, align="center")
    page.text("HIDDEN", 60, 335, 150, "#ffffff", family="Impact", bold=False, **OUTLINE)
    page.text("LAKE", 60, 455, 240, "#facc15", family="Impact", bold=False, **OUTLINE)
    page.text("WE FOUND PARADISE", 560, 560, 52, "#ffffff", **OUTLINE)
    page.arrow((820, 540), (700, 330), "#facc15", width=26)
    return [page]
