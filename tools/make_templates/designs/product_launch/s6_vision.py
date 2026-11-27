"""Slide 6: photo on the left, text on the right."""

from fe import assets

from .theme import BG, CYAN, WHITE, footer, new_slide

POINTS = ["Simple for everyone", "Powerful for experts", "Kind to the planet", "Open to new ideas"]


def build():
    page = new_slide(6, photo_background=True)
    page.photo(assets.photo("nebula"), x=0, y=0, w=900, h=1080, focus=(0.5, 0.5), saturation=1.25, contrast=1.1,
               name="Photo")
    page.overlay([(BG + "00", 0), (BG + "ff", 1)], angle=0, name="Photo fade", box=(500, 0, 400, 1080))
    page.glow(900, -300, 1100, 1100, "#8b5cf6", opacity=0.22, name="Violet glow")
    footer(page, 6)
    page.text("Our Vision", 980, 130, 100, WHITE, name="Title")
    page.shape("rectangle", 984, 275, 140, 8, CYAN, radius=4, name="Title bar")
    for i, point in enumerate(POINTS):
        y = 400 + i * 135
        page.shape("ellipse", 984, y + 18, 30, 30, CYAN, name=f"Dot {i + 1}")
        page.text(point, 1050, y, 54, WHITE, bold=False, name=f"Point {i + 1}")
    return page
