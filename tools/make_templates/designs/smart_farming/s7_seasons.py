"""Slide 7: a year on the farm, four seasons on a timeline."""

from .theme import AMBER, LIME, MUTED, ORANGE, PANEL_LINE, SKY, WHITE, heading, new_slide

STEPS = [
    ("SPRING", LIME, "Plant", "Seeds go into\nthe ground."),
    ("SUMMER", AMBER, "Grow", "Water and care\nevery day."),
    ("AUTUMN", ORANGE, "Harvest", "Crops are picked\nand stored."),
    ("WINTER", SKY, "Plan", "Study the data and\nprepare next year."),
]


def build():
    page = new_slide(7)
    heading(page, "A Year on the Farm")
    page.shape("rectangle", 200, 536, 1520, 8, PANEL_LINE, radius=4, name="Timeline")
    for i, (season, color, title, text) in enumerate(STEPS):
        cx = 280 + i * 453
        page.text(season, cx - 210, 395, 46, color, width=420, align="center", letter_spacing=10, name=f"Season {i + 1}")
        page.shape("ellipse", cx - 44, 496, 88, 88, color, opacity=0.25, name=f"Dot halo {i + 1}")
        page.shape("ellipse", cx - 26, 514, 52, 52, color, name=f"Dot {i + 1}")
        page.text(title, cx - 210, 620, 46, WHITE, width=420, align="center", name=f"Step {i + 1}")
        page.text(text, cx - 210, 700, 30, MUTED, bold=False, width=420, align="center", name=f"Step text {i + 1}")
    return page
