def foo(arr):
    L = arr[0]
    x1, v1 = arr[1], arr[2]
    x2, v2 = arr[3], arr[4]

    if v1 == 0 and v2 == 0:
        if x1 == L - x2:
            print('YES')
            print(0)
            return
        else:
            print('NO')
            return


    x_zero, v_zero = 0, v2
    # temp = x1 - x2
    # temp1 = temp - (x1 - x2) % L
    x_rel, v_rel = (x1 - x2) % L, v1 - v2
    diff = -x2
    center_coord = (0 + diff) % L
    delta = x_rel

    t = 0
    if v_rel == 0:
        x_fake = delta / 2
        v_fake = v_zero
        # t1 = abs((x_fake + diff) / v_fake
        if v_fake > 0:
            t1 = abs((center_coord - x_fake) / v_fake)
        else:
            t1 = abs((L - abs((center_coord - x_fake))) / v_fake)
        t2 = abs(x_fake / v_fake)
        t = min(t1, t2)
    else:
        t = abs(delta / v_rel)

    print('YES')
    print(t)
    return

f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))
# print(arr)
foo(arr)