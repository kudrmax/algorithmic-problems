import collections

with open('input.txt', 'r') as file:
    lines = file.readlines()
arr = list(map(int, lines[1].split()))
# print(arr)

# print(sorted(arr))
# print(set(arr))

m =  collections.defaultdict(int)
for n in arr:
    m[n] += 1
# print(m)

max_count = 0
max_n = -1, -1
for n, count in m.items():
    n1 = n
    n2 = n + 1 if n + 1 in m else n
    count1 = count
    count2 = m[n2] if n + 1 in m else 0
    count = count1 + count2
    # print(f'{n1, n2}: {count = }')
    if count > max_count:
        max_n = n1, n2
        max_count = count
# print(max_n, max_count)
print(len(arr) - max_count)


# for num in set(arr):
#     print(num)