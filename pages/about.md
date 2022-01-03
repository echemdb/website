# About the project

echemdb is a repository for high quality experimental and theoretical data on electrochemical systems. 

While electrochemistry has become a research field of increasing importance,
metadata standards do not exist and published data is often not accessible. 
This is especially the case for data which has been published in the past.

In order to improve reusablity of published data, the authors of echemdb created 
[svgdigitizer](https://github.com/echemdb/svgdigitizer), a tool allowing for 
digitizing published 2D plots. 

Currently the authors of echemdb limit themselves to digitizing cyclic voltammograms.
For ease of access, these digitized voltammograms (CSV) are stored along with a set of
metadata, carefully extracted from the scientific publication, in a so called data package.

A set of data packages forms the electrochemical database, whose entries are displayed in 
different forms on this website. An Python API provides direct access to the entries in the database, 
enabling seamless integration into existing workflows.

<!-- 
Reliable and appropriately standardized data across different systems is still rare, especially
as small changes in the experiments can easily yield dramatic differences in the observations.
-->