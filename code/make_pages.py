import os
import os.path

from mdutils.mdutils import MdUtils
from .build_data import TEMPLATE_FOLDERS, ELEMENTS_DATA, TARGET_FOLDERS, DISPLAYED_INFOS, get_plotly_plot


import frontmatter
import markdown
import pandas as pd
import numpy as np
import copy

ej = ELEMENTS_DATA["exp_cvs_index_csv"]
cv_data = pd.read_csv(ej)
grouped_cv_data = cv_data.groupby(by=['electrode material', 'surface'])


def get_filtered_tables(elementname, surface=None):

    ele_data = cv_data.loc[(cv_data['electrode material'] == elementname)]
    if surface != None:
        tupled = (elementname, surface)
        ele_data = grouped_cv_data.get_group(tupled)

    ele_data = create_nice_table_overview(ele_data)
    ele_data = ele_data[ DISPLAYED_INFOS  ]
    ele_list_md_str = ele_data.to_markdown(index=False)

    return ele_list_md_str







#### Single Page contents ####
def get_echemdb_id_page_contents(echemdb_id):
    '''
    builds the page for a single CV measurement
    echemdb_id needs to classify these correctly
    I prefer to use a hash-like id, or some number
    but then we need a database that stores how something relates to something. A 'protected' csv file that gathers the
    things would as well be sufficient. Let's assume we have everything in a csv file.
    It would make sense just to take the index of the csv file.
    Note, we should then not ever 'automatically' create that csv file
    as then the ids would change.
    I think that it makes sense that we have associated with each data
    I will use hashes because i dont want to
    hashlib.md5(string.encode('utf-8'))).hexdigest()[:10]
    :param echemdb_id:
    :return:
    '''



def get_echemdb_id_file(echemdb_id):
    target = copy.deepcopy(TARGET_FOLDERS['echemdb_id']).replace('tobesubstituted', echemdb_id)
    targetfile = target
    return targetfile.split('.md')[0]

def get_element_file(elementname):
    target = copy.deepcopy(TARGET_FOLDERS['elements']).replace('tobesubstituted', elementname)
    targetfile = target
    return targetfile.split('.md')[0]

def get_element_surface_file(elementname, surfacename):
    target = copy.deepcopy(TARGET_FOLDERS['element_surface']).replace('tobesubstituted', f'{elementname}-{surfacename}')
    targetfile = target
    return targetfile.split('.md')[0]

def get_page_links( property_propertyvals_dict ):
    if len(property_propertyvals_dict.keys()) == 2:
        elementname, surfacename = property_propertyvals_dict['elementname'], property_propertyvals_dict['surfacename']
        filename = get_element_surface_file(elementname, surfacename)
        ln = f'{elementname}({surfacename})'
    else:
        try:
            elementname = property_propertyvals_dict['elementname']
            filename = get_element_file(elementname)
            ln = f'{elementname}'
        except:
            echemdb_id = property_propertyvals_dict['echemdb_id']
            filename = get_echemdb_id_file(echemdb_id)
            ln = f'{echemdb_id}'

    return f'[{ln}](../../../{filename})'




def create_nice_table_overview(df):
    '''
    return a nicer dataframe for direct table creation
    ### AHHH, links need to be relative to current location what a fuck up
    :param df:
    :return:
    '''

    dfc = df.copy()
    dfc['link'] = dfc['path'].apply(lambda path: f'[:material-file-download:]({path})')
    ### AHHH, links need to be relative to current location what a fuck up
    dfc['echemdb-id'] = dfc['echemdb-id'].apply(lambda echemdb_id: f'[{echemdb_id}](../../../{get_echemdb_id_file(echemdb_id)})')
    # reference????
    return dfc



#### Element Page creation, basic copy paste md template ####
def create_element_pages(elementname):
    print(f"Creating {elementname} page")
    with open(TEMPLATE_FOLDERS['elements']) as f:
        templatemd = frontmatter.load(f)
    templatemd['data']['element'] = elementname
    templatemd['title'] = 'echemdb - {} CV data'.format(elementname)

    target = copy.deepcopy(TARGET_FOLDERS['elements']).replace('tobesubstituted', elementname)
    targetfile = TARGET_FOLDERS['path'] + target
    os.makedirs(os.path.dirname(targetfile), exist_ok=True)
    with open(targetfile, 'w') as f:
        frontmatter.dump(templatemd, targetfile)

#### Systems Page creation ####
def create_systems_pages():
    print(f"Creating systems page")
    with open(TEMPLATE_FOLDERS['systems']) as f:
        templatemd = frontmatter.load(f)

    target = copy.deepcopy(TARGET_FOLDERS['systems'])
    targetfile = TARGET_FOLDERS['path'] + target
    os.makedirs(os.path.dirname(targetfile), exist_ok=True)
    with open(targetfile, 'w') as f:
        frontmatter.dump(templatemd, targetfile)

