with open('input.txt', 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines[1:]:
    line = line.rstrip('\n')
    row = list(map(str, line))
    matrix.append(row)

n, m = len(matrix), len(matrix[0])
print(n, m)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '#':
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

print(matrix)


# 1. Найти три точки
# 2. Найти все возможные прямоугольники по этим трем точкам
# 3. Понять является ли оставшаяся фигура прямоугольником

# dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def do_step(i, j, max_i, max_j):
    j += 1
    if j >= max_j:
        j = 0
        i += 1
    if i >= max_i:
        return -1, -1, False
    return i, j, True


black1 = [0, 0]
i, j = 0, 0
while True:

    if matrix[i][j] == 1:
        black1 = [i, j]
        break
    i, j, flag = do_step(i, j, n, m)
    if not flag:
        break

i, j = black1
while j < m and matrix[i][j] == 1:
    j += 1
black2 = [i, j - 1]

i, j = black2
while i < n and matrix[i][j] == 1:
    i += 1
black3 = [i - 1, j]

black4 = [black3[0], black1[1]]
print(black1)
print(black2)
print(black3)
print(black4)

new_matrix = matrix.copy()

print(black1[0], black4[0] + 1)
print(black1[1], black2[1] + 1)
for i in range(black1[0], black4[0] + 1):
    for j in range(black1[1], black2[1] + 1):
        # print(i, j)
        new_matrix[i][j] = 0
print(new_matrix)


