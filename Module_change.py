from Module_search import *


def change(main_display):
    new_cells = []
    for field_x in range(20, 620, 40):
        for field_y in range(20, 620, 40):
            neighbours, state = search(main_display, field_x, field_y)
            if state and neighbours == 2 or neighbours == 3:        #первое условие существования клетки
                new_cells.append((field_x, field_y))
            elif not state and neighbours == 3:         #второе условие существования клетки
                new_cells.append(field_x, field_y)
    return new_cells