<!-- TODO: Create the small heading subtitle from metadata. See #31. -->
# {{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) <small>- 0.1 M CsF + 0.1 M HClO4</small>
<!-- TODO: Simplify the entry for electrode material, throughout the entire document: See #42. -->
<!-- TODO: Create text from metadata. See #31. -->
A cyclic voltammogramm for 
{{ entry.electrochemical_system.electrodes.working_electrode.material }}
({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) 
recorded in 
0.1 M CsF + 0.1 M HClO4 
at a scan rate of 
50 mV s$^{-1}$ <!-- TODO: Create nice representation of the scan rate unit from entry.figure_description.scan_rate_unit -->
from Figure 
{{entry.source.figure }} 
in 
[{{ entry.citation }}
](https://doi.org/{{ entry.source.doi }}).

<!-- TODO: Show plots with original axis units, see #25. It would be great if we could toggle between SI and original units. See #31. -->
<!-- TODO: Properly format plots. They should probably be much bigger since they are nice to look at. See #31. -->
{{ entry.plot()._repr_html_() }}

{{ entry.plot('A / m^2')._repr_html_() }}

**Figure notes:**  
The figure shows {{ entry.figure_description.type }} data.
{% if entry.figure_description.comment %}
Note from the curator: {{ entry.figure_description.comment }}
{% endif %}

<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #31. -->
[Download datapackage with ID-XXXXXXXX](#TODO)

<!-- TODO: Style this section. See #31. -->
## Further information
**Preparation procedure**
{% if entry.electrochemical_system.electrodes.working_electrode.preparation_procedure is defined %}
The {{ entry.electrochemical_system.electrodes.working_electrode.material }}({{ entry.electrochemical_system.electrodes.working_electrode.crystallographic_orientation }}) electrode was prepared by:  
{{ entry.electrochemical_system.electrodes.working_electrode.preparation_procedure }}
{% else %}
Preparation procedure not available.
{% endif %}

`Content from the yaml file`

<!-- TODO: Insert all the metadata from the .yaml file in some collapsible form here. E.g., just the YAML file with syntax highlighting. See #31. -->
## Metdata
<details>
<summary>Click to expand metadata (yaml).</summary>

```yaml
{{ entry.electrochemical_system.yaml }}
```
</details>

----

<!-- TODO: Insert links to other data which are plotted in the same figure and/or even add a plot with all data from that figure. See #31 -->
