# Cyclic Voltammograms
{{ intro }}
<div id="vis"></div>
Click a graph to add it to the comparison.



<input type="text" id="filterInput" onkeyup="quickFilter()" placeholder="Filter list ..." title="Type in a name">

{{ render("components/cv_compare_table.md", entries_path=entries_path, database=database) }}




<script src="https://cdn.plot.ly/plotly-2.12.1.min.js"></script>
<script src="https://d3js.org/d3.v7.js"></script>

<script>

var cache = {};
var traces = [];

var layout = {

    xaxis: {
        title: {
            text: '<i>E</i> [V]',
            font: {
                family: 'Courier New, monospace',
                size: 18,
            }
        },
        showline: true,
        zeroline: false,
        ticks: "outside",
        mirror: true,
        side: "bottom"
    },

    yaxis: {
        title: {
            text: '<i>j</i> [A m⁻²]',
            font: {
                family: 'Courier New, monospace',
                size: 18,
            }
        },
        showline: true,
        zeroline: true,
        ticks: "outside",
        mirror: true,
        side: "left"
    },
    legend: {
        yanchor: "top",
        y: -0.3,
        xanchor: "left",
        x: 0.01
    }
};

Plotly.newPlot('vis', traces, layout);

async function updatePlot(names) {
    Promise.all(
            names.map(name => {
                const source = name.split("_")
                    .slice(0, -2)
                    .join("_");
                if (name in cache) {
                    return cache[name];
                } else {
                    return d3.csv(["/data/generated/svgdigitizer/", source, "/", name, ".csv"].join(""), convertNumbers)
                        .then(processData)
                        .then(function (result) {
                            return {
                                x: result[0],
                                y: result[1],
                                name: name,
                                type: 'scatter'
                            }
                        })
                        .then(function (result) {
                            cache[name] = result;
                            return result;
                        });
                }
            })
        )
        .then(function (traces) {
            Plotly.newPlot('vis', traces, layout);
        });
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
    for (var i = 0; i < allRows.length; i++) {
        row = allRows[i];
        x.push(row['E']);
        y.push(row['j']);
    }

    return [x, y]
};

// selection mechanism
var selected_cyclic_voltammograms = [];
// callback on selections for all checkboxes
// not ideal since for every selection iterate over all checkboxes
d3.selectAll(".checkbox")
    .on("change", function (d, i) {
        selected_cyclic_voltammograms = [...d3.selectAll("input[class='checkbox']:checked")
            ._groups[0]
        ].map(checkbox => {
            return checkbox.name
        });
        updatePlot(selected_cyclic_voltammograms);
    });

function quickFilter() {
    var input, filter, table, tr, i, f, trContent, results;
    input = document.getElementById("filterInput");
    filter = input.value.toUpperCase().split(" ");
    table = document.getElementsByClassName("md-typeset__table")[0];
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
    
        trContent = tr[i].textContent.replace(/[\s]+/g, ' ');

        if (trContent) {
            results = []
            for (f of filter)  {
                if (trContent.toUpperCase().indexOf(f) > -1) {
                    results.push(true);
                } else {
                    results.push(false);
                }
            }

            if (results.every( (val, r, arr) => val === true )) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
}

</script>
