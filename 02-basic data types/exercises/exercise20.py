# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

# Entrada de datos
monedas_2_euros = int(input("Ingrese el número de monedas de 2 euros: "))
monedas_1_euro = int(input("Ingrese el número de monedas de 1 euro: "))
monedas_50_centimos = int(input("Ingrese el número de monedas de 50 céntimos: "))
monedas_20_centimos = int(input("Ingrese el número de monedas de 20 céntimos: "))
monedas_10_centimos = int(input("Ingrese el número de monedas de 10 céntimos: "))
# Cálculo del total en euros y céntimos
total_euros = (monedas_2_euros * 2) + (monedas_1_euro * 1) + (monedas_50_centimos * 0.5) + (monedas_20_centimos * 0.2) + (monedas_10_centimos * 0.1)
total_centimos = int(total_euros * 100)  # Convertir a céntimos para evitar problemas de precisión
# Salida de datos
euros = total_centimos // 100
centimos = total_centimos % 100
print(f"El total de dinero es: {euros} euros y {centimos} céntimos.")
