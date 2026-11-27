"""Slide 8: thank you."""

from .theme import BG, CYAN, MUTED, VIOLET, WHITE, new_slide


def build():
    page = new_slide(8)
    page.glow(360, 60, 1200, 1200, VIOLET, opacity=0.30, name="Center glow")
    page.glow(-200, -300, 900, 900, CYAN, opacity=0.18, name="Corner glow")
    page.text("Thank You", 0, 250, 220, WHITE, width=1920, align="center", shadow=(6, 8, 16, 0.5), name="Title")
    page.text("Questions? Let's talk.", 0, 560, 56, MUTED, bold=False, width=1920, align="center", name="Subtitle")
    page.shape("rectangle", 410, 740, 540, 90, CYAN, radius=45, name="Email pill")
    page.text("hello@yourcompany.com", 410, 761, 34, BG, width=540, align="center", name="Email")
    page.shape("rectangle", 990, 740, 520, 90, WHITE, radius=45, name="Website pill")
    page.text("www.yourcompany.com", 990, 761, 34, BG, width=520, align="center", name="Website")
    return page
