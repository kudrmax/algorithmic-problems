def foo():
    from collections import defaultdict

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    n, k = list(map(int, lines[0].split()))
    arr = list(map(int, lines[1].split()))

    # print(n, k, arr)

    d = defaultdict(int)

    if n == 1:
        return 'NO'

    for i in range(len(arr)):
        a = arr[i]
        d[arr[i]] += 1
        if i - k - 1 >= 0:
            d[arr[i - k - 1]] -= 1
        # print(d)
    # print(d)

    print(d)

    for key, val in d.items():
        if val > 1:
            return 'YES'
    return 'NO'

print(foo())
