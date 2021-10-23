import pygame
import sys
import numpy as np

from pygame.locals import KEYDOWN, K_q
from cell import Cell


def show_cells():
    for i in range(ROWS):
        for j in range(COLS):
            cells[i, j].show(screen, SIZE)


HEIGHT, WIDTH = 600, 600
SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROWS, COLS = HEIGHT // SIZE, WIDTH // SIZE
pygame.init()


temp = []
for i in range(ROWS):
    for j in range(COLS):
        cell = Cell((i, j))
        temp.append(cell)
cells = np.array(temp)
cells.shape = ROWS, COLS      


screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Maze Generator")
screen.fill(BLACK)
show_cells()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()