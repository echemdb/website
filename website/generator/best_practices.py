r"""
Access to the best-practice reference table.

The table is a curated index of best-practice, protocol, and tutorial
literature for electrochemistry. Its source of truth is
``data/best_practices/best_practices_table.json``, with the corresponding
BibTeX entries in ``data/best_practices/bibliography.bib``.

EXAMPLES::

    >>> from website.generator.best_practices import sections
    >>> for section in sections("general"):
    ...     print(section["title"])
    Cross-domain consensus protocols
    Data, metadata, FAIR and open science
    General reproducibility, verification and research software

"""

# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2026 Albert Engstfeld
#
#  echemdb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  echemdb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with echemdb. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************

import functools
import json
import os.path
import re

DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "best_practices")
)

TABLE = os.path.join(DATA_DIR, "best_practices_table.json")

BIBLIOGRAPHY = os.path.join(DATA_DIR, "bibliography.bib")


@functools.cache
def table():
    r"""
    Return the raw best-practice table.

    EXAMPLES::

        >>> from website.generator.best_practices import table
        >>> sorted(table().keys())
        ['_comment', 'sections', 'tags']

    """
    with open(TABLE, encoding="utf-8") as source:
        return json.load(source)


@functools.cache
def bibliography():
    r"""
    Return the bibliography backing the best-practice table, i.e., a dict
    mapping BibTeX keys to their parsed entries.

    EXAMPLES::

        >>> from website.generator.best_practices import bibliography
        >>> bibliography()["boettcher_2021_potentially"]["doi"]
        '10.1021/acsenergylett.0c02443'

    """
    with open(BIBLIOGRAPHY, encoding="utf-8") as source:
        return parse_bibtex(source.read())


def parse_bibtex(bibtex):
    r"""
    Return the entries of the BibTeX database `bibtex`, i.e., a dict mapping
    each key to its verbatim source and to its ``doi`` and ``url`` fields.

    This is a deliberately minimal parser. We only need to identify entries by
    their key and read the two fields that provide a link to the work.

    EXAMPLES::

        >>> from website.generator.best_practices import parse_bibtex
        >>> entries = parse_bibtex('''
        ... @article{doe_2026_example,
        ...   title = {An {Example}},
        ...   doi   = {10.0000/example},
        ... }
        ... ''')
        >>> entries["doe_2026_example"]["doi"]
        '10.0000/example'
        >>> entries["doe_2026_example"]["url"] is None
        True

    """
    entries = {}

    for match in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", bibtex):
        opening = bibtex.index("{", match.start())
        source = bibtex[match.start() : _closing_brace(bibtex, opening) + 1]

        entries[match.group(2)] = {
            "type": match.group(1).lower(),
            "source": source,
            "doi": _field(source, "doi"),
            "url": _field(source, "url"),
        }

    return entries


def _closing_brace(text, opening):
    r"""
    Return the position of the brace in `text` that closes the brace at
    position `opening`.

    EXAMPLES::

        >>> from website.generator.best_practices import _closing_brace
        >>> _closing_brace("{a{b}c}", 0)
        6

    """
    depth = 0

    for position in range(opening, len(text)):
        if text[position] == "{":
            depth += 1
        elif text[position] == "}":
            depth -= 1
            if depth == 0:
                return position

    raise ValueError(f"unbalanced braces in BibTeX entry at position {opening}")


def _field(source, name):
    r"""
    Return the value of the BibTeX field `name` of the entry `source` or
    ``None`` if the entry has no such field.

    EXAMPLES::

        >>> from website.generator.best_practices import _field
        >>> _field("@misc{key, url = {https://echemdb.org}}", "url")
        'https://echemdb.org'
        >>> _field("@misc{key}", "doi") is None
        True

    """
    match = re.search(rf"\b{name}\s*=\s*[{{\"]", source, re.IGNORECASE)

    if match is None:
        return None

    if source[match.end() - 1] == "{":
        value = source[match.end() : _closing_brace(source, match.end() - 1)]
    else:
        value = source[match.end() : source.index('"', match.end())]

    return " ".join(value.split())


def sections(scope):
    r"""
    Return the sections of the best-practice table with this `scope`, i.e.,
    ``"domain"`` for the literature of interfacial electrochemistry and
    electrocatalysis itself, and ``"general"`` for the cross-domain literature
    on reporting, data, and reproducibility that the field builds on.

    Each section carries the ``references`` shown in its table.

    EXAMPLES::

        >>> from website.generator.best_practices import sections
        >>> section = sections("domain")[0]
        >>> section["title"]
        'Basic electrochemistry and measurement practice'

    """
    if scope not in ["domain", "general"]:
        raise ValueError(f"scope must be 'domain' or 'general' but was {scope}")

    return [
        dict(section, references=references(section))
        for section in table()["sections"]
        if section.get("scope", "domain") == scope
    ]


