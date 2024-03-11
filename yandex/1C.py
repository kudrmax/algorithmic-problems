f = open('input.txt', 'r')

arr = []
for num in f:
    arr.append(int(num))

n = arr[0]
arr = arr[1:]
# print(arr)

count = 0
for a in arr:
    backspace_count = 0
    tab_count = a // 4
    space_count = a % 4
    if space_count >= 3:
        tab_count += 1
        backspace_count += 1
        space_count = 0
    count += tab_count + backspace_count + space_count
    # print(tab_count, space_count)
print(count)

