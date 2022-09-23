# Все возможноые комбинации трех входных 3!=6
input_value=[[False,False,False],[False,False,True],[False,True,True],[True,True,True],[True,True,False],[True,False,False]]

for i in input_value:
    left_part=not(i[0] or i[1] or i[2])
    right_part= not i[0] and not i[1] and not i[2] 
    print(f'¬({i[0]} ⋁ {i[1]} ⋁ {i[2]})=¬{i[0]} ⋀ ¬{i[1]} ⋀ ¬{i[2]} -> {left_part==right_part}')
    




