# with open('input.txt') as file:
#     lines = file.readlines()
# n, k, a, m = list(map(int, lines[0].split()))

n, k, a, m = list(map(int, input().split()))


def get_new_seed(e):
    return (a * e + 11) % m


def get_new_coin(seed):
    return (abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8


def get_new_coin_and_seed(seed):
    seed = get_new_seed(seed)
    coin = get_new_coin(seed)
    return coin, seed


candy_counter = 0  # количество конфет на руках
coin_counter = 0  # количество монет, достанных из кармана
min_money = k * 3  # количество денег в автомате при котором автомат выдаст конфеты
money_in_machine = 0  # количество денег в автомате

seed = 0
while candy_counter < n:
    coin, seed = get_new_coin_and_seed(seed)  # получаем монеты
    money_in_machine += coin  # закидываем монету в автомат
    coin_counter += 1
    if money_in_machine > min_money:
        candy_counter += money_in_machine // 3  # количество полученных конфет
        money_in_machine = money_in_machine % 3  # остаток монет в матомате
    # print(f'{coin = }, {money_in_machine = }, {candy_counter = }')
print(coin_counter)
