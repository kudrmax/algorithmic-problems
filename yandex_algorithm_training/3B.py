def foo():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    s1 = lines[0].split('\n')[0]
    s2 = lines[1].split('\n')[0]

    # print(s1, s2)

    d1 = {}
    d2 = {}

    if len(s1) != len(s2):
        return 'NO'
    for ch1, ch2 in zip(s1, s2):
        if ch1 not in d1:
            d1[ch1] = 0
        if ch2 not in d2:
            d2[ch2] = 0
        d1[ch1] += 1
        d2[ch2] += 1

    for ch in s1:
        if ch not in d2:
            return 'NO'
        if d1[ch] != d2[ch]:
            return 'NO'
    return 'YES'

print(foo())