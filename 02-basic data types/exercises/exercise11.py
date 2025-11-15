#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))
diferencia = num1-num2
distance = abs(diferencia)

print(f"La distancia entre los valores es de: {distance}")

