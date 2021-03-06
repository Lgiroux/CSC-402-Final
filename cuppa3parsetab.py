
# cuppa3parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftEQLEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTAPPEND DECLARE DIVIDE ELSE EQ GET ID IF INSERT INTEGER LE MINUS NOT PLUS PREPEND PULL PUT RETURN STRING TIMES WHILE\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | empty\n    \n    stmt : DECLARE ID '(' opt_formal_args ')' stmt\n         | DECLARE ID opt_init opt_semi\n         | DECLARE ID '=' arr_exp opt_semi\n         | ID '=' exp opt_semi\n         | APPEND ID exp opt_semi\n         | PREPEND ID exp opt_semi\n         | INSERT ID exp exp opt_semi\n         | PULL ID exp exp opt_semi\n         | GET ID opt_semi\n         | PUT exp opt_semi\n         | ID '(' opt_actual_args ')' opt_semi\n         | RETURN opt_exp opt_semi\n         | WHILE '(' exp ')' stmt\n         | IF '(' exp ')' stmt opt_else\n         | '{' stmt_list '}'\n    \n     arr_exp : '[' ']'\n             | '[' arr_content ']'\n    \n     arr_content : arr_val\n                 | arr_val ',' arr_content\n    \n     arr_val : arr_exp \n    \n     arr_val : INTEGER \n    \n    opt_formal_args : formal_args\n                    | empty\n    \n    formal_args : ID ',' formal_args\n                | ID\n    \n    opt_init : '=' exp\n             | empty\n    \n    opt_actual_args : actual_args\n                    | empty\n    \n    actual_args : exp ',' actual_args\n                | exp\n    \n    opt_exp : exp\n            | empty\n    \n    opt_else : ELSE stmt\n             | empty\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp EQ exp\n        | exp LE exp\n    \n    exp : INTEGER\n    \n    exp : STRING\n    \n    exp : ID\n    \n    exp : ID '(' opt_actual_args ')'\n    \n    exp : '(' exp ')'\n    \n    exp : MINUS exp %prec UMINUS\n    \n    exp : NOT exp\n    \n    opt_semi : ';'\n             | empty\n    \n    empty :\n    "
    
