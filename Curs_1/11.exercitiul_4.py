
from functools import reduce

lista = [10, 2, 30, 50, 300, 10]

print(sum(lista)/len(lista))

print(reduce(lambda x,y: x+y, lista)/len(lista))

print(reduce(lambda x,y: x+y, lista) / reduce(lambda x,y: x+y, map(lambda x:1, lista))) #GREU