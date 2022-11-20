import random

class Word:
    def __init__(self) -> None:
        self._true_word = ""
        self._guess = []
        self._lib = ["word","guess","game","python","parachute"]

    def print_guess(self):
        #print(*self._guess)
        temp = ""
        for x in range(len(self._guess)):
            temp = temp + self._guess[x]
        print(temp)

    def choose_word(self):
        self._true_word = self._lib[random.randrange(0,len(self._lib))]
        for x in range(len(self._true_word)):
            self._guess.append("_")
    
    def check(self):
        letter = input("Guess a letter [a-z]: ")
        if_failed = True
        for x in range(len(self._true_word)):
            if self._true_word[x] == letter:
                self._guess[x] = letter
                if_failed = False
        return if_failed