r"""
Downloadable zip archives of the entries in the database.

EXAMPLES::

    >>> import io
    >>> import zipfile
    >>> from website.generator.database import cv
    >>> from website.generator.datapackage import datapackage_zip
    >>> entry = cv["alves_2011_electrochemistry_6010_f1a_solid"]
    >>> archive = zipfile.ZipFile(io.BytesIO(datapackage_zip(entry)))
    >>> archive.namelist()
    ['LICENSE.md', 'README.md', 'alves_2011_electrochemistry_6010_f1a_solid.csv', 'alves_2011_electrochemistry_6010_f1a_solid.json']

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

import io
import os.path
import tempfile
import zipfile

from website.generator.database import ECHEMDB_DATABASE_VERSION
from website.macros.render import render


def datapackage_zip(entry):
    r"""
    Return the bytes of a zip archive containing the Data Package of `entry`,
    i.e., its CSV and JSON file, together with a README and a LICENSE.

    EXAMPLES::

        >>> import io
        >>> import zipfile
        >>> from website.generator.database import cv
        >>> archive = zipfile.ZipFile(io.BytesIO(datapackage_zip(cv[0])))
        >>> "Entry.from_local" in archive.read("README.md").decode("utf-8")
        True
        >>> "CC-BY-4.0" in archive.read("LICENSE.md").decode("utf-8")
        True

    """
    with tempfile.TemporaryDirectory() as outdir:
        entry.save(outdir=outdir)

        for name, template in [
            ("README.md", "datapackage/README.md"),
            ("LICENSE.md", "datapackage/LICENSE.md"),
        ]:
            with open(os.path.join(outdir, name), "w", encoding="utf-8") as file:
                file.write(
                    render(
                        template,
                        entry=entry,
                        version=ECHEMDB_DATABASE_VERSION,
                    )
                )

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(os.listdir(outdir)):
                archive.write(os.path.join(outdir, name), arcname=name)

    return buffer.getvalue()
