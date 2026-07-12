# echemdb/website — Project Guide

## Project Overview

This is the **echemdb website generator** — a static site built with MkDocs that displays standardized electrochemistry data (cyclic voltammograms) from the [electrochemistry-data](https://github.com/echemdb/electrochemistry-data) repository. The project promotes FAIR (Findable, Accessible, Interoperable, Reusable) principles for experimental electrochemistry research data.

The site is live at [echemdb.org](https://www.echemdb.org/).

## Tech Stack

- **Static site generator**: MkDocs with Material theme
- **Language**: Python 3.10+
- **Package manager**: Pixi (conda-based)
- **Data library**: `unitpackage` — datapackage structures for electrochemistry
- **Templating**: Jinja2 (via mkdocs-macros-plugin and mkdocs-gen-files)
- **Plotting**: Plotly (interactive CV plots)
- **Math rendering**: KaTeX (frontend)
- **License**: GPLv3

## Project Structure

```
website/                  # Main Python package
├── filters/              # Custom Jinja filters (render, unicode, b64encode)
├── generator/            # Dynamic page generation from electrochemistry database
│   ├── __main__.py       # Entry point for mkdocs-gen-files; generates CV pages
│   └── database.py       # Loads remote CV database (cached singleton)
└── macros/               # Custom Jinja macros (render)

pages/                    # Static markdown pages (site source)
├── index.md              # Homepage
├── about.md              # About page
├── NAVIGATION.md         # Site navigation structure
└── cv/                   # CV section landing page

templates/                # Jinja2 templates for rendering data
├── components/           # Reusable snippets (quantity, electrolyte, cv_overview_table)
└── pages/                # Full page templates (cv_entry, cv overview)

util/                     # Shell scripts for literature PDF management (rclone)
```

## Build & Development

```bash
pixi install              # Set up environment
pixi run preview          # Local dev server with hot reload (mkdocs serve)
pixi run doc              # Build static site (mkdocs build)
pixi run doctest          # Run pytest on doctests
pixi run lint             # Run pylint, black, isort checks
pixi run black            # Auto-format code
pixi run isort            # Sort imports
```

Output goes to `generated/website/`.

## How the Build Works

1. MkDocs reads `pages/` and `mkdocs.yml`
2. The `mkdocs-gen-files` plugin runs `website/generator/__main__.py`
3. That script loads the CV database from a remote ZIP (version pinned in `database.py`)
4. Individual entry pages (`cv/entries/*.md`) and overview pages (aqueous, ionic_liquid, COOR) are generated
5. Jinja templates + custom filters/macros render data into markdown
6. MkDocs Material theme + KaTeX produce the final static HTML

## Key Architecture Patterns

- **Database singleton**: `website.generator.database.cv` is loaded once from remote and reused across all page generation. The URL can be overridden via `ECHEMDB_DATABASE_URL` env var.
- **Template isolation**: The `render()` function creates a fresh Jinja environment per call to avoid state leaks.
- **Filter pipeline**: Jinja filters (`| render(template)`, `| render_plot`, `| unicode`, `| b64encode`) transform data for display.
- **Data filtering**: Entries are filtered by `electrolyte.type` (aqueous/ionic liquid) and `experimental.tags` (BCV, COOR, HER), grouped by electrode material.
- **Generated pages**: Use `mkdocs_gen_files.editor` to write into a virtual filesystem that MkDocs treats as real files.

## Coding Conventions

- GPLv3 license headers on all Python files
- Black formatting, isort import ordering (enforced via `pixi run lint`)
- Extensive doctests in docstrings (tested via `pixi run doctest`)
- No heavy type annotation usage; duck typing preferred
- CSS classes use `.echemdb-*` prefix for custom styling

## Key Dependencies

- `unitpackage >=0.12.0, <0.13.0` — core data structures
- `astropy` — physical units
- `plotly >=5, <6` — interactive plots
- `pylatexenc` — LaTeX to unicode conversion
- `mkdocs-macros-plugin`, `mkdocs-gen-files`, `mkdocs-literate-nav` — MkDocs plugins

## URL Patterns

- CV entries: `/cv/entries/{identifier}.md`
- Overview pages: `/cv/aqueous.md`, `/cv/aqueous/COOR.md`, `/cv/ionic_liquid.md`
- Navigation defined in `pages/NAVIGATION.md`
