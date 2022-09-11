from enum import Enum
from sre_parse import State


class States(Enum):
    s0      = 's0'
    nxtlit  = 'nxtlit'
    error   = 'error'
    stop    = 'stop'

class Lexer():
    def __init__(self):
        self.current_state = States.s0
        self.word = []

    def main(self, lit):
        if self.current_state == States.s0:
            if lit == ' ' or lit == '\n':
                return
            if lit >= '0' and lit <= '9':
                self.current_state = States.error
                return
            if lit >= 'a' and lit <= 'z' or lit >= 'A' and lit <= 'Z': 
                self.word.append(lit)
                self.current_state = States.nxtlit
                return
            self.current_state = States.error
            return 

        if self.current_state == States.nxtlit:
            if (lit >= '0' and lit <= '9') or (lit >= 'a' and lit <= 'z' or lit >= 'A' and lit <= 'Z'):
                self.word.append(lit)
                return
            if lit == ' ' or '\n':
                self.word.append(' ')
                self.current_state = States.s0
                return    
            self.current_state = States.error
            return 

        if self.current_state == States.error: 
            print("".join(self.word)) 
            print('Error') 
            exit()  

lexer = Lexer() 

with open("lab1/text.txt") as file:
    for lit in file.read():
        lexer.main(lit)

lexer.current_state = States.stop
if lexer.current_state == States.stop:
    print("".join(lexer.word))
    print('Stop')  

