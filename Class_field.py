import pygame
class Field():
    def __init__(self):
        pass

    def draw(self, main_display, field_x, field_y):
        for i in range(40, field_y, 40):
            pygame.draw.line(main_display, 'grey', (0, i), (field_x, i))
        for i in range(40, field_x, 40):
            pygame.draw.line(main_display, 'grey', (i, 0), (i, field_y))