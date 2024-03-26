with open('input.txt', 'r') as file:
    lines = file.readlines()

N = list(map(int, lines[0].split()))[0]


def get_length(k):
    l1 = (k * (1 + k) * (2 + k)) // 6
    l2 = k * (1 + k) // 2 - 1
    # print(l1, l2)
    return int(l1 + l2)

k = 0
best_k = 0
while True:
    length = get_length(k)
    if length <= N:
        best_k = k
        k += 1
        continue
    else:
        break
print(best_k)

# print(get_length(888888))