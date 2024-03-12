f = open('input.txt', 'r')
arr = []
for line in f:
    arr.append(list(map(int, line.split()))[0])

x = arr[0]  # мой мощь (хп и солдаты)
y = arr[1]  # хп казармы
delta_p = arr[2]  # кол-во производимых солдат

p = 0

y -= x
if y != 0:
    p = delta_p
c = 1

done = False
data_list = [[x, y, p, c, done]]

def produce_soldiers(data):
    x, y, p, c, done = data
    if not done:
        if p < 0:
            p = 0
        x -= p
        if y != 0:
            p += delta_p
        if x <= 0:
            done = True
    return [x, y, p, c, done]

def check_win(data):
    x, y, p, c, done = data
    if x <= 0:
        done = True
        c = -1
    elif y <= 0 and p <= 0:
        done = True
    elif c > 10000:
        c = -1
        done = True
    return [x, y, p, c, done]

def do_step(data):
    data = check_win(data)
    x, y, p, c, done = data


    if done:
        return [data]
    # if x <= 0:
    #     c = -1
    #     return [[x, y, p, c, True]]
    #
    # if y <= 0 and p <= 0:
    #     return [[x, y, p, c, True]]

    if y == 0:
        # мой ход
        if x >= p:
            c += 1
            return [[x, y, p, c, True]]
        else:  # x < p
            if x > p - x:
                c += 2
                return [[x, y, p, c, True]]
            else:  # x <= p - x
                c = -1
                return [[x, y, p, c, True]]
    else:  # y != 0
        if y > x:
            y -= (x - delta_p)
            p = 0
            arr = [x, y, p, c + 1, False]
            arr = check_win(arr)
            arr = produce_soldiers(arr)
            arr = check_win(arr)
            return [arr]
        else:  # y <= x
            # первый вариант

            # p -= x - y
            # y = 0

            arr1 = [x, 0, p - (x - y), c + 1, False]

            # второй вариант
            # if x >= p:
            #     y -= (x - p)
            #     p = 0
            # else:  # x < p
            #     p -= x
            if x >= p:
                arr2 = [x, y - (x - p), 0, c + 1, False]
            else:
                arr2 = [x, y, p - x, c + 1, False]

            arr1= check_win(arr1)
            arr2= check_win(arr2)
            arr1 = produce_soldiers(arr1)
            arr2 = produce_soldiers(arr2)
            arr1= check_win(arr1)
            arr2= check_win(arr2)

            return [arr1, arr2]

while True:
    new_data_list = []
    while len(data_list) > 0:
        data = data_list.pop()
        datas = do_step(data)
        for d in datas:
            new_data_list.append(d)
    data_list = [list(x) for x in set(tuple(x) for x in new_data_list)]
    # data_list = new_data_list

    count_done = 0
    for i in range(len(data_list)):
        if data_list[i][4] == True:
            count_done += 1
    if count_done == len(data_list):
        break

#
# while True:
#
#     if x <= 0:
#         c = -1
#         break
#
#     if y == 0:
#         # мой ход
#         if x >= p:
#             c += 1
#             break
#         else:  # x < p
#             if x > delta_p - x:
#                 c += 2
#                 break
#             else:  # x <= p - x
#                 c = -1
#                 break
#     else:  # y != 0
#         if y > x:
#             y -= (x - delta_p)
#             p = 0
#         else:  # y <= x
#             # тут должен быть перебор
#             # p -= x - y
#             # y = 0
#             if x >= p:
#                 y -= (x - p)
#                 p = 0
#             else:  # x < p
#                 p -= x
#
#     if p < 0:
#         p = 0
#
#     # его ход
#     x -= p
#     if y != 0:
#         p += delta_p
#
#     c += 1

c_min = 1000000
for i in range(len(data_list)):
    x, y, p, c, done = data_list[i]
    if c != -1:
        c_min = min(c_min, c)
print(data_list)
if c_min == 1000000:
    print(-1)
else:
    print(c_min)
