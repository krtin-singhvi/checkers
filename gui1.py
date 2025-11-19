from board import Board
from piece import Piece
from constants import *

class Game:
    def __init__(self, board):
        # store the board
        self.board = board

        # whose turn ("red" or "black")
        self.turn = "red"

        # currently selected piece (row, col)
        self.selected = None

        # valid moves of the selected piece:
        # format: { (r,c): [ (cap_r, cap_c), ... ] }
        self.valid_moves = {}

        # winner ("red", "black", or None)
        self.winner = None

    # --- utilities for forced captures ---
    def piece_has_capture(self, row, col):
        """Return True if piece at (row,col) has any capture move."""
        moves = self.get_valid_moves_for(row, col)
        for caps in moves.values():
            if caps:  # non-empty captured list -> capture move
                return True
        return False

    def any_capture_for_player(self):
        """Return True if current player has any capture available anywhere."""
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board.grid[r][c]
                if p is not None and p.color == self.turn:
                    if self.piece_has_capture(r, c):
                        return True
        return False

    def select(self, row, col):
        piece = self.board.grid[row][col]

        if piece is not None and piece.color == self.turn:
            # if there is a capture anywhere, only allow selecting pieces that can capture
            if self.any_capture_for_player() and not self.piece_has_capture(row, col):
                return False

            self.selected = (row, col)
            self.valid_moves = self.get_valid_moves_for(row, col)
            return True

        # If selecting an empty square that is a valid move, attempt to move
        if self.selected is not None and (row, col) in self.valid_moves:
            # if capture exists anywhere, this move MUST be a capture
            caps = self.valid_moves.get((row, col), [])
            if self.any_capture_for_player() and not caps:
                return False

            # apply move; returns True if the same piece must continue capturing
            continue_chain = self.apply_move(self.selected, (row, col))

            if continue_chain:
                # keep selected on the landing square, update valid moves to only capture moves
                er, ec = (row, col)
                self.selected = (er, ec)

                all_moves = self.get_valid_moves_for(er, ec)
                # keep only capture moves
                self.valid_moves = {m: caps for m, caps in all_moves.items() if caps}
            else:
                # done, switch turn
                self.selected = None
                self.valid_moves = {}
                self.switch_turn()
                self.check_winner()

            return True

        # otherwise clear selection
        self.selected = None
        self.valid_moves = {}
        return False
        

    def get_valid_moves_for(self, row, col):
        moves = {}
        piece = self.board.grid[row][col]

        if piece is None:
            return moves
        
        if piece.color != self.turn:
            return moves
        
        if piece.king:
            directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        else:
            if piece.color == "red":
                directions = [(-1,-1), (-1,1)]
            else:
                directions = [(1,-1), (1,1)]

        for dr, dc in directions:
            #simple move
            r = row + dr
            c = col + dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                if self.board.grid[r][c] is None:
                    moves[(r, c)] = []

            #capture
            r2 = row + 2*dr
            c2 = col + 2*dc
            mid_r = row + dr
            mid_c = col + dc
            if 0 <= r2 < ROWS and 0 <= c2 < COLS:
                mid_piece = self.board.grid[mid_r][mid_c]
                if mid_piece is not None and mid_piece.color != piece.color and self.board.grid[r2][c2] is None:
                    moves[(r2, c2)] = [(mid_r, mid_c)]

        return moves         
            
    def apply_move(self, start, end):
        sr, sc = start
        er, ec = end

        #get piece
        piece = self.board.grid[sr][sc]
        
        #move the piece on the bord
        if piece is None:
            return False
        
        self.board.grid[sr][sc] = None
        self.board.grid[er][ec] = piece

        # remove captured pieces if any
        captured = self.valid_moves.get((er, ec), [])
        for (cr, cc) in captured:
            self.board.grid[cr][cc] = None

        # kinging a piece
        if not piece.king:
            if piece.color == "red" and er == 0:
                piece.make_king()
            elif piece.color == "black" and er == ROWS - 1:
                piece.make_king()

        # After a capture, check if the same piece can capture again
        if captured:
            next_moves = self.get_valid_moves_for(er, ec)
            for caps in next_moves.values():
                if caps:  # another capture?
                    self.valid_moves = next_moves
                    return True  # must continue capturing

        # no more captures
        self.valid_moves = {}
        return False

    def switch_turn(self):
        if self.turn == "red":
            self.turn = "black"
        else:
            self.turn = "red"

    def check_winner(self):
        # count pieces
        red_count = 0
        black_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board.grid[r][c]
                if p is not None:
                    if p.color == "red":
                        red_count += 1
                    else:
                        black_count += 1
        
        if red_count == 0:
            self.winner = "black"
            return
        if black_count == 0:
            self.winner = "red"
            return
        
        # check if current player has moves
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board.grid[r][c]
                if p is not None and p.color == self.turn:
                    moves = self.get_valid_moves_for(r, c)
                    if moves:
                        self.winner = None
                        return

        self.winner = "black" if self.turn == "red" else "red"
