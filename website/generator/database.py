r"""
Data packages and bibliography built from local data.

This module provides a (cached) database of CVs which is queried when building
the website. In principle, this is no different than calling ``Database()``
directly. However, this uses data from the local ``data`` directory and it also
caches this information in a global variable for improved performance during
the website build.

EXAMPLES::

    >>> from website.generator.database import cv
    >>> cv
    [...]

"""

# ********************************************************************
#  This file is part of echemdb-website.
#
#        Copyright (C) 2021-2024 Albert Engstfeld
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

from echemdb_ecdata.url import get_echemdb_database_url
from unitpackage.cv.cv_collection import CVCollection
from unitpackage.remote import collect_datapackages

packages = collect_datapackages(
    data=".", url=get_echemdb_database_url(), outdir="data/generated/"
)

cv = CVCollection(packages)
