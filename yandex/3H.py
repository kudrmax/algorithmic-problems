import matplotlib.pyplot as plt
import numpy as np

def plot(A, B):
    A = np.array(A)
    B = np.array(B)
    for b in B:
        plt.plot(b[[0, 2]], b[[1, 3]], marker = 'o')
    for a in A:
        plt.plot(a[[0, 2]], a[[1, 3]], marker = 'o')
    plt.gca().set_aspect('equal')
    plt.show()

with open('input.txt', 'r') as file:
    lines = file.readlines()
N = int(lines[0].split()[0])
A, B = [], []
A_set, B_set = set(), set()
for line in lines[1:1 + N]:
    a = list(map(int, line.split()))
    x1, y1, x2, y2 = a
    if x1 - x2 < 0:
        x1, y1, x2, y2 = x2, y2, x1, y1
    a = x1, y1, x2, y2
    A.append(a)
    A_set.add(a)
for line in lines[1 + N:]:
    a = list(map(int, line.split()))
    x1, y1, x2, y2 = a
    if x1 - x2 < 0:
        x1, y1, x2, y2 = x2, y2, x1, y1
    a = x1, y1, x2, y2
    B.append(a)
    B_set.add(a)

# print(A_set)
# print(B_set)

# def change_coords(s):
#     x1, y1, x2, y2 = s
#     x, y = x2 - x1, y2 - y1
#     if x < 0:
#         x, y = -x, -y
#     return x, y


# for i in range(len(A)):
#     A_set[change_coords(A[i])] += 1
#     B_set[change_coords(B[i])] += 1

max_count = 0
for a in A:
    # перенос фигуры B в точку с координатами ...
    ax1, ay1, ax2, ay2 = a
    pa = ax1, ay1

    count = 0
    for b in B:
        bx1, by1, bx2, by2 = b
        pb = bx1, by1

        delta = pa[0] - pb[0], pa[1] - pb[1]

        new_b = bx1 + delta[0], by1 + delta[1], bx2 + delta[0], by2 + delta[1]
        new_bx1, new_by1, new_bx2, new_by2 = new_b

        if new_b in A_set:
            count += 1
    # print(f'{count = }')
    max_count = max(max_count, count)
print(f'{max_count = }')
print(len(A) - max_count)

print(A)
print(B)

plot(A, B)