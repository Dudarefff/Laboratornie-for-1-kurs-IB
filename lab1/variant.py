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
oplata=float(input('внесенная сумма: '))
procent=float(input('введите процент скидки: '))

sum1=value1*kolvo1
sum2=value2*kolvo2
bez_delivery=sum1+sum2

discount=bez_delivery*(procent/100)
with_discount=bez_delivery-discount
sum_total=with_discount+delivery
change=oplata-sum_total

if kolvo1>=0 and kolvo2>=0 and value1>=0 and delivery>=0 and oplata>=sum_total:
    print(order_name,'--',name)
    print('-'*30)
    print('позиция | количество | цена за штуку | стоимость')
    print(f'{poz1} | {kolvo1} | {value1:.2f} | {sum1:.2f}')
    print(f'{poz2} | {kolvo2} | {value2:.2f} | {sum2:.2f}')
    print('-'*30)
    print(f'стоимость без доставки: {bez_delivery:.2f}')
    print(f'скидка: {discount:.2f}')
    print(f'стоимость со скидкой: {with_discount:.2f}')
    print(f'стоимость доставки: {delivery:.2f}')
    print(f'общее количество: {kolvo1+kolvo2}')
    print(f'итого: {sum_total:.2f}')
    print(f'внесенная сумма: {oplata:.2f}')
    print(f'сдача: {change:.2f}')
else:
    print('ошибка')
