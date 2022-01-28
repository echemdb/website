{% set plus = joiner(" + ") %}
{% for component in value.components
 | selectattr("type", "in", ["acid", "base", "alkaline", "salt"]) %}
  {{- plus() -}}
  {% if component.concentration is defined and component.concentration.value -%}
    {{ component.concentration | render }} {{ component.name }}
  {%- else -%}
    {{ component.name }}
  {%- endif %}
{% endfor %}
