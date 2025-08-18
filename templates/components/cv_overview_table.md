|       | Substrate | Electrolyte {: .echemdb-expand-column } | Year {: .echemdb-hide-mobile } | Reference {: .echemdb-hide-mobile } |
| ----- | --------- | ----------- | ---- | --------- |
{% for entry in database %}
| [![{{ entry.identifier}}](data:image/png;base64,{{ entry.thumbnail(96, 72) | b64encode }}){: .echemdb-cv-thumbnail }](/cv/entries/{{ entry.identifier }}) {: .echemdb-middle-cell } | {{ material }}({{ entry.get_electrode('WE').crystallographicOrientation }}) {: .echemdb-middle-cell } | {{ entry.system.electrolyte | render("components/electrolyte.md") }} {: .echemdb-middle-cell } | {{ database.bibliography.entries[entry.source.citationKey].fields['year'] }} {: .echemdb-hide-mobile .echemdb-middle-cell } | [ {{ entry.bibliography.persons['author'][0].last_names[0] | unicode }} ***et. al.*** Fig. {{ entry.source.figure }} ({{ entry.source.curve }})]({{ entry.source.url }}) {: .echemdb-hide-mobile .echemdb-middle-cell } |
{% endfor %}
