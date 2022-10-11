def input_number(coor):
    try:
        num=int(input(f'Введите координату {coor}: '))
        if num !=0:
            return num
        else:
            print(f'Введенное значение не должно быть 0')
            return None    
    except:
        print(f'Введенное значение не является числом')
        return None

x=input_number('X')
y=input_number('Y')

def quarter(x,y):
    if x>0 and y>0:
        return 1
    if x<0 and y>0:
        return 2
    if x<0 and y<0:
        return 3
    if x>0 and y<0:
        return 4

q=quarter(x,y)
print(f'x = {x}, y = {y} -> {q}')
