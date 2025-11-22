import pygame
import sys
import os
from pygame.locals import *

from constants import *
from board import Board
from game_logic import Game
import gui
import file_manager

pygame.init()
disp = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()

board = Board()
board.setup()
game = Game(board)

# --- STATE VARIABLES ---
# Check if save file exists immediately
if os.path.exists("checkers_save.txt"):
    show_startup_dialog = True
else:
    show_startup_dialog = False

show_quit_dialog = False

# --- HELPER FUNCTIONS ---
def draw_dialog_box(window, lines):
    """Helper to draw a generic white box with text lines."""
    # Dark overlay
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill((0,0,0))
    window.blit(overlay, (0,0))

    # Box dimensions
    box_w, box_h = 400, 160
    box_x = (WINDOW_WIDTH - box_w) // 2
    box_y = (WINDOW_HEIGHT - box_h) // 2
    
    # Draw Box
    pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, box_w, box_h))
    pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_w, box_h), 3)

    # Draw Text
    font = pygame.font.SysFont(None, 32)
    for i, line in enumerate(lines):
        text_surf = font.render(line, True, (0,0,0))
        # Center text horizontally in the box
        text_x = box_x + (box_w - text_surf.get_width()) // 2
        text_y = box_y + 30 + (i * 40)
        window.blit(text_surf, (text_x, text_y))

# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        
        # 1. STARTUP DIALOG LOGIC
        if show_startup_dialog:
            if event.type == KEYDOWN:
                if event.key == K_y:
                    file_manager.load_game(game)
                    show_startup_dialog = False
                elif event.key == K_n:
                    show_startup_dialog = False
                # We block QUIT here so they must choose Y or N
            elif event.type == QUIT:
                # If they close the window during startup, just exit
                running = False

        # 2. QUIT DIALOG LOGIC
        elif show_quit_dialog:
            if event.type == KEYDOWN:
                if event.key == K_y:
                    file_manager.save_game(game)
                    running = False
                elif event.key == K_n:
                    running = False
                elif event.key == K_ESCAPE:
                    show_quit_dialog = False # Cancel quit
            elif event.type == QUIT:
                running = False

        # 3. NORMAL GAME LOGIC
        else:
            if event.type == QUIT:
                show_quit_dialog = True # Trigger quit dialog

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and game.winner is None:
                mx, my = pygame.mouse.get_pos()
                row, col = board.get_square(mx, my)
                game.select(row, col)
            
            # Optional: Keep 'L' to load manually if needed
            elif event.type == KEYDOWN:
                if event.key == K_l:
                    file_manager.load_game(game)

    # --- DRAWING ---
    disp.fill((0,0,0))
    
    # Always draw the game board in the background
    gui.draw(disp, board, game.selected, game.valid_moves, game)

    # Draw overlays on top
    if show_startup_dialog:
        draw_dialog_box(disp, [
            "Previous save found!",
            "Load it? (Y/N)"
        ])
    elif show_quit_dialog:
        draw_dialog_box(disp, [
            "Save game before quitting?",
            "Press 'Y' to Save, 'N' to Quit",
            "Press 'ESC' to Cancel"
        ])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()