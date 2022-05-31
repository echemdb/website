# Cyclic Voltammograms
{% if cv_tag == 'aqueous COOR' %}
Cyclic voltammograms recorded in CO containing aqueous electrolytes.
{% elif cv_tag == 'ionic liquid BCV' %}
Cyclic voltammograms recorded in ionic liquids.
{% else %}
{% endif %}

Click a graph for more details.

{% for material in database.materials() %}

## {{ material }}

{{ render("components/cv_overview_table.md", entries_path=entries_path, database=database.filter(material_filter(material))) }}

{% endfor %}
