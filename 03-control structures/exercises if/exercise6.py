# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cad = input("Introduce una cadena de texto: ")
if cad[0].isupper():
    print("La primera empieza por mayuscula.")
elif cad[0].islower():
    print("La primera no es mayuscula")
else:
    print("El primer carácter no es una letra (es un número o símbolo).")