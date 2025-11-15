import pygame
from piece import Piece
from constants import screen_size, square_size, light_brown, dark_brown, columns, disp, red, black
class Board():
    def __init__(self, columns):
        self.board = []
        disp.fill(light_brown)
        for i in range(columns):
            for j in range(columns):
                x = j*square_size
                y = i*square_size
                if (i + j) % 2 != 0:
                    pygame.draw.rect(disp, dark_brown, (x, y, square_size, square_size))
        self.put_pieces()
                  
    def put_pieces(self): 
        for i in range(columns):
            self.board.append([])
            for j in range(columns):
                if (i + j) % 2 != 0 and i < columns//2-1:
                    self.board[i].append(Piece(i, j, red))
                elif (i + j)%2 != 0 and i > columns//2:
                    self.board[i].append(Piece(i, j, black))
                else:
                    self.board[i].append(0)
        self.draw_pieces()

    def draw_pieces(self):
        for row in self.board:
            for piece in row:
                if piece != 0:
                    piece.draw()
    
    def move_piece(self, old_row, old_col, new_row, new_col):
        if self.board[old_row][old_col] != 0:
            self.board[old_row][old_col].move(new_row, new_col)
            self.board[new_row][new_col] = self.board[old_row][old_col]
            self.board[old_row][old_col] = 0
            pygame.draw.rect(disp, dark_brown, (old_col*square_size, old_row*square_size, square_size, square_size))
        self.draw_pieces()
  
class Select():
    def __init__(self, board):
        self.selected = None
        self.board = board

    def get_row_col(self, x, y):
        row = y//square_size
        col = x//square_size
        return (row, col)
    
    def handle_click(self, x, y):
        row, col = self.get_row_col(x, y)
        clicked_square = self.board.board[row][col]

        if self.selected == None:
            if clicked_square != 0:
               self.selected = clicked_square
               Select.highlight(row, col)

        elif isinstance(self.selected, Piece):
            Select.clear(self.selected.row, self.selected.col)
            if clicked_square == 0 and (row + col)%2 != 0:
                b.move_piece(self.selected.row, self.selected.col, row, col)
                self.selected = None
            elif clicked_square != 0:
                Select.highlight(clicked_square.row, clicked_square.col)
                self.selected = clicked_square         

    def clear(row, col):
        if (col + row)%2 != 0:
            pygame.draw.rect(disp, dark_brown, (square_size*col, square_size*row, square_size, square_size), 5)
        else:
            pygame.draw.rect(disp, light_brown, (square_size*col, square_size*row, square_size, square_size), 5)
    
    def highlight(row, col):
        pygame.draw.rect(disp, (0,255,0), (square_size*col, square_size*row, square_size, square_size), 5)
