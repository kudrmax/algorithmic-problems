# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

with open('input.txt', 'r') as file:
    lines = file.readlines()

N = list(map(int, lines[0].split()))[0]
arr = list(map(int, lines[1].split()))
k = list(map(int, lines[2].split()))[0]
pairs = []
for line in lines[3:]:
    pair = tuple(map(int, line.split()))
    pairs.append(pair)

for L, R in pairs:
    if L > R:
        continue
    left = binary_search(arr, L)
    right = binary_search(arr, R)
    if left == -1:
        pass