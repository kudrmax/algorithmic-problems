file = open('input.txt', 'r')
lines = file.readlines()

arr = []

for line in lines[1:]:
    data = line.strip().split()
    d, h, m, i, s = data
    d = int(d)
    h = int(h)
    m = int(m)
    i = int(i)

    timestamp = d * 24 * 60 + h * 60 + m

    arr.append((timestamp, i, s))

arr = sorted(arr)

from collections import defaultdict

times = defaultdict(int)
d = {}


def process(i, t, s):
    if i not in d:
        d[i] = t
        return
    t_prev = d[i]
    if s == 'B':
        return
    if s == 'A':
        d[i] = t
    if s == 'C' or s == 'S':
        times[i] += t - t_prev


for t, i, s in arr:
    process(i, t, s)
# print(arr)
times = sorted(list(times.items()))

for _, t in times:
    print(t, end=' ')
