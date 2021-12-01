{% if quantity.unit == "K" and 250 <= quantity.value <= 400 %}
  {{- quantity.value - 273.15 }} °C
{%- else %}
  {{- quantity.value }} {{ quantity.unit.to_string("latex_inline") -}}
{% endif %}
