str_to_int = {
    'MON': 0,
    'TUE': 1,
    'WED': 2,
    'THU': 3,
    'FRI': 4,
    'SAT': 5,
    'SUN': 6,
}

arr = [0 for _ in range(29)]
arr[-1] = 1

for week_number in range(4):
    line = input()
    if line != '':
        for day in list(line.split()):
            day_number = week_number * 7 + str_to_int[day]
            arr[day_number] = 1

p1 = -1
max_delta = 0
max_p1, max_p2 = 0, 0

for p2 in range(0, 29):
    if arr[p2] == 0:
        continue
    else:
        delta = p2 - p1 - 1
        if delta > max_delta:
            max_delta = delta
            max_p1, max_p2 = p1 + 1, p2 - 1
        p1 = p2

if max_delta == 0:
    print('0 0')
else:
    print(max_p1 + 1, max_p2 + 1)
