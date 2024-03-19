with open('input.txt', 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines[1:]:
    line = line.rstrip('\n')
    row = list(map(str, line))
    matrix.append(row)

n, m = len(matrix), len(matrix[0])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '#':
            matrix[i][j] = 1
        # else:
        #     matrix[i][j] = 0


def do_step(i, j, max_i, max_j):
    j += 1
    if j >= max_j:
        j = 0
        i += 1
    if i >= max_i:
        return -1, -1, False
    return i, j, True


def find_4_points(matrix, n, m):
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
        if j + 1 < m and i < n:
            if matrix[i][j + 1] == 1:
                # i += 1
                break
    black3 = [i - 1, j]

    black4 = [black3[0], black1[1]]
    return black1, black2, black3, black4

def calc_area(matrix, black1, black2, black3, black4):
    count_black = 0
    for i in range(black1[0], black4[0] + 1):
        for j in range(black1[1], black2[1] + 1):
            if matrix[i][j] == 1:
                count_black += 1
    delta_i = abs((black1[0] - black4[0])) + 1
    delta_j = abs((black1[1] - black2[1])) + 1
    count_black_in_theory = delta_i * delta_j
    return count_black == count_black_in_theory


from copy import deepcopy


def foo(matrix, n, m):
    black1, black2, black3, black4 = find_4_points(matrix, n, m)
    # print(black1, black2, black3, black4)

    if not calc_area(matrix, black1, black2, black3, black4):
        return False, []

    matrix_new = deepcopy(matrix)

    # print(black1[0], black4[0] + 1)
    # print(black1[1], black2[1] + 1)
    for i in range(black1[0], black4[0] + 1):
        for j in range(black1[1], black2[1] + 1):
            matrix_new[i][j] = 'b'
    # print(matrix_new)

    min_i, max_i = 100000, -1
    min_j, max_j = 100000, -1

    count_black = 0
    count_white = 0
    for i in range(n):
        for j in range(m):
            if matrix_new[i][j] == 1:
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)
                count_black += 1
            if matrix_new[i][j] == 'b':
                count_white += 1
    # print([min_i, min_j], [max_i, max_j])
    # print(f'{count_black = }')
    # print(matrix_new)
    if count_black == 0:
        if count_white == 1:
            return False, []
        flag = True
        for i in range(n):
            for j in range(m):
                if matrix_new[i][j] == 'b':
                    flag = False
                if not flag and matrix_new[i][j] == 'b':
                    matrix_new[i][j] = 'a'
            if not flag:
                break

        count_row = 0
        for i in range(n):
            for j in range(m):
                if matrix_new[i][j] == 'a':
                    count_row += 1
                    break
                if matrix_new[i][j] == 'b':
                    count_row = 0

        if count_row == 1:
            flag = True
            for i in range(n):
                for j in range(m):
                    if matrix_new[i][j] == 'a':
                        matrix_new[i][j] = 'b'
                        flag = False
                        break
                if not flag:
                    break
        return True, matrix_new
    delta_i = (max_i - min_i) + 1
    delta_j = (max_j - min_j) + 1
    count_black_in_theory = delta_i * delta_j

    # print(f'{count_black_in_theory = }')
    flag = count_black == count_black_in_theory
    if flag:
        for i in range(n):
            for j in range(m):
                if matrix_new[i][j] == 1:
                    matrix_new[i][j] = 'a'
                if matrix_new[i][j] == 0:
                    matrix_new[i][j] = '.'
    # print(matrix_new)
    return flag, matrix_new


flag1, m1 = foo(matrix, n, m)

matrix_T = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
flag2, m2 = foo(matrix_T, m, n)

def print_matrix(matrix):
    # print(n, m)
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end='')
        print()

if flag1:
    print('YES')
    # print(m1)
    print_matrix(m1)
elif flag2:
    print('YES')
    m2 = [[m2[j][i] for j in range(len(m2))] for i in range(len(m2[0]))]
    print_matrix(m2)
else:
    print('NO')
