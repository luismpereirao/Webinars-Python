# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num2 != 0:
    print(f"La división de {num1} / {num2} es: {num1/num2}")
else:
    print("El divisor es 0.")