import pygame
from Class_cell import *
from Class_field import *

def draw_screen(cell_coord, field_x, field_y):        #отрисовка экрана

    main_display = pygame.display.set_mode((field_x, field_y))
    field = Field()
    cell = Cell()
    field.draw(main_display, field_x, field_y)      #рисуем поле

    for coord in cell_coord:        #отрисовка каждой клетки
        cell.x = coord[0]
        cell.y = coord[1]
        cell.draw(main_display)
    pygame.display.update()
    return main_display