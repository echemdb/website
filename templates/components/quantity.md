{% if value.quantity.unit.is_equivalent('mol / m^3') %}
  {{- '{0:.3g}'.format(value.quantity.to('mol / l').value|float) }} M
{%- else %}
  $`\mathsf{ {{- value.quantity.value }} \, {{ value.quantity.unit.to_string("latex_inline").replace("mathrm", "mathsf")[1:-1] -}}}`$
{% endif %}
