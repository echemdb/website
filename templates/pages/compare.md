# Cyclic Voltammograms
{{ intro }}
<div id="vis"></div>
Click a graph to add it to the comparison.

{% for material in database.materials() %}

## {{ material }}


{{ render("components/cv_compare_table.md", entries_path=entries_path, database=database.filter(material_filter(material))) }}

{% endfor %}

<script src="https://cdn.plot.ly/plotly-2.12.1.min.js"></script>
<script src="https://d3js.org/d3.v7.js"></script>

<script>
// selection mechanism
var selected_cyclic_voltammograms = [];
var traces = [];
Plotly.newPlot('vis', traces);
// console.log([...d3.selectAll('.checkbox')._groups[0]].map(checkbox => { return checkbox.name}));
async function getData(names) {
	//traces = [];

	// for (const name of names) {
	// 	const source = name.split("_").slice(0, -2).join("_");
	// 	const cv_data = await d3.csv(["/data/generated/svgdigitizer/", source, "/", name, ".csv"].join(""), convertNumbers);
	// 	traces.push(cv_data);
	// }


	traces = await Promise.all(
		names.map(name => {
		console.log(name);
		const source = name.split("_").slice(0, -2).join("_");
		return d3.csv(["/data/generated/svgdigitizer/", source, "/", name, ".csv"].join(""), convertNumbers).then(processData);
		// return d3.csv(["/data/generated/svgdigitizer/", source, "/", name, ".csv"].join(""), convertNumbers).then(processData)
		})
	 );
};

function convertNumbers(row) {
  var r = {};
  for (var k in row) {
    r[k] = +row[k];
    if (isNaN(r[k])) {
      r[k] = row[k];
    }
  }
  return r;
}

function processData(allRows) {
  var x = []; 
  var y = [];
  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['E'] );
    y.push( row['j'] );
  }

  return {x: x, y: y, type: 'scatter'}
};

// callback on selections for all checkboxes
// not ideal since for every selection iterate over all checkboxes
d3.selectAll(".checkbox")
.on("change", function(d, i) {
selected_cyclic_voltammograms = [...d3.selectAll("input[class='checkbox']:checked")._groups[0]].map(checkbox => { return checkbox.name});
console.log(selected_cyclic_voltammograms)
getData(selected_cyclic_voltammograms);

console.log(traces);

Plotly.newPlot('vis', traces);

}
);

</script>


