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

import mkdocs_gen_files

import website.generator.database
from website.macros.render import render


def main():
    r"""
    Create MarkDown files in a virtual file system that is consumed by mkdocs
    when building the website.

    This function is invoked automatically by mkdocs during the build process.
    """

    database = website.generator.database.cv
    # Create a single page for each entry in the database
    for entry in database:
        with mkdocs_gen_files.open(
            os.path.join("cv", "entries", f"{entry.identifier}.md"), "w"
        ) as markdown:
            markdown.write(
                render(
                    "pages/cv_entry.md",
                    database=database,
                    entry=entry,
                )
            )
    # Create an overview page with tabulated and linked entries.
    with mkdocs_gen_files.open(os.path.join("cv", "index.md"), "w") as markdown:
        markdown.write(
            render(
                "pages/cv.md",
                database=database,
                # The overview page needs to filter the database by material.
                # Unfortunately, jinja does not allow such generic lambdas so we
                # need to pass the lambda that filters by a material into the
                # template from here.
                material_filter=lambda material: (
                    lambda entry: entry.system.electrodes.working_electrode.material
                    == material
                ),
            )
        )


if __name__ in ["__main__", "<run_path>"]:
    main()
