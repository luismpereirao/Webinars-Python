"""
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

dict_frutas = {'pera': 1.87, 'manzana': 1.43, 'platano': 2.10, 'sandia': 0.87}

while True:
    fruta = input("Dime la fruta que has vendido: ")

    if fruta.lower() not in dict_frutas:
        print("La fruta no existe.")
    else:
        try:
            cantidad = float(input("Dime la cantidad de frutas que has vendido: "))
            precio_final = cantidad * dict_frutas[fruta.lower()]
            print(f"El precio es {precio_final:.2f} €")
        except ValueError:
            print("Cantidad no válida.")

    opcion = input("¿Quieres vender otra fruta? (s/n): ").lower()

    # Validación de opción
    while opcion not in ("s", "n"):
        opcion = input("Opción no válida. Escribe 's' o 'n': ").lower()

    if opcion == "n":
        print("Saliendo del programa...")
        break
