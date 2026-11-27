"""YouTube thumbnail: Easy Recipe (red and yellow, burst badge)."""

from fe.page import Page

META = {
    "id": "easy-recipe", "type": "youtube-thumbnail", "name": "Easy Recipe",
    "keywords": ["food", "colorful", "red", "simple"],
}


def build():
    page = Page(1280, 720)
    page.background("#dc2626")
    page.gradient([("#ef4444", 0), ("#991b1b", 1)], radial=True)
    page.shape("rectangle", 0, 560, 1280, 160, "#fde047", name="Yellow band")
    page.shape("ellipse", 760, 120, 420, 420, "#fef3c7", name="Plate")
    page.shape("ellipse", 810, 170, 320, 320, "#f59e0b", name="Plate inner")
    page.shape("ellipse", 880, 240, 180, 180, "#b45309", name="Food")
    page.text("EASY", 80, 90, 230, "#ffffff", family="Impact", bold=False)
    page.text("RECIPE", 80, 290, 230, "#fde047", family="Impact", bold=False)
    page.text("DELICIOUS DINNER AT HOME", 80, 590, 56, "#7f1d1d", family="Impact", bold=False)
    page.shape("burst", 1010, 40, 230, 230, "#16a34a", name="Burst")
    page.text("10", 1010, 88, 90, "#ffffff", family="Impact", bold=False, width=230, align="center")
    page.text("MIN", 1010, 176, 44, "#ffffff", family="Impact", bold=False, width=230, align="center")
    return [page]
