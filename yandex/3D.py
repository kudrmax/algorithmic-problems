def foo():
    from collections import defaultdict

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    n, k = list(map(int, lines[0].split()))
    arr = list(map(int, lines[1].split()))

    # print(n, k, arr)

    # if n == 1:
    #     return 'NO'

    d = defaultdict(int)

    for i in range(min(n, k)):
        d[arr[i]] += 1

    p1 = 0
    p2 = min(n, k)

    while True:
        for i in range(p1, p2 + 1):
            if d[arr[i]] > 1:
                return 'YES'
        d[arr[p1]] -= 1
        p1 += 1
        p2 += 1
        if p2 >= len(arr):
            break
        d[arr[p2]] += 1
    return 'NO'

print(foo())
