def round_point(b):
    return (round(b[0]), round(b[1]))


def find_two_points(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    b1_x, b1_y = 0.5 * ((x1 + x2) + (y2 - y1)), 0.5 * ((y1 + y2) + (x1 - x2))
    b2_x, b2_y = 0.5 * ((x1 + x2) - (y2 - y1)), 0.5 * ((y1 + y2) - (x1 - x2))

    flag = True
    for obj in [b1_x, b1_y, b2_x, b2_y]:
        if obj % 1 != 0:
            flag = False

    b1_x = round(b1_x)
    b1_y = round(b1_y)
    b2_x = round(b2_x)
    b2_y = round(b2_y)

    b1, b2 = (b1_x, b1_y), (b2_x, b2_y)
    return b1, b2, flag


def foo(N, arr):
    s = set(arr)

    p = arr[0]
    point_coords = [
        [p[0] + 1, p[1]],
        [p[0], p[1] + 1],
        [p[0] + 1, p[1] + 1]
    ]
    point_count = 3

    if N == 1:
        return point_count, point_coords

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            b1, b2, flag = find_two_points(arr[i], arr[j])

            if flag:
                if b1 in s and b2 in s:
                    return 0, []
                elif b1 in s and b2 not in s:
                    point_count = 1
                    point_coords = [b2]
                elif b2 in s and b1 not in s:
                    point_count = 1
                    point_coords = [b1]
                elif b1 not in s and b2 not in s:
                    if point_count > 2:
                        point_count = 2
                        point_coords = [b1, b2]

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
