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

# main.py :
      This is the file through which the game is played and hence we need to call it in the terminal. 
    
   1. Initialization :

    The program begins by importing required modules such as Pygame, system utilities, and the project files (Board, Game, gui, file_manager).
    It then:
        Initializes Pygame
        Creates the game window
        Sets the window caption
        Prepares a clock to control the game’s frame rate
    The board is created and filled with the standard checkers starting layout, and the Game class is initialized to manage turn logic, movement, and win detection.

2. Save/Load Startup Check
    
         When the program starts, it checks if a previous save file (checkers_save.txt) exists.
    
         If it does, a startup dialog appears asking the player:
```
"Previous save found — Load it? (Y/N)"
```
         Press Y → Loads the saved game state
         Press N → Starts a new game
    
         This dialog must be answered before normal gameplay begins.
    
3. Event Management :
        
        Inside the main loop, the program keeps taking inputs of user while running is True.

        a. Startup Dialog Handling:
            It blocks all input until the start-up dialogue is answered.

        b. Quit Confirmation Dialog
            When the user attempts to close the window, the game displays:
   ```
   "Save game before quitting?"
   ```
                Y : Save and quit  
                N : Quit without saving  
                ESC : Cancel and return to game  
            running=False after this and the programs tops via pygame.quit()
        
        c. Normal Gameplay Input
        Once dialogs are cleared, the game accepts normal input:
            Mouse click : To make a move
            Keyboard ‘L’ : Manually load the save file
            Window close : Trigger quit confirmation dialog and exit game.
            The mouse position is converted into board coordinates using board.get_square() and passed to game.select() to perform selection, movement, and capturing logic.

4. Graphics
        
        Each frame, the game:
            1)Clears the screen
            2)Draws the board and all pieces
            3)Highlights selected pieces and valid moves (via gui.draw())
            4)Displays dialog boxes on top when required.Rendering is updated every frame using pygame.display.flip(), and the clock ensures the game runs at the specified frames per second.
5. Saving and Exiting

         When quitting, the program uses the file_manager module to optionally save the game state. Finally, Pygame is safely shut down and the program exits.
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
                Parameters:
                window → The Pygame display surface to draw on.
                x, y → Screen coordinates (pixel position) where the piece should appear.
                radius → Size of the checker piece.

                How it works:
                ->Selects the correct color based on self.color .
                ->Draws the main filled circle of the checker.
                ->If the piece is a king, it draws a gold ring around it to visually show this.

# board.py

                  This file manages the checkerboard, including the 8×8 grid where pieces are placed drawing the board and the pieces converting mouse clicks into board positions. Here, class "Board" is created which manages entire board.
                  
                   1)__init__(self):
                  -> Creates an 8×8 matrix (list of lists) , every square starts with None, meaning there is no piece placed yet.
                  -> self.grid[row][col] will later store either None or a Piece object (red/black).
                  
                  2)setup(self):
                  -> Placement of Initial Pieces.
                  -> Places checkers on dark squares only ((i + j) % 2 != 0).
                  -> Black pieces are placed on the top 3 rows.
                  -> Red pieces are placed on the bottom 3 rows.
                  -> Matches standard Checkers rules and initializes the board for a new game.
                  
                  3)draw_squares(self, window):
                  -> Filling 8×8 grid of alternating light and dark squares.
                  -> Each square is drawn as a rectangle.
                  -> The color depends on whether (i + j) is even or odd.
                  
                  4)draw_pieces(self, window):
                  -> Drawing all pieces (circles) if they are not None.
                  -> Calls the piece’s own draw method to render it.
                  -> This displays every checker in the correct board location.
                  
                  6)draw(self, window):
                  -> Draw Entire Board
                  
                  5) get_square(self, x, y):
                  -> Converts pixel positions (from mouse click) into Grid Coordinates.
                  -> Uses integer division to figure out which square was clicked.
