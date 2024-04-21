with open('input.txt', 'r') as file:
    lines = file.readlines()

n, k = tuple(map(int, lines[0].strip().split()))

prices = list(map(int, lines[1].strip().split()))

# res = [0 for _ in range(n)]
res = []

dp = [0 for _ in range(n + 1)]
dp[-1] = prices[-1]

for i in range(n - 1, 0, -1):
    min_price = float('inf')
    min_j = -1
    for j in range(i + 1, min(i + k, n) + 1):
        if prices[i - 1] * (j - i) + dp[j] <= min_price:
        # if dp[j] <= min_price:
            min_price = prices[i] * (j - i) + dp[j]
            min_j = j
    dp[i] = min_price
    res.append(min_j)
# res.append(1)

print(dp)
print(dp[1])
print(list(reversed(res)))
