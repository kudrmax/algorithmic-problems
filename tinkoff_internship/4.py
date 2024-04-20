n, type = tuple(input().strip().split())
n, rotation_type = int(n), str(type)
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
# for i in range(len(arr)):
#     print(*arr[i], sep=' ')
n = len(arr)

res = []


def get_points(i, j):
    points = []
    points.append((i, j))
    points.append((0 + j, n - 1 - i))
    points.append((n - 1 - i, n - 1 - j))
    points.append((n - 1 - j, 0 + i))
    return points


if rotation_type == 'R':
    action_sequence = [
        (0, 1),
        (2, 3),
        (0, 2)
    ]
else:
    action_sequence = [
        (0, 3),
        (1, 2),
        (0, 2)
    ]


def print_rotation(points):
    for action in action_sequence:
        p1, p2 = points[action[0]], points[action[1]]
        res.append([*p1, *p2])
        # print(*p1, *p2)
        # arr[p1[0]][p1[1]], arr[p2[0]][p2[1]] = arr[p2[0]][p2[1]], arr[p1[0]][p1[1]] # реально меняем точки


counter = 0
n_max_i = n // 2 if n % 2 == 0 else (n // 2) + 1
for i in range(n_max_i):
    n_max_j = n - i - 1
    for j in range(i, n_max_j):
        points = get_points(i, j)
        print_rotation(points)
        counter += 3

print(counter)
for r in res:
    print(*r, sep=' ')

# print()
# for i in range(len(arr)):
#     print(*arr[i], sep=' ')
