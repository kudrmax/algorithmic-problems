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


def find_4_points(matrix):
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
    return black1, black2, black3, black4

black1, black2, black3, black4 = find_4_points(matrix)
print(black1, black2, black3, black4)

matrix_new = matrix.copy()

print(black1[0], black4[0] + 1)
print(black1[1], black2[1] + 1)
for i in range(black1[0], black4[0] + 1):
    for j in range(black1[1], black2[1] + 1):
        matrix_new[i][j] = 0
print(matrix_new)

min_i, max_i = 100000, -1
min_j, max_j = 100000, -1

count_black = 0
for i in range(n):
    for j in range(m):
        if matrix_new[i][j] == 1:
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)
            count_black += 1
print([min_i, min_j], [max_i, max_j])
print(f'{count_black = }')

delta_i = max_i - min_i + 1
delta_j = max_j - min_j + 1
count_black_in_theory = delta_i * delta_j

print(f'{count_black_in_theory = }')