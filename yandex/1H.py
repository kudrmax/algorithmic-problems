def get_time_collision(x1, v1, x2, v2, L):
    v_rel = v1 - v2
    if v_rel < 0:
        delta = (x1 - x2) % L
    else:
        delta = (x2 - x1) % L
    t = delta / v_rel
    return abs(t)


def foo(arr):
    L = arr[0]
    x1, v1 = arr[1], arr[2]
    x2, v2 = arr[3], arr[4]

    x2_fake = L - x2
    v2_fake = -v2

    if x1 == (L - x2) % L or x1 == x2:
        print('YES')
        print(0)
        return

    if v1 == 0 and v2 == 0:
        print('NO')
        return

    if v1 != v2:
        # print(1)
        t1 = get_time_collision(x1, v1, x2, v2, L)
        if v2_fake != v1:
            t2 = get_time_collision(x1, v1, x2_fake, v2_fake, L)
            t = min(t1, t2)
        else:
            t = t1
        print('YES')
        print(t)
    if v1 == v2:
        # print(2)
        v = v1
        x_fake1 = ((x1 + x2) / 2) % L
        x_fake2 = (x_fake1 + L / 2) % L
        t1 = get_time_collision(x_fake1, v, 0, 0, L)
        t2 = get_time_collision(x_fake2, v, 0, 0, L)
        t = min(t1, t2)
        print('YES')
        print(t)


f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))
# print(arr)
foo(arr)
