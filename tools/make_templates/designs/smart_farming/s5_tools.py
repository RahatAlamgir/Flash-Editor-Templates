"""Slide 5: text on the left, satellite crop map on the right."""

from fe import assets

from .theme import BG, LIME, WHITE, footer, new_slide

POINTS = ["Sensors in the soil", "Drones over the fields", "Satellite crop maps", "Smart irrigation"]


def build():
    page = new_slide(5, photo_background=True)
    page.glow(-350, 550, 1000, 1000, "#fbbf24", opacity=0.12, name="Golden glow")
    page.photo(assets.photo("satellite"), x=1020, y=0, w=900, h=1080, focus=(0.5, 0.5), saturation=1.1,
               name="Photo")
    page.overlay([(BG + "ff", 0), (BG + "00", 1)], angle=0, name="Photo fade", box=(1020, 0, 400, 1080))
    footer(page, 5)
    page.text("Smart Tools", 120, 130, 100, WHITE, name="Title")
    page.shape("rectangle", 124, 275, 140, 8, LIME, radius=4, name="Title bar")
    for i, point in enumerate(POINTS):
        y = 400 + i * 135
        page.shape("ellipse", 124, y + 18, 30, 30, LIME, name=f"Dot {i + 1}")
        page.text(point, 190, y, 54, WHITE, bold=False, name=f"Point {i + 1}")
    return page
