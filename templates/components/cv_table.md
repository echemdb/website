
## {{ material }}

| Entry | Substrate | Electrolyte | year | Reference |
| ----- | --------- | ----------- | ---- | --------- |
{% for entry in database %}
| [{{ entry.thumbnail(stream=True, html=True, width=0.8, height=0.4) }}](entries/{{ entry.identifier }}) | {{ material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) | {{ entry.system.electrolyte | render("components/electrolyte.md") }} | {{ database.bibliography.entries[entry.source.citation_key].fields['year'] }} | [ {{ entry.bibliography.persons['author'][0].last_names[0] }} ***et. al.*** ]({{ entry.source.url }}) |  
{% endfor %}
  
