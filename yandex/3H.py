# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def plot(A, B):
#     A = np.array(A)
#     B = np.array(B)
#     for b in B:
#         plt.plot(b[[0, 2]], b[[1, 3]], marker='o')
#     for a in A:
#         plt.plot(a[[0, 2]], a[[1, 3]])
#     plt.gca().set_aspect('equal')
#     plt.show()


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

max_count = 0
for a in A:
    ax1, ay1, ax2, ay2 = a
    pa = ax1, ay1
    for b in B:
        bx1, by1, bx2, by2 = b
        pb = bx1, by1
        delta = pa[0] - pb[0], pa[1] - pb[1]

        count = 0
        for bb in B:
            bx1, by1, bx2, by2 = bb
            new_b = bx1 + delta[0], by1 + delta[1], bx2 + delta[0], by2 + delta[1]
            if new_b in A_set:
                count += 1
        # print(f'{count = }, {delta = }')
        max_count = max(max_count, count)
# print(f'{max_count = }')
print(len(A) - max_count)

# print(A)
# print(B)

# plot(A, B)