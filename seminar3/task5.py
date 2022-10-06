def input_number():
    try:
        #Проверяем, что введено именно вещественное число
        num=int(input('Ведите число: '))
        return num
        
    except:
        print(f'Введенное значение не является числом')
        return None

number= input_number()

flag=-1
out_list=[1,0,1]
for i in range(2,number+1):
    ind=len(out_list)-1
    fn=out_list[ind]+out_list[ind-1]
    out_list.append(fn)
    out_list.insert(0,fn*flag)
    flag*=-1


print(f'Для k =  {number} список чисел негафибоначчи и чисел фибоначи :\n {out_list}')