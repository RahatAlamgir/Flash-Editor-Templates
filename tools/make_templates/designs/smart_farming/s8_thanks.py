"""Slide 8: thank you, with the greenhouse photo on the right."""

from fe import assets

from .theme import AMBER, BG, LIME, MUTED, WHITE, footer, new_slide


def build():
    page = new_slide(8, photo_background=True)
    page.glow(-350, 550, 1000, 1000, AMBER, opacity=0.12, name="Golden glow")
    page.photo(assets.photo("greenhouse"), x=1000, y=0, w=920, h=1080, focus=(0.62, 0.5), saturation=1.15,
               name="Photo")
    page.overlay([(BG + "ff", 0), (BG + "00", 1)], angle=0, name="Photo fade", box=(1000, 0, 420, 1080))
    footer(page, 8)
    page.text("Thank You", 120, 250, 170, WHITE, shadow=(6, 8, 16, 0.5), name="Title")
    page.text("Let's grow together.", 124, 500, 52, MUTED, bold=False, name="Subtitle")
    page.shape("rectangle", 124, 660, 580, 90, LIME, radius=45, name="Email pill")
    page.text("hello@yourfarm.com", 124, 681, 34, BG, width=580, align="center", name="Email")
    page.shape("rectangle", 124, 780, 580, 90, WHITE, radius=45, name="Website pill")
    page.text("www.yourfarm.com", 124, 801, 34, BG, width=580, align="center", name="Website")
    return page
