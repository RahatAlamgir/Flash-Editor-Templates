"""Slide 3: one big statement."""

from .theme import AMBER, LIME, MUTED, WHITE, new_slide


def build():
    page = new_slide(3)
    page.glow(400, 100, 1120, 1120, LIME, opacity=0.18, name="Center glow")
    page.text("OUR GOAL", 0, 190, 36, AMBER, width=1920, align="center", letter_spacing=20, name="Label")
    page.text("Feed the world,\nprotect the soil.", 0, 290, 130, WHITE, width=1920, align="center",
              shadow=(6, 8, 16, 0.5), name="Statement")
    page.shape("rectangle", 900, 700, 120, 8, LIME, radius=4, name="Divider")
    page.text("A new way to grow", 0, 740, 38, MUTED, bold=False, width=1920, align="center", name="Signature")
    return page
