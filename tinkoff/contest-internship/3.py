arr = []
n = int(input().strip())
for _ in range(n):
    arr.append(input().strip())
arr.sort()

# before_path = ''
# for path in arr:
#     splitted_path = path.split('/')
#     dir_name = splitted_path[-1]
#     dir_count = len(splitted_path) - 1
#     print('  ' * dir_count + dir_name)

for path in arr:
    last_slash_ptr = path.rfind('/') + 1
    dir_name = path[last_slash_ptr:]
    dir_count = path[:last_slash_ptr].count('/')
    print('  ' * dir_count + dir_name)