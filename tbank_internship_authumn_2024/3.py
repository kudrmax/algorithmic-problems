from typing import Set, Dict


def find_password(s: str, good_letters: Set[str], k: int):
    letter_count: Dict[str, int] = {}
    for l in range(len(s)):
        letter_count[s[l]] += 1  # сдвигаем левый указатель
        if (l + k) < len(s):
            letter_count[s[l + k]] -= 1  # сдвигаем правый указатель


def foo(s: str, good_letters: Set[str], k: int):
    s_list = []
    p1 = 0
    for p2 in range(len(s) + 1):
        if p2 == len(s) or s[p2] not in good_letters:
            s_list.append(s[p1:p2])
            p1 = p2 + 1
    # find_password()
    # print(s_list)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    s = lines[0].strip()
    good_letters = set(lines[1].strip())
    k = int(lines[2])

    # foo(s, good_letters, k)
    find_password('aaa', good_letters, k)
