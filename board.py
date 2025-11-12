import pygame
from piece import piece
from constants import screen_size, square_size, light_brown, dark_brown, columns, disp, red, black
class board():
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
                    self.board[i].append(piece(i, j, black))
                elif (i + j)%2 != 0 and i > columns//2:
                    self.board[i].append(piece(i, j, red))
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
