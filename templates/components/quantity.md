{% if value.quantity.unit.is_equivalent('mol / m^3') -%}
  ${{ '{0:.3g}'.format(value.quantity.to('mol / l').value|float) }} \; \mathrm{M}$
{%- else -%}
  {{ value.quantity.to_string(format="latex_inline") }}
{%- endif %}
