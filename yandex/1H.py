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

    if v1 != 0 or v2 != 0:
        t1 = get_time_collision(x1, v1, x2, v2, L)
        t2 = get_time_collision(x1, v1, x2_fake, v2_fake, L)
        t = min(t1, t2)
        print('YES')
        print(t, t1, t2)

f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))
# print(arr)
foo(arr)
