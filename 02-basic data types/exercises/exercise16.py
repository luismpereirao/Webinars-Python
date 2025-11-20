#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. 
#Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

#Entrada de datos
d = float(input("Ingrese la distancia entre los dos vehículos (km): "))
v1 = float(input("Ingrese la velocidad del vehículo más lento (km/h): "))
v2 = float(input("Ingrese la velocidad del vehículo más rápido (km/h): "))

#Cálculo del tiempo en horas
tiempo_horas = d / (v2 - v1)
#Conversión del tiempo a minutos
tiempo_minutos = tiempo_horas * 60
#Salida de datos
print(f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")
#Suponiendo que v2 > v1

