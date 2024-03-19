cursor_i, cursor_j = 0, 0


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
print(move_sursor(0, 4, 3, N - 1, N - 1))
