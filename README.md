This projects builds a website from the [eletrochemistry-data
repository](https://github.com/echemdb/electrochemistry-data) which contains
high quality experimental and theoretical data on electrochemical systems. The
standardized and validated data displayed on the [projects
website](https://www.echemdb.org/) so far is from the community and
publications aiming at fullfilling the [FAIR
principles](https://www.go-fair.org/fair-principles/).

The repository can be browsed on [our
websites](https://www.echemdb.org/) or explored with a [Python
API](https://github.com/echemdb/unitpackage).

# For developers

Install [pixi](https://pixi.sh) and clone this repository

```sh
git clone git@github.com:echemdb/website.git
```

To preview the website run

```sh
cd website
pixi run preview
```

If you make changes to the code test the modules with

```sh
pixi run doctest
pixi run lint
```

# License

The contents of this repository are licensed under the [GNU General Public
License v3.0](./LICENSE) or, at your option, any later version.  The contents
of [data/](./data/) and [literature/](./literature/) are additionally licensed
under the [Creative Commons Attribution 4.0 International
License](https://creativecommons.org/licenses/by/4.0/).
