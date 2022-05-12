
## {{ material }}

| entry | material | components | year | reference |
| ----- | -------- | ---------- | ---- | --------- |
{% for entry in database %}
| [{{ entry.thumbnail(stream=True, html=True) }}](entries/{{ entry.identifier }}) | {{ material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) | {{ entry.system.electrolyte | render("components/electrolyte.md") }} | {{ database.bibliography.entries[entry.source.citation_key].fields['year'] }} | [:link:]({{ entry.source.url }}) |  
{% endfor %}
  
