sub1=input('Введите название первого предмета: ')
amt_sub1=int(input('количество занятий в неделю: '))
sub2=input('Введите название второго предмета: ')
amt_sub2=int(input('количество занятий в неделю: '))
dlina=int(input('длительность одного занятия в минутах: '))
d_time=60*(int(input('доступное время на неделю в часах: ')))
vrem1=amt_sub1*dlina
vrem2=amt_sub2*dlina
vrem_all=vrem1+vrem2
ostatok=round((d_time-vrem_all)/60,2)
if d_time>(vrem1 + vrem2) and amt_sub1>0 and amt_sub2>0 and dlina>0:
    print('----------------------')
    print(sub1,':',vrem1,'минут в неделю')
    print(sub2,':',vrem2,'минут в неделю')
    print('общая нагрузка в минутах: ', vrem_all)
    print('общая нагрузка в часах: ', round(vrem_all/60,2))
    print('остаток свободного времени в часах: ', ostatok)
    print('общая нагрузка за 4 недели: ', vrem_all*4,'минут')
else:
    print('ошибка!')
    

