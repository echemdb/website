# About the project

The echemdb projects aim at standardizing experimental and theoretical 2D or time series data
according to the [FAIR principles](https://www.go-fair.org/fair-principles/).
Ultimately, this approach allows for a seamless comparison of published data
with laboratory-derived data and theoretical models.

Key issues for compliance with the FAIR principles are that many research areas lack
(i) metadata standards and (ii) published data is mostly inaccessible or not machine-readable.
More specifically, research data often stored as CSV usually do not contain information
on the units of the axis/columns or contain metadata annotating and describing the data.

To solve these issues, in a first step the authors of echemdb limit their approach
to a popular research field of interfacial electrochemistry.
In recent decades, the study of the electrochemical properties of
well-defined single crystal electrodes by cyclic voltammetry has played a crucial role
in the fundamental understanding of more complex three dimensional systems
found in more applied research areas or even in application.
These materials are very well defined and the measurement principle is also well established
within the community.

## Standardization

The data standardization approach is described in [Engstfeld et al., *Data Science Journal*, **24** (2025) 13](https://datascience.codata.org/articles/10.5334/dsj-2025-013).

In brief, to standardize CSV data the authors of echemdb adopt the
[frictionless datapackage](https://specs.frictionlessdata.io/data-package/#introduction)
structure.
According to frictionless a data package consists of:

> * Metadata that describes the structure and contents of the package
> * Resources such as data files that form the contents of the package
>
> The Data Package metadata is stored in a “descriptor”.

The echemdb authors augmented the frictionless schema, by adding

* units, allowing for simple unit transformations or data manipulation.
* metadata describing a resource within the package.

The metadata describes for example the [electrochemical system](https://github.com/echemdb/metadata-schema/blob/main/examples/objects/system.yaml),
which contains detailed information about the electrodes
or the components of the electrolyte. The metadata also contains information
on the curation process, i.e., who was the experimentalist,
a URL to an entry in an electronic laboratory notebook (ELN), or details on the experimental set-up.
The [JSON metadata schema](https://github.com/echemdb/metadata-schema) is developed
as a separate project.

By following this approach, a set of datapackages forms a collection.
The entries of such a collection are displayed in different forms on this
website based on the available descriptors.
The [unitpackage](https://echemdb.github.io/unitpackage/) Python API provides direct access
to the entries of such a collection, enabling more specific filtering,
and enabling seamless integration into existing workflows, including locally stored data.

## Reusability

In order to improve the reusability of published data, the authors of echemdb created
[svgdigitizer](https://echemdb.github.io/svgdigitizer/), a tool allowing for
digitizing any kind of published 2D plots from carefully prepared SVG files.
This approach has some superior functionalities compared to other tools, for example,
allowing to extract units from the axis labels or reconstructing a time axis based on a given scan rate.
Modules for specific types of plots, such as the [electrochemistry module](https://echemdb.github.io/svgdigitizer/workflow.html)
offers convenience functionality, and allow extracting additional properties such as the reference potential of a potential axis.
By providing a set of metadata, the digitized data can directly be stored as a [unitpackage](https://echemdb.github.io/unitpackage/).

## What's next

We anticipate developing additional tools which help in generating [unitpackages](https://echemdb.github.io/unitpackage/)
or allow for interacting with unitpackages.
The latter comprises common tools for the evaluation of electrochemical data.
We also plan to include other electrochemical data from methods other than cyclic voltammetry in our database,
including data which have been recorded concomitantly, such as disc electrode currents
or mass spectrometry signals.

## Contact

The authors of echemdb are from the fields of experimental and theoretical physical chemistry,
as well as from computer science and mathematics.

Direct Contact:

* [Albert Engstfeld](mailto:albert.engstfeld@uni-ulm.de) (Institute of Electrochemistry, Ulm university, DE)
* [Nicolas Hoermann](mailto:hoermann@fhi-berlin.mpg.de) (Theory Department, Fritz-Haber Institute, Berlin (DE))

Ideas and suggestions, tell us more on our [discussion board](https://github.com/orgs/echemdb/discussions).

Reach individual contributors on the [GitHub organization](https://github.com/echemdb).

Discuss and stay up to date on [echemdb.zulipchat.com](https://echemdb.zulipchat.com).

## Funding, Support, & Related Projects

Most of the work has been supported by funding from the following institutions:

<div class="echemdb-logo-table" markdown>

| | |
|---|---|
| [Institute of Electrochemistry, Ulm University (GER)](https://www.uni-ulm.de/en/nawi/institute-of-electrochemistry/) | [![](images/logos/logo-uni-ulm.svg){width=200 .logo-bg}](https://www.uni-ulm.de/en/nawi/institute-of-electrochemistry/) |
| [Theory Department, Fritz-Haber Institute, Berlin (GER)](https://www.fhi.mpg.de/th-department) | [![](images/logos/logo_fhi.png){width=200 .logo-bg}](https://www.fhi.mpg.de/th-department) |
| [Department of Material Chemistry, National Institute of Chemistry, Ljubljana (SLO)](https://www.ki.si/en/departments/d10-department-of-materials-chemistry/) | [![](images/logos/Logo_national_institue_chemistry.png){width=200 .logo-bg}](https://www.ki.si/en/departments/d10-department-of-materials-chemistry/) |

</div>

The work is also supported by:

<div class="echemdb-logo-table" markdown>

| | |
|---|---|
| [CRC-1316](https://sfb1316.rub.de/index.php/en/) | [![](images/logos/logo-crc1316.jpg){width=250 .logo-bg}](https://sfb1316.rub.de/index.php/en/) |
| [NFDI4Chem](https://nfdi4chem.de/) | [![](images/logos/logo_nfdi4chem.svg){width=200 .logo-bg}](https://nfdi4chem.de/) |

</div>

## Cite

For the individual repositories, refer to the Zenodo DOIs provided in the repositories readme or documentation.

The general concept is described in [A.K. Engstfeld, J. M. Hermann, N. Hörmann, & J. Rüth, *Data Science Journal*, **24** (2025) 13](https://datascience.codata.org/articles/10.5334/dsj-2025-013).

The dataset itself can be cited according to the respective version on <a href="https://doi.org/10.5281/zenodo.20723429"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.20723429.svg" alt="DOI"></a>.
