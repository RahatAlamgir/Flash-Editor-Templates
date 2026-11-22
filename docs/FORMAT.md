# Format (draft, nothing is built yet)

## Templates (shown in Project Manager > New project)

One folder per template, inside the folder of its type:

    templates/<type-id>/<template-id>/
        template.flash     the editable project (one or more pages)
        thumb.jpg          preview shown in the browser (about 400 px wide)

Type ids and their normal sizes are in `types.json`. A template may use another size than its type's normal one.

## catalog.json entry (made by a script, not by hand)

    {
      "id": "new-year-sale",
      "type": "youtube-thumbnail",
      "name": "New Year Sale",
      "keywords": ["new year", "sale", "business", "gift"],
      "pages": 1,
      "width": 1280,
      "height": 720,
      "bytes": 123456,
      "sha256": "...",
      "added": "2026-11-22"
    }

Search matches the name, the type name and the keywords. `added` drives the "New" badge and newest-first order.

## Keywords

English only, lowercase. The preferred list is in `keywords.json`; new ones may be added.

## Elements and styles (planned, format not decided yet)

    elements/icons/        icon packs
    elements/graphics/     lines, arrows, blobs, decorations, frames, patterns
    elements/badges/       ready-made labels
    styles/text-looks/     text designs (font, color or gradient, effects)

These will be small data files (vector shapes / settings, never code) with their own entries and keywords in `catalog.json`.

## Rules

* Data only: no code, no macros, no scripts inside any file.
* Only content you made yourself or that is free to reuse (note the license in the entry).
* Keep each template small: shapes, text and icons instead of big photos; JPG / WebP, shown size only.
