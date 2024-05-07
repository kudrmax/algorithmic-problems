def foo(a, target):
    a = sorted(a)

    p1 = 0
    p2 = len(a) - 1

    best_delta = float('inf')
    best_p1 = 0
    best_p2 = 1

    while p1 + 1 < p2:
        s = a[p1] + a[p2]
        delta = target - s
        if delta < best_delta:
            best_p1, best_p2, best_delta = p1, p2, delta
        if s == target:
            return a[p1], a[p2]
        if s > target:
            p2 -= 1
        else:
            p1 += 1
    return a[p1], a[p2]

arr = [1, 2, 2]
target = 4
p1, p2 = foo(arr, target)
print(p1, p2)
