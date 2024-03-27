with open('input.txt', 'r') as file:
    lines = file.readlines()
w, _, _ = list(map(int, lines[0].split()))
arr_l = list(map(int, lines[1].split()))
arr_r = list(map(int, lines[2].split()))

# print(w, arr_l, arr_r)

def calc_h(w, arr):
    x, y = 0, 0
    for word in arr:
        if x != 0:
            x += 1
        if x + word > w:
            x = 0
            y += 1
        if word > w:
            return -1
        x += word
    return y + 1


def calc_h_max(w_i):
    h1 = calc_h(w_i, arr_l)
    h2 = calc_h(w - w_i, arr_r)
    h = max(h1, h2)
    return h


def bs_l(l, r):
    while l < r:
        m = (l + r) // 2
        h1 = calc_h(m, arr_l)
        h2 = calc_h(w - m, arr_r)
        if h1 == -1 and h2 == -1:
            pass
        if h1 == h2:
            return m
        elif h2 == -1:
            r = m
        elif h1 < h2:
            r = m
        elif h1 == -1:
            l = m + 1
        else: # h1 > h2
            l = m + 1
    return l

def bs_r(l, r):
    while l < r:
        m = (l + r + 1) // 2
        h1 = calc_h(m, arr_l)
        h2 = calc_h(w - m, arr_r)
        if h1 == -1 and h2 == -1:
            pass
        if h1 == h2:
            return m
        elif h2 == -1:
            r = m - 1
        elif h1 < h2:
            r = m - 1
        elif h1 == -1:
            l = m
        else: # h1 > h2
            l = m
    return l

def print_all_w():
    for w_i in range(w):
        h1 = calc_h(w_i, arr_l)
        h2 = calc_h(w - w_i, arr_r)
        print(f'{w_i}: {(h1, h2)}', end='\t')
    print()
    for w_i in range(w):
        h1 = calc_h(w_i, arr_l)
        h2 = calc_h(w - w_i, arr_r)
        print(f'{w_i}: {max(h1, h2)}', end='\t')
    print()


w1 = bs_l(1, w)
w2 = bs_r(1, w)
h1 = calc_h_max(w1)
h2 = calc_h_max(w2)

# print_all_w()
# print(f'w={w1}, h={h1}')
# print(f'w={w2}, h={h2}')

print(min(h1, h2))

# print(f'{max(arr_l) = }')
# print(f'{max(arr_r) = }')