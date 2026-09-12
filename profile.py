surname = input('Введите фамилию:')
name = input('Введите имя:')
gr = input('Введите группу:')
city = input('Введите город:')
age = int(input('Возраст в полных годах:'))
z = input('Введите любимый предмет:')
time = float(input('Введите кол-во часов подготовки в неделю'))
t= time/7
t4=time*4
if 1<age<120 and time>0:
    print('---------------------------')
    print('полное имя: ', surname, name)
    print('возраст через 4 года:', age+4)
    print("среднее время подготовки в день:", round(t,2), "часов")
    print("среднее время подготовки за 4 недели:", round(t4,2), "часов")
    print('полная карточка:')
    print(surname,name,gr,city,age,z,time)
else:
    print('ошибка')
