lista1 = []
print(type(lista1))
lista2=[1,"a",True]
lista = [1,2,3,4,5,6]

for num in lista:
    print(num)
    
lista2 = ["a", "b", "c", "d", "e"]
for num, car in zip(lista, lista2):
    print(num, " ", car)
    
print(2 in lista)
print("a" in lista2)
print(7 in lista)

print(lista + [6, 7, 8])
print(lista * 2)
print(lista[0])
print(lista[4])
print(lista[-1])
print(lista[2:4])
print(lista[2:5:2])
print(lista[2:])
print(lista[:3])
print(lista[::-1])
print(len(lista))
print(max(lista))
print(min(lista))
print(sum(lista))

lista = [3,4,2,1,5]
print(sorted(lista))
print(sorted(lista, reverse=True))

tabla = [[1,2,3],[4,5,6],[7,8,9]]
for fila in tabla:
    for elem in fila:    
        print(elem)