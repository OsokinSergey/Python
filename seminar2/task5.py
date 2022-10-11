#Алгоритм перемешивает входный список произвольным образом
from random import randrange

input_values=['Торопыжка','был','голодный','проглотил','утюг','холодный']
output_values=[]
for i in range(0,len(input_values)):
       output_values.insert(randrange(len(input_values)-1),input_values[i])
print(input_values)    
print(output_values)