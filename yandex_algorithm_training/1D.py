f = open('input.txt', 'r')

field = []
for line in f:
    line = line.rstrip('\n')
    row = list(map(str, line))
    field.append(row)

ans = [[0 for i in range(8)] for j in range(8)]

def do_step(i, j, step):
    new_i = i + step[0]
    new_j = j + step[1]
    flag = True
    if new_i < 0 or new_j < 0 or new_i >= 8 or new_j >= 8:
        flag = False
    return new_i, new_j, flag

def do(i, j, field, ans):
    new_i, new_j = i, j
    while True:
        new_i, new_j, flag = do_step(new_i, new_j, step)
        if not flag:
            break
        if field[new_i][new_j] != '*':
            break
        ans[new_i][new_j] = 1


for i in range(8):
    for j in range(8):
        figure = field[i][j]
        if figure == 'R':
            ans[i][j] = 1
            for step in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                do(i, j, field, ans)
        if figure == 'B':
            ans[i][j] = 1
            for step in [[-1, -1], [1, 1], [1, -1], [-1, 1]]:
                do(i, j, field, ans)

count = 0
for i in range(8):
    for j in range(8):
        count += ans[i][j]

print(64 - count)
