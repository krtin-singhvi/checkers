import pygame
from constants import *
from piece import Piece

class Board:
    def __init__(self):
        # create an 8x8 grid filled with None
        self.grid = []
        for i in range(ROWS):
            self.grid.append([])
            for j in range(COLS):
                self.grid[i].append(None)
        

    def setup(self):
        # place pieces in starting positions on dark squares
        # top 3 rows = black, bottom 3 rows = red
        for i in range(ROWS):
            for j in range(COLS):
                if (i +j)%2 != 0 and i<ROWS//2 -1:
                    self.grid[i][j] = Piece("black") 
                elif (i +j)%2 != 0 and i>ROWS//2:
                    self.grid[i][j] = Piece("red")    
                else:
                    self.grid[i][j] = None 

    def draw_squares(self, window):
        # draw 8x8 alternating light/dark squares
        for i in range(ROWS):
            for j in range(COLS):
                rect = (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                if (i + j)%2 !=0:
                    pygame.draw.rect(window, DARK_COLOR, rect)
                else:
                    pygame.draw.rect(window, LIGHT_COLOR, rect)                 
        

    def draw_pieces(self, window):
        # loop through grid; if there is a piece, tell it to draw itself
        for i in range(ROWS):
            for j in range(COLS):
                piece = self.grid[i][j]
                if piece is not None:
                    x = SQUARE_SIZE * (j + 0.5)
                    y = SQUARE_SIZE * (i + 0.5)
                    radius =  SQUARE_SIZE // 2 - 10
                    piece.draw(window, x, y, radius)
        

    def draw(self, window):
        self.draw_squares(window)
        self.draw_pieces(window)
        

    def get_square(self, x, y):
        # convert pixel x,y to board row,col
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
