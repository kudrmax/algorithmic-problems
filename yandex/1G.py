f = open('input.txt', 'r')
arr = []
for line in f:
    arr.append(list(map(int, line.split()))[0])

x = arr[0]  # мой мощь (хп и солдаты)
y = arr[1]  # хп казармы
delta_p = arr[2]  # кол-во производимых солдат

p = 0

y -= x
if y != 0:
    p = delta_p
c = 1

while True:

    if x <= 0:
        c = -1
        break

    if y == 0:
        # мой ход
        if x >= p:
            c += 1
            break
        else:  # x < p
            if x > delta_p - x:
                c += 2
                break
            else:  # x <= p - x
                c = -1
                break
    else:  # y != 0
        if y > x:
            y -= (x - delta_p)
            p = 0
        else:  # y <= x
            # тут должен быть перебор
            # p -= x - y
            # y = 0
            if x >= p:
                y -= (x - p)
                p = 0
            else:  # x < p
                p -= x

    if p < 0:
        p = 0

    # его ход
    x -= p
    if y != 0:
        p += delta_p

    c += 1

print(c)
