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

from unitpackage.database.echemdb import Echemdb

ECHEMDB_DATABASE_VERSION = "0.9.1"

ECHEMDB_DATABASE_URL = os.environ.get(
    "ECHEMDB_DATABASE_URL",
    f"https://github.com/echemdb/electrochemistry-data/releases/download/{ECHEMDB_DATABASE_VERSION}/data-{ECHEMDB_DATABASE_VERSION}.zip",
)

cv = Echemdb.from_remote(url=ECHEMDB_DATABASE_URL)

# Limit the number of entries per experimental tag (BCV, COOR, ...) and
# electrolyte type (aqueous, ionic liquid, ...) for fast local test builds
# where all overview pages contain at least some entries,
# e.g., `pixi run doc-fast` or `pixi run preview-fast`.
ECHEMDB_WEBSITE_MAX_ENTRIES = os.environ.get("ECHEMDB_WEBSITE_MAX_ENTRIES")


def _limit_per_group(database, max_entries):
    r"""
    Return a sub-collection of `database` containing at most `max_entries`
    entries for each experimental tag and each electrolyte type.
    """
    counts = {}
    identifiers = []
    for entry in database:
        try:
            groups = set(entry.experimental.tags)
        except (KeyError, AttributeError):
            groups = set()
        try:
            groups.add(entry.system.electrolyte.type)
        except (KeyError, AttributeError):
            pass
        if any(counts.get(group, 0) < max_entries for group in groups):
            identifiers.append(entry.identifier)
            for group in groups:
                counts[group] = counts.get(group, 0) + 1
    return database[identifiers]


if ECHEMDB_WEBSITE_MAX_ENTRIES:
    cv = _limit_per_group(cv, int(ECHEMDB_WEBSITE_MAX_ENTRIES))
