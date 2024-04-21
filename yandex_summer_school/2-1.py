with open('input.txt', 'r') as file:
    lines = file.readlines()

arr = []
for line in lines[1:]:
    arr.append(tuple(map(int, line.strip().split())))
n = len(arr)


def foo():
    hy = {}
    hx = {}
    hd_positive = {}
    hd_negative = {}

    step_counter = 0
    for x, y in arr:
        if y not in hy:
            hy[y] = {}
        hy[y][x] = 1
        max_counter = 0
        i = 1
        while x + i in hy[y]:
            max_counter += 1
            i += 1
        j = 1
        while x - j in hy[y]:
            max_counter += 1
            j += 1
        for k in range(x - j + 1, x + i):
            hy[y][k] = max_counter + 1
        if max_counter + 1 == 5:
            return step_counter

    # for x, y in arr:
    #     step_counter += 1
    #     for h, key_fixed, key_changing in zip([hy, hx], [y, x], [x, y]):
    #         h[key_fixed] = 1
    #         max_counter = 1
    #         i = 0
    #         while key_changing + i in h[key_fixed]:
    #             max_counter += 1
    #             i += 1
    #         j = 0
    #         while key_changing - j in h:
    #             max_counter = max(max_counter, h[key_changing - j])
    #             j += 1
    #         for k in range(key_changing - j + 1, key_changing + i):
    #             h[key_fixed][k] = max_counter
    #         if max_counter == 5:
    #             return step_counter
    # return step_counter


step_counter = foo()
if step_counter % 2 == 0:
    print('First')
else:
    print('Second')
