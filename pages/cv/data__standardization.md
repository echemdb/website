---
author: Nicolas G. Hoermann
title: echemdb - The community database for electrochemical data
---

# Standardized CV data

In general a CV is the measured current $j = -e \frac{ {\rm d} n_e}{ {\rm d} t}$ while cyclically scanning the potential $\Phi_E$. The current depends on the scan speed $v = \frac{ {\rm }d \Phi_E}{ {\rm d} t}$ as well as the active surface area (number of active surface sites). With

In table we analyse different possible normalization schemes:



Different conventional normalizations are possible

# Data Standardization

In our database we try to follow certain data standards, more or less closely.Some informative websites are listed at the bottom. For maximum compatibility and flexibility we follow the [Data Package](https://specs.frictionlessdata.io/data-package/ ) standard. The Data Package specification does NOT impose any requirements on their form or structure and can therefore be used for packaging any kind of data.


## Data Package
###Definitions

> *Data Package* consists of:
>
> - Metadata that describes the structure and contents of the Data Package
> - Resources such as data files that form the contents of the Data Package



> *Metadata*
>
> - stored in a "Descriptor".
> - Metadata Descriptor MUST be a valid JSON object.
> - MUST be named datapackage.json and it MUST be placed in the top-level directory (relative to any other resources provided as part of the Data Package)
> - MUST contain a resources property describing the data resources, in form of a list of resource descriptors
> - All other properties are considered metadata properties. The descriptor MAY contain any number of other metadata properties.


> *Resource*
>
> - Files bundled locally with the Metadata Descriptor
> - Remote resources, referenced by URL
> - "Inline" data, included directly in the Descriptor
> - The Data Resource Descriptor, that is listed in the Metadata Descriptor MUST be a valid JSON object.


###[Metadata](https://specs.frictionlessdata.io/data-package/#descriptor) example###

```python
jsondict = {
  "name" : "a-unique-human-readable-and-url-usable-identifier",
  "title" : "A nice title",
  "licenses" : [ ... ],
  "sources" : [...],
  # list of the data resources in this data package
  "resources": [...],
  # optionally other json key-value pairs
}
```

###[Data Resource](https://specs.frictionlessdata.io/data-resource/#descriptor) example###
1 resource with all required, recommended and optional properties
```python
[{
  "name": "example data",
  "path": "http://example.com/example.csv",
  "title": "Random data 0",
  "description": "My favourite random data about nothing.",
  "format": "csv",
  "mediatype": "text/csv",
  "encoding": "utf-8",
  "bytes": 1,
  "hash": "",
  "schema": "",
  "sources": "",
  "licenses": ""
}]
```









## Links
### General
- Research Data Management - Max Planck Digital Library (MPDL) - https://rdm.mpdl.mpg.de/

### Data Packages
- https://frictionlessdata.io/
- https://specs.frictionlessdata.io/
- https://specs.frictionlessdata.io/data-package/
- https://specs.frictionlessdata.io/data-resource/
- https://ckan.org/
- https://json-schema.org/understanding-json-schema/about.html#about
