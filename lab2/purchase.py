price = int(input())
count = int(input())
paid = int(input())

cost = price * count
change = paid - cost #сдача

print("Стоимость: ", cost)
print("Сдача: ", change)