"""Hooks for local usage."""

import logging
import os
import shutil

import mkdocs.plugins

log = logging.getLogger("mkdocs")


@mkdocs.plugins.event_priority(-50)
def on_post_build(config):
    """Copy the data to the website folder."""
    site_dir = config["site_dir"]
    shutil.copytree("data", os.path.join(site_dir, "data"))
