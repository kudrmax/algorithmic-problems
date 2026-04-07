from collections import deque

# with open('input.txt') as file:
#     lines = file.readlines()
#
# n, m = tuple(map(int, lines[0].split()))
# arr = []
# for line in lines[1:]:
#     s, t = tuple(map(int, line.split()))
#     arr.append((s, t))


n, m = tuple(map(int, input().split()))
arr = []
for _ in range(m):
    s, t = tuple(map(int, input().split()))
    arr.append((s, t))


def get_arr_with_min(arr, w):
    """
    Создание массива минимумов в окне ширины w через monotonic stack за O(len(arr))
    """
    n = len(arr)
    if w == 0 or n == 0:
        return []
    if w == 1:
        return arr

    deq = deque()
    result = []

    # обрабатываем первые w элементов
    for i in range(w):
        while deq and arr[i] <= arr[deq[-1]]:
            deq.pop()
        deq.append(i)
    result.append(arr[deq[0]])  # минимум первого окна

    # обрабатываем оставшиеся элементы
    for i in range(w, n):
        while deq and deq[0] <= i - w:  # удаляем из deq все то, что не входит в окно
            deq.popleft()
        while deq and arr[i] <= arr[deq[-1]]:  # удаляем из deq все то, что больше
            deq.pop()
        deq.append(i)
        result.append(arr[deq[0]])

    return result


dp_left, dp_right = [float('inf') for _ in range(n)], [float('inf') for _ in range(n)]

# заполняем dp_left в самом начале — dp_left[i] — сколько минимум шагов нужно, чтобы сдвинуть поезд в данную клетку
up, down = arr[0]
for i in range(n):
    if i + 1 < up:
        dp_left[i] = up - i - 1
    elif i + 1 > down:
        dp_left[i] = i + 1 - down
    else:
        dp_left[i] = 0
# print(f'{(up, down) = }')
# print(f'{dp_left = }\n')

for up, down in arr[1:]:
    # print(f'{(up, down) = }')
    # двигаем окно
    row = 0
    for x in range(-(up - 1), n - down + 1):
        window_up = up - 1 + x  # верхняя позиция окна
        window_down = down - 1 + x  # нижняя позиция окна

        # минимальное количество действий, которые нужно сделать,
        # чтобы все, что находится слева от платформы было связным
        arr_with_min = get_arr_with_min(dp_left,
                                        window_down - window_up + 1)  # массив с минимуми (через monotonic stack)
        delta = abs(x) + arr_with_min[row]  # O(m * n) — итоговая ассимптотика
        # delta = abs(x) + min(dp_left[window_up:window_down + 1])  # O(m * n^2) — ассимптотика в данном случае

        # заполняем dp_right, причем всегда храним мимальное значение
        for i in range(window_up, window_down + 1):
            dp_right[i] = min(dp_right[i], delta)
        row += 1
        # print(f'{x = }\t{dp_right = }')

    dp_left = dp_right
    dp_right = [float('inf') for _ in range(n)]
    # print(f'{dp_left = }')
    # print()

# print(f'ans = {min(dp_left)}')
print(min(dp_left))
