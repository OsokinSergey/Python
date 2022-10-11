inp_list=[2,3,5,6,7,8,9]
inp_len=len(inp_list)
out_list=[]
if(inp_len%2!=0):
    for n in range(0,int((inp_len+1)/2)):
        out_list.append(inp_list[n]*inp_list[inp_len-1-n])
    
else:
    for n in range(0,int(inp_len/2)):
        out_list.append(inp_list[n]*inp_list[inp_len-1-n])
print(f'Входной спискок: {inp_list}\nВыходной список: {out_list}')

    