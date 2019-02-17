## Change Return Program 
# The user enters a cost and then the amount of money given.
# The program will figure out the change using the less paper and coins as possible
##
import unittest

def change_return_calculator(cost, money_given):
    if money_given < cost:
        print('Você deu menos do que o produto custa.')
        return False

    if money_given == cost:
        return True

    change = money_given - cost
    used_money = {'100': 0, '50': 0, '25': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.5': 0, '0.25': 0, '0.1': 0, '0.05': 0, '0.01': 0}

    for value in list(used_money.keys()):
        while change - float(value) >= 0:
            change -= float(value)
            used_money[value] += 1

    print('Troco:')
    for value in list(used_money.keys()):
        if used_money[value]:
            print(f'R${float(value):5.2f}: {used_money[value]}')

    return True

if change_return_calculator(float(input('Qual o valor do produto? ')), float(input('Quanto você deseja pagar? '))):
    print('\nPRODUTO COMPRADO!')
else:
    print('\nPRODUTO NÃO COMPRADO.')