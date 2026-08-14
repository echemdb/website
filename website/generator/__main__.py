r"""
Create generated pages for the website.

This module is invoked by the `mkdocs-gen-files module
<https://oprypin.github.io/mkdocs-gen-files/>` to generate pages such as the
individual pages for each entry in the database.
"""

# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2021-2026 Albert Engstfeld
#        Copyright (C) 2021      Johannes Hermann
#        Copyright (C) 2021-2022 Julian Rüth
#        Copyright (C) 2021      Nicolas Hörmann
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

import os.path
import time

import mkdocs_gen_files

import website.generator.best_practices
import website.generator.database
from website.macros.render import render


def main():  # pylint: disable=R0914
    r"""
    Create MarkDown files in a virtual file system that is consumed by mkdocs
    when building the website.

    This function is invoked automatically by mkdocs during the build process.
    """
    t_pages_start = time.time()
    database = website.generator.database.cv
    # Create a single page for each entry in the database
    for entry in database:
        print(f"Generating page for {entry.identifier}")
        with mkdocs_gen_files.open(
            os.path.join("cv", "entries", f"{entry.identifier}.md"), "w"
        ) as markdown:
            markdown.write(
                render(
                    "pages/cv_entry.md",
                    entry=entry,
                )
            )
    t_pages = time.time() - t_pages_start
    print(f"Generated {len(database)} pages in {t_pages:.2f} seconds")
    t_aqueous_start = time.time()
    # Create an overview page with tabulated and linked entries for aqueous systems.
    with mkdocs_gen_files.open(os.path.join("cv", "aqueous.md"), "w") as markdown:
        print("Generating overview page for aqueous systems")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "aqueous"
                    and "BCV" in entry.experimental.tags
                ),
                title="Aqueous Systems",
                intro="Overview of cyclic voltammograms for electrodes"
                "recorded in aqueous electrolytes, denoted by the tag BCV (base cyclic voltammograms).",
                material_filter=material_filter(),
            )
        )
    t_aqueous = time.time() - t_aqueous_start
    print(f"Generated aqueous overview page in {t_aqueous:.2f} seconds")
    t_bcv_start = time.time()
    # Create an overview page with tabulated and linked entries for aqueous BCV systems with a single electrolyte component besides water.
    with mkdocs_gen_files.open(
        os.path.join("cv", "aqueous", "single_component.md"), "w"
    ) as markdown:
        print("Generating overview page for aqueous BCV (single component)")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "aqueous"
                    and "BCV" in entry.experimental.tags
                    and len(
                        [
                            c
                            for c in entry.system.electrolyte.components
                            if c.type not in ("solvent", "gas")
                        ]
                    )
                    == 1
                ),
                title="Single Component Systems",
                intro="Base cyclic voltammograms for electrodes recorded"
                " in aqueous electrolytes with a single additional component (water + one acid, base, or salt).",
                material_filter=material_filter(),
            )
        )
    t_bcv = time.time() - t_bcv_start
    print(f"Generated BCV overview page in {t_bcv:.2f} seconds")
    t_coor_start = time.time()
    # Create an overview page with tabulated and linked entries for CO oxidation (COOR) in aqueous systems.
    with mkdocs_gen_files.open(
        os.path.join("cv", "aqueous", "COOR.md"), "w"
    ) as markdown:
        print("Generating overview page for COOR in aqueous systems")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "aqueous"
                    and "COOR" in entry.experimental.tags
                ),
                title="CO oxidation reaction - COOR",
                intro="Cyclic voltammograms for electrodes recorded in CO containing aqueous electrolytes "
                "(COOR - CO oxidation reaction).",
                material_filter=material_filter(),
            )
        )
    t_coor = time.time() - t_coor_start
    print(f"Generated COOR overview page in {t_coor:.2f} seconds")
    t_faor_start = time.time()
    # Create an overview page with tabulated and linked entries for formic acid oxidation reaction (FAOR) in aqueous systems.
    with mkdocs_gen_files.open(
        os.path.join("cv", "aqueous", "FAOR.md"), "w"
    ) as markdown:
        print("Generating overview page for FAOR in aqueous systems")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "aqueous"
                    and "FAOR" in entry.experimental.tags
                ),
                title="Formaic Acid Oxidation Reaction - FAOR",
                intro="Cyclic voltammograms for electrodes recorded in formic acid "
                "containing aqueous electrolytes (FAOR - formic acid oxidation reaction).",
                material_filter=material_filter(),
            )
        )
    t_faor = time.time() - t_faor_start
    print(f"Generated FAOR overview page in {t_faor:.2f} seconds")
    t_sha_start = time.time()
    # Create an overview page with tabulated and linked entries for specific halide adsorption (SHA) in aqueous systems.
    with mkdocs_gen_files.open(
        os.path.join("cv", "aqueous", "SHA.md"), "w"
    ) as markdown:
        print("Generating overview page for SHA in aqueous systems")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "aqueous"
                    and "SHA" in entry.experimental.tags
                ),
                title="Specific Halide Adsorption - SHA",
                intro="Cyclic voltammograms for electrodes recorded in "
                "halide containing aqueous electrolytes (SHA - specific halide adsorption).",
                material_filter=material_filter(),
            )
        )
    t_sha = time.time() - t_sha_start
    print(f"Generated SHA overview page in {t_sha:.2f} seconds")
    t_ionic_liquid_start = time.time()
    # Create an overview page with tabulated and linked entries for ionic liquid systems.
    with mkdocs_gen_files.open(os.path.join("cv", "ionic_liquid.md"), "w") as markdown:
        print("Generating overview page for ionic liquids")
        markdown.write(
            render(
                "pages/cv.md",
                database=database.filter(
                    lambda entry: entry.system.electrolyte.type == "ionic liquid"
                ),
                title="Ionic Liquids - ILs",
                intro="Cyclic Voltammograms for electrodes recorded in Ionic Liquids",
                material_filter=material_filter(),
            )
        )
    t_ionic_liquid = time.time() - t_ionic_liquid_start
    print(f"Generated ionic liquid overview page in {t_ionic_liquid:.2f} seconds")
    best_practices()


