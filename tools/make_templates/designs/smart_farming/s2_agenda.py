"""Slide 2: agenda, with the tractor photo on the left."""

from fe import assets

from .theme import BG, LIME, MUTED, PANEL_LINE, WHITE, footer, heading, new_slide

ROWS = [
    ("The Challenge", "Feeding more people"),
    ("Smart Tools", "Data in every field"),
    ("Key Numbers", "What farms gain"),
    ("The Seasons", "A year on the farm"),
]


def build():
    page = new_slide(2, photo_background=True)
    page.photo(assets.photo("tractor"), x=0, y=0, w=720, h=1080, focus=(0.68, 0.5), saturation=1.15, contrast=1.1,
               name="Photo")
    page.overlay([(BG + "00", 0), (BG + "ff", 1)], angle=0, name="Photo fade", box=(420, 0, 300, 1080))
    page.glow(1050, -350, 1100, 1100, LIME, opacity=0.20, name="Lime glow")
    footer(page, 2, brand=False)
    heading(page, "Agenda", x=860, size=100)
    for i, (title, note) in enumerate(ROWS):
        y = 290 + i * 170
        page.shape("ellipse", 860, y, 100, 100, LIME, name=f"Number circle {i + 1}")
        page.text(str(i + 1), 860, y + 18, 50, BG, width=100, align="center", name=f"Number {i + 1}")
        page.text(title, 1000, y - 6, 56, WHITE, name=f"Item {i + 1}")
        page.text(note, 1002, y + 62, 32, MUTED, bold=False, name=f"Item note {i + 1}")
        page.shape("rectangle", 860, y + 130, 940, 2, PANEL_LINE, name=f"Line {i + 1}")
    return page
