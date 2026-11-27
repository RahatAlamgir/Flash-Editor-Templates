"""YouTube thumbnail: Tech Review (dark blue, cyan accent, big two-line title)."""

from fe.page import Page

META = {
    "id": "tech-review", "type": "youtube-thumbnail", "name": "Tech Review",
    "keywords": ["tech", "dark", "modern", "gaming"],
}

CYAN = "#22d3ee"


def build():
    page = Page(1280, 720)
    page.background("#0b1020")
    page.gradient([("#1d3a8a", 0), ("#0b1020", 1)], radial=True)
    # decoration on the right
    page.shape("hexagon", 700, 90, 460, 460, CYAN, opacity=0.18, name="Hexagon big")
    page.shape("hexagon", 800, 190, 260, 260, CYAN, opacity=0.35, name="Hexagon middle")
    page.shape("diamond", 880, 270, 100, 100, "#ffffff", name="Diamond")
    page.shape("ellipse", 1090, 520, 70, 70, CYAN, opacity=0.6, name="Dot")
    # title
    page.shape("rectangle", 70, 190, 14, 380, CYAN, name="Accent bar")
    page.text("TECH", 120, 130, 210, "#ffffff", family="Impact", bold=False)
    page.text("REVIEW", 120, 352, 210, CYAN, family="Impact", bold=False)
    page.shape("rectangle", 120, 612, 430, 70, "#ffffff", radius=35, name="Label")
    page.text("IS IT WORTH IT?", 120, 618, 38, "#0b1020", width=430, align="center")
    return [page]
