x=float(input())
z=input('введите знак операции: ')
y=float(input())
if z=='+':
    print(f'{x+y:.2}')
elif z=='-':
    print(f'{x-y:.2}')
elif z=='*':
    print(f'{x*y:.2}')
elif z=='/':
    if y==0:
        print('деление на 0 запрещено')
    else:
        print(f'{x/y:.2}')
else:
    print('неизвестная операция')