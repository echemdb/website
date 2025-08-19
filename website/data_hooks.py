"""Hooks for local usage."""

import logging
import os
import shutil
import io
import zipfile

import requests

import mkdocs.plugins

log = logging.getLogger("mkdocs")

ECHEMDB_DATABASE_URL = os.environ.get(
    "ECHEMDB_DATABASE_URL",
    "https://github.com/echemdb/electrochemistry-data/releases/download/0.5.0/data-0.5.0.zip",
)

@mkdocs.plugins.event_priority(-50)
def on_post_build(config):
    """Download electrochemistry-data and extract to the website folder."""
    url = ECHEMDB_DATABASE_URL
    resp = requests.get(url)
    buf = io.BytesIO(resp.content)
    site_dir = config["site_dir"]   
    with zipfile.ZipFile(buf) as zf:
        zf.extractall(site_dir)
