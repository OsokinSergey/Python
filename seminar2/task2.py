def input_number():
    try:
        #Проверяем, что введено именно целое число
        num=int(input('Введите число: '))
        return num
        
    except:
        print(f'Введенное значение не является числом')
        return None

inp=input_number()
fact=1
factorial=[1]
for n in range(2,inp+1):
    fact*=n
    factorial.append(fact)
print(factorial)