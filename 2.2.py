a = int(input("введите номер места "))
if a % 2 == 0 and a <= 36:
    print('Вверхнее место в купе')
elif a > 54:
    print('Ошибка')
elif a % 2 != 0 and a <= 35:
    print('Нижннее место в купе')
elif a % 2 == 0 and a > 36:
    print('Вверхнее боковое место')
else:
    print('Нижнее боковое место')