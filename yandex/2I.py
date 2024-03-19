def move_sursor(i, j, zero_j, max_i, max_j):
    if j <= zero_j:
        j -= 1
    if j < 0:
        j = zero_j + 1
    if j >= max_j:
        j = zero_j
        i += 1
    if i >= max_i:
        return -1, -1, False
    return i, j, True


N = 5
col = 3
i, j = 0, col
while True:
    i, j, flag = move_sursor(i, j, col, N - 1, N - 1)
    if not flag:
        break
    # if [i, j] in 