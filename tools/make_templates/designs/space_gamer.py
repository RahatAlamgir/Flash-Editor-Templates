"""YouTube thumbnail: Space Gamer (NASA nebula photo, dark left side for a huge two-line title)."""

from fe import assets
from fe.page import Page

META = {
    "id": "space-gamer", "type": "youtube-thumbnail", "name": "Space Gamer",
    "keywords": ["gaming", "dark", "tech", "modern"], "photos": ["nebula"],
}
OUTLINE = dict(outline=7, outline_color="#000000", shadow=(8, 10, 14, 0.65))


def build():
    page = Page(1280, 720)
    page.background("#000000")
    page.glow(560, 0, 900, 900, "#7c3aed", opacity=0.5, name="Purple glow")
    page.photo(assets.photo("nebula"), x=340, y=0, w=940, h=720, focus=(0.5, 0.5), saturation=1.25, contrast=1.1,
               name="Nebula photo")
    page.overlay([("#000000ff", 0), ("#00000000", 1)], angle=0, name="Seam fade", box=(340, 0, 320, 720))
    page.vignette(0.6)
    page.shape("rectangle", 70, 60, 300, 64, "#ffd400", rotation=-3, name="Tag")
    page.text("NEW SERIES", 70, 69, 36, "#111111", width=300, align="center", rotation=-3, name="Tag text")
    page.text("GALAXY", 60, 120, 225, "#ffffff", family="Impact", bold=False, **OUTLINE)
    page.text("WARS", 60, 345, 225, "#ffd400", family="Impact", bold=False, **OUTLINE)
    page.shape("rectangle", 70, 622, 330, 66, "#e11d48", radius=12, name="Episode box")
    page.text("EPISODE 12", 70, 631, 38, "#ffffff", width=330, align="center")
    page.shape("burst", 1020, 50, 210, 210, "#e11d48", rotation=8, name="Burst")
    page.text("PART", 1020, 97, 40, "#ffffff", family="Impact", bold=False, width=210, align="center", rotation=8)
    page.text("2", 1020, 130, 92, "#ffffff", family="Impact", bold=False, width=210, align="center", rotation=8)
    return [page]
