with open('input.txt', 'r') as file:
    lines = file.readlines()

w, count_l, count_r = list(map(int, lines[0].split()))
arr_l = list(map(int, lines[1].split()))
arr_r = list(map(int, lines[2].split()))

print(w, arr_l, arr_r)

def calc_h(m):
    x, y = 0, 0
    for word in arr_l:
        if y != 0:
            x += 1
        if x + word > m:
            x = 0
            x = 0
            y += 1
        x += word
    return x, y


# p1, p2 = 0, w
# while p1 + 1 < p2:
#     m = (p1 + p2) // 2
#     h1 = calc_h(m)
#     h2 = calc_h(w - m)

print(calc_h(10))