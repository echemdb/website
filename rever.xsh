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

# Check that we are on the main branch
branch=$(git branch --show-current)
if branch.strip() != "main":
  raise Exception("You must be on the main branch to release.")
# and that it is up to date with origin/main
git fetch https://github.com/echemdb/website.git
git reset FETCH_HEAD
git diff --exit-code
git diff --cached --exit-code

$PROJECT = 'website'

# Pushing the tag triggers the Build workflow, which publishes the website
# to GitHub Pages. No package is uploaded anywhere.
$ACTIVITIES = [
    'version_bump',
    'changelog',
    'tag',
    'push_tag',
    'ghrelease',
]

$VERSION_BUMP_PATTERNS = [
    ('pyproject.toml', r'version =', 'version = "$VERSION"'),
]

$CHANGELOG_FILENAME = 'ChangeLog'
$CHANGELOG_TEMPLATE = 'TEMPLATE.rst'
$CHANGELOG_NEWS = 'news'
$PUSH_TAG_REMOTE = 'git@github.com:echemdb/website.git'

$GITHUB_ORG = 'echemdb'
$GITHUB_REPO = 'website'

$CHANGELOG_CATEGORIES = ('Added', 'Changed', 'Deprecated', 'Removed', 'Fixed', 'Performance')
