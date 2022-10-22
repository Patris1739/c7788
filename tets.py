while True:
    p = int(input('Введите превое число:'))
    p1 = int(input('Введите второе число:'))

    action = int(input('1.+ \ 2.- \ 3.* \ 4./ \Выберите действие:'))

    if action == 1:
        result = p + p1
        p = 'Сумма'
        t = p

    if action == 2:
        result = p - p1
        m = 'Вычитания'
        t = m

    if action == 3:
        result = p * p1
        u = 'Умножение'
        t = u

    if action == 4:
        result = float(p / p1)
        d = 'Деление'
        t = d
    print('Ответ:', t, ' = ', result)

    q = input("Начать заново? ")
    if q == 'нет':
        break





