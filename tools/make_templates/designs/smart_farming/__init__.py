"""Presentation: Smart Farming (8 slides about modern agriculture: title, agenda, goal, challenges, smart tools,
numbers, a year on the farm, thank you). Each slide is its own small file."""

from . import (s1_title, s2_agenda, s3_statement, s4_challenges, s5_tools, s6_numbers, s7_seasons, s8_thanks)

META = {
    "id": "smart-farming", "type": "presentation", "name": "Smart Farming",
    "keywords": ["agriculture", "farm", "green", "education", "modern", "project"],
    "photos": ["wheat", "tractor", "satellite", "greenhouse"],
}

SLIDES = [s1_title, s2_agenda, s3_statement, s4_challenges, s5_tools, s6_numbers, s7_seasons, s8_thanks]


def build():
    return [slide.build() for slide in SLIDES]
