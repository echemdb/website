# Best-Practice Reference Table

A curated index of best-practice, protocol, and tutorial literature for
electrochemistry, i.e., of works describing how electrochemical measurements
should be performed, reported, and reproduced.

The table is the source of truth for the *Best Practices* pages of the website,
which are generated from it during the build, see
[`website/generator/best_practices.py`](../../website/generator/best_practices.py).

## Files

* `bibliography.bib` — the BibTeX entry of each work. This is where a work is
  described: its authors, its title, the year it appeared, its DOI or URL, and
  everything else one needs to cite it.
* `best_practices_table.json` — where each work belongs, i.e., its topic and
  its tags. A row points to a BibTeX entry by its `key` and repeats nothing
  that the entry already says.

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

Everything a table shows about a work comes from its bibliography entry, which
is read with [pybtex](https://pybtex.org):

* the title from the `title` field, with its LaTeX markup rendered as text, so
  that `CO\textsubscript{2}` is shown as CO₂,
* the label of the link from the authors: one author is named, two are named
  with an ampersand, and more are shortened to `Boettcher *et al.*`,
* the year from the `year` field, which has to be the one the work is cited
  under, i.e., for a journal article the year of its issue rather than the year
  it first appeared online,
* the link from the `doi` field, or from the `url` field for works without a
  DOI.

A row therefore never repeats any of this. The one thing it may add is a
`gloss`, a short parenthesis appended to the title where the title alone does
not say what the work provides.

## Adding a work

1. Add its BibTeX entry to `bibliography.bib`. Its `key` is
   `surname_year_firstword`, i.e., the surname of the first author, the year it
   is cited under, and the first significant word of the title. The `year` of
   the entry has to agree with the year in the key.
2. Add a row for that `key` to the section it belongs to, and tag it with the
   slug of every other section it should appear in. Store a work exactly once;
   never duplicate a row to make it appear twice.
3. Only use tags that exist in the top-level `tags` object; add the tag there
   first if it does not.

Both files are plain text, so a work can be suggested with a pull request that
touches nothing else. Alternatively, open an
[issue](https://github.com/echemdb/website/issues) with the DOI of the work and
the topic it belongs to, and we add it.
