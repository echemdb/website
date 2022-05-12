{% for material in database.materials() %}

## {{ material }}

| Entry | Substrate | Electrolyte | year | Reference |
| ----- | --------- | ----------- | ---- | --------- |
{% for entry in database %}
{%- if entry.system.electrodes.working_electrode.material == material -%}
| [{{ entry.thumbnail(stream=True, html=True, width=0.8, height=0.4, linewidth=1, color='b') }}](entries/{{ entry.identifier }}) | {{ material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) | {{ entry.system.electrolyte | render("components/electrolyte.md") }} | {{ database.bibliography.entries[entry.source.citation_key].fields['year'] }} | [ {{ entry.bibliography.persons['author'][0].last_names[0] }} ***et. al.*** Fig. {{ entry.source.figure }} ({{ entry.source.curve }})]({{ entry.source.url }}) |
{% endif -%} 
{% endfor %}
{% endfor %}
