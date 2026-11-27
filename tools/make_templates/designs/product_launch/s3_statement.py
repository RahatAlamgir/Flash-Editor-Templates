"""Slide 3: one big statement."""

from .theme import CYAN, MUTED, VIOLET, WHITE, new_slide


def build():
    page = new_slide(3)
    page.glow(400, 100, 1120, 1120, VIOLET, opacity=0.25, name="Center glow")
    page.text("OUR MISSION", 0, 190, 36, CYAN, width=1920, align="center", letter_spacing=20, name="Label")
    page.text("Technology should\nfeel effortless.", 0, 290, 130, WHITE, width=1920, align="center",
              shadow=(6, 8, 16, 0.5), name="Statement")
    page.shape("rectangle", 900, 700, 120, 8, CYAN, radius=4, name="Divider")
    page.text("The Nova X Team", 0, 740, 38, MUTED, bold=False, width=1920, align="center", name="Signature")
    return page
