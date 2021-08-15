def game_core3():
    count = 0  # Создаём счётчик
    n_1, n_2 = 0, 101  # вводим 2 переменные и присваиваем им значения (начальное и конечное)
    comparison = 0
    while comparison != '=':  # Угадываем число, пока оно не будет равно загаданному
        count += 1
        num = round((n_1 + n_2) / 2)  # Вначале находим значение середины заданного поля поиска
        print(num)
        comparison = input("Угадал '=', больше '>' ,меньше '<': ")  # Сравниваем предложенное число с загаданным

        if comparison == '<':
            n_2 = num
        elif comparison == '>':
            n_1 = num
        print(f"Попыток {count} Загаданное число {num}")  # данный алгоритм позволяет угадывать число за 5-7 попыток
    return {comparison}
