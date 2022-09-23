days=['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']

# Отвечает за ввод и проверку введенного значения
def input_number():
    try:
        num=int(input('Введите номер дня недели: '))
        if num > 0 and num< 8:
            return num
        else:
            print(f'Введенное значение {num} не входит в диапазон возможных значений')
            return None    
    except:
        print(f'Введенное значение не является числом')
        return None

inp=input_number()
if inp is not None:
    if inp < 6:
        print(f'Нет. {days[inp-1]} является рабочим днем')
    else:
        print(f'Да. {days[inp-1]} является выходным днем')
else:
    print('Повторите ввод')
    



