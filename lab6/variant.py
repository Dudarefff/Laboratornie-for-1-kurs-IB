text = input("Введите целые числа через пробел: ")
if text.strip():
    numbers = [int(x) for x in text.split()]
else:
    numbers = []
filtered_numbers = []
for num in numbers:
    if num >= 10:
        filtered_numbers.append(num)
count = len(filtered_numbers)
total_sum = sum(filtered_numbers)
sorted_copy = sorted(filtered_numbers)

print(f"Исходный порядок: {filtered_numbers}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Отсортированная копия: {sorted_copy}")