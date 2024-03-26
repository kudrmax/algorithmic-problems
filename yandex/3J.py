from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()
n, k = list(map(int, lines[0].split()))

##################################

devices = [d for d in range(n)]
parts = [p for p in range(k)]

# print(f'{devices = }')
# print(f'{parts = }')

##################################

parts_of_device = defaultdict(set)
parts_of_device[0] = set([p for p in range(k)])
for i in range(1, n):
    parts_of_device[i] = set()
# print(f'{parts_of_device = }')

count_parts_received = [[0 for _1 in range(n)] for _2 in range(n)]

timeslot_count = [1 for _ in range(n)]


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


def get_most_valuable_device(A, Bs):
    '''
    Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
    '''
    # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
    valuable_devices = set()
    counts = count_parts_received[A]

    max_count = 0
    for B in Bs:
        count = counts[B]
        if count > max_count:
            max_count = count

    for B in Bs:
        count = counts[B]
        if count == max_count:
            valuable_devices.add(B)

    return valuable_devices


##################################
# print(f'{parts_of_device = }')

for _ in range(100000):

    # Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    count_of_parts_dict = get_count_of_parts_dict()
    sorted_parts = sorted(parts, key=lambda p: count_of_parts_dict[p])  # Отсортирую все parts по частоте отсутствия
    # print(f'{sorted_parts = }')

    # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
    # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.
    chosen_parts_dict = {}
    for d in devices:
        missing_parts = set([p for p in parts if p not in parts_of_device[d]])
        chosen_part = -1
        for missing_part in sorted_parts[::-1]:
            if missing_part in missing_parts:
                chosen_part = missing_part
        if chosen_part != -1:
            chosen_parts_dict[d] = chosen_part
        # print(f'{d = },  {chosen_part = }')

    # После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже скачана.
    # Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее количество частей обновления.
    # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
    requests_dict = defaultdict(list)  # {devise: [<devises которые сделали request>]}
    for d, _ in chosen_parts_dict.items():  # если нам вообще нужно делать запрос, то делаем запрос
        chosen_part = chosen_parts_dict[d]

        # составить список устройств, у которых есть эта часть
        devices_that_own_chosen_part = set([d for d in devices if chosen_part in parts_of_device[d]])

        # выбрать из devices_that_own_chosen_part то, на котором скачано наименьшее количество частей обновления
        parts_of_device_count = {}
        for key, val in parts_of_device.items():
            if key in devices_that_own_chosen_part:
                parts_of_device_count[key] = len(val)
        devices_that_own_chosen_part_sorted_by_count_of_parts = sorted(
            list(devices_that_own_chosen_part),
            key=lambda d: (parts_of_device_count[d], devices.index(d))
        )

        # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
        best_device = devices_that_own_chosen_part_sorted_by_count_of_parts[0]
        requests_dict[best_device].append(d)

    # После того, как все запросы отправлены, каждое устройство выбирает, чей запрос удовлетворить.
    # Устройство A удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства.
    devices_for_sending_part = {}
    for d, ds_that_make_request in requests_dict.items():

        # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
        valuable_devices = get_most_valuable_device(d, ds_that_make_request)

        # Если на устройство A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего скачанных частей обновления.
        parts_of_device_count = {}
        for key, val in parts_of_device.items():
            if key in valuable_devices:
                parts_of_device_count[key] = len(val)

        devices_that_most_valuavle_sorted_by_count_of_part = sorted(
            list(valuable_devices),
            key=lambda d: (parts_of_device_count[d], devices.index(d))
        )

        # Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.
        device_for_sending_part = devices_that_most_valuavle_sorted_by_count_of_part[0]
        devices_for_sending_part[d] = device_for_sending_part

    # Устройства, чьи запросы удовлетворены, скачивают запрошенную часть обновления, а остальные не скачивают ничего.
    for d, device_for_sending_part in devices_for_sending_part.items():
        chosen_part = chosen_parts_dict[device_for_sending_part]
        parts_of_device[device_for_sending_part].add(chosen_part)
        B = d
        A = device_for_sending_part
        count_parts_received[A][B] += 1

    # print(f'{parts_of_device = }')

    flag_to_break = True
    for d, ps in parts_of_device.items():
        if len(ps) != k and d != 0:
            timeslot_count[d] += 1
            flag_to_break = False

    if flag_to_break:
        break
    # if timeslot_count[1] > 5000:
    # print(*timeslot_count[1:])

print(*timeslot_count[1:])
