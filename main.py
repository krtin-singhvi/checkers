# finally game runs from here

import pygame
from constants import *
from board import Board
from game_logic import Game
import gui
import sys
from pygame.locals import *

pygame.init()
disp = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()

board = Board()
board.setup()
game = Game(board)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and game.winner is None:
            mx,my = pygame.mouse.get_pos()
            row,col = board.get_square(mx,my)
            game.select(row,col)

    disp.fill((0,0,0))
    gui.draw(disp, board, game.selected, game.valid_moves, game)
    pygame.display.flip()
    clock.tick(FPS)



