# Cyclic Voltammograms

This Section shows the content of the [electrochemistry-data](https://github.com/echemdb/electrochemistry-data)
repository, containing cyclic voltammograms (CVs[^1]) for single crystal electrodes (using dataset version {{ ECHEMDB_DATABASE_VERSION }}).

The CVs are sorted based on categories relevant to certain communities
such as the type of electrolyte, i.e., aqueous or non-aqueous,
as well as tags used for categorizing the systems.

## Database Access

The data shown on this website can either be downloaded directly as a ZIP from <a href="https://doi.org/10.5281/zenodo.20723429"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.20723429.svg" alt="DOI"></a> or the
release section of the [electrochemistry-data](https://github.com/echemdb/electrochemistry-data) repository.

Alternatively, the dataset can be downloaded using the [unitpackage API](https://echemdb.github.io/unitpackage/usage/echemdb_usage.html).
The API also allows browsing, filtering and manipulating the database, which is described in detail in the API documentation.

Example usage to download the database using the API:

```python
from unitpackage.database.echemdb import Echemdb

db = Echemdb.from_remote(version="{{ ECHEMDB_DATABASE_VERSION }}")
db.describe()
```

## Systems

* **[Aqueous](aqueous.md)**: Aqueous systems use water as a solvent, which is mixed with ions from an acid, a base, a salt, or a combination of such chemicals.
Other chemicals or gases can be added.
* **Non aqueous**: The ion conducting electrolyte can be a solid or a liquid.
In the case of a liquid, the solvent is either conductive itself,
as in **[Ionic Liquids](ionic_liquid.md)**, or it consists of a non-conductive solvent mixed with a salt.

## Tags

We use common tags used by the community or new (or less known) ones
for the purpose of categorizing the systems.
An entry can have several tags.

Currently available tags are:

* **BCV**: We consider a "base cyclic voltammogram" as a CV that shows no electrocatalysis except possibly the decomposition of the electrolyte.
* **SHA**: Specific Halide Adsorption, studied in electrolytes containing at least one halide component.
* **COOR**: CO Oxidation Reaction, usually studied in a CO saturated electrolyte.
* **FAOR**: Formic Acid Oxidation Reaction, usually studied in a formic acid containing electrolyte.
* **HER**: Hydrogen Evolution Reaction.


[^1]:
    Note that in the literature the abbreviation CV is sometimes
    used for the technique cyclic voltammetry.
