import pygame
from sys import exit
pygame.init()

width,height = 480,480
rows,cols = 8,8
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()

RED = (200, 30, 30)
WHITE = (245, 245, 245)
HIGHLIGHT_FILL = (255, 255, 0, 80)   # yellow, with alpha for translucent fill
HIGHLIGHT_BORDER = (255, 220, 0)     # brighter yellow for border

sq = width//cols

selected = None

highlight_surf = pygame.Surface((sq,sq),pygame.SRCALPHA)
highlight_surf.fill(HIGHLIGHT_FILL)

def draw_board():
    for row in range(rows):
        for col in range(cols):
            x = col * sq
            y = row * sq
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = RED
            pygame.draw.rect(screen, color, (x, y, sq, sq))

def draw_highlight():
    if selected is None:
        return
    row, col = selected
    x = col * sq
    y = row * sq
    screen.blit(highlight_surf, (x, y))
    border_rect = pygame.Rect(x + 2, y + 2, sq - 4, sq - 4)
    pygame.draw.rect(screen, HIGHLIGHT_BORDER, border_rect, width=4, border_radius=6)

def get_square_under_mouse(pos):
    mx, my = pos
    if mx < 0 or mx >= width or my < 0 or my >= height:
        return None
    col = mx // sq
    row = my // sq
    return (row, col)

def main_loop():
    global selected
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                square = get_square_under_mouse(event.pos)
                if square is None:
                    selected = None
                elif selected == square:
                    selected = None
                else:
                    selected = square

        draw_board()
        draw_highlight()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main_loop()
