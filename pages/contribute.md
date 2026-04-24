# Contribute

Contributions are always welcome and do not necessarily require programming skills and can involve

* Providing data to the database
* Digitize data for the database
* Develop metadata standards
* Improve the website content
* Develop data evaluation tools
* ...

Please [leave us a message](https://github.com/orgs/echemdb/discussions),
contact directly [albert.engstfeld@uni-ulm.de](mailto:albert.engstfeld@uni-ulm.de),
or suggest changes in the issue boards of the respective repositories.

We would also be thrilled to hear about your ideas to extend these projects to other areas.

## Contribute data

Data can be provided directly, for example, as csv file (source data)
or involves digitizing data from a publication.
In either case additional metadata and a PDF of the work should be provided (PDFs should not be uploaded in the repository).
Contributions can made via a pull request in the [electrochemistry dataa repository](https://github.com/echemdb/electrochemistry-data) or send via mail to a [albert.engstfeld@uni-ulm.de](mailto:albert.engstfeld@uni-ulm.de) to determine further steps.

### Source data

The data should be in a simple machine readable format, such as CSV, TSV, TXT, ... which contains columns with data. Header lines with additional metadata are acceptable. The data must contain a potential (E) or voltage (U) axis and a current (I) or current density (j) axis. A time (t) axis is preferable. If not present, the scan rate (V/s), must be provided in the metadata to reconstruct the time axis.

Metadata is preferably submitted as YAML. Templates can be found either in the [metadata-scheme repository](https://github.com/echemdb/metadata-schema/blob/main/examples/file_schemas/source_data.yaml) (remove all parts that are not necessary) or browse through existing schemas from [works that are already included in the database](https://github.com/echemdb/electrochemistry-data/tree/main/literature) (check the entries in the subfolders).

### Digitize data

To digitize data from published works, follow the instructions in the [svgdigitizer documentation](https://echemdb.github.io/svgdigitizer/workflow.html).
