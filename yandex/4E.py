import math

with open('input.txt', 'r') as file:
    lines = file.readlines()
n = list(map(int, lines[0].split()))[0]
print(f'{n = }')


def get_N(n):
    N = -(3 / 2) + 1 / 2 * math.sqrt(1 + 8 * n)
    if N % 1 != 0:
        N = int(N // 1 + 1)
    else:
        N = int(N)
    return N


def get_sum(N):
    return N * (N + 1) // 2

def bs(s1, s2, target):
    left, right = s1, s2
    while left < right:
        mid = (left + right) // 2
        # if mid == target:
        #     return mid
        if mid < target:
            left = mid + 1
        else:
            right = mid
    return left


N = get_N(n)
s1 = get_sum(N) + 1
s2 = get_sum(N + 1)
print(f'{N = }')
print(f'{s1 = }, {s2 = }')

# index = bs(s1, s2, n)
# print(f'{index = }')

# index = n - s1 + 1
# print(f'{index = }')

print(f'{s2 - n + 1}/{n - s1 + 1}')