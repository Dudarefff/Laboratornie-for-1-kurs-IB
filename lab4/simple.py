n = int(input("Введите целое число >= 2: "))
if n < 2:
    print("Число должно быть >= 2")
else:
    prime = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            prime = False
            break
        divisor += 1
        
    if prime:
        print("Простое")
    else:
        print("Составное")