

lista = [10, 2, 30, 50, 300, 10]

def mare_5(element):
    return element > 5
    
print(list(filter(mare_5, lista)))

print(list(filter(lambda x: x > 5, lista)))

print([element for element in lista if element > 5])