# with open('input.txt') as file:
#     lines = file.readlines()
#
# n = int(lines[0])
# arr = list(map(int, lines[1].split()))

n = int(input())
arr = list(map(int, input().split()))


# sum = 0
# for a in arr:
#     sum += a
#
# if sum % 2 == 0:
#     print('YES')
# else:
#     print('NO')

count_odd = 0
for a in arr:
    if a % 2 == 1:
        count_odd += 1

if count_odd % 2 == 0:
    print('YES')
else:
    print('NO')