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

## Photos

Designs may use photos from `fe/assets.py` (public domain / CC0 pictures from Wikimedia Commons). Run
`python fetch_assets.py` once: it downloads them into `assets/cache/` (not in Git), refuses any picture whose licence is
not public domain / CC0, and writes `assets/credits.json`. `build.py` copies the credits into each catalog entry.
To use a new photo: add `"key": "File name on Commons"` to `ASSETS`, run `fetch_assets.py`, and *look at the picture*
before designing around it.

## Structure

    build.py                 the command above
    fetch_assets.py          downloads the photos (see Photos)
    assets/credits.json      source, author and licence of every photo
    designs/                 one file per template: META (id, type, name, keywords) and build() -> list of pages
    fe/                      the small library the designs use
        page.py              Page: background(), gradient(), shape(), text()  (one call = one editable layer)
        shapes.py            draws rectangle, ellipse, triangle, star, diamond, hexagon, burst
        gradient.py          linear and radial gradients
        text.py, fonts.py    lays out and draws text with Windows fonts (Segoe UI, Arial, Impact, ...)
        color.py             "#RRGGBB" / "#RRGGBBAA" helpers
        photo.py, effects.py cropping and tuning photos; baked shadows and arrows
        assets.py            the photo list and where the downloaded copies are
        writer.py            writes the .fe zip (project.json, preview.png, lossless WebP layers)

## Add a design

Copy a file in `designs/`, change `META` and `build()`, run `python build.py <id>`. Coordinates are in pixels of the
page. Text uses `x, y` for the top-left of its box; pass `width=` with `align="center"` to centre it in a box. Shapes
can be rotated (`rotation=` degrees) and made see-through (`opacity=`). Impact looks best with `bold=False`.

## Limits

* Only the shapes listed above, fills (no borders), and fonts every Windows PC has (the app finds fonts by name): Segoe UI,
  Arial, Impact, Georgia, Palatino Linotype, Times New Roman, Segoe Script, Segoe Print and a few more. `italic=True`
  works for families that have an italic file. `letter_spacing=` (percent of the font size) spaces capitals out.
* `page.crescent(...)` draws a crescent moon as a picture layer.
* Photos become plain picture layers (not frames), and shadows, glow and arrows are baked pictures. Groups, effects and animations are not made by this tool. Open the template in the app to add them.
* Text and shapes stay editable in the app; the layer picture is a cached drawing that the app redraws when edited.
