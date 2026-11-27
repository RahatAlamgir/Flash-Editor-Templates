"""The template designs. Every module here has META (id, type, name, keywords) and build() -> list of Page."""

import importlib
import pkgutil


def all_designs():
    """Every design module, in file-name order."""
    found = []
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda m: m.name):
        found.append(importlib.import_module(f"{__name__}.{info.name}"))
    return found
