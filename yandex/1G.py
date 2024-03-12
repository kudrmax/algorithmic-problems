f = open('input.txt', 'r')
arr = []
for line in f:
    arr.append(list(map(int, line.split()))[0])

x = arr[0]  # мой мощь (хп и солдаты)
y = arr[1]  # хп казармы
delta_p = arr[2]  # кол-во производимых солдат

p = 0

y -= x
if y > 0:
    p = delta_p
c = 1

if y < 0:
    y = 0

done = False
data_list = [[x, y, p, c, done]]


def produce_soldiers(data):
    x, y, p, c, done = data
    if not done:
        if p < 0:
            p = 0
        x -= p
        if y > 0:
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
    # elif c > 10000:
    #     c = -1
    #     done = True
    return [x, y, p, c, done]


def do_step(data):
    data = check_win(data)
    x, y, p, c, done = data

    if done:
        return [data]

    if y == 0:
        if x >= p:
            c += 1
            return [[x, y, p, c, True]]
        else:  # x < p
            if x > p - x:
                while x > 0 and p > 0:
                    p -= x
                    if p <= 0:
                        c += 1
                        break
                    x -= p
                    if x <= 0:
                        c += 1
                        break
                    c += 1
                arr = check_win([x, y, p, c, done])
                return [arr]
            else:  # x <= p - x
                c = -1
                return [[x, y, p, c, True]]
    else:  # y != 0
        if y > x:
            if x <= p:
                return [[0, 1, 1, -1, True]]
            y -= (x - p)
            p = 0
            arr = [x, y, p, c + 1, False]
            # arr = check_win(arr)
            arr = produce_soldiers(arr)
            arr = check_win(arr)
            return [arr]
        else:  # y <= x
            # первый вариант
            arr1 = [x, 0, p - (x - y), c + 1, False]
            arr1 = check_win(arr1)

            # второй вариант

            if p == x:
                arr2 = [0, 1, 1, -1, True]
            elif p > x:
                arr2 = [0, 1, 1, -1, True]
            else:  # p < x
                arr2 = [x, y - (x - p), 0, c + 1, False]
            # if x >= p:
            #     arr2 = [x, y - (x - p), 0, c + 1, False]
            # else:
            #     arr2 = [x, y, p - x, c + 1, False]

            arr2 = check_win(arr2)
            arr1 = produce_soldiers(arr1)
            arr2 = produce_soldiers(arr2)
            arr1 = check_win(arr1)
            arr2 = check_win(arr2)

            return [arr1, arr2]


kk = 0
while True:
    new_data_list = []
    while len(data_list) > 0:
        data = data_list.pop()
        datas = do_step(data)
        for d in datas:
            if d[3] != -1:
                new_data_list.append(d)
    # data_list = [list(x) for x in set(tuple(x) for x in new_data_list)]
    new_data_list.append([0, 1, 1, -1, True])
    data_list = new_data_list

    count_done = 0
    for i in range(len(data_list)):
        if data_list[i][4] == True:
            count_done += 1
    if count_done == len(data_list):
        break
    kk += 1
    # if kk % 100 == 0:
    #     print(kk)


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
