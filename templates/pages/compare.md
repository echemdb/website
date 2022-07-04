# Cyclic Voltammograms
{{ intro }}
<div id="vis"></div>
Click a graph to add it to the comparison.



<input type="text" id="filterInput" onkeyup="quickFilter()" placeholder="Filter list ..." title="Type in a name">

{{ render("components/cv_compare_table.md", entries_path=entries_path, database=database) }}

<script src="https://cdn.plot.ly/plotly-2.12.1.min.js"></script>
<script src="https://d3js.org/d3.v7.js"></script>
<script src="/javascripts/compare.js"></script>
