num=int(input("Введите целое число больше 1: "))
if num>1:
    position=[0,8,5,3]
    values=[]
    for i in range(-num,num+1):
        values.append(i)
    power=values[position[0]]
    max_ind=len(values)    
    for i in range(1,len(position)):
        if position[i]<max_ind:
            power*=values[position[i]]
    print(values)        
    print(power)
else:
    print("Введенное число не удовлетворяет условию")
