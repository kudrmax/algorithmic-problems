from typing import List


def minimize_deviation(n, k, a):
    # Сортируем список a
    sorted_a = sorted(a)

    # Получаем все уникальные значения в a
    unique_a = sorted(set(a))

    # Если количество уникальных значений уже меньше или равно k, то мы можем использовать их все
    if len(unique_a) <= k:
        return a

    # Находим k значений, которые будут использоваться в последовательности b
    # Берем середину всех возможных вариантов уникальных значений
    best_k_values = unique_a[:k]

    # Создаем итоговую последовательность b
    b = []

    for ai in a:
        # Подбираем ближайшее значение из best_k_values
        closest_value = min(best_k_values, key=lambda x: abs(x - ai))
        b.append(closest_value)

    return b


# Чтение входных данных
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Получаем результат
b = minimize_deviation(n, k, a)

# Выводим результат
print(" ".join(map(str, b)))

def get_delta_between_arrs(a_arr: List[int], b_arr: List[int], d: int = 2):
    return sum([abs(a - b) ** d for a, b in zip(a_arr, b_arr)])

delta = get_delta_between_arrs(a, b)
print(f'{delta = }')