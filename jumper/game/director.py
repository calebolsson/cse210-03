from game.parachute import Parachute
from game.console import Console
from game.word import Word

class Director:
    def __init__(self) -> None:
        self._playing = True
        self.para = Parachute()
        self.console = Console()
        self.word = Word()

    def start_game(self):
        self.word.choose_word()
        while self._playing:
            self._display()
            self._prompt()
            self._evaluate()
    
    def _display(self):
        self.console.print_word(self.word)
        self.console.print_parachute(self.para)

    def _prompt(self):
        if self.word.check():
            self.para.cut()

    def _evaluate(self):
        if self.para.at_head():
            self._playing = False
            self._display()
            self.console.print_end()