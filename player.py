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

    def makeMove(self,moves):
        move = -1
        while move not in moves:
            try:
                move =int(input("Entrer the value of your next valid move (0-8) : "))
            except:
                print(f"a valid number please 🤕 {moves}")
            
        print(f"You played square {move}")
        return move
    
    def toString(self):
        return f"I am a humain player with  letter {self.letter}"

#
# machine auto guessing letters 😼 
#

class virtualPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self,moves):
        move = random.choice(moves)
        print(f"The computer played square {move}")
        return move
    
    def toString(self):
        return f"I am a virtual player with  letter {self.letter}"