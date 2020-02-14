"""
1. Є описи:
days = range (1, 32)
months = range (1, 13)
years = range (1901, 2020)
d, m, y = int (input ( 'day:')), \
int (input ( 'month:')), \
int (input ( 'year:'))
За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
наявність високосних років.
Барбак Владислав 1 курс група 122в
"""
days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
    while True:
        try:
            d, m, y = int(input('Day: ')), \
                      int(input('Month:')), \
                      int(input('Year:'))
            break
        except ValueError:
            print('Enter correct number')
    popered = 0
    if d in days and m in months and y in years:
        if y % 4 == 0:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                index = 1
            elif m == 4 or m == 6 or m == 9 or m == 11:
                index = 2
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                index = 3

            while d < 1 or (d > 29 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
                d = int(input("input d!:"))

            if (d == 29 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
                sled = 1
            else:
                sled = d + 1
            if (d == 1 and index == 1) or (d == 1 and index == 2):
                popered = 31
            elif (m == 3 and d == 1):
                popered = 29
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                popered == 30
            else:
                popered = d - 1

            print('The previous day-',popered, ".",'The next day-',sled)

        else:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                index = 1
            elif m == 4 or m == 6 or m == 9 or m == 11:
                index = 2
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                index = 3

            while d < 1 or (d > 28 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
                d = int(input("input d!:"))

            if (d == 28 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
                sled = 1
            else:
                sled = d + 1
            if (d == 1 and index == 1) or (d == 1 and index == 2):
                popered = 31
            elif (m == 3 and d == 1):
                popered = 28
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                popered == 30
            else:
                popered = d - 1

            print('The previous day-',popered, ".",'The next day-',sled)
    print('Error, some of the input is incorrect')
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break