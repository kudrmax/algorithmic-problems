import math

with open('input.txt', 'r') as file:
    lines = file.readlines()
N = int(lines[0].split()[0])
A, B = [], []
for line in lines[1:1 + N]:
    A.append(list(map(int, line.split())))
for line in lines[1 + N:]:
    B.append(list(map(int, line.split())))

print(f'{N = }')
print(f'{A = }')
print(f'{B = }')

A_set = set()
B_set = set()

def get_angle(s):
    x1, y1, x2, y2 = s
    if x2 - x1 == 0:
        return math.pi
    return math.atan((y2 - y1) / (x2 - x1))

for i in range(len(A)):
    A_set.add(get_angle(A[i]))
    B_set.add(get_angle(B[i]))

print(A_set)
print(B_set)

print(A_set.symmetric_difference(B_set))

# for i in range(len(A)):
#     a = A[i]
#     for j in range(len(A)):
#         b = B[j]
