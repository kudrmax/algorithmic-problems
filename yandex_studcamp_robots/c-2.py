from typing import List


def get_delta_between_arrs(a_arr: List[int], b_arr: List[int]):
    return sum([abs(a - b) ** 2 for a, b in zip(a_arr, b_arr)])


def get_mean(arr: List[int]) -> float:
    return round(sum(arr) / len(arr))


if __name__ == '__main__':
    a = [1, 2, 10, 21, 22]
    mean = get_mean(a)
    print(f'{a = }')
    print(f'{mean = }')

    bs = [
        [11, 11, 11, 11, 11],
        [11, 11, 11, 21, 21],
        [11, 11, 11, 21, 21],
        [11, 11, 11, 20, 20],
    ]

    for b in bs:
        delta = get_delta_between_arrs(a, b)
        print(f'{delta = } with {b = }')