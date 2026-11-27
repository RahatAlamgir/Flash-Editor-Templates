"""YouTube thumbnail: Pizza Taste Test (pizza photo, big title, rating burst, arrow)."""

from fe import assets
from fe.page import Page

META = {
    "id": "pizza-taste-test", "type": "youtube-thumbnail", "name": "Pizza Taste Test",
    "keywords": ["food", "red", "colorful", "simple"], "photos": ["pizza"],
}
OUTLINE = dict(outline=8, outline_color="#000000", shadow=(8, 10, 14, 0.7))


def build():
    page = Page(1280, 720)
    page.photo(assets.photo("pizza"), focus=(0.5, 0.5), saturation=1.35, contrast=1.15, name="Pizza photo")
    page.overlay([("#000000a8", 0), ("#00000000", 0.5)], angle=90, name="Dark top")
    page.overlay([("#00000000", 0.55), ("#000000c0", 1)], angle=90, name="Dark bottom")
    page.vignette(0.5)
    page.text("BEST PIZZA", 0, 10, 215, "#ffd400", family="Impact", bold=False, width=1280, align="center", **OUTLINE)
    page.shape("rectangle", 330, 575, 620, 90, "#e11d48", radius=14, name="Label")
    page.text("TASTE TEST", 330, 579, 76, "#ffffff", family="Impact", bold=False, width=620, align="center")
    page.shape("burst", 70, 300, 250, 250, "#16a34a", rotation=-8, name="Rating burst")
    page.text("9/10", 70, 380, 86, "#ffffff", family="Impact", bold=False, width=250, align="center", rotation=-8)
    page.arrow((1130, 330), (960, 430), "#ffffff", width=26, outline="#e11d48")
    return [page]
