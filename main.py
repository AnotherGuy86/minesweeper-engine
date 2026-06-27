
import random

#This is a simple minesweeper engine
#It should be able to interact with like a closed box, by 'clicking' the specfic boxes.

class Board():
    def __init__(self,row_count:int,col_count:int,bomb_count:int):
            self.row_count = row_count #this is discrete height ie the col-length
            self.col_count = col_count #this is discrete width  ie the row-length
            self.bomb_count = bomb_count
            
            self.board = [[ Cell(i,j) for i in range(col_count)] for j in range(row_count)]
            
            #Now randomly distribute the bombs
            #We need to randomly disribute bombs across a list of spaces
            #To do this, we start with a filler list , that shows every open space
            #For each item removed, we simply pop that index (not value) and this creates a mismatch
            #between the value and the index which solves the allocation problem
            
            total = row_count*col_count
            filler = list(range(total))

            for i in range(bomb_count):
                bomb_index = filler.pop(random.randrange(0,total-i))
                cell = self.board[bomb_index//col_count][bomb_index%col_count]
                cell.bomb = 1
    
    def print(self):
        #print the current case of the board to the terminal
        sprite_board = ""
        for row in self.board:
            for cell in row:
                if cell.bomb: sprite_board += "X"
                else: sprite_board += "#"
            sprite_board += "\n"
        
        print(sprite_board)
    pass

class Cell():
    def __init__(self,row,col,bomb=0,flagged=0):
            self.row = row
            self.col = col
            self.bomb = bomb
            self.flagged = flagged
    pass

