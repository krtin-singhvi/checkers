# Checkers Game (Python + Pygame)

A classic Checkers game implemented in **Python** using **Pygame**. This project features smooth gameplay, piece movement rules, king promotion, capturing logic, and a safe file I/O system for saving and loading game state.

---

## Features

* 8×8 checkers board using dark squares
* Turn-based gameplay (Red vs. Black)
* Legal move validation
* Mandatory capturing rules
* Multi-jump support
* King promotion
* Safe and simple **Save/Load system** (text-based)
* Clean and modular object-oriented structure
* Error-proof file loading (no crashes)

---

## Controls

| Key                  | Action                        |
| -------------------- | ----------------------------- |
| **Left Mouse Click** | Select and move pieces        |
| **Y**                | Save game to `savegame.txt`   |
| **N**                | Quit the game                 |

---

## Save/Load System (Text-Based)

The game uses a custom text-based format (not JSON) for saving progress.
Example save file:

```
red
None
---b-b-b
b---b-b-
-----b-b
----b---
--------
----r-r-
---r-r-r
r-B-r-r-
```

Saved data includes:

* Board size
* Current player's turn
* All pieces (row, col, color, king-status)

The save/load system prevents crashes even if the file is corrupted.

---

## Game Rules (Short Version)

* The game is played on an 8×8 board using dark squares.
* Each player begins with 12 pieces.
* Normal pieces move diagonally **forward**.
* Capturing is **mandatory**.
* Multi-captures must continue until no further captures exist.
* Reaching the opponent's back row crowns a **King**, which can move backward.
* The game ends when one player has no legal moves or no pieces left.

---

## Installation

1. Install Python 3.x.
2. Install Pygame:

```
pip install pygame
```

3. Run the game:

```
python main.py
```

---

## Project Structure

```
checkers/

main.py            # Game loop
board.py           # Board class (movement, saving, loading)
piece.py           # Piece class (movement, king logic)
constants.py       # Colors, sizes, board settings
file_manager.py    # Auto-generated save file
checkers_save.txt  # Saving game progress as a text file
game_logic.py      # Logic of the game
gui.py             # Interface of the game
```

---

# Explanation of all files :

# main.py
      1. Game Initialization
          Starts Pygame and creates the game window
          Creates the Board and Game objects
          Automatically checks if a previous save file exists
      2. Dialog Management
            Displays two types of popup dialogs:
                  Startup dialog → “Load previous save? (Y/N)”
                  Quit dialog → “Save before quitting? (Y/N/ESC)”
                  These dialogs pause normal gameplay until answered.
      3. Input Handling
          Handles mouse clicks to select and move pieces
          Detects window close events
          Allows manual loading using the L key
          Enforces turn logic and prevents actions when the game is won
      4. Rendering
          Continuously draws:
              The board
              Pieces
              Highlights (via gui.draw())
              Dialog overlays when required
      5. Game Loop & Shutdown
          Runs the main loop at a fixed FPS, updates the display every frame, and cleanly exits when the user quits.
    
      This file acts as the central controller of the program, connecting gameplay logic, rendering, and the save/load system into one cohesive game loop.
# piece.py
                  1) __init__(self, color):
                  -> init is a constructor.
                  -> It creates a new checker piece.
                  -> It assigns a variable color.
                  -> It assigns king → False by default (regular piece).
                  -> Color will contain of piece either "black" or "red".
      
                  2) make_king(self):
                  -> Upgrades the piece to a King when it reaches the last row opponent’s side of the board, allowing it to move backwards.
      
                  3) draw(self, window, x, y, radius):
                      window → The Pygame display surface to draw on.
                      x, y → Screen coordinates (pixel position) where the piece should appear.
                      radius → Size of the checker piece.
                      ->Selects the correct color based on self.color .
                      ->Draws the main filled circle of the checker.
                      ->If the piece is a king, it draws a gold ring around it to visually show this.

