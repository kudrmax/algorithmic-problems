with open('input.txt', 'r') as file:
    lines = file.readlines()

k = int(lines[0].split()[0])
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))

min_y = arr[0][1]
max_y = arr[0][1]
min_x = arr[0][0]
max_x = arr[0][0]

for x, y in arr:
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)
    # print(x, y)

print(min_x, min_y, max_x, max_y)

