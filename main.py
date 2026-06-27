
import random

#This is a simple minesweeper engine
#It should be able to interact with like a closed box, by 'clicking' the specfic boxes.

class Board():
    def __init__(self,row_count:int,col_count:int,bomb_count:int):
            self.row_count = row_count #this is discrete height
            self.col_count = col_count #this is discrete width
            self.bomb_count = bomb_count
            
            self.board = [[ 0 for i in range(col_count)] for i in range(row_count)]
            
            #Now randomly distribute the bombs
            #We need to randomly disribute bombs across a list of spaces
            #To do this, we start with a filler list , that shows every open space
            #For each item removed, we simply pop that index (not value) and this creates a mismatch
            #between the value and the index which solves the allocation problem
            
            total = row_count*col_count
            filler = list(range(total))

            for i in range(bomb_count):
                
                bomb_index = filler.pop(random.randrange(0,total-i))
                self.board[bomb_index%row_count][bomb_index//col_count] = 1

            pass
    pass

class Cell():
    pass