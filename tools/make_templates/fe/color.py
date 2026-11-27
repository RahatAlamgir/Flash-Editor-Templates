"""Colors: "#RRGGBB" text in the designs, RGBA tuples for drawing, {"R","G","B","A"} objects in project.json."""


def rgba(value, alpha=255):
    """"#RRGGBB" (or an (r, g, b) tuple) to an (r, g, b, a) tuple."""
    if isinstance(value, str):
        text = value.lstrip("#")
        return (int(text[0:2], 16), int(text[2:4], 16), int(text[4:6], 16), alpha)
    r, g, b = value[:3]
    return (r, g, b, alpha)


def to_json(color):
    r, g, b, a = rgba(color) if isinstance(color, str) else color
    return {"R": r, "G": g, "B": b, "A": a}
