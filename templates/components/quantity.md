{% if value.quantity.unit.is_equivalent('mol / m^3') %}
  {{- value.quantity.to('mol / l').value }} M
{%- else %}
  {{- value.quantity.value }} {{ value.quantity.unit.to_string("latex_inline") -}}
{% endif %}

