"""Finds the Windows font files the designs use (the app loads fonts by family name, so keep to fonts every Windows
PC has: no Office-only fonts)."""

import os
from functools import lru_cache

from PIL import ImageFont

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

# family -> (regular, bold, italic, bold italic) file names; None = the family has no such file.
# A family whose bold file is the regular file is already heavy: "Bold" is then left off in the project.
FAMILIES = {
    "Segoe UI": ("segoeui.ttf", "segoeuib.ttf", "segoeuii.ttf", "segoeuiz.ttf"),
    "Arial": ("arial.ttf", "arialbd.ttf", "ariali.ttf", "arialbi.ttf"),
    "Arial Black": ("ariblk.ttf", "ariblk.ttf", None, None),
    "Impact": ("impact.ttf", "impact.ttf", None, None),
    "Bahnschrift": ("bahnschrift.ttf", "bahnschrift.ttf", None, None),
    "Segoe Print": ("segoepr.ttf", "segoeprb.ttf", None, None),
    "Segoe Script": ("segoesc.ttf", "segoescb.ttf", None, None),
    "Georgia": ("georgia.ttf", "georgiab.ttf", "georgiai.ttf", "georgiaz.ttf"),
    "Palatino Linotype": ("pala.ttf", "palab.ttf", "palai.ttf", "palabi.ttf"),
    "Times New Roman": ("times.ttf", "timesbd.ttf", "timesi.ttf", "timesbi.ttf"),
}


def has_real_bold(family):
    files = FAMILIES[family]
    return files[0] != files[1]


def has_italic(family):
    return FAMILIES[family][2] is not None


@lru_cache(maxsize=None)
def load(family, size, bold, italic=False):
    regular, heavy, slanted, heavy_slanted = FAMILIES[family]
    if italic and slanted:
        name = (heavy_slanted or slanted) if bold else slanted
    else:
        name = heavy if bold else regular
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size=int(round(size)))
