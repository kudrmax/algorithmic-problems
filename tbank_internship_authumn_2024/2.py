from typing import List, Optional

with open('input.txt', 'r') as f:
    lines = f.readlines()

arr = list(map(int, lines[1].strip().split()))


def foo() -> Optional[List[int]]:
    if arr[0] == -1:
        arr[0] = 1

    for i in range(len(arr)):
        if arr[i] == -1:
            arr[i] = arr[i - 1] + 1
            continue
        if arr[i] > arr[i - 1]:
            continue
        return None

    result = []
    for i in range(1, len(arr)):
        result.append(arr[i] - arr[i - 1])
    return result


if __name__ == '__main__':
    result = foo()
    if not result:
        print('NO')
    else:
        print('YES')
        print(*result)
