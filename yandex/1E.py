f = open('input.txt', 'r')
arr = []
for line in f:
    arr = list(map(int, line.split()))

n = arr[0]
k = arr[1]
d = arr[2]

flag = False

for i in range(d):
    if n % k == 0:
        n = 10 * n
        flag = True
    else:
        for m in range(10):
            new_n = n * 10 + m
            if new_n % k == 0:
                n = new_n
                flag = True
                break
if flag:
    print(n)
else:
    print(-1)

# i = 0
# while i < d:
#     if i < 0:
#         n = -1
#         break
#     new_figures = []
#     if is_index_checked[i] == False:
#         for m in range(10):
#             new_num = n * 10 + m
#             if new_num % k == 0:
#                 new_figures.append(m)
#         map[i] = new_figures
#     if len(map[i]) == 0:
#         is_index_checked[i] = False
#         n = n // 10
#         i -= 1
#         continue
#
#     m = map[i].pop()
#     n = n * 10 + m
#     is_index_checked[i] = True
#
#     i += 1
#
# print(n)