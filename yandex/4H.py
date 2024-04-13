with open('input.txt', 'r') as file:
    lines = file.readlines()

n = list(map(int, lines[0].split()))[0]
arr = []
for i in range(n):
    pair = tuple(map(int, lines[i + 1].split()))
    arr.append(pair)
# print(arr)

arr_sorted = sorted(arr, key=lambda x: x[0], reverse=True)
print(arr_sorted)

best_choice = arr_sorted[0][0]
how_match_money = arr_sorted[0][1]

print(f'{best_choice = }, {how_match_money = }')

d = {}

for i in range(len(arr_sorted)):
    count, bribe = arr_sorted[i]
    d[count]