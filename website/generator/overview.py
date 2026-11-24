r"""
Overview figure of the CV dataset.

The figure shows the CVs of single crystal metal electrodes recorded in aqueous
electrolytes arranged as in the periodic table of elements. Each panel shows
one example CV of a material and the number of CVs in the dataset for that
material. It is generated from the database each time the website is built,
so that the numbers follow the database version shown on the website.

The figure was originally created for the echemdb data descriptor in
*Scientific Data*.

EXAMPLES::

    >>> from website.generator.database import cv
    >>> png = periodic_table(cv)
    >>> png[:8] == b"\x89PNG\r\n\x1a\n"
    True

"""

# ********************************************************************
#  This file is part of echemdb-website.
#
#        Copyright (C) 2026 Albert Engstfeld
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
import hashlib
import io
import os.path

from matplotlib.figure import Figure

# Where the rendered figure is cached between builds (ignored by git).
CACHE = os.path.join(
    os.path.dirname(__file__), "..", "..", "generated", "cache", "overview"
)

# Groups 8 to 11 of the periods 4 to 6 of the periodic table.
MATERIALS = [
    ["Fe", "Co", "Ni", "Cu"],
    ["Ru", "Rh", "Pd", "Ag"],
    ["Os", "Ir", "Pt", "Au"],
]

# Low index surfaces. The order determines which CV is shown for a material.
ORIENTATIONS = ["111", "110", "100", "0001"]


def aqueous_entries(database):
    r"""
    Return the entries of `database` recorded in aqueous electrolytes on the
    low index surfaces of the materials in :data:`MATERIALS`, grouped by
    material.

    Within a material, base CVs (tag BCV) come first, then entries are sorted
    by the order of :data:`ORIENTATIONS` and otherwise keep the order of the
    database.

    EXAMPLES::

        >>> from website.generator.database import cv
        >>> entries = aqueous_entries(cv)
        >>> len(entries["Pt"]) > 0
        True
        >>> {entry.get_electrode("WE").material for entry in entries["Pt"]}
        {'Pt'}

    """
    materials = [material for row in MATERIALS for material in row]
    entries = {material: [] for material in materials}

    for entry in database:
        if entry.system.electrolyte.type != "aqueous":
            continue
        electrode = entry.get_electrode("WE")
        if electrode.material not in entries:
            continue
        if electrode.crystallographicOrientation not in ORIENTATIONS:
            continue
        entries[electrode.material].append(entry)

    for material in materials:
        entries[material].sort(
            key=lambda entry: (
                not _is_bcv(entry),
                ORIENTATIONS.index(
                    entry.get_electrode("WE").crystallographicOrientation
                ),
            )
        )

    return entries


def _is_bcv(entry):
    r"""
    Return whether `entry` is tagged as base CV.
    """
    try:
        return "BCV" in entry.experimental.tags
    except (KeyError, AttributeError):
        return False


def cached_periodic_table():
    r"""
    Return the overview figure of the complete database as PNG.

    The figure is always created from the complete database, also when the
    entries are limited for fast builds. It is cached in ``generated/cache``
    and only recreated when the database URL or this module changes.

    EXAMPLES::

        >>> png = cached_periodic_table()
        >>> png == cached_periodic_table()
        True

    """
    from website.generator.database import (
        ECHEMDB_DATABASE_URL,
        ECHEMDB_DATABASE_VERSION,
    )

    with open(__file__, "rb") as source:
        key = hashlib.sha1(
            ECHEMDB_DATABASE_URL.encode("utf-8") + source.read()
        ).hexdigest()[:12]

    path = os.path.join(CACHE, f"cv_overview_{ECHEMDB_DATABASE_VERSION}_{key}.png")

    if not os.path.exists(path):
        from website.generator.database import cv_all

        os.makedirs(CACHE, exist_ok=True)
        with open(path, "wb") as png:
            png.write(periodic_table(cv_all))

    with open(path, "rb") as png:
        return png.read()


def periodic_table(database, dpi=200):
    r"""
    Return the overview figure for `database` as PNG.

    Each panel shows the first CV of a material in :func:`aqueous_entries`
    and the number ``n`` of such CVs in the database.
    """
    entries = aqueous_entries(database)

    figure = Figure(figsize=(9, 6), facecolor="white")
    axes = figure.subplots(len(MATERIALS), len(MATERIALS[0]))

    for row, materials in enumerate(MATERIALS):
        for column, material in enumerate(materials):
            ax = axes[row][column]

            if entries[material]:
                entry = entries[material][0]
                y = "j" if "j" in entry.resource.schema.field_names else "I"
                entry.df.plot("E", y, ax=ax, legend=False)

            ax.text(
                0.03,
                0.97,
                f"{material} (n={len(entries[material])})",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=11,
                bbox={
                    "facecolor": "white",
                    "alpha": 0.7,
                    "edgecolor": "none",
                    "pad": 1.5,
                },
            )
            ax.set_xlabel("")
            ax.set_ylabel("")
            ax.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    figure.supxlabel("E (a.u.)", fontsize=12)
    figure.supylabel("j (a.u.)", fontsize=12)
    figure.subplots_adjust(
        wspace=0, hspace=0, top=0.98, bottom=0.07, left=0.05, right=0.98
    )

    png = io.BytesIO()
    figure.savefig(png, format="png", dpi=dpi)
    return png.getvalue()
