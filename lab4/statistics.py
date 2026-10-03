n=int(input('введите число n>=1 '))
summ=0
cont=0
first=int(input('введите число '))
maxi=first
summ+=first
if first>0:
    cont+=1
for i in range(2,n+1):
    num=int(input('введите число ',))
    summ+=num
    if num>0:
        cont+=1
    if num>maxi:
        maxi=num
print('сумма', summ)
print('количество положительных',cont)
print('максимум',maxi)