# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
import math
x1 = int(input("Introduce un número:"))
y1 = int(input("Introduce un número:"))
x2 = int(input("Introduce un número:"))
y2 = int(input("Introduce un número:"))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre el punto ({x1}, {y1}) y el punto ({x2}, {y2}) es: {distance}")