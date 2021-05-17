from .markdown_pieces import get_table, get_periodic_table_span, sometest
from .make_pages import get_element_page_contents, create_element_pages, get_systems_page_contents, create_systems_pages, get_echemdb_id_page_contents, create_echemdb_id_pages, get_element_surface_page_contents, create_element_surface_pages #get_surface_page_contents, create_surface_pages

from .build_data import ELEMENTS_DATA
import pandas as pd
from .data import collect_datapackages, make_cvs_dataframe

allele_data = make_cvs_dataframe(collect_datapackages())

ag  = allele_data.groupby(by = ['electrode material', 'surface'])

def create_pages():
    create_systems_pages()

    for elementname in list(set(allele_data['electrode material'].values)):
        create_element_pages(elementname)
    #for surfacename in list(set(allele_data['surface'].values)):
    #    create_surface_pages(surfacename)
    for echemdb_id in list(set(allele_data['echemdb-id'].values)):
        create_echemdb_id_pages(echemdb_id)

    for tupled in ag.groups:
        create_element_surface_pages(tupled[0], tupled[1])
        #subdf  = ag.get_group(tupled)


def define_env(env):
    # you could, of course, also define a macro here:
    @env.macro
    def test(s:str):
        return sometest(s)

    @env.macro
    def table_from_csv(csvfile):
        return get_table(csvfile)

    @env.macro
    def periodic_table():
        return get_periodic_table_span()
        #return get_periodic_table()

    @env.macro
    def make_element_page(elementname):
        return get_element_page_contents(elementname)

    #@env.macro
    #def make_surface_page(surfacename):
    #    return get_surface_page_contents(surfacename)

    @env.macro
    def make_systems_page():
        return get_systems_page_contents()
    @env.macro
    def make_element_surface_page(elementname, surfacename):
        return get_element_surface_page_contents(elementname, surfacename)

    @env.macro
    def make_echemdb_id_page(echemdb_id):
        return get_echemdb_id_page_contents(echemdb_id)
