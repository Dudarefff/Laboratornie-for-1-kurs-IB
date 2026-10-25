text = input("Введите целые числа через пробел: ")
if not text.strip():
    print("Нет данных")
else:
    numbers = [int(x) for x in text.split()]
    max_val = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == max_val:
            positions.append(index)    
    print(f"Индексы максимума: {positions}")