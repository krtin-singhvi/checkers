import pygame
from constants import black, red, gold, square_size, screen_size, disp
class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.find_coord()
    
    def make_king(self):
        self.king = True
        self.color = gold
    
    def find_coord(self):
        self.x = int(square_size*(self.col + 0.5))
        self.y = int(square_size*(self.row + 0.5))
    
    def draw(self):
        radius = square_size//2 - 10
        if self.king:
            pygame.draw.circle(disp, self.color, (self.x, self.y), radius)
        else:
            pygame.draw.circle(disp, self.color, (self.x, self.y), radius)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.find_coord()
