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
print(f'{parts_of_device = }')

count_parts_received = [[0 for _1 in range(n)] for _2 in range(n)]


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
    valuable_devices = []
    counts = count_parts_received[A]

    max_count = 0
    for B in Bs:
        count = counts[B]
        if count > max_count:
            max_count = count

    for B in Bs:
        count = counts[B]
        if count == max_count:
            valuable_devices.append(B)

    return valuable_devices


##################################

for i in range(1):
    # Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    count_of_parts_dict = get_count_of_parts_dict()
    sorted_parts = sorted(parts, key=lambda p: count_of_parts_dict[p])  # Отсортирую все parts по частоте отсутствия
    # print(count_of_parts_dict)
    # print(sorted_parts)

    # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
    # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.
    chosen_parts_dict = {}
    for d in devices:
        missing_parts = set([p for p in parts if p not in parts_of_device[d]])
        chosen_part = -1
        for missing_part in sorted_parts:
            if missing_part in missing_parts:
                chosen_part = missing_part
        if chosen_part != -1:
            chosen_parts_dict[d] = chosen_part
        print(f'{d = },  {chosen_part = }')

    # После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже скачана.
    # Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее количество частей обновления.
    # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
    requests_dict = defaultdict(list)  # {devise: [<devises которые сделали request>]}
    for d in devices:
        if d in chosen_parts_dict:  # если нам вообще нужно делать запрос, то делаем запрос
            print(f'\nfor {d = }')
            chosen_part = chosen_parts_dict[d]

            # составить список устройств, у которых есть эта часть
            devices_that_own_chosen_part = set([d for d in devices if chosen_part in parts_of_device[d]])
            print(f'{devices_that_own_chosen_part = }')

            # выбрать из devices_that_own_chosen_part то, на котором скачано наименьшее количество частей обновления
            parts_of_device_count = {}
            for key, val in parts_of_device.items():
                if key in devices_that_own_chosen_part:
                    parts_of_device_count[key] = len(val)
            print(f'{parts_of_device_count = }')
            sorted_by_count_of_part_devices_that_own_chosen_part = sorted(
                list(devices_that_own_chosen_part),
                key=lambda d: (parts_of_device_count[d], devices.index(d))
            )
            print(f'{sorted_by_count_of_part_devices_that_own_chosen_part = }')

            # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
            pass

            if len(sorted_by_count_of_part_devices_that_own_chosen_part) > 0:
                best_device = sorted_by_count_of_part_devices_that_own_chosen_part[0]
                requests_dict[best_device].append(d)
    print(f'\n{requests_dict = }')

    # После того, как все запросы отправлены, каждое устройство выбирает, чей запрос удовлетворить.
    # Устройство A удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства.
    devices_for_sending_part = {}
    for d, ds_that_make_request in requests_dict.items():
        print(d, ds_that_make_request)

        # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
        valuable_devices = set(get_most_valuable_device(d, ds_that_make_request))
        print(f'{valuable_devices = }')

        # Если на устройство A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего скачанных частей обновления.
        parts_of_device_count = {}
        for key, val in parts_of_device.items():
            if key in valuable_devices:
                parts_of_device_count[key] = len(val)

        sorted_by_count_of_part_devices_that_most_valuavle = sorted(
            list(valuable_devices),
            key=lambda d: (parts_of_device_count[d], devices.index(d))
        )
        # print(f'{sorted_by_count_of_part_devices_that_most_valuavle = }')

        # Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.
        pass

        device_for_sending_part = sorted_by_count_of_part_devices_that_most_valuavle[0]
        devices_for_sending_part[d] = device_for_sending_part
        print(f'{device_for_sending_part = }')
    