import string

with open('input.txt', 'r') as file:
    lines = file.readlines()

s = lines[0].strip()

lower_case_letters = set(list('abcdefghijklmnopqrstuvwxyz'))
upper_case_letters = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
numbers = set(list(map(int, '0123456789')))


has_lower = False
has_upper = False
has_number = False
for letter in s:
    if letter in lower_case_letters:
        has_lower = True
    elif letter in upper_case_letters:
        has_upper = True
    else:
        letter = int(letter)
        if letter in numbers:
            has_number = True

if has_upper and has_lower and has_number and len(s) >= 8:
    print('YES')
else:
    print('NO')