# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
lista_original = []
for i in range(5):
    cadena = input(f"Introduce la cadena {i+1}: ")
    lista_original.append(cadena)
lista_invertida = []
for i in range(len(lista_original)-1, -1, -1):
    lista_invertida.append(lista_original[i])
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
