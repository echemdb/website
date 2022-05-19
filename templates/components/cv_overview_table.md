| Entry | Substrate | Electrolyte | year | Reference |
| ----- | --------- | ----------- | ---- | --------- |
{% for entry in database %}
| [![{{ entry.identifier}}](data:image/png;base64,{{ entry.thumbnail(width=0.8, height=0.4) | b64encode }})](entries/{{ entry.identifier }}) | {{ material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) | {{ entry.system.electrolyte | render("components/electrolyte.md") }} | {{ database.bibliography.entries[entry.source.citation_key].fields['year'] }} | [ {{ entry.bibliography.persons['author'][0].last_names[0] | unicode }} ***et. al.*** Fig. {{ entry.source.figure }} ({{ entry.source.curve }})]({{ entry.source.url }}) |
{% endfor %}
