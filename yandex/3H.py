import collections
import math

with open('input.txt', 'r') as file:
    lines = file.readlines()
N = int(lines[0].split()[0])
A, B = [], []
for line in lines[1:1 + N]:
    A.append(list(map(int, line.split())))
for line in lines[1 + N:]:
    B.append(list(map(int, line.split())))

# print(f'{N = }')
# print(f'{A = }')
# print(f'{B = }')

A_set = collections.defaultdict(int)
B_set = collections.defaultdict(int)


def change_coords(s):
    x1, y1, x2, y2 = s
    x, y = x2 - x1, y2 - y1
    if x < 0:
        x, y = -x, -y
    return x, y


for i in range(len(A)):
    A_set[change_coords(A[i])] += 1
    B_set[change_coords(B[i])] += 1

max_count = 0
for key_a, val_a in A_set.items():
    val_b = B_set[key_a]
    if val_b == val_a:
        max_count = max(max_count, val_a)

for key_a, val_a in B_set.items():
    val_b = A_set[key_a]
    if val_b == val_a:
        max_count = max(max_count, val_a)

print(A_set)
print(B_set)
print(max_count)
print(len(A) - max_count)

# print(A_set.symmetric_difference(B_set))

# for i in range(len(A)):
#     a = A[i]
#     for j in range(len(A)):
#         b = B[j]
