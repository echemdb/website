# {{ entry.identifier }}

A cyclic voltammogram for
{{ entry.get_electrode('WE').material }}({{ entry.get_electrode('WE').crystallographicOrientation }})
from Figure {{ entry.source.figure }} in

{{ entry.citation('text') }}

{{ entry.source.url }}

The data was curated by echemdb and is displayed at
https://www.echemdb.org/cv/entries/{{ entry.identifier }}/

## Content

This archive contains a [frictionless Data Package](https://specs.frictionlessdata.io/data-package/):

* `{{ entry.identifier }}.csv`: the digitized data.
* `{{ entry.identifier }}.json`: the description of the data, i.e., the units of the columns and the metadata of the entry.
* `LICENSE.md`: the terms under which the data can be used.

The data is taken from release {{ version }} of the
[electrochemistry-data](https://github.com/echemdb/electrochemistry-data) repository.

## Usage

The Data Package can be loaded with [unitpackage](https://echemdb.github.io/unitpackage/):

```python
from unitpackage.entry import Entry

entry = Entry.from_local("{{ entry.identifier }}.json")
entry.df
```

## Citation

When using this data, please cite the original publication:

```bibtex
{{ entry.bibliography.to_string('bibtex') }}
```
