text = input("Введите целые числа через пробел: ")
if not text.strip():
    print("Нет данных")
else:
    numbers = [int(x) for x in text.split()]
    cont = len(numbers)
    total_sum = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    aver = total_sum / cont
    
    print(f"Количество: {cont}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {aver:.2f}")