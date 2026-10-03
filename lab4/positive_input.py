cont=0
while True:
    n=int(input('введите число '))
    if n>0:
        break
    else:
        cont+=1
        print('пробуй еще раз ')
print('квадрат числа ',n**2)
print('количество отклоненных попыток ',cont)
