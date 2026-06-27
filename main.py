
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
                row_index = bomb_index//col_count
                col_index = bomb_index%col_count

                cell = self.board[row_index][col_index] #which row which col
                cell.bomb = 1
                #Update adj bomb count for cells (this includes self)
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        try: self.board[row_index+i][col_index+j].value += 1
                        except IndexError: pass


    def flag(self,row_position,col_position):
        #uses regular coordinate systems
        cell= self.board[col_position][row_position]
        cell.flagged = not cell.flagged
    
    def print(self,make_visible=False,invert=True):
        #print the current case of the board to the terminal
        sprite_board = ""
        for row in self.board:
            for cell in row:
                if cell.visible or make_visible:
                    if cell.bomb: sprite_board += "X"
                    elif cell.value == 0: sprite_board += " "
                    else: sprite_board += str(cell.value)
                else:
                    if cell.flagged: sprite_board += "F"
                    else: sprite_board += "_"

            sprite_board += "\n"
        
        if invert:
            #fixes the issue of negative y indexing, now coordinate systems should work
            sprite_board = '\n'.join(sprite_board.splitlines()[::-1])
        print(sprite_board)
    pass

class Cell():
    def __init__(self,row,col,bomb=0,flagged=0,value = 0,visible=0):
            self.row = row
            self.col = col
            self.bomb = bomb
            self.flagged = flagged
            self.value = value #this is inclusive if its a bomb
            self.visible = visible
    pass

