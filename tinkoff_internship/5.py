n = int(input().strip())
arrs = [[0, 0, 0]]
for _ in range(n):
    arrs.append(input().strip())
# print(arrs)

prev_row = [0, 0, 0]

max_val = max(prev_row)

for i in range(1, len(arrs)):
    row = []
    for j in range(3):
        p = arrs[i][j]
        value = 0
        if p == 'C':
            value = 1
        elif p == 'W':
            value = -float('inf')
        if j == 0:
            value += max(prev_row[:-1])
        elif j == 1:
            value += max(prev_row)
        elif j == 2:
            value += max(prev_row[1:])
        row.append(value)

    prev_row = row
    max_val = max(max_val, *prev_row)

print(max_val)
