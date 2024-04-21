def foo():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    n, t = tuple(map(int, lines[0].split()))
    arr = list(map(int, lines[1].split()))
    index = list(map(int, lines[2].split()))[0]

    h0 = arr[index - 1]
    h2 = max(h0 + t, 0)
    h1 = max(h0 - t, 0)

    h_max = max(arr)
    h_min = min(arr)

    delta1 = h_max - h2
    delta2 = h1 - h_min

    delta1 = max(delta1, 0)
    delta2 = max(delta2, 0)

    print(h0, h1, h2, t)
    print(delta1, delta2)
    print(h_max, h_min)

    return 2 * min(delta1, delta2) + h_max - h_min

    return (2 * t - 2) + 2 * min(delta1, delta2) + max(delta1, delta2)

print(foo())