def foo():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    N = int(lines[0].split()[0])
    arr = []
    for line in lines[1:]:
        arr.append(tuple(map(int, line.split())))

    print(N, arr)

    if N == 1:
        return 1

    arr = [(0, 0), (2, 2)]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x1, y1 = arr[i]
            x2, y2 = arr[j]

            a1 = (x1, y1)
            a2 = (x2, y2)

            b1 = (round(0.5 * ((x1 + x2) + (y2 - y1))), round(0.5 * ((y1 + y2) + (x1 - x2))))
            b2 = (round(0.5 * ((x1 + x2) - (y2 - y1))), round(0.5 * ((y1 + y2) - (x1 - x2))))

            print(a1, a2, b1, b2)

foo()