# Lexer for excalibur

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

def t_DECIMAL(t): #write decimal number token definition
    r'[0-9]+\.[0-9]+'
    return t

def t_INTEGER(t):#write integer token definition
    r'[0-9]+'
    return t

def t_ID(t):
    r'[a-z]+'
    return t

def t_COMMENT(t):#write comment token definition. comments are denoted by //
    r'//.*'
    pass

def t_NEWLINE(t):# this is already completed for you
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)