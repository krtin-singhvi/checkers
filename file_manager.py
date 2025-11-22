import os
from constants import ROWS, COLS
from piece import Piece

SAVE_FILE = "checkers_save.txt"

''' save game in the format
red (current turn)
None (winner)(if any)
---R----
-b------
----b--R
--------
--------
--r-----
--------
r------B
(the above given board is just an example)
r = red piece , R = red king
b = black piece, B = black king
'''
def save_game(game):
    with open(SAVE_FILE, "w") as f:
        f.write(f"{game.turn}\n")
        
        winner_str = str(game.winner) if game.winner is not None else "None"
        f.write(f"{winner_str}\n")

        for row in range(ROWS):
            row_str = ""
            for col in range(COLS):
                piece = game.board.grid[row][col]
                if piece is None:
                    row_str += "-"
                else:
                    char = piece.color[0]
                    if piece.king:
                        char = char.upper()
                    row_str += char
            f.write(f"{row_str}\n")
    print("Game Saved!")
    
#load game through checkers_save.txt file
def load_game(game):
    if not os.path.exists(SAVE_FILE):
        print("No save file found.")
        return


    with open(SAVE_FILE, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    game.turn = lines[0]
    if lines[1] == "None":
        game.winner = None
    else:
        game.winner = lines[1]

    # reset grid and update to old state
    for r in range(ROWS):
        row_data = lines[r + 2]
        for c in range(COLS):
            char = row_data[c]
            if char == "-":
                game.board.grid[r][c] = None
            else:
                color = "red" if char.lower() == "r" else "black"
                new_piece = Piece(color)
                if char.isupper():
                    new_piece.make_king()
                game.board.grid[r][c] = new_piece
    
    # clear selection
    game.selected = None
    game.valid_moves = {}
    print("Game Loaded!")
