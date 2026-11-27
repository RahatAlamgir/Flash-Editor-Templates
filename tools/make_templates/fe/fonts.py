"""Finds the Windows font files the designs use (the app loads fonts by family name, so keep to Windows fonts)."""

import os
from functools import lru_cache

from PIL import ImageFont

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

# family -> (regular file, bold file). A family with one file is already heavy; "Bold" is then left off in the project.
FAMILIES = {
    "Segoe UI": ("segoeui.ttf", "segoeuib.ttf"),
    "Arial": ("arial.ttf", "arialbd.ttf"),
    "Arial Black": ("ariblk.ttf", "ariblk.ttf"),
    "Impact": ("impact.ttf", "impact.ttf"),
    "Bahnschrift": ("bahnschrift.ttf", "bahnschrift.ttf"),
    "Segoe Print": ("segoepr.ttf", "segoeprb.ttf"),
}


def has_real_bold(family):
    regular, bold = FAMILIES[family]
    return regular != bold


@lru_cache(maxsize=None)
def load(family, size, bold):
    regular, heavy = FAMILIES[family]
    path = os.path.join(FONT_DIR, heavy if bold else regular)
    return ImageFont.truetype(path, size=int(round(size)))
