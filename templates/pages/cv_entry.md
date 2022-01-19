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

<!-- TODO: It would be great if we could toggle between SI and original units. See #31. -->
<!-- TODO: Format plots. See #31. -->
{{ entry.plot(xunit='original', yunit='original')._repr_html_() }}

**Figure notes:**  
The figure shows {{ entry.figure_description.type }} data.
{% if entry.figure_description.comment %}
Note from the curator: {{ entry.figure_description.comment }}
{% endif %}
<details>
<summary>Click to expand complete figure metadata (yaml).</summary>

```yaml
{{ entry.figure_description.yaml }}
```
</details>

<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #31. 
[Download datapackage with ID-XXXXXXXX](#TODO)
-->

<!-- TODO: Style this section. See #31. -->
## Further information
**Preparation procedure**
{% if entry.electrochemical_system.electrodes.working_electrode.preparation_procedure is defined %}
The {{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) electrode was prepared by:  
{{ entry.electrochemical_system.electrodes.working_electrode.preparation_procedure }}
{% else %}
Preparation procedure not available.
{% endif %}

## Metadata
<details>
<summary>Click to expand metadata (yaml).</summary>

```yaml
{{ entry.electrochemical_system.yaml }}
```
</details>

## Bibliography
<details>
<summary>Bibliography (bibtex). Click to expand.</summary>

```bibtex
{{ entry.bibliography.to_string('bibtex') }}
```
</details>


----

<!-- TODO: Insert links to other data which are plotted in the same figure and/or even add a plot with all data from that figure. See #31 -->
