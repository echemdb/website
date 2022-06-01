# {{ entry.system.electrodes.working_electrode.material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) <small>- {{ entry.system.electrolyte | render("components/electrolyte.md") }}</small>
<small>echemdb identifier: `{{ entry.identifier }}`</small>  
<small>tags:
{% set separator = joiner(", ") %}
{% for tag in entry.experimental.tags %}
    {{- separator() -}}
    {{ tag }}
{% endfor %}
</small>

A cyclic voltammogramm for 
{{ entry.system.electrodes.working_electrode.material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) 
recorded in 
{% if 'COOR' in entry.experimental.tags %}
CO containing 
{% endif %}
{{ entry.system.electrolyte | render("components/electrolyte.md") }}
at a scan rate of 
{{ entry.figure_description.scan_rate | render }}
from Figure 
{{ entry.source.figure }} 
in 
[{{ entry.citation('md') }}]({{ entry.source.url }}).

<!-- TODO: It would be great if we could toggle between SI and original units. See #104. -->
<!-- TODO: Format plots. See #104. -->
{{ entry.rescale('original').plot()._repr_html_() }}


<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #104. 
[Download datapackage with ID-XXXXXXXX](#TODO)
-->

## Further information
The figure shows {{ entry.figure_description.type }} data.

{% if entry.system.electrodes.working_electrode.preparation_procedure is defined %}
The {{ entry.system.electrodes.working_electrode.material }}({{ entry.system.electrodes.working_electrode.crystallographic_orientation }}) electrode was prepared by:  
{{ entry.system.electrodes.working_electrode.preparation_procedure }}
{% else %}
Preparation procedure not available.
{% endif %}

{% if entry.figure_description.comment %}
**Comment left by the curator on the published figure**  
{{ entry.figure_description.comment }}
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
{{ entry.figure_description.yaml }}
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
