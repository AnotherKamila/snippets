# A pretty interactive console with access to the scope, for awesome debugging:

def code_i_want_to_debug(a, b):
    x = 47*a + b
    
    from ptpython.repl import embed
    embed(globals(), locals())  # has access to all the variables
