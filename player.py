import random
class player:
    def __init__(self,letter):
        self.letter = letter
        pass

#
# humain typing on keyboard to play
#

class humainPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def makeMove(self):
        move =int(input("Entrer the value of your next move (0-8) : "))
        return move
    
    def toString(self):
        return f"I am a humain player with  letter {self.letter}"

#
# machine auto guessing letters 😼 
#

class virtualPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self):
        move = random.randint(0,8)
        return move
    
    def toString(self):
        return f"I am a virtual player with  letter {self.letter}"