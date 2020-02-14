"""
3. Є описи:
class month (Enum):
January = 1
February = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9
October = 10
November = 11
December = 12
class season (Enum):
Winter = 1
Spring = 2
Summer = 3
Autumn = 4
s = month [input ( 'month:')]
За s-назвою місяця визначити відповідну пору року.
Барбак Владислав 1 курс група 122в
"""
from enum import Enum
class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    while True:
        try:
            s=int(input('month:'))
            break
        except ValueError:
            print('Input number month')
    if 1<=s<=12:
        if s==month.December.value or s==month.January.value or s==month.February.value:
            print(f'{season.Winter.name}')
        elif s==month.March.value or s==month.April.value or s==month.May.value:
            print(f'{season.Spring.name}')
        elif s==month.June.value or s==month.July.value or s==month.August.value:
            print(f'{season.Summer.name}')
        elif s==month.September.value or s==month.October.value or s==month.November.value:
            print(f'{season.Autumn.name}')
    print('Has no such month')
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break