import pygame
import sys
import os
from pygame.locals import *

from constants import *
from board import Board
from game_logic import Game
import gui
import file_manager
from pygame.locals import *
pygame.init()
disp = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()

board = Board()
board.setup()
game = Game(board)
# Check if save file exists
if os.path.exists("checkers_save.txt"):
    show_startup_dialog = True
else:
    show_startup_dialog = False

show_quit_dialog = False

# main loop
running = True
while running:
    for event in pygame.event.get():
        
     
        if show_startup_dialog:
            if event.type == KEYDOWN:
                if event.key == K_y:
                    file_manager.load_game(game)
                    show_startup_dialog = False
                elif event.key == K_n:
                    show_startup_dialog = False
            elif event.type == QUIT:
                running = False

        # quit dialog logic
        elif show_quit_dialog:
            if event.type == KEYDOWN:
                if event.key == K_y:
                    file_manager.save_game(game)
                    running = False
                elif event.key == K_n:
                    running = False
                elif event.key == K_ESCAPE:
                    show_quit_dialog = False # cancel quit
            elif event.type == QUIT:
                running = False

        # normal game logic
        else:
            if event.type == QUIT:
                show_quit_dialog = True #trigger quit dialog

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and game.winner is None:
                mx, my = pygame.mouse.get_pos()
                row, col = board.get_square(mx, my)
                game.select(row, col)
            

    #drawing
    disp.fill((0,0,0))
    gui.draw(disp, board, game.selected, game.valid_moves, game)

    # draw overlays on top
    if show_startup_dialog:
        gui.draw_dialog_box(disp, [
            "Previous save found!",
            "Load it? (Y/N)"
        ])
    elif show_quit_dialog:
        gui.draw_dialog_box(disp, [
            "Save game before quitting?",
            "Press 'Y' to Save, 'N' to Quit",
            "Press 'ESC' to Cancel"
        ])
        
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()

