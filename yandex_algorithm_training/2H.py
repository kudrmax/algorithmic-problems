with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split(' '))))
# print(arr)

max_el = arr[0][0]
max_index = [0, 0]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        a = arr[i][j]
        if a > max_el:
            max_el = a
            max_index = [i, j]

d_list = []

for k in range(2):

    d = {}
    if k == 0:
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

    # print(f'{max_el = }')
    # print(f'{max_index = }')
    # print(f'{second_max_el = }')
    # print(f'{second_max_index = }')
    # print(d)
    # print(f'{third_max_el = }')
    # print(f'{third_max_index = }')
    # print(f'{row} {col}')

    d_list.append(d)

# print(d_list)

d_max = []
max_el_list = []
for d in d_list:
    max_el = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            already_checked = i == d['row'] or j == d['col']
            if not already_checked:
                max_el = max(max_el, arr[i][j])
    max_el_list.append(max_el)
# print(max_el_list)

index = max_el_list.index(min(max_el_list))

row = d_list[index]['row'] + 1
col = d_list[index]['col'] + 1
print(f'{row} {col}')