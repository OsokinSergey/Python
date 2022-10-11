inp_list=[1.1, 1.9, 3.1, 5, 10]
min=round(inp_list[0]-int(inp_list[0]),2)
max=round(inp_list[0]-int(inp_list[0]),2)
for n in inp_list:
    val=round(n-int(n),2)
    
    if val < min and val !=0:
        min=val
    if val > max:
        max=val
    
print(f'Входной список: {inp_list}\nРезультат: {max-min}')