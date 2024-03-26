with open('input.txt', 'r') as file:
    lines = file.readlines()

n, m = list(map(int, lines[0].split()))
arr = list(map(int, lines[1].split()))
pairs = []
for line in lines[2:]:
    pair = tuple(map(int, line.split()))
    pairs.append(pair)

print(arr)
print(pairs)

prefix_sums = [_ for _ in range(len(arr))]
prefix_sums[-1] = 0
for i in range(len(arr)):
    prefix_sums[i] = prefix_sums[i - 1] + arr[i]

print(prefix_sums)