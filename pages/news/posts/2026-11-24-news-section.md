---
date: 2026-11-24
slug: news-section-and-scientific-data
---

# echemdb has a news section, and our data descriptor was accepted in *Scientific Data*

Welcome to the new news section of echemdb.org!
From now on, we announce new data, software releases, publications, and events here.

We open it with good news: the data descriptor of the echemdb CV dataset was accepted in *Scientific Data*.

<!-- more -->

The data descriptor presents the dataset of fingerprint cyclic voltammograms (CVs) for single crystal electrodes,
digitized from the literature, annotated with metadata, and standardized into unit-aware Data Packages.
It also describes the framework behind it: the [svgdigitizer](https://echemdb.github.io/svgdigitizer/) to recover data from published figures,
the [metadata schema](https://github.com/echemdb/metadata-schema),
and the [unitpackage](https://echemdb.github.io/unitpackage/) Python API to explore and reuse the data.

The publication is the result of a joint effort of many contributors, who digitized, annotated, and validated the data.
Thank you all!

When using the dataset, please cite

{{ render('components/citation_dataset.md') }}

and the specific dataset version on <a href="https://doi.org/10.5281/zenodo.20723429"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.20723429.svg" alt="DOI"></a>.

[→ Explore the CV dataset](../../cv/index.md)

We will update the citation with the volume and DOI once the article is published.
