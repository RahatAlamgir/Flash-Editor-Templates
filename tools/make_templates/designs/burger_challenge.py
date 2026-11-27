"""YouTube thumbnail: Burger Challenge (burger photo on black, red/yellow title, timer burst)."""

from fe import assets
from fe.page import Page

META = {
    "id": "burger-challenge", "type": "youtube-thumbnail", "name": "Burger Challenge",
    "keywords": ["food", "red", "dark", "colorful"], "photos": ["burger"],
}
OUTLINE = dict(outline=7, outline_color="#000000", shadow=(8, 10, 14, 0.65))


def build():
    page = Page(1280, 720)
    page.background("#050505")
    page.glow(520, 60, 760, 760, "#dc2626", opacity=0.55, name="Red glow")
    page.photo(assets.photo("burger"), x=300, y=0, w=980, h=720, focus=(0.5, 0.55), saturation=1.3, contrast=1.1,
               name="Burger photo")
    page.overlay([("#050505ff", 0), ("#05050500", 1)], angle=0, name="Seam fade", box=(300, 0, 300, 720))
    page.vignette(0.55)
    page.text("BIGGEST", 55, 40, 150, "#ffffff", family="Impact", bold=False, **OUTLINE)
    page.text("BURGER", 55, 170, 230, "#ffc400", family="Impact", bold=False, **OUTLINE)
    page.text("CHALLENGE", 55, 365, 170, "#ef4444", family="Impact", bold=False, **OUTLINE)
    page.shape("rectangle", 60, 600, 400, 80, "#ffffff", radius=40, rotation=-3, name="Label")
    page.text("CAN I FINISH IT?", 60, 612, 40, "#111111", width=400, align="center", rotation=-3)
    page.shape("burst", 1040, 30, 220, 220, "#16a34a", rotation=10, name="Burst")
    page.text("10", 1040, 50, 92, "#ffffff", family="Impact", bold=False, width=220, align="center", rotation=10)
    page.text("MINUTES", 1040, 160, 34, "#ffffff", family="Impact", bold=False, width=220, align="center", rotation=10)
    return [page]
