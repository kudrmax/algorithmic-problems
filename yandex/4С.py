with open('input.txt', 'r') as file:
    lines = file.readlines()

n, m = list(map(int, lines[0].split()))
arr = list(map(int, lines[1].split()))
pairs = []
for line in lines[2:]:
    pair = tuple(map(int, line.split()))
    pairs.append(pair)

prefix_sums = [_ for _ in range(len(arr))]
prefix_sums[-1] = 0
for i in range(len(arr)):
    prefix_sums[i] = prefix_sums[i - 1] + arr[i]


def bs(arr, prefix_sums, l, s):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        delta = prefix_sums[mid] - prefix_sums[mid - l] if mid - l >= 0 else prefix_sums[mid]
        if delta == s:
            return mid
        elif delta < s:
            left = mid + 1
        else:
            right = mid
    if prefix_sums[left] == s:
        return left
    return -1

# print(arr)
# print(pairs)
# print(prefix_sums)

for l, s in pairs:
    t = bs(arr, prefix_sums, l, s)
    if t == -1:
        print(-1)
    # print(t, t - l + 1)
    else:
        print(t - l + 1 + 1)
