"""Slide 4: three challenge cards."""

from .theme import AMBER, LIME, MUTED, PANEL, PANEL_LINE, SKY, WHITE, heading, new_slide

CARDS = [
    ("diamond", SKY, "Water", "Farms use 70% of the\nworld's fresh water."),
    ("hexagon", AMBER, "Soil", "Good soil takes years\nto build and days\nto lose."),
    ("star", LIME, "Climate", "Heat and storms make\nharvests hard to\nplan."),
]


def build():
    page = new_slide(4)
    heading(page, "Three Big Challenges", size=84)
    for i, (kind, color, title, text) in enumerate(CARDS):
        x = 120 + i * 580
        page.shape("rectangle", x - 2, 338, 544, 504, PANEL_LINE, radius=30, name=f"Card border {i + 1}")
        page.shape("rectangle", x, 340, 540, 500, PANEL, radius=28, name=f"Card {i + 1}")
        page.shape("ellipse", x + 40, 380, 120, 120, color, opacity=0.22, name=f"Icon halo {i + 1}")
        page.shape(kind, x + 65, 405, 70, 70, color, name=f"Icon {i + 1}")
        page.text(title, x + 40, 540, 56, WHITE, name=f"Card title {i + 1}")
        page.text(text, x + 42, 630, 34, MUTED, bold=False, name=f"Card text {i + 1}")
    return page
