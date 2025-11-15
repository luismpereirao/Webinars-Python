# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
num = int(input("input a number:"))
for var in range (0,11):
    print(f"{num} x {var} = {num*var}")