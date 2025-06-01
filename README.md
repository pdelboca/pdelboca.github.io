# My Personal Website

This repository host the content and script to build my personal website: [pdelboca.me](https://pdelboca.me)

## Architecture

  - `static/` for CSS
  - `static/old-site` host my old website that I use to write using RMarkdown.
  - `content/` folder with Markdwon files stored in `YYYY/MM/DD` folder.
  - `template/` folder with a bunch of templates.
  - `docs/` folder to host the static site (for Github publishing)
  - `main.py` file to read the content using `markdown` library and render the website using `jinja2`.

## How to run

To generate the static site:
```bash
$ uv run main.py
```

To previsualize the content:
```bash
$ python -m http.server -d docs/
```
