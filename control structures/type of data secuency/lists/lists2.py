lista1 = [1,2,3]
lista1[1]=100
print(lista1)
del lista1[1]
print(lista1)
lista1.append(5)
print(lista1)
a=4
b=a
print(b)
a=6
print(b)
lista2 = lista1
print(lista2)
lista1.append(100)
print(lista1)
print(lista2)
lista2 = lista1[:]
print(lista2)
lista1.append(200)
print(lista1)
print(lista2)