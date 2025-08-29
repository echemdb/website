r"""
Data packages and bibliography built from local data.

This module provides a (cached) database of CVs which is queried when building
the website. In principle, this is no different than calling ``CVDatabase.from_remote()``
directly. The data is cached in a global variable for improved performance during
the website build.

EXAMPLES::

    >>> from website.generator.database import cv
    >>> cv
    [...]

"""

# ********************************************************************
#  This file is part of echemdb-website.
#
#        Copyright (C) 2021-2025 Albert Engstfeld
#        Copyright (C)      2021 Johannes Hermann
#        Copyright (C) 2021-2022 Julian Rüth
#        Copyright (C)      2021 Nicolas Hörmann
#
#  echemdb-website is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  echemdb-website is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with echemdb-website. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************
import os

from mkdocs.config import load_config
from unitpackage.database.echemdb import Echemdb

config = load_config("mkdocs.yml")

ECHEMDB_DATABASE_URL = os.environ.get(
    "ECHEMDB_DATABASE_URL",
    "https://github.com/echemdb/electrochemistry-data/releases/download/0.5.1/data-0.5.1.zip",
)

cv = Echemdb.from_remote(url=ECHEMDB_DATABASE_URL)
cv.save_entries(outdir=os.path.join(config["site_dir"], "data"))