def references(section):
    r"""
    Return the references shown in the table of `section`, sorted by year, most
    recent first.

    A work is stored exactly once in the table, namely in the section it is
    filed under. It is however cross-listed into every section whose slug it
    carries as a tag, so that a reader browsing a topic sees everything that is
    relevant to it. A section of scope ``domain`` only collects works of that
    same scope, so that no table for interfacial electrochemistry pulls in
    literature from outside the field.

    EXAMPLES:

    The work on iR compensation is filed under basic electrochemistry but
    tagged, and therefore also shown, with water electrolysis::

        >>> from website.generator.best_practices import references, table
        >>> water = [section for section in table()["sections"] if section["slug"] == "water_electrolysis"][0]
        >>> "son_2023_navigating" in [reference["key"] for reference in references(water)]
        True

    The references are sorted by year, most recent first::

        >>> years = [reference["year"] for reference in references(water)]
        >>> years == sorted(years, reverse=True)
        True

    """
    collect = set(section.get("collect") or [section["slug"]])
    general = section.get("scope", "domain") == "general"

    collected = list(section["rows"])

    for other in table()["sections"]:
        if other["slug"] == section["slug"]:
            continue

        for row in other["rows"]:
            if not collect & set(row.get("tags", [])):
                continue
            if general or _scope(other, row) == "domain":
                collected.append(row)

    return sorted(
        [reference(row) for row in collected],
        key=lambda reference: reference["year"],
        reverse=True,
    )


def _scope(section, row):
    r"""
    Return the scope of `row`, which it inherits from the `section` it is filed
    under unless it overrides it.

    EXAMPLES::

        >>> from website.generator.best_practices import _scope
        >>> _scope({"scope": "general"}, {})
        'general'
        >>> _scope({"scope": "general"}, {"scope": "domain"})
        'domain'

    """
    return row.get("scope") or section.get("scope", "domain")


def reference(row):
    r"""
    Return a row of the best-practice table as it is displayed on the website,
    i.e., the title of the work, the year it appeared, and a link to it that is
    labeled with its authors.

    Works are linked through their DOI. For the few without one, we fall back
    to the URL recorded in the bibliography.

    EXAMPLES::

        >>> from website.generator.best_practices import reference
        >>> displayed = reference({"key": "boettcher_2021_potentially",
        ...                        "authors": "Boettcher *et al.*",
        ...                        "title": "Potentially Confusing: Potentials in Electrochemistry",
        ...                        "journal": "ACS Energy Lett.",
        ...                        "year": "2021",
        ...                        "doi": "10.1021/acsenergylett.0c02443"})
        >>> displayed["title"]
        'Potentially Confusing: Potentials in Electrochemistry'
        >>> displayed["authors"], displayed["year"]
        ('Boettcher *et al.*', '2021')
        >>> displayed["url"]
        'https://doi.org/10.1021/acsenergylett.0c02443'

    A work without a DOI is linked through the URL of its bibliography entry::

        >>> reference({"key": "biologic_2024_practices",
        ...            "authors": "BioLogic Science Instruments",
        ...            "title": "An Essential Guide to the Best Laboratory Practices for Electrochemistry",
        ...            "year": "2024"})["url"]
        'https://www.electrochem.org/ecsnews/biologic-best-lab-practices-guide'

    """
    entry = bibliography().get(row.get("key"), {})

    doi = row.get("doi") or entry.get("doi")

    return {
        "key": row.get("key", ""),
        "title": title(row),
        "authors": row.get("authors", ""),
        "journal": row.get("journal", ""),
        "year": row.get("year", ""),
        "url": f"https://doi.org/{doi}" if doi else entry.get("url"),
        "tags": row.get("tags", []),
    }


def title(row):
    r"""
    Return the title of the work in `row`, extended by the gloss that the table
    provides for some of them.

    EXAMPLES::

        >>> from website.generator.best_practices import title
        >>> title({"title": "Reproducibility of Water Oxidation",
        ...        "gloss": "(NiFe OER interlaboratory study)"})
        'Reproducibility of Water Oxidation (NiFe OER interlaboratory study)'

    """
    if row.get("gloss"):
        return f"{row['title']} {row['gloss']}"

    return row["title"]


def count(scope):
    r"""
    Return the number of works with this `scope` in the best-practice table.

    Works are counted where they are stored, so cross-listing does not inflate
    these counts.

    EXAMPLES::

        >>> from website.generator.best_practices import count
        >>> count("domain") + count("general") == sum(
        ...     len(section["rows"]) for section in table()["sections"])
        True

    """
    return len(
        [
            row
            for section in table()["sections"]
            for row in section["rows"]
            if _scope(section, row) == scope
        ]
    )
