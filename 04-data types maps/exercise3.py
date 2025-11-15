"""
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

dict_frutas = {'pera':1.87,'manzana':1.43, 'platano':2.10, 'sandia':0.87}

while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in dict_frutas:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio de %f"%{cantidad*dict_frutas[fruta]})
    opcion=input("¿Quieres vender otra fruta? (s/n)")
    while opcion.lower() != "s" and opcion.lower != "n":
        opcion = input("¿Quieres vender otra fruta? (n/s)")
    if opcion.lower() == "n":
        break