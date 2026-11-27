"""Colours and the shared look of the Smart Farming slides (deep green, lime and golden accents)."""

from fe.page import Page

W, H = 1920, 1080
BG = "#0b1a12"
PANEL = "#12281b"
PANEL_LINE = "#1d3b29"
LIME = "#a3e635"
AMBER = "#fbbf24"
SKY = "#38bdf8"
ORANGE = "#fb923c"
WHITE = "#ffffff"
MUTED = "#a9c4b2"


def new_slide(number, photo_background=False):
    """A blank slide: dark green, soft glows, small footer (a photo slide adds its own footer after the photo)."""
    page = Page(W, H, name=f"Slide {number}")
    page.background(BG)
    if not photo_background:
        page.glow(1050, -350, 1100, 1100, LIME, opacity=0.20, name="Lime glow")
        page.glow(-350, 550, 1000, 1000, AMBER, opacity=0.12, name="Golden glow")
        footer(page, number)
    return page


def footer(page, number, brand=True):
    if brand:
        page.text("SMART FARMING  |  AGRICULTURE TODAY", 120, 1000, 22, MUTED, bold=False, name="Footer")
    page.text(f"{number:02d}", 1700, 1000, 24, MUTED, width=100, align="right", name="Slide number")


def heading(page, text, x=120, y=80, size=84):
    """Slide title with a short accent bar under it."""
    page.text(text, x, y, size, WHITE, name="Title")
    page.shape("rectangle", x + 4, y + round(size * 1.36) + 6, 140, 8, LIME, radius=4, name="Title bar")
