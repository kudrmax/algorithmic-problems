f = open('input.txt', 'r')
arr = []
for line in f:
    arr.append(list(map(int, line.split()))[0])

x = arr[0]  # мой мощь (хп и солдаты)
y = arr[1]  # хп казармы
p = arr[2]  # кол-во производимых солдат

y -= x
c = 1

while True:

    if y == 0:
        if x >= p:
            c += 1
            break
        else:  # x < p
            if x > p - x:
                c += 2
                break
            else:  # x <= p - x
                c = -1
                break
    else:  # y != 0
        if y > x:
            y -= (x - p)
        else:  # y <= x
            # тут должен быть перебор
            y = 0
            p -= x - y

    c += 1

print(c)
