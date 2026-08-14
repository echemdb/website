| Title {: .echemdb-expand-column } | Year | Reference |
| ----- | ---- | --------- |
{% for reference in references %}
| {{ reference.title }} | {{ reference.year }} | {% if reference.url %}[{{ reference.authors }}]({{ reference.url }}){% else %}{{ reference.authors }}{% endif %} |
{% endfor %}
