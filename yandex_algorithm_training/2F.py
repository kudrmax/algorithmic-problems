with open('input.txt', 'r') as file:
    lines = file.readlines()

n = list(map(int, lines[0].split()))[0]
arr = list(map(int, lines[1].split()))
a, b, k = list(map(int, lines[2].split()))

# print(n ,arr, a, b, k)

def get_sector_number(i0, v0):
    count_sectors = v0 // k
    if v0 % k == 0:
        count_sectors -= 1
    i0  = i0 + count_sectors
    return i0


i_min = get_sector_number(0, a)
i_max = get_sector_number(0, b)
# print(i_min, i_max)
max_val = 0
count = 0
for i in range(i_min, i_max + 1):
    i = i % n
    if arr[i] > max_val:
        max_val = arr[i]
    if count > n:
        break
    count += 1

arr.reverse()
i_min_rev = get_sector_number(len(arr) - 1, a)
i_max_rev = get_sector_number(len(arr) - 1, b)
# print(i_min_rev, i_max_rev)
max_val_rev = 0
count = 0
for i in range(i_min_rev, i_max_rev + 1):
    i = i % n
    if arr[i] > max_val_rev:
        max_val_rev = arr[i]
    if count > n:
        break
    count += 1

# print(max_val)
# print(max_val_rev)

print(max(max_val, max_val_rev))
