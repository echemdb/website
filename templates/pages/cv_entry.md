# {{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) <small>- {{ entry.electrochemical_system.electrolyte | render("components/electrolyte.md") }}</small>
<small>echemdb identifier: `{{ entry.identifier }}`</small>  

A cyclic voltammogramm for 
{{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) 
recorded in 
{{ entry.electrochemical_system.electrolyte | render("components/electrolyte.md") }}
at a scan rate of 
{{ entry.figure_description.scan_rate | render }}
from Figure 
{{ entry.source.figure }} 
in 
[{{ entry.citation('md') }}]({{ entry.source.url }}).

<!-- TODO: It would be great if we could toggle between SI and original units. See #104. -->
<!-- TODO: Format plots. See #104. -->
{{ entry.plot(xunit='original', yunit='original')._repr_html_() }}


<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #104. 
[Download datapackage with ID-XXXXXXXX](#TODO)
-->

## Further information
The figure shows {{ entry.figure_description.type }} data.

{% if entry.electrochemical_system.electrodes.working_electrode.preparation_procedure is defined %}
**Preparation procedure**  
The {{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) electrode was prepared by:  
{{ entry.electrochemical_system.electrodes.working_electrode.preparation_procedure }}
{% else %}
Preparation procedure not available.
{% endif %}

{% if entry.figure_description.comment %}
**Comment left by the curator on the published figure**  
Note from the curator: {{ entry.figure_description.comment }}
{% endif %}

## Metadata
Details on the electrochemical system:
<details>
<summary>Click to expand (yaml)</summary>

```yaml
{{ entry.electrochemical_system.yaml }}
```
</details>

Bibtex citation key:
<details>
<summary>Click to expand (bibtex)</summary>

```bibtex
{{ entry.bibliography.to_string('bibtex') }}
```
</details>

Details about the original figure in the publicaton:
<details>
<summary>Click to expand (yaml).</summary>

```yaml
{{ entry.figure_description.yaml }}
```
</details>

Details about the curators of this entry:
<details>
<summary>Click to expand (yaml).</summary>

```yaml
{{ entry.curator.yaml }}
```
</details>

----

<!-- TODO: Insert links to other data which are plotted in the same figure and/or even add a plot with all data from that figure. See #104 -->
