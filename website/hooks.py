"""Hooks for local usage."""
import os
import shutil

def copy_data(config):
    """Copy the data to the website folder."""
    site_dir = config['site_dir']
    shutil.copytree('data', os.path.join(site_dir, 'data'))
