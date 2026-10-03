import math

radius = float(input("Введите положительный радиус: "))
if radius > 0:
    circle = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    print(f"Длина окружности: {circle:.2f}")
    print(f"Площадь круга: {area:.2f}")
else:
    print("Радиус должен быть положительным числом")