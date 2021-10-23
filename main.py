import pygame
import sys
import numpy as np
import random
import time

from pygame.locals import KEYDOWN, K_q
from cell import Cell


def unvisited_left():
    for i in range(ROWS):
        for j in range(COLS):
            if cells[i, j].is_visited == False:
                return True
    return False


def show_cells():
    for i in range(ROWS):
        for j in range(COLS):
            cells[i, j].show(screen, SIZE)


def find_neighbours(i, j, arr):

    neighbors = []

    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
        # corners
        new_neighbors = []
        if i != 0:
            new_neighbors.append(arr[i - 1, j])  # top neighbor
        if j != len(arr[i]) - 1:
            new_neighbors.append(arr[i, j + 1])  # right neighbor
        if i != len(arr) - 1:
            new_neighbors.append(arr[i + 1, j])  # bottom neighbor
        if j != 0:
            new_neighbors.append(arr[i, j - 1])  # left neighbor

    else:
        # add neighbors
        new_neighbors = [
            arr[i - 1, j],  # top neighbor
            arr[i, j + 1],  # right neighbor
            arr[i + 1, j],  # bottom neighbor
            arr[i, j - 1],   # left neighbor
        ]

    return new_neighbors


def check_neighbours(current):
    i, j = current.loc
    neighbours = find_neighbours(i, j, cells)
    unvisited = []
    for neighbour in neighbours:
        if neighbour.is_visited == False:
            unvisited.append(neighbour)
    return unvisited


def choose_next_cell(current):
    i_c, j_c = current.loc
    cells[i_c, j_c].is_current = False
    unvisited = check_neighbours(current)
    if len(unvisited) != 0:
        next_cell = random.choice(unvisited)
        remove_walls(current, next_cell)
        i, j = next_cell.loc
        cells[i, j].is_current = True
        current = cells[i, j]
        stack.append(current)
        return True, current
    else:
        
        return False, None


def remove_walls(current, next_cell):
    x_c, y_c = current.loc
    x_n, y_n = next_cell.loc

    if x_c - 1 == x_n:
        # left
        cells[x_c, y_c].left = False
        cells[x_n, y_n].right = False
    elif x_c + 1 == x_n:
        # right
        cells[x_c, y_c].right = False
        cells[x_n, y_n].left = False
    elif y_c - 1 == y_n:
        # up
        cells[x_c, y_c].top = False
        cells[x_n, y_n].bottom = False
    elif y_c + 1 == y_n:
        # down
        cells[x_c, y_c].bottom = False
        cells[x_n, y_n].top = False


HEIGHT, WIDTH = 400, 400
SIZE = 40
BLACK = (0, 0, 0)
WHITE = (245, 255, 255)
PURPLE = (200, 0, 255)
ROWS, COLS = HEIGHT // SIZE, WIDTH // SIZE
pygame.init()


temp = []
for i in range(ROWS):
    for j in range(COLS):
        cell = Cell((i, j))
        temp.append(cell)
cells = np.array(temp)
cells.shape = ROWS, COLS
stack = []

current = cells[0, 0]
current.is_current = True
stack.append(current)


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
    if unvisited_left():
        b, temp = choose_next_cell(current)
        if b:
            current = temp
        else:
            current = stack.pop()
            i, j = current.loc
            cells[i, j].is_current = True
            
        show_cells()
        pygame.display.update()
    time.sleep(.5)
