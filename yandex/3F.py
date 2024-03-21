with open('input.txt', 'r') as file:
    lines = file.readlines()

s = set(map(str, lines[0].split()))
arr = list(map(str, lines[1].split()))

# print(s)
# print(arr)

for word in arr:
    is_short = False
    for i in range(0, len(word)):
        short_word = word[:i + 1]
        # print(short_word)
        if short_word in s:
            print(short_word, end=' ')
            is_short = True
            break
    if not is_short:
        print(word, end=' ')