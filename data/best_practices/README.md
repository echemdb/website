# Best-Practice Reference Table

A curated index of best-practice, protocol, and tutorial literature for
electrochemistry, i.e., of works describing how electrochemical measurements
should be performed, reported, and reproduced.

The table is the source of truth for the *Best Practices* pages of the website,
which are generated from it during the build, see
[`website/generator/best_practices.py`](../../website/generator/best_practices.py).

## Files

* `best_practices_table.json` — the table itself, one entry per work.
* `bibliography.bib` — the BibTeX entry of each work, keyed by the `key` of its
  row. It is published alongside the generated pages so that readers can import
  the entire collection into a reference manager.

## Structure

The table consists of `sections`, each of which holds the `rows` filed under it:

```json
{
  "slug": "basic_electrochemistry",
  "scope": "domain",
  "group": "measurement_practice",
  "title": "Basic electrochemistry and measurement practice",
  "nav": "Basic electrochemistry",
  "rows": [
    {
      "key": "boettcher_2021_potentially",
      "authors": "Boettcher *et al.*",
      "title": "Potentially Confusing: Potentials in Electrochemistry",
      "journal": "ACS Energy Lett.",
      "volume": "6",
      "page": "261",
      "year": "2021",
      "doi": "10.1021/acsenergylett.0c02443",
      "tags": ["reference_electrodes", "fundamental"]
    }
  ]
}
```

The `scope` of a section is either

* `domain` — the literature of interfacial electrochemistry and
  electrocatalysis itself, or
* `general` — cross-domain literature on reporting, data, and reproducibility
  that the practices of the field build on.

The two scopes are shown on separate pages, so that no table of the field
carries a reference from outside it. A row may override the `scope` of its
section, which is how a work on electrochemistry filed under a cross-domain
topic is still shown with the field.

Sections are shown in the order in which they appear in the file, under the
heading of the `group` they name. The groups themselves, and their order, are
declared in the top-level `groups` object. A section without a `group` is shown
after the groups, at the same level as their headings.

Every row carries `tags` from the controlled vocabulary in the top-level `tags`
object. Tags in the `topic` group are section slugs and decide where a work is
shown: it appears in the table of the section it is filed under, plus in the
table of every section whose slug it carries as a tag. The remaining groups
(`reaction`, `approach`, `aspect`) are descriptive and are meant for filtering
the collection.

Rows without a `doi` are linked through the `url` of their bibliography entry
instead. A `gloss` is a short parenthesis appended to the title where the title
alone does not say what the work provides.

## Adding a work

1. Add its row to the section it belongs to, and tag it with the slug of every
   other section it should appear in. Store a work exactly once; never
   duplicate a row to make it appear twice.
2. Add its BibTeX entry to `bibliography.bib`, using the same `key`, which is
   `surname_year_firstword` of the first author, the year, and the first
   significant word of the title.
3. Only use tags that exist in the top-level `tags` object; add the tag there
   first if it does not.

Both files are plain text, so a work can be suggested with a pull request that
touches nothing else. Alternatively, open an
[issue](https://github.com/echemdb/website/issues) with the DOI of the work and
the topic it belongs to, and we add it.
