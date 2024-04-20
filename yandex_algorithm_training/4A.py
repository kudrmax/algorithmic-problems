with open('input.txt', 'r') as file:
    lines = file.readlines()

N = list(map(int, lines[0].split()))[0]
arr = list(map(int, lines[1].split()))
k = list(map(int, lines[2].split()))[0]
pairs = []
for line in lines[3:]:
    pair = tuple(map(int, line.split()))
    if len(pair) > 0:
        pairs.append(pair)
arr.sort()
# print(arr)
# print(pairs)


def bs_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def bs_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


for L, R in pairs:
    l = bs_left(arr, L)
    r = bs_right(arr, R)
    count = r - l
    print(count, end=' ')