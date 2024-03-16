with open('input.txt', 'r') as file:
    lines = file.readlines()

t = int(lines[0].split()[0])

arr_list = []

for i in range(2, t * 2 + 1, 2):
    arr = list(map(int, lines[i].split(' ')))
    arr_list.append(arr)

for arr in arr_list[:1]:
    print(arr)

    segment_count = 0
    cursor = 0

    i = 0
    while i < len(arr):
        a = arr[i]
        for length in range(1, a + 1):
            index = i + length - 1
            if index >= len(arr):
                break
            if arr[index] >= length:
                pass
            else:
                break
        i += length
        segment_count += 1
    print(segment_count)
