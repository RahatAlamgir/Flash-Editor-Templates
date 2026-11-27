# Changelog

Changes to the template repository, newest first. (The app's own change log is in the Flash Editor project.)

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
