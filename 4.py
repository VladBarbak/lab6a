"""
4. Робота світлофора для водіїв запрограмована таким чином: на початку кожної
години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
момент.
Барбак Владислав 1 курс група 122в
"""
while True:
    while True:
        try:
            t=int(input('Input time '))
            break
        except ValueError:
            print('Error!')
    while t<0 or t>60:
        print('In 1 hour there are not so many minutes')
        t = int(input('Input time '))
    a=t%6
    if 1<=a<=3:
        print('Glowing green')
    elif a==4:
        print('Glowing yellow')
    else:
        print('Glowing red')
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break