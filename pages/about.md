# About the project

echemdb aims at standardizing experimental and theoretical data on electrochemical systems
according to the [FAIR principles](https://www.go-fair.org/fair-principles/).
Ultimately, this approach allows for a seamless comparison of published data
with laboratory-derived data and theoretical models.

The key issues for compliance with the FAIR principles for electrochemical data
are (i) metadata standards and (ii) accessibility to published data
which are often not machine-readable.

To solve these issues, in a first step the authors of echemdb limit themselves to a popular research
field of electrochemistry. In recent decades, the study
of the electrochemical properties of well-defined single crystal electrodes by
cyclic voltammetry has played a crucial role in the fundamental understanding of more
complex three dimensional systems found in more applied research areas or even in application.

## Standardization

To standardize electrochemical data the authors of echemdb adopt
the [data package](https://specs.frictionlessdata.io/data-package/#introduction)
structure developed by [frictionless](https://frictionlessdata.io/).
According to frictionless a data package consists of:

> * Metadata that describes the structure and contents of the package
> * Resources such as data files that form the contents of the package
>
> The Data Package metadata is stored in a “descriptor”.

The metadata describe for example the [electrochemical system](https://github.com/echemdb/metadata-schema/blob/main/examples/system.yaml),
which contains detailed information about the electrodes
or the components of the electrolyte. The metadata also contains information
on the curation process, i.e., who was the experimentalist,
a URL to an entry in an electronic laboratory notebook (ELN), or details on the experimental set-up.
The [JSON metadata schema](https://github.com/echemdb/metadata-schema) is developed
as a separate project.

The frictionless resource descriptors are enhanced by units,
allowing for simple unit transformations or data manipulation.

By following this approach, a set of data packages forms a database.
The entries of such a database are displayed in different forms on this
website based on the available descriptors.
A [Python API](https://echemdb.github.io/echemdb/) provides direct access
to the entries of such a database, enabling more specific filtering,
and enabling seamless integration into existing workflows.

## Reusability

In order to improve the reusability of published data, the authors of echemdb created
[svgdigitizer](https://echemdb.github.io/svgdigitizer/), a tool allowing for
digitizing any kind of published 2D plots from carefully prepared SVG files.
An [electrochemistry module](https://echemdb.github.io/svgdigitizer/workflow.html)
offers convenience functionality, e.g., to reconstruct a time
axis based on the scan rate, extract axis units, or reference potentials.
By providing a set of metadata, the digitized data can directly be stored as an echemdb data package.

## Contribute

Contributions are always welcome and do not necessarily require programming skills.
Please leave us a message if you are interested in contributing to the echemdb.

You could get started by [digitizing some published data](https://echemdb.github.io/svgdigitizer/workflow.html)
in your area of research or by extending any of the pages of the [echemDB website](https://echemdb.github.io/website/).
If your interest is outside of cyclic voltammograms or electrochemistry,
we would also be thrilled to hear about your ideas to extend these projects to other areas.

## What's next

The collection of metadata for a single measurement in the laboratory is often a tedious task.
We are currently developing a tool that stores a predefined set of metadata along with the measurement data.
Furthermore we develop file converters for electrochemical data,
which in combination with the metadata files produce an echemdb data package.

## Contact

E-mail: contact@echemdb.org

To reach individual contributors visit our [GitHub organization](https://github.com/echemdb).