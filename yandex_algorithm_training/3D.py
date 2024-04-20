def foo():
    from collections import defaultdict

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    n, k = list(map(int, lines[0].split()))
    arr = list(map(int, lines[1].split()))

    # print(n, k)

    d = defaultdict(int)

    for a in arr[:k + 1]:
        d[a] += 1
    for _, count in d.items():
        if count >= 2:
            return False

    for i in range(k + 1, len(arr)):
        d[arr[i]] += 1
        d[arr[i - k - 1]] -= 1
        # for index in range(i - k, i + 1):
        if d[arr[i - k]] >= 2:
            return False
        if d[arr[i]] >= 2:
            return False

    return True

res = 'NO' if foo() else 'YES'
print(res)
