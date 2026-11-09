# CV Dataset

This Section shows the content of the [electrochemistry-data](https://github.com/echemdb/electrochemistry-data)
repository, containing cyclic voltammograms (CVs[^1]) for single crystal electrodes (using dataset version {{ ECHEMDB_DATABASE_VERSION }}).
The dataset currently contains {{ ECHEMDB_ENTRY_COUNT }} entries from {{ ECHEMDB_SOURCE_COUNT }} literature sources.

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

Each entry can be downloaded individually as a ZIP from the Download section at the bottom of its entry page.

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

* **BCV**: We consider a "base cyclic voltammogram" as a CV that shows no electrocatalytic processes except possible currents related to the decomposition of the electrolyte.
* **SHA**: Specific Halide Adsorption, studied in electrolytes containing at least one halide component. The tag is not common in the literature, but used here to simply differentiate between certain systems.
* **COOR**: CO Oxidation Reaction, usually studied in a CO saturated electrolyte.
* **FAOR**: Formic Acid Oxidation Reaction, usually studied in a formic acid containing electrolyte.
* **HER**: Hydrogen Evolution Reaction.
* **ORR**: Oxygen Reduction Reaction.

## Notes and Limitations

Please keep the following in mind when using the dataset.

* **Data are reproduced as published.** The CVs are digitized from figures in the original publications. Their precision is limited by the resolution and quality of the published figures.
* **Only metadata provided in the publication are included.** This limits for example conversion between RHE/SHE scales, if a pH is not explicitly mentioned, or the conversion between $I$ and $j$ if the electrode surface area is not provided.
* **Curation errors can be fixed.** If you find an error introduced during curation, such as wrong metadata or a digitization error, please report it on the [issue board](https://github.com/echemdb/electrochemistry-data/issues) of the electrochemistry-data repository.
* **Errors in the original publications cannot be fixed.** Known problems with a published figure, such as wrong axis labels or inconsistent units, are kept as published and are described in the curator's comment on the respective entry page.

## Contribute

The dataset is not exhaustive and many more CVs of the listed systems exist in the literature.
Contributions are welcome and do not require programming skills:

* **Digitize figures** from publications with [svgdigitizer](https://echemdb.github.io/svgdigitizer/).
* **Provide source data** behind a published figure that you measured yourself, for example, as CSV files.
* **Check existing entries** against their publications and correct errors.

The [contributing guide](https://github.com/echemdb/electrochemistry-data/blob/main/CONTRIBUTING.md)
of the electrochemistry-data repository describes each of these routes step by step.
If you prefer to send data without using Git, or want to discuss a contribution first,
see the contact options on the [Contribute](../contribute.md#contact) page.

[^1]:
    Note that in the literature the abbreviation CV is sometimes
    used for the technique cyclic voltammetry.
