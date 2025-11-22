# filio stuff - small helpers used by GUI / main

from constants import SQUARE_SIZE, ROWS, COLS

def inside_board(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS

def pos_to_pixel_center(row, col):
    x = SQUARE_SIZE * (col + 0.5)
    y = SQUARE_SIZE * (row + 0.5)
    return int(x), int(y)
