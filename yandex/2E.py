with open('input.txt', 'r') as file:
    lines = file.readlines()

n = list(map(int, lines[0].split()))[0]
lines = lines[1:]

a, b = [], []

for line in lines:
    arr = list(map(int, line.split(' ')))
    a.append(arr[0])
    b.append(arr[1])

delta = []
for i in range(n):
    delta.append(a[i] - b[i])

positive_indexes = []
for i in range(n):
    if delta[i] > 0:
        positive_indexes.append(i)

negative_indexes = []
for i in range(n):
    if delta[i] <= 0:
        negative_indexes.append(i)

delta_sum = 0
for i in positive_indexes:
    delta_sum += delta[i]

arr = [-1 for i in range(n)]
for i in positive_indexes:
    arr[i] = delta_sum + b[i]

max_positive_index = -1
max_positive = 0
for i in positive_indexes:
    if arr[i] > max_positive and arr[i] != -1:
        max_positive = arr[i]
        max_positive_index = i

max_a_after_b = max_positive - b[max_positive_index] if len(positive_indexes) > 0 else 0

max_negative = max_a_after_b
max_negative_index = max_positive_index
for i in negative_indexes:
    if max_a_after_b + a[i] > max_negative:
        max_negative = max_a_after_b + a[i]
        max_negative_index = i

max_val = max_positive if max_positive > max_negative else max_negative
max_val_index = max_positive_index if max_positive > max_negative else max_negative_index
is_negative = False if max_positive > max_negative else True
print(max_val)

indexes = []

if not is_negative:
    for i in positive_indexes:
        if i != max_positive_index:
            indexes.append(i)
    indexes.append(max_positive_index) if len(positive_indexes) > 0 else 0
    for i in negative_indexes:
        indexes.append(i)
else:
    for i in positive_indexes:
        if i != max_positive_index:
            indexes.append(i)
    indexes.append(max_positive_index) if len(positive_indexes) > 0 else 0
    indexes.append(max_negative_index)
    for i in negative_indexes:
        if i != max_negative_index:
            indexes.append(i)

for index in indexes:
    print(index + 1, end=' ')

# print()
# print(f'{indexes = }')
# print('1 6 3 4 0 2 5')
# # print('2 7 4 5 1 3 6')
# print(f'{a = }')
# print(f'{b = }')
# print(f'{delta = }')
# print(f'{positive_indexes = }')
# print(f'{negative_indexes = }')
# print(f'{delta_sum = }')
# print(f'{arr = }')
# print(f'{max_positive = }')
# print(f'{max_negative = }')
# print(f'{max_positive_index = }')
# print(f'{max_a_after_b = }')
# print(f'{is_negative = }')







# summ = 0
# max_vall = 0
# for i in indexes:
#     summ += a[i]
#     if max_vall < summ:
#         max_vall = summ
#     summ -= b[i]
#     if max_vall < summ:
#         max_vall = summ
# print(summ)
# print(max_vall)