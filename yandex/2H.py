with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
# print(arr)

max_el = arr[0][0]
max_indexes_x = []
max_indexes_y = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        a = arr[i][j]
        max_el = max(max_el, a)
# print(f'{max_el = }')

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == max_el:
            max_indexes_y.append(i)
            max_indexes_x.append(j)
max_indexes_y = list(set(max_indexes_y))
max_indexes_x = list(set(max_indexes_x))
# print(f'{max_indexes_y = }')
# print(f'{max_indexes_x = }')

d_y = {}
for max_index_y in max_indexes_y:
    count = 0
    for el in arr[max_index_y]:
        if el == max_el:
            count += 1
    d_y[max_index_y] = count

d_x = {}
for max_index_x in max_indexes_x:
    count = 0
    for i in range(len(arr)):
        el = arr[i][max_index_x]
        if el == max_el:
            count += 1
    d_x[max_index_x] = count

# print(f'{d_y = }')
# print(f'{d_x = }')

max_val_y = 0
for key, val in d_y.items():
    max_val_y = max(max_val_y, val)
# print(f'{max_val_y = }')

max_val_x = 0
for kex, val in d_x.items():
    max_val_x = max(max_val_x, val)
# print(f'{max_val_x = }')

max_key_y = 0
for key, val in d_y.items():
    if val == max_val_y:
        max_key_y = key
        break
# print(f'{max_key_y = }')

max_key_x = 0
for key, val in d_x.items():
    if val == max_val_x:
        max_key_x = key
        break
# print(f'{max_key_x = }')

print(f'{max_key_y + 1} {max_key_x + 1}')