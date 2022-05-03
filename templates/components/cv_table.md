
## {{ material }}

| material | orientation | components | identifier | year | reference |
| -------- | ----------- | ---------- | ---------- | ---- | --------- |
{% for entry in database %}
| {{material }}| ({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) | {{ entry.system.electrolyte | render("components/electrolyte.md") }} | [{{ entry.identifier }}](entries/{{ entry.identifier }}) | {{ database.bibliography.entries[entry.source.citation_key].fields['year'] }} | [:link:]({{ entry.source.url }}) |  
{% endfor %}
  
