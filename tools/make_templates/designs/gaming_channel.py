"""YouTube thumbnail: Gaming Channel (the first template, first drawn by hand in the app, now made by script)."""

from fe.page import Page

META = {
    "id": "gaming-channel", "type": "youtube-thumbnail", "name": "Gaming Channel",
    "keywords": ["gaming", "dark", "modern", "colorful"],
}


def build():
    page = Page(1280, 720)
    page.background("#ffffff")
    page.gradient([("#5856d6", 0), ("#404040", 1)], angle=90)
    page.shape("ellipse", 140, 20, 1000, 520, "#8b5cf6", opacity=0.30, name="Glow")
    page.shape("hexagon", 40, 420, 220, 220, "#ffffff", opacity=0.10, name="Hexagon left")
    page.shape("hexagon", 1010, 70, 230, 230, "#ffffff", opacity=0.10, name="Hexagon right")
    page.shape("star", 1060, 470, 130, 130, "#ffcc00", rotation=14, name="Star")
    page.shape("diamond", 120, 130, 60, 60, "#22d3ee", name="Diamond")
    page.text("EPIC GAMEPLAY", 237, 140, 105, "#ffffff")
    page.text("NEW EPISODE OUT NOW", 307, 330, 56, "#ffcc00")
    page.shape("burst", 532, 470, 216, 216, "#f97316", name="Burst")
    page.text("HOT", 578.5, 538, 58, "#ffffff")
    return [page]
