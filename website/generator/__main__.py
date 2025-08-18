r"""
Create generated pages for the website.

This module is invoked by the `mkdocs-gen-files module
<https://oprypin.github.io/mkdocs-gen-files/>` to generate pages such as the
individual pages for each entry in the database.
"""

# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2021-2022 Albert Engstfeld
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

import website.generator.database
from website.macros.render import render


def main():
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
                intro="",
                material_filter=material_filter(),
            )
        )
    t_aqueous = time.time() - t_aqueous_start
    print(f"Generated aqueous overview page in {t_aqueous:.2f} seconds")

    # Create an overview page with tabulated and linked entries for all systems to compare.
    with mkdocs_gen_files.open(os.path.join("cv", "compare.md"), "w") as markdown:
        markdown.write(
            render(
                "pages/compare.md",
                database=database,
                intro="Cyclic voltammograms to compare.",
                material_filter=material_filter(),
            )
        )

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
                intro="Cyclic voltammograms recorded in CO containing aqueous electrolytes.",
                material_filter=material_filter(),
            )
        )
    t_coor = time.time() - t_coor_start
    print(f"Generated COOR overview page in {t_coor:.2f} seconds")
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
                intro="Cyclic voltammograms recorded in ionic liquids.",
                material_filter=material_filter(),
            )
        )

    t_ionic_liquid = time.time() - t_ionic_liquid_start
    print(f"Generated ionic liquid overview page in {t_ionic_liquid:.2f} seconds")



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
