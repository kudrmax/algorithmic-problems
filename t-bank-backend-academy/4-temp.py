from collections import deque


def get_arr_with_min(arr, w):
    n = len(arr)
    if w == 0 or n == 0:
        return []
    if w == 1:
        return arr

    deq = deque()
    result = []

    # обрабатываем первые w элементов
    for i in range(w):
        while deq and arr[i] <= arr[deq[-1]]:
            deq.pop()
        deq.append(i)
    result.append(arr[deq[0]])  # минимум первого окна

    # обрабатываем оставшиеся элементы
    for i in range(w, n):
        while deq and deq[0] <= i - w:  # удаляем из deq все то, что не входит в окно
            deq.popleft()
        while deq and arr[i] <= arr[deq[-1]]:  # удаляем из deq все то, что больше
            deq.pop()
        deq.append(i)
        result.append(arr[deq[0]])

    return result


res = get_arr_with_min([1, 3, 2, 5, 8, 3], 3)
print(res)
