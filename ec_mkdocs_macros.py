from code.markdown_readwrite_gensites import get_table, get_periodic_table_span

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
