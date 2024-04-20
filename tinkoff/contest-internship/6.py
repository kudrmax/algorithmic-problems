# with open('input.txt', 'r') as file:
#     lines = file.readlines()
# n = int(tuple(lines[0].strip().split())[0])
# arr = []
# for line in lines[1:]:
#     arr.append(list(line.strip()))
# n = len(arr)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(input().strip()))
n = len(arr)

K_set = set()
G_set = set()


def check_coords(i, j):
    for coord in [i, j]:
        if coord < 0 or coord >= n:
            return False
    return True


def do_steps(i, j, type):
    res = []
    if type == 'K':
        dir = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    else:  # if == 'K':
        dir = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]
    for d in dir:
        new_i, new_j = i + d[0], j + d[1]
        if (check_coords(new_i, new_j)):
            new_type = type
            if arr[new_i][new_j] == 'G':
                new_type = 'G'
            elif arr[new_i][new_j] == 'K':
                new_type = 'K'
            if new_type == 'K' and (new_i, new_j) not in K_set:
                res.append((new_i, new_j, new_type))
                K_set.add((new_i, new_j))
            if new_type == 'G' and (new_i, new_j) not in G_set:
                res.append((new_i, new_j, new_type))
                G_set.add((new_i, new_j))

    return res


start_coord = None
end_coord = None
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            start_coord = i, j, 'K'
        if arr[i][j] == 'F':
            end_coord = i, j, 'K'

from queue import Queue

q = Queue()
q.put(start_coord)
K_set.add((start_coord[0], start_coord[1]))
step_count = 0
flag = True
while not q.empty():
    new_q = Queue()
    flag = True

    while not q.empty():
        i, j, type = q.get()
        if i == end_coord[0] and j == end_coord[1]:
            flag = False
            break
        new_points = do_steps(i, j, type)
        for new_point in new_points:
            new_q.put(new_point)

    if flag is False:
        break
    step_count += 1

    q = new_q

print(step_count if not flag else -1)
