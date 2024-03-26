from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()
n, k = list(map(int, lines[0].split()))

##################################

devices = [d for d in range(n)]
parts = [p for p in range(k)]
parts_set = set([p for p in range(k)])

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

# def get_count_of_part(p):
#     '''
#     Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
#     '''
#     count = 0
#     for key, val in parts_of_device.items():
#         if p in val:
#             count += 1
#     return count
#
#
# def get_count_of_parts_dict():
#     '''
#     Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
#     '''
#     count_of_parts = {}
#     for p in parts:
#         count_of_parts[p] = get_count_of_part(p)
#     return count_of_parts

def get_count_of_parts_dict():
    '''
    Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    '''
    count_of_parts = defaultdict(int)
    for d, ps in parts_of_device.items():
        for p in ps:
            count_of_parts[p] += 1
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

count_of_parts_in_device_dict = defaultdict(int)
for key, val in parts_of_device.items():
    count_of_parts_in_device_dict[key] = len(val)

for _ in range(100000):

    # Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть
    count_of_parts_dict = get_count_of_parts_dict()

    requests_dict = defaultdict(list)  # {devise: [<devises которые сделали request>]}
    chosen_parts_dict = {}
    for d in devices:
        # missing_parts = set([p for p in parts if p not in parts_of_device[d]])
        missing_parts = parts_set.difference(parts_of_device[d])
        chosen_part = float('inf')
        chosen_part_index = float('inf')
        chosen_part_count = float('inf')
        for missing_part in missing_parts:
            count = count_of_parts_dict[missing_part]
            if count < chosen_part_count:
                chosen_part = missing_part
                chosen_part_count = count
            elif count == chosen_part_count:
                if missing_part < chosen_part:
                    chosen_part = missing_part
                    chosen_part_count = count
        if chosen_part != float('inf'):
            chosen_parts_dict[d] = chosen_part

        # После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже скачана.
        # Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее количество частей обновления.
        # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
        # for d, _ in chosen_parts_dict.items():  # если нам вообще нужно делать запрос, то делаем запрос
        #     chosen_part = chosen_parts_dict[d]

        # составить список устройств, у которых есть эта часть
        devices_that_own_chosen_part = set([d_i for d_i in devices if chosen_part in parts_of_device[d_i]])

        # выбрать из devices_that_own_chosen_part то, на котором скачано наименьшее количество частей
        min_count = float('inf')
        min_device = float('inf')
        for valuable_device in devices_that_own_chosen_part:
            count = count_of_parts_in_device_dict[valuable_device]
            if count < min_count:
                min_device = valuable_device
                min_count = count
            elif count == min_count:
                if valuable_device < min_device:
                    min_device = valuable_device
                    min_count = count
        best_device = min_device
        # parts_of_device_count = {}
        # for key, val in parts_of_device.items():
        #     if key in devices_that_own_chosen_part:
        #         parts_of_device_count[key] = len(val)
        # devices_that_own_chosen_part_sorted_by_count_of_parts = sorted(
        #     list(devices_that_own_chosen_part),
        #     key=lambda d: (parts_of_device_count[d], devices.index(d))
        # )

        # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
        # if len(devices_that_own_chosen_part_sorted_by_count_of_parts) > 0:
        #     best_device = devices_that_own_chosen_part_sorted_by_count_of_parts[0]
        if best_device != float('inf'):
            requests_dict[best_device].append(d)

    # После того, как все запросы отправлены, каждое устройство выбирает, чей запрос удовлетворить.
    # Устройство A удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства.
    devices_for_sending_part = {}
    for d, ds_that_make_request in requests_dict.items():

        # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
        valuable_devices = get_most_valuable_device(d, ds_that_make_request)

        # Если на устройство A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего скачанных частей обновления.

        min_count = float('inf')
        min_device = float('inf')
        for valuable_device in valuable_devices:
            count = count_of_parts_in_device_dict[valuable_device]
            if count < min_count:
                min_device = valuable_device
                min_count = count
            elif count == min_count:
                if valuable_device < min_device:
                    min_device = valuable_device
                    min_count = count
        best_device = min_device



        # parts_of_device_count = {}
        # for key, val in parts_of_device.items():
        #     if key in valuable_devices:
        #         parts_of_device_count[key] = len(val)
        #
        # devices_that_most_valuavle_sorted_by_count_of_part = sorted(
        #     list(valuable_devices),
        #     key=lambda d: (parts_of_device_count[d], devices.index(d))
        # )
        #
        # # Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.
        # device_for_sending_part = devices_that_most_valuavle_sorted_by_count_of_part[0]
        # devices_for_sending_part[d] = device_for_sending_part
        devices_for_sending_part[d] = best_device

    # Устройства, чьи запросы удовлетворены, скачивают запрошенную часть обновления, а остальные не скачивают ничего.
    for d, device_for_sending_part in devices_for_sending_part.items():
        chosen_part = chosen_parts_dict[device_for_sending_part]
        parts_of_device[device_for_sending_part].add(chosen_part)
        B = d
        A = device_for_sending_part
        count_parts_received[A][B] += 1
        count_of_parts_in_device_dict[device_for_sending_part] += 1

    # for key, val in parts_of_device.items():
    #     count_of_parts_in_device_dict[key] = len(val)

    # print(f'{parts_of_device = }')

    flag_to_break = True
    for d in devices[1:]:
        if count_of_parts_in_device_dict[d] != k:
            timeslot_count[d] += 1
            flag_to_break = False

    if flag_to_break:
        break
    # print(*timeslot_count[1:])

print(*timeslot_count[1:])

# s1 = '5394 4883 1317 5430 6458 6447 2322 2897 5701 6419 5702 5261 4891 6150 6459 6166 6275 5232 6417 6266 6459 4894 5202 5793 3898 5790 6452 6030 4531 6154 6460 6363 4993 6337 4032 6458 5252 6114 6461 3910 6245 3408 4123 6235 6462 4261 6421 4279 6443 5391 5619 6461 4969 6244 4563 5990 6107 3788 3903 6094 4934 6264 6460 5794 6067 5498 6451 5425 5768 6462 5801 3466 6457 5530 6341 5944 6391 3367 6060 6036 5434 6172 6455 5922 4124 6463 4966 6435 6463 6339 6209 6464 6254 6464 5293 6465 5003 4242 4197'
# s2 = ' '.join([str(ch) for ch in timeslot_count[1:]])
#
# print(s1 == s2)
