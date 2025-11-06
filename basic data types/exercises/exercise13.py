"""
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
"""

import math


num = int(input("Introduce un número para calcular sus raíces cuadrada y cúbica:"))

raiz_cuadrada = math.pow(num, 2)

print(f"La raiz cuadrada de {num} es: {raiz_cuadrada}")

raiz_cubica = math.pow(num, 3)
print(f"La raiz cuadrada de {num} es: {raiz_cubica}")