#### Element Surface Page creation ####
def create_element_surface_pages(elementname, surfacename):
    print(f"Creating {elementname}  {surfacename} page")
    with open(TEMPLATE_FOLDERS['element_surface']) as f:
        templatemd = frontmatter.load(f)
    templatemd['data']['element'] = elementname
    templatemd['data']['surface'] = surfacename
    templatemd['title'] = f'echemdb - {elementname} {surfacename} surfaces CV data'

    target = copy.deepcopy(TARGET_FOLDERS['elements']).replace('tobesubstituted', f'{elementname}-{surfacename}')
    targetfile = TARGET_FOLDERS['path'] + target
    os.makedirs(os.path.dirname(targetfile), exist_ok=True)
    with open(targetfile, 'w') as f:
        frontmatter.dump(templatemd, targetfile)



#### echemdb-id Page creation ####
def create_echemdb_id_pages(echemdb_id):
    print(f"Creating {echemdb_id} page")
    with open(TEMPLATE_FOLDERS['echemdb_id']) as f:
        templatemd = frontmatter.load(f)
    templatemd['data']['echemdb_id'] = echemdb_id
    templatemd['title'] = 'echemdb - {} CV data'.format(echemdb_id)

    target = copy.deepcopy(TARGET_FOLDERS['echemdb_id']).replace('tobesubstituted', echemdb_id)
    targetfile = TARGET_FOLDERS['path'] + target
    os.makedirs(os.path.dirname(targetfile), exist_ok=True)
    with open(targetfile, 'w') as f:
        frontmatter.dump(templatemd, targetfile)



#### Content Creation ####

#### Element Page contents ####
def get_element_page_contents(elementname):
    '''
    creates the contents in markdown for the elements pages

    :param elementname:
    :return: Whatever we want to write/plot for the element

    '''
    ej = ELEMENTS_DATA["elements_data"]

    head = "# {}".format(elementname)
    page_md = [head]

    page_md += ["## Elemental properties"]
    allele_data = pd.read_csv(ej)
    ele_data = allele_data.loc[(allele_data['symbol'] == elementname)]
    ele_data = ele_data[['symbol', 'name', 'atomic mass', 'melting point']]
    ele_properties_md_str = ele_data.to_markdown(index=False)

    page_md += [ele_properties_md_str, ' ']
    page_md += ["## Surface specific CVs"]


    for t in [ tupled for tupled in grouped_cv_data.groups if tupled[0] == elementname]:
        link  = get_page_links({'elementname':t[0], 'surfacename':t[1]})
        local_page_content = f'??? example ' + f'"{link}" \n    '  #+ f'"{t[0]}-{t[1]}" \n    '
        #local_page_content += f'### {link} '  + '\n    '
        ele_list_md_str = get_filtered_tables(t[0], surface=t[1]) # here we could leave away surface, filter differently
        local_page_content += '\n    '.join(ele_list_md_str.split('\n'))
        #local_page_content += '\n    asdfasdfasdfa'
        #print(local_page_content)

        page_md += [local_page_content, '\n ']


    page_md += ["## All experimental CVs"]

    ele_list_md_str = get_filtered_tables(elementname, surface=None)

    page_md += [ele_list_md_str, ' ']
    

    page_md = '\n'.join(page_md)

    return page_md



#### Element surface Page contents ####
def get_element_surface_page_contents(elementname, surfacename):
    '''
    creates the contents in markdown for the elements pages

    :param elementname:
    :return: Whatever we want to write/plot for the element

    '''

    head = f"# {elementname}({surfacename})"
    page_md = [head]

    page_md += ["## Available experimental CVs"]

    ele_list_md_str = get_filtered_tables(elementname, surface=surfacename)

    page_md += [ele_list_md_str, ' ']

    page_md += ["## Plots \n "]

    tupled = (elementname, surfacename)
    ele_data = grouped_cv_data.get_group(tupled)
    #print('ele_data', ele_data.columns)

    paths = ele_data['path'].values
    echemdb_ids = ele_data['echemdb-id'].values
    pl = paths.tolist()
    ech = echemdb_ids.tolist()
    print(pl,ech)
    page_md += [get_plotly_plot(ech, pl)]

    page_md = '\n'.join(page_md)


    return page_md


#### systems contents ####
def get_systems_page_contents():
    '''

    :return:
    '''

    page_md = ["# All available experimental CVs"]

    ele_data = create_nice_table_overview(cv_data)
    ele_data = ele_data[ DISPLAYED_INFOS  ]

    ele_list_md_str = ele_data.to_markdown(index=False)


    page_md += [ele_list_md_str, ' ']
    

    page_md = '\n'.join(page_md)

    return page_md






#### echembd_id contents ####
def get_echembd_id_page_contents(echembd_id):
    '''
    creates the contents in markdown for the elements pages

    :param elementname:
    :return: Whatever we want to write/plot for the element

    '''

    head = "# {}".format(echembd_id)
    page_md = [head]

    page_md += ["## Experimental setup"]

    ele_data = cv_data.loc[(cv_data['echemdb-id'] == echembd_id)]
    ele_data = ele_data[['electrode material', 'surface', 'electrolyte' ]] # maybe more
    ele_list_md_str = ele_data.to_markdown(index=False)

    page_md += [ele_list_md_str, ' ']

    page_md += ["## Experimental results \n"]
    # Now read Datapackage and do something with it e.g. plot

    ele_data = cv_data.loc[(cv_data['echemdb-id'] == echembd_id)]
    path = ele_data['path'].values[0]
    print("datain", ele_data , path)
    page_md += [get_plotly_plot(str(echembd_id), path)]

    page_md = '\n'.join(page_md)

    return page_md
