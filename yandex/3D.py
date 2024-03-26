def foo():
    from collections import defaultdict

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    n, k = list(map(int, lines[0].split()))
    arr = list(map(int, lines[1].split()))

    d = defaultdict(int)

    for a in arr[:k]:
        d[a] += 1
    for _, count in d.items():
        if count >= 2:
            return False
    
    for a in arr[k:]:
        d[a] += 1
        d[a - k] -= 1
        for _, count in d.items():
            if count >= 2:
                return False

    return True

res = 'NO' if foo() else 'YES'
print(res)
