"""
2. Є описи:
class converter (Enum):
USD = 1
EUR = 2
CZK = 3
PLN = 4
x = float (input ( 'amount of money:'))
p = converter [input ( 'currency:')]
Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
цієї ж суми в гривнях.
Барбак Владислав 1 курс група 122в
"""
from enum import Enum
class converter (Enum):
    USD=1
    EUR=2
    CZK=3
    PLN=4
while True:
    while True:
        try:
            p=converter[input('Currency: ')]
            break
        except KeyError:
            print('Please enter a currency')
    while True:
        try:
            x=float(input('Amount of money: '))
            break
        except ValueError:
            print('Enter the amount of money')
    t=0
    if p==converter.USD:
        t=x*24.6
        print(f'The amount {t} UAH in {x} USD')
    elif p==converter.EUR:
        t=x*26.9
        print(f'The amount {t} UAH in {x} EUR')
    elif p==converter.CZK:
        t=x*1.1
        print(f'The amount {t} UAH in {x} CZK')
    elif p==converter.PLN:
        t=x*6.25
        print(f'The amount {t} UAH in {x} PLN')
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break