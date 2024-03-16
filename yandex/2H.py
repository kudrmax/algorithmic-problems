with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
# print(arr)

d = {}

max_el = arr[0][0]
max_index = [0, 0]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        a = arr[i][j]
        if a > max_el:
            max_el = a
            max_index = [i, j]

second_max_el = -1
second_max_index = [0, 0]
for j in range(len(arr[0])):  # прохожусь по строке
    i = max_index[0]
    a = arr[i][j]
    if a >= second_max_el:
        if [i, j] != max_index:
            second_max_el = a
            second_max_index = [i, j]
for j in range(len(arr)):  # прохожусь по столбцу
    i = max_index[1]
    a = arr[i][j]
    if a >= second_max_el:
        if [i, j] != max_index:
            second_max_el = a
            second_max_index = [i, j]

if max_index[0] == second_max_index[0]:
    d['row'] = max_index[0]
else:
    d['col'] = max_index[1]

third_max_index = [0, 0]
third_max_el = -1
for i in range(len(arr)):
    for j in range(len(arr[0])):
        a = arr[i][j]
        if 'row' in d:
            already_checked = i == d['row']
        else:
            already_checked = j == d['col']
        if not already_checked:
            if a > third_max_el:
                third_max_el = a
                third_max_index = [i, j]

if 'row' in d:
    d['col'] = third_max_index[1]
else:
    d['row'] = third_max_index[0]

row = d['row'] + 1
col = d['col'] + 1

print(f'{max_el = }')
print(f'{max_index = }')
print(f'{second_max_el = }')
print(f'{second_max_index = }')
print(d)
print(f'{third_max_el = }')
print(f'{third_max_index = }')

print(f'{row} {col}')
