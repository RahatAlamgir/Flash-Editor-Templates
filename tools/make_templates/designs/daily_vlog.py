"""YouTube thumbnail: Daily Vlog (warm pink-to-orange, sticker label)."""

from fe.page import Page

META = {
    "id": "daily-vlog", "type": "youtube-thumbnail", "name": "Daily Vlog",
    "keywords": ["colorful", "travel", "simple", "holiday"],
}


def build():
    page = Page(1280, 720)
    page.background("#ff7a59")
    page.gradient([("#ff4d8d", 0), ("#ff9f43", 1)], angle=35)
    page.shape("ellipse", -140, 420, 520, 520, "#ffffff", opacity=0.14, name="Circle left")
    page.shape("ellipse", 930, -150, 460, 460, "#ffffff", opacity=0.14, name="Circle right")
    page.shape("star", 1010, 430, 190, 190, "#ffe066", rotation=12, name="Star")
    page.shape("star", 120, 90, 90, 90, "#ffffff", rotation=-10, name="Star small")
    page.text("MY DAY", 0, 150, 250, "#ffffff", family="Impact", bold=False, width=1280, align="center")
    page.text("IN THE CITY", 0, 412, 120, "#2b1b3d", family="Impact", bold=False, width=1280, align="center")
    page.shape("rectangle", 440, 570, 400, 90, "#2b1b3d", radius=45, rotation=-4, name="Sticker")
    page.text("VLOG #01", 440, 584, 50, "#ffe066", width=400, align="center", rotation=-4)
    return [page]
