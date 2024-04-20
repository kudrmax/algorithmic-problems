from functools import cache
import math

with open('input.txt', 'r') as file:
    lines = file.readlines()

N = list(map(int, lines[0].split()))[0]


@cache
def foo_rustam(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    min_res = n - 1
    for i in range(2, n // 2 + 1):
        res = 1 + foo(n - i)
        min_res = min(res, min_res)
    return min_res

def foo(n):
    if n == 1 or n == 0:
        return 0
    l = math.log2(n)
    if l % 1 == 0:
        return int(l)
    return int(l) + 1

# N = 8
# print(foo_rustam(8))
# print(foo(N))


for n in range(1, 10000):
    if foo(n) != foo_rustam(n):
        print(f'Wrong: {foo(n) = }, {foo_rustam(n) = }, {n = }')