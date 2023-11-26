per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада = '))
deposit = {key: (value * money) / 100 for key, value in per_cent.items()}
deposit = list(map(int, deposit.values()))
print('Накопленные средства за год =', deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))