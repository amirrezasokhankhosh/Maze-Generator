import pygame


WHITE = (255, 255, 255)


class Cell:
    def __init__(self, loc):
        self.loc = loc
        self.top, self.right, self.bottom, self.left = True, True, True, True

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
