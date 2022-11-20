class Parachute:
    def __init__(self) -> None:
        self.image = ["  ___"," /___\\"," \\   /","  \\ /","   O","  /|\\","  / \\","","^^^^^^^"]
    
    def reset(self):
        self.image = ["  ___"," /___\\"," \\   /","  \\ /","   O","  /|\\","  / \\","","^^^^^^^"]
    
    def cut(self):
        self.image.pop(0)
        if self.image[0] == "   O":
            self.image[0] = "   X"
    
    def print(self):
        for x in range(len(self.image)):
            print(self.image[x])

    def at_head(self):
        if self.image[0] == "   X":
            return True