The [echemdb repository](https://github.com/echemdb/website) contains high
quality experimental and theoretical data on electrochemical systems. The
standardized and validated data displayed on the [projects
website](https://echemdb.github.io/website/) so far is from the community and
publications aiming at fullfilling the [FAIR
principles](https://www.go-fair.org/fair-principles/).

The repository can be browsed on [our
websites](https://echemdb.github.io/website/) or explored with a [Python
API](https://github.com/echemdb/echemdb).

# License

The contents of this repository are licensed under the [GNU General Public
License v3.0](./LICENSE) or, at your option, any later version.  The contents
of [data/](./data/) and [literature/](./literature/) are additionally licensed
under the [Creative Commons Attribution 4.0 International
License](https://creativecommons.org/licenses/by/4.0/).

# For developers

The build of the website can be tested locally with the following steps.

## Installation

Clone the repository

```sh
git clone git@github.com:echemdb/website.git
```

Install dependencies (mamba or conda)

```sh
mamba env create --file enviornment.yaml
mamba activate echemdb-website
pip install -e .
```

## Build website

```sh
mkdcos serve
```

The HTML files are generated in `generated/website`

Entries are created from datapackaes in `data/generated/svgdigitizer`. Follow the next section to create such data.

## Convert literature to datapackages

To digitize all data

```sh
cd data
make
```

To run the svgdigitizer in parallel on 8 cores, use instead

```sh
make -j8
```

We can also only digitize a single data set

```sh
make generated/svgdigitizer/mello_2018_understanding_J3045/mello_2018_understanding_J3045_p1_f1H_black.csv
```

To digitize data coming from a different source directory than
`literature/` use

```sh
make SOURCE_DIR=/another/path
```

## Code changes

If you make changes to the code test the modules with pylint, isort, and black.

```sh
pylint website
isort website
black website
```
