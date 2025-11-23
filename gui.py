import pygame
from constants import *

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
def draw_dialog_box(window, lines):
    #draws the dialog box that appears while opening closing
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill((0,0,0))
    window.blit(overlay, (0,0))

    # box dimensions
    box_w, box_h = 400, 160
    box_x = (WINDOW_WIDTH - box_w) // 2
    box_y = (WINDOW_HEIGHT - box_h) // 2
    
    # draw Box
    pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, box_w, box_h))
    pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_w, box_h), 3)

    # draw Text
    font = pygame.font.SysFont(None, 32)
    for i, line in enumerate(lines):
        text_surf = font.render(line, True, (0,0,0))
        # Center text horizontally in the box
        text_x = box_x + (box_w - text_surf.get_width()) // 2
        text_y = box_y + 30 + (i * 40)
        window.blit(text_surf, (text_x, text_y))
