from functions import sum_digits, average, normalize_text, select_numbers

def main():
    print("--- Демонстрация функций ---")
    # 1.sum_digits
    num_input = int(input("Введите целое число: "))
    print(f"Сумма цифр: {sum_digits(num_input)}")
    # 2.average
    nums_str = input("Введите строку чисел через пробел: ")
    if nums_str.strip():
        nums_list = [int(x) for x in nums_str.split()]
        avg = average(nums_list)
        if avg is None:
            print("Нет данных")
        else:
            print(f"Среднее: {avg:.2f}")
    else:
        print("Нет данных")
    # 3.normalize_text
    text_input = input("Введите произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(text_input)}'")
    # 4.Вариант 10
    print("\n--- Индивидуальный вариант №10 ---")
    var_nums_str = input("Введите числа для фильтрации: ")
    threshold_input = int(input("Введите порог: "))
    
    if var_nums_str.strip():
        var_nums = [int(x) for x in var_nums_str.split()]
        filtered = select_numbers(var_nums, threshold_input)
        print(f"Результат: {filtered}")
    else:
        print("Результат: []")

if __name__ == "__main__":
    main()