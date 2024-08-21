from typing import List

with open('input.txt') as f:
    lines = f.readlines()

# t = int(lines[0])
data = []
for i in range(1, len(lines[1:]), 2):
    _, k = map(int, lines[i].strip().split())
    a_arr = list(map(int, lines[i + 1].strip().split()))
    n = len(a_arr)
    data.append((n, k, a_arr))


def get_mean(arr: List[int]) -> float:
    return sum(arr) / len(arr)


def get_sigma(arr: List[int], a_fix: int, d: int = 2):
    return sum([abs(a - a_fix) ** d for a in arr]) / len(arr)


def get_delta(a_arr: List[int], b_arr: List[int], d: int = 2):
    return sum([abs(a - b) ** d for a, b in zip(a_arr, b_arr)])


def get_diff_with_mean(arr: List[int], mean: float = None) -> List[float]:
    if not mean:
        mean = get_mean(arr)
    return [abs(a - mean) for a in arr]


for n, k, a_arr in data:
    a_arr = sorted(a_arr)
    b_arr = [float('inf') for _ in range(len(a_arr))]
    mean = get_mean(a_arr)
    diff_arr = get_diff_with_mean(a_arr, mean=mean)

    print(f'{n = },\t {k = },\t {mean = }')
    print(f'{a_arr = }')
    print(f'{diff_arr = }')

    for _ in range(k - 1):
        max_diff = -float('inf')
        max_diff_index = -1
        for i, diff in enumerate(diff_arr):
            if diff > max_diff:
                max_diff = diff
                max_diff_index = i
        print(f'{max_diff = }, {max_diff_index = }')
        # for i, diff in enumerate(diff_arr):
        #     pass
        for i, a in enumerate(a_arr):
            if abs(a - max_diff) < abs(a - mean):
                # print(f'{i = }, {a = }, {abs(a - max_diff) = }, {abs(a - mean) = }')
                b_arr[i] = a_arr[max_diff_index]
        # print(b_arr)
        diff_arr[max_diff_index] = -float('inf')

    for i, b in enumerate(b_arr):
        if b == float('inf'):
            b_arr[i] = mean

    print(f'{b_arr = }')


def print_diff():
    print('PRINT DIFF')
    for n, k, a in data:
        a = sorted(a)

        b_list = [
            [2, 2, 2, 14, 14, 14],
            [6, 6, 6, 14, 14, 14],
        ]

        print(f'{n = },\t {k = },\t mean = {get_mean(a)}')
        print(f'{a = }')
        print(f'diff = {get_diff_with_mean(a, mean=5)}')
        print()
        for b in b_list:
            print(f'{b = },\tdelta = {get_delta(a, b)}')

# print_diff()