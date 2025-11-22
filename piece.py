import pygame
from constants import *

class Piece:
    def __init__(self, color):
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True

    def draw(self, window, x, y, radius):
        if self.color == "red":
            color = RED_COLOR
        elif self.color == "black":
            color = BLACK_COLOR
        pygame.draw.circle(window, color, (x,y), radius)
        if self.king:
            pygame.draw.circle(window, GOLD, (x,y), radius, 3)
