with open('input.txt', 'r') as file:
    lines = file.readlines()

n = list(map(int, lines[0].split()))[0]
arr = []
for line in lines[1:]:
    row = [*line.strip()]
    arr.append(row)
print(arr)

def do_steps(arr, i, j, k):
    dirs = [[]]

def bs(arr):
    left, right = min(len(arr), len(arr[0])) // 3, 1
    while left < right:
        k = (left + right) // 2

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                do_steps(arr, i, j, k)

        if arr[k] < target:
            left = k + 1
        else:
            right = k
    return left
