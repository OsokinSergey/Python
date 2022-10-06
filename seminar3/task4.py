#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def input_number():
    try:
        #Проверяем, что введено именно вещественное число
        num=int(input('Ведите число: '))
        return num
        
    except:
        print(f'Введенное значение не является числом')
        return None


number= input_number()
#Можно использовать встроенную функцию bin, но мы не ищем легких путей.
b=''
while number > 0:
    b=str(number%2)+b
    number=number//2
print(b)