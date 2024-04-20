with open('input.txt', 'r') as file:
    lines = file.readlines()

t = int(lines[0].split()[0])

arr_list = []

for i in range(2, t * 2 + 1, 2):
    arr = list(map(int, lines[i].split(' ')))
    arr_list.append(arr)

for arr in arr_list:
    # print(arr)

    segment_count = 0
    lengths = []

    i = 0
    while i < len(arr):

        a = arr[i]

        length = 1
        max_length = a
        while length < max_length + 1:
            index = i + length - 1
            if index >= len(arr):
                break

            max_length = min(max_length, arr[index])

            if arr[index] < length:
                break
            length += 1
        i += length - 1
        lengths.append(length - 1)
        segment_count += 1

    print(segment_count)
    for l in lengths:
        print(l, end=' ')
    print()
    # print(lengths)
