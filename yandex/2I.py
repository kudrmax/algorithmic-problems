with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
N = len(arr)
for i in range(len(arr)):
    arr[i] = [arr[i][0] - 1, arr[i][1] - 1]
# print(arr, N)

def move_sursor(i, j, zero_j, max_i, max_j):
    if j <= zero_j:
        j -= 1
        if j < 0:
            j = zero_j + 1
    elif j > zero_j:
        j += 1
    if j > max_j:
        j = zero_j
        i += 1
    if i > max_i:
        return -1, -1, False
    return i, j, True


def calc_dist(cursor_i, cursor_j, i, j):
    delta_i = cursor_i - i
    delta_j = cursor_j - j
    dist = abs(delta_i) + abs(delta_j)
    return dist



col = 1
i, j = 0, col
cursor_i = 0
res = 0
while True:
    if [i, j] in arr:
        dist = calc_dist(cursor_i, col, i ,j)
        res += dist
        cursor_i += 1

    i, j, flag = move_sursor(i, j, col, N - 1, N - 1)
    if not flag:
        break

print(res)
