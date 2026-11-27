"""YouTube thumbnail: How To Tutorial (light, clean, green step badge)."""

from fe.page import Page

META = {
    "id": "how-to-tutorial", "type": "youtube-thumbnail", "name": "How To Tutorial",
    "keywords": ["education", "simple", "minimal", "tech"],
}

GREEN = "#16a34a"
INK = "#111827"


def build():
    page = Page(1280, 720)
    page.background("#f8fafc")
    page.shape("rectangle", 0, 0, 1280, 30, GREEN, name="Top stripe")
    page.shape("rectangle", 0, 690, 1280, 30, GREEN, name="Bottom stripe")
    page.shape("hexagon", 830, 130, 380, 380, "#dcfce7", name="Hexagon big")
    page.shape("hexagon", 900, 200, 240, 240, GREEN, name="Hexagon small")
    page.text("1", 900, 200, 190, "#ffffff", width=240, align="center", family="Impact", bold=False)
    page.shape("rectangle", 90, 120, 330, 64, GREEN, radius=32, name="Label")
    page.text("STEP BY STEP", 90, 126, 36, "#ffffff", width=330, align="center")
    page.text("HOW TO", 90, 200, 190, INK, family="Impact", bold=False)
    page.text("GET STARTED", 90, 400, 120, GREEN, family="Impact", bold=False)
    page.text("Easy guide for beginners", 90, 560, 46, "#475569", bold=False)
    return [page]
