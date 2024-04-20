import string

with open('input.txt', 'r') as file:
    lines = file.readlines()

s = lines[0].strip()
log = lines[1].strip()

typed_string = ['']

def print_typed_string(cursor):
    s = []
    for i in range(len(typed_string)):
        letter = typed_string[i]
        if i == cursor:
            letter = letter.upper()
        s.append(letter)
    s = ''.join(s)
    if s == '':
        return 'empty'
    return s


def cursor_is_correct(p):
    if p >= len(typed_string):
        return False
    if p <= 0:
        return False
    return True


def run_command(command, p):
    if command == 'delete':
        if cursor_is_correct(p + 1):
            typed_string.pop(p + 1)
    elif command == 'bspace':
        if cursor_is_correct(p):
            typed_string.pop(p)
        if cursor_is_correct(p - 1):
            p -= 1
    elif command == 'left':
        if cursor_is_correct(p - 1):
            p -= 1
    elif command == 'right':
        if cursor_is_correct(p + 1):
            p += 1
    return p


log_p = 0
cursor = 0
break_flag = False
while log_p < len(log):
    while log[log_p] != '<':
        typed_string.insert(cursor + 1, log[log_p])
        cursor += 1
        log_p += 1
        if log_p >= len(log):
            break_flag = True
            break
    if break_flag:
        break
    p_end_coomand = log.find('>', log_p)
    command = log[log_p + 1:p_end_coomand]
    cursor = run_command(command, cursor)
    print(print_typed_string(cursor))
    log_p = p_end_coomand + 1

print(print_typed_string(cursor))