import hashlib
import csv
import numpy as np
import pandas as pd
import requests, zipfile, io
import six
import tempfile
import os
from datapackage import Package
from datapackage.package import _validate_zip
import datapackage.package
import plotly.express as px
import plotly.graph_objects as go
import plotly.io
TEMPLATE_FOLDERS = {'elements': "./code/templates/element.md",
                    'echemdb_id': "./code/templates/echemdb_id.md",
                    'systems': "./code/templates/systems.md",
                    'surfaces': "./code/templates/surface.md",
                    'element_surface': "./code/templates/element_surface.md"
                    }

TARGET_FOLDERS = {'path': "./docs/",
                 'elements': "cv/elements/tobesubstituted.md",
                'element_surface': "cv/elements/tobesubstituted.md",
                 'echemdb_id': "cv/echemdb_pages/tobesubstituted.md",
                  'systems': "cv/systems.md",
                  'surfaces': "cv/surfaces/tobesubstituted.md"}


ELEMENTS_DATA = {
    "elements_data": "./elements.csv",
    "exp_cvs_index_csv": "./docs/cv/data/exp_cvs_index.csv"}

DISPLAYED_INFOS = ['electrode material', 'surface', 'electrolyte', 'reference', 'link', 'echemdb-id']


# MonkeyPatch
def _extract_zip_if_possible(descriptor):
    """If descriptor is a path to zip file extract and return (tempdir, descriptor)
    """
    tempdir = None
    result = descriptor
    try:
        if isinstance(descriptor, six.string_types):
            res = requests.get(descriptor)
            res.raise_for_status()
            result = res.content
    except (IOError,
            ValueError,
            requests.exceptions.RequestException):
        pass
    try:
        the_zip = result
        if isinstance(the_zip, bytes):
            try:
                if not os.path.isfile(the_zip): raise ValueError("not a file")
            except (TypeError, ValueError):
                # the_zip contains the zip file contents
                the_zip = io.BytesIO(the_zip)
        if zipfile.is_zipfile(the_zip):
            with zipfile.ZipFile(the_zip, 'r') as z:
                _validate_zip(z)
                descriptor_path = [
                    f for f in z.namelist() if f.endswith('datapackage.json')][0]
                tempdir = tempfile.mkdtemp('-datapackage')
                z.extractall(tempdir)
                result = os.path.join(tempdir, descriptor_path)
        else:
            result = descriptor
    except (TypeError,
            zipfile.BadZipfile):
        pass
    if hasattr(descriptor, 'seek'):
        # Rewind descriptor if it's a file, as we read it for testing if it's
        # a zip file
        descriptor.seek(0)
    return (tempdir, result)

#monkeypatch
datapackage.package._extract_zip_if_possible = _extract_zip_if_possible
#Now we can use Package(url_or_local_path)

def get_echemdb_id(elementname, filename):
    '''
    We start with hashes only containing the first 10 characters
    If we see problems we could move forward to 20 or more characters. Resulting ids would have the same first 10 character and so the ids should be also 'future-proof'
    :param elementname:
    :param filename:
    :return:
    '''
    echemdb_id = elementname + '-' + hashlib.md5(filename.encode('utf-8')).hexdigest()[:10]
    return echemdb_id


def collect_data_local(basefolder = '/'.join(ELEMENTS_DATA["exp_cvs_index_csv"].split('/')[:-1]), outfile= ELEMENTS_DATA["exp_cvs_index_csv"]):
    '''
    Let us agree that each experiment/single data is collected as datapackage. Meaning one
     experiment is one datapackage (one experiment is e.g. one single CV).
    We have to discuss whether we should package together data maybe when from the
    same publication ?
    :param basefolder: here is where the data lies
    :param outfile: this csv file will collect all the data we have, only including the most important metadata
    :return:
    '''
    return None


def datapackage_to_dataframe(datapkg):
    '''
    Generate directly pandas dataframe from firsr resource entry. Assumes tabular data.
    Should also work for remote resource path and for csv data as we assume here
    :param datapkg: datapackage object
    :return: pandas dataframe object
    '''
    # get resource to be updated
    res = datapkg.get_resource(datapkg.resource_names[0])
    # get resource data into pandas dataframe: This works for local and remote csv files
    df  = pd.read_csv(res.raw_iter(stream=False))
    return df


def get_plotly_plot(names, paths):
    alldfs = get_plot_data_from_paths(names, paths)
    fightml = make_plotly_figure_from_dataframes(alldfs)
    return fightml

def get_plot_data_from_paths(names, paths):
    if type(paths) == list:
        alldfs = []
        for name, path in zip(names, paths):
            print("path", path)
            datapkg = Package(path)
            # to be done
            metadata = None
            alldfs.append((name, datapackage_to_dataframe(datapkg), metadata))
    else:
        print("path", paths)
        datapkg = Package(paths)
        # to be done
        metadata = None
        alldfs = [(names, datapackage_to_dataframe(datapkg), metadata)]

    return alldfs

def make_plotly_figure_from_dataframes(alldfs):
    fig = go.Figure()

    for (descr, df, meta) in alldfs:

        fig.add_trace(go.Scatter( x= df['potential'], y =df['current'],  mode='lines', name=descr))
        fig.update_layout(template="simple_white",
                          showlegend=True,
                          autosize=True,
                          width=450,
                          height=350,
                          margin=dict(
                              l=70,
                              r=70,
                              b=70,
                              t=70,
                              pad=7
                          ),
                          # paper_bgcolor="LightSteelBlue",
                          )
    # to be done
    fig.update_xaxes(mirror="allticks", ticks="inside", title={'text': 'potential (V)'})
    fig.update_yaxes(mirror="allticks", ticks="inside",title={'text': 'current (mA)'}) #range=[0., 400],


    figstring = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script> \n \n '

    figstring += plotly.io.to_html(fig,include_plotlyjs=False, full_html=False)



    return figstring







#def build_datapackages_from_yamlandcsv(listofyaml)