# Lexer for xcalibur
from ply import lex

reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'not'   : 'NOT'
}

literals = [';','=','(',')','{','}'] #literals used in the language

tokens = [
          'PLUS','MINUS','TIMES','DIVIDE',
          'EQ','LE', 
          'INTEGER','ID','DECIMAL'
          ] + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQ      = r'=='
t_LE      = r'<='

t_ignore = ' \t'#ignore these characters from input
def t_SCIENTIFIC(t):
    r'scientific'
    return t
    
def t_ID(t):
    r'id'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_DECIMAL(t): #write decimal number token definition
    r'decimal'
    return t

def t_INTEGER(t):#write integer token definition
    r'integer'
    return t

def t_COMMENT(t):#write comment token definition. comments are denoted by //
    r'comment'
    pass

def t_NEWLINE(t):# this is already completed for you
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)

data = '''
while(1){5;}
'''

if (__name__ == "__main__"):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)