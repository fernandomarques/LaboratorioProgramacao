import random
import math

lista = random.sample(range(50),10)

print(lista)
print(*lista) # print(lista[0],lista[1], ... , lista[9])

## atenção código avançado para explicar unpacking ##
p1 = [1,2] # idealmente usariamos (1,2) TUPLAS, pesquisem! 
p2 = [3,3]
'''
3           p2
2  p1 
1
0  
   1    2   3
'''
def dist(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2 + (y1-y2)**2)

d = dist(p1[0],p1[1],p2[0],p2[1])
print(d)
d = dist(*p1,*p2)
print(d)

## FIM DO CODIGO AVANÇADO ##