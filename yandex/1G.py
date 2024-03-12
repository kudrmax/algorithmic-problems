f = open('input.txt', 'r')
arr = []
for line in f:
    arr.append(list(map(int, line.split()))[0])

X = arr[0]  # мой мощь (хп и солдаты)
Y = arr[1]  # хп казармы
P = arr[2]  # кол-во производимых солдат

Y -= X
count = 1
while X > 0 and Y + P > 0:
    x, p = X, P
    # мой удар
    if Y > x:
        p = 0
        Y -= x - P
    elif Y <= x:
        Y = 0
        p -= x
        P = p
    # его удар
    X -= p
    count += 1

print(count)