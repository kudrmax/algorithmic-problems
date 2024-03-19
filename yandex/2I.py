with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
N = len(arr)
for i in range(len(arr)):
    arr[i] = [arr[i][0] - 1, arr[i][1] - 1]

arr_set = set()
for i, j in arr:
    arr_set.add((i, j))
arr = arr_set

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
    return abs(cursor_i - i) + abs(cursor_j - j)


min_res = 1000000000
for col in range(N):
    i, j = 0, col
    cursor_i = 0
    res = 0
    while True:
        if (i, j) in arr:
            res += calc_dist(cursor_i, col, i, j)
            cursor_i += 1
        i, j, flag = move_sursor(i, j, col, N - 1, N - 1)
        if not flag:
            break
    min_res = min(min_res, res)
    # res_list.append(res)
    # print(res)

print(min_res)
# print(min(res_list))
