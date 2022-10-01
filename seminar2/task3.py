def input_number():
    try:
        #Проверяем, что введено именно целое число
        num=int(input('Введите число: '))
        return num
        
    except:
        print(f'Введенное значение не является числом')
        return None

inp=input_number()
sum=0
series=[]
for n in range(1,inp+1):
    val=(1+1/n)**n
    sum+=val
    series.append(round(val,4))
    
print(f'Для n={inp}:\n{series}\nСумма чисел = {round(sum,4)}')