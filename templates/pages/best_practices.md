# {{ title }}

{{ intro }}

{% for section in sections %}
{% if section.references %}

## {{ section.title }}

{{ render("components/best_practices_table.md", references=section.references) }}

{% endif %}
{% endfor %}

{{ outro }}
