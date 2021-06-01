
# parser_tabmodule.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftEQLEleftPLUSMINUSleftTIMESDIVIDEDECIMAL DIVIDE EQ ID INTEGER LE MINUS PLUS SCIENTIFIC TIMES\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | \n    \n    stmt : ID '=' exp\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp LE exp\n        | exp EQ exp\n    \n    exp : SCIENTIFIC\n    \n    exp : DECIMAL\n    \n    exp : INTEGER\n    \n    exp : ID\n    "
    
_lr_action_items = {'$end':([0,1,2,3,5,7,8,9,10,11,18,19,20,21,22,23,],[-3,0,-1,-3,-2,-14,-4,-11,-12,-13,-5,-6,-7,-8,-9,-10,]),'ID':([0,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[4,4,7,-14,-4,-11,-12,-13,7,7,7,7,7,7,-5,-6,-7,-8,-9,-10,]),'=':([4,],[6,]),'SCIENTIFIC':([6,12,13,14,15,16,17,],[9,9,9,9,9,9,9,]),'DECIMAL':([6,12,13,14,15,16,17,],[10,10,10,10,10,10,10,]),'INTEGER':([6,12,13,14,15,16,17,],[11,11,11,11,11,11,11,]),'PLUS':([7,8,9,10,11,18,19,20,21,22,23,],[-14,12,-11,-12,-13,-5,-6,-7,-8,12,12,]),'MINUS':([7,8,9,10,11,18,19,20,21,22,23,],[-14,13,-11,-12,-13,-5,-6,-7,-8,13,13,]),'TIMES':([7,8,9,10,11,18,19,20,21,22,23,],[-14,14,-11,-12,-13,14,14,-7,-8,14,14,]),'DIVIDE':([7,8,9,10,11,18,19,20,21,22,23,],[-14,15,-11,-12,-13,15,15,-7,-8,15,15,]),'LE':([7,8,9,10,11,18,19,20,21,22,23,],[-14,16,-11,-12,-13,-5,-6,-7,-8,-9,-10,]),'EQ':([7,8,9,10,11,18,19,20,21,22,23,],[-14,17,-11,-12,-13,-5,-6,-7,-8,-9,-10,]),}

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
  ('program -> stmt_list','program',1,'p_prog','parser.py',28),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','parser.py',35),
  ('stmt_list -> <empty>','stmt_list',0,'p_stmt_list','parser.py',36),
  ('stmt -> ID = exp','stmt',3,'p_stmt','parser.py',46),
  ('exp -> exp PLUS exp','exp',3,'p_binop_exp','parser.py',57),
  ('exp -> exp MINUS exp','exp',3,'p_binop_exp','parser.py',58),
  ('exp -> exp TIMES exp','exp',3,'p_binop_exp','parser.py',59),
  ('exp -> exp DIVIDE exp','exp',3,'p_binop_exp','parser.py',60),
  ('exp -> exp LE exp','exp',3,'p_binop_exp','parser.py',61),
  ('exp -> exp EQ exp','exp',3,'p_binop_exp','parser.py',62),
  ('exp -> SCIENTIFIC','exp',1,'p_scientific_exp','parser.py',69),
  ('exp -> DECIMAL','exp',1,'p_decimal_exp','parser.py',76),
  ('exp -> INTEGER','exp',1,'p_integer_exp','parser.py',84),
  ('exp -> ID','exp',1,'p_id_exp','parser.py',90),
]