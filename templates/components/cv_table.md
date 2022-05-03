##  {{ material }}
| identifier |
| ---------- |
{% for entry in database %}
| [{{ entry.identifier }}](entries/{{ entry.identifier }}) |
{% endfor %}