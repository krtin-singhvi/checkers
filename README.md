# Checkers Game (Python + Pygame)

A simple 1v1 checkers game with GUI, kinging, multi-captures, and save/load support.

## How to Run

```bash
pip install pygame
python main.py
```

## Controls

* **Left-click** a piece to select it.
* **Left-click** a highlighted square to move.
* Pieces become **king** when they reach the opposite side.

## Save / Load

The game uses `checkers_save.txt` automatically.

### On Starting

If a save exists:

* Press **Y** → Load previous game
* Press **N** → Start a new game

### On Quit

Closing the window shows a quit dialog:

* Press **Y** → Save and quit
* Press **N** → Quit without saving
* Press **ESC** → Cancel and return to game

## Files

* `main.py` – Main game loop
* `board.py` – Board rendering
* `piece.py` – Piece & king logic
* `game_logic.py` – Movement, captures, turn handling
* `gui.py` – Drawing UI elements
* `file_manager.py` – Save / load system
* `constants.py` – Colors, sizes, FPS
