with open('input.txt', 'r') as file:
    lines = file.readlines()

arr = []
for line in lines[1:]:
    arr.append(tuple(map(int, line.strip().split())))
n = len(arr)


def get_d_positive_index(x, y):
    return y - x


def get_d_negative_index(x, y):
    x = -x
    return y - x


def get_d_positive_next_step(x, y, step):
    return x + step, y + step


def get_d_negative_next_step(x, y, step):
    return x + step, y - step


def foo():
    hy = {}
    hx = {}
    hd_positive = {}
    hd_negative = {}

    step_counter = 0

    win_counter = 0
    first_win = False
    second_win = False

    for x, y in arr:
        step_counter += 1

        ##### hy
        if y not in hy:
            hy[y] = {}
        hy[y][x] = 1
        max_counter = 0
        i = 1
        while x + i in hy[y]:
            max_counter += 1
            i += 1
        j = 1
        while x - j in hy[y]:
            max_counter += 1
            j += 1
        for k in range(x - j + 1, x + i):
            hy[y][k] = max_counter + 1
        if max_counter + 1 >= 5:
            win_counter += 1
            if step_counter % 2 != 0:
                first_win = True
            else:
                second_win = True

        ##### hx
        if x not in hx:
            hx[x] = {}
        hx[x][y] = 1
        max_counter = 0
        i = 1
        while y + i in hx[x]:
            max_counter += 1
            i += 1
        j = 1
        while y - j in hx[x]:
            max_counter += 1
            j += 1
        for k in range(y - j + 1, y + i):
            hx[x][k] = max_counter + 1
        if max_counter + 1 >= 5:
            win_counter += 1
            if step_counter % 2 != 0:
                first_win = True
            else:
                second_win = True

        ##### d_positive
        d_positive_index = get_d_positive_index(x, y)
        if d_positive_index not in hd_positive:
            hd_positive[d_positive_index] = {}
        hd_positive[d_positive_index][x] = 1
        max_counter = 0
        i = 1
        while x + i in hd_positive[d_positive_index]:
            max_counter += 1
            i += 1
        j = 1
        while x - j in hd_positive[d_positive_index]:
            max_counter += 1
            j += 1
        for k in range(x - j + 1, x + i):
            hd_positive[d_positive_index][k] = max_counter + 1
        if max_counter + 1 >= 5:
            win_counter += 1
            if step_counter % 2 != 0:
                first_win = True
            else:
                second_win = True

        ##### d_negative
        d_negative_index = get_d_negative_index(x, y)
        if d_negative_index not in hd_negative:
            hd_negative[d_negative_index] = {}
        hd_negative[d_negative_index][y] = 1
        max_counter = 0
        i = 1
        while y + i in hd_negative[d_negative_index]:
            max_counter += 1
            i += 1
        j = 1
        while y - j in hd_negative[d_negative_index]:
            max_counter += 1
            j += 1
        for k in range(y - j + 1, y + i):
            hd_negative[d_negative_index][k] = max_counter + 1
        if max_counter + 1 >= 5:
            win_counter += 1
            if step_counter % 2 != 0:
                first_win = True
            else:
                second_win = True


    if win_counter == 0:
        return 'Draw'
    if win_counter == 1:
        if first_win:
            return 'First'
        if second_win:
            return 'Second'
    return 'Inattention'


print(foo())
