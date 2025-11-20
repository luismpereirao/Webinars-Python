"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas
"""
import math

print("--- CÁLCULO DE POSICIÓN DE CIRCUNFERENCIAS ---")
# Usamos float porque las coordenadas y radios pueden tener decimales
x1 = float(input("Introduce el centro x1: "))
y1 = float(input("Introduce el centro y1: "))
r1 = float(input("Introduce el radio r1: "))

x2 = float(input("Introduce el centro x2: "))
y2 = float(input("Introduce el centro y2: "))
r2 = float(input("Introduce el radio r2: "))

# 1. Calculamos la distancia entre los centros (Teorema de Pitágoras)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 2. Calculamos referencias para comparar
suma_radios = r1 + r2
diferencia_radios = abs(r1 - r2)  # Usamos valor absoluto para evitar negativos

print(f"\nLa distancia entre centros es: {distancia:.2f}")

# 3. Clasificamos según la lógica geométrica
if distancia == 0:
    print("Clasificación: CONCÉNTRICAS")
    
elif distancia > suma_radios:
    print("Clasificación: EXTERIORES")
    
elif distancia == suma_radios:
    print("Clasificación: TANGENTES EXTERIORES")
    
elif distancia < suma_radios and distancia > diferencia_radios:
    print("Clasificación: SECANTES")
    
elif distancia == diferencia_radios:
    print("Clasificación: TANGENTES INTERIORES")
    
elif distancia < diferencia_radios:
    print("Clasificación: INTERIORES")

