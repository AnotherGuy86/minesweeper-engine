
import random
import numpy as np

#This is a simple minesweeper engine
#It should be able to interact with like a closed box, by 'clicking' the specfic boxes.
#For each of the previous properties with cells, we need a specific array to hold them


class Board():
    def __init__(self,row_count:int,col_count:int,bomb_count:int):
            self.row_count = row_count #this is discrete height ie the col-length
            self.col_count = col_count #this is discrete width  ie the row-length
            self.bomb_count = bomb_count
            self.fail = False
            
            #boards
            self.board_value = np.zeros((row_count,col_count),dtype=int)
            self.board_flag  = np.zeros((row_count,col_count),dtype=bool)
            self.board_visible=np.zeros((row_count,col_count),dtype=bool)
            self.board_bomb  = np.zeros((row_count,col_count),dtype=bool)

            
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

                self.board_bomb[row_index,col_index] = True

                #Update adj bomb count for cells (this includes self)
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        try: self.board_value[row_index+i,col_index+j] += 1
                        except IndexError: pass
            
            self.board_blanks = (self.board_value == 0)


    def flag(self,row_pos,col_pos):
        #uses regular coordinate systems
        self.board_flag[row_pos,col_pos] = not self.board_flag[row_pos,col_pos]
    
    def check(self,row_pos,col_pos):
        if self.board_bomb[row_pos,col_pos] == True : self.fail = True
        else:
            self.board_visible[row_pos,col_pos] = True

            #Recusive space expansion
            if self.board_value[row_pos,col_pos] == 0:
                
                self.board_blanks = np.astype((self.board_value == 0),bool)
                board_spaces = np.zeros_like(self.board_value,dtype=bool)
                board_spaces[row_pos,col_pos] = True
                board_spaces_new = np.copy(board_spaces)


                while True:
                    for i in [0,1]:
                        for j in [1,-1]:
                            board_spaces_new |= (np.roll(board_spaces,shift=j,axis=i) & self.board_blanks)
                    
                    if np.array_equal(board_spaces_new,board_spaces):break
                    else: board_spaces[:]=board_spaces_new

                self.board_visible |= board_spaces

    def print(self,make_visible=False,invert=True):
        #print the current case of the board to the terminal
        sprite_board = ""
        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.board_visible[i,j] or make_visible:
                    if self.board_bomb[i,j]: sprite_board += "X"
                    elif (self.board_value[i,j] == 0): sprite_board += " "
                    else: sprite_board += str(self.board_value[i,j])
                else:
                    if self.board_flag[i,j]: sprite_board += "F"
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

