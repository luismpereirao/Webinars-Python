# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

# Entrada de datos
respuestas_correctas = int(input("Ingrese el número de respuestas correctas: "))
respuestas_incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
respuestas_en_blanco = int(input("Ingrese el número de respuestas en blanco: "))
# Cálculo de la nota final
nota_final = (respuestas_correctas * 5) + (respuestas_incorrectas * -1) + (respuestas_en_blanco * 0)
# Salida de datos
print(f"La nota final del estudiante es: {nota_final} puntos.")