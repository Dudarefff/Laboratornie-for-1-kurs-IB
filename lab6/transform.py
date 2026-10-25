text = input("Введите целые числа через пробел: ")
if text.strip():
    numbers = [int(x) for x in text.split()]
    new_numbers = []
    for num in numbers:
        new_numbers.append(abs(num))
    print(f"Исходный список: {numbers}")
    print(f"Новый список: {new_numbers}")
else:
    print("Исходный список: []")
    print("Новый список: []")