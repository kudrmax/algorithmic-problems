f = open('input.txt', 'r')

arr = []
for line in f:
    arr = list(map(int, line.split()))

# input()
# arr = list(map(int, input().split()))

plus = '+'
mul = 'x'

my_str = []

now_is_even = arr[0] % 2 == 0
for i in range(1, len(arr)):
    a = arr[i]
    a_is_even = a % 2 == 0
    if now_is_even and a_is_even:
        my_str.append(plus)
    elif now_is_even and not a_is_even:
        my_str.append(plus)
        now_is_even = False
    elif not now_is_even and not a_is_even:
        my_str.append(mul)
    elif not now_is_even and a_is_even:
        my_str.append(plus)

print(''.join(my_str))
