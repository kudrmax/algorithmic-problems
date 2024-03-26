from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()
n, k = list(map(int, lines[0].split()))

##################################

devices = [d for d in range(n)]
parts = [p for p in range(k)]

print(f'{devices = }')
print(f'{parts = }')

##################################

parts_of_device = defaultdict(set)
parts_of_device[0] = set([p for p in range(k)])
for i in range(1, n):
    parts_of_device[i] = set()
# print(parts_of_device)

##################################

def get_count_of_part(p):
    '''
    Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    '''
    count = 0
    for key, val in parts_of_device.items():
        if p in val:
            count += 1
    return count


def get_count_of_parts_dict():
    '''
    Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    '''
    count_of_parts = {}
    for p in parts:
        count_of_parts[p] = get_count_of_part(p)
    return count_of_parts


for i in range(1):
    # Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    count_of_parts_dict = get_count_of_parts_dict()
    sorted_parts = sorted(parts, key=lambda p: count_of_parts_dict[p]) # Отсортирую все parts по частоте отсутствия
    # print(count_of_parts_dict)
    # print(sorted_parts)

    # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
    # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.
    for d in devices:
        missing_parts = set([p for p in parts if p not in parts_of_device[d]])
        this_missing_part = -1
        for missing_part in sorted_parts:
            if missing_part in missing_parts:
                this_missing_part = missing_part
        print(f'{d = },  {this_missing_part = }')


