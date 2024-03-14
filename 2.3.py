year = int(input("Введите год: "))
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print(f"Год {year} - високосный")
else:
    print("Это год не високосный")

# 4
color1 = input("Введите первый основной цвет (красный, синий или желтый): ")
color2 = input("Введите второй основной цвет (красный, синий или желтый): ")
if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("Фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    print("Оранжевый")
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    print("Зеленый")
else:
    print("Ошибка! Введите названия только красного, синего или желтого.")