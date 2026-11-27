"""Slide 6: four big numbers."""

from .theme import AMBER, LIME, MUTED, ORANGE, PANEL, PANEL_LINE, SKY, WHITE, heading, new_slide

STATS = [
    ("30%", SKY, "Less water", "Smart irrigation\nsaves every drop"),
    ("25%", LIME, "Higher yield", "More food from\nthe same land"),
    ("2x", AMBER, "Faster work", "Drones and machines\nsave hours"),
    ("50%", ORANGE, "Less waste", "Plan better,\nthrow away less"),
]


def build():
    page = new_slide(6)
    heading(page, "What Farms Gain")
    for i, (number, color, label, note) in enumerate(STATS):
        x = 120 + i * 430
        page.shape("rectangle", x - 2, 318, 394, 564, PANEL_LINE, radius=30, name=f"Card border {i + 1}")
        page.shape("rectangle", x, 320, 390, 560, PANEL, radius=28, name=f"Card {i + 1}")
        page.shape("rectangle", x + 135, 372, 120, 8, color, radius=4, name=f"Accent {i + 1}")
        page.text(number, x, 425, 104, color, width=390, align="center", name=f"Number {i + 1}")
        page.text(label, x, 600, 42, WHITE, width=390, align="center", name=f"Label {i + 1}")
        page.text(note, x, 680, 30, MUTED, bold=False, width=390, align="center", name=f"Note {i + 1}")
    return page
