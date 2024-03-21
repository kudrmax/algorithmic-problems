from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()

arr_list = []
for i in range(3):
    arr_list.append(list(map(int, lines[i * 2 + 1].split())))

# print(arr_list)

d_list = [set(), set(), set()]

s = set()

for i in range(3):
    for n in arr_list[i]:
        d_list[i].add(n)
for i in range(3):
    for n in arr_list[i]:
        count = 0
        for j in range(3):
            if n in d_list[j]:
                count += 1
        if count >= 2:
            s.add(n)
print(*sorted(s))