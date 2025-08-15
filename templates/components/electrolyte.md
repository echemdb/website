{% set plus = joiner(" + ") %}
{% if value.type == 'ionic liquid' %}
{% set components = value.components | selectattr("type", "in", ["solvent", "acid", "base", "alkaline", "salt"]) %}
{% else %}
{% set components = value.components | selectattr("type", "in", ["acid", "base", "alkaline", "salt"]) %}
{% endif %}
{% for component in components %}
  {{- plus() -}}
  {% if component.concentration is defined and component.concentration.value -%}
    {{ component.concentration | render }} $\ce{ {{ component.name }} }$
  {%- else -%}
    $\ce{ {{ component.name }} }$
  {%- endif %}
{% endfor %}
