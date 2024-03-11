def foo(arr):
    L = arr[0]
    x1, v1 = arr[1], arr[2]
    x2, v2 = arr[3], arr[4]

    x_zero, v_zero = 0, v2
    x_rel, v_rel = x1 - x2, v1 - v2
    # x_fake, v_fake = L - x1, -v1
    # x_fake_rel, v_fake_rel = x_fake, v_fake - v2

    # if v_fake_rel == 0:
    #     print('NO')
    #     return

    # delta = x_zero - x_fake_rel
    # t = delta / v_fake_rel

    delta = x_rel
    # if v_rel < 0:
    #     delta = delta - L
    t = delta / v_rel

    print('YES')
    print(t)
    return

f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))
print(arr)
foo(arr)