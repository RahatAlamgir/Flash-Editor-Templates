"""Colors: "#RRGGBB" or "#RRGGBBAA" text in the designs, RGBA tuples for drawing, {"R","G","B","A"} in project.json."""


def rgba(value, alpha=255):
    """"#RRGGBB" / "#RRGGBBAA" (or an (r, g, b[, a]) tuple) to an (r, g, b, a) tuple."""
    if isinstance(value, str):
        text = value.lstrip("#")
        if len(text) == 8:
            alpha = int(text[6:8], 16)
        return (int(text[0:2], 16), int(text[2:4], 16), int(text[4:6], 16), alpha)
    r, g, b = value[:3]
    return (r, g, b, value[3] if len(value) > 3 else alpha)


def to_json(color):
    r, g, b, a = rgba(color)
    return {"R": r, "G": g, "B": b, "A": a}
