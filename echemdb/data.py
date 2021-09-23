import os.path

import hashlib

datadir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'literature'))

def collect_datapackages(data = datadir):
    # Collect all datapackage descriptors, see
    # https://specs.frictionlessdata.io/data-package/#metadata
    import os.path
    from glob import glob

    ##NH  Here we want to build the datapackages from literature data on the fly
    ## Note data could also be present already as datapackage.json or zip files
    descriptors = glob(os.path.join(data, '**', '*.json'), recursive=True)

    # Read the package descriptors (does not read the actual data CSVs)
    from datapackage import Package
    packages = [Package(descriptor) for descriptor in descriptors]

    return packages


def echemdb_id_from_descriptor(descriptor):
    '''
    We want to have a unique echemdb-id otherwise things look nasty
    Let's use material-surface-uniqueid

    e.g. namestr = descriptor['resources'][0]["name"] returns namestr = "briega-martos_2021_cation_XXX_p2_Fig1_Cs_2.3"
    then we can do
    '''
    namestr = descriptor['resources'][0]["name"]
    idend = hashlib.md5(namestr.encode()).hexdigest()[:7]
    mat = property_reader(descriptor, "electrode material")
    surf = property_reader(descriptor, "surface")

    return "-".join([mat, surf, idend])








def property_reader(descriptor, basic_property_name):
    """
    This function serves as a translation between basic property tags e.g.
    ['electrode material', 'surface', 'electrolyte', 'reference', 'echemdb-id', 'path', 'relpath']
    and how this is stored in datapackage descriptor

    ['electrode material', 'surface', 'electrolyte', 'reference', 'echemdb-id', 'path', 'relpath']


    """
    def _finditem(obj, key):
        if key in obj: return obj[key]
        for k, v in obj.items():
            if isinstance(v, dict):
                item = _finditem(v, key)
                if item is not None:
                    return item



    if basic_property_name == 'electrolyte':
        els = []
        for r in descriptor['electrochemical system']['electrolyte']['components']:
            els.append(r["name"])
        els.sort()
        response = ", ".join(els)
    elif basic_property_name == 'reference':
        response = descriptor["source"]["doi"]

    elif basic_property_name == 'echemdb-id':
        # question: should we have an echemdb_id, i think yes
        # I think we should have an algorithm that builds it from data in the descriptor e.g. hash
        response = echemdb_id_from_descriptor(descriptor)


    else:
        basicname_toyaml = {'electrode material': ["working electrode", "material"],
                            'surface': ["working electrode", "crystallographic orientation"]}

        r1 = _finditem(descriptor, basicname_toyaml[basic_property_name][0])
        response = _finditem(r1, basicname_toyaml[basic_property_name][1])
        if type(response) == dict:
            response = response['name']


    response = str(response)
    return response










def make_cvs_dataframe(packages, data = datadir):
    '''
    This is supposed to create a lightweight overview of the available data so we can autogenerate webpages, built on
    this logic
    ## Note: path will be the path to load the json dataframe e.g. for plotting
    ## But it will be also the path to download this might fail
    '''
    import pandas as pd



    data = [[
        property_reader(package.descriptor, 'electrode material'),
        property_reader(package.descriptor, 'surface'),
        property_reader(package.descriptor, 'electrolyte'),
        property_reader(package.descriptor, 'reference'),
        property_reader(package.descriptor, 'echemdb-id'),
        #f"{package.base_path}/{package.resource_names[0]}.json",
        f"literature/{os.path.relpath(package.base_path, datadir)}/{package.resource_names[0]}.json",
        f"{os.path.relpath(package.base_path, datadir)}/{package.resource_names[0]}.json",
    ] for package in packages]

    return pd.DataFrame(data, columns=['electrode material', 'surface', 'electrolyte', 'reference', 'echemdb-id', 'path', 'relpath'])
