from typing import List

with open('input.txt') as f:
    lines = f.readlines()


def get_mean(arr: List[int]) -> float:
    return round(sum(arr) / len(arr))


def get_delta_between_arrs(a_arr: List[int], b_arr: List[int], d: int = 2):
    return sum([abs(a - b) ** d for a, b in zip(a_arr, b_arr)])


def get_diff_with_mean_arr(arr: List[int], mean: float = None) -> List[float]:
    if not mean:
        mean = get_mean(arr)
    return [abs(a - mean) for a in arr]


def get_arr_with_sorted_indiices(arr: List[int]) -> List[int]:
    arr_indices = [-1 for _ in range(len(arr))]
    arr_with_tuple = [(-1, -1) for _ in range(len(arr))]
    for i, a, in enumerate(arr):
        arr_with_tuple[i] = (a, i)
    arr_with_tuple_sorted = sorted(arr_with_tuple, key=lambda x: x[0])
    for i, (a_sort, i_sort) in enumerate(arr_with_tuple_sorted):
        arr_indices[i] = i_sort
    return arr_indices


def get_b(n, k, a_arr):
    a_indices = get_arr_with_sorted_indiices(a_arr)
    a_arr = sorted(a_arr)
    b_arr = [float('inf') for _ in range(len(a_arr))]
    mean = get_mean(a_arr)
    diff_arr = get_diff_with_mean_arr(a_arr, mean=mean)

    # print(f'{diff_arr = }')
    # print(f'{mean = }')

    for _ in range(k - 1):
        max_diff = -float('inf')
        max_diff_index = -1
        for i, diff in enumerate(diff_arr):
            if diff > max_diff:
                max_diff = diff
                max_diff_index = i
        for i, a in enumerate(a_arr):
            if abs(a - max_diff) < abs(a - mean):
                b_arr[i] = a_arr[max_diff_index]
        diff_arr[max_diff_index] = -float('inf')

    for i, b in enumerate(b_arr):
        if b == float('inf'):
            b_arr[i] = mean
    b_not_sorted = [-1 for _ in range(len(b_arr))]
    for i, right_index in enumerate(a_indices):
        b_not_sorted[right_index] = b_arr[i]

    # print(f'{b_arr = }')
    # print(f'{b_not_sorted = }')
    # print(f'delta_between_arrs = {get_delta_between_arrs(a_arr, b_arr)}')

    return b_not_sorted


def check(a_arr, b_arrs):
    print(f'{a_arr = }')
    for b_arr in b_arrs:
        print(f'{b_arr = }')
        print(f'delta = {get_delta_between_arrs(a_arr, b_arr)}')


if __name__ == '__main__':
    # считывание
    data = []
    for i in range(1, len(lines[1:]), 2):
        _, k = map(int, lines[i].strip().split())
        a_arr = list(map(int, lines[i + 1].strip().split()))
        n = len(a_arr)
        data.append((n, k, a_arr))

    for n, k, a_arr in data:
        print(f'{n = },\t {k = }')
        print(f'{a_arr = }')
        b_arr = get_b(n, k, a_arr)
        print(f'{b_arr = }')
        print(f'delta = {get_delta_between_arrs(a_arr, b_arr)}')
        print()

    a_true = list(map(int, '1 2 3 4 5 2 3 4 5 6'.split()))
    b_true = list(map(int, '2 2 3 5 5 2 3 5 5 5'.split()))
    delta_true = get_delta_between_arrs(b_true, a_true)
    print(f'{delta_true = }')

    a_true = list(map(int, '1 2 2 3 3 4 4 5 5 6'.split()))
    b_true = list(map(int, '2 2 2 3 3 5 5 5 5 5'.split()))
    delta_true = get_delta_between_arrs(b_true, a_true)
    print(f'{delta_true = }')

    a_true = list(map(int, '1 2 2 3 3 4 4 5 5 6'.split()))
    b_true = list(map(int, '2 2 2 4 4 4 4 5 5 5'.split()))
    delta_true = get_delta_between_arrs(b_true, a_true)
    print(f'{delta_true = }')

