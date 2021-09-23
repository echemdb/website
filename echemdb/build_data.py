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
TEMPLATE_FOLDERS = {'elements': "./templates/element.md",
                    'echemdb_id': "./templates/echemdb_id.md",
                    'systems': "./templates/systems.md",
                    'surfaces': "./templates/surface.md",
                    'element_surface': "./templates/element_surface.md"
                    }

TARGET_FOLDERS = {'path': "./docs/",
                 'elements': "cv/elements/tobesubstituted.md",
                'element_surface': "elements/tobesubstituted.md",
                 'echemdb_id': "cv/echemdb_pages/tobesubstituted.md",
                  'systems': "cv/systems.md",
                  'surfaces': "cv/surfaces/tobesubstituted.md"}


ELEMENTS_DATA = {
    "elements_data": "./elements.csv"
}

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

def datapackage_to_dataframe(datapkg):
    '''
    Generate directly pandas dataframe from firsr resource entry. Assumes tabular data.
    Should also work for remote resource path and for csv data as we assume here
    Note the datapackage can be created only from the json, if csv is in correct path and in ressources
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
            datapkg = Package(path)
            # to be done
            metadata = datapkg.descriptor
            alldfs.append((name, datapackage_to_dataframe(datapkg), metadata))
    else:
        print(paths)
        datapkg = Package(paths)
        # to be done
        metadata = datapkg.descriptor
        alldfs = [(names, datapackage_to_dataframe(datapkg), metadata)]

    return alldfs

def make_plotly_figure_from_dataframes(alldfs):
    '''
    If we want to plot different things on top of each other, it makes no sense to have all different units etc
    so we need to update that code:
    first standardize data, then plot.
    As a result it also makes no sense to read out metadata always for axis labels
    For the moment I read out, but I think it is wrong when digitized

        "figure description": {
        "type": "digitized",
        "measurement type": "CV",
        "scan rate": {
            "value": 50.0,
            "unit": "mV / s"
        },
        "potential scale": {
            "unit": "V",
            "reference": "SHE"
        },
        "current": {
            "unit": "uA / cm2"
        },
        "comment": ""
    },




    '''


    # homogenize data ....

    u = alldfs[0][-1]["figure description"]["potential scale"]
    j = alldfs[0][-1]["figure description"]["current"]



    fig = go.Figure()


    for (descr, df, meta) in alldfs:

        fig.add_trace(go.Scatter( x= df['U'], y =df['j'],  mode='lines', name=descr))
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
    fig.update_xaxes(mirror="allticks", ticks="inside", title={'text': f'E vs {u["reference"]} [{u["unit"]}]'})
    fig.update_yaxes(mirror="allticks", ticks="inside",title={'text': f'j [{j["unit"]}]'}) #range=[0., 400],


    figstring = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script> \n \n '

    figstring += plotly.io.to_html(fig,include_plotlyjs=False, full_html=False)



    return figstring







#def build_datapackages_from_yamlandcsv(listofyaml)
