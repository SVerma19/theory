#######################################################################
# parser for excalibur
#######################################################################
from ply import yacc
from lexer import tokens, lexer
from pprint import pprint

class State:
    def __init__(self):
        self.initialize()
    def initialize(self):
        self.AST = None
state = State()

#######################################################################
# set operator precedence and associativity (if two operators have same 
# precedence, which operator gets priority:left associative means left
# side gets higher priority. Right associative, vice versa)
#######################################################################
precedence = (
              ('left', 'EQ', 'LE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE')
             )

#########################################################################
# grammar rules: the text in docstring represents the context free grammar
# the functions contain logic for creating the abstract syntax tree, one level at a time
#########################################################################
def p_prog(p):
    '''
    program : stmt_list
    '''
    state.AST = p[1]

#########################################################################
def p_stmt_list(p):
    '''
    stmt_list : stmt stmt_list
              | 
    '''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    elif (len(p) == 2):
        p[0] = ('nil')

#########################################################################
def p_stmt(p):
    '''
    stmt : ID '=' exp
    '''
    if p[2] == '=':
        p[0] = ('assign', p[1], p[3])
    else:
        raise ValueError("unexpected symbol {}".format(p[1]))

#########################################################################
def p_integer_exp(p):
    '''
    exp : INTEGER
    '''
    p[0] = ('integer', p[1])   

#########################################################################
def p_id_exp(p):
    '''
    exp : ID
    '''
    p[0] = ('id', p[1])

#########################################################################
def p_decimal_exp(p):
    '''
    exp : DECIMAL
    '''
    p[0] = ('decimal', p[1]) 

#########################################################################
def p_add_exp(p):
    '''
    exp : exp PLUS exp
    '''
    p[0] = (p[2], p[1], p[3])

#########################################################################
def p_subt_exp(p):
    '''
    exp : exp MINUS exp
    '''
    p[0] = (p[2], p[1], p[3]) 

#########################################################################
def p_mult_exp(p):
    '''
    exp : exp TIMES exp
    '''
    p[0] = (p[2], p[1], p[3])  

#########################################################################
def p_divi_exp(p):
    '''
    exp : exp DIVIDE exp
    '''
    p[0] = (p[2], p[1], p[3])  

#########################################################################
def p_equal_exp(p):
    '''
    exp : exp EQ exp
    '''
    p[0] = (p[2], p[1], p[3])

#########################################################################
def p_le_exp(p):
    '''
    exp : exp LE exp
    '''
    p[0] = (p[2], p[1], p[3])   

#########################################################################
def p_scientific_exp(p):
    '''
    exp : SCIENTIFIC
    '''
    p[0] = ('scientific', p[1]) 

#########################################################################
def p_error(t):
    print("Syntax error at '%s'" % t.value)

#########################################################################

#########################################################################
# build the parser
#########################################################################
parser = yacc.yacc(debug=False)
if __name__ == '__main__':
    data = '''r=3.3+6-5
           a=8.8X10e3
           r=3-4
           s=3/4-1.2X10e4
           t=3.1+9*4
           u=9.0 
           v=3*4+4
           w=3==4.5X10e4'''
    parser.parse(data)
    pprint(state.AST)