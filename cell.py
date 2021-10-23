import pygame


WHITE = (255, 255, 255)
PURPLE = (200, 0, 255)
GREEN = (0, 255, 0)


class Cell:
    def __init__(self, loc):
        self.loc = loc
        self.top, self.right, self.bottom, self.left = True, True, True, True
        self.is_visited = False
        self.is_current = False
        
        
    def show(self, screen, size):
        x, y = self.loc
        x, y = x * size, y*size
        if self.top:
            pygame.draw.line(screen, WHITE, (x, y), (x + size, y))  # Top
        if self.left:
            pygame.draw.line(screen, WHITE, (x, y), (x, y + size))  # Left
        if self.right:
            pygame.draw.line(screen, WHITE, (x + size, y),
                             (x + size, y + size))  # Right
        if self.bottom:
            pygame.draw.line(screen, WHITE, (x, y + size),
                             (x + size, y + size))  # Bottom
         
        if self.is_current:
            self.is_visited = True
            pygame.draw.rect(screen, GREEN, (x + 1, y + 1, size, size))
        elif self.is_visited:
            pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, size, size))
