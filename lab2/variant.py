total = int(input())      
capacity = int(input())   

full = total // capacity         
ost = total % capacity      
if total == 0:
    minimum = 0
else:
    minimum = (total + capacity - 1) // capacity  

print("Полных: ", full)
print('Остаток: ', ost)
print('Всего: ', minimum)