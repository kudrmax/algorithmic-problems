with open('input.txt', 'r') as file:
    lines = file.readlines()

n, k = tuple(map(int, lines[0].strip().split()))

prices = list(map(int, lines[1].strip().split()))

res = []

flag = False
dp = [0 for _ in range(n)]
dp[-1] = prices[-1]
dp.append(0)
for i in range(n - 2, -1, -1):
    min_price = float('inf')
    min_j = -1
    for j in range(i + 1, min(i + k + 1, n + 1)):
        var = prices[i] * (j - i) + dp[j]
        if var <= min_price:
            min_price = var
            min_j = j
    dp[i] = min_price
    res.append(min_j)
res.append(0)

flag = False
if res[0] != n:
    flag = True
res.reverse()
if flag:
    res.append(n)

print(dp[0])
# print(dp)
# print(res)
for a, b in zip(res[:-1], res[1:]):
    print(b - a, end=' ')
    print('0' * (b - a - 1), end='')
    if b - a - 1 != 0:
        print(' ', end='')
