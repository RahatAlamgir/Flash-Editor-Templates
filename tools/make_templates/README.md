# make_templates

Makes template files (`template.fe`) from small Python design files, so a new template takes minutes and the result is
the same every time. No Flash Editor window needs to be open.

## Use

Needs Python 3 with Pillow and numpy (`pip install pillow numpy`).

    python build.py                    make every design in designs/
    python build.py tech-review        make only this id
    python build.py --no-pictures      only write template.fe (no thumbnails, no catalog sizes)

For each design it writes `templates/<type>/<id>/template.fe` and adds the entry to `catalog.json` if it is new. Then it
runs the app's own `build_templates` tool (from the Flash Editor Rust project, which this tool never changes; set
`FE_RUST_DIR` if it is not in `D:\AiBuild\Flash Editor Rust`). That tool opens every template with the app's code, so a
file the app cannot read stops the build, and it writes `thumb.jpg`, `page-N.jpg`, and `bytes` / `sha256` in the catalog.

## Structure

    build.py                 the command above
    designs/                 one file per template: META (id, type, name, keywords) and build() -> list of pages
    fe/                      the small library the designs use
        page.py              Page: background(), gradient(), shape(), text()  (one call = one editable layer)
        shapes.py            draws rectangle, ellipse, triangle, star, diamond, hexagon, burst
        gradient.py          linear and radial gradients
        text.py, fonts.py    lays out and draws text with Windows fonts (Segoe UI, Arial, Impact, ...)
        color.py             "#RRGGBB" helpers
        writer.py            writes the .fe zip (project.json, preview.png, lossless WebP layers)

## Add a design

Copy a file in `designs/`, change `META` and `build()`, run `python build.py <id>`. Coordinates are in pixels of the
page. Text uses `x, y` for the top-left of its box; pass `width=` with `align="center"` to centre it in a box. Shapes
can be rotated (`rotation=` degrees) and made see-through (`opacity=`). Impact looks best with `bold=False`.

## Limits

* Only the shapes listed above, fills (no borders), and Windows fonts (the app finds fonts by name).
* Pictures, groups, effects and animations are not made by this tool. Open the template in the app to add them.
* Text and shapes stay editable in the app; the layer picture is a cached drawing that the app redraws when edited.