# board.py

                  This file manages the checkerboard, including the 8×8 grid where pieces are placed drawing the board and the pieces converting mouse clicks into board positions. Here, class "Board" is created which manages entire board.
                  
                  1) __init__(self):
                  -> Creates an 8×8 matrix (list of lists) , every square starts with None, meaning there is no piece placed yet.
                  -> self.grid[row][col] will later store either None or a Piece object (red/black).
                  
                  2) setup(self):
                  -> Placement of Initial Pieces.
                  -> Places checkers on dark squares only ((i + j) % 2 != 0).
                  -> Black pieces are placed on the top 3 rows.
                  -> Red pieces are placed on the bottom 3 rows.
                  -> Matches standard Checkers rules and initializes the board for a new game.
                  
                  3) draw_squares(self, window):
                  -> Filling 8×8 grid of alternating light and dark squares.
                  -> Each square is drawn as a rectangle.
                  -> The color depends on whether (i + j) is even or odd.
                  
                  4) draw_pieces(self, window):
                  -> Drawing all pieces (circles) if they are not None.
                  -> Calls the piece’s own draw method to render it.
                  -> This displays every checker in the correct board location.
                  
                  6) draw(self, window):
                  -> Draw Entire Board
                  
                  5) get_square(self, x, y):
                  -> Converts pixel positions (from mouse click) into Grid Coordinates.
                  -> Uses integer division to figure out which square was clicked.

      
# gui.py

                  1) inside_board(row, col):
                  -> Checks whether a given (row, col) is inside the 8×8 board.
                  -> Returns True if the position is valid, otherwise False.
                  
                  2) pos_to_pixel_center(row, col):
                  -> Converts a board grid position to pixel coordinates.
                  -> Returns the center (x, y) of that square.
                  -> Useful for drawing pieces exactly in the middle.
                  
                  3) draw_selected(window, selected):
                  -> Draws a highlight box around the selected square.
                  -> selected contains (row, col) of the chosen piece.
                  -> Only draws the outline; does nothing if selected = None.
                  
                  4) draw(window, board, selected, valid_moves, game):
                  -> Main GUI drawing function.
                  -> Updates everything visible on the screen each frame.
                  
                  5) board.draw(window):
                  -> Tells the Board class to draw checkerboard squares and checker pieces.
                  
                  6) draw_selected(window, selected):
                  -> Highlights the currently selected piece, if any.
                  -> Draw turn text.
                  -> Creates a small font.
                  -> Renders text like: “Turn: red” or “Turn: black”.
                  -> Displays it at the top-left corner.
                  -> Draw winner text.
                  -> If game.winner is not None, then it uses a bigger font and renders “RED WINS” or “BLACK WINS” and centers it on the window.

# file_manager.py

    save_game(game) :
    1)Writes whose turn it is
        Example: "red" or "black"
    2)Writes the winner
        "None" if the game is still ongoing
        "red" or "black" if someone already won
    3)Saves the board layout (8×8)
        Each square becomes a character:
            - → empty square
            r → red piece
            b → black piece
            R → red king
            B → black king
    4)Writes all 8 board rows to the file
    If everything is successful, it prints:
```
Game Saved!
```

    load_game(game) 
        1)This function restores a previously saved game from checkers_save.txt.
        2)What it loads:
            Turn → sets game.turn
            Winner → sets game.winner
            Rebuilds the board:
                - becomes an empty square
                r/R creates a red piece (uppercase = king)
                b/B creates a black piece (uppercase = king)
            Resets selections and valid moves
                (selected = None, valid_moves = {})
    If successful, it prints:
```
Game Loaded!
```
#game_logic.py
      
      1. Track Game State
         The class stores:
              The board
              Whose turn it is (red or black)
              The currently selected piece
              All valid moves for that piece
              The winner (or None if the game is ongoing)
      2. Enforce Mandatory Capture
          Checkers requires players to capture if possible.
          This is handled by:
              piece_has_capture() – checks if a specific piece can capture
              any_capture_for_player() – checks if the current player must capture
          If a capture exists, only capturing pieces and capturing moves are allowed.
      3. Piece Selection and Movement
          select(row, col) handles both selecting a piece and moving it:
              Clicking your own piece selects it
              Clicking a valid square moves the piece
              Moves that are not allowed are ignored
              Multi-capture chains are enforced automatically
      4. Move Generation
          get_valid_moves_for(row, col) calculates all legal moves for a piece:
              Normal diagonal moves
              Capture moves over opponents
              King movement in all directions
          Returns a dictionary with destination squares and captured pieces.
      5. Applying Moves
          apply_move(start, end):
              Moves the piece on the board
              Removes any captured opponents
              Promotes the piece to king if it reaches the opposite end
              Checks for additional captures (forcing chain captures)
      6. Switching Turns
          After a valid move (unless a chain capture continues),switch_turn() changes the active player.
      7. Determining the Winner
          check_winner() checks:
            If one color has no pieces left
            Or if the current player has no valid moves
          If so, the opponent is declared the winner.
