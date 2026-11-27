"""YouTube thumbnail: Tech Review Pro (motherboard photo, price badge, arrow)."""

from fe import assets
from fe.page import Page

META = {
    "id": "tech-review-pro", "type": "youtube-thumbnail", "name": "Tech Review Pro",
    "keywords": ["tech", "dark", "modern", "gaming"], "photos": ["motherboard"],
}
CYAN = "#22d3ee"
OUTLINE = dict(outline=7, outline_color="#000000", shadow=(8, 10, 14, 0.65))


def build():
    page = Page(1280, 720)
    page.photo(assets.photo("motherboard"), focus=(0.55, 0.5), saturation=1.25, contrast=1.2, name="Motherboard photo")
    page.overlay([("#040814f0", 0), ("#040814c0", 0.5), ("#04081420", 1)], angle=0, name="Dark left")
    page.vignette(0.6)
    page.shape("rectangle", 60, 110, 16, 460, CYAN, name="Accent bar")
    page.text("HONEST", 105, 85, 120, CYAN, family="Impact", bold=False, **OUTLINE)
    page.text("REVIEW", 105, 190, 200, "#ffffff", family="Impact", bold=False, **OUTLINE)
    page.shape("rectangle", 105, 470, 560, 100, "#ffffff", radius=14, name="Question box")
    page.text("IS IT WORTH IT?", 105, 487, 66, "#0b1020", family="Impact", bold=False, width=560, align="center")
    page.shape("rectangle", 105, 40, 210, 50, "#e11d48", radius=8, name="Tag")
    page.text("2026 EDITION", 105, 46, 28, "#ffffff", width=210, align="center")
    page.arrow((720, 640), (900, 440), "#ff2d2d", width=30)
    page.shape("burst", 1000, 400, 240, 240, "#ffd400", rotation=-10, name="Price burst")
    page.text("ONLY", 1000, 455, 34, "#111111", width=240, align="center", rotation=-10)
    page.text("$499", 1000, 490, 74, "#111111", family="Impact", bold=False, width=240, align="center", rotation=-10)
    return [page]
