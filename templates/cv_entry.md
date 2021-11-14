<!-- TODO: Create the heading Pt(111) from metadata. See #31. -->
<!-- TODO: Create the small heading subtitle from metadata. See #31. -->
# Pt(111) <small>- 0.1 M CsF + 0.1 M HClO4</small>

<!-- TODO: Create text from metadata. See #31. -->
<!-- TODO: We should merge all our .bib files when building the pages and then create reference to original article from that .bib file. See #31. -->
A cyclic voltammogramm for Pt(111) recorded in 0.1 M CsF + 0.1 M HClO4 at a scan rate of 50 mV s$^{-1}$ from Figure 2a in [N. Author *et al.*, *Journal Name*, **Volume** (YEAR) Page, "TITLE"](https://doi.org/10.1039/C0CP01001D).

<!-- TODO: Show plots with original axis units, see #25. It would be great if we could toggle between SI and original units. See #31. -->
<!-- TODO: Properly format plots. They should probably be much bigger since they are nice to look at. See #31. -->
{{ entry.plot()._repr_html_() }}

{{ entry.plot('A / m^2')._repr_html_() }}

<!-- TODO: Make download link work, i.e., build .zip package and link to it here. See #31. -->
[Download datapackage with ID-XXXXXXXX](http://link.to.datapackage.XXXXXXXXzip)

<!-- TODO: Style this section. See #31. -->
## Further information
The Pt(111) electrode was prepared by:
`Content from the yaml file`

Properties of the electrochemical cell:

* Type: XXX
* Counter electrode: XXX
* Reference electrode: XXX

<!-- TODO: Insert all the metadata from the .yaml file in some collapsible form here. E.g., just the YAML file with syntax highlighting. See #31. -->
## Metdata
<details>
<summary>Click to expand metadata (yaml).</summary>

```yaml
{{ entry.electrochemical_system.create_yaml() }}
```
</details>

----

<!-- TODO: Insert links to other data which are plotted in the same figure and/or even add a plot with all data from that figure. See #31 -->
