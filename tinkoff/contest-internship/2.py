n, m = tuple(map(int, input().strip().split()))
arr = []
for i in range(m):
    row = [0 for j in range(n)]
    arr.append(row)

for i in range(n):
    row = list(map(int, input().strip().split()))
    for j in range(len(row)):
        arr[j][n - 1 - i] = row[j]

for i in range(m):
    print(*arr[i], sep=' ')