_lr_action_items = {'DECLARE':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[5,5,-54,5,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,5,5,5,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,5,-38,-37,]),'ID':([0,3,5,7,8,9,10,11,12,13,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,69,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[6,6,18,21,22,23,24,25,30,30,6,-54,30,30,30,30,30,30,-54,-54,30,-45,-46,-47,30,30,-54,-35,-36,30,30,70,-54,30,-30,-54,-54,-54,30,30,-12,-52,-53,-13,30,30,30,30,30,30,-50,30,-51,-15,-18,-5,-54,-29,-7,-54,30,-8,-9,-54,30,-54,-39,-40,-41,-42,-43,-44,-49,6,6,70,6,-6,-19,-14,-10,-40,-11,-48,-16,-54,-4,-20,-17,6,-38,-37,]),'APPEND':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[7,7,-54,7,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,7,7,7,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,7,-38,-37,]),'PREPEND':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[8,8,-54,8,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,8,8,8,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,8,-38,-37,]),'INSERT':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[9,9,-54,9,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,9,9,9,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,9,-38,-37,]),'PULL':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[10,10,-54,10,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,10,10,10,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,10,-38,-37,]),'GET':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[11,11,-54,11,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,11,11,11,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,11,-38,-37,]),'PUT':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[12,12,-54,12,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,12,12,12,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,12,-38,-37,]),'RETURN':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[13,13,-54,13,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,13,13,13,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,13,-38,-37,]),'WHILE':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[14,14,-54,14,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,14,14,14,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,14,-38,-37,]),'IF':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[15,15,-54,15,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,15,15,15,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,15,-38,-37,]),'{':([0,3,13,16,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,94,95,97,98,99,104,106,107,108,109,110,111,113,114,116,117,118,120,],[16,16,-54,16,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,16,16,16,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,16,-38,-37,]),'$end':([0,1,2,3,4,13,17,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,98,99,104,106,107,108,109,110,111,113,114,116,118,120,],[-54,0,-1,-54,-3,-54,-2,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,-38,-37,]),'}':([3,4,13,16,17,18,25,26,28,29,30,33,34,35,38,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,98,99,104,106,107,108,109,110,111,113,114,116,118,120,],[-54,-3,-54,-54,-2,-54,-54,-54,-45,-46,-47,-54,-35,-36,69,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,-6,-19,-14,-10,-50,-11,-48,-16,-54,-4,-20,-17,-38,-37,]),'=':([6,18,],[19,41,]),'(':([6,12,13,14,15,18,19,20,21,22,23,24,27,28,29,30,31,32,36,37,41,50,51,56,57,58,59,60,61,62,63,65,80,84,86,87,88,89,90,91,93,107,109,],[20,31,31,36,37,39,31,31,31,31,31,31,31,-45,-46,63,31,31,31,31,31,31,31,31,31,31,31,31,31,-50,31,-51,31,31,-39,-40,-41,-42,-43,-44,-49,-40,-48,]),'INTEGER':([12,13,19,20,21,22,23,24,27,28,29,30,31,32,36,37,41,50,51,56,57,58,59,60,61,62,63,65,77,80,84,86,87,88,89,90,91,93,107,109,115,],[28,28,28,28,28,28,28,28,28,-45,-46,-47,28,28,28,28,28,28,28,28,28,28,28,28,28,-50,28,-51,103,28,28,-39,-40,-41,-42,-43,-44,-49,-40,-48,103,]),'STRING':([12,13,19,20,21,22,23,24,27,28,29,30,31,32,36,37,41,50,51,56,57,58,59,60,61,62,63,65,80,84,86,87,88,89,90,91,93,107,109,],[29,29,29,29,29,29,29,29,29,-45,-46,-47,29,29,29,29,29,29,29,29,29,29,29,29,29,-50,29,-51,29,29,-39,-40,-41,-42,-43,-44,-49,-40,-48,]),'MINUS':([12,13,19,20,21,22,23,24,26,27,28,29,30,31,32,34,36,37,41,43,47,48,49,50,51,56,57,58,59,60,61,62,63,64,65,67,68,76,80,83,84,85,86,87,88,89,90,91,93,107,109,],[27,27,27,27,27,27,27,27,57,27,-45,-46,-47,27,27,57,27,27,27,57,57,57,57,84,84,27,27,27,27,27,27,-50,27,57,-51,57,57,57,27,57,27,57,-39,-40,-41,-42,57,57,-49,-40,-48,]),'NOT':([12,13,19,20,21,22,23,24,27,28,29,30,31,32,36,37,41,50,51,56,57,58,59,60,61,62,63,65,80,84,86,87,88,89,90,91,93,107,109,],[32,32,32,32,32,32,32,32,32,-45,-46,-47,32,32,32,32,32,32,32,32,32,32,32,32,32,-50,32,-51,32,32,-39,-40,-41,-42,-43,-44,-49,-40,-48,]),';':([13,18,25,26,28,29,30,33,34,35,40,42,43,48,49,62,65,75,76,79,83,85,86,87,88,89,90,91,93,99,107,109,114,],[-54,-54,53,53,-45,-46,-47,53,-35,-36,53,-30,53,53,53,-50,-51,53,-29,53,53,53,-39,-40,-41,-42,-43,-44,-49,-19,-50,-48,-20,]),'ELSE':([13,18,25,26,28,29,30,33,34,35,40,42,43,48,49,52,53,54,55,62,65,66,69,74,75,76,78,79,81,82,83,85,86,87,88,89,90,91,93,98,99,104,106,107,108,109,110,111,113,114,116,118,120,],[-54,-54,-54,-54,-45,-46,-47,-54,-35,-36,-54,-30,-54,-54,-54,-12,-52,-53,-13,-50,-51,-15,-18,-5,-54,-29,-7,-54,-8,-9,-54,-54,-39,-40,-41,-42,-43,-44,-49,-6,-19,-14,-10,-50,-11,-48,-16,117,-4,-20,-17,-38,-37,]),')':([20,28,29,30,39,44,45,46,47,62,63,64,65,67,68,70,71,72,73,86,87,88,89,90,91,92,93,105,109,112,],[-54,-45,-46,-47,-54,79,-31,-32,-34,-50,-54,93,-51,94,95,-28,97,-25,-26,-39,-40,-41,-42,-43,-44,109,-49,-33,-48,-27,]),'PLUS':([26,28,29,30,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,93,107,109,],[56,-45,-46,-47,56,56,56,56,56,56,56,-50,56,-51,56,56,56,56,56,-39,-40,-41,-42,56,56,-49,-40,-48,]),'TIMES':([26,28,29,30,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,93,107,109,],[58,-45,-46,-47,58,58,58,58,58,58,58,-50,58,-51,58,58,58,58,58,58,58,-41,-42,58,58,-49,58,-48,]),'DIVIDE':([26,28,29,30,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,93,107,109,],[59,-45,-46,-47,59,59,59,59,59,59,59,-50,59,-51,59,59,59,59,59,59,59,-41,-42,59,59,-49,59,-48,]),'EQ':([26,28,29,30,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,93,107,109,],[60,-45,-46,-47,60,60,60,60,60,60,60,-50,60,-51,60,60,60,60,60,-39,-40,-41,-42,-43,-44,-49,-40,-48,]),'LE':([26,28,29,30,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,93,107,109,],[61,-45,-46,-47,61,61,61,61,61,61,61,-50,61,-51,61,61,61,61,61,-39,-40,-41,-42,-43,-44,-49,-40,-48,]),',':([28,29,30,47,62,65,70,86,87,88,89,90,91,93,99,101,102,103,109,114,],[-45,-46,-47,80,-50,-51,96,-39,-40,-41,-42,-43,-44,-49,-19,115,-23,-24,-48,-20,]),'[':([41,77,115,],[77,77,77,]),']':([77,99,100,101,102,103,114,119,],[99,-19,114,-21,-23,-24,-20,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,3,16,],[2,17,38,]),'stmt':([0,3,16,94,95,97,117,],[3,3,3,110,111,113,120,]),'empty':([0,3,13,16,18,20,25,26,33,39,40,43,48,49,63,75,79,83,85,111,],[4,4,35,4,42,46,54,54,54,73,54,54,54,54,46,54,54,54,54,118,]),'exp':([12,13,19,20,21,22,23,24,27,31,32,36,37,41,50,51,56,57,58,59,60,61,63,80,84,],[26,34,43,47,48,49,50,51,62,64,65,67,68,76,83,85,86,87,88,89,90,91,47,47,107,]),'opt_exp':([13,],[33,]),'opt_init':([18,],[40,]),'opt_actual_args':([20,63,],[44,92,]),'actual_args':([20,63,80,],[45,45,105,]),'opt_semi':([25,26,33,40,43,48,49,75,79,83,85,],[52,55,66,74,78,81,82,98,104,106,108,]),'opt_formal_args':([39,],[71,]),'formal_args':([39,96,],[72,112,]),'arr_exp':([41,77,115,],[75,102,102,]),'arr_content':([77,115,],[100,119,]),'arr_val':([77,115,],[101,101,]),'opt_else':([111,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_prog','cuppa3_frontend.py',23),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','cuppa3_frontend.py',30),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','cuppa3_frontend.py',31),
  ('stmt -> DECLARE ID ( opt_formal_args ) stmt','stmt',6,'p_stmt','cuppa3_frontend.py',41),
  ('stmt -> DECLARE ID opt_init opt_semi','stmt',4,'p_stmt','cuppa3_frontend.py',42),
  ('stmt -> DECLARE ID = arr_exp opt_semi','stmt',5,'p_stmt','cuppa3_frontend.py',43),
  ('stmt -> ID = exp opt_semi','stmt',4,'p_stmt','cuppa3_frontend.py',44),
  ('stmt -> APPEND ID exp opt_semi','stmt',4,'p_stmt','cuppa3_frontend.py',45),
  ('stmt -> PREPEND ID exp opt_semi','stmt',4,'p_stmt','cuppa3_frontend.py',46),
  ('stmt -> INSERT ID exp exp opt_semi','stmt',5,'p_stmt','cuppa3_frontend.py',47),
  ('stmt -> PULL ID exp exp opt_semi','stmt',5,'p_stmt','cuppa3_frontend.py',48),
  ('stmt -> GET ID opt_semi','stmt',3,'p_stmt','cuppa3_frontend.py',49),
  ('stmt -> PUT exp opt_semi','stmt',3,'p_stmt','cuppa3_frontend.py',50),
  ('stmt -> ID ( opt_actual_args ) opt_semi','stmt',5,'p_stmt','cuppa3_frontend.py',51),
  ('stmt -> RETURN opt_exp opt_semi','stmt',3,'p_stmt','cuppa3_frontend.py',52),
  ('stmt -> WHILE ( exp ) stmt','stmt',5,'p_stmt','cuppa3_frontend.py',53),
  ('stmt -> IF ( exp ) stmt opt_else','stmt',6,'p_stmt','cuppa3_frontend.py',54),
  ('stmt -> { stmt_list }','stmt',3,'p_stmt','cuppa3_frontend.py',55),
  ('arr_exp -> [ ]','arr_exp',2,'p_arr_exp','cuppa3_frontend.py',93),
  ('arr_exp -> [ arr_content ]','arr_exp',3,'p_arr_exp','cuppa3_frontend.py',94),
  ('arr_content -> arr_val','arr_content',1,'p_arr_content','cuppa3_frontend.py',104),
  ('arr_content -> arr_val , arr_content','arr_content',3,'p_arr_content','cuppa3_frontend.py',105),
  ('arr_val -> arr_exp','arr_val',1,'p_arr_val_exp','cuppa3_frontend.py',115),
  ('arr_val -> INTEGER','arr_val',1,'p_arr_val_int','cuppa3_frontend.py',122),
  ('opt_formal_args -> formal_args','opt_formal_args',1,'p_opt_formal_args','cuppa3_frontend.py',129),
  ('opt_formal_args -> empty','opt_formal_args',1,'p_opt_formal_args','cuppa3_frontend.py',130),
  ('formal_args -> ID , formal_args','formal_args',3,'p_formal_args','cuppa3_frontend.py',137),
  ('formal_args -> ID','formal_args',1,'p_formal_args','cuppa3_frontend.py',138),
  ('opt_init -> = exp','opt_init',2,'p_opt_init','cuppa3_frontend.py',148),
  ('opt_init -> empty','opt_init',1,'p_opt_init','cuppa3_frontend.py',149),
  ('opt_actual_args -> actual_args','opt_actual_args',1,'p_opt_actual_args','cuppa3_frontend.py',159),
  ('opt_actual_args -> empty','opt_actual_args',1,'p_opt_actual_args','cuppa3_frontend.py',160),
  ('actual_args -> exp , actual_args','actual_args',3,'p_actual_args','cuppa3_frontend.py',167),
  ('actual_args -> exp','actual_args',1,'p_actual_args','cuppa3_frontend.py',168),
  ('opt_exp -> exp','opt_exp',1,'p_opt_exp','cuppa3_frontend.py',178),
  ('opt_exp -> empty','opt_exp',1,'p_opt_exp','cuppa3_frontend.py',179),
  ('opt_else -> ELSE stmt','opt_else',2,'p_opt_else','cuppa3_frontend.py',186),
  ('opt_else -> empty','opt_else',1,'p_opt_else','cuppa3_frontend.py',187),
  ('exp -> exp PLUS exp','exp',3,'p_binop_exp','cuppa3_frontend.py',197),
  ('exp -> exp MINUS exp','exp',3,'p_binop_exp','cuppa3_frontend.py',198),
  ('exp -> exp TIMES exp','exp',3,'p_binop_exp','cuppa3_frontend.py',199),
  ('exp -> exp DIVIDE exp','exp',3,'p_binop_exp','cuppa3_frontend.py',200),
  ('exp -> exp EQ exp','exp',3,'p_binop_exp','cuppa3_frontend.py',201),
  ('exp -> exp LE exp','exp',3,'p_binop_exp','cuppa3_frontend.py',202),
  ('exp -> INTEGER','exp',1,'p_integer_exp','cuppa3_frontend.py',209),
  ('exp -> STRING','exp',1,'p_string_exp','cuppa3_frontend.py',216),
  ('exp -> ID','exp',1,'p_id_exp','cuppa3_frontend.py',223),
  ('exp -> ID ( opt_actual_args )','exp',4,'p_call_exp','cuppa3_frontend.py',230),
  ('exp -> ( exp )','exp',3,'p_paren_exp','cuppa3_frontend.py',237),
  ('exp -> MINUS exp','exp',2,'p_uminus_exp','cuppa3_frontend.py',244),
  ('exp -> NOT exp','exp',2,'p_not_exp','cuppa3_frontend.py',251),
  ('opt_semi -> ;','opt_semi',1,'p_opt_semi','cuppa3_frontend.py',258),
  ('opt_semi -> empty','opt_semi',1,'p_opt_semi','cuppa3_frontend.py',259),
  ('empty -> <empty>','empty',0,'p_empty','cuppa3_frontend.py',266),
]
