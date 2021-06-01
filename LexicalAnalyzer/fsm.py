fsm =   {(1, '0') : 2,
         (1, '1') : 2,
         (1, '2') : 2,
         (1, '3') : 2,
         (1, '4') : 2,
         (1, '5') : 2,
         (1, '6') : 2,
         (1, '7') : 2,
         (1, '8') : 2,
         (1, '9') : 2,
         (2, '0') : 2,
         (2, '1') : 2,
         (2, '2') : 2,
         (2, '3') : 2,
         (2, '4') : 2,
         (2, '5') : 2,
         (2, '6') : 2,
         (2, '7') : 2,
         (2, '8') : 2,
         (2, '9') : 2}

accepting = [2]

def fsmsim(string, current, fsm, accepting):
    if string == "": 
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in fsm:
            rest_of_string = string[1:]
            next_state = fsm[(current, letter)]
            return fsmsim(rest_of_string, next_state, fsm, accepting)
        else:
            return False


def is_INTEGER(input_string):
	is_match = fsmsim(input_string,1,fsm,accepting)
	return is_match

if (__name__ == "__main__"):
   print("2", is_INTEGER("2"))
   print("2779", is_INTEGER("2779"))
   print("0", is_INTEGER("0"))
   print("w9", is_INTEGER("w9"))
   print("y", is_INTEGER("y"))
   print("67g56", is_INTEGER("67g56"))