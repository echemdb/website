# About the project

The echemdb projects aim at standardizing experimental and theoretical 3D or time series data
according to the [FAIR principles](https://www.go-fair.org/fair-principles/).
Ultimately, this approach allows for a seamless comparison of published data
with laboratory-derived data and theoretical models.

The tools are developed focusing on electrochemical data.
The key issues for compliance with the FAIR principles for these data
are (i) metadata standards and (ii) accessibility to published data
which are often not machine-readable. More specifically, research data often stored as CSV
usually do not contain information on the units of the axis/columns or contain metadata annotating
and describing the data.

To solve these issues, in a first step the authors of echemdb limit themselves to a popular research
field of electrochemistry. In recent decades, the study
of the electrochemical properties of well-defined single crystal electrodes by
cyclic voltammetry has played a crucial role in the fundamental understanding of more
complex three dimensional systems found in more applied research areas or even in application.
These materials are very well defined and the measurement principle is also well established
within the community.

## Standardization

To standardize CVS data the authors of echemdb adopt
the [frictionless datapackage](https://specs.frictionlessdata.io/data-package/#introduction)
structure.
According to frictionless a data package consists of:

> * Metadata that describes the structure and contents of the package
> * Resources such as data files that form the contents of the package
>
> The Data Package metadata is stored in a “descriptor”.

The frictionless resource descriptors are enhanced by

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
A [Python API](https://echemdb.github.io/unitpackage/) provides direct access
to the entries of such a collection, enabling more specific filtering,
and enabling seamless integration into existing workflows.

## Reusability

In order to improve the reusability of published data, the authors of echemdb created
[svgdigitizer](https://echemdb.github.io/svgdigitizer/), a tool allowing for
digitizing any kind of published 2D plots from carefully prepared SVG files.
This approach has some superior functionalities compared to other tools, for example,
allowing to extract units from the axis labels or reconstructing a time axis based on a given scan rate.
Modules for specific types of plots, such as the [electrochemistry module](https://echemdb.github.io/svgdigitizer/workflow.html)
offers convenience functionality, and allow extracting additional properties such as the reference potential of a potential axis.
By providing a set of metadata, the digitized data can directly be stored as a [unitpackage](https://echemdb.github.io/unitpackage/).

## Contribute

Contributions are always welcome and do not necessarily require programming skills.
Please [leave us a message](https://github.com/orgs/echemdb/discussions)
if you are interested in contributing to the echemdb.

You could get started by [digitizing some published data](https://echemdb.github.io/svgdigitizer/workflow.html)
in your area of research or by extending any of the pages of the [echemdb website](https://echemdb.github.io/website/).
If your interest is outside of cyclic voltammograms or electrochemistry,
we would also be thrilled to hear about your ideas to extend these projects to other areas.

## What's next

The collection of metadata for a single measurement in the laboratory is often a tedious task.
We are currently [developing a tool](https://github.com/echemdb/autotag-metadata)
that stores a predefined set of metadata along with the measurement data.
Furthermore we develop file converters for electrochemical data,
which in combination with the metadata files produce a [unitpackage](https://echemdb.github.io/unitpackage/).

## Contact

The authors of echemdb are from the fields of experimental and theoretical physical chemistry,
as well as from computer science and mathematics.

Ideas and suggestions, tell us more on our [discussion board](https://github.com/orgs/echemdb/discussions).

Reach individual contributors on the [GitHub organization](https://github.com/echemdb).

Discuss and stay up to date on [echemdb.zulipchat.com](https://echemdb.zulipchat.com).
