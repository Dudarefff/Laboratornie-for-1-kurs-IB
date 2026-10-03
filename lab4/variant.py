n=int(input('введите количество чисел: '))
cont=0
summ=0
for i in range (n):
    num=int(input('введите число: '))
    if num >=10:
        cont+=1
        summ+=num
print('количество чисел удовлетовряющих условию:', cont)
print('сумма всех чисел: ', summ)
