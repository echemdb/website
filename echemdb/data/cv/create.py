r"""
Utilities to create datapackages for echemdb from datapackages (CSV and JSON), 
with svgdigitizer (SVG and YAML) or from raw files (CSV and YAML).

Also includes utilities to collect bibliography entries and store them
along with the generated datapackage.
"""

# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2022 Albert Engstfeld
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

def create_from_SVG(sourcedir=None, outdir=None, name=None, replace_files=False, sampling=.005):
    """
    Creates datapackages, consisting of a CSV and JSON, 
    from SVG (prepared with ``svgdigitizer``) and a YAML.
    Datapackages can be created from individual files or 
    all files in a specified folder.

    The default sourcedir is `./literature/svg/` in the basepath of echemdb.
    The default outdir is `./data/generated/svgdigitizer/` in the basepath of echemdb.

    `name` is the name of the folder of a specific file.
    
    """
    import os.path

    sourcedir = sourcedir or os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'literature',
        name or '')

    if not os.path.exists(sourcedir):
        raise ValueError(f"Could not find sourcedir {sourcedir}.")

    outdir = outdir or os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'generated',
        'svgdigitizer',
        name or '')

    # We now might have to digitize some files on demand. When running
    # tests in parallel, this introduces a race condition that we avoid
    # with a global lock in the file system.
    lockfile = f"{outdir}.lock"
    os.makedirs(os.path.dirname(lockfile), exist_ok=True)

    from filelock import FileLock
    with FileLock(lockfile):
        if not replace_files:
            if os.path.exists(outdir):
                raise Exception(f"The directory {outdir} exist. Delete the directory or force overwriting files by setting `replace_files=True`")

        from glob import glob
        for yaml in glob(os.path.join(sourcedir, "*.yaml")):
            svg = os.path.splitext(yaml)[0] + ".svg"

            from svgdigitizer.test.cli import invoke
            from svgdigitizer.__main__ import digitize_cv
            invoke(digitize_cv, "--sampling-interval", str(sampling), "--package", "--metadata", yaml, svg, "--outdir", outdir)

        assert os.path.exists(outdir), f"Ran digitizer to generate {outdir}. But directory is still missing after invoking digitizer."
        assert any(os.scandir(outdir)), f"Ran digitizer to generate {outdir}. But the directory generated is empty after invoking digitizer."

def copy_bibfiles(name, sourcedir=None, outdir=None):

    import os.path

    sourcedir = sourcedir or os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'literature',
        name or '')

    if not os.path.exists(sourcedir):
        raise ValueError(f"Could not find sourcedir {sourcedir}.")

    outdir = outdir or os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'generated',
        'svgdigitizer',
        name or '')

    source_bib_file = os.path.join(sourcedir, f"{name}.bib")
    
    from pathlib import Path
    
    target_bib_file = os.path.join(outdir, Path(source_bib_file).name)

    import shutil

    shutil.copyfile(source_bib_file, target_bib_file)