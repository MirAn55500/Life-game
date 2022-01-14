import pygame

from Class_cell import *
from Class_field import *

from Module_life_game import *

input_field_x = 25      #вводим размеры поля
input_field_y = 20
input_coord = [(6, 6), (7, 6), (6, 7), (5, 6), (14, 11)]        #вводим начальные координаты клеток

field_x = input_field_x * 40      #размеры поля на экране
field_y = input_field_y * 40
start_cell_coord = [(i[0]*40+20, i[1]*40+20) for i in input_coord]      #начальные координаты клеток на экране

life_game(field_x, field_y, start_cell_coord)
