from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()
n, k = list(map(int, lines[0].split()))

##################################

devices = [d for d in range(n)]
parts = [p for p in range(k)]

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
    count_of_parts = {}
    for p in parts:
        count_of_parts[p] = get_count_of_part(p)
    return count_of_parts


for i in range(1):
    # Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    count_of_parts = get_count_of_parts_dict()
    # Отсортирую все parts по частоте отсутствия
    count_of_parts_list = sorted(parts, key=lambda p: count_of_parts[p])
    print(count_of_parts)
    print(count_of_parts_list)

    # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
    # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.
    for d in devices:
        # print(parts_of_device[d])
        missing_parts = [p for p in parts if p not in parts_of_device[d]]
        # print(missing_parts)
        for missing_part in missing_parts:
            pass


