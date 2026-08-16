r"""
Access to the best-practice reference table.

The table is a curated index of best-practice, protocol, and tutorial
literature for electrochemistry. Its source of truth is
``data/best_practices/best_practices_table.json``, with the corresponding
BibTeX entries in ``data/best_practices/bibliography.bib``.

EXAMPLES::

    >>> from website.generator.best_practices import groups
    >>> for group in groups("general"):
    ...     print(group["title"], [section["title"] for section in group["sections"]])
    None ['Cross-domain consensus protocols', 'Data, metadata, FAIR and open science', 'General reproducibility, verification and research software']

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
        ['_comment', 'groups', 'sections', 'tags']

    """
    with open(TABLE, encoding="utf-8") as source:
        return json.load(source)


@functools.cache
def bibliography():
    r"""
    Return the bibliography backing the best-practice table, i.e., the BibTeX
    entries of all the works it lists, keyed by their BibTeX key.

    EXAMPLES::

        >>> from website.generator.best_practices import bibliography
        >>> bibliography()["boettcher_2021_potentially"].fields["doi"]
        '10.1021/acsenergylett.0c02443'

    """
    from pybtex.database.input.bibtex import Parser

    return Parser(encoding="utf-8").parse_file(BIBLIOGRAPHY).entries


# The subscripts of a chemical formula, i.e., CO\textsubscript{2} on the LaTeX
# side and CO₂ on the website.
SUBSCRIPTS = str.maketrans("0123456789xyn+-", "₀₁₂₃₄₅₆₇₈₉ₓᵧₙ₊₋")


def unicode(latex):
    r"""
    Return the LaTeX markup `latex` of a BibTeX field as the text that is shown
    on the website.

    EXAMPLES::

        >>> from website.generator.best_practices import unicode
        >>> unicode(r"Preparing {Alkaline} Electrolytes -- an Overview")
        'Preparing Alkaline Electrolytes – an Overview'

    Subscripts are shown as such, since a chemical formula is much easier to
    read that way::

        >>> unicode(r"Faradaic Efficiency in Electrochemical CO\textsubscript{2} Reduction")
        'Faradaic Efficiency in Electrochemical CO₂ Reduction'

    """
    from pylatexenc.latex2text import LatexNodes2Text

    latex = re.sub(
        r"\\textsubscript\{([0-9xyn+-]+)\}",
        lambda match: match.group(1).translate(SUBSCRIPTS),
        latex,
    )

    return LatexNodes2Text().latex_to_text(latex).strip()


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


def groups(scope):
    r"""
    Return the sections of the best-practice table with this `scope`, grouped
    by the topic groups of the table, in the order in which they are displayed.

    Sections that are not part of any group are returned in a final group
    without a title, so that they are shown at the same level as the groups
    themselves.

    EXAMPLES::

        >>> from website.generator.best_practices import groups
        >>> for group in groups("domain"):
        ...     print(group["title"], len(group["sections"]))
        Measurement practice 6
        Electrodes and surfaces 2
        Reactions and devices 5
        Reporting and rigour 5
        None 1

    """
    grouped = sections(scope)

    ordered = [
        {
            "title": group["title"],
            "sections": [
                section for section in grouped if section.get("group") == group["slug"]
            ],
        }
        for group in table()["groups"]
    ]

    ungrouped = [section for section in grouped if "group" not in section]

    return [group for group in ordered if group["sections"]] + (
        [{"title": None, "sections": ungrouped}] if ungrouped else []
    )


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

    Nothing of this is stored in the table. Everything is read from the
    bibliography entry that the row names, so that a work is described in
    exactly one place. Works are linked through their DOI, and through the URL
    of their bibliography entry when they have no DOI.

    EXAMPLES::

        >>> from website.generator.best_practices import reference
        >>> displayed = reference({"key": "boettcher_2021_potentially"})
        >>> displayed["title"]
        'Potentially Confusing: Potentials in Electrochemistry'
        >>> displayed["authors"], displayed["year"]
        ('Boettcher *et al.*', '2021')
        >>> displayed["url"]
        'https://doi.org/10.1021/acsenergylett.0c02443'

    A work without a DOI is linked through the URL of its bibliography entry::

        >>> reference({"key": "biologic_2024_practices"})["url"]
        'https://www.electrochem.org/ecsnews/biologic-best-lab-practices-guide'

    """
    entry = bibliography()[row["key"]]
    doi = entry.fields.get("doi")

    return {
        "key": row["key"],
        "title": title(entry, row.get("gloss")),
        "authors": authors(entry),
        "year": entry.fields.get("year", ""),
        "url": f"https://doi.org/{doi}" if doi else entry.fields.get("url"),
        "tags": row.get("tags", []),
    }


def title(entry, gloss=None):
    r"""
    Return the title of the work of the bibliography `entry`, extended by the
    `gloss` that the table provides for some of them.

    EXAMPLES::

        >>> from website.generator.best_practices import bibliography, title
        >>> title(bibliography()["hausmann_2025_reproducibility"])
        'Reproducibility in Electrocatalysis'
        >>> title(bibliography()["hausmann_2025_reproducibility"],
        ...       gloss="(NiFe OER interlaboratory study)")
        'Reproducibility in Electrocatalysis (NiFe OER interlaboratory study)'

    """
    text = unicode(entry.fields["title"])

    if gloss:
        return f"{text} {gloss}"

    return text


def authors(entry):
    r"""
    Return the authors of the work of the bibliography `entry` as the label of
    the link to it.

    A work of one or two authors names them, anything beyond that is shortened
    to the first author.

    EXAMPLES::

        >>> from website.generator.best_practices import authors, bibliography
        >>> authors(bibliography()["jerkiewicz_2022_applicability"])
        'Jerkiewicz'
        >>> authors(bibliography()["sebastianpascual_2020_addressing"])
        'Sebastián-Pascual & Escudero-Escribano'
        >>> authors(bibliography()["boettcher_2021_potentially"])
        'Boettcher *et al.*'

    Particles are part of a surname, and an institution that authors a work is
    named in full::

        >>> authors(bibliography()["iglesiasvanmontfort_2023_advanced"])
        'Iglesias van Montfort *et al.*'
        >>> authors(bibliography()["biologic_2024_practices"])
        'Bio-Logic Science Instruments'

    """
    persons = entry.persons.get("author") or entry.persons.get("editor") or []

    names = [
        unicode(" ".join(person.prelast_names + person.last_names))
        for person in persons
    ]

    if not names:
        return ""

    if len(names) == 1:
        return names[0]

    if len(names) == 2:
        return f"{names[0]} & {names[1]}"

    return f"{names[0]} *et al.*"


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
