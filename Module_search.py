def search(main_display, field_x, field_y):     #функция поиска соседних живых клеток
    count = 0

    for neighbour_x in range(field_x - 40, field_x + 80, 40):
        for neighbour_y in range(field_y - 40, field_y + 80, 40):
            try:
                if neighbour_x == field_x and neighbour_y == field_y:       #запоминаем статус поля, у которого ищем соседей
                    state = main_display.get_at((neighbour_x, neighbour_y))[1]
                    continue
                elif main_display.get_at((neighbour_x, neighbour_y))[1]:      #проверка, есть ли на поле клетка
                    count += 1
            except IndexError:
                pass
    return count, state