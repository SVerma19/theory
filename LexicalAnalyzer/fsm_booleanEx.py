# FSM Simulation
#1-(0)-> 2
#1-(1)->2
#2-(0)->2
#2-(1)->2
fsm =   {(1, '0') : 2,
         (1, '1') : 2,
         (2, '0') : 2,
         (2, '1') : 2}

accepting = [2]

def fsmsim(string, current, fsm, accepting):#remaing part of string, current state, FSM, accepting states
    if string == "": # we are at the end of the input so return if current state is an accepting state
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in fsm:#check if there is an outgoing edge
            rest_of_string = string[1:]
            next_state = fsm[(current,letter)]
            return fsmsim(rest_of_string,next_state, fsm, accepting)
        else:
            return False #there

def is_BOOLEAN(input_string):
   is_match = fsmsim(input_string,1,fsm,accepting)
   return is_match
if (__name__ == "__main__"):
   print("100", is_BOOLEAN("100"))
   print("10101", is_BOOLEAN("10101"))
   print("0", is_BOOLEAN("0"))
   print("w9", is_BOOLEAN("w9"))
   print("y", is_BOOLEAN("y"))
   print("1t1", is_BOOLEAN("1t1"))


