{% if value.quantity.unit.is_equivalent('mol / m^3') -%}
  $\mathsf{ {{ '{0:.3g}'.format(value.quantity.to('mol / l').value|float) }} \; M }$
{%- else -%}
  $\mathsf{ {{ value.quantity.value }} \; {{ value.quantity.unit.to_string(format="latex_inline").replace("\\mathrm", "")[2:-2] }} }$
{%- endif %}
