import ply.lex as lex
import sys

reserved_words = (
    'while', 'for', 'print' #Loops and conditions
)

reserved_forms = (
    'line', 'text', 'ellipse', 'rectangle'
)


reserved_params = (
    'pos',
    'width',
    'color',
    'linecolor',
    'fontsize',
    'word'
)
    
reserved_colors = (
    'white', 'black', 'red', 'blue',
    'yellow', 'green', 'pink', 'purple',
    'maroon', 'orange', 'lime'
)

tokens = ('NUMBER', 'ADD_OP', 'MUL_OP',
          'STRING', 'IDENTIFIER', 'FORMS',
          'IDPARAMS', 'COLORPARAMS', 'COMP',
          'EQUALS', 'LESSTHAN','GREATTHAN','NOTEQUAL',)\
         + tuple(map(lambda s:s.upper(), reserved_words)) \
         + tuple(map(lambda s:s.upper(), reserved_params)) \
         + tuple(map(lambda s:s.upper(), reserved_colors))

t_ignore = ' \t'

literals = '(){};=,:'

def t_ADD_OP(t):
    r'[+-]'
    return t

def t_MUL_OP(t):
    r'[*/]'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # [1:-1] enlève les guillemets de la string
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_words:
        #t.type = 'IDENTIFIER'
        t.type = t.value.upper()
    elif t.value in reserved_params:
        t.type = 'IDPARAMS'
        #t.type = t.value.upper()
    elif t.value in reserved_forms:
        t.type = 'FORMS'
        #t.type = t.value.upper()
    elif t.value in reserved_colors:
        t.type = 'COLORPARAMS'
        #t.type = t.value.upper()
    return t

def t_COMP(t):
    r'(<|>)'
    return t

def t_EQUALS(t):
    r'=='
    return t
    
def t_NOTEQUAL(t):
    r'=\!'
    return t

def t_LESSTHAN(t):
    r'=<'
    return t

def t_GREATTHAN(t):
    r'=>'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)
    
lex.lex()
    
if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        filename = "ExempleBoucle.txt"

    prog = open(filename).read()

    lex.input(prog)
    while 1:
        tok = lex.token()
        if not tok:
            print("No token")
            break
        print("line %d: %s(%s)" %(tok.lineno, tok.type, tok.value))