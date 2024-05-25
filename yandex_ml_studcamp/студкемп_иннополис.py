file = open('input.txt', 'r')
lines = file.readlines()

arr = list(map(int, lines[1].strip().split()))

d = {}
for a in arr:
    if a not in d:
        d[a] = 0
    d[a] += 1

k = 0
for a, count in d.items():
    if count > a:
        k += count - a

print(k)
