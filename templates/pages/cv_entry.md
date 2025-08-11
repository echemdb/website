# {{ entry.get_electrode('WE').material }}({{ entry.get_electrode('WE').crystallographicOrientation }}) <small>- {{ entry.system.electrolyte | render("components/electrolyte.md") }}</small>
<small>echemdb identifier: `{{ entry.identifier }}`</small><br>
<small>tags:
{% set separator = joiner(", ") %}
{% for tag in entry.experimental.tags %}
    {{- separator() -}}
    {{ tag }}
{% endfor %}
</small>

A cyclic voltammogramm for
{{ entry.get_electrode('WE').material }}({{ entry.get_electrode('WE').crystallographicOrientation }})
recorded in
{% if 'COOR' in entry.experimental.tags %}
CO containing
{% endif %}
{{ entry.system.electrolyte | render("components/electrolyte.md") }}
at a scan rate of
{{ entry.figureDescription.scanRate | render }}
from Figure
{{ entry.source.figure }}
in
[{{ entry.citation('md') }}]({{ entry.source.url }})

<!-- TODO: It would be great if we could toggle between SI and original units. See #104. -->
<!-- TODO: Format plots. See #104. -->
{{ entry.rescale('original').plot()._repr_html_() }}


<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #104.
[Download datapackage with ID-XXXXXXXX](#TODO)
-->

## Further information

The figure shows {{ entry.figureDescription.type }} data.

{% if entry.get_electrode('WE').preparationProcedure is defined %}
The {{ entry.get_electrode('WE').material }}({{ entry.get_electrode('WE').crystallographicOrientation }}) electrode was prepared by:<br>
{% for step in entry.get_electrode('WE').preparationProcedure.description %}
    * {{ step }}<br>
{% endfor %}
{% else %}
Preparation procedure not available.
{% endif %}

{% if entry.figureDescription.comment %}
**Comment left by the curator on the published figure**
{{ entry.figureDescription.comment }}
{% endif %}

## Metadata

<details>
<summary>Details on the electrochemical system (yaml)</summary>

```yaml
{{ entry.system.yaml }}
```
</details>

<details>
<summary>Citation key (bibtex)</summary>

```bibtex
{{ entry.bibliography.to_string('bibtex') }}
```
</details>


<details>
<summary>Details about the original figure in the publicaton (yaml).</summary>

```yaml
{{ entry.figureDescription.yaml }}
```
</details>

<details>
<summary>Details about the curation process of this entry (yaml).</summary>

```yaml
{{ entry.curation.yaml }}
```
</details>

----

<!-- TODO: Insert links to other data which are plotted in the same figure and/or even add a plot with all data from that figure. See #104 -->
