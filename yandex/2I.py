with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
n = len(arr)
for i in range(len(arr)):
    arr[i] = [arr[i][0] - 1, arr[i][1] - 1]
print(arr, n)

def do_step(i, j, dir):
    return i + dir[0], j + dir[1]


def check_boundaries(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    return True


dir_left = [0, -1]
dir_right = [0, 1]

def calc_dir(i, j, this_i, this_j):
    # print(i, j)
    return 0

for col_number in range(n):
    count = 0
    # filled_arr = [False for _ in range(n)]
    # print(filled_arr)
    # i, j = 0, col_number
    # while True:
    #     i, j = do_step(i, j, dir_left)
    #     check_boundaries(i, j)
    this_i = 0
    this_j = col_number
    i = this_i
    j = this_j
    while i < len(arr):
        while j < len(arr):
            print(i ,j)
            if [i, j] in arr:
                count += calc_dir(i, j, this_i, this_j)
                break
            j += 1
        i += 1


