from game.parachute import Parachute
from game.word import Word

class Console:
    def __init__(self) -> None:
        pass

    def print_word(self,word_obj):
        word_obj.print_guess()
        print()

    def print_parachute(self,para_obj):
        para_obj.print()
        print()
    
    def print_end(self):
        print("END OF LINE")