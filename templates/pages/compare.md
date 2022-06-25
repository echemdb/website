# Cyclic Voltammograms
{{ intro }}

Click a graph to add it to the comparison.

{% for material in database.materials() %}

## {{ material }}


{{ render("components/cv_compare_table.md", entries_path=entries_path, database=database.filter(material_filter(material))) }}

{% endfor %}
<script src="https://d3js.org/d3.v7.js"></script>
<script>
	var selected_cyclic_voltammograms = [];
	console.log(d3.selectAll('.checkbox'))
d3.selectAll(".checkbox")
.on("change", function(d, i) {
	selected_cyclic_voltammograms = d3.selectAll("input[class='checkbox']:checked");
	console.log(selected_cyclic_voltammograms);
	});

</script>
