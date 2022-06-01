r"""
Implements a `link` macro that renders links to internal pages.

EXAMPLES:

When manually creating a link, say to `directory/file`, we need to take into
account from where this link is created to decide whether a URL can be written
as `../directory/file` or `../../directory/file` and so on.

While one could use absolute URLs, absolute URLs do not work when deploying to
a subdirectory which sometimes is what we are doing in GitHub deployments.
"""
# ********************************************************************
#  This file is part of echemdb.
#
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

def create_link(env):
    import os.path

    path = env.globals["filename"]

    if path is None:
        raise NotImplementedError("cannot link when output name is not known")

    if not path.endswith(".md"):
        raise NotImplementedError(f"can only link from outputs written to .md files but this file is called {path}")

    path = path[:-3] + os.path.sep

    def link(*absolute):
        import os.path

        absolute = os.path.join(*absolute)

        absolute = absolute.replace('/', os.path.sep)

        relative = os.path.relpath(absolute, path)

        print(absolute, "became", relative, "in the context of", path)

        return relative.replace(os.path.sep, '/')

    return link
