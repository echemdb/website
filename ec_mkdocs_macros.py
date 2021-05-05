from mdutils.mdutils import MdUtils
import pandas as pd, numpy as np
from matplotlib.cm import jet_r
from matplotlib import colors
#NH: Seems there are problems with code import. cant be found with github pages mkdocs build
# from code.markdown_readwrite_gensites import get_table, get_periodic_table_span

def get_table(filename):
    mdFile = MdUtils(file_name='Example_Markdown', title='Markdown File Example')
    if filename.split(".")[-1] == 'csv':
        columns, rows, text =  shapedlistfrom_csv(filename)
        return mdFile.new_table(columns, rows, text, text_align='center', marker='')  # text is flattened array

def shapedlistfrom_csv(filename):
    df = pd.read_csv(filename)
    rows, columns = df.shape
    rows+=1
    listed = df.columns.tolist()
    for r in df.iterrows():
        listed.extend(r[1].astype(str).tolist())
    return columns, rows, listed


def shapedlistfrom_json(filename):
    return None


def make_element_link(elementname):
    return '[**{}**]'.format(elementname) + '(  # )'

def make_span(elementname, elecolor):
    return '<span class="a" style="background-color:{}"> '.format(elecolor)  + make_element_link(elementname) + ' </span>'


def get_normed_colormap(inarray):
    norm = colors.Normalize(inarray.min(), inarray.max())
    jj = jet_r(norm(inarray))

    cl = [ colors.to_hex(c) for c in jj]
    return cl




def get_periodic_table_span():
    edata = './elements.csv'
    df = pd.read_csv(edata)
    columns = 18
    rows = 6
    table_list = [ '<span class="b"> </span>' for i in range(columns*rows)]

    arr = df.electronegativity.values
    arr = np.nan_to_num(arr)
    nch = get_normed_colormap(arr)
    count=0

    for d in df.iterrows():
        count +=1
        color = nch[count-1]
        data = d[1]
        per = d[1]['period']
        gr = d[1]['group']
        element = d[1]['symbol']
        if per != "La":
            x, y = int(gr) -1, int(per)-1
            pos = y*18 + x

            table_list[pos] = make_span(element, color)

    outer = '<div markdown = "1" style="width: 40rem">'
    for r in range(rows):
        for c in range(columns):
            pos = r * 18 + c
            outer += '\n' + table_list[pos]
        outer += '\n'

    outer += '</div>'

    return outer





def define_env(env):
    # you could, of course, also define a macro here:
    @env.macro
    def test(s:str):
        ns = '| A | B '  \
             '| \n | ------- | ----------- ' \
             '| \n | H  | T       ' \
             '| \n | P  | T       |'

        return ns

    @env.macro
    def table_from_csv(csvfile):
        return get_table(csvfile)

    @env.macro
    def periodic_table():
        return get_periodic_table_span()
        #return get_periodic_table()
