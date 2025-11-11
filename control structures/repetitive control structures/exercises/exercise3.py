# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

num = int(input("Input a number: "))
cont = 0
sum = 0
mean = 0
while num != 0:
    cont += 1
    sum = sum + num
    mean = sum / cont
    num = int(input("Input a number: "))

print(f"La suma es: {sum} y la media es: {mean}")