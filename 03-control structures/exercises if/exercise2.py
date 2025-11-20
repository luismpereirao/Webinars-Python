# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num1 = int(input("Introduce un número: "))

if num1 > 0:
    print(f"El número {num1} es positivo")
elif num1 < 0:
    print(f"El número {num1} es negativo")
else:
    print(f"El número {num1} es 0")