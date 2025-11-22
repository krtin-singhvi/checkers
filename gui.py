# gui.py

import pygame
from constants import *
from game_io import pos_to_pixel_center

def draw_valid_moves(window, moves):
    # intentionally empty (we removed the green dots)
    pass

def draw_selected(window, selected):
    if selected is None:
        return
    r, c = selected
    x = c * SQUARE_SIZE
    y = r * SQUARE_SIZE
    rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(window, HIGHLIGHT_COLOR, rect, 3)

def draw(window, board, selected, valid_moves, game):
    # board draws squares + pieces
    board.draw(window)

    # draw selection outline only
    if selected is not None:
        draw_selected(window, selected)

    # draw turn text
    font = pygame.font.SysFont(None, 24)
    text = f"Turn: {game.turn}"
    surf = font.render(text, True, (0,0,0))
    window.blit(surf, (10, 10))

    # draw winner if any
    if game.winner is not None:
        big = pygame.font.SysFont(None, 48)
        win_surf = big.render(f"{game.winner.upper()} WINS", True, (0,0,0))
        wx = (WINDOW_WIDTH - win_surf.get_width()) // 2
        wy = (WINDOW_HEIGHT - win_surf.get_height()) // 2
        window.blit(win_surf, (wx, wy))
