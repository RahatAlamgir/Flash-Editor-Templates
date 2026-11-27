"""Presentation: Product Launch (8 dark, modern slides: title, agenda, statement, features, numbers, vision, roadmap,
thank you). Each slide is its own small file."""

from . import (s1_title, s2_agenda, s3_statement, s4_features, s5_stats, s6_vision, s7_roadmap, s8_thanks)

META = {
    "id": "product-launch", "type": "presentation", "name": "Product Launch",
    "keywords": ["business", "tech", "startup", "modern", "dark", "corporate"], "photos": ["motherboard", "nebula"],
}

SLIDES = [s1_title, s2_agenda, s3_statement, s4_features, s5_stats, s6_vision, s7_roadmap, s8_thanks]


def build():
    return [slide.build() for slide in SLIDES]
