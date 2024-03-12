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

print(f'{a = }')
print(f'{b = }')
print(f'{delta = }')

positive_indexes = []
for i in range(n):
    if delta[i] > 0:
        positive_indexes.append(i)

negative_indexes = []
for i in range(n):
    if delta[i] <= 0:
        negative_indexes.append(i)

print(f'{positive_indexes = }')
print(f'{negative_indexes = }')

delta_sum = 0
for i in positive_indexes:
    delta_sum += delta[i]
print(f'{delta_sum = }')

arr = [-1 for i in range(n)]
for i in positive_indexes:
    arr[i] = delta_sum + b[i]

print(f'{arr = }')

max_a_index = 0
max_a = 0
for i in positive_indexes:
    if arr[i] > max_a:
        max_a = arr[i]
        max_a_index = i

print(f'{max_a = }')
print(f'{max_a_index = }')

max_a_after_b = a[max_a_index] - b[max_a_index]

print(f'{max_a_after_b = }')

res = max_a_after_b
for i in negative_indexes:
    if max_a_after_b + a[i] > res:
        res = max_a_after_b + a[i]

print(max(res, max_a))