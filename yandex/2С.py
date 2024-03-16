with open('input.txt', 'r') as file:
    lines = file.readlines()

N = list(map(int, lines[0].split()))
arr = list(map(int, lines[1].split()))

arr_sum = sum(arr)
max_el = max(arr)

if 2 * max_el - arr_sum <= 0:
    print(arr_sum)
else:
    print(min(2 * max_el - arr_sum, arr_sum))


