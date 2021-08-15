def splash_screen():
    print("    XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX")
    print("           | Игра крестики-нолики |      ")
    print("    ------------------------------------  ")
    print("    первая координата - это номер строки")
    print("    вторая координата - номер столбца   ")
    print("    ------------------------------------  ")


def yes_no():
    ask = None
    while ask not in ['yes']:
        ask = input("\nСыграем в игру? Введите 'Yes': ").lower()
    return ask


def start():
    while True:
        if yes_no() == "y":
            print("Начинаем игру")
        continue


field = [[" "] * 3 for i in range(3)]


def board():
    print(f" | 0 | 1 | 2 | ")
    print("---------------")
    for i in range(3):
        print(f"{i}| {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("---------------")
    print()


def chek():
    while True:
        step = input("Ваш ход:  ").split()

        if len(step) != 2:
            print(" Введите две координаты:  ")
            continue

        x, y = step

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win():
    combinations = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                    ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for step in combinations:
        symbols = []
        for a in step:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


splash_screen()

yes_no()

variable = 0

while True:

    variable += 1

    board()

    if variable % 2 == 1:
        print(" Ходит крестик")
    else:
        print(" Ходит нолик")

    x, y = chek()

    if variable % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if variable == 9:
        print(" Ничья")
        break
