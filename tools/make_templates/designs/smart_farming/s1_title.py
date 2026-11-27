"""Slide 1: title over the wheat-at-sunset photo."""

from fe import assets

from .theme import AMBER, BG, LIME, MUTED, WHITE, new_slide


def build():
    page = new_slide(1, photo_background=True)
    page.photo(assets.photo("wheat"), focus=(0.5, 0.5), saturation=1.15, contrast=1.1, name="Photo")
    page.overlay([(BG + "f4", 0), (BG + "c0", 0.5), (BG + "20", 1)], angle=0, name="Dark left")
    page.shape("rectangle", 120, 170, 400, 60, AMBER, radius=30, name="Tag")
    page.text("FARMING THE FUTURE", 120, 181, 26, BG, width=400, align="center", name="Tag text")
    page.text("Smart", 120, 270, 130, WHITE, shadow=(6, 8, 14, 0.5))
    page.text("Farming", 120, 410, 200, LIME, shadow=(6, 8, 14, 0.5))
    page.text("Growing more with less water, land and waste.", 124, 700, 44, WHITE, bold=False)
    page.shape("rectangle", 124, 850, 8, 90, AMBER, name="Speaker bar")
    page.text("Presented by Your Name", 156, 848, 36, WHITE, name="Presenter")
    page.text("Your Farm or School  |  November 2026", 156, 896, 30, MUTED, bold=False, name="Company")
    return page
