def input_number():
    try:
        #Проверяем, что введено именно вещественное число
        num=float(input('Введите вещественное число: '))
        return str(num)
        
    except:
        print(f'Введенное значение не является числом')
        return None

inp=input_number()
result=0
for x in inp:
    if x.isdigit():
        result+=int(x)
print(result)
