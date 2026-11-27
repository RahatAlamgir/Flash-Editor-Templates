"""Colours and the shared look of the Product Launch slides."""

from fe.page import Page

W, H = 1920, 1080
BG = "#0b1020"
PANEL = "#131c38"
PANEL_LINE = "#1f2b52"
CYAN = "#22d3ee"
VIOLET = "#8b5cf6"
PINK = "#f472b6"
WHITE = "#ffffff"
MUTED = "#a8b3cf"


def new_slide(number, photo_background=False):
    """A blank slide with the dark background, soft colour glows and the small footer (skipped over a photo)."""
    page = Page(W, H, name=f"Slide {number}")
    page.background(BG)
    if not photo_background:
        page.glow(1050, -350, 1100, 1100, VIOLET, opacity=0.30, name="Violet glow")
        page.glow(-350, 550, 1000, 1000, CYAN, opacity=0.16, name="Cyan glow")
        footer(page, number)
    return page


def footer(page, number):
    page.text("NOVA X  |  PRODUCT LAUNCH 2026", 120, 1000, 22, MUTED, bold=False, name="Footer")
    page.text(f"{number:02d}", 1700, 1000, 24, MUTED, width=100, align="right", name="Slide number")


def heading(page, text, x=120, y=80, size=84):
    """Slide title with a short accent bar under it."""
    page.text(text, x, y, size, WHITE, name="Title")
    page.shape("rectangle", x + 4, y + round(size * 1.36) + 6, 140, 8, CYAN, radius=4, name="Title bar")
