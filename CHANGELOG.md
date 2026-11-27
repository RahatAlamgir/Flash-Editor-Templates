# Changelog

Changes to the template repository, newest first. (The app's own change log is in the Flash Editor project.)

## 2026-11-28 · Presentation type

- The two presentation templates (business-pitch, school-project) are now saved as presentations (`"ProjectType": "presentation"`
  inside `template.fe`), so the app shows the **Animation** tab (slide transitions, slideshow) when one is opened. The files
  were rebuilt, so `bytes` and `sha256` in `catalog.json` changed. Nothing else changed.

## 2026-11-27 · Product Launch presentation

- **New presentation `product-launch`** (8 slides, 1920x1080, saved as a presentation so the Animation tab shows): title,
  agenda, big statement, three feature cards, four numbers, photo + text, roadmap, thank you. Dark with cyan / violet
  accents; two public-domain photos (motherboard, Crab Nebula) credited in its catalog entry. About 4 MB.
- Made by `tools/make_templates` (`designs/product_launch/`, one small file per slide). No animations are set yet.

## 2026-11-27 · Photo thumbnails

- **7 new photo-based YouTube thumbnails (1280x720):** space-gamer, tech-review-pro, burger-challenge, hidden-lake-vlog,
  summer-vibes, match-day-live, pizza-taste-test. Real photos with dark overlays, big outlined titles with shadows,
  labels, badges and arrows.
- **Photos are public domain or CC0** from Wikimedia Commons (NASA/ESA, Pixel.la, Len Rizzi, Kurt Kaiser and others).
  The source, author and licence of each are in the `credits` list of its entry in `catalog.json`, and in
  `tools/make_templates/assets/credits.json`. The photo is baked into the layer, so each file is about 1.1 to 1.7 MB.
- **Tool:** `make_templates` can now place photos, see-through gradient overlays, glow, vignette, arrows and text
  shadows. Photos are fetched with `python fetch_assets.py` (not stored in Git).

## 2026-11-27 · YouTube thumbnails and the template maker

- **7 new YouTube thumbnail templates (1280x720):** gaming-channel, tech-review, daily-vlog, how-to-tutorial,
  travel-diary, easy-recipe, match-highlights. All shapes and text stay editable. Nothing else changed.
- **New tool `tools/make_templates/`** (Python): makes `template.fe` files from small design scripts, then runs the app's
  `build_templates` tool for the pictures and catalog sizes. See its README. The first template (gaming-channel) was drawn
  by hand in the app; the tool reproduces it to within 1 pixel, so the file layout is the same.

## 2026-11-27 · Smaller files, `.fe`, and a page preview

- **File name is now `.fe`.** Every template is `template.fe` (was `template.flash`). The app no longer opens `.flash`.
- **About 9 times smaller.** The 9 templates went from 12.6 MB to 1.4 MB (the whole repo folder from 17 MB to 2.9 MB). A
  `.fe` file stores each layer as only the part that has paint on it, as lossless WebP (no quality loss), instead of a
  picture the size of the whole page.
  - art-exhibition 690 KB to 84 KB, back-to-school 1.56 MB to 177 KB, mega-sale 782 KB to 126 KB,
    new-year-party 2.2 MB to 143 KB, summer-music-festival 921 KB to 124 KB, business-pitch 1.47 MB to 217 KB,
    school-project 1.45 MB to 235 KB, classic-resume 1.57 MB to 150 KB, modern-resume 2.44 MB to 166 KB.
- **New: `page-N.jpg`.** Every template folder now has a picture of every page (`page-1.jpg`, `page-2.jpg`...), up to 960 px,
  for the preview window in the app. A template with more than one page opens that window when clicked (big page, arrows,
  a strip of all pages, "Use template"), like Canva. `thumb.jpg` (the card picture, 480 px) is made again from page 1.
- **`catalog.json` version 2.** `bytes`, `sha256`, `pages`, `width` and `height` were rebuilt from the new files.
- Files are made by the tool `build_templates` in the Flash Editor project, not by hand:
  `cargo run -p fe-app --release --example build_templates -- "<this folder>"`.
- Old versions of the big `.flash` files are still in the Git history.
