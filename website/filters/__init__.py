r"""
Provides custom Jinja filters for rendering the echemdb websites.
"""
# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C)      2021 Albert Engstfeld
#        Copyright (C)      2021 Johannes Hermann
#        Copyright (C) 2021-2022 Julian Rüth
#        Copyright (C)      2021 Nicolas Hörmann
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


def enable_filters(env):
    r"""
    Register filters for use in mkdocs.

    EXAMPLES:

    This registers ``render`` as a filter::

        >>> from website.macros.render import render
        >>> from io import StringIO
        >>> from astropy.units import Unit

        >>> snippet = StringIO("{{ value | render('components/quantity.md') }}")
        >>> render(snippet, value={'quantity': 1 * Unit("mol / l")})
        '1 M'

    """
    from website.filters.render import render
    from website.filters.unicode import unicode
    from base64 import b64encode

    env.filters["render"] = render
    env.filters["unicode"] = unicode
    env.filters["b64encode"] = lambda value: b64encode(value).decode('utf-8')
