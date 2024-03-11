f = open('input.txt', 'r')
arr = []
for line in f:
    arr = list(map(int, line.split()))

n = arr[0]
k = arr[1]
d = arr[2]

map = {}

is_index_checked = {}

for i in range(d):
    is_index_checked[i] = False

i = 0
while i < d:
    if i < 0:
        n = -1
        break
    new_figures = []
    if is_index_checked[i] == False:
        for m in range(10):
            new_num = n * 10 + m
            if new_num % k == 0:
                new_figures.append(m)
        map[i] = new_figures
    if len(map[i]) == 0:
        is_index_checked[i] = False
        n = n // 10
        i -= 1
        continue

    m = map[i].pop()
    n = n * 10 + m
    is_index_checked[i] = True

    i += 1

print(n)