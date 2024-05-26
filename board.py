from piece import Bishop
from piece import King
from piece import Rook
from piece import Pawn
from piece import Queen
from piece import Knight



class Board():
    def chosen(self):
        return self.chosen 
    def __init__(self, row, col):
        
        self.row=row
        self.col=col
        self.board=  [[None for _ in range(8)] for _ in range(8)]
        self.board[0][0]=Rook(0,0,'b')
        self.board[0][1]=Knight(1,0,'b')
        self.board[0][2]=Bishop(2,0,'b')
        self.board[0][3]=Queen(3,0,'b')
        self.board[0][4]=King(4,0,'b')
        self.board[0][5]=Bishop(5,0,'b')
        self.board[0][6]=Knight(6,0,'b')
        self.board[0][7]=Rook(7,0,'b')

        self.board[1][0]=Pawn(0,1,'b')
        self.board[1][1]=Pawn(1,1,'b')
        self.board[1][2]=Pawn(2,1,'b')
        self.board[1][3]=Pawn(3,1,'b')
        self.board[1][4]=Pawn(4,1,'b')
        self.board[1][5]=Pawn(5,1,'b')
        self.board[1][6]=Pawn(6,1,'b')
        self.board[1][7]=Pawn(7,1,'b')


        self.board[7][0]=Rook(0,7,'w')
        self.board[7][1]=Knight(1,7,'w')
        self.board[7][2]=Bishop(2,7,'w')
        self.board[7][3]=Queen(3,7,'w')
        self.board[7][4]=King(4,7,'w')
        self.board[7][5]=Bishop(5,7,'w')
        self.board[7][6]=Knight(6,7,'w')
        self.board[7][7]=Rook(7,7,'w')

        self.board[6][0]=Pawn(0,6,'w')
        self.board[6][1]=Pawn(1,6,'w')
        self.board[6][2]=Pawn(2,6,'w')
        self.board[6][3]=Pawn(3,6,'w')
        self.board[6][4]=Pawn(4,6,'w')
        self.board[6][5]=Pawn(5,6,'w')
        self.board[6][6]=Pawn(6,6,'w')
        self.board[6][7]=Pawn(7,6,'w')
        


    def draw(self, screen,bo, black, white):
        
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] is not None :
                    self.board[i][j].draw(screen)
        
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] is not None and self.board[i][j].selected==True :#and color==self.board[i][j].color:
                    self.board[i][j].draw_selected(screen,bo, black, white)
        
        
       
                   
                    
                



