with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
N = len(arr)
for i in range(len(arr)):
    arr[i] = [arr[i][0] - 1, arr[i][1] - 1]
print(arr, N)

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


col = 1
i, j = 0, col
print(i, j)
while True:
    i, j, flag = move_sursor(i, j, col, N - 1, N - 1)
    print(i, j)
    if not flag:
        break
    # if [i, j] in arr:
    #     print(i, j)