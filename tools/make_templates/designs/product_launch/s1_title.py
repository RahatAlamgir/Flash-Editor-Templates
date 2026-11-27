"""Slide 1: title over the motherboard photo."""

from fe import assets

from .theme import BG, CYAN, MUTED, WHITE, new_slide


def build():
    page = new_slide(1, photo_background=True)
    page.photo(assets.photo("motherboard"), focus=(0.6, 0.5), saturation=1.2, contrast=1.15, name="Photo")
    page.overlay([(BG + "f6", 0), (BG + "d8", 0.5), (BG + "30", 1)], angle=0, name="Dark left")
    page.glow(-300, 500, 1000, 1000, CYAN, opacity=0.22, name="Cyan glow")
    page.shape("rectangle", 120, 170, 370, 60, CYAN, radius=30, name="Tag")
    page.text("PRODUCT LAUNCH 2026", 120, 181, 26, BG, width=370, align="center", name="Tag text")
    page.text("Introducing", 120, 270, 120, WHITE, shadow=(6, 8, 14, 0.5))
    page.text("Nova X", 120, 410, 200, CYAN, shadow=(6, 8, 14, 0.5))
    page.text("The next generation of everyday computing.", 124, 700, 46, WHITE, bold=False)
    page.shape("rectangle", 124, 850, 8, 90, CYAN, name="Speaker bar")
    page.text("Presented by Your Name", 156, 848, 36, WHITE, name="Presenter")
    page.text("Your Company  |  November 2026", 156, 896, 30, MUTED, bold=False, name="Company")
    return page
