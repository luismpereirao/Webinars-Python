# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

num = input("Introduce un número de dos cifras: ")

# Invertir el número usando slicing
num_invertido = num[::-1]

print(f"El número invertido es: {num_invertido}")
