This repository contains the source of the website
[echemdb.org](https://www.echemdb.org/), a community project for interfacial
electrochemistry and local research data management following the [FAIR
principles](https://www.go-fair.org/fair-principles/). The website

* displays the standardized and validated cyclic voltammograms from the
  [electrochemistry-data repository](https://github.com/echemdb/electrochemistry-data),
  which were collected from published works by the community,
* provides a curated collection of [resources](https://www.echemdb.org/resources/),
  i.e., open-source software tools, knowledge bases, and a reference table of
  best-practice literature (maintained in [data/best_practices/](./data/best_practices/)), and
* introduces the tools of the echemdb ecosystem, such as the
  [unitpackage](https://github.com/echemdb/unitpackage) Python API and the
  [svgdigitizer](https://github.com/echemdb/svgdigitizer).

# For developers

Install [pixi](https://pixi.sh) and clone this repository

```sh
git clone git@github.com:echemdb/website.git
```

To preview the website run

```sh
pixi run preview
```

For a fast preview during development run

```sh
pixi run preview-fast
```

which only includes a limited number of database entries per tag
(such as BCV or COOR) and electrolyte type (such as aqueous or ionic liquid),
so that all overview pages contain some entries.

If you make changes to the code test the modules with

```sh
pixi run doctest
pixi run lint
```

The version of the electrochemistry-data must be adapted in the [database generator](website/generator/database.py).

Every pull request should add a news entry in [news/](./news/), see [news/TEMPLATE.rst](./news/TEMPLATE.rst).

# License

The contents of this repository are licensed under the [GNU General Public
License v3.0](./LICENSE) or, at your option, any later version.  The contents
of [data/](./data/) and [literature/](./literature/) are additionally licensed
under the [Creative Commons Attribution 4.0 International
License](https://creativecommons.org/licenses/by/4.0/).
