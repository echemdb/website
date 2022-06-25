import os
import shutil

def copy_data(config, **kwargs):
    site_dir = config['site_dir']
    #shutil.copy('data/generated/svgdigitizer/alves_2011_electrochemistry_6010/alves_2011_electrochemistry_6010_f1a_solid.csv', os.path.join(site_dir, 'alves_2011_electrochemistry_6010_f1a_solid.csv'))
    shutil.copytree('data', os.path.join(site_dir, 'data'))