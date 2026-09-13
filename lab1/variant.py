'''вариант 6'''

order_name=input('введите название заказа: ')
name=input('введите ваше имя: ')

poz1=input('введите название первой позиции: ')
kolvo1=int(input('сколько хотите купить?'))
value1=float(input('сколько стоит одна штука?'))

poz2=input('введите название второй позиции: ')
kolvo2=int(input('сколько хотите купить?'))
value2=float(input('сколько стоит одна штука?'))

delivery=int(input('сколько стоит доставка?'))
oplata=int(input('внесенная сумма: '))

sum1=value1*kolvo1
sum2=value2*kolvo2
sum_total=sum1+sum2+delivery
bez_delivery=sum1+sum2
change=oplata-sum_total

if kolvo1>=0 and kolvo2>=0 and value1>=0 and delivery>=0 and oplata>=sum_total:
    print(order_name,'--',name)
    print('-'*30)
    print('позиция | количество | цена за штуку | стоимость')
    print(f'{poz1} | {kolvo1} | {value1:.2f} | {sum1:.2f}')
    print(f'{poz2} | {kolvo2} | {value2:.2f} | {sum2:.2f}')
    print('-'*30)
    print(f'стоимость без доставки: {bez_delivery:.2f}')
    print(f'стоимость доставки: {delivery:.2f}')
    print(f'общее количество: {kolvo1+kolvo2}')
    print(f'итого: {sum_total:.2f}')
    print(f'внесенная сумма: {oplata:.2f}')
    print(f'сдача: {change:.2f}')
else:
    print('ошибка')
