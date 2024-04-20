f = open('input.txt', 'r')
arr = []
for line in f:
    arr = list(map(int, line.split()))

n = arr[0]
k = arr[1]
d = arr[2]

possible = True
if n % k != 0:
    possible = False
    for m in range(10):
        new_n = n * 10 + m
        if new_n % k == 0:
            n = new_n
            possible = True
            d -= 1
            break
if not possible:
    print(-1)
else:
    n = str(n)
    if d > 0:
        for i in range(d):
            n += '0'
            # n *= (10 ** d)
    print(n)
