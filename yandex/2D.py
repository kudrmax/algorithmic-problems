with open('input.txt', 'r') as file:
    lines = file.readlines()

n = list(map(int, lines[0].split()))[0]

arr = []
for line in lines[1:]:
    line = line.rstrip('\n')
    row = list(map(int, line.split()))
    arr.append(row)

# print(arr, n)

matrix = []
for i in range(11):
    row = [0 for _ in range(11)]
    matrix.append(row)

# for i in range(10):
#     for j in range(10):
#         if i == 0 or i == 9 or j == 0 or j == 9:
#             matrix[i][j] = 0

# print(matrix)

dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

for i, j in arr:
    matrix[i + 1][j + 1] = 1

res = 0
for i, j in arr:
    for dir in dirs:
        el = matrix[i + 1 + dir[0]][j + 1 + dir[1]]
        if el == 0:
            res += 1

print(res)