def best_practices():
    r"""
    Create the pages of the best-practice reference table, i.e., an overview of
    the literature on how to perform, report, and reproduce electrochemical
    measurements.

    The literature of interfacial electrochemistry and electrocatalysis itself
    and the cross-domain literature it builds on are shown on separate pages.
    Both link the bibliography of the entire table, which we publish alongside
    them so that the references can be imported into a reference manager.
    """
    print("Generating best practices pages")

    with mkdocs_gen_files.open(
        os.path.join("resources", "best_practices.md"), "w"
    ) as markdown:
        markdown.write(
            render(
                "pages/best_practices.md",
                title="Best Practices",
                intro="A curated index of best-practice, protocol, and tutorial literature for"
                " interfacial electrochemistry and electrocatalysis, i.e., recommendations on"
                " how electrochemical measurements should be performed, reported, and"
                " reproduced.\n\n"
                "The works are grouped by topic and sorted by year, most recent first."
                " Click a column header to sort a table by that column. A work that is"
                " relevant to several topics is listed in each of them.\n\n"
                "Recommendations on data, metadata, and reproducibility that are not specific"
                " to electrochemistry are collected separately in"
                " [cross-domain references](best_practices/cross_domain.md).",
                groups=website.generator.best_practices.groups("domain"),
                outro=best_practices_outro(
                    bibliography="best_practices/bibliography.bib",
                    resources="index.md",
                ),
            )
        )

    with mkdocs_gen_files.open(
        os.path.join("resources", "best_practices", "cross_domain.md"), "w"
    ) as markdown:
        markdown.write(
            render(
                "pages/best_practices.md",
                title="Cross-Domain References",
                intro="Recommendations on reporting, data, metadata, and reproducibility that"
                " are not specific to electrochemistry but which the practices of the field"
                " build on.\n\n"
                "For the literature of interfacial electrochemistry and electrocatalysis"
                " itself, see [best practices](../best_practices.md).",
                groups=website.generator.best_practices.groups("general"),
                outro=best_practices_outro(
                    bibliography="bibliography.bib",
                    resources="../index.md",
                ),
            )
        )

    with open(
        website.generator.best_practices.BIBLIOGRAPHY, encoding="utf-8"
    ) as bibliography:
        with mkdocs_gen_files.open(
            os.path.join("resources", "best_practices", "bibliography.bib"), "w"
        ) as published:
            published.write(bibliography.read())


def best_practices_outro(bibliography, resources):
    r"""
    Return the closing section of a best-practice page, i.e., the download of
    the bibliography at the relative path `bibliography` and the invitation to
    contribute on the resources page at the relative path `resources`.

    EXAMPLES::

        >>> "[bibliography.bib](bibliography.bib)" in best_practices_outro(
        ...     "bibliography.bib", "../index.md")
        True

    """
    return (
        "## References\n\n"
        "All references listed on this page and on its companion page are available as a"
        f" single BibTeX file, [bibliography.bib]({bibliography}).\n\n"
        "The collection is non-exhaustive. Do you know a work that should be listed here?"
        f" See [suggest a link]({resources}#suggest-a-link)."
    )


def material_filter():
    r"""
    A lambda that filters a database by a material that can be be passed
    into a template.
    Specifically this is required to generate the overview pages.
    Unfortunately, jinja does not allow such generic lambdas.
    """
    return lambda material: (
        lambda entry: entry.get_electrode("WE").material == material
    )


if __name__ in ["__main__", "<run_path>"]:
    main()
