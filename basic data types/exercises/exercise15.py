# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
a = input("Introduce un número:")
b = input("Introduce otro número:")

aux = a
a=b
b=aux

print(f"El nuevo valor de a: {a} y el nuevo valor de b: {b}")
    