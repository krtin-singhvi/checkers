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
│
├── main.py            # Game loop
├── board.py           # Board class (movement, saving, loading)
├── piece.py           # Piece class (movement, king logic)
├── constants.py       # Colors, sizes, board settings
├── savegame.txt       # Auto-generated save file
└── README.md
```

---

# Explanation of all files :

* main.py :
    * This is the file through which the game is played and hence we need to call it in the terminal. 
    
    # Initialization :
        
        1) The initial import lines of code import the necessary modules and files such as pygame GUI and the file manager so that we can run the game and keep saving the progress while the game is played.

        2) Pygame is initialized and the window to play the game is opened via pygame.display.set_mode() function and is initialized as an object. The window then gets a caption "Checkers" at its top via pygame.display.set_caption() function. A clock is then set to control the game's frame rate via pygame.time.Clock() function. 

        3) The board is created and filled with the standard checkers starting layout, and the Game class is initialized to manage turn logic, movement, and win detection.
    
    # Save/Load Check :
        
        When the program starts, it checks if a previous save file (checkers_save.txt) exists. If it does exist then a start-up dialog appears in the game and asks the user whether we want to load the previous game from where we left it. If we enter Y, then we get the previous game restored and ready to play . If we enter N , it starts a new game.
    
    # Event Management :
        Inside the main loop, the program keeps taking inputs of user while running is True.

        a. Startup Dialog Handling:
            It blocks all input until the start-up dialogue is answered.

        b. Quit Confirmation Dialog
            When the user attempts to close the window, the game displays:
                "Save game before quitting?"
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

    # Graphics
        Each frame, the game:
            1)Clears the screen
            2)Draws the board and all pieces
            3)Highlights selected pieces and valid moves (via gui.draw())
            4)Displays dialog boxes on top when required.Rendering is updated every frame using pygame.display.flip(), and the clock ensures the game runs at the specified frames per second.
    # Saving and Exiting
        When quitting, the program uses the file_manager module to optionally save the game state. Finally, Pygame is safely shut down and the program exits.
