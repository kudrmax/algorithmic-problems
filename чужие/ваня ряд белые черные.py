from typing import List


def foo1(n: int, k: int, arr: List[str]):
    """
    O(n*k) version
    """
    min_count_of_white = float('inf')  # это такой способ поставить число равное бесконечности
    p1 = 0
    p2 = k - 1
    while p2 < len(arr):
        count_of_white = arr[p1:p2 + 1].count('W')
        min_count_of_white = min(min_count_of_white, count_of_white)
        p1 += 1
        p2 += 1
    return min_count_of_white


def foo2(n: int, k: int, arr: List[str]):
    """
    O(n) version
    """
    count_of_white = 0
    for i in range(k):
        if arr[i] == 'W':
            count_of_white += 1

    min_count_of_white = count_of_white

    p1 = 0
    p2 = k - 1
    while p2 < len(arr) - 1:
        if arr[p1] == 'W':
            count_of_white -= 1
        if arr[p2 + 1] == 'W':
            count_of_white += 1
        p1 += 1
        p2 += 1
        min_count_of_white = min(min_count_of_white, count_of_white)

    return min_count_of_white


with open('input.txt', 'r') as f:
    lines = f.readlines()

for i in range(1, len(lines[1:]), 2):
    n, k = map(int, lines[i].split())
    arr = list(lines[i + 1].strip())
    res1 = foo1(n=n, k=k, arr=arr)
    res2 = foo2(n=n, k=k, arr=arr)
    print(f'{"".join(arr)}\t{k=}\t{res1=}, {res2=}')
