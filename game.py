import player 

class game:

    def __init__(self,board):
        self.board = board
    
    def __displayBoard(self):
        for row in self.board:
            print (row)
    
    def __addToBoard(self,value,letter):
        indexRow = value // 3
        indexCol = value % 3 
        self.board[indexRow][indexCol] = letter
    
    def __checkSpace(self):
        available = False
        for row in self.board:
            for i in range(len(row)):
                if (row[i]==""):
                    available = True
        
        return available
    
    def play(self,playerOne,playerTwo):
        while (self.__checkSpace()):
            self.__displayBoard()
            moveOne = playerOne.makeMove()
            moveTwo = playerTwo.makeMove()
            self.__addToBoard(moveOne,playerOne.letter)
            self.__addToBoard(moveTwo,playerTwo.letter)

       

playerOne = player.humainPlayer("X")
playerTwo = player.virtualPlayer("Y")
print(playerOne.toString())
print(playerTwo.toString())
game = game( [ [str("") for i in range(3)] for i in range (3)])
game.play(playerOne,playerTwo)