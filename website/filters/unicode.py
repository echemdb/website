r"""
Renders LaTeX markup as unicode characters.

EXAMPLES::

    >>> from website.macros.render import render
    >>> from io import StringIO
    >>> snippet = StringIO("{{ value | unicode }}")
    >>> render(snippet, value=r"Gl{\"o}ckner")
    'Glöckner'

"""
# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2022 Albert Engstfeld
#        Copyright (C) 2022 Julian Rüth
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


def unicode(value):
    r"""
    Return ``value`` rendered in unicode characters.

    EXAMPLES::

        >>> unicode(r'Gl{\"o}ckner')
        'Glöckner'

    """
    from pylatexenc.latex2text import LatexNodes2Text

    return LatexNodes2Text().latex_to_text(value)
