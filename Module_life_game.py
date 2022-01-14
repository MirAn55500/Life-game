import pygame
import time

from Module_draw_screen import *
from Module_change import *


def life_game(field_x, field_y, cell_coord):
    game = True
    while game:
        main_display = draw_screen(cell_coord, field_x, field_y)

        events = pygame.event.get()
        for e in events:                           #выход из игры
            if e.type == pygame.QUIT:
                game = False
                return 'Game closed!'

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                game = False
                return 'Game closed!'

        cell_coord = change(main_display)
        time.sleep(0.9)