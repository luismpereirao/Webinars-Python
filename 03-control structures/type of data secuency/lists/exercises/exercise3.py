#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
lista = []

for nota in range(0,5):
    nota = int(input("Introduce una nota: "))
    lista.append(nota)
    
mean=0
for nota in lista:
    mean += nota

print(lista)
print(f"La nota media es: {mean/len(lista)}")
print(f"La nota mayor es: {max(lista)}")
print(f"La nota menor es: {min(lista)}")