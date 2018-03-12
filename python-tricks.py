# A pretty interactive console with access to the scope, for awesome debugging:

def code_i_want_to_debug(a, b):
    x = 47*a + b
    
    from ptpython.repl import embed
    embed(globals(), locals())  # has access to all the variables

    
# Use a README.md but convert to rst when uploading to PyPI

# install pypandoc, then put this in setup.py:
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print('warning: pypandoc module not found, could not convert Markdown to RST')
    read_md = lambda f: open(f, 'r').read()
# then use e.g. `long_description=read_md('README.md')`
