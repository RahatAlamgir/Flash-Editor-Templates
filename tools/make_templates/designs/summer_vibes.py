"""YouTube thumbnail: Summer Vibes (tropical beach photo, bright title, slanted banner)."""

from fe import assets
from fe.page import Page

META = {
    "id": "summer-vibes", "type": "youtube-thumbnail", "name": "Summer Vibes",
    "keywords": ["summer", "travel", "holiday", "colorful"], "photos": ["beach"],
}
OUTLINE = dict(outline=8, outline_color="#0f3d5e", shadow=(8, 10, 14, 0.6))


def build():
    page = Page(1280, 720)
    page.photo(assets.photo("beach"), focus=(0.5, 0.6), saturation=1.45, contrast=1.1, name="Beach photo")
    page.overlay([("#0b3a5acc", 0), ("#0b3a5a00", 0.6)], angle=90, name="Blue top")
    page.glow(850, -80, 520, 520, "#ffe066", opacity=0.7, name="Sun glow")
    page.text("SUMMER", 0, 25, 270, "#ffffff", family="Impact", bold=False, width=1280, align="center", **OUTLINE)
    page.shape("rectangle", 200, 345, 880, 130, "#ff3d81", radius=8, rotation=-3, name="Banner")
    page.text("VIBES ONLY", 200, 345, 118, "#ffffff", family="Impact", bold=False, width=880, align="center",
              rotation=-3, shadow=(5, 7, 8, 0.4))
    page.shape("rectangle", 440, 600, 400, 76, "#ffe066", radius=38, name="Label")
    page.text("WEEKLY VLOG  #12", 440, 611, 38, "#0f3d5e", width=400, align="center")
    page.shape("star", 90, 380, 130, 130, "#ffe066", rotation=-12, name="Star left")
    page.shape("star", 1060, 400, 110, 110, "#ffe066", rotation=14, name="Star right")
    return [page]
