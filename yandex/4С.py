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
    delta = prefix_sums[left] - prefix_sums[left - l] if left - l >= 0 else prefix_sums[left]
    if delta == s:
        return left
    return -1

# print(arr)
# print(pairs)
# print(prefix_sums)

# with open('output.txt', 'r') as file:
#     lines = file.readlines()
# true_arr = []
# for line in lines:
#     true_arr.append(list(map(int, line.split()))[0])
# print(true_arr)

# for (l, s), true_ans in zip(pairs, true_arr):
#     t = bs(arr, prefix_sums, l, s)
#     if t != -1:
#         ans = t - l + 1 + 1
#     else:
#         ans = -1
#     if ans != true_ans:
#         print(ans, true_ans, (l, s))

for l, s in pairs:
    t = bs(arr, prefix_sums, l, s)
    if t != -1:
        ans = t - l + 1 + 1
    else:
        ans = -1
    # print(ans, (l, s))
    print(ans)

