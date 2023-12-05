import player 

class game:

    def __init__(self,board):
        self.board = board
    
    def __displayBoard(self):
        print("\n")
        for row in self.board:
            print (" | ".join(row))
            print("\n")
    
    def __availableMoves(self):
        movesIndex=[]
        
        for row in range(len(self.board)):  
            
            for column in range(len(self.board[row]) ):
                if self.board[row][column] == " " :
                    movesIndex.append(column + (3 * row))
            
        return movesIndex

        #return [ i if i != '' for i in  self.board]
    
    def __addToBoard(self,value,letter):
        indexRow = value // 3
        indexcolumn = value % 3 
        self.board[indexRow][indexcolumn] = letter
    
    def __checkWinner(self,letter):
        
        
        

        #
        #Row check
        #


        for line in range(len(self.board)):
            win=True
            for column in range(len(self.board)):
                    if (self.board[line][column] != letter):
                        win = False
            if (win==True):
                self.__displayBoard()
                print("row")
                return win
            
        #
        # Column check
        #
        
        for column in range(len(self.board)):
            win=True
            for  line in range(len(self.board)):
                if (self.board[line][column] != letter ):
                    win = False
            if (win==True):
                self.__displayBoard()
                print("Col")
                return win
            
        diagCount=0
        for line in range(len(self.board)):
            
            if (self.board[line][line] == letter ):
                diagCount = diagCount+1

        if (diagCount==len(self.board)):
            self.__displayBoard()
            print("Diag")
            return True
            
            
        
        
        return False

        
            
    
    def __checkSpace(self):
        
        if len( self.__availableMoves() ) > 0:
            return True 
    
    
    def play(self,playerOne,playerTwo):
        currentLetter = "X"
        move= 0
        while (self.__checkSpace()):
            
            self.__availableMoves()
            if (currentLetter=="X"):
                move = playerOne.makeMove(self.__availableMoves())
                self.__addToBoard(move,playerOne.letter)
                if(self.__checkWinner(playerOne.letter)):
                    print(f"Player {playerOne.letter} win !")
                    return 0
            else:
                move = playerTwo.makeMove(self.__availableMoves())
                self.__addToBoard(move,playerTwo.letter)
                if(self.__checkWinner(playerTwo.letter)):
                    print(f"Player {playerTwo.letter} win !")
                    return 0
            
            
            if (currentLetter=="X"):
                currentLetter="Y"
            else:
                currentLetter="X"
            self.__displayBoard()
            


       

playerOne = player.humainPlayer("X")
playerTwo = player.virtualPlayer("Y")
print(playerOne.toString())
print(playerTwo.toString())
game = game( [ [str(" ") for i in range(3)] for i in range (3)])
game.play(playerOne,playerTwo)