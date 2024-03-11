def foo(arr):
    L = arr[0]
    x1, v1 = arr[1], arr[2]
    x2, v2 = arr[3], arr[4]

    x, v = (x1 - x2) % L, v1 - v2
    c = (-x2) % L

    t = 0

    if v != 0:
        p1 = 0
        p2 = (2 * c) % L
        delta1 = (x - p1) % L
        delta2 = (x - p2) % L
        # if v < 0:
        #     delta1 = L - delta1
        #     delta2 = L - delta2
        t1 = abs(delta1 / v)
        t2 = abs(delta2 / v)
        t = min(t1, t2)
        print('YES')
        print(abs(t))
        return


f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))
# print(arr)
foo(arr)
