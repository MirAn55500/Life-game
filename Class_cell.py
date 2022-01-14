import pygame
class Cell():
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, main_display):
        pygame.draw.circle(main_display, 'green', (self.x, self.y), 15)