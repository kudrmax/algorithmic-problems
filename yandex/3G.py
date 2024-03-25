import matplotlib.pyplot as plt
import numpy as np


def print_plot(arr):
    arr = np.array(arr)
    plt.scatter(arr[:, 0], arr[:, 1])
    plt.show()


def find_two_points(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    b1_x, b1_y = (float(0.5 * ((x1 + x2) + (y2 - y1))), float(0.5 * ((y1 + y2) + (x1 - x2))))
    b2_x, b2_y = (float(0.5 * ((x1 + x2) - (y2 - y1))), float(0.5 * ((y1 + y2) - (x1 - x2))))

    flag = True
    for obj in [b1_x, b1_y, b2_x, b2_y]:
        if obj % 1 != 0:
            flag = False

    # print((b1_x, b1_y), (b2_x, b2_y), flag)

    b1_x = round(b1_x)
    b1_y = round(b1_y)
    b2_x = round(b2_x)
    b2_y = round(b2_y)

    b1, b2 = (b1_x, b1_y), (b2_x, b2_y)

    return b1, b2, flag


def foo(N, arr):
    s = set(arr)
    # print(N, arr, s)

    if N == 1:
        p = arr[0]
        point_coords = [
            [p[0] + 1, p[1]],
            [p[0], p[1] + 1],
            [p[0] + 1, p[1] + 1]
        ]
        return 3, point_coords

    point_count = 2
    b1, b2, flag = find_two_points(arr[0], arr[1])
    point_coords = [b1, b2]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            a1, a2 = arr[i], arr[j]
            b1, b2, flag = find_two_points(arr[i], arr[j])

            if flag:
                if b1 in s and b2 in s:
                    return 0, []

                if b1 in s and b2 not in s:
                    point_count = 1
                    point_coords = [b2]

                if b2 in s and b1 not in s:
                    point_count = 1
                    point_coords = [b1]

            # print(a1, a2, b1, b2)
    return point_count, point_coords


with open('input.txt', 'r') as file:
    lines = file.readlines()
N = int(lines[0].split()[0])
arr = []
for line in lines[1:]:
    arr.append(tuple(map(int, line.split())))

point_count, point_coords = foo(N, arr)

print(point_count)
for p in point_coords:
    print(*p, sep=' ')

# print_plot(arr)