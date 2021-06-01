# lexer for excalibur
from ply import lex

literals = [';','=','(',')','{','}']

tokens = [
          'PLUS','MINUS','TIMES','DIVIDE',
          'EQ','LE', 
          'INTEGER','ID','SCIENTIFIC','DECIMAL'
          ] 

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQ      = r'=='
t_LE      = r'<='

t_ignore = ' \t'

def t_SCIENTIFIC(t):
    r'[0-9]+\.[0-9]+X10e[0-9]+'
    return t

def t_DECIMAL(t): 
    r'[0-9]+\.[0-9]+'
    return t

def t_INTEGER(t):
    r'[0-9]+'
    return t

def t_ID(t):
    r'[a-z]+'
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)