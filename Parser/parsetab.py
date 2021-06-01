
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftEQLEleftPLUSMINUSleftTIMESDIVIDEDECIMAL DIVIDE EQ ID INTEGER LE MINUS PLUS SCIENTIFIC TIMES\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | \n    \n    stmt : ID '=' exp\n    \n    exp : INTEGER\n    \n    exp : ID\n    \n    exp : DECIMAL\n    \n    exp : exp PLUS exp\n    \n    exp : exp MINUS exp\n    \n    exp : exp TIMES exp\n    \n    exp : exp DIVIDE exp\n    \n    exp : exp EQ exp\n    \n    exp : exp LE exp\n    \n    exp : SCIENTIFIC\n    "
    
_lr_action_items = {'$end':([0,1,2,3,5,7,8,9,10,11,18,19,20,21,22,23,],[-3,0,-1,-3,-2,-6,-4,-5,-7,-14,-8,-9,-10,-11,-12,-13,]),'ID':([0,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[4,4,7,-6,-4,-5,-7,-14,7,7,7,7,7,7,-8,-9,-10,-11,-12,-13,]),'=':([4,],[6,]),'INTEGER':([6,12,13,14,15,16,17,],[9,9,9,9,9,9,9,]),'DECIMAL':([6,12,13,14,15,16,17,],[10,10,10,10,10,10,10,]),'SCIENTIFIC':([6,12,13,14,15,16,17,],[11,11,11,11,11,11,11,]),'PLUS':([7,8,9,10,11,18,19,20,21,22,23,],[-6,12,-5,-7,-14,-8,-9,-10,-11,12,12,]),'MINUS':([7,8,9,10,11,18,19,20,21,22,23,],[-6,13,-5,-7,-14,-8,-9,-10,-11,13,13,]),'TIMES':([7,8,9,10,11,18,19,20,21,22,23,],[-6,14,-5,-7,-14,14,14,-10,-11,14,14,]),'DIVIDE':([7,8,9,10,11,18,19,20,21,22,23,],[-6,15,-5,-7,-14,15,15,-10,-11,15,15,]),'EQ':([7,8,9,10,11,18,19,20,21,22,23,],[-6,16,-5,-7,-14,-8,-9,-10,-11,-12,-13,]),'LE':([7,8,9,10,11,18,19,20,21,22,23,],[-6,17,-5,-7,-14,-8,-9,-10,-11,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,3,],[2,5,]),'stmt':([0,3,],[3,3,]),'exp':([6,12,13,14,15,16,17,],[8,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_prog','parser.py',29),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','parser.py',36),
  ('stmt_list -> <empty>','stmt_list',0,'p_stmt_list','parser.py',37),
  ('stmt -> ID = exp','stmt',3,'p_stmt','parser.py',47),
  ('exp -> INTEGER','exp',1,'p_integer_exp','parser.py',57),
  ('exp -> ID','exp',1,'p_id_exp','parser.py',64),
  ('exp -> DECIMAL','exp',1,'p_decimal_exp','parser.py',71),
  ('exp -> exp PLUS exp','exp',3,'p_add_exp','parser.py',78),
  ('exp -> exp MINUS exp','exp',3,'p_subt_exp','parser.py',85),
  ('exp -> exp TIMES exp','exp',3,'p_mult_exp','parser.py',92),
  ('exp -> exp DIVIDE exp','exp',3,'p_divi_exp','parser.py',99),
  ('exp -> exp EQ exp','exp',3,'p_equal_exp','parser.py',106),
  ('exp -> exp LE exp','exp',3,'p_le_exp','parser.py',113),
  ('exp -> SCIENTIFIC','exp',1,'p_scientific_exp','parser.py',120),
]