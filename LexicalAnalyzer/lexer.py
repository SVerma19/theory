from ply import lex

reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'not'   : 'NOT'
}

literals = [';','=','(',')','{','}']

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

t_ignore = ' \t' 

def t_INTEGER(t): 
    r'[0-9]+'
    return t

def t_DECIMAL(t):
    r'[0-9]\d*'
    return t

def t_ID(t): 
    r'[a-Z]+'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_SCIENTIFIC(t):
    r'[0-9]\*.[0-9]+([eE][-+][0-9]+)'
    return t

def t_COMMENT(t): 
    r'//'
    pass

def t_NEWLINE(t): 
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

#build the lexer
lexer = lex.lex(debug = 0)

data = '''
while(1){5;}
'''

if (__name__ == "__main__"):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break    
        print(tok)