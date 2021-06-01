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
# set operator precedence and associativity(if two operators have same 
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
def p_binop_exp(p):
    '''
    exp : exp PLUS exp
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp
        | exp LE exp
        | exp EQ exp
    '''
    p[0] = (p[2], p[1], p[3])

    for i in range(1):
        type1 = p[1][0]
        type2 = p[3][0]

        var1 = p[1][1]
        var2 = p[3][1]

        #numberVar1 = var1.replace("'","")
        #numberVar2 = var2.replace("'","")
    
        if (type2 == None):
            print(var1)

        if (type1 == type2):
            if p[2] == "+":
                if isinstance(float(var1), float) == True:
                    addFloat = float(var1) + float(var2)
                    print(addFloat)
                    print("**********************")
                elif isinstance(int(var1), int) == True:
                    addInt = int(var1) + int(var2)
                    print(addInt)
                    print("**********************")
            if p[2] == "-":
                sub = var1 - var2
                print(sub)
                print("**********************")
            if p[2] == "*":
                mult = var1 * var2
                print(mult)
                print("**********************")
            if p[2] == "/":
                div = var1 / var2
                print(div)
                print("**********************")
            if p[2] == "==":
                if (var1 == var2):
                    print(True)
                    print("**********************")
                else:
                    print(False)
                    print("**********************")
            if p[2] == "<=":
                if (var1 <= var2):
                    print(True)
                    print("**********************")
                else:
                    print(False)
                    print("**********************")
        else:
            print("Type mismatch")
            print("**********************")

#########################################################################
def p_scientific_exp(p):
    '''
    exp : SCIENTIFIC
    '''
    p[0] = ('scientific', p[1])

#########################################################################
def p_decimal_exp(p):
    '''
    exp : DECIMAL
    '''
    p[0] = ('decimal', p[1])

#########################################################################
def p_integer_exp(p):
    '''
    exp : INTEGER
    '''
    p[0] = ('integer', int(p[1]))     

#########################################################################
def p_id_exp(p):
    '''
    exp : ID
    '''
    p[0] = ('id', p[1])

#########################################################################
def p_error(t):
    print("Syntax error at '%s'" % t.value)

#########################################################################
# build the parser
#########################################################################
parser = yacc.yacc(debug=False,tabmodule='parser_tabmodule')
if __name__ == '__main__':
    data = '''a=4.4+5.0
              x=1+3.4
              y=1==2
              s=4/2
              v=3*4
              w=2==2
              x=3<=1
              '''

    #Could not figure out how to do it with scientific notation using my method
    #r=1.2X10e4+5.0X10e4
    #r=3.3X10e3+4.1X10e3

    parser.parse(data)
    #print(state.AST)