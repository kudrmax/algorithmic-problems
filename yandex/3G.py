import matplotlib.pyplot as plt
import numpy as np


def print_plot(arr):
    arr = np.array(arr)
    plt.scatter(arr[:, 0], arr[:, 1])
    plt.show()


def round_point(b):
    return (round(b[0]), round(b[1]))


def find_two_points(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    b1_x, b1_y = (0.5 * ((x1 + x2) + (y2 - y1)), 0.5 * ((y1 + y2) + (x1 - x2)))
    b2_x, b2_y = (0.5 * ((x1 + x2) - (y2 - y1)), 0.5 * ((y1 + y2) - (x1 - x2)))

    # flag_b1 = True
    # for obj in [b1_x, b1_y]:
    #     if obj % 1 != 0:
    #         flag_b1 = False
    # flag_b2 = True
    # for obj in [b2_x, b2_y]:
    #     if obj % 1 != 0:
    #         flag_b2 = False

    # b1_x = round(b1_x)
    # b1_y = round(b1_y)
    # b2_x = round(b2_x)
    # b2_y = round(b2_y)

    b1, b2 = (b1_x, b1_y), (b2_x, b2_y)

    return b1, b2  # , flag_b1, flag_b2


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
    b1, b2 = find_two_points(arr[0], arr[1])
    point_coords = [b1, b2]
    print(point_coords)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            a1, a2 = arr[i], arr[j]
            b1, b2 = find_two_points(arr[i], arr[j])

            flag_b1 = True
            for obj in [b1[0], b1[1]]:
                if obj % 1 != 0:
                    flag_b1 = False
            flag_b2 = True
            for obj in [b2[0], b2[1]]:
                if obj % 1 != 0:
                    flag_b2 = False

            b1_int = round_point(b1)
            b2_int = round_point(b2)

            if flag_b1 and flag_b2:
                if b1_int in s and b2_int in s:
                    return 0, []
                elif b1_int in s and b2_int not in s:
                    point_count = 1
                    point_coords = [b2_int]
                elif b2_int in s and b1_int not in s:
                    point_count = 1
                    point_coords = [b1_int]
            # elif flag_b1 and not flag_b2:
            #     if b1_int in s:
            #         point_count = 1
            #         point_coords = [b2]
            # elif flag_b2 and not flag_b1:
            #     if b2_int in s:
            #         point_count = 1
            #         point_coords = [b1]

        # if flag_b1 and b1_int in s and flag_b2 and b2_int in s:
        #         return 0, []
        #     elif flag_b1 and b1_int in s and b2_int not in s:
        #         point_count = 1
        #         point_coords = [b2]
        #     elif b2 in s and b1_int not in s:
        #         point_count = 1
        #         point_coords = [b1]

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
