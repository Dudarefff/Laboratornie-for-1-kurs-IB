year = int(input("Введите год от 1 до 9999: "))
if 1 <= year <= 9999:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Да")
    else:
        print("Нет")
else:
    print("Год должен быть от 1 до 9999")