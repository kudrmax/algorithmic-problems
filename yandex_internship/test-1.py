file = open('input.txt', 'r')
lines = file.readlines()

for line in lines[1:]:
    data = line.strip().split(',')
    f, i, o, d, m, y = data
    s1 = len(set(f + i + o))
    d = sum(list(map(int, list(str(d)))))
    m = sum(list(map(int, list(str(m)))))
    s2 = 64 * (d + m)
    s3 = 256 * (ord(f[0].lower()) - ord('a') + 1)
    s = s1 + s2 + s3
    s = hex(s)
    s = str(s)
    s = s[-3:]
    while len(s) < 3:
        s = '0' + s
    s = s.upper()
    print(s, end=' ')




