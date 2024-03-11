count_of_days_in_month = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31,
}

month_number = {
    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11,
}

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
           'December']

day_of_week_to_index = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_day_of_week(day, month, day_of_week_of_1_jun):
    total_day = 0
    for i in range(month_number[month]):
        total_day += count_of_days_in_month[monthes[i]]
    total_day += day
    total_day %= 7
    index = ((day_of_week_to_index[day_of_week_of_1_jun] + total_day) - 1) % 7
    return days_of_week[index]


f = open('input.txt', 'r')
lines = f.readlines()
N = int(lines[0])
year = int(lines[1])

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    count_of_days_in_month['February'] += 1

day_of_week = lines[-1].rstrip('\n')

dates = []
for i in range(2, N + 2):
    line = lines[i].rstrip('\n')
    day, month = list(line.split(' '))
    day = int(day)
    date = {
        'day': day,
        'month': month,
        'day_of_week': get_day_of_week(day, month, day_of_week)
    }
    dates.append(date)

# print(f'{N = }')
# print(f'{year = }')
# print(f'{dates = }')
# print(f'{day_of_week = }')

count_of_days_of_weeks = [52 for i in range(7)]

count_of_days_of_weeks[day_of_week_to_index[day_of_week]] += 1

# print(count_of_days_of_weeks)

count_of_weekends_of_holidays = [0 for i in range(7)]

for date in dates:
    day_of_week = date['day_of_week']
    count_of_weekends_of_holidays[day_of_week_to_index[day_of_week]] += 1

# print(count_of_days_of_weeks)
# print(count_of_weekends_of_holidays)

best_day = 0
best_sum = 0
worst_day = 0
worst_sum = 10000
for day_index in range(7):
    lst = [0 for i in range(7)]
    for j in range(7):
        lst[j] += count_of_weekends_of_holidays[j]
    lst[day_index] = count_of_days_of_weeks[day_index]
    my_sum = sum(lst)
    if my_sum > best_sum:
        best_day = day_index
        best_sum = my_sum
    if my_sum < worst_sum:
        worst_day = day_index
        worst_sum = my_sum
print(days_of_week[best_day], days_of_week[worst_day])
# print(count_of_weekends_of_holidays)

# sum_of_wekkends = [0 for i in range(7)]
# for i in range(7):
#     sum_of_wekkends[i] = count_of_weekends_of_holidays[i] + count_of_days_of_weeks[i]
#
# print(sum_of_wekkends)

# my_list = []
# for i in range(7):
#     if count_of_weekends_of_holidays[i] != 0:
#         new_list = count_of_days_of_weeks.copy()
#     else:
#         new_list = [0 for i in range(7)]
#         for j in range(7):
#             new_list[j] = count_of_days_of_weeks[j]
#             if j != i:
#                 new_list[j] += count_of_weekends_of_holidays[i]
#     my_list.append(new_list)
#
# print(count_of_days_of_weeks)
# print(count_of_weekends_of_holidays)
#
# import numpy as np
# print(np.array(my_list))
#
# max_max_index = 0
# min_min_index = 0
# max_max_val = 0
# min_min_val = 0
# for lst in my_list:
#     max_val = max(lst)
#     min_val = min(lst)
#     max_index = lst.index(max_val)
#     min_index = lst.index(min_val)
#     if max_val > max_max_val:
#         max_max_val = max_val
#         max_max_index = max_index
#     if min_val < min_min_val:
#         min_min_val = min_val
#         min_min_index = min_index
#     # max_max_index = max(max_max_index, max_index)
#     # min_min_index = min(min_min_index, min_index)
#
# print(max_max_index, min_min_index)
# print(days_of_week[max_max_index], days_of_week[min_min_index])
