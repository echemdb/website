# {{ title }}

{{ intro }}

{% for group in groups %}
{% if group.title %}

## {{ group.title }}

{% endif %}
{% for section in group.sections %}
{% if section.references %}

{{ "###" if group.title else "##" }} {{ section.title }}

{{ render("components/best_practices_table.md", references=section.references) }}

{% endif %}
{% endfor %}
{% endfor %}
