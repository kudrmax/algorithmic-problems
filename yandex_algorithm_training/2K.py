with open('input.txt', 'r') as file:
    lines = file.readlines()

N, K = list(map(int, lines[0].split()))
arr = list(map(int, lines[1].split()))

# print(K)
# print(arr)

max_profit = 0

for i in range(N):
    possible_income = arr[i + 1 : min(N, i + K + 1)]

    possible_profit = []
    for j in range(len(possible_income)):
        possible_profit.append(possible_income[j] - arr[i])

    # print(f'{arr[i] = }')
    # print(f'{possible_income = }')
    # print(f'{possible_profit = }')

    if len(possible_profit) > 0:
        max_profit = max(max_profit, max(possible_profit))

print(max_profit)